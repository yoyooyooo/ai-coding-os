# Architecture Skill Coordination

## Ownership

`agentic-architecture` decides authority, module/port boundaries, transactions,
composition profiles, migrations, and evidence ceilings.

`frontend-architecture` decides frontend state ownership, route/feature topology,
client/query/store/realtime boundaries, React adapters, and UI harnesses.

`effect-best-practices` maps selected capabilities and workflows into Effect
Service, Layer, Runtime, Scope, Stream, Queue, typed error, and test idioms.

## Mapping Rule

Do not infer architecture from Effect syntax:

```text
Context.Service does not automatically mean domain boundary
Layer does not automatically mean composition root
Stream does not automatically mean business event authority
Queue does not automatically mean durable work queue
ManagedRuntime does not automatically mean application singleton
```

Establish the semantic owner first, then choose the Effect primitive.

## Recommended Module Shape

```text
<capability>.contract.ts       ordinary public types when cross-boundary
<capability>.service.ts        Service key and Effect-native contract
<capability>.live.ts           live Layer/adapter
<capability>.fake.ts           deterministic replacement when justified
<use-case>.flow.ts             Effect orchestration
<subject>.domain.ts            pure decisions and data
<profile>.runtime.ts           closed Layer / Runtime assembly
```

These suffixes are examples, not mandatory directory law. Follow project naming
and avoid mechanically creating empty layers.

## Package Boundary

A package that uses Effect internally should normally export:

```text
ordinary capability contract/factory
normalized public errors
subscription/resource close contract
optional explicit Effect-native entry point
```

Keep internal Service keys, Layers, and transports private unless the package is
intentionally an Effect-native library.
