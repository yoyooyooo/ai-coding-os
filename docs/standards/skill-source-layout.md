# Skill Source Layout Standard

## Owns

- Canonical grouped Skill source、invocation boundary、progressive disclosure、Evals 和可移植性。
- Core source 与 Docs/release sidecars 的交付边界。

## Must Not Own

- 单个 Skill 的领域语义、项目执行状态或下游安装状态。

## Canonical Groups

```text
architecture/  architecture-decision-system, EAA, Frontend, Effect
capability/    interface-capability-planning
contracts/     ai-coding-os-suite-contracts
governance/    docs-governance
harness/       shared/headless/UI/frontend-test proof
meta/          skill-evaluation-system, ai-coding-os-evolution
preset/        evolvable-application-preset
product/       product-definition
router/        ai-coding-os
tooling/       effect-api-app-kit, suite audit, release builder
```

目录只服务源码维护。Skill 必须能独立、重排或扁平安装：相对链接不逃逸 Skill root，跨 Skill 关系使用 `$skill-name`，运行时不读取 sibling Skill 路径。需要固定数据时携带 Skill-local snapshot，并由 Suite audit 检查 parity。

## Main Skill Shape

主 `SKILL.md` 优先保留：

```text
owns / does-not-own
trigger boundary
strong invariants
material stop lines
Reference / Tool discovery interfaces
completion and claim ceiling
```

边缘案例、生态细节、长示例和专项方法下沉 References。固定步骤只有在真实状态机、事务、迁移、安全或外部协议要求顺序时出现。

## Invocation

- `$ai-coding-os` 与 `$ai-coding-os-evolution` 是显式调用入口。
- 专业 Skill 是否 model-invoked 取决于其独立 trigger 与相邻 reach value。
- Frontmatter 只允许 `name`、`description` 和必要的 `disable-model-invocation`。
- Description 负责发现，不承载完整方法论。

## Eval Contract

每个 Skill 至少有 owner-local Evals。静态 Eval 描述 trigger、成功行为、Owner 和 Claim Boundary；Model-run Evidence 独立版本化，不得伪装为已执行结果。

新增或修改强指令时，应能追溯到稳定不变量或 Protected Failure。Skill evaluation 先做 failure attribution，再选择 body edit、Reference、Router、Tool、Evaluator、Compatibility Overlay 或不修改。

## Source Hygiene

Canonical source 禁止：

```text
__MACOSX/
._*
.DS_Store
__pycache__ / *.pyc / *.pyo
嵌套 ZIP/TAR/GZ 交付包
生成缓存和机器绝对路径
```

本仓不发布 Flat 副本。Release ZIP、Audit、Manifest、Reports 和 checksums 在 `release/` 作为 sidecars 生成，不回嵌入 `skills/**`。

## Change Coverage

修改 Skill name、Owner、Profile、Schema、shared vocabulary 或 Router 时，同一变更覆盖：

```text
source and frontmatter
bounded handoffs and owner map
References / templates / Evals / golden fixtures
Docs Current Homes and ADR when semantics change
mechanical audit and release provenance
```

## Required Verification

```bash
python3 skills/tooling/suite_audit.py --suite skills --out release/suite-audit.json
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo . --readability
```
