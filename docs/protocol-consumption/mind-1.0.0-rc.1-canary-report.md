# Mind Protocol 1.0.0-rc.1 real-canary report

Status: **PASS**  
Observed: 2026-08-25  
Protocol release: `aiaiaiai-org/mind-protocol@v1.0.0-rc.1`

## Purpose

This report records the four-real-Mind synchronization after Mind Protocol `1.0.0-rc.1` was published from the physically separated canonical protocol authority.

It complements the historical `0.9.0` canary and authority-topology reports. Those reports remain immutable evidence of earlier stages and are not rewritten to make the migration appear simpler than it was.

## Published RC

The consumed protocol release is:

- authority/release repository: `aiaiaiai-org/mind-protocol`;
- tag: `v1.0.0-rc.1`;
- GitHub release kind: prerelease;
- release commit: `6bf8467f0e3990808464e118cc60cc83d8ab2ced`;
- release tree: `c402855fbdfcff7b8e115cd1b277424fcb26bb32`.

The historical `0x0sky/mind@v0.9.0` release remains untouched. Starting with this RC, current protocol authority and immutable release source converge on `aiaiaiai-org/mind-protocol`.

## Four concrete consumers

| Repository | Canonical subject | Display identity | Context | RC merge commit | Green tested head | Verified tree | CI run |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| `0x0sky/mind` | `person:0x0sky` | `0x0sky` | `0.4.0` | `4dee272711f0a6d006d3f3cf9dc62caa42148d19` | `3eddf734979a4d987a4366f658f945402fc00679` | `f5d03ca3c8c13885b692837eec633a889d3e6103` | `32804444545` |
| `aiaiaiai-org/mind` | `organization:aiaiaiai` | `aiaiaiai` | `0.3.0` | `b24670b7879966f85a62fe08ab27093bfbebc625` | `f05c6e5a52ffc6b9c8f385b8c7730f7ffece7e1b` | `2fb55c9a4106d7ed9a2e3b371d017178a5f509dc` | `32804684925` |
| `0xda-market/mind` | `organization:0xda-market` | `0xda-market` | `0.2.0` | `1e5f45a4fd777de63365ce8dae8a2b93a842f90c` | `7ea2b3b7c0f19f92ccf3ff67678f7ec1060918f6` | `859c8bcfcc2eca0fd291597bce79a2b397978e18` | `32804954862` |
| `nilx-one/mind` | `organization:nilx-one` | `nilx.one` | `0.2.0` | `28279af5fa5acefe60bf4c877246a5d7e8a4a596` | `3ea0c7618e39ee21318d3d777c7c6aedcdb83cc8` | `ff78b3949ec6c8b999d3359ce6d2a35957ab151a` | `32805191783` |

For every synchronization PR, the merge-commit tree equals the successful PR-head tree exactly. The green correctness result is therefore reusable without duplicate post-merge full CI.

## Exact release lock

All four concrete Minds now expose byte-identical `protocol.lock.yaml` at Git blob SHA-1:

`70b02753493879294d275e92b4e1289d752bdb44`

The common lock declares:

```yaml
protocol:
  id: mind
  version: 1.0.0-rc.1

authority_repository: aiaiaiai-org/mind-protocol

release_source:
  repository: aiaiaiai-org/mind-protocol
  tag: v1.0.0-rc.1
  commit: 6bf8467f0e3990808464e118cc60cc83d8ab2ced
  floating_branch: forbidden
```

It additionally pins the released descriptor and machine artifacts exactly:

- `protocol.yaml`: `776eee50640361f533f5fd1b9ab7efd9a7b3e458`;
- `conformance.yaml`: `b2c84244e5591539086f156f08fc5cf136a97bd2`;
- `compatibility.yaml`: `12f5a34b27333489cb6adfb89679bc0e69927dbb`.

## Frozen schema continuity

No JSON Schema bytes changed when consumers moved from `0.9.0` to `1.0.0-rc.1`. Every consumer continues to pin the same frozen schema set:

- protocol: `23bc8ffde889c7c20ca446e6fca8e914920f4fd2`;
- manifest: `cc89e3364c404a86fdce72a061195768ee460597`;
- module: `206a9f05feb888c1186d9fb884989d108dc53756`;
- Identity: `32efb75e88b9edd197ded82ca0a77669ad3e5679`;
- Identity resource: `aa9d22d32d7b3ad033032888663488850453f7c2`;
- relationships: `6cae6a6de82a2a225d55969a44fc7773304e94a5`;
- visual assets: `dd65ec62ce70a6fe22ee005339ae9c374451a320`;
- conformance schema: `a94e3a96a5f475a2757da4b4a8533f6b8b150540`;
- compatibility schema: `2fe9f477ff6284e585e9a1ac1e8d0e6434cc964a`.

The RC changes protocol lifecycle/version binding and SemVer/conformance behavior, not the frozen schema shapes.

## Identity and context invariants

The protocol-only synchronization did not silently republish authored context.

| Mind | Identity | Identity blob | Context before/after |
| --- | --- | --- | --- |
| `mind@0x0sky` | `person:0x0sky` / `0x0sky` | `71dca3db25274dae0b26c0d86ca2d5ec20de630c` | `0.4.0` → `0.4.0` |
| `mind@aiaiaiai` | `organization:aiaiaiai` / `aiaiaiai` | `183dc1e49615dacd645f4edd4ea581c4c40da41d` | `0.3.0` → `0.3.0` |
| `mind@0xda-market` | `organization:0xda-market` / `0xda-market` | `ede5a20f994a507826b353832d1b3d8853604c93` | `0.2.0` → `0.2.0` |
| `mind@nilx-one` | `organization:nilx-one` / `nilx.one` | `5a99defa36a76071f7ae875b85466eebcb1aad85` | `0.2.0` → `0.2.0` |

Provider names remain non-authoritative. `aiaiaiai` is not redefined as `aiaiaiai-org`; `nilx-one` remains the organization machine id while `nilx.one` remains its display identity; `0x1` remains a distinct product identity.

## Consumer sovereignty

Each concrete repository remains a concrete-only independent consumer:

- protocol authority disabled locally;
- template/reference authority disabled locally;
- subject/owner explicitly authored locally;
- context version independently owned locally;
- protocol linkage expressed through an immutable release lock;
- no concrete repository receives a new protocol-version tag.

The three organization repositories may still carry historical GitHub fork-network metadata from the original bootstrap era. That hosting metadata is explicitly non-semantic and is not an RC or stable-release gate. Detaching it would discard useful GitHub review metadata, so no destructive detach is performed in this release train.

## Findings

No blocking defect was found in the four-real-Mind RC synchronization.

- protocol release-lock drift: **0**;
- Identity binding failures: **0**;
- context-version accidental bumps: **0**;
- frozen schema drift: **0**;
- named-identity leakage into protocol contracts: **0 observed**;
- provider identity substitutions: **0**;
- invented relationship/visual content during synchronization: **0**;
- unclassified failures: **0**.

## Acceptance

- [x] `v1.0.0-rc.1` published from `aiaiaiai-org/mind-protocol` as prerelease;
- [x] all four real Minds consume `1.0.0-rc.1`;
- [x] all four use byte-identical exact release locks;
- [x] authority and release source both point to the new protocol repository;
- [x] all four preserve their canonical Identity bindings;
- [x] all four preserve independent concrete context versions;
- [x] frozen schema bytes remain unchanged;
- [x] every consumer synchronization PR has green correctness CI;
- [x] every merge tree equals its tested PR-head tree;
- [x] no destructive GitHub fork-network cleanup is required for protocol correctness;
- [x] zero known blocking RC canary defects.

The `1.0.0-rc.1` four-real-Mind canary gate is green. This clears the release-train prerequisite for preparing the stable `1.0.0` promotion source; it does **not** itself publish or authorize stable `v1.0.0`.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
