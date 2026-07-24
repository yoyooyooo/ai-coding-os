# Standards

本层保存可执行规则、命令、质量门和协作 SOP。

## Owns

- 开发和验证命令。
- 文档治理规则。
- skill 源码布局和入口口径。
- Goal Proof System schema 迁移时必须同步的对象。
- agent 协作规则。

## Must Not Own

- 产品定位。
- 当前 Goal Pack 运行状态。
- 未决取舍。

## Boundary

本层写可执行规则：命令、检查门、命名、schema 同步要求、文档治理 SOP、
skill 源码布局规则和 agent 协作规则。它不解释产品为什么存在，也不保存当前任务状态。

当本层规则和代码行为冲突时，代码只能证明当前实现状态；是否接受该行为为新规则，
必须通过本层、SSoT 或 ADR 明确更新。

## Promotion / Demotion

- 重复出现的 review 规则、命令门、docs governance 规则、skill source layout 规则，
  从 Goal Pack、roadmap 或 report promote 到本层。
- 一次性计划、候选取舍或执行证据从本层 demote 到 roadmap、ADR、Goal Pack 或 report。
- 被 ADR 或更高标准替代的旧规则应删除，不能留下并行 current home。

## 开发标准

使用 Bun：

```bash
bun install
bun run build
bun run typecheck
bun run test
bun run check
```

改公开命令、Goal Pack schema、evidence record 语义、skill 口径时，同步更新：

- `README.zh-CN.md`
- `README.md`
- `skills/**`
- `skills/**/templates/**`
- CLI checker / renderer
- tests

## Skill 源码布局标准

- 详细规则见 [Skill Source Layout](skill-source-layout.md)。
- AI Coding OS 是对外开源源码仓；本仓只定义 `skills/**` grouped source layout、公开触发名和本仓验证口径。
- 当前公开 Skill Suite 入口见 [skills/README.md](../../skills/README.md)；跨 Skill 合同、共享词汇和 Harness schemas 由 `$ai-coding-os-suite-contracts` 提供。
- Skill 运行时触发名由 `SKILL.md` frontmatter `name` 决定，不由目录名决定。
- 下游用户或维护者如何安装、复制、镜像或分发 skill，属于 downstream distribution，不写入本仓公开叙事。
- 退役 Skill 不保留兼容 alias；历史 evidence/source 可保留追溯材料，但不能定义当前口径。
- 本仓只维护 grouped source，不生成 Flat 版本。
- 改 suite 收口策略时，默认先改本仓 `skills/**` 和公开 docs，再运行本仓验证；不得把下游 runtime 或同步工具状态说成本仓事实。

## 文档标准

- 新增文档必须放入正确 `docs/*` 层。
- 高密度目录必须有 README。
- 每个 durable docs layer README 至少包含 `Owns`、`Must Not Own`、入口或 `Read Next`；权威密集层还必须包含 `Boundary` 或冲突规则，以及 promotion / demotion 路径。
- 详细文档治理规则见 [Docs Governance](docs-governance.md)。
- 不创建 `docs/specs/**`；实施规格放 root `specs/**`。
- 不保留两个 current home。
- 叙述性正文使用中文；字段名、命令、路径和 schema 示例可保留英文。

## Goal Proof System 标准

- `$goal-proof` 是显式选择的可选执行方法；任务复杂度本身不触发 Goal Pack。
- Proof path 优先；文档、计划和 work item list 只有在缩短执行、验证、审计或交接路径时才保留。
- 用户明确要求目标计划、Goal Pack 或使用 `$goal-proof` 时，由 Goal Pack 承载该 workstream 的 durable planning state。
- 随口小需求不创建 Goal Pack；直接 inline 实施并验证。
- 简单工作不引入 strict proof。
- 高风险工作使用 `evidence_mode: strict`。
- 真实 Goal Pack 的历史 `evidence.jsonl` 不重写，只追加。
- `plans/<work_id>.md` 不作为第二套任务系统。
- Goal Pack ready 必须同时满足 goal contract stable，且 `progress.yaml.proof_step`
  已被授权在 `claim_limit` 内产出或检查 `completion.required_evidence`；roadmap
  段落、future command name、work item list 或 docs-only preface 不能单独使 Goal Pack ready。
- First proof step 应是 runnable 或 inspectable movement。docs-only first proof step
  只在目标 delta 本身就是承载 claim 的 doc / review authority surface，且 proof
  step 能检查 diff、交叉引用、authority conflict 或 static scan 时成立。
- 重要 completion / promotion evidence 应采用 SSoT / Goal Proof 拥有的跨方法
  Evidence Envelope Discipline：列出实际 commands/checks、positive evidence、叙事性的
  changed surfaces、`not_claimed`、叙事性的 `not_proven` 或 remaining gaps，不能只堆散 token。
  除非同步升级 schema、template 和 checker，`changed surfaces` 与 `not_proven` 不表示
  v2 completion review 的正式字段。

## Skill Suite 验证

```bash
python3 skills/tooling/suite_audit.py --suite skills
```

该检查覆盖 frontmatter/cross-Skill reference closure、共享 Schema、`$skill-name` handoff、
Skill-local link containment、Preset isolated-install/golden render、退役入口、
capability-tier 叙事、Flat source 和 Kit 原子性。

## Read Next

- 当前事实：`../ssot/README.md`
- 结构视图：`../architecture/README.md`
- 文档治理：`docs-governance.md`
- Skill source layout：`skill-source-layout.md`
