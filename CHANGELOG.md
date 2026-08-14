# Changelog

> Historical versioned-suite record. The current network of eight core Skills plus one supporting projection Skill is maintained through [`README.md`](README.md), [`docs/README.md`](docs/README.md), and the Future Candidates in [`docs/roadmap/README.md`](docs/roadmap/README.md); this history does not define the current topology.

## 0.6.0-experimental.1 — 2026-07-27

### Owner 与调用面收敛

- Canonical Skill 从 17 收敛为 12；六个语义 Owner 是唯一 model-visible surface。
- `$interface-capability-planning` 并入 `$product-definition` 的 Interface Capability Handoff。
- 三个细分 Harness Skill 并入 `$product-harness-system` 的 headless、UI/browser 与 frontend-test 分支。
- `$architecture-decision-system` 收窄为显式跨 Owner reconciliation Overlay。
- Preset 与 App Kit 改为 user-invoked tools，不再占普通模型上下文。
- `$skill-evaluation-system` 并入 `$ai-coding-os-evolution`；它没有独立入口或变化轴。

### 知识与工程现实

- `$ai-coding-os` 成为唯一完整语义 Owner Map。
- EAA、Frontend、Effect 与 Product Harness 术语迁回 owner-local vocabulary；Contracts 只保留生成式非权威索引。
- 建立唯一、条件加载的 Engineering Operating Doctrine，覆盖 Outcome、Authority、Reality、Changeability、Feedback、Containment、Operability 与 Responsibility；不新增 Workflow、评分或 Registry。
- Product、Docs、EAA、Frontend、Effect、Harness 与 Evolution 各自吸收适用的 Outcome、Quality、Containment、Recovery 与 Operability 语义。
- Harness 主 Skill 从 24 个叶子 Reference 链接收敛为五个分支入口。

### 删除未赚得的治理材料

- 删除 196-case 逐条迁移映射、223 个未执行静态 Eval、32 场景 coverage matrix 和 behavior-eval plan。
- 退休 Skill/Profile 只保留短 `MIGRATION.md`；内部 case ID 不再视为公共兼容合同。
- Release sidecar 从十二项收敛为 README、manifest、Suite audit、Docs audit 与 checksums。
- Suite audit 只保留 source/invocation、Authority、links、Schema/fixture、Preset/Kit 可执行 smoke、deterministic packaging 与 ZIP hygiene 等机械门。
- 模型行为改进只有在具体发布主张需要且真实运行对照后才能声明；当前为 `not_run / not_proven`。

## 0.5.0-experimental.1 — 2026-07-26

- 将 AI Coding OS 定位为 Agent-legible 项目认知、决策与验证基础设施。
- 确立 Project Authority First、Question-scoped Ownership、Evidence Bounds Claims、Earned Persistence 等 Doctrine。
- 将 EAA 收纯为跨语言 authority-first 内核，并增加 Rust Projection。
- 引入 Architecture Decision、Skill Evaluation 与 Suite Evolution 的实验性分层。
- 增强 Docs freshness、Product blind-spot、Harness empirical probes、Preset profile 和发布卫生。
- 该版本未证明独立模型行为、真实 Rust 项目迁移或生产行为。
