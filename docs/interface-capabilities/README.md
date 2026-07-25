# Interface Capabilities

本层保存项目级界面能力合同：用户要完成什么、入口和 surface 是什么、交互状态与前端 owner 如何分配、需要哪些证明。

## Owns

- `InterfaceCapability`：用户工作、入口、交互合同、状态/数据归属和 coverage intent。
- `InterfaceSurface`：surface / region 到 capability 的索引。
- Capability 到 Product、SSoT、Design、Architecture 和 Harness IDs 的引用。
- 从任意 source、proposal 或 execution method 显式 promote 的稳定界面能力语义。

## Must Not Own

- Product、domain、API 或数据库事实。
- HarnessScenario、fixture、route、component 或 raw Evidence 的完整定义。
- 具体 test runner、Playwright/browser steps、fixture data 或 mock handlers。
- 最终 visual design。
- Tracker、ticket、Goal、release 或其他 execution state。

## Boundary

`InterfaceCapability` 可以声明 proof needs 和 `coverage_intent`，但只引用 Harness IDs 或所需 Proof Surface，不复制完整 proof design。

```yaml
coverage_intent:
  required_harness:
    - hs.channel.issue-from-message
  required_surfaces:
    - interface_headless
    - browser
```

完整 Harness contract 放 `docs/product-harness/**`；执行结果留在 owning test/Harness/evidence surface。`InterfaceCapability.status` 只表达 definition lifecycle：`sketch | candidate | accepted | retired`。Product/design owner 接受定义；Harness pass、delivery completion 或 regression 不能自动改变该状态。

## Promotion / Demotion

任何 workflow/source 产生的候选稿只有经项目文档 Authority 接受后才进入本层。Promotion 保留 source 和 Evidence links，但不复制外部 workflow status。

一次性验证脚手架、未产品化 candidate 或被新 capability 吸收的内容，留在 source/report 或标记 retired；不在本层保留两份 Current definition。

## Conflict

按 question-scoped Authority 处理：Product/SSoT 拥有用户和业务意义；本层拥有 interface capability projection；Architecture/Frontend 拥有技术 topology；Harness/Test 拥有 proof implementation。不存在统一文件顺序。

## Routes

- Harness contract：`../product-harness/README.md`
- 文档网络：`../README.md`
- 当前事实：`../ssot/README.md`
- 文档治理：`../standards/docs-governance.md`
