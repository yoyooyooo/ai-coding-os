# Effect v4 差异口径

本 skill 默认面向 Effect v4。若项目仍固定在 v3，项目 adapter 必须显式说明，并按本文件的 v3 对照项降级。

可编译最小示例见 `../examples/effect-v4-runtime-client.example.ts`。

当前裁决来源：

- Context7 可查到 v4 文档仍支持 `ManagedRuntime.make(layer)` 与 `runtime.runPromise(effect)`。
- 本仓本地 `effect@4.0.0-beta.59` 类型显示：`Context.Service` 是 v4 service key 默认写法；`Context.Tag` 未作为当前默认 API 出现。
- 本仓本地 `Layer.ts` 明确标注：v4 `Layer.effect` 替代 v3 `Layer.scoped`，`Layer.effectDiscard` 替代 v3 `Layer.scopedDiscard`。
- 本仓本地 `Scope.ts` 明确标注：v4 `Scope.provide(scope)(effect)` 替代 v3 `Scope.extend`；`Scope.make("sequential")` 与 `Scope.close(scope, Exit.void)` 可用于手动管理一段订阅生命周期。
- 本仓本地 `ManagedRuntime.ts` 支持 `ManagedRuntime.make(layer)`；第二参数属于高级选项，写入模板前先查当前项目安装版本的 `.d.ts`。

Context7 可能返回 main branch / 旧包 README 的混合片段，例如 `Context.Tag` 或尚未进入当前 beta 的 `Effect.Service`。遇到冲突时，以当前项目安装版本的本地类型为准；不要把未被本地 d.ts 支撑的外部示例升级为 skill 默认口径。

## v4 默认写法

### Service key

默认使用 `Context.Service`：

```ts
import { Context, Effect, Layer } from "effect";

export class ChannelGateway extends Context.Service<
  ChannelGateway,
  {
    readonly fetchProjection: (
      channelId: string
    ) => Effect.Effect<ChannelProjection, ChannelError>;
  }
>()("ChannelGateway") {}

export const ChannelGatewayLive = Layer.succeed(ChannelGateway)({
  fetchProjection: (channelId) =>
    Effect.tryPromise({
      try: () => fetchChannelProjection(channelId),
      catch: (cause) => new ChannelError({ cause })
    })
});
```

保留 `yield* ChannelGateway` 获取服务；不要再把 v3 的 `Context.Tag(...)<...>()` 当新项目默认。

### Layer 与资源

无资源、同步构造：用 `Layer.succeed` / `Layer.sync`。

需要 Effect 构造或 `Scope` 资源：用 `Layer.effect`。

```ts
export const SocketGatewayLive = Layer.effect(SocketGateway)(
  Effect.acquireRelease(
    Effect.sync(() => openSocket()),
    (socket) => Effect.sync(() => socket.close())
  ).pipe(
    Effect.map((socket) => ({
      subscribe: (input) => subscribeWithSocket(socket, input)
    }))
  )
);
```

v3 对照：

```text
Layer.scoped        -> Layer.effect
Layer.scopedDiscard -> Layer.effectDiscard
Context.Tag         -> Context.Service
```

### Scope API 对照

v4 不再把 v3 `Scope.extend` 当默认写法。需要把某个 `Scope` 显式提供给依赖 `Scope` 的 Effect 时，用 `Scope.provide(scope)(effect)`；已有 closeable scope 且希望绑定使用时，可用 `Scope.use(effect, scope)` 或 `Scope.use(scope)(effect)`。

per-subscription 资源默认形态：

```ts
import { Effect, Exit, Scope } from "effect";

const openSubscription = Effect.gen(function* () {
  const scope = yield* Scope.make("sequential");
  const resource = yield* Scope.provide(scope)(
    Effect.acquireRelease(
      Effect.sync(() => openSocket()),
      (socket) => Effect.sync(() => socket.close())
    )
  );

  return {
    resource,
    closeEffect: Scope.close(scope, Exit.void)
  };
});
```

`Scope.close(scope, Exit.void)` 是订阅 facade / host close 的释放动作。facade 层仍要保证 close 幂等，并处理“open 还没完成就 close”的情况。

### ManagedRuntime

`ManagedRuntime.make` 在 v4 仍可用，适合 app root / host bootstrap 持有可释放 runtime。

关键约束：

- 传入 `ManagedRuntime.make` 的 Layer 必须已经闭合依赖，即 `Layer.Layer<R, E, never>`。
- 默认模板只写 `ManagedRuntime.make(closedLayer)`；不要为了追随外部示例主动传第二参数。
- `ManagedRuntime.make` 的第二参数在 Context7/main branch 示例与本地 beta d.ts 之间可能有差异。确实需要 `memoMap` 等高级选项时，先查当前项目安装版本的 `ManagedRuntime.d.ts` / `ManagedRuntime.ts`。
- `runtime.runPromise(effect)` 运行的是依赖 `R` 的 Effect；这是应用边界行为，不要藏进业务模块。
- 有资源的 runtime 必须在 host 生命周期结束时 `dispose()`。

```ts
import { Effect, ManagedRuntime } from "effect";

const runtime = ManagedRuntime.make(ChannelGatewayLive);

await runtime.runPromise(
  Effect.gen(function* () {
    const gateway = yield* ChannelGateway;
    return yield* gateway.fetchProjection("channel-1");
  })
);

await runtime.dispose();
```

`Effect.runPromise(effect)` 只用于已经不需要环境的 `Effect<A, E, never>`。已有 `Context.Context<R>` 时可以用 `Effect.runPromiseWith(context)`，但长期 app / React 集成优先通过 `ManagedRuntime` 或 runtime-bound client 管生命周期。

### 暂不默认 `Effect.Service`

Context7 的 main branch 示例里可见 `Effect.Service`，但 `effect@4.0.0-beta.59` 本地类型未导出该公共 API。新项目在升级到实际支持该 API 前，不把 `Effect.Service` 设为默认标准；同理，不把 `Context.Tag` 示例回灌为 v4 新项目默认。

## React 集成补充

React 集成只在 app root / host bootstrap 创建 runtime-bound client。feature、Query hook、React component 不创建 runtime，不 `provide` live Layer，不直接跑 `Effect.runPromise`。

长期结构：

```text
app bootstrap
  createLiveProductClient(config)
  owns ManagedRuntime lifecycle

packages/client
  Context.Service / Layer / transport / decode / normalized errors
  exposes Promise/subscription capability client

features/*
  query/realtime/view-model only consume client contract
```
