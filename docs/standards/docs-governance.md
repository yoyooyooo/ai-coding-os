# Docs Governance Standard

本标准是 `$docs-governance` 在本项目中的 adopted surface。

## Core anchors

```text
One Scoped Meaning, One Current Home.
Route Is an Edge, Not a Sequence.
Freshness Is Part of Meaning.
Build Documentation In; Do Not Bolt It On.
Shape Must Be Earned.
```

## Default first-level Homes

当项目拥有持久文档时，必须有：

```text
docs/README.md  documentation router
```

默认保留的一级 Home 名称：

| Home | Owns | Creation rule |
| --- | --- | --- |
| `product/` | 产品结果、范围、规则、质量、验收 | 首次产生持久产品知识时创建 |
| `ssot/` | 共享语言、对象、状态、不变量和跨域当前事实 | 首次出现跨多个 Owner 的共享意义时创建 |
| `standards/` | 当前真正绑定工作的工程或政策规则 | 首次接受长期约束时创建 |
| `architecture/` | 当前架构、边界、Host、Runtime、Composition 与变化关系 | 首次需要持久架构知识时创建 |

条件 Home 只有在独立语义长期成立时出现：

```text
adr/  design/  features/  protocols/  runbook/  security/
data/ research/ roadmap/ reports/ product-harness/ evals/
```

本项目当前的 `adr/` 与 `roadmap/` 分别由稳定引用和真实 Future Candidate 压力赚得。不得为了对称创建空 Home。

## Naming and depth

```text
ordinary paths and files       kebab-case
local router                   README.md
ordinary durable document      no numeric prefix
ordered stable decisions       0001-short-title.md
default depth                   docs/<home>/<optional-partition>/file.md
```

一级 Home 存在时应有 `README.md` 说明 scope、Current routes 和局部形状。一个层级默认只使用一个主要分类轴；子目录继承父 Home 的语义角色。

避免把生命周期或杂物状态当稳定 Home：

```text
old/  tmp/  misc/  phase-1/  final/  latest/
```

## Knowledge roles

```text
current authority  accepted meaning or binding constraint
source / evidence  implementation structure or bounded observation
working material   draft, investigation, plan, temporary synthesis
future             accepted target or unaccepted candidate, visibly separated
history            a decision or explanation that used to be current
```

一个文件可以包含多个角色，但每个 current claim 仍需清楚 Owner、scope 和 route。

## Freshness

重要文档应能让读者发现：支持它的 Authority 或 Source、适用 scope/environment、失效条件、更新责任以及可以确认或挑战它的 Evidence。可以用自然语言和链接表达，不要求所有文件拥有统一 frontmatter。

## Multi-entry discovery

项目知识应能从 Source、Failure、Product term、Command、ADR/Standard 和 Repository entry 进入。`AGENTS.md`、根 README 与 `docs/README.md` 是地图，不是必经根。

## Cleanup

当文档误导 Authority 或增加搜索成本时，选择最小动作：

```text
clarify | link | lower | merge | move | flatten | retain as history | delete
```

**A Tolerated Ambiguity Becomes a Copied Convention.** 明显冲突或破窗应被修复或明确隔离，不能让未来 Agent 把它当成项目惯例。

## Language

- `skills/**` canonical prose：English。
- `docs/**` narrative prose：中文；Canonical terms、路径、命令和代码符号保留英文。
- 同一 Home 内保持一致，不用语言混杂制造同义词漂移。
