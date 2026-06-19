# Stream, Queue, and Concurrency

Use when the workload has fanout, continuous consumption, buffering, bounded
parallelism, ordering, or backpressure requirements.

## First Decide

```text
finite batch or continuous service
maximum concurrency
buffer capacity
ordering scope
failure strategy
cancellation/shutdown
overflow/backpressure policy
idempotency and retry safety
```

Do not introduce Stream/Queue only because values arrive asynchronously. A
single request/response Effect may be simpler.

## Boundedness

When input can grow independently of processing, bound concurrency and buffers.
Choose an explicit overflow policy:

```text
backpressure/block
drop newest/drop oldest
sliding/latest-only
fail/reject admission
spill to durable queue
```

Data-loss policies require product approval and diagnostics such as dropped
counts. A durable work queue is a different authority from an in-memory Effect
Queue; do not conflate them.

## Structured Concurrency

Tie child work to a Scope/supervisor. Use parallel combinators with an explicit
concurrency budget rather than unbounded `Promise.all` or orphaned forks.
Separate product ordering from IO pool capacity: same-key serialization and
cross-key parallelism may coexist.

## Stream

Use Stream when zero-or-more values, composition, cancellation, or backpressure
are core to the workflow. Define terminal behavior, retry/reconnect, dedupe, and
partial failure semantics.

## Queue

Use Queue to coordinate producers and consumers inside a runtime. Define who
owns shutdown, whether pending items drain or interrupt, and what happens when a
consumer fails. Do not claim persistence or exactly-once delivery from an
in-memory Queue.

## Observability and Tests

Observe capacity, depth/high-water mark, active workers, latency, retries,
dropped/rejected items, and shutdown state where operationally relevant. Test
ordering, saturation, cancellation, retry duplicates, drain/interrupt, and
resource finalization.
