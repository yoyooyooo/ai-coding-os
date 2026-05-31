# 高级进阶索引（按需加载）

目标：把“非入门但仍需求无关、可固化”的主题放在独立文档里，避免把 `cheatsheet.md` 变成大杂烩；当你遇到对应触发条件时再加载。

## 选择指南（先问自己）

- 需要把日志/trace/metrics 做成可诊断的系统？→ `references/observability.md`
- 需要处理并发、背压、队列/流、长期运行的订阅/轮询？→ `references/stream-queue-concurrency.md`
- 需要把配置/Schema 做成“可演进、可定位错误、可复用”的基础设施？→ `references/config-schema-advanced.md`
- 需要把 Node CLI/服务的构建、发布、dist 组织、ESM/CJS、bin 入口做成稳定工程？→ `references/build-and-release.md`
- 需要做“可移植内核（pure kernel）+ Actor 解释器 + 时间/ID 注入 + 静态门禁”？→ `references/portable-kernel-and-actors.md`

## 与其它文档的关系

- CLI 行为协议：`references/cli-contract.md`（A/B/C）
- 资源生命周期与泄漏：`references/scope-resources.md`
- 测试范式：`references/testing-effect.md`
- HttpApi 分层：`references/httpapi.md`
- Repo/DB 可选：`references/repo-and-db-optional.md`

## 建议的使用方式（最短）

1) 先按 `cheatsheet.md` 做到“核心不变量 + 禁止模式”不再踩坑。
2) 再按“触发条件”打开一个高级文档，只解决当下问题。
3) 最后把你做出的裁决（例如 envelope 字段、超时默认值、log 结构）写进项目内的 SSoT/README 或测试里锁死。
