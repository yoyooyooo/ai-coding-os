# 构建与发布（Node/TS + Effect）（高级进阶）

适用范围：当你的 Effect 项目开始需要稳定的 dist 产物、可安装的 CLI、或可部署的服务。

目标：把“能跑”提升为“可发布、可调试、可升级、可回滚”。

## 触发条件

- 你需要 `bin`（全局命令）、`dist/` 产物、或发布到 npm/private registry。
- 你开始关心：ESM/CJS 兼容、sourcemap、版本号、跨平台路径、依赖外置/打包策略。

## A 类不变量（需求无关）

### A1) 入口必须稳定且可测试

- CLI 入口：
  - 必须有稳定的可执行文件（`bin` 指向 dist）
  - `--help` 必须可运行且不触发副作用（不要在 import 时启动连接/daemon）
  - `--json` 输出契约必须被 contract tests 锁死（见 `references/cli-contract.md`）

### A2) 源码与产物要有清晰边界

- `src/`：TypeScript 源码
- `dist/`：可发布产物（JS + 需要的资源）
- 测试默认跑源码（更快、更易调试）；发布时跑 dist（验证产物可用）

### A3) 版本号必须可用且不依赖外部工具

- `--version`（或 `Command.run({ version })`）必须能在 dist 环境下工作。
- 版本号读取应从打包后的 `package.json` 或构建注入常量获取，避免依赖 git。

## B 类因子（工程模板，建议固化）

### B1) ESM vs CJS 的决策与一致性

固化建议：
- 项目选择一种模块系统作为主线（ESM 或 CJS），并让：
  - tsconfig、package.json（`type`/`exports`）、构建命令、运行方式保持一致
- 不要在同一包里混乱输出（除非你明确需要双产物并能维护）。

### B2) CLI 开发/发布双模式

固化建议：
- dev：用 tsx/ts-node/bun 直接跑 `src/main.ts`（快）
- release：用构建产物跑 `dist/main.js`（验证真实发布路径）

### B3) sourcemap 与错误定位

固化建议：
- 发布产物带 sourcemap（或至少在 debug 构建带），否则线上堆栈不可读。
- `--debug` 下允许输出更详细的错误细节（但仍遵守 stdout/stderr 契约）。

### B4) 依赖外置策略

固化建议：
- Node 内置模块永远外置。
- 体积大/需要原生模块的依赖倾向外置（减少打包复杂度）。
- 对 `optionalDependencies` 与平台差异要显式处理（错误码 + hint）。

### B5) 非 JS 资源（SQL/模板）与 bundling（import.meta.url）陷阱

问题：当你把 CLI/服务打包成单文件或扁平化模块（bun/esbuild/rollup），常见陷阱是：
- `new URL('./schema.sql', import.meta.url)` 在 dist 环境下指向不存在的文件；
- 测试只跑源码，发布后才发现 dist 读不到资源。

建议固化：
- 把资源当成“发布物的一部分”：要么在构建里复制到 dist 并保证相对路径可用，要么提供内嵌 fallback（字符串/内置模板），并允许用 env 覆盖资源路径。
- 增加一个最小“dist 验证”门禁（可用脚本或集成测）：在 dist 环境触发一次会读资源的路径，确保发布形态真实可用。

## C 类情境因子（按需启用）

### C1) monorepo 发布与版本联动

触发条件：workspace 多包发布或内部依赖。

建议：
- 明确哪些包发布、哪些只内部使用。
- 用 `exports` 控制 public surface，避免内部文件路径被依赖方绑定。

### C2) 二进制入口与 shebang

触发条件：你需要像 `mycli` 一样直接执行。

建议：
- dist 的入口文件带 shebang（`#!/usr/bin/env node`），并确保在构建/发布时权限可执行。
- 避免把逻辑写在 shebang 文件里：入口只负责 import/require dist 主模块。

### C3) 平台差异（Windows/WSL）

触发条件：需要跨平台支持。

建议：
- 路径统一用 `os.homedir()` + `path.join/normalize`；不要手写 `~/...`。
- 对 shell 命令/信号（SIGKILL 等）给出替代策略或明确限制。

## 常见坑（建议加入“禁止模式”）

- `--help` 触发副作用（import 时代码就启动 server/连接 DB）。
- 发布只验证源码可跑，不验证 dist（上线才发现入口断了）。
- 没有 sourcemap，导致线上堆栈不可读。
