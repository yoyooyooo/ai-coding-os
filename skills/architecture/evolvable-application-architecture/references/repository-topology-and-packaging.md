# Repository Topology and Packaging

Repository shape is a projection of semantic and operational pressure.

```text
version-control repository
workspace / aggregate root
source module
compilation and public-API unit
runnable host
independently deployed process
fact authority and consistency domain
data store / schema boundary
```

These boundaries may coincide, but none implies another.

## Default

Start with the repository structure already accepted by the project. Within it,
prefer private modules and explicit host composition. Do not introduce a
Monorepo, workspace package, crate, or microservice merely to make the diagram
symmetrical.

## Promotion Signals

Promote a module to a compilation/package unit when one or more durable pressures
exist:

```text
enforced dependency direction
independent public API or SemVer
real reuse by multiple hosts
separate ownership or release cadence
build isolation or toolchain boundary
```

Promote to a deployable when pressure is operational:

```text
independent scaling or failure isolation
trust/security boundary
separate runtime/resource lifecycle
independent deployment or rollback
network protocol already required by product/organization constraints
```

## Monorepo Profile

A Monorepo is a reusable repository topology profile, not the generic doctrine.
When selected, keep repository, package, deployable, fact Authority, and data
boundaries explicit. Package sharing does not grant writer Authority; an app
entry does not become product logic.

## Polyglot Workspaces

Use the same semantic map across languages, then project locally:

```text
TypeScript package exports and project references
Rust Cargo workspace crates and visibility
JVM modules/packages
Go modules/internal packages
```

Generated wire contracts may connect ecosystems. They are compatibility
boundaries, not a shared domain Authority.
