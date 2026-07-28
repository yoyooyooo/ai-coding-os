# ADR-0004: Semantic Compression Language

## Context

精确但冗长的工程术语能够表达边界，却不一定在复杂现场迅速唤醒整条因果链；大量新格言又会形成 Suite 私有方言和隐喻噪声。

## Decision

冻结少量 network-level anchors，并允许每个 Specialist 保留约 3–5 个 local anchors。每个 anchor 必须拥有精确拼写、正式含义、对照边界、现实后果和语义 Owner。

记忆句可以与正式术语成对存在，例如：

```text
One Fact, One Final Writer.
  -> Final Materialization Authority

The Project Should Explain Itself.
  -> Agent-Legible Change Surface

Do Not Outrun Your Headlights.
  -> Feedback Horizon
```

生产路径、API、Schema 和代码符号继续使用直接、可搜索的命名，不追求文学化。

## Alternatives

- 只使用长术语：现场唤醒和跨节点恢复成本较高。
- 大型中央 Glossary/Registry：复制 Owner 定义并增加维护耦合。
- 大量比喻：私有语言过重，重要词失去区分度。

## Consequences

- 根地图、Owner 主 Skill 和关键 Reference 可以精确复现同一 anchor。
- `docs/ssot/shared-vocabulary.md` 只冻结拼写和一句话含义，详细定义仍回到 Owner。
- 新短语需要 admission，旧同义词需要合并或退出。

## Invalidates when

真实使用表明某个 anchor 不再改变判断、产生稳定误读，或同一因果链已有更通用的工程词汇。
