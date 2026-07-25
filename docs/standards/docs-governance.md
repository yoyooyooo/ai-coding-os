# Docs Governance Standard

本标准是 `$docs-governance` 在本仓的 adopted project surface。

## Owns

- `docs/**` 的 Authority、Routes、Earned Shape、生命周期、freshness 和 cleanup。
- Current / accepted-target / future / historical 分类。
- Durable assumption 的 owner、scope、safe boundary 与 invalidation point。
- Context Legibility 与最小充分发现路径。

## Must Not Own

- Product、Architecture、安全、法律、发布或执行决定本身。
- Tracker、Ticket、Agent loop 和 Workflow state。
- Skill 领域语义；归相应 Skill Owner。

## Core Contract

```text
Authority  one canonical Current Home per claim, representation, and scope
Route      discoverable edge, never mandatory reading order
Earned Shape
           layers, partitions, identities, registries and schemas appear under real pressure
Evidence   source/runtime/test/release evidence bounds current claims
```

## Claim Classification

关键 claim 至少区分：

```text
claim class      current-fact | current-binding | accepted-target |
                 future-candidate | source-input | historical-evidence
knowledge basis  accepted | observed | source-derived | inferred | assumed | unknown
evidence state   not-proven | partial | verified | released
semantic owner   one current owner for the scoped meaning
invalidates when source/version/decision/migration/environment/time condition
```

这些字段不必机械出现在每份 Markdown，但治理时必须保持语义非等价。

## Layer Admission

当前层只有：Product、SSoT、Architecture、Standards、ADR、Roadmap 和 Reports。不存在当前内容的分类外壳不保留。新增 layer 需要独立 Authority role；新增 partition 需要 ownership、安全、保留、生命周期、发布或持续路由压力；新增 ID/Registry 需要引用、追踪或机器消费压力。

## Convergence

```text
promote | demote | split | merge | partition | flatten
bridge | retain | delete | block
```

- Stale map 必须 re-ground、标记 drift、降级或 supersede；不能因文件仍存在而继续持有 Authority。
- Durable assumption 必须有 owner、scope、不能跨越的 commitment、expiry/invalidation 与 next probe/decision。
- `block` 只阻塞受影响 claim 或 mutation；无关工作继续。
- Router 只保存 Route，不复制 Current Truth。
- 点时 Report 不能仅因“最新”成为 Current Home。

## Context Legibility

每个高频入口应以低 Context Cost 暴露：用途、scope、owner、Current/Target/Future、直接 Evidence、失效条件和下一跳。主 `SKILL.md` 保留稳定 Owner、不变量、Stop Line 和 Reference 路由；边缘知识下沉并按需加载。

## Audit

```bash
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo . --readability
```

Scanner 证明路径、链接、形状和声明式规则的机械一致性；不自动决定产品或架构语义。

## Routes

- [文档网络](../README.md)
- [当前事实](../ssot/README.md)
- [Skill Source Layout](skill-source-layout.md)
- [Snapshot Report](../reports/2026-07-26-snapshot-convergence.md)
