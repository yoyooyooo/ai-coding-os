# ADR-0001: Semantic Owner Network

## Context

早期 Suite 拥有过多近邻 Skill，Agent 需要先区分多个相似 Owner，横向协调和重复术语增加了默认上下文成本。继续合并全部内容又会把独立问题塞回巨型工程 Skill。

## Decision

保持六个项目面向语义 Owner：Product Definition、Docs Governance、Evolvable Application Architecture、Frontend Architecture、Effect Best Practices、Product Harness System；保留一个薄 Router 和一个维护者 Evolution lens。

任何 Specialist 都可以成为第一入口。Router 不作为门禁，Evolution 不参与普通项目路由。

## Alternatives

- 一个统一工程 Skill：上下文过大，Owner 与变化轴混淆。
- 更多细分 Skill：条件分支被误升为平级 Authority，激活表面积再次膨胀。
- 中央 Workflow/Registry：用编排替代 Agent 判断，并制造新的 Current Home。

## Consequences

- 六个 Owner 的边界和局部 anchors 必须长期保持一致。
- Harness 的 UI、Headless、Frontend Test 作为同一 Proof Owner 的条件 Reference。
- Interface obligation 属于 Product 到 Frontend 的关系，不再独立成 Skill。
- 新 Skill 必须通过独立语义与变化轴检验。

## Invalidates when

真实跨项目任务持续显示某个新问题无法由现有 Owner 局部承担，且合并进任何 Owner 都会造成稳定语义混淆。
