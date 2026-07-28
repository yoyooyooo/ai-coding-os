# Changeability, Modularity, and Repository Shape

Modularity exists to keep independent changes independent. A directory, package, crate, repository, host, or deployable is one possible enforcement surface; none is the definition of a module by itself.

## Change axes

Ask what changes independently:

```text
product rule
fact authority
external provider
public contract
resource lifetime
security or trust boundary
team ownership
build/reuse/public API
runtime scaling or failure
```

A boundary is strong when it contains one or more real axes without forcing unrelated changes through it.

## Boundary strength

```text
lexical cluster
private source module/directory
explicit public surface
package or crate compilation boundary
runnable host
independently deployed/failing boundary
trust or privilege isolation
```

Each promotion is independent. More layers are not automatically more mature.

## Cohesion and coupling

A module should contain knowledge that changes for the same reason. Dependencies should be few, explicit, and expressed in stable domain or capability terms rather than internal data shapes.

Two similar pieces of code may remain separate when they represent different knowledge. Different-looking representations may need one authority when they express the same rule.

## Monorepo and multi-repository

A monorepo can improve discovery, atomic changes, and shared tooling. Multiple repositories can enforce ownership, release, and trust boundaries. Choose based on real collaboration and operational pressure.

Do not split repositories merely to imitate service architecture. Do not keep independent trust or deployment units together merely for convenience.

## Package admission

Promote a private module to a package when one or more are durable:

```text
several hosts need a stable public API
independent ownership or review policy
compile/build isolation
external distribution or compatibility
independent trust boundary
stable reuse with meaningful dependency direction
```

File count alone is not enough.

## Generic shared code

`shared`, `common`, and `utils` often hide unresolved ownership. Admit shared capability only when callers understand its stable responsibility and public contract.

## Architecture tests

Mechanical checks can protect import direction, public exports, forbidden dependencies, or package boundaries. They support the architecture claim; they do not prove product correctness.

## Related knowledge

- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) for files and directories.
- Use [Default repository profile](default-repository-profile.md) for greenfield shape.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for semantic dependency boundaries.
- Use [Forward evolution and migration](forward-evolution-and-migration.md) before splitting or moving authority.
- Return to the [EAA map](../SKILL.md).
