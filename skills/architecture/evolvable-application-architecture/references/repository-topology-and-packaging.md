# Repository Topology and Packaging

Use a Monorepo-first reference profile without turning Monorepo into doctrine.
The architecture must remain valid in a single-package repository or a
multi-repository deployment.

## Five boundaries

```text
repository boundary
  collaboration, version, and change-set boundary

package boundary
  compile/import/public-API boundary

deployable boundary
  process, lifecycle, fault, scaling, and release boundary

authority boundary
  final accepted-fact materialization boundary

data boundary
  transaction and consistency boundary
```

They may align, but they are never equivalent by default.

## Reference monorepo

```text
repo/
  apps/
    web/
    api/
    worker/
    migrator/        # only when a distinct runnable owner is justified
  packages/
    contracts/       # wire schemas or generated public contracts
    client/          # typed product client when multiple hosts consume it
    testkit/         # business-neutral reusable test primitives only
    <named-capability>/
  tooling/
  docs/
  specs/
```

`apps` contains runnable hosts. `packages` contains admitted compile/reuse
boundaries. Product authority modules do not automatically belong in
`packages`.

## Host-first, capability-local backend

```text
apps/api/src/
  host/
    api.main.ts
    api.config.ts
    api.composition.ts
    api.shutdown.ts
  modules/
    orders/
      order.public.ts
      order.wiring.ts
      ...private semantic files...
    billing/
  workflows/
    checkout/
```

`host/` owns runtime construction, config, resources, HTTP server, consumers,
and shutdown. It does not own product transitions.

A private module owns cohesive product state, invariants, commands, queries,
ports, projections, and nearby tests. Cross-module callers use the module's
public surface. Host composition may additionally use the wiring surface.

A workflow coordinates public commands/queries across modules. It cannot write
another module's storage directly.

## Module to package admission

Start in the host-private module. Promote only when one or more pressures are
real:

```text
multiple hosts need the capability
compile-time isolation materially reduces risk
package exports are needed to enforce public/private boundaries
independent ownership, trust, or security boundary exists
independent build/test/release has operational value
long-lived public API is deliberate
```

Package extraction does not grant authority. If both API and Worker import a
domain package, they still require an explicit allowed-writer model and shared
transaction/fencing semantics.

## Package to deployable admission

Promote only for deployment pressure:

```text
independent scaling
independent fault containment
independent lifecycle/resource ownership
network or trust boundary
independent release cadence
regulatory or security isolation
```

Do not use service extraction to compensate for unclear module ownership.

## Shared kernel admission

A small kernel may contain stable protocols such as:

```text
CommandContext
FactRef
IdempotencyKey
ExpectedVersion
CommitReceipt
```

It must not become a shared domain model, BaseEntity hierarchy, generic
repository framework, universal result type, or dependency dumping ground.

## Multiple writer warning

For each durable fact, project SSoT should record:

```text
fact
authority module
allowed writer hosts
formal entrypoints
transaction owner
authority epoch / fencing when relevant
forbidden direct writers
```

A Worker may issue a command without becoming the fact authority. If multiple
hosts can materialize one authority, prove idempotency, concurrency, transaction
ownership, and old-writer fencing explicitly.
