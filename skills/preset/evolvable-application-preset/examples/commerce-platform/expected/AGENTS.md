# Repository Agent Guide

<!-- evolvable-application-preset:begin -->
本仓库采用 `docs/standards/architecture-profile.yaml` 中声明的 Evolvable Application Preset 解析快照。

未采用的 Preset 与 Skill 默认值不能覆盖项目 authority；当前事实、规则、决策和实现证据按其 claim 类型读取。已采用的 Preset 输出归入对应项目 docs layer。

## Read First

1. `docs/README.md`
2. `docs/ssot/README.md`
3. `docs/standards/README.md`
4. `docs/standards/architecture-profile.yaml`
5. `docs/standards/source-topology-and-naming.md`
6. `docs/standards/naming-vocabulary.yaml`
7. 最近的 app/package/module README 或局部 `AGENTS.md`

## Working Rules

- 复用 `docs/standards/naming-vocabulary.yaml` 中的 canonical terms。
- 遵守 module public / host wiring 边界与事实 writer 约束。
- 不通过测试、Harness、Adapter、Worker、前端状态或直接持久化创造第二条 accepted-fact 写入路径。
- 优先复用现有 Harness；缺失时补最薄、可证伪的执行面。
- 区分实际观察、观察支持的结论与尚未证明的邻接能力。
- 只有当前事实、标准、合同、决策或拓扑变化时才更新持久文档。

## Commands

- 安装: `pnpm install --frozen-lockfile`
- 类型检查: `pnpm typecheck`
- 测试: `pnpm test`
- 架构检查: `pnpm architecture:check`
- 受影响验证: `pnpm verify:affected`
- 完整验证: `pnpm verify`

## Skill Routing

当 AI Coding OS Skill Suite 可用时，跨域或不明确任务使用 `$ai-coding-os` 作为知识路由；明确任务可直接使用专业 Skill。Skill 建议不能覆盖仓库内当前权威。

## Language

持久叙事文档使用中文；路径、命令、Schema 字段、协议名和代码符号保留 canonical 形式。

Preset profiles: agent-entry, monorepo-core, typescript-node, react, effect, effect-httpapi-v4, verification-core, headless-product-harness, ui-product-harness
Project: Commerce Platform (`commerce-platform`)
<!-- evolvable-application-preset:end -->

## Repository-Specific Notes

- 在这里补充本仓库特有命令、受限路径、生成路径、安全约束与有意偏差。
