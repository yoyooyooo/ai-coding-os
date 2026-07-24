# Tooling

本目录保存 Suite source 的可执行支持：

- `suite_audit.py`：离线校验 grouped source、frontmatter/cross-Skill reference closure、Schema、
  capability-tier 叙事、`$skill-name` handoff、Skill-local link containment、Preset
  contract snapshot / isolated install / golden output、Docs Governance compatibility
  与 Effect API Kit 原子性。
- `effect-api-app-kit/`：从明确 Change Spec 生成 P0-P3 Effect API capability slice
  的实验性原子 scaffolder。

从仓库根目录运行：

```bash
python3 skills/tooling/suite_audit.py --suite skills
```
