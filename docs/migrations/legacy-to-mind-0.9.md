# Legacy bridge to Mind Protocol 0.9

This document records the one-time audited migration of the `aiaiaiai` organization mind to the first formal Mind Protocol release.

## Source state

- source repository: `aiaiaiai-org/mind`
- source commit: `8e0591d6f592759e45202b6f740bc7b15002084e`
- source protocol: `0.5.0-rc.1`
- source manifest schema: `2`
- source context version: `0.2.2`
- destination protocol: `0.9.0`
- destination manifest schema: `3`
- destination context version: `0.3.0`

The source protocol is below the formally supported `0.6.0` migration floor. This change is therefore an explicit audited bridge, not a claim that Mind Protocol 0.9 generally supports automatic migration from `0.5.0-rc.1`.

## Preservation

The migration preserves existing authored organization content and module boundaries: identity, relationships, governance, engineering, portfolio, decisions, and their human-readable documentation remain owned by this repository. No generic content is copied from the protocol reference implementation.

The authored reciprocal relationship between `person:0x0sky` and `organization:aiaiaiai` remains intact, including authored provenance and the counterpart relationship id `member-of-aiaiaiai`.

## Identity state

The canonical organization id had already been migrated to `aiaiaiai` before this bridge. `aiaiaiai-org` remains a GitHub provider namespace only. This bridge does not reinterpret the provider login as canonical identity.

Several module descriptors still used the stale canonical owner id `aiaiaiai-tech`; those owner references are corrected to `organization:aiaiaiai`. That is a durable authored context change and is one reason the concrete context version advances to `0.3.0`.

## Protocol consumption

This repository consumes the immutable `0x0sky/mind` tag `v0.9.0`, never a floating branch. `protocol.lock.yaml` records the exact protocol descriptor and vendored schema Git blob SHA-1 values. CI verifies those local contract bytes against the release fingerprints.

Protocol version and concrete context version remain independent. This repository does not create a `v0.9.0` tag because that would incorrectly imply the organization context release is the protocol release.

## Manifest v3 changes

- remove `mind.kind`; subject classification is expressed by `mind.subject.type`;
- use the exact `mind@aiaiaiai` concrete mind name;
- publish Identity through the `identity-resource/v1` envelope;
- preserve the existing module catalog and loading policy;
- keep provider-specific organization projection fields out of the core manifest.

## Verification

The canary CI checks:

- all vendored JSON Schemas are valid Draft 2020-12 documents;
- manifest v3 syntax and semantics;
- module graph and machine resources;
- universal Identity envelope semantics;
- relationship authority and subject boundaries;
- exact `v0.9.0` protocol/schema release lock;
- absence of the legacy `aiaiaiai-tech` id from active machine contracts.

This canary provides implementation evidence only. `aiaiaiai-org/mind` does not become Mind Protocol authority.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
