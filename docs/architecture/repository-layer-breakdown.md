# AI Coding OS 整仓分层拆解

## 状态

```yaml
status: current-architecture-view
scope: repository layout and cross-layer ownership
not_authority_over:
  - docs/ssot/**
  - docs/standards/**
  - docs/adr/**
  - packages/cli/src/**
  - Goal Pack evidence records
```

本文是仓库结构视图，用来帮助 agent 判断文件归属、改动传播面和提交边界。它不替代 SSoT、standards、ADR、CLI 代码或 Goal Pack evidence。

## 总体分层

```text
public shell
  -> method source
  -> execution engine
  -> authority docs
  -> long-running artifacts
  -> verification / release support
```

核心状态流保持一条：

```text
human intent -> goal contract -> proof_step -> evidence -> next_action
```

仓库分层不是新 workflow。它只是说明这条状态流在源码仓里的物理落点。

## 1. Public Shell

拥有对外第一印象、安装入口和维护者入口。

```text
README.md
README.zh-CN.md
AGENTS.md
assets/**
package.json
bun.lock
```

职责：

- 说明 AI Coding OS 是面向高智能 agent 的方法论和 skill suite。
- 说明公共主线是 intent-to-evidence state transition。
- 保留 `goal-proof` 作为当前 CLI / npm 包名。
- 给用户安装和启动入口。
- 给维护 agent 本仓语言、命令、同步更新和验证规则。

不拥有：

- schema 事实。
- Goal Pack 当前状态。
- skill phase 的细节规则。
- CLI 行为定义。

改动传播：

- README 公共叙事改变时，检查 `docs/product/**`、`docs/ssot/**`、`skills/**` 是否仍一致。
- AGENTS 维护规则改变时，检查相关 skill、docs audit 和验证命令。

## 2. Method Source

拥有 agent skill 的源码视图。运行时触发名由每个 `SKILL.md` frontmatter `name` 决定，目录只服务维护者阅读。

```text
skills/router/**
skills/goal/**
skills/governance/**
skills/architecture/**
skills/capability/**
skills/harness/**
skills/README.md
```

分组：

| Layer | Owns | Must Not Own |
| --- | --- | --- |
| `skills/router/**` | 默认入口、意图路由、inline-vs-durable 判断 | 持久 artifact、Goal Pack state、docs lifecycle |
| `skills/goal/**` | Goal Pack 生命周期、goal contract、proof_step、evidence、completion review | docs layer placement、UI/harness 具体证明细节 |
| `skills/governance/**` | docs layer、authority placement、cleanup、audit | product truth、Goal Pack evidence |
| `skills/architecture/**` | 可复用工程架构 doctrine 和审计 | 单个产品事实、任务状态 |
| `skills/capability/**` | UI/IA、surface、state/data ownership、trace planning | harness 生命周期和具体测试命令 |
| `skills/harness/**` | harness artifact、claim ceiling、UI/headless proof 方法 | 业务语义和 Goal Pack lifecycle |

当前滚动实施规则：

- `goal-contracts` 校准 `objective` 的 minimum sufficient horizon。
- `finding-proof-step` 只选择当前 falsifiable movement。
- `proof-step-implementation` 把 fresh evidence 归约回现有 progress state。
- `ai-coding-os` 只识别并路由，不保存状态。

改动传播：

- 改 skill frontmatter `name` 或公开触发名，必须检查 `docs/standards/skill-source-layout.md`、README、安装示例和测试。
- 改 Goal Proof 语义，必须检查 `skills/goal/**`、`packages/cli/**`、templates、checker rules、README 和 dogfood Goal Pack。
- 改架构 / capability / harness skill 的公共边界，必须检查 `skills/README.md` 和对应 docs layer。

## 3. Execution Engine

拥有可运行 CLI、Goal Pack 读写、checker、renderer 和测试。

```text
packages/cli/src/**
packages/cli/test/**
packages/cli/README.md
packages/cli/README.zh-CN.md
packages/cli/package.json
```

职责：

- 发布当前 CLI：`goal-proof`。
- 读写 v2 Goal Pack artifacts。
- 提供 `check`、`inspect`、`summary`、`work`、`evidence`、`relations` 等命令。
- 用 tests 固化 CLI 行为和 schema 检查。

不拥有：

- AI Coding OS 顶层品牌重命名。
- docs layer authority。
- skill trigger 分发状态。

改动传播：

- 新增或修改 CLI command / flag / output，需要更新 CLI README、根 README 命令示例、skill references、tests。
- 修改 schema / checker / evidence record 规则，需要同步 templates、checker rules、Goal Pack examples 和相关 dogfood artifacts。

## 4. Authority Docs

拥有当前事实、执行规则、取舍、结构视图和迁移顺序。

```text
docs/product/**
docs/ssot/**
docs/standards/**
docs/adr/**
docs/architecture/**
docs/roadmap/**
docs/review-plan/**
docs/interface-capabilities/**
docs/product-harness/**
docs/README.md
```

分层：

| Layer | Owns | Example |
| --- | --- | --- |
| `docs/product/**` | 产品 / 方法论定位 | 高智能 agent、workspace 边界、用户价值 |
| `docs/ssot/**` | 当前事实、术语、不变量 | skill 分组事实、Goal Pack artifact ownership |
| `docs/standards/**` | 可执行规则、命令、SOP | skill source layout、docs governance |
| `docs/adr/**` | 已采纳取舍 | 命名与边界决策 |
| `docs/architecture/**` | 结构视图和数据流 | 本文件、仓库模块关系 |
| `docs/roadmap/**` | 迁移顺序、状态、证据链接 | 后续波次和 gate |
| `docs/review-plan/**` | plan/proposal review ledger；不拥有 completion evidence | `$plan-optimality-loop` 评审记录 |
| `docs/interface-capabilities/**` | 项目级 interface trace | UI/IA 追溯 |
| `docs/product-harness/**` | 项目级 harness contract | coverage matrix、claim ceiling |

改动传播：

- 当前事实变化：优先更新 `docs/ssot/**`，再更新 README / skill / roadmap。
- 可执行规则变化：更新 `docs/standards/**`，再更新 skill 或脚本。
- 结构视图变化：更新 `docs/architecture/**` 和最近 README 索引。
- 迁移顺序变化：更新 `docs/roadmap/**`，不要把 roadmap 写成 Goal Pack progress ledger。

## 5. Long-Running Artifacts

拥有 Goal Proof System 的长期执行材料、来源和 evidence。

```text
docs/goal-proof/inbox/**
docs/goal-proof/sources/**
docs/goal-proof/goals/**
```

职责：

- `inbox/**`：弱信号、待 triage 候选。
- `sources/**`：已消费的 proposal、handoff、source materials。
- `goals/<goal-id>/goal.yaml`：goal contract。
- `goals/<goal-id>/progress.yaml`：rolling state。
- `goals/<goal-id>/evidence.jsonl`：append-only transition evidence。
- `goals/<goal-id>/plans/<work_id>.md`：仅高风险 `needs_plan` slice。

不拥有：

- 顶层产品事实。
- docs layer governance。
- CLI schema authority。

改动传播：

- Goal Pack completion review 可以 promote 稳定事实到 SSoT / standards / ADR。
- Source material 被采纳后，应保留为 source，不应继续作为当前 authority。
- Roadmap 可以链接 Goal Pack evidence，但不能复制 Goal Pack 运行状态。

## 6. Verification / Release Support

拥有仓库验证、发布和脚本测试。

```text
scripts/**
tsconfig.json
package.json
bun.lock
```

职责：

- `bun run build`、`bun run typecheck`、`bun run test`、`bun run check`。
- release precheck / no-push dry run 行为。
- npm package 内容和发布前检查。

改动传播：

- 修改 release 或 package 行为，更新 scripts tests、README install/release 相关说明。
- 修改验证命令，更新 AGENTS、docs standards 和 CI / local command docs。

## 跨层提交边界

推荐提交按 claim 切分，而不是按目录机械切分。

| Claim | 典型提交范围 |
| --- | --- |
| 公共叙事收口 | README、docs/product、docs/ssot、相关 skill |
| Goal Proof schema / CLI 行为 | `packages/cli/**`、templates、checker refs、tests、README |
| Skill source layout | `skills/**`、`docs/standards/skill-source-layout.md`、README |
| Docs layer / architecture view | `docs/**` indexes、architecture / standards docs |
| Harness / interface capability 方法 | 对应 skill、docs/interface-capabilities 或 docs/product-harness、README |

提交前至少检查：

```text
docs audit
bun run check
```

若只改 docs-only 且不影响 CLI / package / tests，可只跑 docs audit；但当 README / skill / templates 涉及 CLI 文案或 tests 断言时，跑完整 `bun run check`。
