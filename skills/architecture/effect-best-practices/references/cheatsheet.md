# Effect Cheatsheet

## First Checks

```text
inspect installed version and d.ts
choose adoption level
keep pure core ordinary TypeScript
define only genuine capability Services
assign Runtime and Scope owners
separate expected failure, defect, and interruption
```

## Effect Type

`Effect.Effect<A, E, R>` means success value, expected error, and required
capabilities. Never swap the generic order.

## Promise

- `Effect.tryPromise` maps rejection into typed `E`.
- `Effect.promise` treats rejection as a defect; use only when intentional.
- Preserve AbortSignal/cancellation when bridging supported APIs.

## Service and Layer

- Service describes a capability, not a helper namespace.
- Layer constructs implementations and resources.
- Build provider/vendor choices at composition roots.
- Do not pass a fat Context through business functions.
- Give true external capabilities fake/test Layers; test pure functions directly.

## Running

- Run at executable/request/job/host boundaries or a runtime-bound facade.
- Avoid scattered `runPromise` and per-operation Layer construction.
- Dispose long-lived ManagedRuntime/resources at host shutdown.

## Resources and Concurrency

- Acquire and release in one Scope.
- Prefer structured child lifetimes; explicitly supervise daemons.
- Bound parallelism and buffers when load can grow.
- Define ordering, overflow, drain, cancellation, and health semantics.

## Error Policy

- Expected/recoverable -> typed error channel.
- Programming invariant violation -> defect unless deliberately translated.
- Cancellation -> interruption; do not silently relabel as ordinary failure.
- Map vendor errors at capability boundaries and public errors at transport/UI.

## Version Gate

- v3 and v4 syntax are separate adapters.
- Stable production default follows the project's installed stable major.
- v4 is a beta line unless the project explicitly opts in and pins it.
- Local typecheck wins over remembered examples or stale documentation.

## Common Smells

```text
Service per file or pure helper
Layer graph mirrors folders rather than capabilities
Effect.succeed around every pure value
runPromise inside domain/feature code
live Layer inside Query/component/handler loop
unbounded fork/Queue/parallelism
catchAll that erases defects and interruption
v3/v4 imports or APIs mixed in one example
```
