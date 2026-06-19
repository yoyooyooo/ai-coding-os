# Scope and Resources

Use when code acquires something that must be released or supervises work that
must end with an owner: database connection, server, file handle, child process,
WebSocket, worker, subscription, lock, timer, or background fiber.

## Lifetime First

Before choosing an API, record:

```text
resource owner and lifetime
acquisition failure
release action and release failure policy
cancellation behavior
deadline or intentional infinite lifetime
shutdown/drain semantics
```

A server or daemon may intentionally have no per-operation timeout; it still
needs a host shutdown protocol. A request or command that can hang indefinitely
usually needs a deadline. Do not apply one universal timeout to every resource.

## Scoped Acquisition

Acquire and release in the same Scope using the installed version's scoped Layer
or `Effect.acquireRelease`/equivalent. Avoid import-time live resources and
unowned module singletons.

Use a Layer when the resource implements a shared capability. Use a local scoped
workflow when the resource belongs to one operation or subscription.

## Subscription Facade

A runtime-bound subscription may create a child Scope and return:

```text
close(): idempotent release/interruption
status/diagnostics: optional local resource projection
```

Handle close-before-open-completes: once acquisition eventually succeeds, the
resource must still be finalized. Per-subscription resources should not
accidentally live for the entire application Runtime.

## Structured Work

Prefer scoped/supervised child fibers. If work intentionally outlives the parent,
model a daemon supervisor with explicit start, health, stop, drain, and failure
policy; do not simply drop a Fiber handle.

## Finalizers

Finalizers should be idempotent and resilient. Preserve the primary Exit while
recording cleanup failures according to project policy. Never rely on process
exit as the only cleanup mechanism for reusable libraries or tests.

## Entry Boundary

Executable or host composition owns the top-level Runtime/Scope and unified
shutdown. Library/domain modules do not call `process.exit` or hide unowned
`runPromise` calls.

## Tests

Prove successful release, acquisition failure, interruption, repeated close,
close-before-open, and host shutdown. Use deterministic clocks/fakes where timing
matters, then real resource tests for claims that require them.
