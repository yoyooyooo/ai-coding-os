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
cannot cut over atomically. Keep overlap short and observable.

### External Protocols and Plugins

Negotiate supported versions/capabilities or reject clearly. Do not silently
reinterpret an unsupported protocol through a default implementation.

## Temporary Bridge Contract

Every compatibility bridge, adapter shim, dual read, or shadow path must record:

```text
owner
reason
introduced_at
expires_at or review_at
allowed callers
forbidden new dependents
delete_when
evidence required before deletion
```

A bridge without a deletion condition is a new permanent architecture.

## Migration Pattern

Use vertical strangler waves:

```text
1. characterize current behavior and facts
2. introduce the new authority/use-case seam
3. route one real slice through the new path
4. compare projections or shadow reads when useful
5. migrate durable data and callers
6. prove restart, idempotency, and failure behavior
7. cut over
8. delete old writes, old reads, and bridge code
```

Avoid indefinite dual write. When a short dual-write period is unavoidable,
define source of truth, reconciliation, divergence alarms, and a hard deletion
gate.

## Forward-Compatible Versus Backward-Compatible

A useful policy statement is:

> Old internal implementations are not promised to remain callable. Durable
> accepted facts are promised a deliberate forward migration path.

This preserves product data integrity without freezing poor abstractions.

## Destructive Changes

Stop for explicit authority when migration may discard accepted facts, weaken
permissions, change retention, expose private data, or invalidate a public
contract. “We prefer forward-only evolution” is not permission to lose data
silently.
