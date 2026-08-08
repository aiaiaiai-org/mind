# aiaiaiai tech. mind

> A versioned organization context repository for humans and AI systems.

This repository is an integration fork of the vendor-independent [`mind`](https://github.com/0x0sky/mind) baseline. It specializes the baseline contract as the organization mind for `aiaiaiaitech` while keeping reusable framework concerns upstream.

## Organization identity

- **Organization:** `aiaiaiai tech.` / `4xAI tech.`
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** parent organization and organizational hub for non-personal work
- **Current form:** GitHub organization and operating identity
- **Long-term direction:** legal corporate parent
- **Child organizations / namespaces:** [0xda-market](https://github.com/0xda-market), [nilx.one](https://github.com/nilx-one)

The canonical topology is defined in [`ORGANIZATION.md`](ORGANIZATION.md). It treats the ecosystem as a graph: `0x0sky` is the ownership root, `aiaiaiai tech.` is the organizational center, and each child organization has direct relationships to both.

```text
             0x0sky
            /  |  \
           v   v   v
      aiaiaiai tech.
        /         \
       v           v
0xda-market     nilx.one
                   |
                   v
                  0x1
```

GitHub represents these organizations as technically independent peer namespaces. That implementation detail does not define their ownership or organizational relationships.

Personal projects owned by `0x0sky` remain outside the corporate graph unless explicitly declared otherwise.

## Purpose

The repository is the canonical source for stable organization-wide context that should be shared across projects without being duplicated in every repository.

It intentionally excludes secrets, private personal context, repository-local implementation details, and transient operational state.

## Composition

```text
OrganizationMind
├── ORGANIZATION.md
├── manifest.yaml
├── schema/
│   └── mind.schema.json
└── modules/
    ├── identity/
    ├── governance/
    ├── engineering/
    ├── portfolio/
    └── decisions/
```

Default modules:

- `identity` — canonical public organization identity and naming;
- `governance` — durable ownership, review, and publication rules;
- `engineering` — organization-wide engineering contracts;
- `portfolio` — stable project and product index.

Optional module:

- `decisions` — cross-repository decision records.

## Integration model

- `0x0sky/mind` remains the neutral upstream contract.
- `aiaiaiaitech/mind` evolves independently as the concrete parent-organization mind.
- `ORGANIZATION.md` is the canonical human-readable source for ecosystem ownership and topology.
- Child organization minds reference this organization as their parent while remaining independently versioned repositories.
- Neutral improvements may be contributed upstream as isolated commits or versioned contract changes.
- Organization-specific content must not be pushed upstream.
- Repository-specific implementation remains canonical in the owning repository and is referenced from here.

## Change policy

1. Work on a focused branch.
2. Validate `manifest.yaml` against `schema/mind.schema.json`.
3. Open a draft pull request.
4. Require green checks before publication.
5. Merge or release only after explicit review and authorization.

## Visibility

This repository may be public. Never commit secrets, credentials, private health data, access tokens, private personal profiles, or transient infrastructure state.
