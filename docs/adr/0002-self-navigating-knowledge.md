# ADR-0002: Self-Navigating Knowledge

## Context

固定阅读顺序、阶段、Hand-off Artifact 和完整模板会让高能力 Agent 先服从 Suite 再理解项目；只有 `SKILL.md -> leaf Reference` 的 Hub-and-Spoke 结构又无法从叶子恢复相邻模型。

## Decision

将 Suite 组织为自导航知识网络：主 Skill 作为语义 Owner 地图，Reference 回答稳定问题或因果关系，并在关系真正发生处提供少量 Contextual Edges。Agent 可以从需求、源码、故障、术语或局部 Reference 进入。

**Route Is an Edge, Not a Sequence.** Progressive Disclosure 控制上下文，但不规定执行 Workflow。

## Alternatives

- 强制 Router 起点：增加无意义门禁。
- 固定阶段流程：抑制高能力 Agent 的局部判断。
- 全量互链：网络噪声和检索成本过高。
- 无关联叶子：深层知识无法继续导航。

## Consequences

- 每个非终端节点只保留能改变判断的出口。
- 项目源码、命令、测试、日志和 Docs 都应成为入口。
- 主 Skill 与叶子 Reference 不得表达两代相反方法。
- 链接顺序不被解释为实施顺序。

## Invalidates when

真实使用表明上下文图无法被 Agent 稳定导航，且问题不能通过命名、入口或边质量修复。
