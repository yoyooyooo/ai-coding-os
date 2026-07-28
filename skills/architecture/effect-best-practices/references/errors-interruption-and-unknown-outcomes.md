# Errors, Interruption, and Unknown Outcomes

> **Timeout May Mean Unknown Outcome.** A waiting policy ended; the external effect may still have completed, so retry requires identity, idempotency, and reconciliation.

Effect makes several failure channels visible. Preserve their meanings rather than collapsing them into one error message.

## Expected failure

A modeled error that the caller can handle as part of the capability contract:

```text
validation rejection
not authorized
not found
business conflict
provider unavailable when retry or fallback is meaningful
```

Use a typed error channel or discriminated result.

## Defect

A violated assumption or implementation bug, such as impossible state, unchecked null, faulty decoder use, or invariant breach. Defects should normally fail the smallest untrusted Scope and retain Cause information.

Do not convert every defect into a friendly expected error; that hides broken code.

## Interruption

Interruption is cooperative cancellation from an owning Scope. It is not an ordinary business error. Preserve finalization and do not accidentally swallow interruption in broad catch logic.

## Timeout

Timeout is a local waiting policy. It says the caller stopped waiting by a deadline. It does not prove the external operation failed or did not complete.

## Unknown outcome

When an external effect can continue after local timeout/interruption, represent an unknown outcome and preserve operation identity. Reconcile before retrying non-idempotent work.

## Retry

Retry only after answering:

```text
is the operation idempotent under a stable key?
can duplicate external effects occur?
what deadline and backoff apply?
which failures are transient?
how is an unknown outcome reconciled?
what resource or concurrency budget limits retries?
```

## Error translation

Translate provider/infrastructure failures at the capability boundary. Preserve original Cause or diagnostic context for observation while returning application-relevant meaning to callers.

## Fail fast

When an invariant is broken, stop the smallest affected Scope rather than continuing with untrusted state. An outer supervisor decides retry, restart, degrade, isolate, or escalate.

## Related knowledge

- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for cleanup on failure.
- Use [Testing Effect](testing-effect.md) to verify interruption and error channels.
- Use `$evolvable-application-architecture` for idempotency and fact authority.
- Use `$product-harness-system` for timeout/unknown-outcome observation.
- Return to the [Effect map](../SKILL.md).
