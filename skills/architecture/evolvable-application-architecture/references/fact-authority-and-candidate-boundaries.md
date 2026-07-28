# Fact Authority and Candidate Boundaries

> **One Fact, One Final Writer. Candidates Propose; Authorities Materialize.** Many inputs may suggest or observe a fact, but only the governed materialization authority accepts it within the declared consistency scope.

Persistent or externally consequential facts need an explicit final materialization authority. Fast or convenient inputs do not become authoritative by arrival order.

## Fact authority

Within a declared consistency scope, identify:

```text
accepted fact
final writer
allowed commands
transaction or atomic boundary
forbidden or legacy writers
read projections and caches
reconciliation source when outcomes are uncertain
```

A database table, package, service, event stream, or UI cache does not grant authority by itself.

## Candidate versus accepted fact

These are normally candidates or observations:

```text
user draft
provider response
model output
realtime frame
imported file
legacy database row
optimistic UI proposal
replayed event
```

A governed use case validates, authorizes, and materializes accepted facts. If an external system is itself the authoritative source, model the import/reconciliation relationship explicitly rather than pretending the local copy created the fact.

## One writer does not mean one process

A final materialization authority may be implemented by several instances or hosts as long as they share the same governed contract and atomic consistency mechanism. The invariant is semantic write authority, not a singleton server.

## Read models

Projections, caches, search indexes, reports, and frontend state are derived views. They may be rebuilt or reconciled. Their update path should not accidentally become a second writer of the underlying product fact.

## External authority

When a provider owns the fact, distinguish:

```text
provider fact
local observation of provider fact
local decision based on provider fact
local cached projection
```

A timeout may leave the provider outcome unknown. Reconcile by operation identity, status query, webhook, ledger, or other authoritative route.

## Imported legacy data

During migration, imported data may enter as candidate records requiring validation, normalization, or provenance. Avoid silently treating all legacy values as accepted under the new model.

## Permissions

Authorization should guard the use case that can materialize the fact. UI visibility and transport authentication are supporting controls, not the final authority boundary.

## Related knowledge

- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for governed writes.
- Use [Consistency, events, and shared state](consistency-events-and-shared-state.md) for multi-writer and event topologies.
- Use [Forward evolution and migration](forward-evolution-and-migration.md) when authority moves.
- Use [Agent-legible change surface](agent-legible-change-surface.md) to expose the writer.
- Use `$frontend-architecture` for proposals and projections.
- Return to the [EAA map](../SKILL.md).
