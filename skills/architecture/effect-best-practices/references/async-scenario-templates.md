# Async Scenario Templates

Load after choosing Adoption Level 2 or 3. These are shapes, not mandatory APIs;
use the installed Effect version.

## HTTP or SDK Capability

```text
Service contract
  -> typed input/output/error
Live Layer
  -> host config/auth/client
  -> tryPromise/decode/error mapping
Flow
  -> timeout/retry only where policy allows
Facade or handler
  -> public Promise/HTTP/CLI shape
```

Bind `fetch`, base URL, auth, request IDs, and SDK clients once at composition.
Do not thread them through every operation input.

## WebSocket or SSE

```text
live capability owns transport, decode, retry/reconnect, heartbeat, Scope
subscription creates owned child Scope
runtime-bound facade exposes close()
feature adapter reduces typed envelopes
```

Test decode failure, gap/backfill signal, reconnect, repeated close, and
close-before-open.

## Polling or Background Loop

Use Schedule/repeat/forkScoped or version-equivalent when cancellation and test
control matter. Define owner, interval/backoff, overlap policy, deadline,
shutdown, and health. Avoid naked intervals hidden in feature modules.

## Child Process or Worker

Acquire process/worker as a resource. Define startup readiness, stdout/stderr
capture, command protocol, interruption, graceful stop, kill escalation, and
cleanup. Do not start it at module import.

## Fanout

Use bounded parallel Effect operations for finite batches. Use Queue/Stream for
continuous producer-consumer workflows. Define concurrency, ordering,
backpressure, duplicate safety, and partial failure.

## Frontend Bridge

```text
Effect capability + Layer
  -> app-owned runtime-bound facade
  -> Query/realtime/store adapter
  -> React renders and dispatches
```

Frontend state ownership remains defined by `frontend-architecture`; Effect owns
execution and resource semantics only.

## Test Harness

Run the Effect capability without the final host UI/server first using fake
Layers and controlled time. Then add boundary tests only for claims that require
real rendering, transport, process, or database behavior.
