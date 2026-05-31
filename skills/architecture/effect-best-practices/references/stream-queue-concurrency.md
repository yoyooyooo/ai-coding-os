# 并发与背压（Stream / Queue / Fiber）（高级进阶）

适用范围：任何需要并发处理、持续消费、队列/流式数据、或长期运行的 Effect 系统。

目标：让并发行为“可预测、可取消、可背压”，避免隐性无界内存与难以复现的竞态。

## 触发条件

- 你开始用 `fork` / 并行组合（并发抓取、并发写入、批处理）。
- 你需要“持续消费”（daemon/worker），或需要把生产者/消费者解耦（Queue/Hub）。
- 你遇到：偶现卡死、吞吐波动、内存增长、重复处理、顺序不一致。

## A 类不变量（需求无关）

### A1) 并发必须有边界（bounded）

- 默认禁止无界并发与无界缓冲：
  - 并发数必须可配置（flag/env），并有合理默认值。
  - Queue/缓冲区必须有上限（bounded），否则背压失效、内存会线性增长。

### A2) 必须可取消（cancellable）

- 任何后台 fiber 都必须可被 scope 回收（见 `references/scope-resources.md`）。
- 任何“等待外部 IO”的步骤必须可中断并有 timeout（否则一个卡住就拖垮整个 pipeline）。

### A3) 必须可观测（可排障）

- 至少记录：
  - 并发上限
  - 队列容量与当前深度（或高水位）
  - timeout/retry 发生次数
- 这些信息应走结构化日志/metrics（见 `references/observability.md`）。

## B 类因子（工程模板，建议固化）

### B1) 明确选择：一次性并行 vs 持续消费

- 一次性并行（batch）：输入是有限集合；目标是尽快完成并退出（适合 CLI）。
- 持续消费（daemon）：输入无限；目标是稳定运行（适合 worker/bridge）。

模板差异（固化建议）：
- batch：默认必须有总 timeout；失败策略明确（fail-fast 或 best-effort）。
- daemon：必须有健康检查/停止策略；必须能优雅退场（drain 或 interrupt）。

### B2) 用“并发控制原语”而不是手写 Promise.all

建议固化的原则：
- 不要把 `Promise.all` 当并发框架（它没有背压、取消语义也弱）。
- 并发应在 Effect 层表达，才能：
  - 受 Scope 管理
  - 受 retry/timeout 组合约束
  - 在测试里可控

### B3) 分离“业务并发”与“IO 并发”

固化建议：
- 业务并发：由 domain 需求决定（例如同一实体串行、不同实体并行）。
- IO 并发：由外部系统能力决定（例如 DB 连接池、远端限流）。

把两者分开配置并在入口注入：
- `BUSINESS_CONCURRENCY`
- `IO_CONCURRENCY`

### B4) 幂等性与去重（与 C4 关联）

并发与重试会放大重复执行风险；建议：
- 写操作尽可能提供幂等键（见 `references/cli-contract.md` 的 C4）。
- 消费队列时用 idempotency store（至少 memory + 可选持久化）避免重复处理。

## C 类情境因子（按需启用）

### C1) 背压策略选择

触发条件：生产速度可能超过消费速度。

你需要显式选择策略并固化成子契约：
- `block`：生产者阻塞等待（最安全，最简单）
- `drop`：丢弃新消息/旧消息（必须能接受数据丢失）
- `sliding`：保留最新（适合 UI 状态/心跳）

一旦选择：
- 在文档/测试里锁死（例如 drop 时必须输出 dropped_count）。

### C2) 顺序语义

触发条件：你需要保证顺序（按时间/按实体）。

建议：
- 对需要顺序的 key 做“keyed serialization”（同 key 串行，不同 key 并行）。
- 把顺序语义写进 repo/service 契约，而不是靠调用方“凑巧按顺序调用”。

### C3) 批处理与限流

触发条件：外部系统有速率限制或写入成本高。

建议：
- 固化 batch size、flush interval、最大延迟（max latency）。
- 明确失败策略：部分失败如何处理（重试单条/整批）。

## 常见坑（建议加入“禁止模式”）

- 无界并发 + 无界队列（内存稳步上升直到 OOM）。
- 后台 fiber 泄漏（裸 `fork` 丢失 fiber；进程退出不了或行为越来越怪）。
- 并发写同一资源但没有顺序/锁语义（偶现数据错乱）。
