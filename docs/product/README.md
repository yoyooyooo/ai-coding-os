# Product

本层描述 AI Coding OS 的产品和方法论定位。

## Owns

- AI Coding OS 服务的 repository/workspace 场景与用户价值。
- 核心知识/规范网络、Owner Map、Preset、generator 和 proof surfaces 的关系。
- 核心 Suite、共仓实验和外部 execution methods 的边界。

## Must Not Own

- CLI 具体行为、实验运行状态、schema 细节、项目任务状态或未采纳计划。

## Boundary

本层回答 AI Coding OS 解决什么问题、各知识 owner 为何存在，以及默认落地边界。当前事实归 SSoT，可执行规则归 Standards，结构归 Architecture，证明归实际 Evidence。

## Current Positioning

AI Coding OS 是面向 repository/workspace 的项目级多入口知识、规范、Authority、架构、产品和 proof semantics Skill Suite。

它提供：

```text
user-invoked 知识 Owner Map
文档 Authority、Routes、Earned Shape 和生命周期治理
产品定义与产品决策
可演进应用、前端和 Effect 架构 doctrine
界面能力与 Product Harness 规划
可复用 Preset 和确定性 generator
跨 owner 的 Proof Surface 与按真实消费压力存在的方向中立 Evidence Envelope
```

核心 Suite 约束 durable semantics，但不规定 Agent 应从哪里开始、如何规划、如何拆 ticket、如何排依赖或用哪种 execution method。它默认高能力 Agent 能从适用 Authority 和局部模式推导普通可逆细节，隔离真正不可决定的 claim，并继续无关工作。清楚的 concern 直接进入 owning Skill；跨域 concern 使用 `$ai-coding-os` 找到最小 owner 集。

## External Execution Boundary

Tracker、ticket Skill、实验 Goal 方法、release process 和其他 execution systems 可以消费核心知识网络，但独立拥有：

```text
work decomposition
dependency and frontier
assignment and status
execution completion
workflow-specific artifacts
```

这些状态不能自动晋升为 Product、SSoT、ADR、Architecture、Contract、documentation lifecycle 或 release Authority。执行中产生的 durable meaning 由对应项目 owner 显式接受。

## Co-located Experiment

Goal Proof 是共仓、user-invoked、早期 execution-method 实验。它的长期有效性尚未建立，因此：

- 不属于核心 `skills/**`；
- 不进入核心 Router；
- 不随核心 Suite bundle 发布；
- CLI/npm release 与核心 Skill bundle 分开解释；
- 只在用户或项目显式选择时运行自己的状态协议。

## Promotion / Demotion

- 稳定产品定位、用户价值和非目标可以从 README、ADR 或验证证据 promote 到本层。
- 可执行规则转到 Standards；结构关系转到 Architecture；实验状态留在 experiment；迁移 delta 留在 Roadmap。

## Routes

- Public README：`../../README.zh-CN.md`
- 当前事实：`../ssot/README.md`
- 执行规则：`../standards/README.md`
- 结构视图：`../architecture/README.md`
- 核心 Skill source：`../../skills/README.md`
- Goal Proof experiment：`../../experiments/goal-proof/README.md`
