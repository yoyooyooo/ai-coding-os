# AI Coding OS 文档网络

本目录保存 AI Coding OS 当前的产品意义、共享语义、架构关系、跨项目约定和已接受决策。它是一张可以从不同现场进入的知识网络，不是阶段目录、发布记录或必读清单。

> **Route Is an Edge, Not a Sequence.** 路由帮助当前问题找到相关知识，不规定统一阅读、规划或实施顺序。
>
> **Core outbound package mirror.** 八个 core Skill 的 `skills/**` 映射内容来自 Synpraxis，经 Agent Kit upstream admission 后由 accepted snapshot outbound 投影；Skill content 问题回到 Synpraxis，package/release metadata 留在本仓维护。
>
> **Goal Proof boundary.** `experiments/goal-proof/skill/**` 是实验拥有的独立 bidirectional mapping，不属于八项 core outbound ownership。

## 按问题进入

| 当前问题 | Current Home |
| --- | --- |
| AI Coding OS 为谁解决什么问题、成功边界是什么 | [Product Brief](product/product-brief.md) |
| 全套共同世界观、精确术语和语义 Owner | [SSoT](ssot/README.md) |
| 八个 Skill 如何组成自导航网络，项目如何向 Agent 解释自己 | [Architecture](architecture/README.md) |
| 文档 Layer、目录、文件、命名、写法和演进约束 | [Standards](standards/README.md) |
| 为什么接受当前 Owner、网络、默认值和高熵叙事 | [ADR](adr/README.md) |
| 哪些能力仍是 Future Candidate、在什么压力下重新进入 | [Roadmap](roadmap/README.md) |
| 实际便携式知识入口 | [`skills/**/SKILL.md`](../skills/) |
| Skill content ownership 与 mirror routing | [`skills/README.md`](../skills/README.md) |
| package contribution 与 release metadata | [`CONTRIBUTING.md`](../CONTRIBUTING.md) |
| Goal Proof experiment mapping 与边界 | [`experiments/goal-proof/README.md`](../experiments/goal-proof/README.md) |

## 当前一级 Home

```text
product/       当前产品结果、范围、质量与非目标
ssot/          共享 Doctrine、语义 Owner 与统一词汇
standards/     当前绑定文档和 Skill 内容的规则
architecture/  当前知识网络、可发现性与跨 Owner 关系
adr/           已接受且值得稳定引用的长期决策
roadmap/       尚未成为 Current 的能力候选与重新准入压力
```

前四个是本项目已经拥有持久内容的默认核心 Home；`adr/` 与 `roadmap/` 分别由稳定引用和真实 Future Candidate 压力赚得。本项目不保留 `reports/`，因为点时发行证据不再是核心知识面。

## 三种现实必须分开

```text
Accepted Meaning  当前被有权角色接受的产品或工程含义
Source Reality     当前源码、Schema、配置和依赖实际表达的结构
Observed Reality   某次真实执行、测试、浏览器或外部依赖产生的观察
```

**Source Is Not Decision.** 源码可以暴露偏差，但不能静默接受产品或架构含义。

**Evidence Bounds Claims.** 观察只支持它实际执行的性质、路径、依赖、环境和时间范围。

## Package projection route

```text
Synpraxis tracked source (eight core Skills)
  -> Agent Kit upstream admission
  -> Agent Kit admitted snapshot
  -> ai-coding-os skills/** outbound projection
```

Agent Kit collect 不从本 outbound mirror 回收 mapped core Skill content；dirty mirror 的 export 会安全跳过。Goal Proof 的 `experiments/goal-proof/skill/**` 保持 experiment-owned，并使用与上述 core edge 分离的 bidirectional mapping，不属于 core outbound ownership。`README*`、`skills/README.md`、`CONTRIBUTING.md`、`docs/**`、`VERSION`、`CHANGELOG.md` 与 `release/**` 仍是 package-owned surfaces。

## 当前证据边界

本 Ticket 只声明 routing/config contract。当前 docs/config 不证明 Synpraxis source merge、AK admission、export、package commit/push 或 npm release；Ticket 04 提供 live evidence。`release/**` 与 [`release/README.md`](../release/README.md) 继续是 historical pre-import evidence，本 Ticket 不重生成它们。

## 跨项目一致性

当项目已经有清楚、连贯、可发现的本地约定时，保留项目约定；项目沉默时，采用拥有该问题的 Skill 所给出的 Portable Default。默认值负责统一低价值但反复出现的选择，Agent 的判断力应留给真正影响结果的差异。

## 语言策略

- `skills/**` 的 canonical prose、路径、命令、协议、Schema 和代码符号使用英文。
- `docs/**` 使用中文叙事，同时保留稳定英文术语作为跨项目检索和压缩锚点。
- 项目外部合同的语言由合同本身决定。

## 直接路由

- [产品](product/README.md)
- [共享事实与词汇](ssot/README.md)
- [架构](architecture/README.md)
- [标准](standards/README.md)
- [决策](adr/README.md)
- [未来候选](roadmap/README.md)
