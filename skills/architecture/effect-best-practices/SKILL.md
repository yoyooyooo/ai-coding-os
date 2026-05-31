---
name: effect-best-practices
description: >-
  Effect TypeScript best practices. Use when writing/reviewing Effect.gen, Service/Layer, error
  channels, Promise integration, timeout/retry, ManagedRuntime, Cache, SubscriptionRef,
  Config/Schema, @effect/platform, @effect/cli, Scope, or tests. Do not use for scaffolding the
  HttpApi app template; use effect-api-app-kit.
---

# Effect 最佳实践

## 快速使用

- 写/改 Effect 代码时，先对照 `references/cheatsheet.md` 的「核心不变量」与「禁止模式」。
- 采用 Effect v4 或需要从 v3 迁移时，先读 `references/effect-v4-gap.md`；本 skill 默认以当前项目本地 v4 类型为准。
- 设计内部模块组织、命名语义，或需要和项目级架构规范配合时，先读 `references/module-organization-coordination.md`。
- 当项目已经明确采用 Effect 作为总体运行时骨架时，优先遵守“外层骨架默认 Effect、内层纯逻辑保持普通函数”的分层规则；具体边界见 `references/module-organization-coordination.md` 与 `references/cheatsheet.md`。
- 当项目标记为 Effect-first 时，复杂异步、资源生命周期、可替换依赖和测试 harness 默认优先用 Effect Service / Layer / Scope / Stream / Queue 建模；具体场景模板先读 `references/async-scenario-templates.md`。
- 写/评审 Effect CLI 时，先读 `references/cli-contract.md`（A/B/C：对外契约 + 工程模板 + 情境因子）。
- 写/改涉及资源的代码（server/daemon/db/ws/child_process）时，读 `references/scope-resources.md`。
- 写测试（vitest/@effect/vitest/contract/integration）时，读 `references/testing-effect.md`。
- 写/评审 React / 前端中的 Effect 集成时，读 `references/frontend-react-integration.md`；前端目录、命名、Query / Store / UI harness 归 `$frontend-architecture`。
- 写 HttpApi（@effect/platform）时，读 `references/httpapi.md`。
- 设计 repo 与 DB 可选策略时，读 `references/repo-and-db-optional.md`。
- 需要观测性/并发背压/配置进阶/构建发布等主题时，从 `references/advanced-index.md` 进入。
- 遇到“看起来对但 TS 报错”，按 `references/cheatsheet.md` 的「冲突处理」：以本地 d.ts/TS 提示为准，再查官方源码/文档。
- 需要具体范式时，按 `references/cheatsheet.md` 的分节逐个加载。
- 维护本 skill 的 Effect v4 示例时，在本目录运行 `bun install` 后用 `bun run typecheck:examples` 校验。

## 包含内容

- `references/cheatsheet.md`：Effect 最佳实践速查（含错误语义、R/Service/Layer、timeout/retry、Promise、ManagedRuntime、Cache、SubscriptionRef、Schema/Config/HTTP 等）。
- `references/effect-v4-gap.md`：Effect v4 默认口径与 v3 迁移差异（Service、Layer.effect、Scope、ManagedRuntime、React 集成）。
- `references/module-organization-coordination.md`：与 `$meta-project-architecture` 的协同规则，以及 `repo / live / runtime` 的 Effect 映射、骨架与纯函数边界。
- `references/async-scenario-templates.md`：Effect-first 场景模板（WebSocket / SSE、HTTP client、polling、daemon / child_process、Queue / Stream、React bridge、TDD harness）。
- `references/cli-contract.md`：Effect CLI 最佳实践（A/B/C：对外契约、工程模板因子、情境固化因子）。
- `references/scope-resources.md`：资源与生命周期（Scope/Layer.effect/acquireRelease、取消/超时、避免泄漏）。
- `references/testing-effect.md`：测试范式（unit/contract/integration、timeout、FiberFailure 解包、HttpApi/CLI 黑盒测试）。
- `references/frontend-react-integration.md`：React / 前端场景中的 Effect 边界、runtime wiring、Query 集成和 fake 替换口径。
- `references/httpapi.md`：HttpApi 分层与错误策略（contract-first、handler 编排、错误映射、可测试结构）。
- `references/repo-and-db-optional.md`：Repo 抽象与 DB 可选（Service 接口、db/memory 双实现、行为一致性、集成测试门控）。
- `references/advanced-index.md`：高级进阶索引（观测性、并发背压、Config/Schema 进阶、构建发布等）。
- `examples/effect-v4-runtime-client.example.ts`：Effect v4 runtime-bound client 最小示例。
