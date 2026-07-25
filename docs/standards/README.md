# Standards

## Owns

- 当前 AI Coding OS 项目文档、Skill 源码、Architecture Decision、Skill evaluation 和发布的强制规则。
- 机械审计入口与 Claim Ceiling。

## Must Not Own

- Product positioning、Current facts、决策原因、Future candidate 或单次运行结果。

## Current Standards

- [Docs Governance](docs-governance.md)
- [Skill Source Layout](skill-source-layout.md)
- [Architecture Decision And Uncertainty](architecture-decision-and-uncertainty.md)
- [Skill Evaluation And Release](skill-evaluation-and-release.md)

## Rule Admission

一条 `must / never / always` 级指令至少满足一项：

```text
保护模型无关的语义不变量
防止一个可复现、受保护的真实失败
```

否则应考虑缩窄、下沉 Reference、接口化、工具化、Rubric 化、兼容层化或删除。Instruction 也必须 Earn。

## Verification

```bash
python3 skills/tooling/suite_audit.py --suite skills --out release/suite-audit.json
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo . --readability
```

机械检查通过不等于模型行为、真实迁移或生产行为已经证明。

## Routes

- [当前事实](../ssot/README.md)
- [Architecture](../architecture/README.md)
- [ADR](../adr/README.md)
- [Reports](../reports/README.md)
