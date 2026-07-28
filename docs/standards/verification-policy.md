# Verification Policy

本项目的验证目标是确认内容网络内部可用，而不是把机械检查夸大为模型行为或真实项目证明。

## Content integrity

应检查：

```text
8 canonical SKILL.md entries exist
6 project-facing Skills are model-visible
Router and Evolution remain disable-model-invocation: true
frontmatter contains only supported fields
all local Markdown links resolve
all referenced templates and examples are routed
no Reference contradicts its owner SKILL.md
canonical semantic-anchor spellings remain stable
Skill prose remains English
project Docs routes point to current files
archive contains no __MACOSX, ._* or traversal paths
```

## Semantic review

机械链接正确不能证明思想一致。Review 还要检查：

```text
one independent semantic Owner per Skill
portable defaults distinguished from invariants and mandates
no fixed workflow hidden in headings, ladders, gates, or template families
no stale report or historical material acting as Current Home
concrete best practices retained where they reduce real ambiguity
high-entropy anchors decompressed by formal meaning and boundary
```

## Claim boundary

内容检查最多支持：当前文件、路由、命名和内部语义已经按所述规则组织。

它不证明：

```text
模型在真实任务中一定表现更好
某个项目架构或产品决策正确
外部 Provider、浏览器、恢复或生产行为已经验证
Quality Boundary 已被接受
```

这些主张必须由对应项目 Authority 和 Observation Surface 提供证据。
