# ADR: AI Coding OS Naming And Boundary

- Status: superseded-in-part
- Date: 2026-05-28

## Context

本仓从单一 Goal Proof 实验演进为按 decision surface 分组的 AI coding 方法套件，需要稳定品牌、Router 名称、grouped source 与可移植边界。

## Decision

- Suite 品牌使用 `AI Coding OS`。
- 用户入口为 `$ai-coding-os`，只做薄 Owner routing。
- 应用架构入口为 `$evolvable-application-architecture`。
- Canonical source 只维护 grouped layout；跨 Skill 使用 `$skill-name`，运行时不依赖 sibling path。
- 历史 Goal 方法不拥有整个 OS 品牌或当前架构语义。

## Current Disposition

品牌、Router 和 grouped-source 决定仍有效。关于 Core roster、Agent legibility、跨语言架构、ADIR、Skill evaluation 和 Suite evolution 的边界已由 2026-07-26 ADR 更新。

## Routes

- [Current SSoT](../ssot/README.md)
- [Skill Source Layout](../standards/skill-source-layout.md)
- [Current ADRs](README.md)
