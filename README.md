# aiaiaiai tech. mind

> A versioned organization context repository for humans and AI systems.

This repository is an integration fork of the vendor-independent [`mind`](https://github.com/0x0sky/mind) baseline. It specializes the baseline contract as the organization mind for `aiaiaiaitech` while keeping reusable framework concerns upstream.

## Organization identity

- **Organization:** `aiaiaiai tech.` / `4xAI tech.`
- **Owner:** [0x0sky](https://github.com/0x0sky)
- **Role:** parent organization for non-personal work
- **Current form:** GitHub organization
- **Intended legal form:** Ukrainian limited liability company (ТОВ)
- **Child organizations / namespaces:** [0xda-market](https://github.com/0xda-market), [nilx.one](https://github.com/nilx-one)

The parent-child model is canonical ecosystem context, not a GitHub-native hierarchy. GitHub represents the organizations as technically independent peer namespaces.

```text
0x0sky
└── aiaiaiai tech. / 4xAI tech.
    ├── 0xda-market
    └── nilx.one
        └── 0x1
```

Personal projects owned by `0x0sky` remain outside this corporate hierarchy unless explicitly declared otherwise.

## Purpose

The repository is the canonical source for stable organization-wide context that should be shared across projects without being duplicated in every repository.

It intentionally excludes secrets, private personal context, repository-local implementation details, and transient operational state.

## Composition

```text
OrganizationMind
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
