![](https://github.com/yoyooyooo/ai-coding-os/raw/main/assets/banner.png)

[English](README.md) | **中文**

# AI Coding OS

AI Coding OS 是一套可移植的项目级知识、规范、Authority、架构、产品定义和有界证明 Skill Suite。它帮助 Agent 找到问题的语义 owner，并维护长期项目事实，但不规定统一阅读、规划、ticket 或执行 workflow。

ownership 不明确或跨多个 decision surface 时，使用 user-invoked `$ai-coding-os`；边界明确时直接调用专业 Skill。

## 最小知识内核

```text
Project Authority First
Question-scoped Ownership
One Scoped Meaning, One Current Home
Binding Constraint Is Not Semantic Ownership
Evidence Bounds Claims
Route Is an Edge; Change Creates an Impact Obligation
```

可移植 canonical 版本由 `$ai-coding-os-suite-contracts` 携带，以支持独立或扁平安装；本 README 是公开说明投影。

本 Suite 默认 Agent 能自行选择策略，从适用的项目 Authority 和局部模式推导普通可逆细节，隔离真正不可决定的局部 claim，并继续不受影响的工作；它不编码 Agent 的推理过程或实施顺序。

`Pass` 和 decision table 表达 coverage，不表达推理顺序。只有真正拥有状态机、事务、迁移、安全协议或外部协议的 owner 才能规定顺序。Tracker、ticket Skill、实验方法和 release process 在核心 Suite 外拥有自己的 workflow 状态。

## 核心 Skill Suite

| Group | Skill | Decision surface |
| --- | --- | --- |
| `router/` | `$ai-coding-os` | user-invoked 知识 Owner Map |
| `contracts/` | `$ai-coding-os-suite-contracts` | 可移植最小知识内核、Proof Surface、Evidence Envelope、eval 与 Harness schema |
| `governance/` | `$docs-governance` | 文档 Authority、Routes、Earned Shape、生命周期、清理和审计 |
| `product/` | `$product-definition` | 产品 framing、source synthesis、业务模型、决策、需求与验收 |
| `architecture/` | `$evolvable-application-architecture` | 事实权威、事务、模块、端口、组合和迁移 |
| `architecture/` | `$frontend-architecture` | 前端状态、feature topology、projection、Query/store/realtime |
| `architecture/` | `$effect-best-practices` | Effect Service/Layer/Scope/runtime、错误、资源和版本映射 |
| `capability/` | `$interface-capability-planning` | 用户工作、IA、surface、交互状态、前端归属和 proof needs |
| `harness/` | `$product-harness-system` | Harness 共享词汇、coverage、trace、claim ceiling 和 lifecycle |
| `harness/` | `$headless-product-harness` | Headless command、fixture/replay、DB/restart 和 boundary proof |
| `harness/` | `$ui-product-harness` | interface-headless、render focus 和 browser-visible proof |
| `harness/` | `$frontend-test-system` | 具体 frontend test lane 和 runner 选择 |
| `preset/` | `$evolvable-application-preset` | 发现并选择性采用项目默认值 |
| `tooling/` | `$effect-api-app-kit` | 从已确定 Effect API Change Spec 原子生成代码 |

每个核心 Skill 都能独立安装。相对链接只指向本 Skill；跨 Skill 关系使用 `$skill-name`，不依赖 grouped source 路径。

## 项目知识网络

项目文档是多入口网络。Agent 可以从问题、源码区域、术语、ADR、schema、测试、Harness Result、source file、仓库入口或 docs index 进入，只沿当前 claim 相关的边探索。

```text
Product / Requirements       系统应该做什么
SSoT                         共享术语、对象、状态和不变量是什么意思
Standards                    当前适用哪些规则和质量门
ADR / Product decisions      为什么接受某个选择
Architecture                 当前拓扑、ownership 和 accepted seam
Protocols / API              接口接受什么
Source / schema / migrations 当前存在什么实现结构和静态属性
Tests / runtime / release    哪些行为在有界路径上被实际观察
Harness / Evidence           哪个有界 claim 被真实观察
Selected execution method    工作拆解、依赖、状态和完成
```

`AGENTS.md` 暴露稳定项目约束和可用知识表面；`docs/README.md` 可以按问题、Authority、code area 或 artifact 建索引。它们都不是必经根节点，也不复制当前事实。

Portable Skill 的输出路径只是候选默认值。项目已有 Home 优先；外部 Skill 不能为已有语义创建第二份 glossary、ADR、Standard 或 execution ledger。

## Proof 与 Evidence

共享 Proof Surface 正交区分：

```text
surface_kind       实际观察表面
dependency_reality none / fixture / fake / replay / real_local / real_external
environment_class  isolated / local process / local stack / staging / production
proof_focus        render_wiring、persistence_restart 等 owner-local property
```

`none` 只用于纯静态证明，不能与其他 dependency reality 同时出现。

Evidence Envelope 只有在真实机器消费者、durable citation 或重复跨 owner handoff 需要共享 shape 时才使用。v2 无方向：保留 source、claim ceiling、observations、supported interpretation、not_proven、Evidence refs 和可选 Proof Surface，不传递 workflow 或文档生命周期。

```text
Harness pass != execution completion
execution status != product 或 document acceptance
accepted target != verified implementation
observed behavior != accepted future intent
```

源码可以证明当前实现结构和静态属性；runtime、reachability、deployment 和 environment claim 需要实际执行或观察 Evidence。源码和 Evidence 都不单独决定 accepted product intent。

## 使用

ownership 不明确或跨域：

```text
使用 $ai-coding-os 找出当前 concern 所需的最小知识 owner 集合；不要选择 workflow 或创建 durable state。
```

文档治理：

```text
使用 $docs-governance 收敛 Authority、多入口 Routes、Earned Shape、生命周期、source alignment 和 audit findings。
```

产品定义：

```text
使用 $product-definition 综合来源、建立产品模型、挑战冲突、记录 accepted decision，并产出适量 acceptance。
```

应用架构：

```text
使用 $evolvable-application-architecture 检查事实 writer、事务、模块边界、capability、composition、迁移与 claim ceiling。
```

界面与证明：

```text
使用 $interface-capability-planning 处理用户工作、surface、state、frontend ownership 与 proof needs；再由对应 Harness/Test owner 选择最小诚实观察面。
```

Preset 与生成：

```text
使用 $evolvable-application-preset 发现并选择性采用兼容默认值；renderer 输出在项目 owner 合入 Current Home 前始终是 candidate。只有架构和 Effect 版本决策稳定后，才使用 $effect-api-app-kit。
```

## 核心分发

核心 canonical source 位于 [`skills/**`](skills/README.md)。生成 deterministic core-only grouped-source ZIP、audit JSON 和 sidecar manifest：

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run bundle:skills
```

Bundle 包含核心 Skill Suite，不包含共仓实验、CLI packages、项目 docs 和仓库 release scripts。它是自包含交付单元：`skills/VERSION` 提供 Core 版本，`skills/requirements-audit.txt` 固定 audit 依赖，解压后可以运行 bundle-local audit/builder，`source_tree_sha256` 将通过的 audit 绑定到实际打包的 `skills/**`。Builder 同目录输出 canonical audit、manifest、change report 和 composition review；canonical provenance 排除机器绝对路径与 compiler-dependent template-typecheck 状态，因此相同源码可跨路径复现。Sidecar 中的每 Skill SHA-256 用于标识未独立版本化的源码。

## 共仓实验：Goal Proof

Goal Proof 是关于 Goal Pack state、proof step、append-only evidence 和 completion review 的早期 user-invoked 实验，目前尚不能确认长期有效。它不是核心 Skill、Router branch、知识网络默认项或核心 Bundle 成员。

- 实验边界与 Skill：[`experiments/goal-proof/`](experiments/goal-proof/README.md)
- 实验 CLI：[`packages/cli/`](packages/cli/README.zh-CN.md)
- 历史 dogfood：[`experiments/goal-proof/dogfood/`](experiments/goal-proof/dogfood/README.md)

实验评估期间，npm package 仍叫 `goal-proof`：

```bash
npm install -g goal-proof@^0.2.0
goal-proof --help
```

## 仓库结构

```text
skills/                              AI Coding OS 核心 grouped Skill source
  router/ contracts/ governance/ product/
  architecture/ capability/ harness/ preset/ tooling/
experiments/goal-proof/              独立早期 workflow experiment
packages/cli/                         Goal Proof 实验 CLI
scripts/                              仓库 release support
docs/                                 当前项目知识与规范网络
assets/                               README media
```

## 仓库验证

```bash
bun run check:core
bun run check:goal-proof-experiment
bun run check
```

- `check:core`：核心 Suite audit 与 Docs Governance audit。
- `check:goal-proof-experiment`：实验 Skill self-check、CLI build、typecheck 和 tests。
- `check`：整仓聚合门；通过不代表 Goal Proof 属于核心 Suite。

## 发布

`bun run bundle:skills` 只创建带版本的核心 Skill bundle，不发布。核心 Suite 版本与 CLI package 版本独立。

Tag-oriented 本地 release helper 只为实验 `goal-proof` CLI 版本化并创建 tag。实际 npm 发布是单独配置的 release step，本仓不声称已配置：

```bash
bun run release:check patch
bun run release patch
```

npm tarball 包含 `dist/`、package README、`LICENSE` 和 package metadata，不分发核心 Skill Suite。

## 许可证

MIT
