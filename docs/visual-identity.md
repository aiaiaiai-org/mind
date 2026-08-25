# aiaiaiai visual identity publication

This concrete Mind publishes the named visual assets for the `aiaiaiai` organization. Mind Protocol defines how canonical visual references resolve; this repository owns the actual `aiaiaiai` asset bytes and their integrity digests.

## Provenance

The approved visual direction is **aiaiaiai Visual Identity v0.9 (23 August 2026)**. Its final recommendation preserves the 2023 master lockup and defines the cyan faceted polyhedron as the compact parent production emblem.

The 2023 master lockup is historical brand authority and is **not reconstructed in this change**. The available design package explicitly records that the original vector/source typography was not recovered and forbids silent auto-tracing. When exact owner-approved master bytes are recovered, they can be added as a separately referenced asset without changing the compact emblem reference.

The compact emblem in this repository is a deterministic vector reconstruction of the approved v0.9 compact parent emblem, not a trace of the missing master lockup.

## Canonical production asset

| Property | Value |
| --- | --- |
| semantic ref | `aiaiaiai-compact-emblem` |
| source | `assets/visual/aiaiaiai/compact-emblem.svg` |
| grid | `64 × 64` |
| heritage cyan | `#5BC6F4` |
| full channel width | `3.2` units |
| SVG outside/channel space | transparent |
| provider PNG canvas | `#FFFFFF` |
| effects | no gradient, no glow |
| integrity | SHA-256 in `modules/identity/visual-assets.yaml` |

The geometry uses the v0.9 family grammar: faceted construction, negative-space channels, intersection nodes, sharp outer vertices, and white-first provider behavior. Meaning must survive monochrome.

## Provider export

`assets/visual/aiaiaiai/exports/compact-emblem-1024.png` is a deterministic 1024×1024 PNG derived from the canonical SVG by `scripts/export_visual_assets.py`.

The renderer is repository-owned and pinned by the exact `scripts/export_visual_assets.py` bytes plus `Pillow==12.3.0` in CI. The PNG is a provider-ready presentation derivative. It is suitable for square surfaces such as the GitHub Enterprise profile picture, but GitHub does not become the source of truth by receiving a copy.

The export is regenerated in memory and checked byte-for-byte in CI. Any change to canonical SVG bytes or generated PNG bytes must update the corresponding SHA-256 descriptor deliberately.

## Identity boundary

The current concrete consumer is pinned to Mind Protocol `1.0.0-rc.1`. This change deliberately **does not** author `identity.visual_identity.primary_mark` yet.

After stable Mind Protocol `1.0.0` is published and this concrete Mind is pinned to that immutable release, the canonical identity can bind:

```yaml
visual_identity:
  primary_mark:
    kind: emblem
    asset_ref: aiaiaiai-compact-emblem
    alt: aiaiaiai
```

The opaque `asset_ref` is the identity-level reference. Repository paths, raw GitHub URLs, CDN URLs, provider avatar identifiers, and content hashes are not universal Identity semantics.

## Asset discovery audit

The approved visual identity package and current accessible organization repositories were inspected before this publication was prepared. No standalone approved parent `compact-emblem.svg` or original 2023 master vector was found in repository state.

HQBase contains its own orange product logo and PWA assets; those are product-specific and are not parent-brand sources. The missing master lockup therefore remains untouched rather than being silently reconstructed.

## Consumer rule

Provider or application projections may cache or transform the verified canonical asset, but they must remain reproducible from this repository and must not silently replace the canonical mark.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
