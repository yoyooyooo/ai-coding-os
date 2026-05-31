# 资源与生命周期（Scope / Layer.effect）

适用范围：Effect v4 的任何长期运行或涉及外部资源的代码（HTTP server、daemon、DB 连接、文件句柄、child process、WebSocket、定时任务）。v3 项目把本文的 `Layer.effect` 对照为 `Layer.scoped`。

目标：把资源释放、取消、超时变成“默认正确”，避免泄漏与不可控的常驻阻塞。

## A 类不变量（需求无关，应该默认成立）

### A1) 资源必须有明确生命周期

- 任何需要释放的资源都必须绑定到 `Scope`：
  - 用 `Effect.acquireRelease` / `Effect.acquireUseRelease`，或
  - 用 `Layer.effect`（推荐：把资源封装成服务的 Live Layer）。
- 不要把“需要释放”的东西放进全局单例（模块顶层 `const client = ...`）然后指望进程退出时自动回收。

WebSocket / EventSource / worker / daemon bridge 属于资源型能力。Effect-first 项目中，这类 live 实现默认应由 `Layer.effect`、`Effect.acquireRelease` 或 scoped subscription facade 管理；React hook 只负责调用已经 runtime-bound 的 `subscribe` 并在 unmount 时 close。

per-subscription 资源不要挂在 app-level runtime 全局 scope 里。推荐拆分：

```text
app-level runtime
  owns global deps / config / service Layer

each subscribe()
  creates independent Scope.make("sequential")
  registers resource with Scope.provide(scope)(Effect.acquireRelease(...))
  returns facade close -> Scope.close(scope, Exit.void)
```

facade 的 `close()` 必须幂等。允许 open Promise 未完成前先 close；open 完成后仍要触发 finalizer，不能留下 WebSocket / EventSource / worker。

### A2) 取消与超时是协议的一部分

- 任何可能无限等待的外部 IO（网络、IPC、锁、队列、daemon 响应）必须能被中断，并提供 timeout：
  - timeout 的默认值要保守（让命令“可自动结束”）。
  - timeout 必须可被 flag/env 覆盖（便于 CI/慢环境）。

### A3) “入口”负责收口生命周期

- 入口（CLI `main.ts` / server `main.ts`）必须是唯一负责：
  - 组装 Layer
  - 运行 `Effect`（并设置 exit code）
  - 处理失败/defect 的统一输出
  - 确保 scope 结束时触发 finalizer
- 业务模块内部禁止 `Effect.runPromise` / `process.exit(...)`（会破坏可测试性与资源释放）。

## 常用实现因子（可固化为工程模板）

### Layer.effect：把资源“服务化”

推荐：对外暴露 `Context.Service` 的最小接口；Live 里用 scoped effect 方式申请/释放资源。

关键收益：
- 调用方不用关心关闭逻辑
- 测试时可替换为 memory/mock layer
- 入口只需要 `Layer.mergeAll(...)` / `provide(...)`

### Effect.acquireRelease：最小可控封装

适合在一个函数内部临时打开/关闭资源（例如：读一次文件、做一次网络请求但需要显式 teardown）。

长期订阅场景里，可把 `Effect.acquireRelease(...)` 注册到手动创建的 scope：

```ts
const scope = yield* Scope.make("sequential");
const resource = yield* Scope.provide(scope)(
  Effect.acquireRelease(acquire, release)
);

return {
  resource,
  closeEffect: Scope.close(scope, Exit.void)
};
```

约束：
- `release` 必须“幂等且不会抛出”（失败也要吞掉或转换为可控错误）。
- 释放应该放在 error 通道之外（finalizer 不应再失败污染主错误）。

### forkScoped：后台 fiber 必须可回收

当你真的需要后台 fiber（polling、订阅、心跳）：
- 用 `Effect.forkScoped` 或者等价方案确保 scope 结束时自动 interrupt；
- 禁止裸 `Effect.fork` 后把 fiber 丢掉（会泄漏）。

## 常见坑（建议写进“禁止模式”）

- 资源申请在模块顶层执行（import 即副作用），导致测试/CLI 帮助输出时也创建连接。
- 在库函数里 `Effect.runPromise`，导致调用方无法注入 Layer、无法控制取消/重试、无法回收资源。
- 用 `Effect.promise` 包装会 reject 的 Promise，然后把 reject 当作“业务错误”（reject 是 defect，错误通道是 `never`）。

## 测试提示（与 `references/testing-effect.md` 配合）

- 有资源的测试优先用 `Effect.scoped` 包住整个 program，确保 finalizer 一定跑到。
- 对“可能卡住”的测试强制 timeout（测试 helper 层面统一做，而不是每个 test 手写）。
- WebSocket / subscription 测试优先 fake Layer + TestClock + scoped finalizer：证明 open、decode failure、retry/backoff、close、提前 close 后 open 完成也会释放。

---

## 落地证据：agent-remnote（remnote-mcp）

- WebSocket client（可中断连接 + timeout + acquireRelease）：`packages/agent-remnote/src/services/WsClient.ts`（`Effect.async(..., AbortSignal)` + `Effect.acquireRelease`）；单测：`packages/agent-remnote/tests/unit/ws-client.unit.test.ts`
- 子进程资源（spawn + 等待 + 释放时 TERM→等待→KILL）：`packages/agent-remnote/src/services/ChildProcess.ts`（释放阶段必须先发信号并等待 outcome，再做 listener cleanup，避免中断卡死）
- 守护循环（Queue + forkScoped + 信号 stop + 文件落盘）：`packages/agent-remnote/src/runtime/supervisor/runSupervisorRuntime.ts`；集成测：`packages/agent-remnote/tests/integration/supervisor.integration.test.ts`
- 外围 IO 收口（subprocess/worker）：`packages/agent-remnote/src/services/Subprocess.ts`、`packages/agent-remnote/src/services/WorkerRunner.ts`（统一超时、可诊断字段、资源释放）
