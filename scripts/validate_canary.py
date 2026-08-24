#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate aiaiaiai organization canary invariants for Mind Protocol 0.9."""

from __future__ import annotations

import sys
from pathlib import Path

from validate_manifest import load_yaml_mapping

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.yaml"
MACHINE_CONTRACTS = (
    ROOT / "manifest.yaml",
    ROOT / "protocol.lock.yaml",
    ROOT / "modules/identity/module.yaml",
    ROOT / "modules/identity/identity.yaml",
    ROOT / "modules/relationships/module.yaml",
    ROOT / "modules/relationships/relationships.yaml",
    ROOT / "modules/governance/module.yaml",
    ROOT / "modules/engineering/module.yaml",
    ROOT / "modules/portfolio/module.yaml",
    ROOT / "modules/decisions/module.yaml",
)
EXPECTED_ENTITY = {"type": "organization", "id": "aiaiaiai"}


def validate() -> list[str]:
    errors: list[str] = []
    manifest = load_yaml_mapping(MANIFEST)
    mind = manifest.get("mind", {})

    if manifest.get("schema_version") != 3:
        errors.append("manifest schema_version must be 3")
    if manifest.get("protocol") != {"id": "mind", "version": "0.9.0"}:
        errors.append("manifest must consume Mind Protocol 0.9.0")
    if mind.get("name") != "mind@aiaiaiai":
        errors.append("canonical mind name must be mind@aiaiaiai")
    if mind.get("subject") != EXPECTED_ENTITY:
        errors.append("canonical subject must be organization:aiaiaiai")
    if mind.get("owner") != EXPECTED_ENTITY:
        errors.append("publication owner must be organization:aiaiaiai")
    if mind.get("context_version") != "0.3.0":
        errors.append("this audited bridge must publish context_version 0.3.0")
    if "kind" in mind:
        errors.append("mind.kind is forbidden by manifest v3")
    if "public_organizations" in manifest:
        errors.append("public_organizations is forbidden by manifest v3")

    catalog = manifest.get("modules", {}).get("catalog", {})
    if isinstance(catalog, dict):
        for module_id, relative_path in catalog.items():
            if not isinstance(relative_path, str):
                continue
            descriptor = load_yaml_mapping(ROOT / relative_path)
            owner = descriptor.get("module", {}).get("owner")
            if owner != EXPECTED_ENTITY:
                errors.append(f"module {module_id} owner must be organization:aiaiaiai")

    relationships = load_yaml_mapping(ROOT / "modules/relationships/relationships.yaml")
    for index, relation in enumerate(relationships.get("relationships", [])):
        if not isinstance(relation, dict):
            continue
        if relation.get("provenance", {}).get("authority") != EXPECTED_ENTITY:
            errors.append(f"relationship[{index}] authority must be organization:aiaiaiai")
        endpoints = (relation.get("source"), relation.get("target"))
        if EXPECTED_ENTITY not in endpoints:
            errors.append(f"relationship[{index}] must involve organization:aiaiaiai")

    for path in MACHINE_CONTRACTS:
        if path.is_file() and "aiaiaiai-tech" in path.read_text(encoding="utf-8"):
            errors.append(f"legacy canonical id remains in active machine contract: {path.relative_to(ROOT)}")

    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, TypeError) as error:
        print(f"organization canary validation failed:\n- {error}", file=sys.stderr)
        return 1

    if errors:
        print("organization canary validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("aiaiaiai organization canary invariants are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
