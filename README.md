# aiaiaiai tech. mind

> The canonical public organization mind of `aiaiaiai tech.`.

This repository is a concrete organization implementation of the vendor-independent [Mind Protocol](https://github.com/0x0sky/mind). Protocol semantics remain upstream; organization-specific identity and context remain here.

## Organization identity

- **Organization:** `aiaiaiai tech.` / `4xAI tech.`
- **Canonical subject id:** `aiaiaiai-tech`
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** parent organization and organizational hub for non-personal work
- **Current form:** GitHub organization and operating identity
- **Long-term direction:** legal corporate parent
- **Child organizations / namespaces:** [0xda-market](https://github.com/0xda-market), [nilx.one](https://github.com/nilx-one)

The canonical topology is defined in [`ORGANIZATION.md`](ORGANIZATION.md). GitHub namespaces are technically peers and do not define conceptual ownership hierarchy.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. The current instance implements Mind Protocol `0.4.0-rc.1` with manifest schema v2.

The manifest separates:

- `mind.subject` — the organization this mind describes;
- `mind.owner` — the repository publication authority;
- `mind.context_version` — this organization's independently versioned context;
- `protocol.version` — the shared Mind Protocol version.

Both subject and publication owner are currently `organization:aiaiaiai-tech`.

## Composition

```text
OrganizationMind
├── manifest.yaml
├── ORGANIZATION.md
├── schema/
│   ├── mind.schema.json
│   ├── module.schema.json
│   └── identity.schema.json
└── modules/
    ├── identity/
    ├── governance/
    ├── engineering/
    ├── portfolio/
    └── decisions/
```

Required modules:

- `identity` — canonical public organization identity;
- `governance` — durable ownership, review, and publication rules;
- `engineering` — organization-wide engineering contracts;
- `portfolio` — stable project and product index.

Optional module:

- `decisions` — cross-repository decision records.

Every module has a validated `module.yaml`. The identity module additionally exposes the typed machine-readable resource `modules/identity/identity.yaml`.

## Protocol relationship

- `0x0sky/mind` is the canonical protocol reference implementation and personal reference mind.
- `aiaiaiai-tech/mind` is independently versioned organization context implementing that protocol.
- reusable protocol semantics belong upstream;
- organization-specific content belongs here;
- repository-specific implementation remains canonical in its owning repository and is referenced rather than copied.

## Validation

Mind Contract CI validates the manifest, module catalog and descriptors, dependency graph, typed resources, subject consistency, and repository paths.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.
