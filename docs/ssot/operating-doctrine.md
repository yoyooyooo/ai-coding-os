# Operating Doctrine

这些短句是整套体系的认知压缩点。它们不是脱离上下文的口号；每一句都在正确 Owner 中继续解压为因果、边界、反例、默认值和实现知识。

## Project Authority First.

使用项目已经接受的 Product、SSoT、Standard、ADR、Contract 和直接 Evidence，优先于便携式 Skill、外部模板和模型猜测。Portable guidance 在项目沉默时提供默认，不覆盖清楚的本地 Authority。

## Source Is Not Decision.

源码、Schema、配置和 Lockfile 说明当前实现现实，也可能暴露文档漂移；它们不能仅凭存在自动接受产品意义、质量、权限或目标架构。

## Evidence Bounds Claims.

观察只支持它实际执行的性质、入口、依赖真实性、环境、输入和时间范围。`observed`、`supports`、`not observed`、`contradicted` 和 `not proven` 必须保持不同；通过命令不等于产品完成。

## One Scoped Meaning, One Current Home.

同一 scoped meaning 在同一 time plane 只有一个 Current Home。地图、README、局部注释、报告和历史材料可以路由或解释，但不复制第二份平级当前真相。

## Route Is an Edge, Not a Sequence.

链接表示“当前判断可能需要这份相邻知识”，不表示必须按固定顺序阅读、规划或执行。只有真实状态机、事务、安全协议、迁移和外部协议可以拥有必要顺序。

## Local Agency, Bounded Authority.

Agent 应主动完成局部、可逆、保持 accepted semantics 的选择；不得静默扩大范围、重定义权限、改变持久数据含义、破坏公共兼容或替有权角色接受重大风险。一个 Unknown 只阻塞它能够改变的承诺。

## No Silent Material Assumption.

足以改变 Accepted Meaning、Authority、持久数据、公共兼容、权限、迁移或不可逆外部效果的 Unknown，不能被 Agent 静默填成事实。普通、低风险、可逆细节可以自主决定；Material Unknown 必须保持可见并归属能够决定它的 Owner。

## Strong Invariants, Weak Choreography.

明确稳定语义、不变量、决策权、Stop Line 和 Claim Boundary，但不要用固定 Workflow 代替高能力 Agent 的策略判断。真正有必要的顺序只来自业务状态机、事务、安全协议、迁移或外部协议。

## Minimal Context, Maximal Legibility.

只加载能够改变当前判断的最小充分知识，同时让 Product meaning、源码入口、命令、测试、日志和相邻节点容易恢复。更多文本不自动等于更清楚；不可发现的项目也不能靠更厚 Prompt 修复。

## Shape Must Be Earned.

目录、Package、Port、Service、Schema、Registry、模板和新 Skill 只有在独立变化、所有权、失败、生命周期、信任、复用、导航或机器消费压力下才成立。视觉对称、流行和想象未来不能单独赚得结构。

## Portable Defaults Standardize the Boring Choices.

项目没有 coherent adopted convention 时，使用正确 Owner 的稳定默认。默认值减少跨项目重复发明、搜索和工具歧义；它们不是 Universal Mandate，也不会要求生成未使用的完整树。

## The Project Should Explain Itself.

项目应让新上下文从 Product meaning、源码入口、事实 Writer、Capability boundary、Composition root、命令、测试、日志和局部知识中恢复完整变化路径。Agent 失败时，先检查项目是否缺少可发现、可运行或可诊断的工程表面。

## Feedback Horizon Sets the Safe Step Size.

安全速度取决于多久能知道自己错了，以及错后能否定位、停止和恢复。生成速度不是安全速度；不可逆数据、真实资金、公共契约和外部副作用会缩短可接受照距。

## One Failure, One Lowest Reliable Owner.

一次失败的学习应进入最底层、最可靠的防线：产品语言、类型、契约、不变量、Use Case、Port、State Owner、测试、监控、工具或项目知识。不要在多个 Skill 中复制同一条提醒。

## Preserve Semantics; Re-earn Scaffolding and Conventions.

模型、工具和项目能力改变后，仍然会改变重要判断的语义继续保留；步骤、模板、默认值、Schema 和工具则需要继续证明其边际价值。强 Agent 能推断出一个答案，不自动意味着跨项目默认已经失去价值。
