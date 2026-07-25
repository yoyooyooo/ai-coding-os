# ADR: AI Coding OS 命名与边界

## Status

Superseded by [2026-07-25 Core Knowledge Network and Goal Proof Experiment Boundary](2026-07-25-core-knowledge-network-and-goal-proof-experiment.md).

## Context

本仓已经从单一 Goal Proof / Goal Diffusion 实验，演进为按 decision surface
分组的 AI coding 方法套件。旧口径存在三个问题：

- `ai-coding-project-os` 把品牌拉回项目管理或项目级工具。
- `Goal Diffusion` 曾同时承担隐喻、方法名、CLI/package、skill 名和目录名，边界过宽。
- `Project` 作为品牌词会遮蔽真实方法论边界；当前默认落地边界其实是 workspace/repo。

本仓还需要同时保留一个现实约束：`goal-proof` CLI / npm package 已经是独立公开
命令面，重命名 CLI/package 会引入额外 release 和兼容决策。

## Decision

采纳以下命名和边界：

- 方法论和 skill suite 品牌名：`AI Coding OS`。
- 默认用户入口 Skill：`$ai-coding-os`，采用 user-invoked 薄路由。
- Suite 共享合同 Skill：`$ai-coding-os-suite-contracts`；名称显式携带服务归属，可在大型扁平 Skill 集合中独立识别。
- 应用架构主入口：`$evolvable-application-architecture`。
- 长目标与 Goal Pack 系统：`Goal Proof System`。
- CLI / npm package：继续使用 `goal-proof`。
- `Goal Diffusion` 从活跃叙事和对象中退役，只保留在 ADR context 与历史材料中。
- `Project` 不进入品牌名；默认落地边界表述为 `workspace/repo`。
- 活跃 docs、skills、templates、tests、CLI docs 和 package metadata 不保留旧入口 alias。
- 历史 `evidence.jsonl` 和 `docs/goal-proof/sources/**` 可保留旧口径作为追溯材料，但不能作为当前口径引用。
- Skill source 只保留 grouped layout；人类可读的跨 Skill 关系使用 `$skill-name`，不生成 Flat 副本。
- grouped path 不是 runtime contract；Skill 内相对链接不得越界，可安装 Contract Skill 不保存静态 Skill 清单，可执行 Skill 不通过 sibling path 读取其他 Skill。

## Alternatives

- 保留 `ai-coding-project-os`：
  - 拒绝。该名称会让 agent 把套件误解成项目管理 OS，而不是通用 AI coding 方法论。
- 把 CLI / npm package 也改成 `ai-coding-os`：
  - 暂不采纳。CLI 当前明确服务 Goal Pack / Goal Proof，不拥有整个 OS suite。
- 在 README 保留 `Goal Diffusion` 隐喻：
  - 拒绝。它会与 authority routing 和 Goal Proof state transition 形成重复心智模型。

## Consequences

- 跨域或入口不明确的工作从 `$ai-coding-os` 进入；明确任务可直接使用专业 Skill。
- 只有显式选择或仓库采用 Goal Proof 时才路由到 `$goal-proof`。
- 后续新增方法或 Skill 时，按 decision surface 放入 grouped source；Preset、可执行 profile 与 Suite contracts 分别进入 `skills/preset`、`skills/tooling` 和 `skills/contracts`。
- 旧 skill 名和旧目录名不得作为兼容 alias 分发。
- repo 外壳、公开 skill source layout 和旧名退役必须按
  [Skill Source Layout](../standards/skill-source-layout.md) 收敛。

## Evidence

- 当前事实：[docs/ssot/README.md](../ssot/README.md)
- 文档路由：[docs/README.md](../README.md)
- skill suite index：[skills/README.md](../../skills/README.md)
- 验证命令：
  - `bun run check`
  - `python3 skills/tooling/suite_audit.py --suite skills`
  - `python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .`
  - `goal-proof check docs/goal-proof/goals/<goal-id>`
