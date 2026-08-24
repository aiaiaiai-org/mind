# Mind Protocol 0.9 real-canary report

Status: **PASS**  
Observed: 2026-08-24  
Protocol release: `0x0sky/mind@v0.9.0`

## Purpose

This report records the P5 compatibility-canary evidence for four real Mind publications. It is named implementation evidence owned by the parent organization mind; it is not part of the universal Mind Protocol contract and does not make any real identity a protocol authority.

The matrix verifies the released `0.9.0` contract against one person mind, one parent organization mind, and two child organization/namespace minds after their canonical default branches were normalized to `master`.

## Evidence set

| Canary | Canonical subject | Context | Observed `master` | Tested PR head | Verified tree | CI evidence |
| --- | --- | ---: | --- | --- | --- | --- |
| `0x0sky/mind` | `person:0x0sky` | `0.4.0` | `457844c8ced0318d91d628617ff6f8ec6f428ab7` | `af8d9d66f4fb7b5899f365db4755ddee84100f9e` | `e40ac6607b17336039b2ffa0dd578285e1112bb6` | Mind Contract CI #62, run `32750120216`, success |
| `aiaiaiai-org/mind` | `organization:aiaiaiai` | `0.3.0` | `db720ae2c824f27c2957277590a16b8c7b2a910d` | `17e40490d5309227deb98ce09f6e2ffc2776ee54` | `dfadcb318c7f143205c8c86ceafd94cf865f1efa` | Mind Contract CI #11, run `32752638826`, success |
| `0xda-market/mind` | `organization:0xda-market` | `0.2.0` | `ab91a92e82ba63877ee0482baff3bd8b3b8d2684` | `0ba519c2f4b3bbecc122b012e3a0d841c1f15c82` | `97275be83064ac1bd328ed692f121581eebe39d4` | Mind Contract CI #1, run `32753218195`, success |
| `nilx-one/mind` | `organization:nilx-one` | `0.2.0` | `f8aee45393f084f0552e23821e9ae44704e1fd60` | `ece7ff41624d5b376504f7b8e6e1e4f93e4add72` | `0e8afcb65dc6171045447301f240ff8d1282efb4` | Mind Contract CI #1, run `32753729447`, success |

For every row, the merge commit tree equals the tree of the successful PR head, so the already-green correctness result is reusable without a duplicate post-merge full-CI run.

Repository metadata was re-read after the child migrations. All four repositories now expose `master` as their default branch. The historical `foundation/baseline-v0.1.0` branches in the two child minds remain history rather than implicit consumer entry points.

## Release consumption

All four manifests explicitly declare:

```yaml
schema_version: 3
protocol:
  id: mind
  version: 0.9.0
```

The three organization consumers vendor the same exact release lock. Their `protocol.lock.yaml` blobs are byte-identical (`abbd50998f4723fb5a4a575ce2356ea186f9d294`) and pin:

- source repository `0x0sky/mind`;
- immutable release ref `v0.9.0`;
- release commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`;
- floating branch consumption as forbidden;
- the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set by Git blob SHA-1 and schema `$id`.

Protocol version and concrete context version remain independent. None of the organization repositories creates a protocol-version tag.

## Identity binding

Every concrete Identity envelope binds exactly to its manifest subject:

| Mind | Identity type | Identity id | Display name | Manifest binding |
| --- | --- | --- | --- | --- |
| `mind@0x0sky` | `person` | `0x0sky` | `0x0sky` | exact |
| `mind@aiaiaiai` | `organization` | `aiaiaiai` | `aiaiaiai` | exact |
| `mind@0xda-market` | `organization` | `0xda-market` | `0xda-market` | exact |
| `mind@nilx-one` | `organization` | `nilx-one` | `nilx.one` | exact |

Provider names do not define canonical ids. This is visible most clearly for `aiaiaiai`: canonical id `aiaiaiai`, current GitHub namespace `aiaiaiai-org`. For `0xda-market` and `nilx-one`, a canonical id currently resembles the provider namespace, but the id is explicitly authored in the Mind publication and is not inferred from GitHub metadata. `nilx.one` remains the authored display identity while `nilx-one` is the stable machine id used by this publication.

## Relationship provenance

The real published relationship resources preserve authored provenance.

`mind@0x0sky` publishes `member_of` assertions for `aiaiaiai`, `0xda-market`, and `nilx-one`, each with `provenance.kind: authored` and authority `person:0x0sky`.

`mind@aiaiaiai` independently publishes the reciprocal `0x0sky -> aiaiaiai` relationship with `provenance.kind: authored` and authority `organization:aiaiaiai`. The reciprocal ids agree:

- person side: `member-of-aiaiaiai`;
- organization side: `member-0x0sky`.

The two child organization canaries do not publish machine relationship modules in this phase. Their human-authored parent/product context was deliberately not converted into inferred canonical relationship predicates. Absence remains absence rather than derived authority.

## Visual identity boundary

None of the four current canary Identity envelopes publishes a canonical `visual_identity.primary_mark`. This is valid in `0.9.0`: canonical visual identity is optional, and a missing mark must not invalidate Identity.

The released protocol's green conformance evidence separately covers deterministic visual behavior: valid canonical resolution and integrity failure are both exercised by the protocol fixtures. This keeps visual behavior a protocol concern while avoiding invented organization logos before the stable `1.0.0` rollout.

## Optional and unknown capability policy

The released `0.9.0` compatibility contract defines modules as the capability-negotiation unit:

- unknown optional module: ignore when not requested;
- unknown required module: reject;
- unknown default-loaded module: reject;
- unknown root manifest field: reject.

Publication-side checks pass for all four real manifests: required/default/optional module sets contain only registered modules, and each registered module is discoverable through `modules.catalog`.

Consumer behavior is not reimplemented separately by each identity repository. It is protocol-owned and is exercised by the two independent `schema` and `minimal` conformance modes. Mind Contract CI #62 passed the dual-mode conformance, canonical visual fixtures, compatibility freeze, migration policy, and regression suite. The organization consumers pin those exact released conformance and compatibility artifacts.

## Layout independence

No real canary requires the reference instance's repository layout. The personal mind registers Identity at `identity/module.yaml`, while organization minds register it at `modules/identity/module.yaml`. Consumers discover modules through the manifest catalog rather than a hard-coded reference-owner path.

The release lock names `0x0sky/mind` only as the immutable distribution source for the `0.9.0` contract artifacts. That packaging reference is not a universal Identity field, provider requirement, or repository-layout requirement.

## Findings and ownership

No P5 defect was found.

- implementation-specific failures: **0**;
- universal non-breaking protocol defects: **0**;
- universal breaking protocol defects: **0**;
- unclassified failures: **0**.

Ownership remains explicit: universal behavior belongs to the released Mind Protocol contracts and conformance suite; concrete identity, authored relationships, context versions, and repository packaging belong to each sovereign Mind publication.

## Acceptance

- [x] four real minds green;
- [x] every canary explicitly declares Mind Protocol `0.9.0`;
- [x] every canary uses manifest schema v3;
- [x] every Identity type/id binds exactly to its manifest subject;
- [x] provider metadata does not define canonical identity ids;
- [x] published relationship provenance remains authored;
- [x] missing optional visual identity does not fail Identity;
- [x] deterministic visual and unknown-module behavior is green in protocol conformance;
- [x] no canary requires the reference repository owner or fixed instance layout;
- [x] zero unclassified failures;
- [x] protocol-vs-implementation ownership is explicit for every finding.

P5 is green. This evidence clears the compatibility-canary prerequisite for preparing `1.0.0-rc.1`; it does not itself publish, tag, or alter the universal protocol.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
