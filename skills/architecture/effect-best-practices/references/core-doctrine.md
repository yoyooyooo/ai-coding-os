# Core Doctrine

## Effect's Role

Effect is an execution model for programs that can succeed, fail, require
capabilities, run concurrently, and own resources. It is especially useful for:

```text
typed failure and recovery
capability dependency injection
resource acquisition/release
structured cancellation and concurrency
retry/timeout/scheduling
streams, queues, and backpressure
repeatable tests with controlled dependencies/time
```

Effect is not automatically:

```text
a domain model
a module boundary
a reason to create a Service
a replacement for frontend state ownership
a transaction authority
a requirement for every async function
```

Use `evolvable-application-architecture` to decide where authority, ports, transactions, and
composition boundaries exist. Then map real capability boundaries into Effect.

## Pure Core, Effectful Shell

Keep deterministic calculation as ordinary functions:

```text
parse/normalize/map/rank/reduce
state-transition decision
schema-independent derivation
view-model calculation
id/reference composition
```

Use Effect around operations whose execution semantics matter:

```text
network/filesystem/database/provider calls
resource ownership
cancellation/deadline/retry
concurrency and backpressure
observability context
host entry points and workers
```

A pure function may return a domain result, Option/Either, or a typed data error.
Lift it into Effect at the orchestration boundary when that improves composition.
Do not wrap every value in `Effect.succeed` for stylistic uniformity.

## Capability Test

Create a Service when most of these are true:

- callers depend on a capability rather than one implementation;
- live and fake/test implementations are useful;
- construction has dependencies or resources;
- errors/lifecycle deserve a stable contract;
- the capability crosses process, SDK, storage, platform, or trust boundaries.

Do not create a Service for a tiny pure helper, a local data transform, or a
class that has no meaningful replacement or lifecycle pressure.

## Execution Ownership

Run Effects at an owned edge:

```text
CLI/server/worker main
request or job adapter
app composition root
runtime-bound package facade
React host bridge designed for Effect execution
```

Avoid scattered `Effect.runPromise` in business modules. Build a closed Layer
once when lifetime permits; run many programs through the owned Runtime; dispose
it when the host ends.

## Architecture Family

```text
evolvable-application-architecture       decides authority and consistency
frontend-architecture      decides browser/UI state and topology
effect-best-practices      implements chosen boundaries with Effect
```

A lower-level Effect convenience never overrides a higher-level authority,
transaction, visibility, or lifecycle rule.
