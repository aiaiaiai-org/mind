# modules

A module is a focused, replaceable unit of context composed into a concrete mind.

## Interface

Each `module.yaml` is validated by [`../schema/module.schema.json`](../schema/module.schema.json) and declares a stable `id`, one `purpose`, a stability class, explicit dependencies and entrypoints, an owner, visibility, and optional typed machine-readable resources.

## Machine-readable resources

Resources let modules expose structured data without adding module-specific fields to the root manifest.

Protocol-defined resources currently include:

- `identity` — canonical subject metadata via `schema/identity.schema.json`;
- `relationships` — authored entity relations, provenance, direction, and confirmation via `schema/relationships.schema.json`.

Mind CI validates each resource against its declared schema. Relationship-specific CI also enforces subject/owner authority boundaries and legacy migration semantics where applicable.

## Rules

- one reason to change per module;
- no duplicated canonical content;
- dependencies resolve to registered module IDs;
- self-dependencies and dependency cycles are forbidden;
- every entrypoint/resource/schema remains inside the repository;
- optional consumers can ignore optional modules safely;
- module-specific data belongs in typed resources instead of new root-manifest fields unless the concept is genuinely protocol-wide.
