# Mechanism Selection

> **Use Effect for Execution Pressure, Not Architectural Decoration.** Choose the smallest mechanism that clarifies the current capability, failure, resource, concurrency, cancellation, or dependency problem.

Choose Effect mechanisms from the pressure they solve. Do not use Effect to create uniform visual architecture.

## Ordinary function or Promise

Prefer ordinary TypeScript when logic is:

```text
pure or local
simple to compose
not resource-owning
not meaningfully improved by typed failure or interruption
not shared as a replaceable capability
```

A `Promise` may be sufficient for one straightforward asynchronous boundary with conventional error and lifetime needs.

## Effect value

Use Effect when a computation benefits from explicit:

```text
typed expected failure
dependency requirements
structured resources
cancellation/interruption
retry, timeout, scheduling, or concurrency
Clock/random/config substitution
compositional observability
```

## Service

Create a Service when callers need a stable capability with replaceable implementations or dependency injection. A Service should own meaningful semantics, not merely wrap one helper for symmetry.

## Layer

Use Layer to construct capability implementations and their resources. A Layer graph is a composition mechanism, not product authority or repository topology.

## Runtime

Create an owned Runtime when a host must execute Effect from non-Effect entry points over a stable live graph. Do not construct one per request callback, React hook, or feature function.

## Queue and Stream

Use Queue for explicit asynchronous handoff, bounded buffering, mailbox-like ownership, or producer/consumer coordination. Use Stream for time-ordered values, transformation, backpressure, and resource-aware consumption.

## Actor or deterministic kernel

Use an Actor-like interpreter when one long-lived identity genuinely owns private state and serial message processing. Keep a pure deterministic transition kernel when replay, model-based testing, or event reasoning creates value.

## Ref and shared state

A Ref can safely coordinate in-process state but does not solve semantic ownership. Prefer the smallest owner and do not use global Refs as a domain database.

## Decision question

Ask:

```text
what failure semantics become clearer?
what lifetime becomes owned?
what independent implementation becomes replaceable?
what concurrency becomes structured?
what evidence becomes easier to produce?
what complexity does the mechanism add?
```

## Related knowledge

- Use [Service, Layer, and Runtime](service-layer-runtime.md) for construction boundaries.
- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for lifetime.
- Use [Structured concurrency, Queue, and Stream](structured-concurrency-queue-stream.md) for asynchronous coordination.
- Use [Deterministic kernel and Actors](deterministic-kernel-and-actors.md) only under real state-machine pressure.
- Return to the [Effect map](../SKILL.md).
