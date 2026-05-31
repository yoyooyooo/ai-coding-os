# React / 前端集成

本文件只定义 Effect 在前端中的职责边界。前端目录结构、命名语义、`packages/client` / `packages/ui`、Query / Store / realtime adapter 和 harness-ready surface 归 `$frontend-architecture`。

可编译最小示例见 `../examples/effect-v4-runtime-client.example.ts`。

## 核心定位

Effect 在前端里是边界运行时骨架，不是 React 状态层，也不是所有业务建模的默认语言。

Effect-first 项目默认把复杂异步、长生命周期资源、可替换依赖、并发、重试、超时、取消和测试 harness 放进 Effect Service / Layer / Scope / Stream / Queue。`client` 只是常见载体，不是唯一触发条件；只要一个能力边界需要 fake、隔离、错误通道或资源释放，就应优先考虑 Effect DI。

版本口径：新项目默认 Effect v4。service key 默认用 `Context.Service`；资源型 Layer 默认用 `Layer.effect`。v3 项目的 `Context.Tag` / `Layer.scoped` 只作为旧项目 adapter 兼容项。

推荐分工：

```text
Effect
  RequestClient / RealtimeClient / Config / 错误归一化
  timeout / retry / cancellation / resource lifecycle
  Context.Service / Layer / live / fake 替换

React
  component tree / render lifecycle / event handlers

TanStack Query 或等价 server-state cache
  server projection cache / query lifecycle / mutation lifecycle

Zustand 或等价 local state
  local interaction state only

普通 TypeScript 函数
  mapper / parser / normalizer / view-model transform
```

## 推荐 home

长期 home：

```text
packages/client
  capability client interface
  Effect service key / Layer
  request/realtime transport
  live/fake implementation
  normalized errors

app runtime wiring
  选择 config
  创建 live client/runtime
  通过 route/provider/context 注入下层
```

feature 不 import `app/runtime`。app 创建已经绑定 runtime/config 的 client，route/provider 把 client contract 传给 feature。

## Thin Bridge

React 集成层应薄封装 runtime-bound deps，而不是把 Effect runtime 暴露给组件：

```text
app runtime
  creates ManagedRuntime / closed Layer
  creates runtime-bound deps / actions / subscription facades

React provider
  provides deps object, not raw Runtime

feature / component
  calls stable actions
  renders Query / Zustand / view-model state
```

推荐薄封装类型：

- runtime provider / deps context；
- action runner，把 Effect program 绑定成普通 async action；
- subscription facade，把 Effect-managed resource 暴露成 `{ close() }`；
- test harness helper，创建 fake deps、scoped runtime、TestClock 驱动器。

禁止把这层扩成万能 `useEffectProgram()` 框架；React hook 仍应只是 adapter。

## Package Boundary Facade

在 Effect-first 子包里，不要把“外部 API 不暴露 Effect”误读成“内部也不用 Effect”。推荐模式是：

```text
package internal
  Effect Service / Layer / Scope / typed errors / live/fake

package factory / host runtime boundary
  normalize host deps once
  build closed Layer
  create ManagedRuntime

package public API
  Promise functions
  subscription facade such as { close(): void }
  optional dispose / close for runtime owner
```

`createXClient(config)` 这类工厂是 composition root，不是数学意义的纯函数。它可以创建 runtime、绑定 config、绑定 `fetch` / `WebSocket` 等 host deps，然后把 Effect 程序包成普通 function。外部 consumer 不需要知道 Effect，内部也不需要通过每层 input 透传依赖。

推荐规则：

- host deps 只在 factory / Layer boundary 归一化一次；
- operation helper 只接收业务 input，依赖从 Service 获取；
- `runtime.runPromise(...)` 只出现在 runtime-bound facade 或明确入口里；
- package root 默认只导出 capability client contract / factory / normalized errors；
- internal service key、Layer、transport 不从 package root 暴露，除非该包明确提供单独的 Effect-native API；
- 有资源的 facade 必须提供 `close` / `dispose`，或由宿主声明生命周期 owner。

禁止把“规避 Effect 传染”变成参数隧道：

```ts
requestJsonEffect({ config, fetchImpl, path, init });
openProjectionWebSocketEffect({ config, WebSocketImpl, subscriptionInput, handlers });
```

这种形态应改成 `RequestTransport` / `RealtimeTransport` / `Gateway` 之类 Service，从环境读取依赖。

## Runtime 管理

前端必须有明确的 runtime owner。默认 owner 是 app composition root 或宿主 bootstrap，不是 React component、feature module、Query hook 或 mapper。

推荐规则：

```text
browser host
  app bootstrap 创建一个 runtime-bound ProductClient
  route/provider/context 把 client contract 传给 feature
  feature.query.ts / feature.realtime.ts 只消费 client contract

test / headless harness
  创建 isolated fake client 或 test runtime
  通过同一个注入点替换 live client

server host
  按 request 或 process 生命周期创建 server live client/runtime
  不复用 browser-only live implementation

desktop host
  使用 desktop live implementation，例如 IPC transport
  仍暴露同一 capability client contract
```

禁止把 runtime 创建藏进：

```text
React component render
useMemo / useEffect 内部随手 new runtime
feature.query.ts
feature.realtime.ts
feature module-level singleton
packages/client React hook
```

`ManagedRuntime.make` 或等价 runtime 构造必须接收已经闭合依赖的 Layer。不要把仍带未满足依赖的 Layer 交给 runtime；也不要在每个 queryFn 内临时 `provide` 一整套 live Layer。

v4 口径：

```text
Context.Service    定义 capability service key
Layer.succeed      提供无资源实现
Layer.effect       提供 Effect / Scope 资源实现；v3 对照为 Layer.scoped
ManagedRuntime.make(appLayer) 由 app root / host bootstrap 持有
runtime.runPromise(effect)    只在 runtime-bound client 内部使用
runtime.dispose()             host 生命周期结束时释放
```

### Browser host 方法 binding

把浏览器原生方法作为 deps 传入 Effect Service / client 时，保留 host binding。典型例子是 `fetch`：

```ts
const fetchImpl = globalThis.fetch
  ? (globalThis.fetch.bind(globalThis) as typeof fetch)
  : undefined;
```

不要裸传 `const fetchImpl = globalThis.fetch` 后跨 runtime / facade 调用。浏览器里这类 host method 可能依赖 `this`，裸函数调用会丢 binding，表现为请求未发出或抛出 illegal invocation。

## React 注入形态

推荐把 Effect runtime 隐藏在 runtime-bound client 之后。React 层只看见稳定的 capability interface。

```ts
// packages/client
import { Context, Effect, Layer, ManagedRuntime } from "effect";

export type ProductClient = {
  channel: ChannelClient;
  close: () => Promise<void>;
};

export class ChannelGateway extends Context.Service<
  ChannelGateway,
  {
    readonly fetchProjection: (
      channelId: string
    ) => Effect.Effect<ChannelProjection, ChannelError>;
    readonly sendMessage: (
      input: SendMessageInput
    ) => Effect.Effect<SendMessageResult, ChannelError>;
  }
>()("ChannelGateway") {}

const ChannelGatewayLive = (config: AppConfig) =>
  Layer.succeed(ChannelGateway)({
    fetchProjection: (channelId) =>
      Effect.tryPromise({
        try: () => fetchChannelProjection(config, channelId),
        catch: (cause) => new ChannelError({ cause })
      }),
    sendMessage: (input) =>
      Effect.tryPromise({
        try: () => postChannelMessage(config, input),
        catch: (cause) => new ChannelError({ cause })
      })
  });

const fetchChannelProjectionEffect = (channelId: string) =>
  Effect.gen(function* () {
    const gateway = yield* ChannelGateway;
    return yield* gateway.fetchProjection(channelId);
  });

const sendChannelMessageEffect = (input: SendMessageInput) =>
  Effect.gen(function* () {
    const gateway = yield* ChannelGateway;
    return yield* gateway.sendMessage(input);
  });

export function createLiveProductClient(config: AppConfig): ProductClient {
  const runtime = ManagedRuntime.make(ChannelGatewayLive(config));
  return {
    channel: {
      fetchProjection: (channelId) =>
        runtime.runPromise(fetchChannelProjectionEffect(channelId)),
      sendMessage: (input) =>
        runtime.runPromise(sendChannelMessageEffect(input)),
      subscribeProjection: (input, handlers) =>
        createChannelSubscription(runtime, input, handlers)
    },
    close: () => runtime.dispose()
  };
}
```

```tsx
// app / route adapter
function ChannelRoute() {
  const { client } = Route.useRouteContext();
  const { channelId } = Route.useParams();
  return <ChannelPage channelId={channelId} client={client.channel} />;
}
```

```ts
// feature.query.ts
export function channelProjectionQueryOptions(
  client: ChannelClient,
  channelId: string
) {
  return queryOptions({
    queryKey: channelKeys.projection(channelId),
    queryFn: () => client.fetchProjection(channelId)
  });
}
```

React Context 可以作为注入机制，但 Context 的 value 应是 client contract 或 app dependencies object，不是裸 Effect runtime。只有少数 app wiring 文件应该知道 runtime 的存在。

## 生命周期与释放

有资源的 runtime 必须有释放策略：

```text
HTTP-only browser client
  通常无显式释放；仍需支持 request cancellation / timeout

WebSocket / EventSource / worker / daemon bridge
  用 Scope / Layer.effect / acquireRelease 管理
  subscription 必须返回 close / unsubscribe
  component unmount 或 route leave 必须释放订阅

test runtime
  每个测试独立创建
  测试结束释放 Scope / close subscriptions
```

React StrictMode 可能重复 mount / unmount。live subscription adapter 必须能正确 close，不能依赖“只 mount 一次”的假设。

## 禁止模式

```text
React component 直接 Effect.runPromise
React context 暴露裸 Runtime 供任意组件调用
feature.query.ts 创建 live Layer / live client
feature.query.ts 读取 app env/config
Effect service import React / TanStack Query / Zustand
纯 mapper 层层 Effect.succeed
operation helper 层层透传 config / fetchImpl / WebSocketImpl
为了规避 Effect 传染而把 host deps 塞进每个 input
module-level 不可替换 live singleton
packages/client export React hook
Zustand store 创建 Effect runtime / WebSocket / live Layer
```

## Query 集成

Query 层消费 runtime-bound client function，不直接创建 Effect runtime。

推荐形态：

```ts
export function channelProjectionQueryOptions(
  client: ChannelClient,
  channelId: string
) {
  return queryOptions({
    queryKey: channelKeys.projection(channelId),
    queryFn: () => client.fetchProjection(channelId)
  });
}
```

`client.fetchProjection` 内部可以由 Effect 运行时实现，但 Query 层只看到稳定 Promise / subscription contract。

## Fake 替换

测试和 headless harness 优先替换 client 或 Layer，而不是 mock 全局 fetch / axios / WebSocket。

```ts
const fakeClient: ChannelClient = {
  fetchProjection: async () => projectionFixture,
  sendMessage: async (input) => ({ clientMutationId: input.clientMutationId }),
  subscribeProjection: () => ({ close() {} })
};
```

需要验证 Effect 语义时，再对 `Layer`、`TestClock`、`Scope`、错误通道或 retry 策略做 Effect-level 测试。

Effect-first 前端优先让 action / subscription 在不渲染 React 的情况下可测：fake Layer 或 fake deps 替换真实 transport，Zustand action 只验证本地 UI transition，Query adapter 只验证 cache patch / invalidate。

## 判断法

优先 Effect：

- IO；
- 外部依赖；
- timeout / retry / cancellation；
- resource acquire/release；
- typed error channel；
- DI / fake replacement。

优先普通函数：

- DTO mapper；
- view-model transform；
- key builder；
- pure parser / normalizer；
- deterministic object merge。
