# Scope, Resources, and Finalization

> **Scope Owns Lifetime.** The owner that can explain why a resource exists must also explain every normal, failed, interrupted, and timed-out path by which it ends.

Resources should be owned by the Scope that can explain why they exist and when they must end.

## Resource examples

```text
database pool or transaction
HTTP/provider client
file/socket/stream
subscription or listener
Queue or Hub
worker or Fiber
browser socket or service worker
lock, semaphore, permit, or temporary directory
```

## Acquisition and release

Keep acquisition and finalization in one structured lifetime. Every success, error, interruption, and early return path must close correctly.

A finalizer is not enough when the resource was created in the wrong lifetime. A socket acquired inside a component or request callback may be finalized eventually while still duplicating ownership.

## Scope owner

For each resource, name:

```text
host or parent Scope
acquisition condition
consumer set
shutdown/cancellation trigger
failure policy
observability
```

## Nested scopes

Child work should not outlive the parent unless the design explicitly transfers ownership. Structured Scope prevents detached orphan Fibers and hidden background work.

## Finalizer behavior

Finalizers should be:

- safe under partial acquisition;
- idempotent when practical;
- ordered so dependent resources close before dependencies;
- observable when cleanup fails;
- free from new product decisions based on already untrusted state.

## Transactions

A transaction is a resource and a semantic boundary. Ensure commit/rollback follows the use-case invariant. Do not use `Scope` alone to imply database atomicity.

## Time-based garbage

Logs, temporary files, caches, queues, artifacts, and Agent Runs also need retention and cleanup. Any process that continuously creates finite resources needs a matching destruction mechanism.

## Host shutdown

Define:

```text
stop accepting new work
interrupt or drain child work
flush or commit where semantics allow
close providers and pools
report unresolved unknown outcomes
exit with stable status
```

## Related knowledge

- Use [Service, Layer, and Runtime](service-layer-runtime.md) for construction.
- Use [Structured concurrency, Queue, and Stream](structured-concurrency-queue-stream.md) for child work.
- Use [Testing Effect](testing-effect.md) for finalizer and interruption evidence.
- Use `$evolvable-application-architecture` for host composition and transaction semantics.
- Return to the [Effect map](../SKILL.md).
