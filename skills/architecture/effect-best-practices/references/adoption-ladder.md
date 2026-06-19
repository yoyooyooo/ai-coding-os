# Adoption Ladder

Choose the lowest level that solves current pressure. Promotion is allowed;
starting at the top without pressure increases type, runtime, and migration cost.

## Level 0 — Plain TypeScript

Use ordinary functions, Promise, AbortSignal, and explicit dependency parameters
when the workflow is small, resources are trivial, and tests remain clear.

Evidence to stay here:

```text
few dependencies
simple error model
no long-lived resource
no structured concurrent workflow
no repeated retry/timeout boilerplate
```

## Level 1 — Effect at an Edge

Wrap unstable Promise/SDK/IO boundaries with `Effect.tryPromise`, typed errors,
timeout, retry, or observability, while the rest of the module remains ordinary
TypeScript.

Good for one capability adapter or command handler.

## Level 2 — Capability Services and Layers

Introduce Service/Layer when multiple use cases share replaceable capabilities,
construction dependencies, fake implementations, or consistent error policy.
Keep domain rules and mappers pure.

## Level 3 — Scoped or Concurrent Subsystem

Use Scope, Fiber, Stream, Queue, Schedule, Semaphore, or related primitives when
the subsystem owns long-lived resources, background loops, fanout, bounded
parallelism, cancellation, or backpressure.

Define:

```text
scope owner
shutdown/drain policy
queue capacity and overflow policy
concurrency budget
ordering and idempotency
observability and health
```

## Level 4 — Application Runtime

Use Effect as the application execution skeleton when most entry points and
capabilities benefit from one Layer graph, shared runtime context, structured
lifecycle, and unified tests.

The host still owns the Runtime and final disposal. Product authority remains in
application/domain modules; it does not move into Layer construction.

## Promotion Signals

Promote one level when repeated code or failure evidence shows:

```text
inconsistent error mapping
unreleased resources
uncancellable background work
manual dependency plumbing across many use cases
unbounded Promise concurrency
hard-to-fake platform/SDK dependencies
flaky time/retry tests
```

## Demotion Signals

Simplify when:

```text
Services wrap pure one-line helpers
Layers mirror directory structure without replacement pressure
business APIs expose huge R environments
runPromise/provide appears in every function
React features import internal Service keys only to fetch data
Effect types obscure a stable ordinary public facade
```
