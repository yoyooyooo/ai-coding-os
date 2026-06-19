# Repository and Database Adapter

Use only after the application architecture has identified a real persistence
capability and transaction boundary. A Repository is not required for every
entity and Effect does not make a generic repository desirable.

## Contract

A repository/transaction Service should expose the smallest consistency-aware
operations the use case needs. Do not expose a database client, ORM model, SQL
builder, or transport type through the inward-facing contract.

Prefer use-case or aggregate capabilities over CRUD symmetry when invariants or
atomicity matter:

```text
load facts needed for decision
commit typed change set with expected version/idempotency
append event/outbox in same transaction
return commit receipt
```

## Errors

Map driver exceptions into stable capability errors. Preserve conflict,
not-found, unavailable, constraint, and transaction failure distinctions when
callers need different decisions. Do not use exception text as a public API.

## Replacement

Create a memory/fake Layer when it provides real test or deployment value. It
must share contract tests with the live adapter for behavior being claimed:

```text
uniqueness and conflicts
ordering/pagination
idempotency
transaction atomicity
restart or persistence semantics when applicable
error mapping
```

A simple Map is useful for narrow unit tests but must not be presented as proof
of database behavior it does not implement.

## Optional Database Profiles

When a product intentionally supports durable and ephemeral profiles, select the
adapter only at a composition root. Keep public use-case semantics stable or
make profile capability differences explicit; do not silently downgrade durable
promises in memory mode.

## Integration Tests

Gate heavy database tests explicitly, isolate schemas/databases, and clean up.
Use real database tests for transaction, migration, locking, index/constraint,
and restart claims. Use fake Layer tests for application decisions and failure
branches that do not require real storage behavior.
