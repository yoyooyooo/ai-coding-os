# Structured Concurrency, Queue, and Stream

> **Structured Concurrency Leaves No Orphans.** Child work remains attached to an owning Scope, cancellation policy, resource budget, and observation surface.

Concurrency is first a question of dependency, ownership, cancellation, and budget. Parallel execution is only one consequence.

## Structured child work

A parent should own the lifetime of child Fibers. Define:

```text
whether sibling failure cancels others
whether partial success is allowed
how results are combined
which deadline applies
what concurrency and resource budget exists
what happens during parent interruption
```

Detached Fibers are conditional and require an explicit new owner.

## Queue

Use Queue when there is a real asynchronous handoff, mailbox, producer/consumer relationship, or buffering need.

Choose capacity deliberately:

```text
bounded      exposes overload and backpressure
unbounded    accepts memory risk and still needs monitoring
dropping     sacrifices work under declared semantics
sliding      keeps recent work under declared semantics
```

A Queue is not a semantic owner by itself.

## Stream

Use Stream for values over time with resource-aware composition. Name:

```text
source and lifetime
ordering and partitioning
backpressure
failure and retry
restart/replay behavior
end-of-stream meaning
consumer side effects and idempotency
```

## Fanout

A Hub or broadcast pattern should define slow-consumer behavior, replay, subscription lifetime, and whether every consumer must observe every value.

## Parallelism

Use bounded parallelism when independent work and resource capacity justify it. More Fibers can reduce throughput when they contend for the same database pool, provider quota, CPU, or lock.

## Shared state

Prefer ownership, message passing, immutable data, or atomic APIs. Refs, synchronized Refs, semaphores, and locks are mechanisms; the invariant and owner remain application questions.

## Cancellation

Cancellation should be cooperative and observable. External effects may need idempotency or reconciliation because local interruption cannot undo them.

## Related knowledge

- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for lifetime.
- Use [Errors, interruption, and unknown outcomes](errors-interruption-and-unknown-outcomes.md) for cancellation semantics.
- Use [Deterministic kernel and Actors](deterministic-kernel-and-actors.md) for mailbox-owned state.
- Use `$evolvable-application-architecture` for shared-state authority and events.
- Use `$product-harness-system` for overload, restart, ordering, and leak observation.
- Return to the [Effect map](../SKILL.md).
