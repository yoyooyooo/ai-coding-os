# Source Topology and Naming

## Canonical Skill groups

```text
skills/
  architecture/  evolvable-application-architecture, frontend-architecture, effect-best-practices
  governance/    docs-governance
  harness/       product-harness-system
  meta/          ai-coding-os-evolution
  product/       product-definition
  router/        ai-coding-os
```

目录用于 Suite package projection 和本地 audit，不赋予运行时顺序或跨仓 content Authority；本仓八个 tracked core Skill 的 `skills/**` 内容由 Agent Kit admitted snapshot outbound 投影，候选正文和附件变化按 package contribution route 回到 Synpraxis，再经 AK admission。`experiments/goal-proof/skill/**` 是 experiment-owned 的独立 bidirectional mapping，不属于 core outbound ownership。

本 Ticket 的 docs/config 只声明 routing contract，不证明 Synpraxis source merge、AK admission、export、package commit/push 或 npm release；Ticket 04 提供 live evidence。`release/**` 仍是 historical pre-import evidence，不在本 Ticket 重生成。

## Canonical roster

```text
6 project-facing model-visible semantic Owners
1 thin Router with disable-model-invocation: true
1 Evolution lens with disable-model-invocation: true
```

新增 Skill 必须拥有独立语义问题、变化轴和反复昂贵的上下文；仅拥有输出格式、总与另一节点共同触发或同步变化的节点应保持为 Reference 或退出。

## Skill root shape

```text
<skill>/
  SKILL.md
  references/   conditional causal depth
  templates/    small reusable defaults only when repeatedly valuable
```

Example 可以放在 `references/` 中并明确标识。不得为目录对称生成空 `templates/` 或完整文件家族。

## Frontmatter

`SKILL.md` 只使用：

```yaml
name: canonical-skill-name
description: problem-oriented discovery description
disable-model-invocation: true  # only when needed
```

Description 负责让真实问题发现 Owner，不承载完整方法论。

## Knowledge-node writing

主 Skill 优先保留：owned question、3–5 个 Semantic Anchors、最小因果模型、recognizable pressures、critical boundaries、Portable Default 和少量 adjacent Owner routes。

Reference 回答一个稳定问题或因果关系；跨 Skill 关系使用 `$skill-name`，不要求独立安装的 Skill 读取 sibling 路径。Owner 内部相对链接不得逃逸 Skill root。

## File naming

```text
Skill and reference directories        kebab-case
main entry                              SKILL.md
ordinary references/templates          kebab-case.md
canonical Skill name                    kebab-case
semantic anchor spelling                exact Title Case sentence defined by Owner
```

不要使用 `misc`, `common`, `general`, `other`, `manager` 等无法预测 scope 的桶名。

## Language

- Portable Skill prose、frontmatter 和 examples：English。
- Paths、commands、protocols、schemas、symbols：English unless an external contract requires otherwise。
- Project Docs language 由项目决定；本项目采用中文叙事。

## Templates and examples

保留模板的条件是它反复减少真实歧义、足够短、由正确 Owner 拥有且容易删除未使用章节。优先少数真实 Example，不恢复空白 Artifact 操作系统。

Example 先展示 smallest valid base，再以 pressure-labelled deltas 表达可选文件、目录、机制和文档。Role 与 suffix 列表是 vocabulary，不是 generation manifest；semantic separation 不自动要求 physical separation。

## Deliberately outside canonical Skills

不把版本、Release、迁移账本、统一 Machine Contract、代码生成 Kit、静态 Eval Corpus、中央 Vocabulary Registry 或 Suite Builder 作为日常 Skill 内容。真实消费者出现时，由消费者或正确 Owner 建立最小载体。
