# 测试（vitest / @effect/vitest）（需求无关）

目标：让 Effect 代码的测试具备三件事——可重复、可定位、不会挂死。

## A 类不变量（任何项目都应该满足）

### A1) 测试必须可自动结束

- 禁止 watch 模式（CI/自动化里会阻塞）。
- 任何可能阻塞的测试都必须有 timeout（推荐在测试 helper 里统一设置）。
- 所有资源必须可释放（见 `references/scope-resources.md`）。

### A2) 失败必须“可读且可归因”

- 测试里运行 Effect 时，优先把 FiberFailure 解包为真实 failure（否则你只会看到一坨 FiberFailure）。
- 断言应围绕“领域错误（Data.TaggedError）/稳定 tag/message”，而不是断言整段 pretty stack。

### A3) 入口测试与库测试分层

- CLI contract tests：spawn 子进程黑盒验证（stdout/stderr/exit code/--json 单行等）。
- 业务库单测：直接调用导出的 Effect/函数（更快更稳定）。
- 集成测试：只测关键路径，用 env 开关 gate（例如 `DATABASE_URL` 才跑）。
- 若 CLI 选择 Agent-first strict protocol（`--json` 作为协议/API），contract tests 应额外锁死：`--json` 时 stderr 必须为空（包含错误场景）。
- 架构边界 contract tests：用静态扫描锁死“禁止 deep import / 禁止反向依赖”等结构性不变量（防止规模增长时边界变软）。

## 建议固化的工程模板（B 类）

### B1) 统一的 `runEffect` helper

职责：
- 运行一个 `Effect` 并返回值（或抛出解包后的错误）
- 可选地包 `Effect.scoped`，确保 finalizer 执行
- 把 timeout 作为测试默认配置的一部分（而不是散落在每个 test）

最小接口建议（伪码）：
- `runEffect(effect, { timeoutMs, scoped })`

### B2) CLI contract test helper

职责：
- `spawn(node, [...])` 运行入口
- 收集 stdout/stderr
- 强制 timeout，超时后 `SIGKILL`
- 返回 `{ exitCode, stdout, stderr }`

这能把 A 类 CLI 契约（`references/cli-contract.md`）变成可执行的门禁。

### B3) 集成测试 gate

约定：
- 用 `const describeX = condition ? describe : describe.skip` 控制套件
- 条件来自 env（例如 `DATABASE_URL`、`E2E=1`）

收益：本地默认快；需要时再跑重测试。

### B4) Effect-first 前端 harness

职责：
- 不渲染 React 也能运行 action / subscription；
- fake Layer 或 fake deps 替换真实 transport；
- 用 `TestClock` 锁死 retry/backoff/heartbeat；
- 用 `Effect.scoped` 或等价 helper 证明 finalizer / close。

建议最小用例：
- action success / typed failure；
- subscription open -> envelope -> close；
- decode failure 只进入 diagnostic / degraded；
- gap / requiresBackfill 不发明业务事实；
- close 在 open resolve 前发生时仍会释放资源。

## C 类情境因子（按需启用）

### C1) HTTP/HttpApi 黑盒测试

触发条件：你使用 `@effect/platform` 的 HttpApi 或 Web handler。

建议：
- 用 `HttpApiBuilder.toWebHandler` 构造 handler 做黑盒测试（`Request` → `Response`）。
- 必须 `dispose()`（放在 `finally`）避免资源泄漏。

### C2) DB 集成测试

触发条件：真实 DB（Postgres/SQLite）行为必须验证。

建议：
- 用 env gate（例如 `DATABASE_URL`）。
- 每个测试用独立 schema/临时库，避免互相污染。
- 测试结束清理（必要时提供 `KEEP_DB=1` 便于排障）。

## 常见坑（建议加入“禁止模式”）

- 直接断言 FiberFailure 字符串（脆弱且不可读）。
- 没有 timeout 的集成测试（卡住一次就拖垮整套 CI）。
- 忘记 dispose / close（测试间互相影响，偶现失败）。

---

## 落地证据：agent-remnote（remnote-mcp）

- CLI contract tests：`packages/agent-remnote/tests/helpers/runCli.ts`（spawn 子进程 + 收集 stdout/stderr + timeout SIGKILL）；覆盖 `--json` 单行 + stderr 为空等：`packages/agent-remnote/tests/contract/**`
- unit tests：用 `TestClock` 锁死 timeout/interrupt 的确定性：`packages/agent-remnote/tests/unit/ws-client.unit.test.ts`、`packages/agent-remnote/tests/unit/status-line-controller.unit.test.ts`
- integration-ish：受控 runtime 测试（临时目录 + 文件断言 + timeout）：`packages/agent-remnote/tests/integration/ws-bridge-runtime.integration.test.ts`、`packages/agent-remnote/tests/integration/supervisor.integration.test.ts`
- static gates：把“分层/可移植 kernel/禁止 primitive usage”做成快速 contract tests：`packages/agent-remnote/tests/gates/**`
