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
REPOSITORY_METADATA = ROOT / "mind-repository.yaml"
MACHINE_CONTRACTS = (
    ROOT / "manifest.yaml",
    ROOT / "mind-repository.yaml",
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
EXPECTED_PROTOCOL_CONSUMPTION = {
    "id": "mind",
    "version": "0.9.0",
    "authority_repository": "aiaiaiai-org/mind-protocol",
    "release_repository": "0x0sky/mind",
    "release_tag": "v0.9.0",
    "release_commit": "457844c8ced0318d91d628617ff6f8ec6f428ab7",
    "floating_master": "forbidden",
}


def validate() -> list[str]:
    errors: list[str] = []
    manifest = load_yaml_mapping(MANIFEST)
    repository = load_yaml_mapping(REPOSITORY_METADATA)
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

    roles = repository.get("repository", {}).get("roles", {})
    if roles.get("protocol_authority") != {"enabled": False}:
        errors.append("aiaiaiai-org/mind must not declare protocol authority")
    concrete = roles.get("concrete_mind", {})
    if concrete.get("enabled") is not True:
        errors.append("concrete mind role must be enabled")
    if concrete.get("canonical_for_subject") != EXPECTED_ENTITY:
        errors.append("repository role must be canonical only for organization:aiaiaiai")
    if concrete.get("template_authority") is not False:
        errors.append("organization Mind must not be a template authority")

    if repository.get("protocol_consumption") != EXPECTED_PROTOCOL_CONSUMPTION:
        errors.append(
            "repository metadata must separate current protocol authority from immutable v0.9.0 release provenance"
        )
    if repository.get("fork_policy", {}).get("relationship_to_protocol_repository") != "independent_consumer":
        errors.append("protocol relationship must be independent_consumer, not GitHub fork inheritance")

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

    print("aiaiaiai organization Mind is a standalone concrete 0.9 consumer with truthful provenance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
