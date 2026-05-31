# 异步场景模板

本文用于 Effect-first 项目。核心规则：

```text
复杂异步 / 长生命周期 / 可替换依赖 / 并发 / 资源释放 / 重试 / 超时 / 测试 harness
  -> 默认优先用 Effect Service / Layer / Scope / Stream / Queue

纯 reducer / mapper / DTO transform / view-model
  -> 保持普通 TypeScript 函数
```

“client”不是使用 Effect DI 的触发条件。触发条件是能力边界是否需要替换、隔离、错误建模、资源生命周期、并发语义或 harness。

## WebSocket / SSE Subscription

推荐分层：

```text
packages/client 或 host runtime package
  owns Service contract
  owns live/fake Layer
  owns WebSocket / EventSource acquireRelease
  owns decode, typed errors, retry/backoff, heartbeat timeout, cancellation

app root / host bootstrap
  owns ManagedRuntime / runtime-bound deps
  injects stable facade into React / route / worker

feature adapter
  owns typed envelope -> pure reducer -> cache/store action
  does not create transport, Layer, runtime, or config

React
  owns mount/unmount glue only
```

Live template:

```text
ChannelRealtime Service
  subscribe(input) -> Effect<Subscription, ChannelRealtimeError, Scope>

Layer.effect(ChannelRealtime)
  acquire WebSocket
  onmessage -> decode -> Queue.offer / handler
  onclose / heartbeat timeout -> typed close state
  release -> idempotent close
```

Facade template:

```text
runtime-bound client exposes:
  subscribeProjection(input, handlers): { close(): void }

Internally:
  runtime.runPromise(openScopedSubscription(...))
  close() interrupts / finalizes Scope
```

callback-shaped facade 只是 React / Query / host 的外部形态，不等于 live implementation 只能写 callback。WebSocket / SSE / EventSource 资源仍归 Effect Scope，facade 只负责把 `close()` 映射到 scope finalizer。

不要把 `WebSocketImpl`、base URL、auth header builder 等 host deps 透传到每次 subscribe input。它们应在 client factory / Layer boundary 归一化，并由 Realtime Service 持有。

Testing template:

```text
fake Layer emits envelopes
TestClock drives retry/backoff/heartbeat
Effect.scoped proves finalizer / close
close() before open Promise resolves still releases after open completes
close idempotency
unmount / StrictMode repeat mount
decode failure stays diagnostic
gap/requiresBackfill does not invent facts
```

Do not put reconnect loops, heartbeat timers, DTO decode policy, or WebSocket construction inside React hooks.

## HTTP Client / Request Gateway

Use Effect for:

- request id / headers;
- timeout / retry / cancellation;
- transport/domain/contract error split;
- schema decode / contract mismatch;
- fake Layer / test request recorder.

Feature Query functions should consume a runtime-bound Promise facade:

```text
queryFn -> deps.channel.fetchProjection(input)
```

Query code should not build Layer, read env, or call `Effect.runPromise` directly.

Do not pass `fetchImpl`, base URL, request id factory, or auth header builder through every request helper. Bind them once in a Request Service / Layer, then expose a Promise facade from the package boundary.

## Polling / Background Loop

Use `Effect.repeat` / `Schedule` / `Queue` / `forkScoped` when:

- loop may outlive one function call;
- cancellation matters;
- retry/backoff must be deterministic;
- tests need `TestClock`.

Forbidden:

- naked `setInterval` in feature modules;
- `Effect.fork` without Scope ownership;
- polling loop hidden in React render/hook without a runtime owner.

## Daemon / Child Process / Worker Bridge

Use Effect for process/resource ownership:

```text
Layer.effect(Service)
  acquire child process / worker
  expose command API
  release TERM -> wait -> KILL / worker terminate
```

Timeout, stdout/stderr capture, cancellation and diagnostic fields are part of the contract, not call-site decoration.

## Queue / Stream Fanout

Use `Queue` / `Stream` when multiple consumers need the same async signal or when backpressure / buffering is a product concern.

Default shape:

```text
transport event
  -> decode
  -> Queue.offer typed event
  -> Stream consumers / subscription facade
```

Prefer explicit overflow policy over unbounded buffering.

## React / Zustand Bridge

React should see stable deps/actions, not raw runtime:

```text
Effect Service / Layer
  -> runtime-bound deps
  -> action bridge / subscription facade
  -> Zustand local actions + Query cache adapter
  -> React calls stable actions and renders derived state
```

Zustand may own local synchronous actions:

- draft;
- drawer target;
- pending echo;
- connection UI state;
- last cursor / retry UI state.

Zustand must not own:

- server projection truth;
- WebSocket transport;
- Effect runtime / Layer;
- app config / env reads.

## TDD Harness

Effect-first code should make the non-React path testable first:

```text
makeTestRuntime / fake Layer
run action without React
open scoped subscription without browser
advance TestClock for retry/backoff
assert finalizers / close
then add minimal React wiring tests
```

If a test must mock global `fetch` / `WebSocket` first, the DI boundary is probably too late.
