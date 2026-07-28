# Consistency, Events, and Shared State

Consistency design begins with fact authority and product invariants, not with a fashionable event or distributed-systems pattern.

## Shared mutable state

If several actors can update the same state without coordination, correctness depends on timing. Prefer:

```text
single semantic writer
atomic API or transaction
version/compare-and-set
immutable event or message transfer
partitioned ownership
```

Locks may be necessary, but lock discipline is not a substitute for clear ownership.

## Consistency scope

Define which facts must change together and what intermediate states are acceptable. Stronger consistency costs availability, latency, and operational complexity; weaker consistency costs reconciliation and user-visible uncertainty.

## Events

An event is an accepted statement that something happened. Do not use an event to avoid naming the owner or transaction that made it true.

Define:

```text
event owner and schema
event time and version
ordering scope
duplicate behavior
publication guarantee
consumer failure/retry semantics
relationship to current source of truth
```

## Outbox

Use an outbox when a local fact transition and the intent to publish must commit atomically. The outbox does not prove downstream processing; it proves durable publication intent.

## Saga and compensation

Use a Saga when a business operation spans independent authorities and cannot be one transaction. Each step needs explicit accepted/pending/failed states, idempotency, compensation semantics where valid, and reconciliation.

Compensation is a new business action, not time travel.

## Event sourcing

Event sourcing is justified when the event log is the authoritative fact model and its replay, versioning, and evolution costs are accepted. Do not adopt it merely for audit history; an ordinary fact model plus audit/outbox may be enough.

## CRDT and mergeable state

CRDTs are useful when independent concurrent updates must merge without central coordination and the domain operation is mathematically mergeable. They do not solve arbitrary business conflicts or permission decisions.

## Import and federation

When another system owns facts, record provenance, version, conflict policy, and reconciliation. Avoid two systems each believing they are final authority.

## Related knowledge

- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) first.
- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for local commits and unknown outcomes.
- Use [Forward evolution and migration](forward-evolution-and-migration.md) for dual-read/write periods.
- Use `$frontend-architecture` for realtime projection continuity.
- Use `$product-harness-system` for duplicate, ordering, restart, and replay observation.
- Return to the [EAA map](../SKILL.md).
