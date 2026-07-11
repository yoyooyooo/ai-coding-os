# Forward Evolution

Forward evolution allows architecture and product semantics to change without
turning every previous internal shape into a permanent compatibility burden.

## Compatibility Classes

Treat compatibility differently by boundary.

### Internal Code APIs

Break and delete freely once all in-repository callers migrate. Avoid long-lived
deprecation facades that preserve a bad internal model.

### Durable Facts and Stored Data

Use one-way schema/data migrations. New code need not understand every old
shape, but existing accepted facts must be transformed or deliberately retired
under an approved data policy.

### Product APIs and Client Contracts

Use an epoch, media type, or explicit version when multiple deployed clients
cannot cut over atomically. Keep overlap short, observable, and bounded.

### External Protocols, Devices, and Plugins

Negotiate supported versions/capabilities or reject clearly. Do not silently
reinterpret an unsupported protocol through a default implementation.

### Replicas and Authority Membership

Treat leader terms, CRDT membership, schema versions, and policy epochs as
explicit compatibility boundaries. Fence stale writers before deleting the old
path.

## Temporary Bridge Contract

Every compatibility bridge, adapter shim, dual read, shadow path, translator, or
legacy writer must record:

```text
owner
reason
introduced_at
expires_at or review_at
allowed callers
forbidden new dependents
source of truth
divergence handling
delete_when
evidence required before deletion
```

A bridge without a deletion condition is a new permanent architecture.

## Migration Pattern

Use vertical strangler waves:

```text
1. characterize current behavior and accepted facts
2. introduce the new authority/use-case seam
3. route one real slice through the new path
4. compare projections, receipts, or shadow reads when useful
5. migrate durable data, epochs, and callers
6. prove restart, idempotency, failure, and backfill behavior
7. cut over and fence old writers
8. delete old writes, reads, bridges, and schema paths
```

Avoid indefinite dual write. When a short dual-write period is unavoidable,
define source of truth, reconciliation, divergence alarms, and a hard deletion
gate.

## Forward-Compatible Versus Backward-Compatible

A useful policy statement is:

> Old internal implementations are not promised to remain callable. Durable
> accepted facts are promised a deliberate forward migration path.

This preserves product data integrity without freezing poor abstractions.

## Rollback Boundaries

Code rollback is not always data rollback. State whether rollback can:

```text
run old code against new data
reverse a schema transformation
replay from canonical facts
compensate external effects
only roll forward after cutover
```

Do not promise rollback across irreversible effects or destructive migrations
without evidence.

## Destructive Changes

Stop for explicit authority when migration may discard accepted facts, weaken
permissions, change retention, expose private data, alter financial meaning, or
invalidate a public contract. Forward-only evolution is not permission to lose
data silently.
