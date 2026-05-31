# Effect 最佳实践速查

## 冲突处理（优先级）

- 优先相信当前项目的 TypeScript 类型提示（含本地 d.ts）与编译器报错。
- 若与“固有记忆”冲突：以本地类型为准，再查官方源码/文档。
- 自动化跑测试或脚本时，避免 watch 模式（防止常驻阻塞），优先一次性 run。
- 新项目默认 Effect v4；若项目仍固定 v3，必须在项目 adapter 中显式说明。v4/v3 差异先看 `references/effect-v4-gap.md`。

## 核心签名与泛型顺序

- `Effect.Effect<A, E = never, R = never>`：成功值 / 业务错误 / 依赖环境（顺序不可调）。
- 可用调用方顺序别名：`type Fx<R, E, A> = Effect.Effect<A, E, R>`（底层仍是 `Effect.Effect<A, E, R>`）。
- 设计公共 Flow / 库函数时，优先暴露可扩展环境：`<R>() => Effect.Effect<A, E, R>`，由调用方用 Layer 提供环境实现。

## 环境 R 与 Service/Layer

- 将 `R` 理解为“按需注入的服务集合”；在类型上是逆变：依赖更少的 Effect 可赋给依赖更多的地方，反之不行。
- v4 推荐 service key class 写法：`class X extends Context.Service<X, Service>()("X") {}`
- 在 `Effect.gen` 中用 `yield* X` 获取服务；用 `Layer.succeed(X)(impl)` / `Layer.succeed(X, impl)` 或 `Effect.provideService` 提供实现。
- v3 项目才使用旧 `Context.Tag` 口径；不要把它作为新项目默认示例。

## Context / Env 使用边界

- runtime/middleware 层可用 `Effect.context<R>()` 做 Context 级操作（约束管道、调试工具等）。
- 业务 Flow / Service 层避免显式构造/传递 `Context.Context`（胖 Env）；一律用 service key 按需获取：`yield* Logger` 等。

## 骨架与纯函数边界

- 总体运行时骨架默认用 Effect。
- 纯计算、纯转换、纯建模代码默认保持普通函数。
- 可失败但无副作用的纯逻辑，优先返回 `Option / Either / ParseResult`，只有在外层需要统一编排时再提升到 Effect。

典型适合保持普通函数的内容：

- schema normalize
- front matter 解析后的数据整形
- manifest merge
- ranking score 合成
- canonical ref 拼装
- locator / mapper / parser

典型适合放在 Effect 骨架里的内容：

- CLI / MCP / HTTP handler
- repo / gateway / provider 调用
- timeout / retry / fallback
- 文件系统 / 网络 / 子进程 IO
- 资源生命周期与 Scope

建议避免的坏味道：

- 对纯函数结果层层包 `Effect.succeed`
- 让普通函数直接触碰外部依赖
- 在 mapper / parser 中混入日志、重试、降级等运行时语义

## timeout / retry

- 使用对象参数 + `pipe`：`effect.pipe(Effect.timeoutFail({ duration, onTimeout }))`；避免旧版多参数形态。
- `Effect.retry` 接收配置对象（如 `{ times: 3 }`），不会改变环境 `R`；优先在通用约束层封装重试，而不是散落在每个业务 Flow 内。

## Promise 集成与错误语义

- `Effect.promise(evaluate)` 的错误通道类型为 `never`；Promise reject 被视为 defect。
- 需要业务错误通道时，使用 `Effect.tryPromise` 并在 `catch` 中把异常映射为领域错误 `E`。
- 领域错误 `E` 应语义化（领域/校验/可透出），避免直接冒泡 `unknown` 或裸 `Error`。

## 运行入口与 Layer 组合

- `Effect.runPromise` 等 run API 默认期望环境为 `never`；带依赖的 Effect 先 `Effect.provide(...)`/`Effect.provideService(...)` 注入完整 Layer 再运行。
- Layer 组合：`Layer.succeed(Service)(impl)` 或 `Layer.succeed(Service, impl)` 提供实现；再用 `Layer.mergeAll(...)` / `pipe(layer, Layer.provide(...))` 聚合。
- `ManagedRuntime.make` 的 layer 第三个泛型必须是 `never`；不要把仍带依赖的 Layer 直接交给它。
- v4 可用 `Effect.runPromiseWith(context)` 运行已有 `Context.Context<R>` 的 Effect；长期 app/runtime 仍优先用明确 owner 管理 `ManagedRuntime`。

## Runtime-bound facade

- Effect-first 子包内部可以大量使用 Service / Layer / Scope；包出口默认暴露 runtime-bound 普通 facade。
- `createXClient(config)` / `makeXDeps(config)` 是 composition root：一次性归一化 host deps，创建 closed Layer / ManagedRuntime，再导出 Promise function 或 subscription facade。
- 不要为了避免 Effect 类型外泄，把 `config`、`fetchImpl`、`WebSocketImpl` 等依赖塞进每个 operation input 或 helper 参数。
- operation helper 应只接收业务 input；可替换依赖从 Service 获取。
- `runtime.runPromise(...)` 不应散落在业务库函数里，只放在明确入口或 runtime-bound facade。
- 若调用方本身是 Effect 程序，可以额外提供 Effect-native API；不要让普通 React / feature consumer 被迫 import Service key 或 Layer。

## Cache 泛型（Environment）

- `Cache.make<Key, Value, Error = never, Environment = never>`：`Environment` 表示 lookup 过程中额外需要的环境。
- 通过闭包捕获 Service 时，尽量保持 `Environment = never`（不要写成 `typeof SomeService`）。
- 若 `Value` 的错误类型是领域错误，但对外希望“永不失败”，在边界用 `Effect.catchAll(() => Effect.succeed(default))` 收敛，再暴露 `Stream<_, never, _>`。

## SubscriptionRef

- 将其视为“可订阅 Ref”：读写都用模块函数，而不是实例方法。
- 写入：`SubscriptionRef.set(ref, value)` / `SubscriptionRef.update(ref, f)`；订阅变化：`ref.changes`；不要假设存在 `ref.set/ref.get`。

## Effect.gen 推荐写法

- 在业务 Flow 中统一使用 service key 的 `yield*`：`Effect.gen(function* () { const svc = yield* ServiceKey; ... })`。
- 避免旧式的 `_` 适配器等 `yield* _(Tag)` 风格，减少 `R` 推导污染（`unknown`/`never`）。

## Schema / Config / HTTP 解码

- Schema 统一从 `effect` 导入：`import { Schema } from 'effect'`（避免与 `@effect/schema` 混用）。
- 领域模型推荐 `Schema.Struct({ ... })`；类型通过 `Schema.Schema.Type<typeof X>` 或 `typeof X.Type` 推导。
- Config 读取：`Config.xxx('KEY').pipe(Config.withDefault(...))`；在 `Effect.gen` 中用 `yield* Config.xxx(...)`，避免旧版 `Effect.config(...)`。
- HTTP 解码优先 `HttpClientResponse.schemaBodyJson(effect/Schema)`。
- `Schema.Array(X)` 返回 `ReadonlyArray`；若需要可变数组，显式 `Array.from(...)`。
- Service key 的方法签名与实现必须严格一致（数组可变性、错误类型、环境类型）。

## CLI 对外契约（@effect/cli，可选）

- 把 `--json` 当作对外协议：stdout 单行 JSON envelope；stderr 承载错误/日志；exit code 固定 `0/2/1`。
- 统一错误归一化：解包 FiberFailure；ValidationError 在 `--json` 下也要输出 envelope；未知 defect 用稳定错误码（例如 `INTERNAL`）。
- 统一输入与配置：stdin 用 `-`；互斥参数显式检查；`flags > env > default`；路径支持 `~` 展开并 `normalize`。
- 所有命令必须可自动结束并有 timeout；用 contract tests 锁死这些不变量。
- 常见坑：`@effect/cli` 在多级 `Command.withSubcommands(...)` 下的 `--help` 命令列表可能出现重复前缀（例如 `a a b c` / `read read`）。最佳实践是用包管理器的 patch 机制修复依赖（Bun `patchedDependencies` / pnpm patch 等），而不是在入口做 stdout 拦截去重；并用 contract test 锁死 `--help` 的关键不变量。
- 当项目开始模块化（命令/服务/kernel 分层）时：用静态门禁锁死架构边界（禁止 deep import、禁止 kernel 反向依赖 CLI/Effect），避免规模增长后边界变软。
- B/C（工程模板与情境因子）也在 `references/cli-contract.md`。

## 资源与生命周期（Scope，可选）

- 任何需要释放的资源必须绑定 `Scope`（v4 用 `Layer.effect` / `Effect.acquireRelease`；v3 对照为 `Layer.scoped`），禁止模块顶层隐式创建连接/句柄。
- 后台 fiber 必须可回收（优先 `forkScoped`）；所有外部 IO 必须可中断并有 timeout。
- 详见 `references/scope-resources.md`。

## 测试范式（vitest/@effect/vitest，可选）

- 测试必须可自动结束：统一 timeout；资源必须可释放；避免 watch。
- 断言围绕结构化领域错误（解包 FiberFailure），避免断言整段 runtime 文本。
- 详见 `references/testing-effect.md`。

## HttpApi 分层（@effect/platform，可选）

- contract-first：Schema/Endpoint/Group 不做 IO；handler 只编排；repo/service 不依赖 HTTP。
- 错误语义分层：infra → domain → transport；错误映射只在边界层做。
- 详见 `references/httpapi.md`。

## Repo 与 DB 可选（可选）

- 用 `Context.Service` 暴露最小接口；db/memory 双实现对上层行为一致；选择逻辑只放入口。
- 详见 `references/repo-and-db-optional.md`。

## 高级进阶（按需加载）

- 观测性（Logging/Tracing/Metrics）：`references/observability.md`
- 并发与背压（Stream/Queue/Fiber）：`references/stream-queue-concurrency.md`
- Config/Schema 进阶：`references/config-schema-advanced.md`
- 构建与发布（Node/TS/ESM/CJS/bin）：`references/build-and-release.md`
- 入口索引：`references/advanced-index.md`

## 禁止模式（常见坑）

- 把 `Effect.Effect` 的泛型顺序写成 `Effect.Effect<R, E, A>`，或据此设计别名。
- 在业务层直接操作 `Context.Context` 构造/传递胖 Env。
- 使用旧版 API 形态（如 `Effect.timeoutFail(effect, ...)`、`Effect.config(...)`），或误以为 Promise reject 会走业务错误通道。
- 在 `@effect/platform` 的 HTTP 解码里混用 `@effect/schema` 与 `effect/Schema`，或把 `ReadonlyArray` 直接赋给 `Array`。
- 定义 Service key 时契约与实现不一致（尤其数组可变性、错误类型、环境类型）。

## 命名约定

- 统一 `*.make` 风格强调构造语义；避免 `*.define`。
