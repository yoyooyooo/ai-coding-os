# Product Brief

## Outcome and why now

AI Coding OS 要让一个高能力 Coding Agent 在陌生或长期演进的项目中，从任意真实问题进入，快速恢复正确的产品意义、知识 Authority、事实写入、状态所有权、运行入口、反馈边界和相邻知识，然后自主完成规划、实施、诊断与验证。

局部代码生成越来越便宜，但模糊 Authority、重复知识、隐式耦合、不可发现入口和偶然成功会被同样加速。系统的价值因此不在于增加 Agent 步骤，而在于让项目本身成为可靠的认知与反馈环境。

## Users and context

| User | Context | Desired result |
| --- | --- | --- |
| 技术/产品负责人 | 同时维护产品意义、架构边界与长期演进 | 多项目之间拥有统一但可覆盖的默认语法，减少重复对齐 |
| 本地高能力 Agent | 从代码、故障、需求或局部文档进入 | 无需先学习一套 Workflow，即可沿语义网络恢复足够上下文 |
| Skill 维护者 | 模型、工具和项目环境持续变化 | 保留稳定语义，删除失效脚手架，并防止体系再次膨胀 |

## Product capability

```text
六个项目面向语义 Owner
+ 一个可选 Router
+ 一个 Evolution 维护透镜
+ Owner-local Portable Defaults
+ 多入口 Progressive Disclosure
+ 项目级 Current Home、Architecture 与 Standards
```

这套能力不替 Agent 编排每一步，而是清楚表达世界、边界、默认值和现实反馈，使 Agent 能够自己选择策略。

## Product anchors

- **Project Authority First.** 使用项目已经接受的产品、SSoT、Standard、ADR、Contract 和直接 Evidence，优先于便携式 Skill 与模型猜测。
- **Local Agency, Bounded Authority.** Agent 主动完成局部可逆选择，但不能静默改变产品意义、持久数据、权限、公共契约或接受重大风险。
- **The Project Should Explain Itself.** 意图、源码、命令、测试、日志和局部知识共同构成 Agent-legible Change Surface。
- **Portable Defaults Standardize the Boring Choices.** 项目沉默时采用稳定默认，而不是让每个 Agent 重新发明目录和文件语法。
- **Feedback Horizon Sets the Safe Step Size.** 自主步长由可信反馈、错误定位和恢复能力决定，而不是由生成速度决定。

## Scope

### In scope

- Product Definition、Docs Governance、Application Architecture、Frontend、Effect、Harness 六个独立语义域。
- 自导航知识节点、Contextual Edges、精简模板和真实示例。
- 文档一级 Home、目录、文件、命名、项目入口和验证接口等跨项目默认值。
- Skill 网络自身的准入、消融、合并和反 Cargo Cult 判断。

### Explicit non-goals

- 统一 Ticket、Tracker、发布、审批或多 Agent Workflow。
- 中央 Architecture Database、全局 Registry、固定 ADIR、统一 Evidence Envelope 或静态 Eval Corpus。
- 用模板完整度代替产品理解、架构判断或运行证据。
- 自动替有权角色接受产品 Quality Boundary，或安全、隐私、法律、财务和不可逆风险。

## Quality Boundary

本项目至少必须保持：

```text
语义 Owner 边界清楚且无平行 Current Home
主 Skill、Reference、Template、Example 与项目 Docs 表达同一套思想
从任一常见现场可以进入，不依赖 Router 门禁
没有固定 Workflow 伪装成最佳实践
Portable Default 足够明确，但不要求创建未使用结构
高熵短语有稳定拼写、正式含义、适用边界和正确 Owner
Skill prose 为英文；项目 Docs 叙事为中文；路径和标识符保持英文
内部相对链接可解析，Reference 与 Template 都有真实路由
```

## Success and guardrails

| Outcome | Success signal | Guardrail |
| --- | --- | --- |
| 正确路由 | Agent 从问题直接命中最小 Owner 集 | 不把 Router 变成必经入口 |
| 局部演进 | 一次真实变化能沿 Agent-legible Change Surface 被理解和验证 | 不为想象未来创建全套抽象 |
| 跨项目一致 | 相同欠约束问题默认产生兼容目录、文件名和命令角色 | coherent project override 保持权威 |
| 真实反馈 | Claim 与实际 Observation Surface 对齐 | pass 不等于产品接受或生产证明 |
| 体系可演进 | 旧机制可以被缩窄、下沉、工具化或退出 | 不因强 Agent 可推断就删除有价值默认 |

## Assumptions and invalidating feedback

当前模型假设高能力 Agent 在语义、边界、默认值和反馈表达清楚后，能够自主完成策略选择与实施。如果真实项目反复表明某个独立语义域缺少必要 Owner、某项默认值制造持续冲突，或某种项目工程表面比 Skill 指令更可靠，应由 `$ai-coding-os-evolution` 重新评估，而不是继续堆叠流程。

## Current capability routes

- [Semantic Owners](../ssot/semantic-owners.md)
- [Skill Network](../architecture/skill-network.md)
- [Project Legibility](../architecture/project-legibility.md)
- [Portable Conventions](../standards/portable-conventions.md)
- [Semantic Compression](../standards/semantic-compression.md)
