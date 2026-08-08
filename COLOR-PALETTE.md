# Ecosystem identity palette

> Canonical visual identity colors for the aiaiaiai tech. ecosystem graph.

This palette is derived from the cosmic / neural-network visualization of the ecosystem. The colors identify **entities**, not product states, severity levels, or UI actions. They should remain recognizable across diagrams, graph rendering, documentation, and future visual systems.

## Canonical colors

| Entity | Role | Primary | Deep | Luminous |
| --- | --- | --- | --- | --- |
| `Core ☦️` | soul / spiritual core | `#D9B66F` | `#765A2D` | `#F4D99B` |
| `0x0sky` | human / personal identity | `#5597DA` | `#123878` | `#8BC5FF` |
| `aiaiaiai tech.` | organizational / corporate identity | `#906FC8` | `#3A2B72` | `#C2A1F2` |
| `0xda-market` | child organization / market ecosystem | `#93C482` | `#41704E` | `#BCE8A9` |
| `nilx.one` | child organization / protocol ecosystem | `#7765C6` | `#392F78` | `#B4A6F2` |

The **Primary** value is the canonical identity color. **Deep** is intended for low-light surfaces, shadows, borders, and dense graph regions. **Luminous** is intended for glow, highlights, active nodes, and emissive WebGPU effects.

## Relationship to the topology

```text
Core ☦️             warm gold
│
├─ 0x0sky           electric blue
│
└─ aiaiaiai tech.   cosmic violet
   │
   ├─ 0xda-market   living green
   │  ├─ core
   │  ├─ webapp-core
   │  └─ telegram-bot
   │
   └─ nilx.one      indigo violet
      └─ 0x1
```

Child systems and products inherit the identity family of their owning organization by default. They may use variations within that family when differentiation is necessary, but should not silently adopt another organization's canonical primary color.

## Usage rules

1. **Identity first.** The palette communicates which entity a node belongs to.
2. **Primary is canonical.** When only one color can be stored or exchanged, use the Primary value.
3. **Glow is not a new identity.** Emissive effects may interpolate from Primary toward Luminous without changing semantic ownership.
4. **Dark surfaces use Deep.** Deep values preserve identity on black and near-black backgrounds without relying on opacity alone.
5. **State is orthogonal.** `Stable | Recovering | Open`, health, warnings, errors, selection, and focus must be encoded independently from entity color.
6. **Core is distinct.** Gold belongs to `Core ☦️` and should not become a generic success, premium, or corporate accent.
7. **Inheritance is explicit.** `0xda-market/core`, `webapp-core`, and `telegram-bot` inherit the `0xda-market` green family. `nilx.one/0x1` inherits the `nilx.one` indigo family unless a product-specific palette is later declared.

## Rendering intent

The visual language is a dark cosmic field crossed by neural connections. Entity nodes should feel luminous rather than flat: a dense Deep center / boundary, the Primary identity hue, and restrained Luminous emission around active connections.

The palette is intentionally compatible with the ecosystem model in [`ORGANIZATION.md`](ORGANIZATION.md). `ORGANIZATION.md` defines **what the nodes are**; this file defines **how those nodes are visually identified**.

## Source

The initial values were sampled and normalized from the approved cosmic / human-neural-network concept image. They are design tokens rather than claims about exact physical pixel values; future calibration should preserve the same perceptual identities and update this document deliberately.
