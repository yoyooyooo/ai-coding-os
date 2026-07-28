# Restart, Retry, Reconnect, and Recovery

These properties cross ordinary function boundaries and expose authority, persistence, idempotency, resource, and continuity assumptions.

## Restart

Observe what happens when a host or process stops and starts:

```text
which facts survive
which work resumes, repeats, or is abandoned
whether locks/leases expire
whether child work is orphaned
whether resources close
whether pending operations reconcile
```

## Retry

Exercise duplicate delivery and unknown outcome, not only a clean transient failure. Verify stable operation identity, idempotency scope, backoff/deadline, and external provider semantics.

## Reconnect

For sockets or streams, observe sequence/cursor, dedupe, gap detection, backfill, permission change, and projection freshness. A reconnected transport may still carry stale state.

## Reload

For browser/desktop, reload reveals what was incorrectly owned only in memory. Verify drafts, pending operations, URL, remote projection, and security-sensitive cache behavior according to product meaning.

## Recovery

Recovery should be a product and operational contract:

```text
what is preserved
what is rebuilt from authority
what is retried automatically
what requires user confirmation
what becomes unknown or needs reconciliation
what evidence remains for diagnosis
```

## Failure injection

Use controlled process kill, connection drop, duplicate message, provider timeout, stale version, storage interruption, or corrupted input. Do not rely only on graceful code paths.

## Related knowledge

- Use [Dependency realities](dependency-realities.md) to label the environment.
- Use [Investigation and the first wrong state](investigation-and-first-wrong-state.md) to capture causal evidence.
- Use [Observation limits](observation-limits.md) before claiming resilience.
- Use `$evolvable-application-architecture` for idempotency, migration, and authority.
- Use `$frontend-architecture` for reload and realtime continuity.
- Use `$effect-best-practices` for Scope and interruption.
- Return to the [Harness map](../SKILL.md).
