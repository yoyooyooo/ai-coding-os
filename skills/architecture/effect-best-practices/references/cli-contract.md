# Effect CLI 最佳实践（A/B/C）

适用范围：TypeScript（Node.js）+ Effect v3 + `@effect/cli` 的命令行工具。

目标：
- A 类：把“与业务需求无关、任何 CLI 都应满足”的外部行为固化成可执行规范（并可用 contract tests 自动验证）。
- B 类：把“仍然需求无关、但更偏工程模板”的结构性因子展开（建议固化为通用 CLI 基建）。
- C 类：把“只有在特定场景才需要”的情境因子展开（按需启用，但启用后要形成子契约与测试）。

约定：本文用 MUST/SHOULD/Conditional MUST 表达强制程度；除非明确说明，否则都以 `--json` 机器模式为主线。

## 0) 范围与非目标

必须覆盖：
- 输出契约（stdout/stderr、`--json` 单行、无污染）
- 错误归一化（ValidationError / FiberFailure / 未知 defect）
- exit code 语义
- 输入与解析约定（stdin `-`、互斥参数）
- 配置与路径解析（优先级、`~` 展开、normalize）
- 可终止性（不挂死、默认 timeout）
- 薄 CLI（边界清晰、可测试）
- contract tests（锁死不变量）

不包含（交给业务/产品层自行定义）：
- 子命令集合与命名
- 领域 JSON schema / 输出字段设计
- daemon 协议细节、artifact 大输出策略、交互式 UI（这些属于情境策略，不是 A 类）

---

## A 类不变量（对外契约）

## 1) 输出契约（stdout/stderr）

### 必须（MUST）

- 提供 machine-readable 模式（推荐 `--json`）。
- machine 模式下：
  - **stdout 只输出主结果**（机器可解析）。
  - stdout **必须且只能输出一行 JSON**（`JSON.stringify(...) + "\\n"`）。
  - stdout **禁止**输出 banner、进度条、表格、多行日志、彩色文本。
  - stderr 策略必须二选一并用 contract tests 锁死：
    - **Unix-first（默认）**：stderr 输出所有非结果文本（错误、人类提示、调试、日志）。
    - **Agent-first strict protocol（Conditional MUST）**：当 `--json` 输出被当作“协议/API”消费，且上游可能合并 stdout/stderr（例如 agent / MCP / LLM runner），则 stderr **必须为空**；所有诊断信息必须进入 JSON envelope（`error.details` / `hint[]`），`--debug` 也只能扩大 envelope，不得写 stderr。
- human 模式下：
  - stdout 输出正常结果文本（可多行）。
  - stderr 只输出错误与必要提示。
- 错误文本（当输出到 stderr 时）必须：
  - 英文
  - 单行优先（必要时用 `--debug` 才输出多行细节）
  - 以 `Error:` 前缀开头（便于 grep/上游统一处理）

### 应该（SHOULD）

- 在 `--json` 模式下，注入/替换 Effect `Console`，避免 stdout 被污染：
  - Unix-first：`Console.log/info/debug/...` 默认写到 stderr
  - Agent-first strict protocol：`Console.log/info/debug/...` 默认写到“非 stderr 的诊断汇聚”（例如收集进 envelope 的 `details`，或直接丢弃并要求上层显式返回结构化诊断）
- 主输出与错误输出都保持 UTF-8；避免依赖终端颜色（ANSI）表达语义。

## 2) `--json` 的 envelope（单行对象）

### 必须（MUST）

- 成功与失败都使用 **稳定 envelope**；禁止“成功直接输出裸对象，失败输出另一种形状”。
- envelope 必须可 `JSON.parse` 且单行（不要 pretty print）。
- envelope 字段必须稳定、可向前演进（允许新增字段；禁止重命名/删除已发布字段）。
- `details`（若存在）必须是 JSON 可序列化值（禁止塞 Error/BigInt/循环引用）。

### 推荐默认 shape（可直接复用）

```ts
export type JsonEnvelope =
  | { readonly ok: true; readonly data: unknown }
  | {
      readonly ok: false;
      readonly error: { readonly code: string; readonly message: string; readonly details?: unknown };
      readonly hint?: readonly string[];
    };
```

约束建议：
- `error.code`：稳定的机器码（例如 `INVALID_ARGS` / `INTERNAL`），不要用自由文本。
- `error.message`：人类可读英文短句；不要包含堆栈。
- `hint[]`：可操作的英文建议（每条一句）。

允许替换（但要全项目统一并用测试锁死）：
- `data` vs `result` 命名
- `error.code` vs `error.tag`（但必须提供一个稳定字段充当“机器码”）

## 3) exit code 语义

### 必须（MUST）

- `0`：成功
- `2`：参数/用法错误（含 `@effect/cli` 的 `ValidationError`）
- `1`：其他失败（运行时失败、依赖不可用、未知 defect）

理由：让 shell/CI/上游工具可以稳定分流（重试、提示用户用法、报警等）。

## 4) 错误归一化（Effect / @effect/cli）

### 必须（MUST）

- 统一在 **CLI 入口（main/runner）** 做错误归一化与输出；子命令只返回 `Effect`（成功值或失败错误），避免“命令里打印 + 入口又打印”导致重复。
- 解包 FiberFailure：
  - 先判断是否是 `Runtime.FiberFailure`；若是，取 `Cause.failureOption` 的 `failure.value` 作为真实错误（若无 failure，视为 defect）。
- 识别 `@effect/cli` `ValidationError`：
  - human 模式：交给 `@effect/cli` 默认 help 输出即可（exit code 2）。
  - `--json` 模式：必须把 ValidationError 映射成失败 envelope（`ok:false`），并设置 exit code 2。
- 未知 defect（无 failure）：
  - `--json`：输出 `INTERNAL`/等价码 + 稳定 message；`--debug` 才附带 `Cause.pretty`。
  - human：输出稳定英文短句；`--debug` 才输出更详细信息。

### 建议（SHOULD）

- 定义一个项目内统一的 `CliError`（结构化错误），携带：
  - `code`（机器码）
  - `message`（英文短句）
  - `exitCode`（1/2）
  - 可选 `details`、`hint[]`
- 在边界层做错误映射：底层错误 → `CliError`；不要把 IO/平台错误裸抛到入口。

## 5) 输入与解析约定

### 必须（MUST）

- `-` 表示从 stdin 读取（适用于“payload/脚本/spec/文本”等内容参数）。
- 所有可选字符串参数都先 `trim()`；空字符串视为未提供（`undefined`）。
- 互斥参数必须显式检测并报用法错误（exit code 2），避免“最后一个 wins”导致不可预期。

### 建议（SHOULD）

- 对 stdin / payload 设置上限（字节数或条数），避免卡死或 OOM；超限用稳定错误码（例如 `PAYLOAD_TOO_LARGE`）并 exit 2。

## 6) 配置与路径解析

### 必须（MUST）

- 固化优先级：`flags > env > default`。
- 所有用户输入路径必须：
  - 支持 `~` / `~/` / `~\\` 展开
  - 解析后立即 `path.normalize(...)`
- 所有默认路径必须用 `os.homedir()` + `path.join(...)` 生成；禁止手写 `${home}/...`。
- 提供一个“打印最终解析配置”的入口（命令或 debug 输出），用于排障与 CI 固化。

## 7) 可终止性与 timeout

### 必须（MUST）

- 所有命令必须可自动结束；默认禁止 watch/常驻阻塞。
- 任何可能无限等待的外部依赖（网络/IPC/锁/daemon 响应）必须有 timeout，并允许通过 flag/env 覆盖。
- 测试与脚本必须设置超时，避免挂死 CI。

### 条件必须（Conditional MUST）

当 CLI 提供 daemon/后台进程管理能力时：
- 必须提供可验证的 `start/status/stop/health`（或等价）闭环。
- 后台进程启动必须可追踪（pid/log/state 文件或等价机制），并保证 stop 可可靠终止。

## 8) 薄 CLI（架构边界）

### 必须（MUST）

- CLI 层只做：
  - 参数解析与校验（含互斥/默认值）
  - 依赖注入与编排（Layer/Tag）
  - 错误映射为 `CliError`（或等价）
  - 输出（stdout/stderr + envelope）
- 业务逻辑与 IO 细节下沉到可复用模块（可被单测/集成测直接调用）。

## 9) contract tests（锁死 A 类）

最低覆盖建议（按优先级）：
- `--help`：exit code 0；输出包含主要子命令名（只测关键子串，不依赖 ANSI）。
- `--json` 成功：stdout 仅 1 行 JSON；`JSON.parse` 成功；`ok:true`；stderr 为空（Agent-first strict protocol）或仅包含非结果日志（Unix-first）。
- `--json` 用法错误：exit code 2；stdout 为失败 envelope；错误码稳定（例如 `INVALID_ARGS`）；stderr 为空（Agent-first strict protocol）或以 `Error:` 开头（Unix-first）。
- `--json` 运行时错误：exit code 1；stdout 为失败 envelope；错误码稳定（例如 `INTERNAL`）。
- “不挂死”：所有 CLI contract tests 都必须有超时（例如 30s），超时视为失败。

实现建议：
- 写一个 `runCli(args, { env, stdin, timeoutMs })` helper：spawn 子进程，收集 stdout/stderr，timeout 后 `SIGKILL`。

## 10) Effect/@effect/cli 实现提示（可选）

只固化“怎么做”而不是“放哪儿”：
- 使用 `Command.run(rootCommand, { name, version })` 生成 runner。
- `Effect.exit` + `Exit` 设置 `process.exitCode`，不要在子命令里 `process.exit(...)`。
- 用 `Cause.failureOption` 提取 failure；无 failure 视为 defect。
- 用 `HelpDoc.toAnsiText` + strip ANSI 把 `ValidationError` 渲染为稳定英文单行 message（用于 `--json` 模式）。

---

## B 类因子（工程模板，建议固化）

B 类仍然“需求无关”，但它们不是对外契约本身，而是让你更容易持续满足 A 类、并显著降低重复代码的工程结构因子。

### B1) 抽出统一的 CLI Runtime/Runner（单一出口）

问题：当命令越来越多，如果每个命令都自己写输出/错误处理，必然出现 stdout 污染、重复打印、exit code 不一致、ValidationError 漏处理等。

建议固化：
- 定义统一的 `CliOutput = { stdout; stderr; exitCode }`，并集中 `writeOutput(output)`：唯一允许写 `process.stdout/err` 与 `process.exitCode` 的地方。
- 定义 `renderSuccess(options, value)` / `renderFailure(options, error)`：只负责“把运行结果变成输出对象”，不触碰 process。
- 定义 `runWithOutput(options, program)`：统一做 `Effect.matchEffect`，成功走 renderSuccess、失败走 renderFailure；并把 `--json` 的 envelope 一次性落实。

强约束（SHOULD）：
- 子命令 handler 不直接写 stdout/stderr；一律返回 `Effect`（或 fail structured error）。
- 所有“unwrap FiberFailure / ValidationError”逻辑只写一份（在 renderFailure 里）。

最小 contract tests（SHOULD）：
- “不会重复报错”：同一失败只输出一次（stderr 不出现重复行；stdout 只有 1 行 JSON）。

### B2) 注入 Effect Console，隔离日志与结果（stdout 防污染）

问题：在 Effect 生态里，很多库/内部代码会用 `Console.log`；如果不处理，`--json` 模式下 stdout 很容易被污染。

建议固化：
- 在 CLI 入口根据 `process.argv.includes('--json')` 决定 console 策略：
  - `json=true`：`Console.log/info/debug` 默认写 stderr
  - `json=false`：stdout 保持人类输出
- 以 Layer 的方式注入（例如 `Console.setConsole(createCliConsole({ json }))`），确保所有 Effect 代码走同一策略。

最小 contract tests（SHOULD）：
- `--json` 成功时 `stdout` 只有 1 行 JSON（即使内部有 `Console.log`）。

### B3) 提前识别 unknown subcommand，给出更清晰的错误

问题：`@effect/cli` 的默认错误对人类还行，但对脚本/LLM/用户诊断不一定最清晰；而且不同层级的 command mismatch 信息有时不够聚焦。

建议固化：
- 在 root 层维护一个 `rootSubcommandNames` 常量数组（手动或由构建生成都行）。
- CLI 入口在真正运行 `Command.run` 前，对 `argv` 做一次轻量 guard：
  - 如果发现未知子命令：直接输出 ValidationError 风格错误（human 模式可用 help doc；json 模式输出 envelope），exit code 2。

最小 contract tests（SHOULD）：
- `unknown-subcommand` → exit code 2，stderr 以 `Error:` 开头；`--json` 下 stdout 为失败 envelope。

### B4) help 输出稳定性与可测试性

问题：help 文本通常会被拿来写 README、自动补全文档、截图比对；一旦内容不稳定（重复前缀/噪音），会拖累整个工程的可维护性。

建议固化：
- 把 `--help` 当成“半公开接口”：至少保证关键子命令名存在、不会出现明显重复（例如 `read read`）。
- 如果框架输出存在系统性瑕疵（例如重复前缀），最佳实践是：
  1) 先升级到上游最新版本确认是否已修复；
  2) 若仍存在：用包管理器的 patch 机制修复依赖（Bun `patchedDependencies` / pnpm patch / yarn patch 等），把修复“固化在依赖层”，而不是在应用入口做 stdout 拦截去重；
  3) 用 contract test 锁死 `--help` 的关键不变量，防止未来升级回归。

#### B4.1) 坑点：`@effect/cli` 多级子命令的 `--help` 重复前缀

现象（示例）：
- 当命令树出现多级嵌套（`a -> b -> c`），`--help` 的 `COMMANDS` 列表可能输出 `- a a b c`（重复了前缀）。
- 在真实 CLI 中通常表现为 `read read ...`、`write write ...` 等重复段。

最小复现（伪代码）：
- `c = Command.make('c', {})`
- `b = Command.make('b', {}).pipe(Command.withSubcommands([c]))`
- `a = Command.make('a', {}).pipe(Command.withSubcommands([b]))`
- `root = Command.make('demo', {}).pipe(Command.withSubcommands([a]))`
- `node demo.ts --help` 观察 `COMMANDS`

根因（实现层面）：
- `@effect/cli` 在构建 help 的命令列表时，递归处理 `Subcommands` 会把“已包含 preceding 的 parent usage span”再次 append 进 preceding，导致子命令路径被重复拼接。

推荐修复方式（依赖层 patch）：
- 用包管理器的 patch 能力，把修复限定在**具体版本**，避免引入运行时 hack：
  - Bun：在根 `package.json` 里用 `patchedDependencies` 指向 `patches/<pkg>@<ver>.patch`。
  - pnpm/yarn：使用各自的 patch 工作流（原则相同：版本绑定 + 自动应用）。
- Patch 的目标是修正 help usage 拼接逻辑：对子命令递归时 append 的应该是“parent 自身 usage”，而不是“包含 preceding 的 usage”。

一个可直接照抄的 Bun 示例：

```json
{
  "patchedDependencies": {
    "@effect/cli@0.73.1": "patches/@effect%2Fcli@0.73.1.patch"
  }
}
```

Patch 文件的关键 diff（示意，精简版）：

```diff
- onSome: ([usage]) => getUsage(child, Arr.append(preceding, usage))
+ onSome: () => getUsage(child, Arr.append(preceding, parentSelfUsage))
```

回归门禁（tests）：
- `--help` contract：包含关键子命令名；不包含已知重复模式（例如 `/\\bread read\\b/`、`/\\bwrite write\\b/`）。

最小 contract tests（SHOULD）：
- `--help`：包含关键子命令名；不包含已知重复模式；不依赖 ANSI。

### B5) 模块边界门禁（No deep imports / 可抽取 kernel）

问题：当命令与服务增长后，最常见的“结构性退化”是：
- 为了省事直接 import 深路径实现文件（例如 `../internal/queue/dao`），导致边界变软；
- kernel/infra 代码开始反向依赖 `@effect/cli` / 命令层，未来拆分与测试替换成本爆炸。

建议固化：
- 为每个可复用模块提供 **唯一入口**（例如 `internal/<module>/index.ts`，必要时再加一个 `internal/public.ts` 门面）。
- 约束跨层依赖只能引用入口文件：`commands/**`/`services/**` 禁止引用 internal 深层实现文件。
- 若你有“未来抽包/复用”的目标：kernel 模块（internal）应尽量保持 **Effect/CLI-free**；由 `services/**` 负责把它们适配到 Effect（错误映射、timeout、资源生命周期）。

最小 contract tests（SHOULD）：
- 增加一个快速静态扫描测试：遍历 `src/**/*.ts` 的 import specifiers，禁止 deep import（允许白名单入口）；并禁止 `internal/**` import `commands/**`/`services/**`/`@effect/cli`/`effect/*`。

---

## C 类因子（情境固化，按需启用）

C 类不是“每个 CLI 都必须有”，但一旦你的需求触发了对应情境，就应该把它提升为“子契约 + 测试”，否则极易出现安全/一致性/可靠性问题。

### C1) 破坏性/不可逆副作用 → `--dry-run` / 显式确认

触发条件：
- 命令会写入外部系统（DB/队列/远端 API）、删除/覆盖文件、发送消息、执行不可逆操作。

建议固化（Conditional MUST）：
- 必须提供 `--dry-run`（或默认 dry-run=true + `--no-dry-run/--apply` 才执行）。
- dry-run 输出必须足够让调用方确认“将做什么”（至少包含关键计数/目标/摘要）。
- `--json` 下 dry-run 仍需满足 A 类：stdout 单行 envelope。

最小 contract tests：
- dry-run 不产生真实副作用（可通过 mock/临时目录/假服务验证）。

### C2) 常驻/daemon/后台进程 → start/status/stop/health 闭环

触发条件：
- CLI 负责启动/管理后台进程、守护线程、WS bridge、长期任务等。

建议固化（Conditional MUST）：
- 必须形成可验证闭环：`start`（返回可追踪信息）/ `status`（可机器判断）/ `stop`（可可靠终止）/ `health`（探活，带 timeout）。
- 必须处理“pid stale / 重复启动 / 权限不足”等边界，并映射为稳定错误码。

最小 contract tests：
- 在隔离环境（临时目录/随机端口）下跑 start→health→stop；每步都有 timeout。

### C3) 大输出（--json 可能过大）→ 输出降级策略

触发条件：
- 预期 `--json` 会输出大对象（容易超过上游限制或拖慢解析）。

建议固化（SHOULD / Conditional MUST，取决于上游限制）：
- 选择一个稳定策略并固化：
  - `--out <path>`：把完整 JSON 写文件，stdout 只输出引用；
  - 或 artifact store：输出 `{ artifact_path, sha256, bytes, excerpt, response_truncated }`；
  - 或 `--json-file` 专用开关。
- 不管策略如何，stdout 仍必须是一行 JSON（A 类）。

最小 contract tests：
- 构造超大结果，验证触发降级且 stdout 仍单行可 parse。

### C4) 重试/幂等性（写操作可重复调用）→ idempotency key

触发条件：
- 写操作可能被调用方重试（网络抖动、超时、CI 重新跑、LLM 重发）。

建议固化（Conditional MUST）：
- 提供 `--idempotency-key`（或等价）与可选 `--client-id`，并保证底层真正用它去做幂等去重。
- 明确幂等边界：同 key 的重复调用返回“同结果”或“可判定的重复”。

最小 contract tests：
- 相同 idempotency key 连续执行两次：第二次不产生重复副作用，输出可预测。

### C5) 多上下文/多目标（多实例、多工作区）→ 显式上下文选择 + 可观测

触发条件：
- CLI 可能作用于多个目标实例（多 server、多 workspace、多 repo、多 profile）。

建议固化（Conditional MUST）：
- 提供显式选择参数（例如 `--server/--profile/--workspace` 等），并规定默认选择规则。
- 提供 `config print`（或等价）输出“最终解析后的上下文”，便于排障与脚本固化。
- 禁止静默选择“危险默认值”（例如默认写入生产），默认必须保守。

最小 contract tests：
- flags/env/default 的优先级可被验证；冲突参数报 exit code 2。

---

## 落地证据：agent-remnote（remnote-mcp）

可作为“真实工程可运行样例”对照本文件的 A/B/C：

- A 类（`--json` 严格协议 + stderr 为空 + strict argv 预检）：`packages/agent-remnote/src/main.ts`；对应门禁：`packages/agent-remnote/tests/contract/invalid-options.contract.test.ts`、`packages/agent-remnote/tests/contract/invalid-command.contract.test.ts`
- 配置与路径解析（flags/env/default 优先级、`~` 展开/normalize、禁止 env 注入）：`packages/agent-remnote/src/services/CliConfigProvider.ts`、`packages/agent-remnote/src/services/Config.ts`
- file spec 统一解析（`@file` / `-` / `~`）：`packages/agent-remnote/src/services/FileInput.ts`；单测：`packages/agent-remnote/tests/unit/file-input.unit.test.ts`
- 架构边界静态门禁（分层/portable kernel/禁止 primitive usage）：`packages/agent-remnote/tests/gates/**`
- 多上下文可观测（`config print` 输出最终解析值）：`packages/agent-remnote/src/commands/config/print.ts`
