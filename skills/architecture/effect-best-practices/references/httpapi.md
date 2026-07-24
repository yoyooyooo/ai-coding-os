# HttpApi Architecture and Version Handoff

This reference owns HttpApi design and Effect implementation judgment. It does
not own project generation. When the user asks to initialize, add a managed
resource, or verify a Node HttpApi application, use the separate
`$effect-api-app-kit` after selecting the architecture and Effect major.

```text
Effect v3 -> @effect/platform HttpApi profile
Effect v4 -> effect/unstable/httpapi beta profile
never mix imports, builders, or Service syntax across profiles
installed package declarations and compiler output arbitrate concrete syntax
```

The generator must keep migrations outside request execution, normalize
infrastructure errors at adapter boundaries, provide memory adapters as fakes
rather than production-equivalence claims, and report real database evidence
separately.


目标：把 HttpApi 代码写成“可组合、可测试、可演进”的结构，而不是把 HTTP/DB/业务揉成一团。

## A 类不变量（任何 HttpApi 项目都应满足）

### A1) Contract-first：定义与实现分离

- `contract` 只包含：
  - `Schema`（请求/响应）
  - `HttpApiEndpoint`（method/path/name）
  - `HttpApiGroup`（组织 endpoints）
- contract 文件必须 **不做 IO**、不读取 env、不依赖 Node 平台层。

### A2) Handler 只做“编排”，不做“细节”

- handler（`HttpApiBuilder.group(...).handle(...)`）只做：
  - 参数校验（基于 Schema 的解码 + 额外业务校验）
  - 获取依赖（Service/Layer）
  - 调用领域 service/repo
  - 统一错误映射（见 A4）
- handler 禁止：
  - 写 SQL
  - 直接调用外部 HTTP client 的细节（应封装在 repo/service）
  - 在 handler 里 `provide` 一堆 Layer（依赖应在入口组装好）

### A3) Repo/Service 走 DIP：依赖抽象，不依赖 HTTP

- 用当前版本的 Service key 暴露最小能力接口（v3/v4 写法见对应 version adapter）。
- repo/service 不引入 HttpApi 相关类型，避免把“传输层语义”向下渗透。

### A4) 错误语义分层：infra → domain → transport

- infra 层错误：用结构化错误（推荐 `Data.TaggedError`），可带 `cause`。
- domain 层错误：稳定、可枚举（便于上层决定 4xx/5xx）。
- transport 层（HTTP）：
  - 只在边界做映射（handler 层）
  - 对外使用稳定 `_tag/code + message`（或等价），避免把底层错误原样透出

## B 类因子（工程模板，建议固化）

### B1) 命名稳定性

- GroupName 与 endpoint name 应稳定（改名会影响路由组织、调用方与文档）。
- handler 的 `.handle('<name>', ...)` 与 endpoint name 必须严格一致，避免“定义了但没实现/实现了但没挂上”。

### B2) 可测试结构：可替身 Layer + 黑盒 HTTP 测试

- 对真实外部能力，repo/service 应能通过 fake/memory Layer 做应用级测试；真实 DB/网络行为仍由集成测试证明。
- HTTP 测试优先黑盒（`Request → Response`），而不是直接调用内部 handler 函数。

### B3) 入口组装（main）只做 wiring

- 入口负责拼 Layer、选择 logger/middleware、启动 server；禁止写业务逻辑。
- 依赖组合优先 `Layer.mergeAll(...)` / `Layer.provideMerge(...)`，避免在 handler 内散落 provide。

## C 类情境因子（按需启用）

### C1) DB 可选（memory/db 双实现）

触发条件：同一套 HttpApi 需要在“有 DB / 无 DB”两种部署形态复用。

建议：
- `repo` 抽象固定；`repo.live` 提供两个实现：`db` / `memory`。
- 要求“对上层行为一致”（至少在 HTTP 层一致），差异封装在 repo.live 内。

### C2) DB 集成测试（门控 + 最小关键路径）

触发条件：真实 SQL 行为需要验证。

建议：
- 用 env gate（例如 `DATABASE_URL`）控制是否跑。
- 只测关键 CRUD/事务路径，不追求覆盖所有边界。

## 常见坑（建议加入“禁止模式”）

- contract 文件里做 IO（导致 `--help`/测试时也触发副作用）。
- handler 里写 SQL / HTTP client（不可测、不可复用、错误语义混乱）。
- repo/service 直接返回/抛出裸 `Error`（上层无法可靠映射）。
