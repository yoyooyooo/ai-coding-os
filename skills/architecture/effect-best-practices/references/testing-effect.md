# Testing Effect

Match the test level to the claim and ensure every test can terminate.

## Layers of Proof

```text
pure function / domain decision test
Effect flow with fake Services
Service/adapter contract test
Scope/finalizer and interruption test
Stream/Queue concurrency test
HTTP/CLI/worker black-box test
real database/provider/resource integration
declared local-stack or staging recovery scenario
```

A fake Layer proves application behavior against the contract, not the real
adapter. A typecheck proves API compatibility, not runtime cleanup or network
behavior.

## Determinism

Inject or control Clock, random/ID, configuration, and external capabilities.
Use TestClock or version-equivalent tools for schedules, retries, sleeps, and
heartbeats. Avoid real sleeps in unit tests.

## Termination

Use non-watch commands in automation. Give potentially blocking tests a test
harness deadline and guarantee resource disposal in success and failure paths.
Do not blindly add business timeouts merely to make tests end; use fake
capabilities or explicit test cancellation where appropriate.

## Failure Assertions

Assert stable typed errors/tags/codes and relevant context. Do not snapshot whole
FiberFailure stacks or runtime-rendered messages. Preserve separate tests for
expected failure, defect reporting, and interruption when the distinction is
part of the contract.

## Runtime/Resource Tests

Test:

```text
Layer construction failure
Runtime disposal
Scope finalizers on success/failure/interruption
idempotent close
close-before-open
child fiber supervision
Queue/Stream shutdown and saturation
```

## Boundary Tests

CLI tests spawn the real process when stdout/stderr/exit codes are claimed.
HTTP tests use a real handler/server boundary when routing/serialization is
claimed. Database/provider tests run real adapters when transaction or provider
behavior is claimed. Use explicit environment gates for expensive tests.
