# AI Coding OS

[English](README.md) | **简体中文**

AI Coding OS 是一套面向高能力 Coding Agent 的工程知识网络。它不替 Agent 规定统一步骤，而是让项目中的产品意义、知识 Authority、事实写入、状态所有权、运行入口、反馈边界和工程默认值变得清楚、可发现、可验证。

它建立在一个明确前提上：当项目能够解释自己的世界、边界和现实反馈时，成熟 Agent 已经能够自主规划、实施、诊断与验证。真正稀缺的不是更多流程，而是足够可靠的项目认知环境。

## 两个对齐的知识表面

```text
skills/  面向不同项目复用的语义知识，canonical prose 使用英文
docs/    维护本 Skill 网络的项目级 Current Home，使用中文叙事
```

`skills/**` 保存可移植的因果模型、边界、Portable Default、Reference、Template 与 Example；`docs/**` 保存本项目当前接受的 Product、SSoT、Architecture、Standards、ADR 和 Future Candidates。两者表达同一套思想，但拥有不同 Authority，不能互相冒充。

## 为什么需要它

代码生成越来越便宜，但下列问题会被同样加速：

```text
产品意义没有明确 Owner
源码现实被误当成目标决策
多个模块都能写同一事实
前端 intent、proposal、projection 与 interaction state 混为一体
资源、Runtime 和后台任务没有生命周期 Owner
测试通过，却说不清实际观察了什么
知识散落在聊天、旧文档、代码和个人记忆中
每个项目反复发明目录、文件名和验证命令
```

AI Coding OS 不用一套更重的 Workflow 包住这些问题，而是把稳定语义交还给正确 Owner，把可重复的低价值选择收敛为可覆盖的默认值，并让源码、命令、测试、日志和局部知识共同形成 Agent-legible Change Surface。

## 压缩原则

| Anchor | 当前含义 |
| --- | --- |
| **Project Authority First.** | 项目已经接受的 Product、SSoT、Standard、ADR、Contract 与直接 Evidence，优先于便携式 Skill、外部模板和模型猜测。 |
| **Source Is Not Decision.** | Source 说明当前实现现实，也能暴露漂移；它不能仅凭存在自动接受产品意义、质量、权限或目标架构。 |
| **Evidence Bounds Claims.** | Observation 只支持实际执行的性质、入口、路径、依赖、环境与时间范围；命令通过不等于产品完成。 |
| **Route Is an Edge, Not a Sequence.** | 链接表示相邻知识可能改变当前判断，不规定统一阅读、规划或实施顺序。 |
| **Local Agency, Bounded Authority.** | Agent 主动完成局部、可逆选择，但不能静默改变 Accepted Meaning、持久数据、权限、公共契约或重大风险接受。 |
| **No Silent Material Assumption.** | 足以改变结果或 Authority 的 Unknown 必须保持可见；普通低风险细节由 Agent 自主决定。 |
| **Strong Invariants, Weak Choreography.** | 冻结稳定语义、不变量、Stop Line 与 Claim Boundary，把普通可逆策略留给 Agent。 |
| **Minimal Context, Maximal Legibility.** | 只加载能改变当前判断的最小充分知识，同时让项目入口和因果关系容易恢复。 |
| **Shape Must Be Earned.** | 新目录、Package、Port、Service、Schema、Registry、Template 或 Skill 必须由真实变化、所有权、失败、生命周期、信任、复用、导航或机器消费压力赚得。 |
| **Portable Defaults Standardize the Boring Choices.** | 项目沉默时使用正确 Owner 的稳定默认，避免每个 Agent 重新发明一种方言。 |
| **The Project Should Explain Itself.** | Product meaning、源码边界、命令、测试、日志和局部知识应让新上下文恢复完整变化路径。 |
| **Feedback Horizon Sets the Safe Step Size.** | 自主步长取决于多久能发现错误，以及能否及时定位、停止与恢复，而不是取决于生成速度。 |
| **Preserve Semantics; Re-earn Scaffolding and Conventions.** | 保留仍会改变判断的语义；步骤、模板、默认值、Schema 和工具必须持续证明边际价值。 |

这些短句是认知压缩点，不是脱离上下文的口号。正式含义、反例、边界和具体机制仍由对应 Skill 与项目 SSoT 持有。

## 八个语义节点

六个项目面向 Specialist 可以直接成为入口：

| 当前问题 | Owner |
| --- | --- |
| 用户结果、Accepted Meaning、规则、权限、Quality Boundary、范围与验收 | [`$product-definition`](skills/product/product-definition/SKILL.md) |
| Current Home、Route、Freshness、文档拓扑、命名与清理 | [`$docs-governance`](skills/governance/docs-governance/SKILL.md) |
| 事实 Authority、Use Case、Transaction、Port、Composition、Consistency 与 Migration | [`$evolvable-application-architecture`](skills/architecture/evolvable-application-architecture/SKILL.md) |
| Intent、Projection、Interaction State、Realtime continuity 与 Frontend Host | [`$frontend-architecture`](skills/architecture/frontend-architecture/SKILL.md) |
| Effect failure、Scope、Resource、Structured Concurrency、Layer 与 Runtime | [`$effect-best-practices`](skills/architecture/effect-best-practices/SKILL.md) |
| Runnability、Observation、Diagnosis、Recovery Evidence 与 Regression Placement | [`$product-harness-system`](skills/harness/product-harness-system/SKILL.md) |

两个支持节点不占普通任务默认上下文：

- [`$ai-coding-os`](skills/router/ai-coding-os/SKILL.md) 只在问题确实模糊或跨域时提供薄 Owner Map，不是入口门禁。
- [`$ai-coding-os-evolution`](skills/meta/ai-coding-os-evolution/SKILL.md) 维护知识网络自身的准入、消融、合并、Portable Default 与 anti-Cargo-Cult 判断。

大型任务不自动需要全部 Skill。只加载能够改变当前判断的最小 Owner 集。

## Portable Default 与项目覆盖

跨项目默认遵循以下优先级：

```text
1. accepted project authority
2. coherent adopted project convention
3. owning Skill's Portable Default
4. free invention
```

一个 Project Override 只要可发现、保护相关 invariant，并说明本地压力为何使默认值不合适，就继续有效。Portable Default 用来统一低价值但反复出现的选择，不要求生成未使用的完整目录或 Artifact 家族。

## 从当前问题进入

- 需要便携式专业知识时，直接进入匹配的 `skills/**/SKILL.md`。
- 需要理解本项目当前意义和知识路由时，从 [`docs/README.md`](docs/README.md) 进入。
- 需要确认八个 Owner 与共同 Doctrine 时，查看 [`docs/ssot/README.md`](docs/ssot/README.md)。
- 需要稳定跨 Skill 词汇时，查看 [`docs/ssot/shared-vocabulary.md`](docs/ssot/shared-vocabulary.md)。
- 需要目录、命名、Semantic Compression 与验证约束时，查看 [`docs/standards/README.md`](docs/standards/README.md)。
- 需要理解当前网络为何如此设计时，查看 [`docs/adr/README.md`](docs/adr/README.md)。

不要求先经过 Router，不要求遍历全部 Skill，也不要求先生成固定 Artifact 再开始真实工作。

## 明确不做什么

AI Coding OS 不提供：

- 统一 Ticket、Tracker、审批、发布或多 Agent Workflow；
- 中央 Architecture Database、全局 Registry、固定 ADIR 或统一 Evidence Envelope；
- 用模板完整度替代产品理解、架构判断和运行 Evidence；
- 由 Agent 自动替有权角色接受产品、权限、安全、隐私、法律、财务或不可逆风险；
- 把一次测试通过夸大为生产行为、产品完成或 Quality Boundary 已被接受。

它提供的是更清楚的意义、Owner、边界、默认值、路由和反馈，使高能力 Agent 能在这些约束内自主工作。

## 语言约定

- `skills/**` 的 canonical prose、路径、命令、协议、Schema 与代码符号使用英文。
- `docs/**` 使用中文叙事，同时保留稳定英文术语作为跨项目检索和压缩锚点。
- 本中文 README 与 [English README](README.md) 独立可读，但共享同一组 Current Homes，不维护第二套语义真相。
