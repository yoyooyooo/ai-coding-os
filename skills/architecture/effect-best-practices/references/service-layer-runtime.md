# Service, Layer, and Runtime

## Service

A Service is a capability contract available through Effect context. Keep the
interface cohesive and implementation-neutral. Do not expose SDK response types,
ORM models, host config, or React state through the capability contract.

Service methods usually return `Effect<A, E, R2>` where `E` is a stable expected
failure and `R2` contains only additional capabilities genuinely needed at call
time.

## Layer

A Layer constructs one or more Services and owns construction dependencies and
resource acquisition. It is a dependency graph, not a service locator and not a
business workflow.

```text
contract Service
  <- live Layer using transport/config/credentials
  <- fake Layer for deterministic tests
  <- profile composition selecting implementations
```

Keep vendor selection, environment loading, and live/fake choice in composition
roots. Avoid a reusable library that imports every vendor and switches on a
provider enum.

## Runtime

A Runtime executes Effects with a supplied context. Assign a lifetime owner:
request, command, route, tab, application, worker, or process.

Prefer:

```text
build closed Layer once
-> create runtime at host boundary
-> expose ordinary runtime-bound methods when consumers are not Effect-native
-> dispose runtime at host shutdown
```

Avoid creating a Runtime or rebuilding a live Layer inside each Query function,
HTTP handler, component render, or domain method.

## Runtime-Bound Facade

A package can use Effect internally while exposing an ordinary capability:

```ts
export type ProductClient = {
  readonly fetchProjection: (id: string) => Promise<Projection>
  readonly subscribe: (input: Input, handlers: Handlers) => Subscription
  readonly close: () => Promise<void>
}
```

The factory is the package composition root. It normalizes host dependencies,
builds a closed Layer, creates the Runtime, maps typed failures into public
errors, and exposes disposal.

Offer a separate Effect-native API only when callers are already Effect programs.
Do not force ordinary React/features to import Service keys and Layers.

## Environment Hygiene

Do not pass a “fat Context” or generic environment object through business code.
Depend on specific Services. Avoid one Service per file; organize around
capabilities and use cases.

## Test Replacement

Provide fake/test Layers for true external capabilities and resource boundaries.
Pure functions need ordinary unit tests, not fake Services. A memory repository
must match the live contract semantics if it is used as a conformance substitute;
a casual Map is not automatically equivalent.
