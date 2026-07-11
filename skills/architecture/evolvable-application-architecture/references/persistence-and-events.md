# Persistence and Events

Persistence ports should describe the application's consistency needs, not the
current in-memory representation.

## Avoid Whole-State Snapshot Contracts

A contract such as `loadEntireState()` / `persistEntireState(state)` can be a
prototype seam, but becomes a bottleneck when every new fact forces every store
adapter to understand the whole product.

Symptoms include:

- application memory mirrors the entire database;
- store methods receive a universal command outcome;
- special-case persist methods grow for each workflow;
- restart correctness depends on serializing transient caches;
- projections scan a giant restored state object;
- one module cannot change schema independently.

## Use-Case Transaction Seam

Prefer an explicit transaction or unit-of-work boundary for each pressured
vertical slice:

```text
load required facts
-> verify authority epoch / expected version / idempotency
-> compute typed ChangeSet or Decision
-> write owning business rows or canonical events
-> append event/audit/outbox in the same transaction
-> commit
-> return CommitReceipt
```

Repository APIs should be owned by the application module that consumes them.
Do not expose ORM/database models as core contracts.

## Do Not Build a Universal Repository

Start with use-case-oriented operations or small repository capabilities. A
universal generic repository leaks persistence semantics and hides invariants.

The application should be able to state:

```text
which facts are read
which facts are written
which version, epoch, lock, or causal frontier is checked
which event/audit/outbox records are appended
what makes the operation idempotent
```

## Atomicity and External Effects

When an event or outbox record represents an accepted change, write it in the
same transaction as the fact. Publishing to a broker, websocket, email, device,
or remote API occurs after commit and may retry from durable work.

An external effect failure must not erase an already committed local fact by
implication. Record pending, acknowledged, failed-known, outcome-unknown,
reconciliation, and compensation states when semantics require them.

## Inbox, Dedupe, and Source Versions

For external ingress, preserve source identity and version. Use durable inbox or
uniqueness records when retries and reordering are possible. Transport message
ID alone may be insufficient if the source can correct or supersede records.

## Projections and Backfill

Projections should be rebuildable from authoritative facts and/or the canonical
event spine under a documented ceiling. Realtime clients need cursor, dedupe,
gap detection, schema/version handling, and backfill behavior.

Do not assume event sourcing by default. A relational fact store plus a durable
event/outbox spine is often sufficient. Adopt full event sourcing only when
history-as-authority and replay semantics justify its complexity.

For CRDTs, federation, leader epochs, or sagas, choose storage and ordering from
[Consistency and Authority Topologies](consistency-and-authority-topologies.md)
rather than forcing one transaction model onto every fact.

## Adapter Conformance

In-memory, fake, local-file, and database adapters should share contract tests
for applicable properties:

- transaction atomicity;
- idempotency after restart;
- expected-version or fencing conflicts;
- event/outbox coupling;
- inbox dedupe and source corrections;
- ordering and pagination;
- projection rebuild and backfill;
- error normalization;
- schema/data migration behavior.
