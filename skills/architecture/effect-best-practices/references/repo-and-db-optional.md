# Repo 抽象与 DB 可选策略（需求无关）

目标：让“领域逻辑”只依赖稳定接口（Effect v4 默认 `Context.Service`），而 infra（DB/网络/文件）变成可替换实现；同时确保测试与无 DB 部署形态可行。

## A 类不变量（任何项目都应满足）

### A1) Repo 以 Service + 最小接口暴露能力（DIP/ISP）

- 用 `Context.Service` 定义 repo/service 抽象。
- 接口只包含上层需要的最小方法集（不要把 DB client 透出）。
- repo 层不依赖传输层（HttpApi/Node）类型。

### A2) 错误语义：结构化、可枚举、可映射

- repo/service 的业务错误类型应稳定、可枚举（推荐 `Data.TaggedError`）。
- 禁止“抛异常当业务错误”；需要把异常映射到错误通道（例如 `Effect.tryPromise` 的 `catch`）。

### A3) 可测试性：必须有替身实现

- 每个 repo/service 至少提供一种可替身 Layer（memory/mock）。
- 测试默认用替身；真实 infra 只在集成测试覆盖关键路径。

## B 类因子（工程模板，建议固化）

### B1) live 实现只做“适配”

- `repo.live` 负责把 infra 细节（SQL、HTTP client）封装起来，并把错误映射到领域错误。
- `repo` 抽象文件只放接口与 Tag（不做 IO）。

### B2) memory 实现不是“随便写个 Map”

为了让测试可信，memory 实现应尽量对齐真实行为：
- 约束一致（唯一性、排序、分页语义等）
- 错误语义一致（例如找不到就返回 `Option.none` 或 fail `NotFound`，不要 silent）

### B3) 组装位置固定

- 入口（main/runner）负责选择注入哪个实现（db/memory/mock）。
- 上层（handler/flow）不关心选择逻辑，只依赖 Service key。

## C 类情境因子（按需启用）

### C1) DB 可选（同一套 API 支持无 DB 部署）

触发条件：需要在“无 DB（轻量代理/webhook）”与“有 DB（持久化）”之间切换。

建议固化：
- 通过配置/flag/env 选择 `RepoLiveDb` vs `RepoLiveMemory`（选择逻辑只在入口）。
- 行为差异必须被限制在 repo.live 内；HTTP 层与 contract 不因是否有 DB 而改变语义。

### C2) DB 集成测试门控

触发条件：需要验证真实 DB 行为。

建议固化：
- 用 env gate（如 `DATABASE_URL`）控制；默认跳过避免拖慢反馈。
- 每次测试使用独立 schema/临时库，避免污染与并发冲突。

## 常见坑（建议加入“禁止模式”）

- 在 handler/flow 里直接 new DB client（导致无法替换、泄漏资源）。
- repo 抽象暴露 DB client（上层开始写 SQL，边界失效）。
- memory 实现与 db 实现行为不一致（测试“绿了但线上挂”）。
