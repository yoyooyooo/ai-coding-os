# Naming and Feature Boundaries

Frontend names should reveal the product capability, state role, and host responsibility. A visual component collection is not automatically a feature.

## Feature naming

Prefer user work or product capability:

```text
orders
case-review
identity-access
exception-resolution
```

Avoid architecture or page-only names as top-level product boundaries:

```text
components
screens
services
common
core
widgets
```

A `shared/` area is acceptable only for stable cross-feature primitives or capabilities with clear ownership.

## Public surface

A feature may expose `<feature>.public.ts` when another feature or host needs a stable contract. Keep exports deliberate. Do not use wildcard barrels to make private files appear public.

## Generic bucket test

A generic directory is a problem when:

```text
callers cannot predict its scope
unrelated imports accumulate
ownership is unclear
private and public APIs are mixed
it exists because no semantic owner was named
```

## Naming dimensions

Use the portable TypeScript grammar:

```text
kebab-case within one semantic segment
dots between semantic dimensions
```

Examples:

```text
order.client.ts
order.query.ts
order.realtime.ts
order.view-model.ts
order-list.surface.tsx
checkout.page.tsx
```

## Mapping and view models

Name conversions by source and target when ambiguity exists:

```text
order.wire-to-projection.mapper.ts
order.projection-to-view-model.mapper.ts
```

Do not hide important domain conversion in `utils.ts`.

## Renaming

A misleading name is an architecture defect. Rename early while the public compatibility surface is small. External names may require aliases and migration; internal names should not remain wrong for fear of change.

## Related knowledge

- Use [Default frontend source conventions](default-frontend-source-conventions.md) for canonical suffixes.
- Use [State roles and ownership](state-roles-and-ownership.md) when `state`, `model`, or `store` hides several meanings.
- Use [Topology, composition, and hosts](topology-composition-and-hosts.md) when a feature may need a package or host boundary.
- Use `$product-definition` for canonical product language.
- Return to the [Frontend Architecture map](../SKILL.md).
