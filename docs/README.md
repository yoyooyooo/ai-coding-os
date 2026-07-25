# AI Coding OS 文档网络

本目录保存 AI Coding OS Skill Suite 的当前产品定位、共享事实、架构、约束、决策、未来路线和点时证据。它是一张多入口知识网络，不是阶段目录、工作流或必读清单。

## By Question

| 当前问题 | Current Home / Evidence |
| --- | --- |
| AI Coding OS 解决什么问题 | [Product](product/README.md) |
| 当前 Suite 有哪些稳定事实和 Skill Owner | [SSoT](ssot/README.md) |
| Core、投影、ADIR、评估与演进如何组合 | [Architecture](architecture/README.md) |
| 当前必须遵守什么规则 | [Standards](standards/README.md) |
| 为什么采用这些边界 | [ADR](adr/README.md) |
| 哪些能力仍是未来候选 | [Roadmap](roadmap/README.md) |
| 本次快照做了什么、证明到哪里 | [Reports](reports/README.md) |
| 实际 Skill 内容和机械证据 | [`skills/**`](../skills/README.md) 与 release sidecars |

## Authority Model

| Layer | Owns | Must Not Own |
| --- | --- | --- |
| `product` | 产品定位、用户价值、非目标 | 架构实现细节、运行结果 |
| `ssot` | 当前共享事实、术语、Owner 和版本边界 | 未来路线、点时报告 |
| `architecture` | 当前 Suite 结构、决策与组合关系 | 产品含义、单次运行状态 |
| `standards` | 当前强制规则、验证和发布门 | 未采纳候选、历史结论 |
| `adr` | 已接受决策、替代方案和后果 | Current facts 的重复副本 |
| `roadmap` | Future candidate、晋升条件与首个可证伪步骤 | 当前已完成状态 |
| `reports` | 点时审计、来源和 Claim Ceiling | 仅因“最新”而成为 Current Authority |

每个 claim、representation 和 scope 只有一个 Current Home。源码、Schema、运行结果和外部文章可以挑战 Current Home，但不能仅凭存在自动改写它。

## Current / Target / Future

```text
current-binding / current-fact  -> 当前已接受且仍有效
accepted-target                 -> 已接受目标，但不冒充当前实现
future-candidate                -> 尚未接受，保留前提与晋升门
historical-evidence             -> 只解释过去，不参与当前路由
```

## Context Legibility

Agent 应按当前问题加载最小充分上下文：先定位语义 Owner、Current Home、直接 Evidence、material unknown 和失效条件，再读取相邻 Reference。不要预加载整套 Docs 或全部 Skills。

## Routes

- [产品定位](product/README.md)
- [当前事实](ssot/README.md)
- [架构](architecture/README.md)
- [标准](standards/README.md)
- [决策](adr/README.md)
- [未来路线](roadmap/README.md)
- [点时报告](reports/README.md)
