# Source Topology and Naming

## Scope

This Standard records the project-adopted source grammar. It should describe only rules that currently bind work.

## Repository Topology

```text
<current application/workspace tree>
```

Default roles when applicable:

```text
apps/<host>/src/host/          executable composition and lifetime
apps/<host>/src/modules/       product capability modules
apps/<host>/src/workflows/     conditional cross-capability orchestration
packages/                      conditional compile/reuse/public-API boundaries
tooling/                       repository-owned mechanical tools
docs/                          durable project knowledge
```

## Filename Grammar

```text
segment case: kebab-case
semantic dimension separator: dot
order: subject -> operation/facet -> responsibility -> provider/host qualifier
```

Adopted examples:

```text
order.submit.command.ts
order.command-context.ts
order.submit.use-case.ts
order.repository.port.ts
order.repository.postgres.live.ts
order.http.handlers.ts
api.composition.ts
```

## Dependency Direction

```text
model / policy
  must not import transport, database, provider SDK, live adapter, or process environment

use case
  may depend on model, policy, Port, and transaction contracts
  must not import live implementations or framework handlers

Port
  must not expose provider SDK or ORM types

transport handler
  decode -> map -> call use case -> map result
  must not write accepted facts directly

host composition
  selects live implementations and owns resources
  must not become product transition logic
```

## Public Surfaces

- `<capability>.public.ts` or the ecosystem-equivalent is the normal cross-module surface when one is needed.
- Deep private imports are `<allowed/prohibited and how checked>`.
- Package/crate promotion requires `<project pressure>`.

## Ecosystem Extensions

- Frontend: `<local path or $frontend-architecture defaults>`
- Effect: `<local path or $effect-best-practices defaults>`
- Rust or other ecosystem: `<local idiom>`

## Tests and Generated Material

- Focused tests: `<co-located or local convention>`
- Cross-capability/system tests: `<tests/ or local convention>`
- Generated source: `<generated/ or suffix plus regeneration command>`
- Data migrations: `<owning store/framework path and ordering>`

## Deliberate Exceptions

- `<exception>` — reason, scope, protected invariant, and removal/review condition.
