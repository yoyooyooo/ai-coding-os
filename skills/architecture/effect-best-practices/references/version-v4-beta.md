# Version Adapter: Effect v4 Beta

Use only when the project explicitly installs or evaluates Effect v4 beta. Beta
APIs can change between releases: pin an exact version, inspect local `.d.ts`,
and compile every promoted example.

The bundled fixture is pinned to `effect@4.0.0-beta.84`; it demonstrates one
known-compatible shape, not “latest forever.”

## Confirmed Fixture Idioms

```text
Context.Service<Shape>("Key")
class X extends Context.Service<X, Shape>()("X") {}
Layer.succeed(Service, implementation)
Layer.effect(Service, effectProducingImplementation)
ManagedRuntime.make(closedLayer)
Scope.make / Scope.provide / Scope.use / Scope.close
```

`Layer.effect` construction runs in the Layer scope and removes the `Scope`
requirement from its output requirements. `ManagedRuntime.make` requires a
closed Layer with no remaining construction dependencies.

## Migration Discipline

- Do not mix v3 `Context.Tag` examples and v4 `Context.Service` examples in one
  file unless it is a deliberate compatibility adapter.
- Characterize errors, interruption, Scope/finalizer behavior, Layer sharing,
  Schema decoding, platform APIs, and build output before cutover.
- Pin beta dependencies exactly; avoid floating `beta` ranges in reproducible
  projects.
- Remove old-major bridges after callers and fixtures migrate.

Run `npm install && npm run typecheck:examples` in this skill source to validate
both bundled v3 and v4 examples.
