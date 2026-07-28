# Default Repository Profile

Use this profile when a greenfield or weakly structured application has no coherent adopted topology. It is a portable default, not a universal mandate.

## Small single-host TypeScript application

```text
src/
  host/
    <host>.main.ts
    <host>.config.ts
    <host>.composition.ts
    <host>.shutdown.ts
  modules/
    <capability>/
      ... semantic dot files ...
  workflows/                    # only for real cross-capability orchestration
tooling/                        # project-owned mechanical tools
docs/
```

## Multi-host or workspace application

```text
apps/
  <host>/
    src/
      host/
        <host>.main.ts
        <host>.config.ts
        <host>.composition.ts
        <host>.shutdown.ts
      modules/
        <capability>/
      workflows/                # conditional
packages/                       # conditional
  <package>/
tooling/
docs/
```

Typical hosts:

```text
api
worker
scheduler
cli
web
migration
```

## Directory semantics

### `host/`

Executable composition, environment decoding, resource construction, startup, and shutdown.

### `modules/<capability>/`

Private capability clusters organized by product responsibility. Keep semantic dot files flat inside the capability by default; add a child directory only after a durable sub-capability, ownership, security, lifecycle, or navigation boundary appears. They may expose one explicit public surface when cross-module use is stable.

### `workflows/<workflow>/`

Only for genuine cross-capability orchestration that does not belong to one capability. Do not use it as a generic application layer.

### `packages/`

Admit after compile, stable reuse, ownership, public API, trust, or distribution pressure. A workspace package is not required merely because several files exist.

### `tooling/`

Repository-owned scripts, architecture checks, generators, migrations, and mechanical utilities. Tools do not become semantic owners.

## Dependency direction

```text
host composition
  -> capability public surfaces and live implementations

transport adapters
  -> use cases

use cases
  -> model, policy, Ports, transaction contracts

live adapters
  -> external SDKs, database, filesystem, network

model/policy
  -> ordinary language/runtime libraries only
```

No ordinary capability imports the host composition root.

## Public API

Keep module internals private. Add `<capability>.public.ts` only when another module or host needs a stable surface. Reject deep private imports with package exports, lint/import rules, project references, or architecture tests when pressure justifies mechanical enforcement.

## Monorepo boundary

Use a workspace/Monorepo as the portable default once the product has multiple real hosts or earned packages. A small single-host service may remain one package. Existing repositories remain authoritative. Do not create packages merely to imitate a Monorepo diagram.

## Examples

- [Minimal application tree](minimal-application-tree-example.md)
- [TypeScript capability tree](typescript-capability-tree-example.md)

## Related knowledge

- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) for filenames.
- Use the [source topology Standard template](../templates/source-topology-and-naming.md) when the convention becomes project-binding.
- Use [Changeability, modularity, and repository shape](changeability-modularity-and-repository-shape.md) before promoting packages or deployables.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for host ownership.
- Use `$docs-governance` for `docs/` topology.
- Return to the [EAA map](../SKILL.md).
