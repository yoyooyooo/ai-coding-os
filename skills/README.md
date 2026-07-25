# AI Coding OS Core Skills

本目录是 AI Coding OS 核心 Skill Suite grouped source。它承载项目级知识、规范、Authority、架构、产品和 proof semantics；不承载 tracker、ticket、Goal 或 release workflow state。

## Groups

| Group | Owns | Skills |
| --- | --- | --- |
| `router/` | user-invoked knowledge Owner Map | `$ai-coding-os` |
| `contracts/` | portable knowledge kernel、Proof Surface、Evidence Envelope、eval、vocabulary、Harness schemas | `$ai-coding-os-suite-contracts` |
| `governance/` | documentation Authority、Routes、Earned Shape、cleanup、audit | `$docs-governance` |
| `product/` | product framing、source synthesis、model、decision、requirements、acceptance | `$product-definition` |
| `architecture/` | application、frontend、Effect architecture decisions | `$evolvable-application-architecture`, `$frontend-architecture`, `$effect-best-practices` |
| `capability/` | interface capability、surface、state/data ownership、proof needs | `$interface-capability-planning` |
| `harness/` | shared Harness architecture、headless/UI proof、frontend test lane | `$product-harness-system`, `$headless-product-harness`, `$ui-product-harness`, `$frontend-test-system` |
| `preset/` | reusable default discovery, candidate render, and selective project adoption | `$evolvable-application-preset` |
| `tooling/` | deterministic generation、core source audit、core bundle | `$effect-api-app-kit`, `suite_audit.py`, `build_suite_release.py` |

Goal Proof 位于 `../experiments/goal-proof/**`，是独立 user-invoked 早期实验，不属于本 roster。

## Portable Kernel

跨 Skill 的完整最小知识内核由 `$ai-coding-os-suite-contracts` 携带；根 README 提供面向用户的中英文说明。本索引不维护第三份 doctrine。

本目录只补充 source-authoring 约束：Skill 中的 Pass/Steps 默认表达 owner-local completeness 和 semantic dependency；只有真实状态机、事务、安全顺序、迁移或外部协议拥有 sequence。

## Common Vocabulary

- `claim`：当前观察允许声明的有界结论。
- `Proof Surface`：`surface_kind`、`dependency_reality`，以及按需存在的 `environment_class`、`proof_focus`。
- `Evidence Envelope`：只有真实机器消费者、durable citation 或重复 handoff 需要时，才以方向中立 v2 传递 source、claim ceiling、observed、supports、not_proven、evidence refs 和可选 Proof Surface；不传递 workflow lifecycle。
- `gap`：尚未实现、验证、决定或纳入 claim 的相邻面。
- `Route`：到 Authority、Evidence、source 或 neighboring owner 的 discoverable edge。

## Source Rules

- Runtime 触发名只取 `SKILL.md` frontmatter `name`。
- `$ai-coding-os` 是 user-invoked；边界明确时直接调用专业 Skill。
- Model-invoked description 只保留独立 trigger branches 和必要 reach clause。
- 相对链接只指向本 Skill；跨 Skill handoff 使用 `$skill-name`。
- `SKILL.md` 内联各 branch 共用的内容；branch-only reference 通过 context pointer 按需加载。
- 一个 meaning 一个 source；删除 duplication、sediment、sprawl 和 no-op。
- Skill split 由独立 invocation 或真实 sequence boundary 支撑，不由目录对称和篇幅支撑。
- 核心只维护 grouped source，不生成 Flat 副本。
- Project Authority 优先于 Preset、Router 和通用 Skill defaults。

## Bundle-local Verification

解压 Core ZIP 后，可在 bundle root 直接运行：

```bash
python3 -m pip install -r skills/requirements-audit.txt
PYTHONDONTWRITEBYTECODE=1 python3 skills/tooling/suite_audit.py --suite skills --out audit.json
python3 skills/tooling/build_suite_release.py --repo . --audit audit.json --out-dir dist
```

`skills/VERSION` 提供 Core 版本；audit 的 `source_tree_sha256` 必须与待打包
`skills/**` 完全一致，否则 builder 拒绝输出。Builder 会在 `dist/` 同目录写入
versioned canonical audit、manifest、change report 与 composition review；canonical
provenance 不包含机器绝对路径或 compiler-dependent template-typecheck 状态。

## Bundle-local Route

- Core contracts：[`contracts/ai-coding-os-suite-contracts/SKILL.md`](contracts/ai-coding-os-suite-contracts/SKILL.md)

完整仓库还提供根 `README.zh-CN.md`、`docs/standards/skill-source-layout.md`
和 `experiments/goal-proof/README.md`。这些是 Core ZIP 明确排除的上游 surface，
因此这里只作普通路径说明，不伪造 bundle 内链接。
