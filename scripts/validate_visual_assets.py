#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the concrete aiaiaiai canonical visual-asset publication."""

from __future__ import annotations

import hashlib
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from validate_manifest import load_schema, load_yaml_mapping, schema_errors

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "modules" / "identity" / "visual-assets.yaml"
IDENTITY_PATH = ROOT / "modules" / "identity" / "identity.yaml"
SCHEMA_PATH = ROOT / "schema" / "visual-assets.schema.json"

REQUIRED_ASSETS = {
    "aiaiaiai-compact-emblem": (
        "image/svg+xml",
        Path("assets/visual/aiaiaiai/compact-emblem.svg"),
    ),
    "aiaiaiai-compact-emblem-png-1024": (
        "image/png",
        Path("assets/visual/aiaiaiai/exports/compact-emblem-1024.png"),
    ),
}
MEDIA_SUFFIXES = {
    "image/svg+xml": ".svg",
    "image/png": ".png",
    "image/webp": ".webp",
}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_path(relative_path: str) -> Path | None:
    root = ROOT.resolve()
    candidate = (ROOT / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        return None
    return candidate


def validate_svg(path: Path, prefix: str) -> list[str]:
    errors: list[str] = []
    try:
        document = ET.parse(path)
    except (ET.ParseError, OSError) as error:
        return [f"{prefix}: invalid SVG: {error}"]

    root = document.getroot()
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append(f"{prefix}: root element must be SVG")
    if root.attrib.get("viewBox") != "0 0 64 64":
        errors.append(
            f"{prefix}: canonical compact emblem must use viewBox '0 0 64 64'"
        )
    return errors


def png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as handle:
            header = handle.read(24)
    except OSError:
        return None

    if len(header) != 24 or header[:8] != PNG_SIGNATURE or header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


def validate_png(path: Path, prefix: str) -> list[str]:
    dimensions = png_dimensions(path)
    if dimensions is None:
        return [f"{prefix}: invalid PNG signature or IHDR"]
    if dimensions != (1024, 1024):
        return [
            f"{prefix}: provider export must be 1024x1024, "
            f"got {dimensions[0]}x{dimensions[1]}"
        ]
    return []


def validate_descriptor(
    descriptor: dict[str, Any],
    index: int,
    seen_refs: set[str],
) -> list[str]:
    errors: list[str] = []
    prefix = f"assets[{index}]"
    asset_ref = descriptor.get("ref")
    media_type = descriptor.get("media_type")
    relative_path = descriptor.get("resource_path")
    integrity = descriptor.get("integrity")

    if isinstance(asset_ref, str):
        if asset_ref in seen_refs:
            errors.append(f"{prefix}.ref: duplicate asset ref {asset_ref!r}")
        seen_refs.add(asset_ref)

    if isinstance(relative_path, str):
        path = safe_path(relative_path)
        if path is None:
            errors.append(f"{prefix}.resource_path: path escapes publication root")
            return errors
        if not path.is_file():
            errors.append(
                f"{prefix}.resource_path: file does not exist: {relative_path}"
            )
            return errors

        expected_suffix = MEDIA_SUFFIXES.get(media_type)
        if expected_suffix is not None and path.suffix.lower() != expected_suffix:
            errors.append(
                f"{prefix}.media_type: {media_type!r} does not match {path.suffix!r}"
            )

        expected_digest = (
            integrity.get("digest") if isinstance(integrity, dict) else None
        )
        actual_digest = sha256(path)
        if expected_digest != actual_digest:
            errors.append(
                f"{prefix}.integrity.digest: expected {expected_digest!r}, "
                f"actual {actual_digest!r}"
            )

        if media_type == "image/svg+xml":
            errors.extend(validate_svg(path, prefix))
        elif media_type == "image/png":
            errors.extend(validate_png(path, prefix))

    return errors


def validate_required_assets(catalog: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    by_ref = {
        descriptor.get("ref"): descriptor
        for descriptor in catalog.get("assets", [])
        if isinstance(descriptor, dict) and isinstance(descriptor.get("ref"), str)
    }
    for asset_ref, (media_type, path) in REQUIRED_ASSETS.items():
        descriptor = by_ref.get(asset_ref)
        if descriptor is None:
            errors.append(f"required canonical asset is missing: {asset_ref}")
            continue
        if descriptor.get("media_type") != media_type:
            errors.append(
                f"{asset_ref}: expected media type {media_type!r}, "
                f"got {descriptor.get('media_type')!r}"
            )
        if descriptor.get("resource_path") != path.as_posix():
            errors.append(
                f"{asset_ref}: expected resource path {path.as_posix()!r}, "
                f"got {descriptor.get('resource_path')!r}"
            )
    return errors


def validate_identity_binding(catalog: dict[str, Any]) -> list[str]:
    """Validate a primary-mark binding if/when the concrete identity authors one."""
    identity_resource = load_yaml_mapping(IDENTITY_PATH)
    identity = identity_resource.get("identity")
    if not isinstance(identity, dict):
        return ["identity resource is missing the embedded identity mapping"]

    visual_identity = identity.get("visual_identity")
    if visual_identity is None:
        return []
    if not isinstance(visual_identity, dict):
        return ["identity.visual_identity must be a mapping"]

    primary_mark = visual_identity.get("primary_mark")
    if primary_mark is None:
        return []
    if not isinstance(primary_mark, dict):
        return ["identity.visual_identity.primary_mark must be a mapping"]

    asset_ref = primary_mark.get("asset_ref")
    matches = [
        descriptor
        for descriptor in catalog.get("assets", [])
        if isinstance(descriptor, dict) and descriptor.get("ref") == asset_ref
    ]
    if len(matches) != 1:
        return [
            "identity.visual_identity.primary_mark.asset_ref must resolve exactly "
            f"once; {asset_ref!r} resolved {len(matches)} times"
        ]

    descriptor = matches[0]
    path = safe_path(descriptor["resource_path"])
    if path is None or not path.is_file():
        return [f"primary mark {asset_ref!r} does not resolve to an existing file"]
    if sha256(path) != descriptor["integrity"]["digest"]:
        return [f"primary mark {asset_ref!r} failed SHA-256 integrity validation"]
    return []


def main() -> int:
    errors: list[str] = []
    catalog = load_yaml_mapping(CATALOG_PATH)
    schema = load_schema(SCHEMA_PATH)
    errors.extend(
        f"catalog{error[1:]}"
        for error in schema_errors(Draft202012Validator(schema), catalog)
    )

    if not errors:
        seen_refs: set[str] = set()
        for index, descriptor in enumerate(catalog["assets"]):
            errors.extend(validate_descriptor(descriptor, index, seen_refs))
        errors.extend(validate_required_assets(catalog))
        errors.extend(validate_identity_binding(catalog))

    if errors:
        print("canonical visual asset validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("canonical aiaiaiai visual assets are valid")
    for descriptor in catalog["assets"]:
        path = safe_path(descriptor["resource_path"])
        assert path is not None
        print(
            f"- {descriptor['ref']}: {descriptor['media_type']} "
            f"sha256={sha256(path)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
