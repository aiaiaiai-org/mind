#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the exact Mind Protocol release contracts consumed by this canary."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from typing import Any

from validate_manifest import load_json_mapping, load_yaml_mapping

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "protocol.lock.yaml"
MANIFEST_PATH = ROOT / "manifest.yaml"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    lock = load_yaml_mapping(LOCK_PATH)
    manifest = load_yaml_mapping(MANIFEST_PATH)

    protocol = lock.get("protocol")
    if protocol != {"id": "mind", "version": "0.9.0"}:
        errors.append("protocol.lock.yaml must pin Mind Protocol 0.9.0 exactly")
    if manifest.get("protocol") != protocol:
        errors.append("manifest protocol must match protocol.lock.yaml exactly")

    source = lock.get("source")
    if source != {
        "repository": "0x0sky/mind",
        "tag": "v0.9.0",
        "floating_branch": "forbidden",
    }:
        errors.append("protocol source must be the immutable 0x0sky/mind v0.9.0 release tag")

    descriptor = lock.get("protocol_descriptor")
    if not isinstance(descriptor, dict):
        errors.append("protocol_descriptor lock is missing")
    else:
        path = ROOT / str(descriptor.get("path", ""))
        expected = descriptor.get("git_blob_sha1")
        if not path.is_file():
            errors.append("locked protocol descriptor is missing")
        elif git_blob_sha1(path) != expected:
            errors.append("protocol.yaml does not match the locked v0.9.0 release blob")

    contracts = lock.get("vendored_contracts")
    if not isinstance(contracts, dict) or not contracts:
        errors.append("vendored_contracts lock is missing")
        return errors

    seen_ids: set[str] = set()
    for relative_path, descriptor in contracts.items():
        if not isinstance(relative_path, str) or not isinstance(descriptor, dict):
            errors.append("vendored_contracts entries must be path -> descriptor mappings")
            continue
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"locked contract is missing: {relative_path}")
            continue
        expected_sha = descriptor.get("git_blob_sha1")
        if git_blob_sha1(path) != expected_sha:
            errors.append(f"contract drift from v0.9.0 release: {relative_path}")
        schema = load_json_mapping(path)
        schema_id = descriptor.get("schema_id")
        if schema.get("$id") != schema_id:
            errors.append(f"schema id mismatch for {relative_path}")
        if not isinstance(schema_id, str) or schema_id in seen_ids:
            errors.append(f"duplicate or invalid locked schema id for {relative_path}")
        else:
            seen_ids.add(schema_id)

    context_versioning = lock.get("context_versioning")
    if context_versioning != {
        "independent_from_protocol": True,
        "protocol_tags_in_this_repository": "forbidden",
    }:
        errors.append("context/protocol versioning boundary is not canonical")

    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, TypeError) as error:
        print(f"protocol release lock validation failed:\n- {error}", file=sys.stderr)
        return 1

    if errors:
        print("protocol release lock validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Mind Protocol v0.9.0 release contracts are pinned exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
