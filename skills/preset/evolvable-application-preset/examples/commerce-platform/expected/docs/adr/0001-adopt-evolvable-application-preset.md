# ADR-0001: Proposed Evolvable Application Preset Adoption

- Status: proposed
- Date: 2026-07-23

## Context

本候选解析所选 profiles 的最小默认值，供项目 semantic owners 审阅；未选择领域不进入候选快照。

## Proposed Decision

建议采用 Evolvable Application Preset `1.4.0-experimental.1`，profiles：agent-entry, application-core, monorepo-core, typescript-node, react, effect, effect-httpapi-v4, verification-core, headless-product-harness, ui-product-harness。
Renderer 只生成 `candidate-snapshot`；各内容只有在对应 owner 审阅并合入 Current Home 后才成为项目 Authority。

## Consequences If Adopted

- 通用规则不需要每个项目重新讨论。
- 项目仍拥有产品语言、fact authority、实际拓扑与例外。
- source naming 只引用项目 SSoT 的产品词义，不复制第二份定义。
- Preset 升级必须显式比较并采纳，不能动态覆盖当前标准。
- docs layer 可按项目需要省略；二级目录和 identity 字段必须经过 `$docs-governance` 的 earned-shape 判断。
