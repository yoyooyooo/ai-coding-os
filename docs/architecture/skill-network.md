# Skill Network

## Topology

```text
                         $product-definition
                          /        |        \
                         /         |         \
            $docs-governance  $frontend-architecture
                    \            /          |
                     \          /           |
             $evolvable-application-architecture
                         |                 |
                 $effect-best-practices   |
                         \                 /
                          $product-harness-system

$effect-server-module-design  supporting projection from settled EAA + Effect decisions
$ai-coding-os                 optional map legend
$ai-coding-os-evolution       maintainer lens
```

图只表达高频关系，不是调用顺序。任何 Specialist 都可以从当前症状直接进入。

## Direct entries

- [`$product-definition`](../../skills/product/product-definition/SKILL.md)
- [`$docs-governance`](../../skills/governance/docs-governance/SKILL.md)
- [`$evolvable-application-architecture`](../../skills/architecture/evolvable-application-architecture/SKILL.md)
- [`$frontend-architecture`](../../skills/architecture/frontend-architecture/SKILL.md)
- [`$effect-best-practices`](../../skills/architecture/effect-best-practices/SKILL.md)
- [`$effect-server-module-design`](../../skills/architecture/effect-server-module-design/SKILL.md)
- [`$product-harness-system`](../../skills/harness/product-harness-system/SKILL.md)
- [`$ai-coding-os`](../../skills/router/ai-coding-os/SKILL.md)
- [`$ai-coding-os-evolution`](../../skills/meta/ai-coding-os-evolution/SKILL.md)

## Why six project-facing Owners

六个 Owner 分别拥有独立 Authority、变化原因和失败方式：

```text
Product      what the product is supposed to mean
Docs         where durable project knowledge is current and discoverable
EAA          how accepted facts, capabilities, lifetimes, and migrations are governed
Frontend     how intent, projection, interaction, continuity, and host state are owned
Effect       how Effect models failure, Scope, resource, concurrency, and Runtime
Harness      how a property is run, observed, diagnosed, and protected
```

继续合并会让 Agent 必须加载更大的通用工程 Skill；继续拆分则容易把条件分支误升为独立 Owner。

## Server Module projection boundary

`$effect-server-module-design` 不是第七个项目语义 Owner。它只在 final writer、module/package admission 与 Effect v4 机制已经基本定案后，把这些决策投影为 private/public/Host bridge 文件边界。若 Authority、transaction、package pressure 或 Runtime 语义仍未定，必须回到 `$evolvable-application-architecture` 或 `$effect-best-practices`。

## Router boundary

`$ai-coding-os` 只在问题真正模糊或跨域时提供 Owner Map。它不维护任务状态、不规定 Hand-off Artifact、不要求所有任务先经过中央入口。

## Evolution boundary

`$ai-coding-os-evolution` 只处理 Skill 网络自身：知识放在哪里、某条指令是否应保留、Portable Default 是否仍有价值、某个节点是否拥有独立语义、失败应归因到哪一层。它不替项目决定产品或架构。

## Shared project qualities

全套 Skill 共同推动项目形成：

```text
meaning is discoverable
fact and state ownership are discoverable
run and reproduction entries are discoverable
failure preserves causal evidence
portable defaults reduce cross-project dialect drift
local changes remain local where the domain allows
old paths have fencing and deletion conditions when authority moves
```

这些是项目性质，不是必须生成的中央 Artifact。
