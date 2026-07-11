# Architecture Skill Family Coordination

Use the family as one knowledge system with separate selection units. The first
three are doctrine skills; `effect-api-app-kit` is an executable profile.

## Ownership

```text
evolvable-application-architecture
  authority, ports, transactions, module/process boundaries, composition,
  forward migration, replaceability, and evidence

frontend-architecture
  frontend intent/projection model, state ownership, route/feature topology,
  client/query/store/realtime boundaries, React adapters, and UI harnesses

effect-best-practices
  Effect adoption, Service, Layer, Scope, Runtime, Stream, Queue, typed errors,
  resources, tests, and version-specific implementation judgment

effect-api-app-kit
  managed Effect Node HttpApi v3/v4 templates, generation, registries, manifests,
  exact profile pins, and compile/HTTP verification
```

An executable profile implements doctrine; it does not redefine authority.
Project SSoT, ADRs, schemas/protocols, lockfiles, installed declarations, and
compiler/test evidence remain more authoritative than generic defaults.

## Selection

| Task | Lead | Supporting |
|---|---|---|
| System authority, transaction, storage, migration | agentic | frontend/effect as needed |
| Frontend state, feature topology, realtime projection | frontend | agentic for cross-system authority |
| Effect API, runtime, Scope, Layer, Stream, typed errors | effect | agentic/frontend for surrounding boundaries |
| Scaffold or extend a managed Node HttpApi app | kit | effect; agentic if domain/transaction design is open |
| React + Effect runtime injection | frontend | effect |
| Effect backend architecture before generation | agentic | effect |
| Full-stack architecture audit | agentic | frontend + effect; kit only for approved implementation |

## Conflict Resolution

1. Keep project product facts and public contracts unchanged unless explicitly
   asked to change them.
2. Use agentic doctrine for authority, consistency, transactions, and migration.
3. Use frontend doctrine for browser/UI ownership and topology.
4. Use Effect doctrine only after an adoption/version decision exists.
5. Use the kit only after those decisions; generated convenience never overrides
   an authority or transaction boundary.
6. If a lower-level mapping conflicts with a higher-level invariant, change the
   implementation profile rather than the invariant.
