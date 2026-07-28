# Default Frontend Source Conventions

Use this portable default when a frontend project has no coherent adopted topology. It provides stable feature, host, and suffix semantics without requiring every file role.

## Default topology

```text
src/
  app/ or host/                 live composition, providers, router, global resources
  features/
    <feature>/
      ... only the roles the feature actually uses ...
  shared/                       stable cross-feature primitives/capabilities only
```

Use `app/` when the framework already establishes that convention. Use `host/` when the repository benefits from explicit runtime composition terminology. Do not create both unless they have distinct roles.
Keep each feature flat by default. Do not pre-create `components/`, `hooks/`, `api/`, `stores/`, or `models/` subdirectories; add a partition only when a stable local cluster or boundary earns it.

## Default suffix semantics

```text
.client.ts                 typed product capability facade; no React/query/store/view code
.client.<host>.live.ts     host-specific live implementation and resource construction
.client.fake.ts            explicit deterministic behavioral substitute
.query.ts                  remote projection and mutation lifecycle over an injected client
.store.ts                  local interaction state, not a server projection mirror
.realtime.ts               continuity, dedupe, gap/backfill, projection reduction
.mapper.ts                 pure conversion between named representations
.view-model.ts             pure composition for a surface
.page.tsx                  route/page container glue
.surface.tsx               Harnessable UI consuming a view model and callbacks
.fixture.ts                static sample data
.public.ts                 explicit feature public surface
```

Additional common roles:

```text
.model.ts                  pure frontend-specific data/value types when not already owned elsewhere
.policy.ts                 pure interaction/product decision local to the feature
.test.ts / .spec.ts        project runner convention; add semantic role before the test suffix
```

Do not create every file mechanically.

## Default import rules

- features do not deep-import another feature's private files;
- host selects live clients, Runtime, Query client, socket, workers, and global resources;
- components render and emit intent;
- query modules do not own local interaction state;
- stores do not mirror accepted server facts;
- realtime modules do not construct transports;
- `shared/` does not become a generic dumping ground;
- package and feature boundaries expose explicit exports.

## Default state map

```text
router       URL/navigation
query cache  remote projection and mutation lifecycle
local store  local interaction state
realtime     continuity and projection-update coordination
Effect       execution/resources/concurrency/failure
React        rendering and event adaptation
```

## Project override

Preserve a coherent local convention such as framework-defined `app/`, `routes/`, or `modules/`. Record only material differences and keep the state-role invariant.

## Example

See the [frontend feature tree](frontend-feature-tree-example.md).

## Related knowledge

- Use [Naming and feature boundaries](naming-and-feature-boundaries.md) for feature semantics.
- Use [Topology, composition, and hosts](topology-composition-and-hosts.md) for live resources.
- Use [State roles and ownership](state-roles-and-ownership.md) before adding state mechanisms.
- Use `$evolvable-application-architecture` for cross-application source grammar.
- Return to the [Frontend Architecture map](../SKILL.md).
