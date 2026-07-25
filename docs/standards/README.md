# Standards

本层保存可执行规则、命令、质量门和协作标准。

## Owns

- 核心 Suite 与共仓实验的验证命令。
- 文档治理和 Skill source layout。
- Skill 写作、invocation、coverage 与 eval 标准。
- 公开 contract/schema 变化时必须同步的 surface。

## Must Not Own

- 产品定位、当前 execution state、未决取舍或实验结论。

## Boundary

Standards 规定当前如何检查和协作。代码只能证明实现状态；是否接受实现为新规则，需要更新对应 Standard、SSoT 或 ADR。

## Repository Gates

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run check:core
bun run check:goal-proof-experiment
bun run check
bun run bundle:skills
```

- `check:core`：核心 Suite audit 与 Docs audit。
- `check:goal-proof-experiment`：Goal Proof Skill self-check、CLI build/typecheck/tests。
- `check`：整仓聚合门，不合并 Core/Experiment claim。
- `bundle:skills`：生成 core-only Suite ZIP、audit JSON 与 manifest。

## Skill Authoring Standard

详细 source 规则见 [Skill Source Layout](skill-source-layout.md)。

- Skill 触发名由 `SKILL.md` frontmatter `name` 决定，不由 grouped folder 决定。
- Model-invoked description 只保留独立 trigger branches 和必要 reach clause。
- User-invoked Skill 由人类承担索引成本；核心 `$ai-coding-os` 和实验 `$goal-proof` 均为 user-invoked，但属于不同分发边界。
- `SKILL.md` 内联所有 branches 共用的步骤、强不变量和 completion criterion；branch-only reference 通过条件明确的 pointer 披露。
- Pass/Steps 默认表示 owner-local coverage 与 semantic dependency，不规定 Agent 推理顺序。真实状态机、事务、安全顺序、迁移和外部协议可以拥有 sequence。
- 一个 meaning 一个 source；清理 duplication、sediment、sprawl 和 no-op。
- Leading word 必须真实改变 invocation 或 execution predictability，不为形式对称复制。
- Eval 使用真实近邻 prompt；关键 case 的 expectations 同时覆盖正向产物、ownership 和 claim boundary。
- 相对链接只指向本 Skill；跨 Skill 关系使用 `$skill-name`。
- 核心 source 只维护 `skills/**` grouped layout；Goal Proof experiment 位于 `experiments/**`，不进入核心 roster。

## Documentation Standard

- Durable 内容按语义 Authority 放入 `docs/*` layer。
- `docs/README.md` 与 layer README 暴露 Routes，不规定 Read First 顺序。
- Agent 可以从问题、code area、term、artifact、source 或 Evidence 进入知识网络。
- Layer 默认扁平；partition、identity、registry 和 graph metadata 由实际压力触发。
- 同一 claim、representation 和 scope 不保留两个 canonical Current Home；portable Skill output path 不能覆盖项目 Authority。
- Execution artifact、ticket blockers 和 workflow status 留在 selected method，不复制到 Roadmap、SSoT 或 Artifact Graph。
- 高密度 durable layer 需要薄 router；router 只链接，不复制 current truth。
- 不创建 `docs/specs/**`；项目采用 implementation spec 时使用 root `specs/**`。

详细规则见 [Docs Governance](docs-governance.md)。

## Contract Synchronization

改公开 contract、schema、Skill boundary、Preset output 或 CLI behavior 时，按 owner 同步：

```text
SKILL.md and references
templates and schemas
evals and fixtures
public README / owner docs
checker / renderer / CLI help
tests and golden output
migration note when semantics break
```

核心 Evidence Envelope v2 是按真实消费者压力存在的方向中立 claim-boundary shape，不编码 tracker、ticket、Goal 或 release workflow lifecycle；legacy v1 directional shape 仅作有限 reader compatibility。Goal-specific schema/template/CLI compatibility 留在 experiment。

## Core Suite Audit

```bash
python3 skills/tooling/suite_audit.py --suite skills
```

覆盖 core frontmatter、Skill-local links、cross-Skill refs、Proof/Evidence/Harness/eval schemas、targeted negative cases、eval IDs、Preset candidate/profile provenance/language closure/golden/merge/upgrade、Docs audit compatibility、Effect Kit project-bound P3/command timeout/structured rollback、subprocess timeout、bundle-only rebuild、canonical audit sidecar、跨路径确定性、source provenance 和 source hygiene。

## Experiment Audit

```bash
python3 experiments/goal-proof/scripts/self_check.py
bun run --filter goal-proof test
```

实验自检覆盖 user invocation、Skill-local references、Goal/Progress/Evidence templates 与 eval shape；CLI tests 覆盖实际读写与兼容。实验通过不构成核心 Suite claim。

## Promotion / Demotion

- 重复出现且当前适用的命令、质量门和协作规则 promote 到本层。
- 一次性计划、候选取舍、历史 evidence 和 experiment status 留在其 owner。
- 被新 ADR/Standard 替代的旧规则应 supersede 或删除，不能并行保持 current。

## Routes

- 当前事实：`../ssot/README.md`
- 文档治理：`docs-governance.md`
- Skill source layout：`skill-source-layout.md`
- 结构视图：`../architecture/README.md`
- Goal Proof experiment：`../../experiments/goal-proof/README.md`
