# 观测性（Logging / Tracing / Metrics）（高级进阶）

适用范围：任何需要“可排障、可解释、可回放”的 Effect 系统（CLI、daemon、HTTP server、worker、集成任务）。

目标：把“出了事如何定位”变成工程默认能力，而不是靠临时 print/猜测。

## 触发条件（什么时候需要读这份）

- 你开始关心：请求/任务的链路、失败原因、重试次数、耗时分布、资源瓶颈。
- 你发现：`--debug` 不够用；线上问题无法复现；日志分散且不可关联。

## A 类不变量（需求无关）

### A1) 日志必须可机器处理（结构化优先）

- 任何会进入长期保存/集中检索的日志都应结构化（JSON 或 key-value），而不是拼接长字符串。
- 日志字段必须稳定、可演进（允许新增；避免重命名/删除核心字段）。

最低字段建议（按重要性）：
- `level`（debug/info/warn/error）
- `msg`（简短英文句子）
- `ts`（时间戳，ISO 或 epoch）
- `component`（模块/子系统名）
- `op`（操作名，稳定字符串）
- `err`（错误形状：`code/tag/message` + 可选 details）

### A2) 必须能做“关联”

你至少需要一种关联键，贯穿一次处理链路：
- HTTP：`request_id`（或 `trace_id`）
- CLI/任务：`run_id` / `job_id` / `txn_id`
- daemon/worker：`worker_id` / `conn_id`

要求：
- 关联键在入口生成或提取，并在内部传播（不要在深层临时生成不同 id）。
- 错误日志必须包含关联键，否则定位会断链。

### A3) stdout/stderr 语义不能被观测性破坏

- CLI `--json` 模式下：日志必须走 stderr，严禁污染 stdout（见 `references/cli-contract.md`）。
- server/daemon：日志应走 stdout 或专用 sink，但不要把“业务结果输出”混在日志里。

### A4) 不要泄漏敏感信息

- secrets（token、cookie、db url 密码）不得出现在日志中。
- 对用户输入/外部响应做 redact（至少对常见字段名：`token`, `authorization`, `cookie`, `password`）。

## B 类因子（建议固化为工程模板）

### B1) 分层：业务日志 vs 平台日志

- 平台日志：进程启动、端口、依赖检查、重试策略、超时、队列长度等。
- 业务日志：某个 domain 操作的开始/成功/失败、关键输入摘要（可脱敏）、关键输出摘要。

固化建议：
- 每个命令/handler 在边界输出一次“开始/结束”日志（debug/info），内部不要到处散落 log。
- 错误只在边界统一 log 一次（避免重复打印 + 噪音淹没根因）。

### B2) 统一错误形状

把所有错误收敛成稳定 shape（与 CLI envelope 类似）：
- `code/tag`：机器码
- `message`：短句
- `details`：结构化上下文（不要塞 raw Error 对象）

收益：日志、metrics、告警都能按 code 聚合。

### B3) 让“可观测”成为可测试的契约

把关键观测点变成测试门禁：
- CLI：`--json` 不污染 stdout；`--debug` 才输出 details。
- daemon：health/status 输出包含关键状态字段（例如 pid、port、last_seen）。
- HTTP：错误响应包含稳定 code/tag（别把内部堆栈透出）。

## C 类情境因子（按需启用）

### C1) Tracing（Span）

触发条件：你需要在一次请求/任务里看“每一步耗时与失败点”。

建议：
- 用 span 包住关键边界（入口、外部 IO、DB 调用、队列写入）。
- span 上附加少量关键标签（`op`, `component`, `retry`, `timeout_ms`），不要把大 payload 全塞进去。

### C2) Metrics（计数/耗时/队列深度）

触发条件：你开始关心容量、SLO、告警阈值、性能回归。

建议最小集：
- `requests_total` / `jobs_total`（按 `op` 与 `status` 分维度）
- `latency_ms`（p50/p95/p99）
- `retries_total`、`timeouts_total`
- queue：`queue_depth`、`queue_lag_ms`

### C3) Debug log 文件（本地诊断）

触发条件：需要把调试信息持久化到文件（例如用户上报时附带日志）。

建议：
- 明确文件位置与 rotate 策略（或按日期分片）。
- 文件写入必须可失败不致命（观测性不应导致主流程失败）。

## 常见坑（建议加入“禁止模式”）

- 用 `console.log` 到处打点，然后在 `--json` 模式污染 stdout。
- 错误既在底层 log 又在入口 log，导致重复 + 根因被淹没。
- 把用户隐私/secret 直接 stringify 打到日志里（不可挽回）。
