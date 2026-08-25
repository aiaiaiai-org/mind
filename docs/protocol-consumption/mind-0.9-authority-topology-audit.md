# Mind 0.9 authority topology audit

Status: **PASS — content/contract topology normalized; historical GitHub fork metadata intentionally preserved**  
Observed: 2026-08-25

## Purpose

This report records the post-split state after Mind Protocol authority moved physically from the historical hybrid `0x0sky/mind` repository to `aiaiaiai-org/mind-protocol` and the four real Mind implementations were normalized as concrete consumers.

It complements, rather than rewrites, `mind-0.9-canary-report.md`. The earlier report remains historical evidence for the pre-split P5 state.

## Authority boundary

Current canonical protocol authority:

- repository: `aiaiaiai-org/mind-protocol`;
- master: `6bf8467f0e3990808464e118cc60cc83d8ab2ced`;
- tree: `c402855fbdfcff7b8e115cd1b277424fcb26bb32`;
- role: protocol/schema/conformance/compatibility/bootstrap/release authority only;
- concrete root Mind: absent.

Historical Mind Protocol `0.9.0` publication remains immutable at:

- repository: `0x0sky/mind`;
- tag: `v0.9.0`;
- release commit: `457844c8ced0318d91d628617ff6f8ec6f428ab7`.

The historical release is not recreated, retagged, or rewritten in `aiaiaiai-org/mind-protocol`. The first formal protocol publication from the new authority is intended to be `v1.0.0-rc.1`.

## Four concrete consumers

| Repository | Canonical subject | Display identity | Context | Observed master | Tested head | Verified tree |
| --- | --- | --- | ---: | --- | --- | --- |
| `0x0sky/mind` | `person:0x0sky` | `0x0sky` | `0.4.0` | `8ac50ec18a0ce71fb188189845452b80bc17838a` | `3d64fde4ac0ef373be6f76331d77141a58eb5872` | `5d532aeeba623195e168865d11eda57e9e644eec` |
| `aiaiaiai-org/mind` | `organization:aiaiaiai` | `aiaiaiai` | `0.3.0` | `60497aa72468fc27087f278efea10f1a271309b6` | `edcc89eb6c0b3d3d613a55e3042bb6d20f82c1e0` | `a7686713b3daccf0de7d9f6d52d523b99a8d8548` |
| `0xda-market/mind` | `organization:0xda-market` | `0xda-market` | `0.2.0` | `e35f1455db02cd7d5f93d0d0c1948c5a5ac0e587` | `cf47d96940473c65cf524b19105a5d0f78a5de3a` | `2986f78e0ccfab24e639600f66624a7d7af686fc` |
| `nilx-one/mind` | `organization:nilx-one` | `nilx.one` | `0.2.0` | `f7f8221476bfe1291e99d986922f704a1e4d2c2f` | `dce86fbccbeeeaec49a911f3eca247a2e5446f5d` | `2f07da15c4f07b338ba230d26909ff7c6521b29f` |

For each normalization PR, the merge commit tree equals the already-green tested PR-head tree. No duplicate post-merge full-CI run is required for that evidence.

## Common consumer contract

Every concrete repository now declares:

- protocol authority role disabled;
- concrete Mind role enabled;
- reference implementation disabled;
- template authority disabled;
- canonical subject explicitly bound to that repository's Identity;
- protocol relationship to `aiaiaiai-org/mind-protocol` as `independent_consumer`;
- exact-release bootstrap as the creation mechanism for new concrete Minds;
- protocol and context version axes as independent.

All four `protocol.lock.yaml` files are byte-identical at Git blob SHA-1:

`97280e91a4342d11f57fc36bba2c83629d73aa8a`

They separate two facts explicitly:

```yaml
authority_repository: aiaiaiai-org/mind-protocol

release_source:
  repository: 0x0sky/mind
  tag: v0.9.0
  commit: 457844c8ced0318d91d628617ff6f8ec6f428ab7
  floating_branch: forbidden
```

This is intentionally transitional for `0.9.0`. After `v1.0.0-rc.1` is published from the new authority, release authority and release source converge on `aiaiaiai-org/mind-protocol` for the RC synchronization.

## Identity invariants

- `0x0sky` remains a person Identity, not a protocol owner abstraction.
- `aiaiaiai` remains the provider-independent organization id; `aiaiaiai-org` is the current GitHub namespace.
- `0xda-market` remains its authored organization id.
- `nilx-one` remains the stable machine id and `nilx.one` the authored display name.
- `0x1` remains a distinct product identity and is not treated as the `nilx.one` organization.

No Identity/context version was changed merely because protocol authority moved repositories.

## GitHub repository topology

The semantic topology is already complete: each concrete Mind is an independent protocol consumer and none treats GitHub fork ancestry as protocol inheritance.

GitHub still records `aiaiaiai-org/mind`, `0xda-market/mind`, and `nilx-one/mind` inside the historical `0x0sky/mind` fork network. This host-level relationship predates the physical authority split and is explicitly **non-semantic**.

GitHub's current `Leave fork network` operation is destructive to repository metadata: Git commits are preserved, but issues, pull requests, comments, stars, watchers, wikis, child forks, and other associated metadata are not retained; the detach is permanent. Because review/CI history is valuable migration evidence, physical fork-network detachment is deliberately **deferred and is not an RC or 1.0 protocol gate**.

The concrete repositories must not be attached to `aiaiaiai-org/mind-protocol` as forks. Protocol linkage is represented by immutable release locks and protocol contracts, not GitHub fork ancestry.

If physical detachment is ever desired later, it requires a separate repository-metadata migration with an explicit decision on preserving/exporting relevant GitHub metadata before the irreversible action.

## Acceptance

- [x] pure protocol authority exists at `aiaiaiai-org/mind-protocol`;
- [x] four real repositories are concrete-only consumers;
- [x] all four consume Mind Protocol `0.9.0`;
- [x] all four name `aiaiaiai-org/mind-protocol` as current authority;
- [x] all four preserve exact historical `0x0sky/mind@v0.9.0` release provenance;
- [x] all four use the same release lock bytes;
- [x] all four preserve canonical Identity and independent context versions;
- [x] latest normalization CI is green for all four;
- [x] GitHub fork relationship is explicitly non-semantic;
- [x] destructive fork-network detachment is not required for RC/stable protocol correctness;
- [x] existing GitHub PR/review metadata is preserved by deferring detach;
- [ ] publish `v1.0.0-rc.1` from `aiaiaiai-org/mind-protocol` after final release validation;
- [ ] synchronize all four concrete consumers to that immutable RC release.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
