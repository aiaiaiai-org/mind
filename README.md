# aiaiaiai mind

> The canonical public organization mind of `aiaiaiai`.

This repository is a standalone concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/aiaiaiai-org/mind-protocol). Protocol semantics and future releases live in the protocol authority repository; organization-specific identity and durable context remain here.

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

`manifest.yaml` is the machine-readable entry point. This instance is a compatibility canary for Mind Protocol `0.9.0`, using manifest schema v3 and organization context `0.3.0`.

`mind-repository.yaml` declares this repository as a concrete Mind only. It is neither protocol authority nor template authority, and its intended relationship to `aiaiaiai-org/mind-protocol` is `independent_consumer` rather than GitHub fork inheritance.

`protocol.lock.yaml` keeps two facts separate:

- **current protocol authority:** `aiaiaiai-org/mind-protocol`;
- **immutable `0.9.0` release provenance:** `0x0sky/mind@v0.9.0`, commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`.

The authority moved after `0.9.0`; that historical tag/release is not recreated or rewritten in the new authority repository. Starting with `1.0.0-rc.1`, formal protocol releases are published from `aiaiaiai-org/mind-protocol`.

The lock also pins the protocol descriptor, complete frozen schema set, conformance contract, compatibility policy, schema `$id` values, and Git blob fingerprints consumed by this repository. CI rejects drift from those published contract bytes. The protocol version and this organization's context version are independent.

The `0.3.0` context line records the v3 representation change, Identity resource envelope adoption, and cleanup of legacy module-owner identifiers. The canonical subject itself was already `aiaiaiai` before this bridge.

## Composition

```text
OrganizationMind
├── manifest.yaml
├── mind-repository.yaml
├── protocol.yaml
├── protocol.lock.yaml
├── conformance.yaml
├── compatibility.yaml
├── ORGANIZATION.md
├── schema/
│   ├── protocol.schema.json
│   ├── mind.schema.json
│   ├── module.schema.json
│   ├── identity.schema.json
│   ├── identity-resource.schema.json
│   ├── relationships.schema.json
│   ├── visual-assets.schema.json
│   ├── conformance.schema.json
│   └── compatibility.schema.json
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

- `aiaiaiai-org/mind-protocol` defines universal Mind Protocol semantics and is the current release authority;
- `0x0sky/mind` remains the immutable historical publication source for `v0.9.0` and separately owns `person:0x0sky` context;
- `aiaiaiai-org/mind` owns organization-specific identity, relationship, governance, engineering, and portfolio context;
- this concrete Mind consumes an exact immutable protocol release and never becomes protocol authority;
- protocol compatibility is represented by `protocol.lock.yaml`, not GitHub fork ancestry.

The audited legacy bridge is recorded in [`docs/migrations/legacy-to-mind-0.9.md`](docs/migrations/legacy-to-mind-0.9.md).

## Validation

Mind Contract CI validates published schema syntax, manifest v3 semantics, module graph, typed resources, universal Identity envelopes, relationship authority, the exact protocol release lock, repository-role metadata, and organization-specific canary invariants.

## Visual identity boundary

Mind Protocol 0.9 supports optional canonical visual identity references, but this canary synchronization does not perform the full named visual-family rollout. That remains a separate post-1.0 implementation phase.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
