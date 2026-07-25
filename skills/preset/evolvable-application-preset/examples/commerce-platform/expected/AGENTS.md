# Repository Agent Guide

<!-- evolvable-application-preset:begin -->
本节来自 Evolvable Application Preset 候选快照，尚未成为项目 Authority。

Preset 与 Skill 默认值不能覆盖项目 authority；当前事实、规则、决策和实现证据按其 claim 类型读取。只有经对应 semantic owner 显式采纳的内容才进入项目 Current Home。

## Knowledge Surfaces

- `docs/README.md`（存在时）索引项目 Authority 网络。
- 当前问题、code area、artifact、owning layer 和直接 Evidence 都可以作为入口。
- app/package/module README 或局部 `AGENTS.md` 只声明真实 local delta。
- Portable Skill 输出路径是候选默认值；现有项目 Current Home 优先。

## Candidate Working Rules

- 采纳后复用项目 vocabulary 中的 canonical terms。
- 只有当前事实、标准、合同、决策或拓扑变化时才更新持久文档。
- 遵守 module public / host wiring 边界与事实 writer 约束。
- 测试、Adapter、Worker、前端状态或直接持久化不能创造第二条 accepted-fact 写入路径。
- 远端投影只有一个 owner；本地 store 不镜像 server truth。
- Effect API 与运行时规则服从已安装 major 和声明文件。
- 优先复用现有 Harness；缺失时补最薄、可证伪的执行面。
- 区分 Proof Surface、依赖真实性、实际观察、支持结论与未证明项。

## Commands

- 安装: `pnpm install --frozen-lockfile`
- 类型检查: `pnpm typecheck`
- 测试: `pnpm test`
- 架构检查: `pnpm architecture:check`
- 受影响验证: `pnpm verify:affected`
- 完整验证: `pnpm verify`

## Skill Routing

当 AI Coding OS Skill Suite 可用时，跨域或不明确任务可按需使用 `$ai-coding-os`；明确任务可直接使用专业 Skill。Skill 建议不能覆盖仓库内当前权威。

## Language

持久叙事文档使用中文；路径、命令、Schema 字段、协议名和代码符号保留 canonical 形式。

Preset profiles: agent-entry, monorepo-core, typescript-node, react, effect, effect-httpapi-v4, verification-core, headless-product-harness, ui-product-harness
Project: Commerce Platform (`commerce-platform`)
<!-- evolvable-application-preset:end -->

## Repository-Specific Notes

- 在这里补充本仓库特有命令、受限路径、生成路径、安全约束与有意偏差。
