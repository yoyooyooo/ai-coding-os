# Skill Source Layout

本标准规定 AI Coding OS 公开 Skill Suite 的 grouped source、触发名、可移植共享合同和本仓验证口径。grouped layout 只服务源码维护；运行时不得依赖该目录层级。

## Owns

- `skills/**` grouped source layout。
- `SKILL.md` frontmatter `name`、`description` 和必要的 `disable-model-invocation`。
- `$ai-coding-os-suite-contracts`、Preset/tooling source placement 与扁平安装兼容约束。
- 本仓 source-updated 与 repo-verified claim。

## Must Not Own

- 单个 Skill 的方法论内容。
- Goal Pack 当前执行状态。
- 下游安装、镜像、同步或 runtime 状态。
- npm/GitHub release 策略。

## Source Groups

| Group | Source role |
| --- | --- |
| `skills/router/**` | user-invoked Suite entry |
| `skills/goal/**` | optional Goal Pack method and phases |
| `skills/governance/**` | docs governance |
| `skills/architecture/**` | application, frontend, and Effect doctrine |
| `skills/capability/**` | interface capability planning |
| `skills/harness/**` | shared, headless, UI, and frontend-test proof |
| `skills/preset/**` | reusable resolved project defaults |
| `skills/tooling/**` | executable profiles and source audit |
| `skills/contracts/ai-coding-os-suite-contracts/**` | independently installable coordination, vocabulary, patterns, Harness schemas |
| `skills/examples/**` | index to owner-local examples |

本仓只维护 grouped source，不生成、提交或发布一份并行 Flat source tree；但每个
Skill 必须能在下游被打平、重排或单独安装，不能把 grouped path 当成运行时合同。

## Canonical Trigger Names

```text
ai-coding-os
ai-coding-os-suite-contracts
goal-proof
goal-contracts
finding-proof-step
proof-step-implementation
write-work-plans
docs-governance
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

触发和人类可读的跨 Skill handoff 使用 `$skill-name`。目录名只服务源码组织；
共享 vocabulary/pattern 中的 `owner` 使用不带 `$` 的 canonical Skill ID。

## Invocation

- `$ai-coding-os` 是 user-invoked Router，frontmatter 使用
  `disable-model-invocation: true`。
- 需要自动发现或被相邻 Skill handoff 的专业 Skill 保留 model invocation。
- Frontmatter 保持最小：`name`、`description`，以及必要时的
  `disable-model-invocation`。
- 描述只承担触发分支和必要 reach clause，不复制 Skill body。

## Portable Suite Contracts

- `$ai-coding-os-suite-contracts` 是独立可安装 Skill，名称必须显式标识其服务于 AI Coding OS Suite。
- 安装集合由 runtime 实际发现；Contract Skill 不保存静态 Skill 清单、role taxonomy、invocation 副本或 routing 副本。
- 路由分支只在 `$ai-coding-os` 维护；共享 precedence、handoff、词汇、filename patterns、guarded terms 和 Harness schemas 由 `$ai-coding-os-suite-contracts` 提供。
- Skill 内相对链接只能落在本 Skill 目录内；跨 Skill 关系一律使用 `$skill-name`，不保留 sibling pointer。
- 可执行 Skill 不得在运行时读取其他 Skill 的相对路径。必须自包含的数据采用本 Skill 内固定快照，并由 Suite audit 校验与来源同步。

## Change Protocol

改 Skill 名、分组、触发、Schema、共享词汇或公开路由时，同一波次必须：

1. 更新 `skills/**` grouped source 与 frontmatter。
2. 更新 `$ai-coding-os-suite-contracts`、owner 字段和 owner-local `$skill-name` handoff。
3. 更新 `README*.md`、`AGENTS.md`、`docs/ssot/**`、本标准和必要 ADR。
4. 更新 templates、evals、checker、golden examples 和测试。
5. 运行 suite、repo 和 docs 验证并复扫 active surface。
6. 仅声明本仓实际证明的 source/repo 状态；下游分发保持 `not_claimed`。

## Public Claim Levels

| Claim | Required evidence |
| --- | --- |
| `source-updated` | grouped source、公开 docs、必要 templates/evals/checkers 已同步 |
| `repo-verified` | 本仓 build/typecheck/test、Suite audit 和 Docs audit 通过 |
| `retired-entry-absent` | active source/docs/templates/evals/registry 无退役入口 |
| `flatten-install-portable` | Skill 内链接不越界、Contract Skill 无静态 roster/path taxonomy、可执行 Skill 的隔离运行验证通过 |
| `downstream-distribution-not-claimed` | 未声明任何下游 runtime 或安装状态 |

## Required Verification

```bash
bun run check
python3 skills/tooling/suite_audit.py --suite skills
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
```

存在真实 Goal Pack 时逐个运行：

```bash
goal-proof check docs/goal-proof/goals/<goal-id>
```

复扫至少覆盖：

```text
frontmatter parse and invocation
cross-Skill reference closure and owner resolution
$skill-name handoff syntax
Skill-local relative-link containment
Preset isolated-install render and contract snapshot parity
capability-tier wording in Skill doctrine
retired trigger names
Flat source directories
relative Markdown links
Preset golden render
Effect API Kit atomicity and repair
```

历史 `evidence.jsonl` 与 retained source 保持原样；它们不定义当前 trigger 口径。
