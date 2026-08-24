# aiaiaiai mind

> The canonical public organization mind of `aiaiaiai`.

This repository is a concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/0x0sky/mind). Protocol semantics remain upstream; organization-specific identity and durable context remain here.

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

`manifest.yaml` is the machine-readable entry point. This instance is a compatibility canary for the immutable Mind Protocol `v0.9.0` release, using manifest schema v3 and organization context `0.3.0`.

`protocol.lock.yaml` pins the exact release tag, protocol descriptor, schema `$id` values, and Git blob fingerprints consumed by this repository. CI rejects drift from those published contract bytes. The protocol version and this organization's context version are independent.

The `0.3.0` context line records the v3 representation change, Identity resource envelope adoption, and cleanup of stale `aiaiaiai-tech` module-owner identifiers. The canonical subject itself was already `aiaiaiai` before this bridge.

## Composition

```text
OrganizationMind
├── manifest.yaml
├── protocol.yaml
├── protocol.lock.yaml
├── ORGANIZATION.md
├── schema/
│   ├── mind.schema.json
│   ├── module.schema.json
│   ├── identity.schema.json
│   ├── identity-resource.schema.json
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

- `0x0sky/mind` publishes reusable protocol semantics and the personal endpoint's canonical context;
- `aiaiaiai-org/mind` owns organization-specific identity, relationship, governance, engineering, and portfolio context;
- this canary consumes the immutable `v0.9.0` release and does not become protocol authority;
- repository-specific implementation remains canonical in the owning repository and is referenced rather than copied.

The audited legacy bridge is recorded in [`docs/migrations/legacy-to-mind-0.9.md`](docs/migrations/legacy-to-mind-0.9.md).

## Validation

Mind Contract CI validates published schema syntax, manifest v3 semantics, module graph, typed resources, universal Identity envelopes, relationship authority, the exact protocol release lock, and organization-specific canary invariants.

## Visual identity boundary

Mind Protocol 0.9 supports optional canonical visual identity references, but this canary synchronization does not perform the full named visual-family rollout. That remains a separate post-1.0 implementation phase.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.
