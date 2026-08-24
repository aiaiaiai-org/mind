# aiaiaiai mind

> The canonical public organization mind of `aiaiaiai`.

This repository is a concrete organization implementation of the vendor-independent [Mind Protocol](https://github.com/0x0sky/mind). Protocol semantics remain upstream; organization-specific identity and context remain here.

## Organization identity

- **Organization:** `aiaiaiai` / `4xAI`
- **Canonical subject id:** `aiaiaiai`
- **GitHub namespace:** [`aiaiaiai-org`](https://github.com/aiaiaiai-org)
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** parent organization and organizational hub for non-personal work
- **Current form:** GitHub organization and operating identity
- **Long-term direction:** legal corporate parent
- **Child organizations / namespaces:** [0xda-market](https://github.com/0xda-market), [nilx.one](https://github.com/nilx-one)

The canonical organization id is provider-independent. `aiaiaiai-org` is the current GitHub namespace and must not be used as the protocol-level organization identity.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This instance implements Mind Protocol `0.5.0-rc.1` with manifest schema v2 and organization context `0.2.2`.

The context version moves from `0.2.1` because the organization identity is now separated from its GitHub provider namespace: `aiaiaiai` is the canonical subject and `aiaiaiai-org` is provider metadata.

## Composition

```text
OrganizationMind
├── manifest.yaml
├── ORGANIZATION.md
├── schema/
│   ├── mind.schema.json
│   ├── module.schema.json
│   ├── identity.schema.json
│   └── relationships.schema.json
└── modules/
    ├── identity/
    ├── relationships/
    ├── governance/
    ├── engineering/
    ├── portfolio/
    └── decisions/
```

Required organization modules remain `identity`, `governance`, `engineering`, and `portfolio`. The `relationships` module is registered and loaded by default because this organization publishes authored relationship context. `decisions` remains optional.

## Reciprocal relationship

The organization independently publishes:

```text
person:0x0sky --member_of--> organization:aiaiaiai
```

Its local relationship id is `member-0x0sky`. The assertion is marked `reciprocal` and references `person:0x0sky` plus the personal mind's local relationship id `member-of-aiaiaiai`.

This is not inferred from GitHub. The two canonical minds independently author the same semantic relation under their own publication authorities. Provider membership may be used only as derived corroborating evidence.

## Protocol relationship

- `0x0sky/mind` owns reusable protocol semantics and the personal endpoint's canonical context;
- `aiaiaiai-org/mind` owns organization-specific identity, relationship, governance, engineering, and portfolio context;
- repository-specific implementation remains canonical in the owning repository and is referenced rather than copied.

## Validation

Mind Contract CI validates the manifest, module graph, typed resources, identity consistency, relationship subject/owner boundaries, reciprocal endpoint shape, and repository paths.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.
