# goal-proof

[English](README.md) | **中文**

Goal Proof 实验 CLI。用于查看 Goal Pack 状态、读取当前 work item、
记录 evidence、应用确定性进展、校验文件一致性。Goal Proof 是共仓早期实验，
不属于 AI Coding OS 核心 Skill Suite 或 Router。实验边界见仓库中的
`experiments/goal-proof/README.md`。

可用于任意 Goal Pack 目录。裸 goal id 从 writer fallback
`.goal-proof/goals/` 解析；采用其他 artifact home 的项目显式传入已解析的
`goal_pack_root`。CLI 0.2.x 仍读取旧 `docs/goal-proof/goals/`，用于有限迁移兼容。

Goal Pack schema v2 新模板需要 CLI `>=0.2.0 <0.3.0` 才能读取列表形态的
`completion.required_evidence`；0.2.x 继续兼容旧 scalar reader。

```bash
npm install -g goal-proof@^0.2.0
```

## 常用流程

```bash
goal-proof summary .
goal-proof list . --completion todo
goal-proof inspect <goal-id>
goal-proof work list <goal-id>
goal-proof evidence list <goal-id> --limit 5
goal-proof relations goals . --thread <thread-id> --completion todo --json
goal-proof relations work . --thread <thread-id> --completion todo --json
goal-proof relations check . --thread <thread-id>
goal-proof work brief <goal-id>
goal-proof check <goal-id>
```

`summary` 和 `list` 面向项目级使用。`inspect`、`work list`、`work brief`、
`work activate`、`evidence list`、`evidence show`、`evidence add`、`apply`
和 `check` 面向单个 Goal Pack。`relations` 面向项目或 goals 目录使用，
用于检查连续性元数据，并发现 thread 成员 goal/work 候选。它不创建队列、
scheduler、thread 生命周期、存储图或执行顺序。

## 命令

```bash
goal-proof --help
goal-proof <command> --help
goal-proof inspect <goal-pack> [--json]
goal-proof summary [project-root|goals-dir] [--completion all|todo|done] [--status <status>] [--depth repo|groups|items] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof list [project-root|goals-dir] [--completion all|todo|done] [--status <status>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof work list <goal-pack> [--completion all|todo|done] [--status queued|active|blocked|done] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof work brief <goal-pack> [--work <id>] [--json]
goal-proof work activate <goal-pack> --work <id> [--dry-run]
goal-proof evidence list <goal-pack> [--limit N] [--work <id>] [--type discovery|decision|implementation|coordination|review|planning] [--result done|blocked] [--decision <value>] [--next-action proof_step|continue|needs_plan|blocked|review|done|needs_human] [--completion-satisfied true|false] [--changed-file <glob>] [--command-status pass|fail] [--contains <text>] [--include fields] [--show-empty] [--json]
goal-proof evidence show <goal-pack> --index N [--json]
goal-proof evidence add <goal-pack> (--file evidence-record.json | --json '<json>' | --stdin) [--apply] [--check] [--dry-run]
goal-proof relations list [project-root|goals-dir] [--thread <id>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations goals [project-root|goals-dir] [--thread <id>] [--completion all|todo|done] [--status forming|ready|running|blocked|done|retired] [--next-action proof_step|continue|needs_plan|blocked|review|done|needs_human] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations work [project-root|goals-dir] [--thread <id>] [--completion all|todo|done] [--status queued|active|blocked|done] [--goal-completion all|todo|done] [--goal-status forming|ready|running|blocked|done|retired] [--goal <goal-id>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations check [project-root|goals-dir] [--thread <id>] [--json]
goal-proof relations graph [project-root|goals-dir] [--thread <id>] [--json]
goal-proof apply <goal-pack> [--dry-run]
goal-proof check <goal-pack>
```

`<goal-pack>` 可以是显式 `goal_pack_root` 目录，也可以是
`.goal-proof/goals/` 下的裸 goal id。`summary` 可接收项目根目录或 goals
目录；不传参数时从当前目录向上查找。

读类 JSON 命令使用统一输出控制：`--limit` 限制可见集合，`--include
path,objective,links` 补回省略字段，`--show-empty` 显示空值和默认值。
`summary` 默认 `--depth groups`、`--limit 20`；`--depth items` 把 threaded
goals 放在 `threads` 下，顶层 `items` 只放 unthreaded goals。

对 `summary` 和 `list`，`--completion todo` 表示 Goal Pack status 既不是
`done` 也不是 `retired`。对 `work list`，`--completion todo` 表示 work item
status 不是 `done`。

对 `evidence list`，多个过滤条件按 AND 组合，默认输出 compact evidence
record 摘要。需要展开单条完整 evidence record 时使用 `evidence show --index N`。
对 `evidence add`，必须在 `--file`、`--json`、`--stdin` 三个输入源里选一个。
`--stdin` 用于 heredoc JSON；常见追加、确定性 apply、校验路径可用
`--apply --check`。加 `--dry-run` 可预览 append/apply/check 而不写文件；
JSON 输出包含 `changed_paths`。

对 `relations`，`list` 显示关系元数据，`goals` 发现 thread 成员 Goal Pack，
`work` 发现 thread 成员 work item，`check` 用 token-aware 方式校验关系证据，
`graph` 渲染派生关系图。`relations.thread_id` 只是标签。

典型执行环：

```text
check -> inspect -> work brief -> work -> evidence add -> apply -> check
```

## 发布

从仓库根目录执行发布：

```bash
bun run release:check patch
bun run release patch
# 或
bun run release 0.2.0
```

`bun run release:check` 验证发布所需 git 状态，不改文件。
`bun run release` 在临时本地 release 分支写入 CLI 版本，同步 `packages/cli/package.json` 与 `bun.lock` workspace 版本，给该提交打 tag，并且只 push tag。
实际 npm 发布是单独配置的 release step，本仓不声称已配置。

## 开发

```bash
bun install
bun run --filter goal-proof build
bun run --filter goal-proof typecheck
bun run --filter goal-proof test
```
