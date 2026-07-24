# Skills

本目录是 AI Coding OS 公开 Skill Suite 的 grouped source。目录按决策面服务维护者；
运行时触发名只取各 `SKILL.md` frontmatter 的 `name`。

## Groups

| Group | Owns | Skills |
| --- | --- | --- |
| `router/` | 用户显式入口与跨域知识路由 | `$ai-coding-os` |
| `goal/` | 可选 Goal Pack 方法及内部阶段 | `$goal-proof`, `$goal-contracts`, `$finding-proof-step`, `$proof-step-implementation`, `$write-work-plans` |
| `governance/` | docs layer、authority placement、cleanup、audit | `$docs-governance` |
| `architecture/` | 应用、前端与 Effect 架构决策 | `$evolvable-application-architecture`, `$frontend-architecture`, `$effect-best-practices` |
| `capability/` | interface capability、surface、state/data ownership、trace planning | `$interface-capability-planning` |
| `harness/` | 共享 harness、headless/UI proof、具体前端 test lane | `$product-harness-system`, `$headless-product-harness`, `$ui-product-harness`, `$frontend-test-system` |
| `preset/` | Agent-guided 可复用默认值发现、增量采用和 resolved project snapshot | `$evolvable-application-preset` |
| `tooling/` | 已确定架构决策的可执行生成与套件审计 | `$effect-api-app-kit`, `suite_audit.py` |
| `contracts/` | AI Coding OS 跨 Skill 协作、共享词汇和 Harness schema | `$ai-coding-os-suite-contracts` |

Supporting source：

- `examples/`：指向各 Skill/Preset 自有示例的索引。

## Common Vocabulary

- `claim`：当前观察允许声明的有界结论。
- `proof`：能够支持或证伪 claim 的执行或检查路径。
- `evidence`：实际命令、测试、截图、日志或 evidence record。
- `gap`：尚未实现、验证、决定或纳入 claim 的相邻面。
- `harness`：proof 的可运行观察面。

结构化 artifact 只在改善后续执行、验证、审计、交接或 claim 诚实时创建。

## Source Rules

- 触发 Skill 时使用 `$skill-name`，不使用目录名。
- 跨 Skill handoff 和关系使用 `$skill-name`。
- Skill 内相对链接不得逃逸本 Skill 目录；grouped source path 不是运行时依赖。
- 新 Skill 先确定独立 decision surface，再进入对应 group。
- 一个概念只有一个主 owner；相邻 Skill 通过 artifact/decision contract 协作。
- 本仓只维护 grouped source，不生成或保存 Flat 副本。
- Project authority 优先于 Preset 和通用 Skill 默认值。
