# Architecture Decision And Uncertainty Standard

## Owns

- 架构 Claim、material issue、decision rights、Commitment Boundary、ADIR 和 Health 的项目级规则。

## Must Not Own

- 产品语义、事实本身、某生态的地道实现细节或模型行为分数。

## Local ADIR First

默认只构建当前问题所需的最小 ADIR。不得为了形式完整性扫描全仓、填满 Schema 或虚构 unknown values。只有跨 Agent、长期迁移、多生态投影、持续 Health/Diff 或机器消费者出现时，才持久化并提升 IR 层级。

## Scope And Claim Axes

关键 Claim 必须能区分：

```text
scope / version / host / consistency domain
authority state
knowledge basis
temporal plane
evidence state
semantic owner / decision owner / fact authority / evidence owner
invalidates_when
```

这些 Owner 不得合并为一个泛化 `authority` 字段。

## Material Unknown

只有会实质改变结果、承诺或 Claim 的 Unknown 才升级为 Issue。普通私有命名、可逆局部结构和 owning Agent 能自行决定的技术细节不升级给人类。

处理顺序是语义规则，不是固定 Workflow：

```text
normalize scope
classify issue
identify owner and decision rights
choose decide | assumption | probe | isolate | escalate | stop
preserve safe-to-proceed boundary
attach proof obligation and invalidation
```

## Stop Lines

在以下边界前，相关决定必须闭合：

- 产品语义、权限、安全或法律义务；
- 持久数据、公共兼容性和不可逆迁移；
- 金钱、生产操作或不可逆外部 effect；
- 新的事实 Writer、Authority Epoch 或双写；
- 声称真实 Adapter、重启恢复、迁移或生产行为已经成立。

## Architecture Health

Health Finding 必须说明 basis、scope、rule、severity、smallest repair、smallest verification、not_proven 和 invalidates_when。不得把 Unknown 当 Failure，不得用平均分遮蔽 critical writer、stale assumption 或 Claim Overreach。

## Project Materialization

```text
current topology / boundary -> docs/architecture
accepted tradeoff           -> docs/adr
binding rule                -> docs/standards
future migration/gate       -> docs/roadmap
point-in-time health        -> docs/reports
```

不创建 `docs/architecture-ir/` 或全局 `unknowns.md`。
