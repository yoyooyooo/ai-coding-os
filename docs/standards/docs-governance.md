# Docs Governance

本标准是 `$docs-governance` 在本仓的项目适配：约束 docs layer、question-scoped Authority、multi-entry Routes、Earned Shape、生命周期和审计门。

## Owns

- `docs/*` layer、partition、router 和 identity 的准入。
- Current / accepted-target / future / historical classification。
- 文档 promotion、demotion、retention 和 cleanup。
- 从问题、code area、artifact、source 与 Evidence 到 Authority 的 Routes。
- 本仓 Docs audit 最低机械检查口径。

## Must Not Own

- AI Coding OS 产品定位；归 `docs/product/**`。
- 产品 requirements、acceptance 和 product decision；归项目 Product Authority。
- 当前术语与方法事实；归 `docs/ssot/**`。
- 技术取舍；归 `docs/adr/**`。
- Tracker、ticket、实验方法、release process 或其他 execution state。
- Skill source layout；归 [Skill Source Layout](skill-source-layout.md)。

## Network Contract

```text
Authority  one canonical Current Home per claim, representation, and scope
Route      discoverable edge, not mandatory sequence
Shape      semantic layers and earned partitions
Evidence   bounded support for current claims
```

`AGENTS.md`、`docs/README.md`、layer README、source anchors 和 direct artifact links 都可以是入口。不存在必须从根文件开始的统一阅读顺序。

`docs/README.md` 可按 question、Authority、code area 或 artifact 提供并列投影视图。投影视图只保存 links 和 scope，不复制 current truth。

## Layer Contract

`docs/<layer>` 表示 durable semantic Authority role，不表示阶段、团队、临时计划、工具或 workflow。

| Layer | Owns | Must Not Own |
| --- | --- | --- |
| `product` | 产品/方法论定位、用户价值、非目标 | implementation status、工程规则 |
| `ssot` | 当前共享对象、术语、状态、不变量 | future complete model、execution state |
| `standards` | 可执行规则、命令、质量门和协作标准 | 未采纳愿景或一次性计划 |
| `adr` | 已采纳技术取舍和后果 | Product decision，除非项目显式扩大范围 |
| `architecture` | 当前拓扑、owner、boundary 和 accepted seam | Product behavior、task queue |
| `roadmap` | future sequence、gate 和 Evidence links | tracker/ticket/experiment status 副本 |
| `reports` | audit、delivery、experiment、migration、validation evidence | current Authority merely because recent |
| `interface-capabilities` | InterfaceCapability trace | 产品事实、测试代码、execution state |
| `product-harness` | Harness contract、coverage、claim ceiling、Evidence refs | 用户能力语义、runner code、workflow state |

Layer 可以省略。创建 top-level layer 需要独立 Authority role、未来可判断的语义名、清楚 Owns/Must Not Own 和实际 reader/lifecycle pressure。

## Internal Shape And Identity

Layer 默认扁平。只有 durable ownership、安全、保留、生命周期、release、reader routing 或持续导航压力成立时才增加 partition。子目录继承父 Authority。

普通 artifact 默认使用 semantic path。Sequential ID 只用于 ADR 等 append-only collection；requirement/control/test ID 由真实 traceability 触发；`node_id` 只用于 opt-in Artifact Graph。

数量、成熟度、对称性和美观只是 review signal，不是 admission rule。

## Authority By Question

| Question | Primary Authority |
| --- | --- |
| 系统应该做什么 | accepted product/business decision 或 baselined requirement |
| 当前存在什么实现结构 | source、schema、migration、lockfile、generated artifact |
| 哪些行为被实际观察 | executed tests、Harness、runtime、release 或 operational Evidence |
| 共享 term/state/invariant 是什么 | SSoT 与 accepted decision |
| 为什么这样决定 | Product Decision Record 或技术 ADR |
| 接口接受什么 | adopted protocol/schema 与 contract evidence |
| 当前 topology/owner 是什么 | source facts 与 Architecture view |
| 当前 work status/complete 是什么 | repository-selected execution owner 与 release evidence |

源码证明实现结构和静态属性；runtime、reachability、deployment 和 environment behavior 需要执行或观察 Evidence。它们都不能静默重定义 Product、SSoT、Standards 或 ADR。冲突按 question 和 scope 分类为 coexistence、supersession、documentation drift、implementation gap、unaccepted implementation、Evidence gap、obsolete source 或 missing Authority；这些不是全局状态机。

被接受的决定改变其他 Current Home 时，更新受影响 Home、记录暂时 drift、降低相关 claim，或说明影响不适用；本标准不规定处理顺序。

## Lifecycle

```text
promote   accepted durable meaning enters its owner
demote    non-authoritative material remains source/report/evidence
split     mixed Authority or lifecycle separates
merge     duplicate current meanings converge
partition durable local boundary earns a child route
flatten   redundant partition returns to semantic parent
bridge    broken Route or traceability edge is repaired
retain    source/evidence still affects future decisions
delete    obsolete material has no Authority or evidence value
block     higher-authority decision is required for the affected claim or mutation
```

`block` 默认局部化：保留 competing source 与 Evidence Route，标出所需外部决定，继续其他不受影响的 classification、link、layer 和 cleanup。只有 Evidence 无法保全或继续修改会造成不可逆仓库级损坏时，才停止整个 run。

Execution artifacts remain with their selected method. A done ticket, workflow item, Goal, or release task does not automatically accept Product intent, document lifecycle, Standards, ADR, or Roadmap state. Durable decisions discovered during execution return to their semantic owner through an explicit decision.

## Scan Policy

默认 Docs audit 机械检查：

```text
declared routes and relative links
layer ownership contracts
explicit identity conflicts
Earned Shape review signals
Future route honesty
AGENTS managed markers
repository-root boundaries
declared source anchors
```

Scanner 只检查已声明 edge 是否可达，不规定阅读顺序，也不把语义判断自动化。可选 readability extension 检查 discovery surfaces 和 local Routes，不要求 `Read First`。

## Required Verification

```bash
bun run check:core
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
git diff --check
```

涉及共仓 experiment 时运行其 owner-local check，但不把 experiment pass 写成 core claim。

## Routes

- 文档网络：`../README.md`
- 当前事实：`../ssot/README.md`
- Standards：`README.md`
- Skill source layout：`skill-source-layout.md`
- Core architecture：`../architecture/README.md`
