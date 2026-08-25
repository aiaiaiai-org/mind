# aiaiaiai mind

> The canonical public organization mind of `aiaiaiai`.

This repository is a standalone concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/aiaiaiai-org/mind-protocol). Protocol semantics and releases live in the protocol authority repository; organization-specific identity and durable context remain here.

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

`manifest.yaml` is the machine-readable entry point. This concrete Mind currently consumes **Mind Protocol `1.0.0-rc.2`** using manifest schema v3 while organization context remains `0.3.0`.

`mind-repository.yaml` declares this repository as a concrete Mind only. It is neither protocol authority nor template authority, and its relationship to `aiaiaiai-org/mind-protocol` is `independent_consumer`.

Exact release provenance:

- authority/release repository: `aiaiaiai-org/mind-protocol`;
- tag: `v1.0.0-rc.2`;
- commit: `acdcedcf02c8b4ef314179bf54955a84606c8fb5`.

`protocol.lock.yaml` pins the protocol descriptor, complete frozen schema set, conformance contract, compatibility policy, schema `$id` values, and Git blob fingerprints consumed by this repository. The JSON Schema bytes remain the frozen `0.9.0` shapes; only the protocol lifecycle/release binding advances to the RC.

The protocol version and this organization's context version are independent. This synchronization does **not** change canonical Identity, authored relationships, governance, engineering, portfolio, decisions, or `context_version: 0.3.0`.

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

This is not inferred from GitHub. The two canonical minds independently author the same semantic relation under their own publication authorities.

## Protocol relationship

- `aiaiaiai-org/mind-protocol` defines universal Mind Protocol semantics and owns all new protocol releases;
- historical `v0.9.0` remains immutable in `0x0sky/mind` and is not rewritten;
- `aiaiaiai-org/mind` owns organization-specific identity and durable context;
- protocol compatibility is represented by the immutable release lock, not GitHub fork ancestry.

The audited legacy bridge is recorded in [`docs/migrations/legacy-to-mind-0.9.md`](docs/migrations/legacy-to-mind-0.9.md).

## Validation

Mind Contract CI validates published schema syntax, manifest v3 semantics, module graph, typed resources, universal Identity envelopes, relationship authority, the exact protocol release lock, repository-role metadata, and organization-specific consumer invariants.

## Visual identity boundary

The RC continues to support optional canonical visual identity references. Canonical `aiaiaiai` production assets are versioned by this concrete Mind, while binding the Identity primary mark and provider projections remains gated on stable Mind Protocol `1.0.0`.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
