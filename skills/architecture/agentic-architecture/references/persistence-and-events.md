# Persistence and Events

Persistence ports should describe the application's consistency needs, not the
current in-memory representation.

## Avoid Whole-State Snapshot Contracts

A contract such as `loadEntireState()` / `persistEntireState(state)` can be a
prototype seam, but it becomes a bottleneck when every new fact forces every
store adapter to understand the whole product.

Symptoms include:

- application memory mirrors the entire database;
- store methods receive a universal command outcome;
- special-case persist methods grow for each new workflow;
- restart correctness depends on serializing transient caches;
- projections scan a giant restored state object;
- one module cannot change schema independently.

## Use-Case Transaction Seam

Prefer an explicit transaction or unit-of-work boundary for each high-pressure
vertical slice:

```text
load required facts
-> compute typed ChangeSet
-> write owning business rows
-> append event/audit/outbox in the same transaction
-> commit
-> return CommitReceipt
```

Repository APIs should be owned by the application module that consumes them.
Do not expose ORM/database models as domain contracts.

## Do Not Build a Universal Repository

Start with use-case-oriented operations or small repository capabilities. A
universal generic repository often leaks persistence semantics and makes
invariants invisible.

Acceptable shapes vary by language, but the application should be able to state:

```text
which facts are read
which facts are written
which version or lock is checked
which event/outbox records are appended
what makes the operation idempotent
```

## Atomicity

When a product event or outbox record represents an accepted change, write it in
the same transaction as the business fact. Publishing to a broker or websocket
occurs after commit and may retry from the outbox.

A transport or event delivery failure must not roll back an already committed
business fact by implication.

## Projection Rebuild and Backfill

Projections should be rebuildable from authoritative facts and/or the canonical
event spine under a documented ceiling. Realtime clients need cursor, dedupe,
gap detection, and backfill behavior.

Do not assume event sourcing by default. A relational fact store plus a durable
event/outbox spine is often sufficient. Adopt full event sourcing only when
history-as-authority and replay semantics justify its complexity.

## Adapter Conformance

In-memory, fake, local-file, and database adapters should share contract tests
for:

- transaction atomicity;
- idempotency after restart;
- expected-version conflicts;
- event/outbox coupling;
- ordering and pagination;
- projection rebuild;
- error normalization;
- migration behavior.
