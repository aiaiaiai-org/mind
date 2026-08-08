# aiaiaiai tech. — organization topology

> The canonical human-readable description of identity, organizational relationships, systems, and the long-term corporate direction of the aiaiaiai tech. ecosystem.

## Core model

The model begins with `Core ☦️`: the soul / spiritual core. It is not a legal entity, company, GitHub account, or ownership object.

From that core, the ecosystem distinguishes a human identity and an organizational identity. `0x0sky` is the human owner and root identity. `aiaiaiai tech.` (`4xAI tech.`) is the organizational center for non-personal work and may evolve into the corporate parent.

```text
Core ☦️
│
├─ 0x0sky
│  human / personal identity
│  ├─ owner / root
│  └─ state: Stable | Recovering | Open
│
└─ aiaiaiai tech.
   organizational / corporate identity
   │
   ├─ 0xda-market
   │  ├─ core
   │  ├─ webapp-core
   │  └─ telegram-bot
   │
   └─ nilx.one
      └─ 0x1
```

This is a **native graph**, not a filesystem hierarchy. The diagram shows the primary direction of the model; nodes may also carry direct relationships that are not visually expanded here.

## Canonical relationships

- `Core ☦️` is the soul / spiritual core from which identity is described; it does not own assets or repositories.
- `0x0sky` is the human owner, founder, and root identity.
- `aiaiaiai tech.` is the organizational center for non-personal work and the intended future corporate parent.
- The relationship between `0x0sky` and `aiaiaiai tech.` is intentionally not defined as identity equality. They share the same core, while remaining distinct nodes so the organization can evolve independently.
- `0xda-market` has direct relationships to `aiaiaiai tech.` and `0x0sky`.
- `nilx.one` has direct relationships to `aiaiaiai tech.` and `0x0sky`.
- sibling organizations may collaborate directly without changing their parent relationship.
- personal projects remain attached to `0x0sky` and outside the corporate graph unless explicitly moved into it.

## 0xda-market systems

`0xda-market` currently exposes three primary active implementation nodes:

- [`core`](https://github.com/0xda-market/core) — market domain, API, persistence, authorization, pricing, and shared backend contracts;
- [`webapp-core`](https://github.com/0xda-market/webapp-core) — reusable web / Mini App application layer and user-facing market interface;
- [`telegram-bot`](https://github.com/0xda-market/telegram-bot) — Telegram integration and transport surface for the market.

These are systems of `0xda-market`, not sibling organizations of it. Repository names are used as canonical technical identifiers. The older `web-app` wording maps to the current `webapp-core` repository.

## nilx.one products

- `0x1` is a protocol product in the `nilx.one` namespace; it is not a separate company identity.

## GitHub representation

GitHub organizations are technically peer namespaces. GitHub does not provide a native parent/subsidiary hierarchy between organizations.

That limitation does not redefine this ecosystem. The organizational relationship is expressed through public profiles, `mind` repositories, manifests, documentation, repository references, and the graph rendered by ecosystem tooling.

> GitHub defines where repositories live. This document defines what the entities are to one another.

A consumer should therefore treat GitHub membership and namespace ownership as transport metadata, while treating the declared ecosystem graph as the canonical organizational model.

## Corporate direction

Today, `aiaiaiai tech.` is a GitHub organization and an operating organizational identity.

The intended long-term direction is for `aiaiaiai tech.` to become the legal corporate parent — initially through an appropriate Ukrainian legal entity and, as the organization grows, potentially a broader corporate structure capable of owning or governing subsidiaries, products, intellectual property, and shared infrastructure.

The exact future legal form is intentionally not encoded as a permanent technical invariant. Legal structure can evolve; the durable invariant is that `aiaiaiai tech.` is the organizational center for non-personal work.

## Identity boundaries

### Core ☦️

Soul / spiritual core. It precedes the technical and legal model and must not be interpreted as a legal person, repository owner, authentication principal, or corporate entity.

### 0x0sky

Human owner, founder, and root identity. Personal work originates here and does not automatically become corporate property merely because it appears in the wider ecosystem graph.

### aiaiaiai tech.

Organizational identity, coordination hub, and future corporate center. Shared engineering principles, organizational context, cross-project infrastructure, and future company-level governance belong here.

### 0xda-market

Child organization focused on digital commerce and market infrastructure. Its primary systems are `core`, `webapp-core`, and `telegram-bot`.

### nilx.one

Child organization / namespace for protocol and ecosystem work. `0x1` is a product within this branch, not an independent parent organization.

## Design principle

The structure should remain legible to both people and software:

```text
spiritual core:       Core ☦️
human root / owner:   0x0sky
organizational hub:   aiaiaiai tech.
children:             0xda-market, nilx.one
0xda-market systems:  core, webapp-core, telegram-bot
nilx.one product:     0x1
```

As new non-personal organizations are created, they should connect to `aiaiaiai tech.` as their organizational parent and to `0x0sky` as owner unless a later governance or legal document explicitly changes that relationship.

This file is the canonical human-readable source for that topology. Machine-readable manifests may encode the same relationships, but must not contradict them.
