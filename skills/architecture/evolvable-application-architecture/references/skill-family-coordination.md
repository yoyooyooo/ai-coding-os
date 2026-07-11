# Architecture Skill Family Coordination

Use the family as one knowledge system with separate selection units. The first
three are doctrine skills; `effect-api-app-kit` is an executable profile.

## Ownership

```text
evolvable-application-architecture
  fact authority, consistency, ports, transactions, module/process boundaries,
  composition, forward migration, replaceability, and evidence

frontend-architecture
  frontend intent/projection model, state ownership, route/feature topology,
  client/query/store/realtime boundaries, React adapters, and UI harnesses

effect-best-practices
  Effect adoption, Service, Layer, Scope, Runtime, Stream, Queue, typed errors,
  resources, tests, and version-specific implementation judgment

effect-api-app-kit
  managed Effect Node HttpApi templates, generation, registries, manifests,
  exact profile pins, and compile/HTTP verification
```

An executable profile implements doctrine; it does not redefine authority.
Project SSoT, ADRs, schemas/protocols, lockfiles, installed declarations, and
compiler/test evidence remain more authoritative than generic defaults.

## Selection

| Task | Lead | Supporting |
|---|---|---|
| System authority, transaction, storage, migration | evolvable application | frontend/effect as needed |
| Frontend state, feature topology, realtime projection | frontend | evolvable application for cross-system authority |
| Effect API, runtime, Scope, Layer, Stream, typed errors | effect | evolvable application/frontend for boundaries |
| Scaffold or extend managed Effect HttpApi app | kit | effect; evolvable application if domain design is open |
| React + Effect runtime injection | frontend | effect |
| Effect backend architecture before generation | evolvable application | effect |
| Full-stack architecture audit | evolvable application | frontend + effect; kit only for approved implementation |

## Conflict Resolution

1. Keep project product facts and public contracts unchanged unless explicitly
   asked to change them.
2. Use evolvable-application doctrine for authority, consistency, transactions,
   migration, and claim ceilings.
3. Use frontend doctrine for browser/UI ownership and topology.
4. Use Effect doctrine only after an adoption/version decision exists.
5. Use the kit only after those decisions; generated convenience never
   overrides an authority or transaction boundary.
6. If a lower-level mapping conflicts with a higher-level invariant, change the
   implementation profile rather than the invariant.
