# aiaiaiai tech. — organization topology

> The canonical human-readable description of ownership, organizational relationships, and the long-term corporate direction of the aiaiaiai tech. ecosystem.

## Core model

`aiaiaiai tech.` (`4xAI tech.`) is the organizational center of all non-personal work in this ecosystem.

`0x0sky` is the human owner and root identity. `aiaiaiai tech.` is the organization through which non-personal projects, products, and future companies are grouped. Child organizations maintain direct relationships with both the parent organization and the owner; they are not merely nested folders in a tree.

```text
                         0x0sky
                       owner / root
                      /      |      \
                     /       |       \
                    v        v        v
             aiaiaiai tech. <------> child organizations
               parent / hub            /       \
                    ^                 /         \
                    |                v           v
                    +---------- 0xda-market    nilx.one
                                      \          /
                                       \        /
                                        products
```

The useful mental model is therefore a **native graph**, not a strict filesystem hierarchy.

## Canonical relationships

- `0x0sky` owns and originates the ecosystem.
- `aiaiaiai tech.` is the parent organization and primary organizational hub for non-personal work.
- `0xda-market` has a direct relationship to `aiaiaiai tech.` and to `0x0sky`.
- `nilx.one` has a direct relationship to `aiaiaiai tech.` and to `0x0sky`.
- `0x1` is a protocol product in the `nilx.one` namespace; it is not a separate company identity.
- sibling organizations may collaborate directly without changing their parent relationship.
- personal projects remain attached to `0x0sky` and outside the corporate graph unless explicitly moved into it.

In graph terms, `aiaiaiai tech.` is the **organizational center** and `0x0sky` is the **ownership root**. Both are first-class nodes. Neither relationship should be reduced to GitHub repository ownership alone.

## GitHub representation

GitHub organizations are technically peer namespaces. GitHub does not provide a native parent/subsidiary hierarchy between organizations.

That limitation does not redefine this ecosystem. The organizational relationship is expressed natively through public profiles, `mind` repositories, manifests, documentation, repository references, and the graph rendered by ecosystem tooling.

The rule is simple:

> GitHub defines where repositories live. This document defines what the organizations are to one another.

A consumer should therefore treat GitHub membership and namespace ownership as transport metadata, while treating the declared ecosystem graph as the canonical organizational model.

## Corporate direction

Today, `aiaiaiai tech.` is a GitHub organization and an operating identity for the ecosystem.

The intended long-term direction is for `aiaiaiai tech.` to become the legal corporate parent — initially through an appropriate Ukrainian legal entity and, as the organization grows, potentially a broader corporate structure capable of owning or governing subsidiaries, products, intellectual property, and shared infrastructure.

The exact future legal form is intentionally not encoded as a permanent technical invariant. Legal structure can evolve; the durable invariant is that `aiaiaiai tech.` is the parent organizational identity for non-personal work.

## Identity boundaries

### 0x0sky

Human owner, founder, and root identity. Personal work originates here and does not automatically become corporate property merely because it appears in the wider ecosystem graph.

### aiaiaiai tech.

Parent organization, coordination hub, and future corporate center. Shared engineering principles, organizational context, cross-project infrastructure, and future company-level governance belong here.

### 0xda-market

Child organization focused on digital commerce and market infrastructure. It keeps its own repositories, product contracts, and operational context while remaining connected to the parent and owner.

### nilx.one

Child organization / namespace for protocol and ecosystem work. `0x1` is a product within this branch, not an independent parent organization.

## Design principle

The structure should remain legible to both people and software:

```text
ownership root:       0x0sky
organizational hub:   aiaiaiai tech.
children:             0xda-market, nilx.one
product:              nilx.one / 0x1
```

As new non-personal organizations are created, they should connect to `aiaiaiai tech.` as their parent and to `0x0sky` as owner unless a later governance or legal document explicitly changes that relationship.

This file is the canonical human-readable source for that topology. Machine-readable manifests may encode the same relationships, but must not contradict them.
