# ADR：Agent-legible Project、局部 ADIR 与 Suite 实证演进（已拆分）

- Status: Superseded by split decisions
- Date: 2026-07-26
- Scope: AI Coding OS Skill Suite 0.5 capability epoch
- Superseded by:
  - [Agent-legible AI Coding OS](2026-07-26-agent-legible-ai-coding-os.md)
  - [Cross-language EAA And Local ADIR](2026-07-26-cross-language-eaa-and-adir.md)
  - [Evidence-driven Skill Evaluation And Suite Evolution](2026-07-26-evidence-driven-skill-evolution.md)

## Historical Context

本记录曾把本轮升级的三个决定合并在同一 ADR 中：

1. AI Coding OS 从规则集合升级为面向 Agent 的项目认知、决策与验证基础设施；
2. `$evolvable-application-architecture` 收纯为跨语言语义内核，并引入局部、Earned 的 Architecture Decision IR；
3. 引入 `$skill-evaluation-system` 与 `$ai-coding-os-evolution`，以 held-out Evidence、Capability Epoch、Checkpoint 和显式发布 Authority 治理 Suite 演进。

该合并记录有助于解释本次讨论如何从 Rust 投影逐步上升到 Agent Legibility 与 Suite 自我演进，但它同时拥有多个可独立复审的决定，已不适合作为 Current ADR。

## Disposition

当前决策分别由上方三份 ADR 拥有。本文件只保留为历史来源，不拥有 Current Product、Architecture、Standard 或 Release meaning。

## Current Routes

- [Current SSoT](../ssot/README.md)
- [Architecture](../architecture/README.md)
- [Architecture Decision And Uncertainty Standard](../standards/architecture-decision-and-uncertainty.md)
- [Skill Evaluation And Release Standard](../standards/skill-evaluation-and-release.md)
