# ADR-0001: Adopt Evolvable Application Preset

- Status: accepted
- Date: 2026-07-23

## Context

本项目希望复用稳定的 authority-first、Monorepo/reference topology、Bounded Semantic Flatness、语义词汇与 Harness 默认值，同时让项目内 Docs 保持当前权威。

## Decision

采用 Evolvable Application Preset `1.0.0-experimental.1`，profiles：agent-entry, monorepo-core, typescript-node, react, effect, effect-httpapi-v4, verification-core, headless-product-harness, ui-product-harness。
Preset 以 `resolved-snapshot` 模式渲染；项目 `AGENTS.md` 与 `docs/**` 是当前权威。

## Consequences

- 通用规则不需要每个项目重新讨论。
- 项目仍必须填写自身产品语言、authority、实际拓扑与例外。
- Preset 升级必须显式比较并采纳，不能动态覆盖当前标准。
