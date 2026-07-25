# Agent 协作规则

本仓库维护 AI Coding OS 核心 Skill Suite，以及共仓但独立的 Goal Proof 早期实验与 CLI。

## 沟通与文档语言

- 始终用中文回复用户。
- `README.zh-CN.md`、`docs/**` 和实验叙述性正文优先使用中文。
- YAML 字段、CLI 命令、代码符号、协议名、schema 示例和可复制模板可保留英文。
- 不写情绪价值开场白；分歧按事实、Authority 和证据说明。

## 核心定位

AI Coding OS 是项目级多入口知识、规范、Authority、架构、产品与 proof semantics 网络。它不规定统一阅读、规划、ticket 或执行 workflow。

```text
Route is an edge, not a sequence.
Pass is coverage, not reasoning order.
Router selects knowledge; Agent selects strategy.
```

核心 user-invoked 入口是 `$ai-coding-os`。ownership 明确时直接使用专业 Skill：

- `$ai-coding-os-suite-contracts`：最小知识内核、可选 handoff guidance、Proof Surface、方向中立的可选 Evidence Envelope、eval、owner-declared source vocabulary 和 Harness schemas。
- `$docs-governance`：文档 Authority、Routes、Earned Shape、生命周期、清理和审计。
- `$product-definition`：产品 framing、source synthesis、业务模型、决策、需求、acceptance 和 UAT。
- `$evolvable-application-architecture`：fact authority、事务、Capability Port / Adapter、composition、source topology 和迁移。
- `$frontend-architecture`：前端 state、feature topology、Query/store/realtime 和 host composition。
- `$effect-best-practices`：Effect Service / Layer / Scope / runtime、错误、资源和版本映射。
- `$interface-capability-planning`：用户工作、IA、surface、交互状态、前端归属和 proof needs。
- `$product-harness-system`：Harness 共享词汇、coverage、trace、claim ceiling 和 lifecycle。
- `$headless-product-harness`：headless command、fixture/replay、DB/restart 和 boundary proof。
- `$ui-product-harness`：interface-headless、render focus 和 browser proof。
- `$frontend-test-system`：具体 frontend test lane 与 runner。
- `$evolvable-application-preset`：发现并选择性采用项目默认值；renderer 只生成 candidate，不自称项目 Authority。
- `$effect-api-app-kit`：从已确定 Change Spec 原子生成 Effect API slice。

Tracker、ticket Skill、实验 Goal 方法、release process 和其他 execution system 在核心 Router 外拥有自己的拆解、依赖、状态和完成生命周期。它们可以消费项目 Authority 和有界 Evidence，但不能成为 Product、SSoT、ADR、Architecture、Contract 或 documentation Authority。

## 共仓实验

Goal Proof 位于 `experiments/goal-proof/**`，是 user-invoked 早期实验，不属于核心 `skills/**`、Router branch 或核心 Suite ZIP。CLI 位于 `packages/cli/**`。

- 不因任务规模、持续时间或复杂度自动使用 Goal Proof。
- 同一 workstream 不保留 tracker/tickets 与 Goal Pack 两套 execution ledger。
- `experiments/goal-proof/dogfood/**/evidence.jsonl` 是历史证据，不重写；修正解释时追加记录或更新当前实验文档。
- Goal Proof 的状态机和 CLI reducer 是实验 owner-local 协议，不扩散为核心 OS workflow。

## Skill 迭代原则

按 `$writing-great-skills` 与 `$skill-creator` 的共同质量门维护 Skill：

- **Invocation**：只有 Agent 或其他 Skill 必须自主发现时才使用 model-invoked；user-invoked Skill 由人类承担索引成本。
- **Description**：只保留做什么、独立触发 branch 和必要 reach clause；每个词都承担 context load。
- **Information hierarchy**：所有 branch 共用的步骤、强不变量和 completion criterion 留在 `SKILL.md`；branch-only reference 通过条件明确的 context pointer 披露。
- **Predictability**：owner-local Pass 默认表达 coverage 和可检查完成标准，不规定推理顺序；只有真实状态机、事务、安全顺序、迁移或外部协议可以规定 sequence。
- **Pruning**：一个 meaning 一个 source；删除 duplication、sediment、sprawl 和 no-op，不为结构对称新增 Skill、reference、字段或 artifact。
- **Leading words**：复用已经能稳定触发行为的词，不为形式统一给所有 Skill 发明同一套口号。
- **Eval**：真实近邻 prompt 优先；`expected_output` 说明成功；每个 core case 用至少两个可区分 expectations 检查正向产物/观察与 ownership/claim boundary。
- **Portability**：相对链接只指向本 Skill；跨 Skill 关系使用 `$skill-name`；运行时不依赖 grouped source 路径。
- **Ownership**：一个 claim、representation 和 scope 有一个主 semantic owner；binding constraint、implementation Evidence 和 observed Evidence 保持独立。

默认从适用 Project Authority 和局部模式推导普通可逆细节，隔离真正不可决定的局部 claim，并继续无关工作。结构化 artifact 只有在改善后续执行、验证、审计、交接或 claim 诚实时才存在；字段必须有真实消费者并能约束 claim、暴露 gap、避免 overclaim 或改善可靠消费。

## 文档网络

- `docs/README.md` 是多入口索引，不承载领域真相，也不是必经阅读根。
- Agent 可以从问题、code area、term、artifact、source、test、Evidence 或任一 owner 进入，只沿相关 Route 探索。
- `docs/product/**`：产品/方法论定位和用户价值。
- `docs/ssot/**`：当前事实、术语和不变量。
- `docs/standards/**`：可执行规则、命令、质量门和协作标准。
- `docs/adr/**`：已采纳取舍及原因。
- `docs/architecture/**`：结构、模块关系和运行时视图。
- `docs/roadmap/**`：迁移顺序、gate 和 Evidence links；不复制 execution status。
- `docs/interface-capabilities/**`：项目级 InterfaceCapability trace。
- `docs/product-harness/**`：项目级 Harness contract、coverage 和 claim ceiling。

新增或迁移 durable 文档必须满足：语义 layer 正确、同一 claim/representation/scope 一个 canonical Current Home、相关 Routes 更新、Evidence 保留、生命周期明确。Portable Skill 的默认输出路径不能覆盖项目已有 Authority。

## 目录结构

- `skills/**`：核心 AI Coding OS grouped Skill source。
- `experiments/goal-proof/**`：Goal Proof 独立实验 Skill、dogfood 和 self-check。
- `packages/cli/src/**`、`packages/cli/test/**`：实验 CLI 源码与测试。
- `skills/tooling/suite_audit.py`：核心 Suite source audit。
- `skills/tooling/build_suite_release.py`：核心 Suite-only release bundle；canonical audit 与待打包源码必须具有同一 `source_tree_sha256`，并与 manifest/review sidecars 在不同绝对路径下保持确定性。
- `skills/governance/docs-governance/scripts/**`：Docs audit。
- `docs/**`：本项目当前知识和规范网络。

## 开发命令

使用 Bun；Python audit 依赖由 `requirements-dev.txt` 固定。

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run check:core
bun run check:goal-proof-experiment
bun run check
bun run bundle:skills
```

- `check:core`：核心 Suite audit 和 Docs audit。
- `check:goal-proof-experiment`：实验 Skill self-check、CLI build/typecheck/tests。
- `check`：整仓聚合门，不改变 Core/Experiment 边界。
- `bundle:skills`：生成不含 experiment、CLI、项目 docs 或 release scripts 的核心 Suite ZIP、audit JSON 和 manifest。

## 代码规范

- TypeScript 使用 ES modules、2 空格缩进、分号、双引号和显式 `node:*` imports。
- 源码文件用 kebab-case；函数和变量用 camelCase。
- CLI 行为保持确定性；优先结构化解析，避免 ad hoc 字符串处理。
- 改公开 CLI、Goal schema 或实验 Skill 时，同步更新 experiment docs、templates、checker 和 tests，不把它写回核心 Router/roster。
- 改核心 contract、Skill boundary、Preset output 或 docs route 时，同步更新 source、references、evals、golden、audit 和公共 docs。

## Pull Request

提交保持 claim scope 清楚。PR 应包含变更摘要、用户可见 contract/command 变化、Core/Experiment 边界、文档与 template 同步情况，以及实际验证命令。
