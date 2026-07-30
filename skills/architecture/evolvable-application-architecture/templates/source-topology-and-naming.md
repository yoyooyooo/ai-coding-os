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

## Role-to-file policy

```text
semantic roles are distinct
physical files are pressure-earned
role/suffix lists are vocabularies, not manifests
```

Default co-location policy:

- Command, Outcome, Receipt, and local Policy may stay in the owning `*.use-case.ts` while small and private.
- Transport contract, decoder, and mapper may stay beside the handler while local and trivial.
- A fake, public surface, wiring file, transaction capability, or idempotency capability is added only after a real consumer, test, consistency, reuse, lifecycle, navigation, or mechanical-enforcement pressure appears.
- Transaction naming follows the consistency scope; idempotency naming follows the operation/replay scope. Neither is generated once per module by default.

Project-specific extraction pressure: `<independent change/reuse/public contract/test/lifetime/trust/navigation/tooling rules>`.

## Filename Grammar

```text
segment case: kebab-case
semantic dimension separator: dot
order: subject -> operation/facet -> responsibility -> provider/host qualifier
```

Adopted examples:

```text
order.submit.use-case.ts
order.repository.port.ts
order.repository.postgres.live.ts
order.http.handlers.ts
api.composition.ts
```

Conditional examples when earned:

```text
order.submit.command.ts
order.submit.outcome.ts
order.submit.receipt.ts
order-commit.transaction.port.ts
order-submit.idempotency.port.ts
```

## Dependency Direction

```text
model / policy
  must not import transport, database, provider SDK, live adapter, or process environment

use case
  may depend on model, policy, Port, and consistency-scope contracts
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

## Capability contract projection

- Application capability contracts use `<ordinary Port / Effect Service / project idiom>`.
- One capability has one canonical contract by default.
- A parallel Port and Effect Service require `<distinct consumer, compatibility, or trust pressure>` and an explicit translation boundary.
- Provider-qualified live files may construct the selected implementation or Effect Layer.

## Public Surfaces

- `<capability>.public.ts` or the ecosystem-equivalent is the normal cross-module surface only after one is needed.
- Deep private imports are `<allowed/prohibited and how checked>`.
- Package/crate promotion requires `<project pressure>`.

## Consistency and idempotency

- Transaction scope: `<product invariant / participants / mechanism>`.
- Idempotency scope: `<command type / actor-tenant-resource scope / key / fingerprint / retention / replay semantics>`.
- Database constraints and migrations that protect accepted facts: `<paths and checks>`.

## Ecosystem Extensions

- Frontend: `<local path or $frontend-architecture defaults>`
- Effect: `<Effect-specific Service/Layer/Runtime/mechanism overlay; not a second application grammar>`
- Rust or other ecosystem: `<local idiom>`

## Tests and Generated Material

- Focused tests: `<co-located or local convention>`
- Cross-capability/system tests: `<tests/ or local convention>`
- Generated source: `<generated/ or suffix plus regeneration command>`
- Data migrations: `<owning store/framework path and ordering>`

## Deliberate Exceptions

- `<exception>` — reason, scope, protected invariant, and removal/review condition.
