# Architecture

## Owns

- 当前 AI Coding OS Suite 的 Skill 分层、语义 Owner、组合和发布结构。
- Architecture Decision IR、Skill evaluation 与 Suite evolution 的结构关系。
- Core 与语言/生态投影之间的边界。

## Must Not Own

- 产品价值、单个项目业务语义、未来候选或模型运行结论。

## Current Views

- [Agent Legibility And Decision Control Plane](agent-legibility-and-decision-control-plane.md)：认知控制面、双闭环与 federated ownership。
- [Suite Topology](suite-topology.md)：Core、投影、Harness、Preset、Tooling 与 Meta Skills。
- [Architecture Decision System](architecture-decision-system.md)：ADIR、Decision Forest、Unknown、Commitment 与 Health。
- [Skill Evaluation And Evolution](skill-evaluation-and-evolution.md)：SkillOpt 吸收方式、评估 Gate 与 Capability Epoch。

## Architectural Invariants

```text
semantic owner != documentation home != fact authority != evidence owner
repository boundary != package/crate boundary != deployable boundary != authority boundary
memory ownership != product fact authority
source observation != accepted decision
candidate target != current implementation
successful local test != broad behavioral proof
```

## Routes

- [当前事实](../ssot/README.md)
- [架构决策与未知标准](../standards/architecture-decision-and-uncertainty.md)
- [Skill 评估与发布标准](../standards/skill-evaluation-and-release.md)
- [关键 ADR](../adr/README.md)
