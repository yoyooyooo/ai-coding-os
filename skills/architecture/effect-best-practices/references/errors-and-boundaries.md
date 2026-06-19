# Errors and Boundaries

Effect distinguishes expected failures, defects, and interruption. Preserve
that distinction until the outer boundary needs a stable response.

## Expected Failure

Use the typed error channel for recoverable, anticipated outcomes:

```text
validation rejected
not found/conflict
provider unavailable
permission denied
retry exhausted
decode failure
```

Prefer discriminated/data errors with stable tags/codes and useful context. Do
not place secrets or raw provider payloads in public error values.

## Defect

A defect is an unexpected bug or violated invariant. Do not convert every defect
to a generic business error too early; doing so hides programming failures and
breaks observability. Catch defects only at a boundary that can report, isolate,
or restart safely.

## Interruption

Interruption represents cancellation/lifetime end. Do not map it to ordinary
“failed” unless the product contract requires that view. Finalizers must still
run. Preserve cancellation through Promise/SDK adapters when possible.

## Promise Boundary

Use `Effect.tryPromise` when rejection belongs in the expected error channel and
map `unknown` into a stable boundary error. Use `Effect.promise` only when
rejection should be treated as a defect or the Promise is guaranteed not to
reject by contract.

## Boundary Mapping

Map errors once at the relevant edge:

```text
SDK/infra error
  -> capability error
  -> application/domain decision when needed
  -> HTTP/CLI/UI public error
```

Do not let transport handlers, React components, or CLI formatters understand
vendor exceptions. Do not erase all domain distinctions into `Error` inside the
capability layer.

## Retry and Timeout

Retry only errors known to be safe and useful to retry. Consider idempotency,
external side effects, deadlines, and rate limits. A timeout is a policy decision
at a use-case/host boundary, not a decoration blindly applied to every Effect.

Record:

```text
retryable tags/codes
attempt/backoff/jitter budget
overall deadline
idempotency key or safety argument
operator/user-visible outcome
```
