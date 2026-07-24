![](https://github.com/yoyooyooo/ai-coding-os/raw/main/assets/banner.png)

[English](README.md) | **中文**

# AI Coding OS

AI Coding OS 是一套按 decision surface 分组的 AI coding 方法与 Skill Suite。
它为 repository/workspace 工作提供薄用户路由、项目文档权威、可演进架构、界面能力、
Product Harness、可选 Goal Pack 方法、可复用 Preset 和确定性生成工具。

默认落地边界是 workspace/repo。跨域或入口不明确的工作使用 user-invoked
`$ai-coding-os`；边界明确时直接使用拥有该决策面的专业 Skill。

## 核心原则

```text
project authority 优先
一个决策面一个主 owner
proof surface 与 claim 匹配
observed / supports / not_proven 分离
Preset 只生成 resolved snapshot
跨 Skill 依赖使用 `$skill-name`，不依赖安装目录
结构化 artifact 按长期价值创建
```

这不是形式化证明系统，也不规定唯一执行流程。架构和治理约束 durable semantics；
当前任务依据项目权威、风险和可用验证面决定实施策略。

## Skill Suite

| Group | Skill | 作用 |
| --- | --- | --- |
| `router/` | `$ai-coding-os` | user-invoked 薄路由；选择 Lead/Supporting Skill |
| `contracts/` | `$ai-coding-os-suite-contracts` | 可独立安装的跨 Skill 协作、共享词汇与 Harness schema |
| `goal/` | `$goal-proof` | 显式采用时的 Goal Pack、proof step、evidence 和 completion review |
| `goal/` | `$goal-contracts` | 创建或修复 `goal.yaml` |
| `goal/` | `$finding-proof-step` | 寻找可证伪的 `proof_step` |
| `goal/` | `$proof-step-implementation` | 执行、验证、追加 evidence、归约 progress |
| `goal/` | `$write-work-plans` | 为选中的高风险 work item 写 `plans/<work_id>.md` |
| `governance/` | `$docs-governance` | docs layer、AGENTS.md、authority placement、cleanup、audit |
| `architecture/` | `$evolvable-application-architecture` | authority、事务、端口、组合根、Monorepo/source topology、迁移与可替换性 |
| `architecture/` | `$frontend-architecture` | 前端状态权威、feature topology、host composition、realtime reconciliation |
| `architecture/` | `$effect-best-practices` | Effect Service/Layer/Scope/runtime、错误、资源与版本映射 |
| `capability/` | `$interface-capability-planning` | UI/IA、InterfaceCapability、surface、state/data ownership、proof handoff |
| `harness/` | `$product-harness-system` | 共享 Harness 词汇、descriptor/result、coverage、claim ceiling、lifecycle |
| `harness/` | `$headless-product-harness` | capability command、fixture/replay、DB/restart、boundary proof |
| `harness/` | `$ui-product-harness` | interface-headless、render wiring、browser-visible proof |
| `harness/` | `$frontend-test-system` | 具体前端 test lane 与 runner 选择 |
| `preset/` | `$evolvable-application-preset` | Agent 发现并选择性采用可复用默认值，产出项目拥有的 snapshot |
| `tooling/` | `$effect-api-app-kit` | 从已确定 Change Spec 原子生成 Effect API capability slice |

## Goal Proof 状态变化模型

`$goal-proof` 是显式选择的可选 durable execution method。采用后，目标通过
intent-to-evidence state transition 推进：

```text
human intent -> goal contract -> proof_step -> evidence -> next_action
```

正式方法名是 Goal Proof System。正式 CLI 是 `goal-proof`。

## 核心词汇

| 词 | 含义 |
| --- | --- |
| Goal Pack | 一个长期目标的持久 completion unit |
| Goal Contract | `goal.yaml`；目标授权、边界、完成标准和 claim limit |
| Proof Step | `progress.yaml.proof_step`；当前可证伪推进步 |
| Proof Path | 支撑或证伪 proof step 的可运行/可检查路径 |
| Work Item | `progress.yaml.work_items` 内的有界工作单元，通常 `W###` |
| Evidence Record | `evidence.jsonl` 内 append-only 证据记录，通常 `E###` |
| Completion Review | 最终把 evidence 回扣到 `completion.required_evidence` 的 review evidence |
| Claim Limit | 当前目标或 proof 能声明和不能声明的范围 |
| Gap | 未覆盖 claim、缺证据、待决策或需人类介入点 |
| Goal Thread | 多个 Goal Pack 共享的 `relations.thread_id` 标签 |
| Goal Relation | Goal Pack 之间的 typed metadata link |
| Derived Graph View | CLI 从 relations 派生出来的图视图，不是存储状态 |

## Goal Proof System

Goal Proof System 是 Suite 中可选的长期目标载体。

```text
human intent
  -> goal.yaml goal contract
  -> progress.yaml proof_step
  -> evidence.jsonl evidence
  -> apply progress
  -> next_action: proof_step | continue | needs_plan | blocked | review | done | needs_human
```

Goal Pack ready 的条件是：goal contract 稳定，且当前 `proof_step` 已被授权在
`claim_limit` 内产出或检查 `completion.required_evidence`。
不是因为列了 work item 就 ready。

Work item 和 checks 是执行细节，不是顶层目标循环的必经概念。
`plans/<work_id>.md` 只在高风险 work item 需要先审计划时出现。它不是第二套任务系统。

完成必须有 review evidence record，包含 `completion_satisfied: true`，并用
`claim_evidence` 把 completion claim 映射到 evidence。
跨方法 Evidence Envelope Discipline 由 SSoT / Goal Proof 拥有。这里的
`changed surfaces` 和 `not_proven` 是叙事 envelope 概念；除非同步升级
templates / checker，不是 v2 schema 正式字段。

## Goal Pack 文件

```text
docs/goal-proof/
  README.md
  inbox/
  sources/
  goals/<goal-id>/
    goal.yaml
    progress.yaml
    evidence.jsonl
    plans/<work_id>.md  # only when needs_plan
    interface-capabilities.yaml  # optional UI/interface trace companion
    product-harness.yaml  # optional harness proof companion
    notes/
```

`goal.yaml` 拥有 objective、authority refs、engineering guidance、completion、
claim limit、stop rules 和 agent authority。`progress.yaml` 拥有运行态、
active work item、proof step、blockers、last check 和 next action。`evidence.jsonl`
是 append-only evidence。`notes/` 只存长上下文。

## Interface Capability 和 Harness

UI / Harness 体系让 agent 可以从底层和界面两端验证产品能力。

```text
Product Capability
  -> InterfaceCapability
  -> InterfaceSurface / Region
  -> Interaction State Contract
  -> Frontend State/Data Ownership
  -> Harness Scenario
  -> Headless Proof and/or UI Proof
  -> Evidence
  -> Claim / Gap
```

最终 UI 未定时，仍可用 harness route、harness component、interface-headless test
或 browser-visible candidate path 先证明局部链路。正式界面稳定后，可复用 proof path
再提升为 regression。

持久放置：

- 项目级界面 trace：`docs/interface-capabilities/**`
- 项目级 harness contract：`docs/product-harness/**`
- Goal-local interface companion：`docs/goal-proof/goals/<goal-id>/interface-capabilities.yaml`
- Goal-local harness companion：`docs/goal-proof/goals/<goal-id>/product-harness.yaml`

## 安装

安装 CLI：

```bash
npm install -g goal-proof
goal-proof --help
```

安装全套 AI Coding OS skills：

```bash
npx skills add https://github.com/yoyooyooo/ai-coding-os -g --agent '*' --skill '*' --full-depth -y
```

Codex-only：

```bash
npx skills add https://github.com/yoyooyooo/ai-coding-os -g --agent codex --skill '*' --full-depth -y
```

仓库和 skill suite 名是 AI Coding OS。CLI 和 npm package 仍是 `goal-proof`。
安装器可以重排或打平 Skill 目录：每个 Skill 的相对链接只指向自身文件，跨 Skill
依赖通过 `$skill-name` 发现。共享合同的独立入口是
`$ai-coding-os-suite-contracts`，不依赖本仓 grouped path。

## 使用

日常项目工作：

```text
使用 $ai-coding-os：
我要治理/规划/实施/审计……
背景：……
边界：……
验收：……
```

长期目标：

```text
使用 $goal-proof：
目标：……
背景：……
边界：……
验收：……
停止条件：……
```

UI capability 规划：

```text
使用 $interface-capability-planning：
拆 InterfaceCapability、surface、interaction state、frontend state/data ownership 和 harness needs。
```

UI proof：

```text
使用 $ui-product-harness：
规划 interface-headless、render wiring、browser-visible proof、evidence、gap 和 `claim_ceiling`。
```

Headless proof：

```text
使用 $headless-product-harness：
设计最小 proof command、fixture/replay、headless command output envelope，并记录 `not_proven` gaps。
```

Docs governance：

```text
使用 $docs-governance：
检查 docs layer、authority placement、README route、obsolete planning docs 和 audit。
```

本仓文档层规则见 `docs/standards/docs-governance.md`；公开 skill 源码布局和触发名规则见
`docs/standards/skill-source-layout.md`。

Architecture baseline：

```text
使用 $evolvable-application-architecture：
检查 authority、事务、Capability Port / Adapter、composition root、source topology、迁移与 claim ceiling。
```

Project Preset：

```text
使用 $evolvable-application-preset：
基于已确定的技术选型和现有项目权威，发现最小 profile closure，增量采用兼容的 AGENTS/docs/check surfaces；renderer 仅作为可选原语。
```

Effect API scaffold：

```text
使用 $effect-api-app-kit：
从已确认的 Change Spec plan/apply/verify 一个原子 capability slice。
```

## CLI 快速查看

```bash
goal-proof summary .
goal-proof list . --completion todo
goal-proof inspect <goal-pack> --json
goal-proof work list <goal-pack>
goal-proof evidence list <goal-pack> --limit 5
goal-proof relations goals . --thread <thread-id> --completion todo --json
goal-proof relations work . --thread <thread-id> --completion todo --json
goal-proof relations check . --thread <thread-id>
goal-proof relations graph . --thread <thread-id>
goal-proof work brief <goal-pack>
goal-proof check <goal-pack>
```

Relations commands 用于检查跨 Goal Pack 连续性和发现 thread 成员候选。它不创建队列、
worklist、scheduler、thread 生命周期、存储图或执行顺序。`relations.thread_id` 只是标签。

典型循环：

```text
check -> inspect -> work brief -> work -> evidence add -> apply -> check
```

完整 CLI 见 [packages/cli/README.zh-CN.md](packages/cli/README.zh-CN.md)。

## 文档和 Artifact Homes

| 路径 | 作用 |
| --- | --- |
| `docs/README.md` | 文档层路由和 authority 顺序 |
| `docs/product/**` | OS 产品/方法论定位 |
| `docs/ssot/**` | 当前事实、术语、不变量 |
| `docs/standards/**` | 可执行规则、命令、质量门、协作 SOP |
| `docs/adr/**` | 已采纳取舍 |
| `docs/roadmap/**` | 顺序、状态、证据链接、迁移波次 |
| `docs/interface-capabilities/**` | 项目级 InterfaceCapability / InterfaceSurface trace |
| `docs/product-harness/**` | 项目级 harness scenario、`claim_ceiling`、Harness Coverage Matrix、evidence refs |
| `docs/goal-proof/**` | Goal Pack、inbox、sources、evidence records、Goal Relations |
| `skills/**` | AI Coding OS 公开 skill suite 源码视图 |
| `packages/cli/**` | `goal-proof` CLI |

## 仓库结构

```text
packages/cli/                         TypeScript CLI，使用 Bun 构建
skills/router/                        OS 入口和用户意图路由
skills/goal/                          Goal Pack 方法和执行阶段
skills/governance/                    文档层治理
skills/architecture/                  application / frontend / Effect doctrine
skills/capability/                    Interface capability planning
skills/harness/                       shared、headless、UI 与 frontend test guidance
skills/preset/                        resolved project defaults
skills/tooling/                       executable profiles and source audit
skills/contracts/                     可独立安装的 AI Coding OS Suite contracts
skills/examples/                      owner-local examples index
skills/README.md                      grouped source 索引
docs/                                 文档治理与方法论分层入口
assets/                               README media
```

CLI 包发布名为 `goal-proof`。

## 发布

发布由 tag 驱动，通过 GitHub Actions 和 npm Trusted Publishing 完成：

```bash
bun run release:check patch
bun run release patch
# 或
bun run release 0.2.0
```

`bun run release:check` 只执行发布决策预检，不改文件。`bun run release`
创建临时本地 release 分支，更新版本文件，提交，给该提交打 `vX.Y.Z` tag，
只把 tag 推到配置好的公网 GitHub release remote，然后回到原分支。
GitHub Actions 从 tag 发布 npm 包。AGS remote 可以继续用于局域网同步，
但不是发布触发面。

## 开发

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run build
bun run typecheck
bun run test
bun run check
python3 skills/tooling/suite_audit.py --suite skills
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
```

CLI 源码是 TypeScript。`bun build` 将 npm 包产物输出到 `packages/cli/dist/`。

## 许可证

MIT
