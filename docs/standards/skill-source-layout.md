# Skill Source Layout

本标准规定 AI Coding OS 核心 Skill Suite 的 grouped source、invocation、可移植合同、写作质量和验证口径。Grouped layout 只服务源码维护，运行时不依赖目录层级。

## Owns

- 核心 `skills/**` source groups。
- `SKILL.md` frontmatter 与 invocation boundary。
- Skill-local progressive disclosure 和 flat-install portability。
- 核心 Suite、共仓 experiment 与下游 distribution 的分界。

## Must Not Own

- 单个 Skill 的领域方法论。
- Tracker、ticket、Goal、release 或其他 execution state。
- 下游安装、镜像、同步或 runtime 状态。

## Core Source Groups

| Group | Source role |
| --- | --- |
| `skills/router/**` | user-invoked knowledge Owner Map |
| `skills/contracts/**` | portable cross-Skill contracts and schemas |
| `skills/governance/**` | documentation Authority and knowledge-network governance |
| `skills/product/**` | product framing, decisions, requirements, acceptance |
| `skills/architecture/**` | application, frontend, and Effect doctrine |
| `skills/capability/**` | interface capability and state/ownership trace |
| `skills/harness/**` | shared, headless, UI, and frontend-test proof |
| `skills/preset/**` | reusable defaults and reviewable candidate snapshots |
| `skills/tooling/**` | deterministic generators, audit, core bundle |
| `skills/examples/**` | routes to owner-local examples |

`experiments/**` 不属于核心 source group。Goal Proof experiment 位于 `experiments/goal-proof/**`，有独立 invocation、自检、CLI 和历史 dogfood，不进入核心 Router、Suite audit roster 或 core ZIP。

## Canonical Core Trigger Names

```text
ai-coding-os
ai-coding-os-suite-contracts
docs-governance
product-definition
evolvable-application-architecture
frontend-architecture
effect-best-practices
interface-capability-planning
product-harness-system
ui-product-harness
headless-product-harness
frontend-test-system
evolvable-application-preset
effect-api-app-kit
```

跨 Skill handoff 使用 `$skill-name`。目录名只服务源码组织；共享 vocabulary/pattern 的 `owner` 使用不带 `$` 的 core Skill ID。

## Invocation

- `$ai-coding-os` 是核心 user-invoked Router，使用 `disable-model-invocation: true`。
- 专业 Skill 只有在 Agent 必须自主发现或被相邻 Skill reach 时才保留 model invocation。
- Goal Proof experiment 独立使用 user invocation，不占核心 description context load。
- Frontmatter 只允许 `name`、`description` 和必要的 `disable-model-invocation`。
- Model-invoked description 只承担做什么、独立 trigger branch 和必要 reach clause；user-invoked description 是给人看的单行索引。

## Information Hierarchy

- `SKILL.md` 内联所有 branches 共用的 steps、strong invariants 和 completion criteria。
- Branch-only reference 通过条件明确的 Skill-local context pointer 披露。
- 一个 concept 的定义、规则和 caveats co-locate；一个 meaning 只有一个 source。
- Skill split 需要独立 invocation surface，或真实 sequence boundary 与 observed premature-completion risk。
- Pass/Steps 默认表示 owner-local coverage 和 semantic dependencies，不规定项目 workflow 或 Agent reasoning order。
- 真实状态机、事务、安全顺序、迁移和外部协议可以规定 sequence，并必须有可检查 completion criterion。
- 删除 duplication、sediment、sprawl 和 no-op；Leading word 只有在改变 invocation/execution predictability 时保留。

## Eval Standard

- 每个 core Skill 至少有一个 `evals/*.json`。
- Prompt 使用真实用户表达，优先覆盖 trigger 近邻和 owner 冲突。
- `expected_output` 描述成功行为；每个 core case 的至少两个 `expectations` 分别覆盖正向产物/观察与 ownership/claim boundary。
- 只写“不要做什么”的 eval 不足以区分 Skill；同时说明正确 owner 或替代动作。
- 结构审计不等于 model-run benchmark；未运行的 stochastic eval 必须保持 `not_claimed`。
- Machine contract 变更优先增加能证明非法实例被拒绝的 targeted negative case，不以关键词型静态 eval 数量代替 closure。
- Model-run 评估必须记录实际加载的 Skill SHA，防止旧 runtime mirror 污染；重点观察 unnecessary escalation、wrong owner selection、overclaim、duplicate Authority、unnecessary artifact、forced sequence、irrelevant Skill loading 和 failure to continue unaffected work。
- Model-run 结果是版本化 sidecar，不新增 Core eval-result Schema；静态 case 继续服务 trigger、ownership 和 compatibility 回归。

## Portability

- 本仓只维护 grouped core source，不生成或发布 Flat 副本。
- 每个 Skill 能独立、重排或扁平安装。
- 相对链接不得逃逸 Skill root；跨 Skill 关系用 `$skill-name`。
- 可执行 Skill 不在运行时读取 sibling Skill path。必须自包含的数据使用 Skill-local snapshot，并由 audit 校验 parity。
- `$ai-coding-os-suite-contracts` 不保存静态安装 roster、分组 taxonomy 或 Router 副本。
- Core ZIP 内 `skills/README.md` 的链接必须 bundle-local；`skills/VERSION`、audit 和 builder 不得依赖被 archive scope 排除的根文件。

## Association Policy

Skill 默认独立，只声明稳定 ownership boundary。Router 选择默认 Lead；用户请求和项目 Authority 决定更强组合。外部 execution Skill 可以消费核心知识，但不进入核心 roster 或把其 workflow schema 注入 Suite Contracts。

## Change Coverage

改 Skill name、group、invocation、Schema、shared vocabulary 或 Router boundary 时，同一变更集覆盖：

```text
core source and frontmatter
owner fields and bounded handoffs
public README / AGENTS / SSoT / Standards / ADR
references, templates, evals, checker, golden, tests
core / experiment / downstream claim boundaries
mechanical validation and active-surface scan
```

历史 evidence/source 保留当时路径和词汇，但不定义当前 trigger 或 roster。

## Claim Levels

| Claim | Required evidence |
| --- | --- |
| `source-updated` | core source、public docs、必要 templates/evals/checkers 同步 |
| `core-repo-verified` | core Suite audit 与 Docs audit 通过 |
| `experiment-verified` | experiment self-check 和 owner-local executable tests 通过 |
| `flatten-install-portable` | Skill-local links、no sibling runtime dependency、isolated render/check 通过 |
| `core-bundle-self-contained` | 干净解压后 Suite audit 与 builder 可运行，README 不含 archive 外相对链接 |
| `release-source-bound` | canonical audit 与 manifest 的 `source_tree_sha256` 等于待打包 `skills/**` |
| `release-sidecars-self-contained` | manifest 引用的 versioned audit、change report 与 composition review 均存在于 release output，hash 可复算 |
| `release-cross-machine-deterministic` | 不同绝对 source path 与 compiler availability 下，canonical ZIP/audit/manifest/reports byte-identical |
| `downstream-distribution-not-claimed` | 未声称任意 runtime 已安装或同步 |

## Required Verification

```bash
bun run check:core
bun run check:goal-proof-experiment
bun run check
bun run bundle:skills
```

核心 active scan 应无 Goal experiment trigger、旧 phase Skill、`skills/goal/**` 或 workflow-specific Evidence adapter。实验历史中的旧路径是允许的 provenance，不需要重写。
