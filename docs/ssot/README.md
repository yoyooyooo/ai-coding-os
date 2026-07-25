# SSoT

本层保存 AI Coding OS 当前事实、术语和不变量。

## Owns

- 核心 Suite identity、owner boundary 和发布边界。
- 当前方法对象的权威含义。
- 不应被 Roadmap、实验、README 或 execution artifact 静默改写的事实。

## Must Not Own

- 迁移顺序、任务状态、历史讨论、未采纳提案或外部 workflow state。

## Boundary

SSoT 是共享语义在其 scope 内的 canonical Current Home，不是所有 claim 的全局最高 Authority。ADR 解释采用原因；Standards 规定执行规则；Architecture 展示结构；Roadmap 记录未来 delta；源码证明实现结构，执行或观察 Evidence 证明有界行为。它们不能静默重定义本层事实。

## Current Facts

- AI Coding OS 核心是项目级多入口知识、规范、Authority、架构、产品和 proof semantics Skill Suite；当前 Core source version 由 `skills/VERSION` 声明为 `0.4.2`。
- 核心不规定统一阅读、规划、ticket 或执行 workflow。
- `Route is an edge, not a sequence`；owner-local Pass 默认是 coverage，不是推理顺序。
- `$ai-coding-os` 是 user-invoked Owner Map，只选择知识 owner，不拥有 durable artifact、模型编排或 execution state。
- 核心 source 位于 `skills/**`，按 Router、Contracts、Governance、Product、Architecture、Capability、Harness、Preset、Tooling 分组。
- `$ai-coding-os-suite-contracts` 独立携带最小知识内核、可选 handoff guidance、Proof Surface、方向中立的可选 Evidence Envelope、eval、owner-declared source vocabulary 和 Harness schemas；不保存静态安装 roster。
- `$docs-governance` 拥有 documentation Authority、Routes、Earned Shape、生命周期、清理和 audit。
- `$product-definition` 拥有 product framing、source synthesis、业务模型、产品决策、requirements、acceptance 和 UAT。
- `$evolvable-application-architecture`、`$frontend-architecture`、`$effect-best-practices` 分别拥有应用、前端和 Effect 决策面。
- `$interface-capability-planning` 拥有用户工作到 IA、surface、interaction state、frontend ownership 和 proof needs 的映射；InterfaceCapability status 只表达 definition lifecycle，Harness Evidence 不自动改变其 acceptance。
- Harness/Test Skills 分别拥有共享 Harness architecture、headless proof、UI proof 和具体 frontend test lane。
- `$evolvable-application-preset` 是可复用默认来源；renderer 只输出 `candidate-snapshot`，不得自称 accepted/current。Profile provenance 分别记录 `requested`、`defaults_added`、`dependency_added` 和 `resolved`；语言中立 profile 不引入 TypeScript filename patterns。只有对应 semantic owner 合入 Current Home 的内容才成为项目 Authority；legacy `resolved-snapshot` 仅保留 reader compatibility。
- `$effect-api-app-kit` 只实例化已确定的 Change Spec，并拥有其原子写入协议。P3 Descriptor 的 Harness entry、command、observables、exclusions 和 claim ceiling 必须来自项目输入；Kit 只验证绑定与有界命令结果，不推断 declared coverage 已被证明。
- 对当前问题和 scope 仍有效的 Project Product、SSoT、Standards、ADR、contracts 与 Evidence 优先于未采用 Preset、Router 和通用 Skill 默认值；`AGENTS.md` 约束 Agent 行动，但不自动拥有产品、协议或运行事实。
- Evidence 结论不得超过实际 observation surface；纯静态 Proof Surface 使用 `dependency_reality: [none]` 且不得与 runtime dependency 混写；`observed`、`supports`、`not_proven`、execution completion、document lifecycle 和 product acceptance 保持非等价。
- Tracker、ticket Skill、实验方法和 release process 在核心外拥有 execution decomposition、dependency、status 和 completion。
- Goal Proof 位于 `experiments/goal-proof/**`，是 user-invoked 共仓早期实验；不属于核心 Router、Skill roster 或 Suite bundle。
- `packages/cli/**` 是 Goal Proof 实验 CLI；npm package 继续使用 `goal-proof`，不代表核心 Suite 名称。
- 核心 Suite ZIP 只包含 `skills/**`；`skills/VERSION` 是 bundle-local Core 版本来源，解压后 audit/builder 可独立运行。Canonical audit 的 `source_tree_sha256` 必须与实际打包源码一致；audit、manifest 和 review reports 是同目录版本化 sidecar。Release provenance 排除机器绝对路径和 compiler-dependent template-typecheck 状态，因此同一源码在不同路径上产生 byte-identical canonical artifacts；experiments、CLI、project docs 和 repository release scripts 不进入 ZIP。
- 本仓只维护 grouped core source，不生成 Flat source；每个 Skill 必须兼容独立、重排或扁平安装。

## Authority By Question

| Question | Current owner |
| --- | --- |
| 产品或系统应该做什么 | accepted product/business decision 或 baselined requirement |
| 当前存在什么实现结构和静态属性 | source、schema、migration、lockfile、generated artifact |
| 哪些行为被实际观察 | executed tests、Harness、runtime、release 或 operational Evidence |
| 共享术语、对象、状态或不变量是什么意思 | SSoT 与 accepted decision |
| 为什么接受某个选择 | Product Decision Record 或技术 ADR |
| 接口接受什么 | adopted protocol/schema 与 contract evidence |
| 当前结构和 owner 是什么 | source facts 与 Architecture view |
| 当前 work 状态和完成 | repository-selected execution owner 与 release evidence |

冲突必须显式分类为 scoped coexistence、supersession、stale documentation、implementation drift、unaccepted implementation、Evidence gap、obsolete source 或 missing Authority；这些是自然语言处分，不是全局状态机。不存在覆盖所有问题的统一文件顺序。

被接受的决定改变其他 Current Home 时，必须更新受影响 Home、记录暂时 drift、降低相关 claim，或说明影响不适用；核心不规定处理顺序。

## Promotion / Demotion

- 从 accepted decision、验证证据或完成迁移中抽取稳定事实时 promote 到本层。
- 迁移计划、历史解释、execution state 和 evidence summary 分别留在 Roadmap、ADR、selected method 或 report。
- 废弃事实从当前口径移除；需要的追溯由 Git history、superseded ADR 或历史 source 保留。

## Routes

- 文档网络：`../README.md`
- 执行规则：`../standards/README.md`
- 文档治理：`../standards/docs-governance.md`
- 结构视图：`../architecture/README.md`
- 核心 Skill source：`../../skills/README.md`
- Goal Proof experiment：`../../experiments/goal-proof/README.md`
