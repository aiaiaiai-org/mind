# Identity

Canonical public organization identity for `aiaiaiai`.

## Canonical identity

- **type:** organization
- **id:** `aiaiaiai`
- **display name:** `aiaiaiai`
- **GitHub namespace:** `github.com/aiaiaiai-org`

The machine-readable source is [`identity.yaml`](identity.yaml). Its type and id must match `manifest.yaml -> mind.subject` exactly.

The canonical identity is provider-independent. `aiaiaiai-org` identifies the current GitHub namespace; it is not the organization id used by Mind Protocol.

Visual identity belongs to this module when canonical repository-local assets are explicitly versioned here. The current visual asset publication is [`visual-assets.yaml`](visual-assets.yaml), with production files under [`../../assets/visual/aiaiaiai/`](../../assets/visual/aiaiaiai/). Provider avatars remain presentation projections; they do not become identity authority.

The `1.0.0-rc.1` consumer intentionally does not bind `identity.visual_identity.primary_mark` yet. Asset publication can be prepared and validated independently; canonical Identity binding remains part of the post-stable-`1.0.0` rollout.

See [`../../docs/visual-identity.md`](../../docs/visual-identity.md) for provenance, production rules, and provider boundaries.

## Scope

- organization name and public identifiers;
- stable naming conventions shared across repositories;
- references to public domains and communication surfaces;
- canonical visual identity resources when explicitly versioned here.

## Exclusions

Do not store credentials, private personal profiles, access tokens, transient account state, or provider-derived presentation data as canonical identity facts.

## Dependencies

None.
