# 可移植内核 + Actor 解释器范式（pure kernel / deterministic）

目标：把“业务状态机”做成可移植、确定性的纯逻辑（kernel），把所有 IO/计时/并发/取消放到 runtime（Actor 解释器）里；并用静态门禁锁死边界，避免项目增长后退化成“任何地方都能直接 IO”。

适用场景：
- 有长期运行状态机（daemon/WS bridge/supervisor/poller）
- 需要严格可测试（unit 测 kernel、integration 测 runtime）
- 未来可能抽包/复用（kernel 需要跨平台/跨运行时）

## 核心契约（必须）

### 1) kernel 必须是纯的、确定性的

- 禁止在 kernel 里：
  - `node:*`（fs/net/process/timers/random 等）
  - `effect/*`（Effect/Layer/Fiber/Clock 等）
  - 读取环境/全局状态
  - 直接生成随机值/时间戳（除非由事件/注入提供）
- kernel 只做：
  - 数据结构与状态推进
  - 规则裁决与命令生成（command list）

### 2) runtime 负责解释 command，并管理生命周期

runtime（Actor interpreter）是唯一允许：
- 外部 IO（网络/WS/DB/child process/fs）
- 定时/延迟（sleep/backoff/interval）
- 并发与背压（Queue、Fiber、并发度）
- 取消/超时（interrupt、timeout、signal stop）

## 推荐结构（最小可执行）

### A) kernel API：`reduce(state, event) -> { state, commands }`

- `State`：纯数据（serializable 优先）
- `Event`：纯数据（外部输入、时间点、回执、错误等）
- `Command`：对 runtime 的“意图请求”（纯数据，不带函数）

建议：
- 把所有“当前时间/窗口/随机/ID”作为 `Event` 字段传入（由 runtime 注入），保持 reducer 的确定性。
- reducer 只返回 command 的“应该做什么”，不做“怎么做”。

### B) runtime Actor loop：`Queue<Event>` + `while(true) take -> reduce -> interpret`

- 用 `Effect.scoped` + `forkScoped` 让后台 fiber 可回收
- 用 `acquireRelease` 管理资源（WS/client/db/file handles/child process）
- 用 `Stop` 事件或 signal handler 触发收敛退出（并在退出前写最后快照/清理 pid/state）

## 时间/ID 注入（关键点）

常见需要注入的东西：
- `nowMs` / `deadlineMs` / `backoffUntilMs`
- `id`（txnId/opId/connId）
- “外部状态快照”（例如 UI context / ws clients）

做法：
- runtime 在接收事件或定时 tick 时，生成 `Event` 并填入 `now`/`id`。
- kernel 只消费这些字段，不自己取时间、不自己生成随机。

## 静态门禁（建议固化为 contract tests）

最小两类门禁：

1) **kernel portability gate**
- 扫描 `src/kernel/**` 的 import specifiers
- 禁止出现 `node:` / `effect/` / `@effect/*` 等

2) **module boundary gate**
- 定义允许的依赖方向（例如 `commands -> services/runtime -> kernel`）
- 禁止 deep imports（只允许从入口文件 import）
- 允许“显式例外”必须写入 allowlist（避免暗中漂移）

提示：门禁尽量快（纯静态扫描），让它成为日常开发的“结构回归测试”。

## 落地证据：agent-remnote（remnote-mcp）

- kernel/runtime 分层：`packages/agent-remnote/src/kernel/**` 与 `packages/agent-remnote/src/runtime/**`
- 典型 Actor：WS bridge runtime（事件驱动 + state file snapshot）：`packages/agent-remnote/src/kernel/ws-bridge/**` + `packages/agent-remnote/src/runtime/ws-bridge/**`
- supervisor：kernel（restart plan）+ runtime（Queue loop）：`packages/agent-remnote/src/kernel/supervisor/**` + `packages/agent-remnote/src/runtime/supervisor/**`
- 静态门禁：`packages/agent-remnote/tests/gates/kernel-portability.contract.test.ts`、`packages/agent-remnote/tests/gates/module-boundaries.contract.test.ts`、`packages/agent-remnote/tests/gates/primitive-usage.contract.test.ts`

