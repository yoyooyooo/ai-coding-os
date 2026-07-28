# Project Legibility

> **The Project Should Explain Itself.** 高能力 Agent 的可靠性首先取决于项目能否暴露真实意图、边界、入口和反馈，而不是取决于 Prompt 有多长。

## Agent-Legible Change Surface

对一个重要能力，新上下文应能够发现：

```text
Accepted Meaning or invariant
formal command/query/use-case entry
Final Materialization Authority and consistency scope
external Port / capability boundary
Composition Root and lifetime owner
smallest run or reproduction command
Observation Surface and Claim Ceiling
migration fence or old-path deletion condition when relevant
```

不是每个能力都需要一份专门文档。关系可以存在于产品知识、源码命名、类型、命令、测试、日志、Architecture 和 source-adjacent links 中；关键是它们能被恢复，而不是被一份中央表重复。

## Multi-entry discovery

健康项目允许从不同现场进入：

```text
product term -> Accepted Meaning -> use case -> source / proof
source module -> public entry -> final writer / Port / Composition Root
failing command -> original symptom -> First Wrong State -> owning contract
runtime event -> operation identity -> Unknown Outcome / reconciliation
ADR or Standard -> current source and observation that can challenge it
```

`AGENTS.md`、根 README 和 `docs/README.md` 是地图，不是唯一入口。

## Project surface before more instructions

当 Agent 反复失败时，优先检查：

```text
命名是否暴露领域概念和责任
源码边界是否让 Writer、Port 和 Host 可发现
命令是否稳定、非交互且保留第一条有用错误
测试是否能在最低正确层捕获回归
日志是否保留 operation identity、Cause、ordering 和版本
文档是否有 Current Home、Freshness 和局部路由
```

如果这些工程表面缺失，新增 Skill 提醒通常只是把不可发现性搬到 Prompt 中。

## Legibility is not verbosity

更多文档、注释和 Schema 不自动提升可读性。高质量 Legibility 来自：单一 Authority、稳定命名、局部入口、清楚依赖、真实验证和少量有意义的 Contextual Edges。
