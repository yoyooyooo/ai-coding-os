# Source Topology and Naming

本文件是 Preset 生成的候选 standard，不是当前项目 Authority。只有对应 owner 审阅并合入 Current Home 后才生效。

## Repository Topology

- Repository mode: `monorepo`
- Deployable hosts: apps/web, apps/api, apps/worker
- Workspace packages: packages/contracts, packages/testkit
- capability module 默认保持私有，跨边界只暴露明确 public surface。
- host composition 与普通业务调用分离。
- package 不得 import app internals。
- TypeScript 跨 module 普通调用使用 `<subject>.public.ts`；host composition 可使用 `<subject>.wiring.ts`。
- Effect 使用不自动创建 package；API 与 runtime 规则服从已安装 major。

## Source Topology: Bounded Semantic Flatness

```text
目录表达 durable ownership
文件名表达 local subject / responsibility / implementation / proof role
package 表达 compile/import boundary
app 表达 runnable/deployable lifecycle
```

文件名语法：

```text
<subject>[.<facet>...].<responsibility>[.<qualifier>...].<extension>
```

一个 segment 内使用 kebab-case；不同语义维度使用点号。按“产品语义 -> 局部能力/操作 -> 架构职责 -> 实现细节”排序。

重复点号前缀只是 lexical cluster，不是 module/package/authority。只有独立 owner、依赖规则、资源生命周期、替换/迁移、编译或部署压力出现时才晋升。

## Documentation Shape

项目 `docs/**` 的 layer、partition 与 identity 由 `$docs-governance` 负责。Preset 输出可以提供 broad candidate，但不是每个项目都必须采用的目录树；未使用的 layer 可以省略，layer 默认保持扁平，二级目录只有在 durable ownership、安全、保留、生命周期、读者路由或重复导航压力成立后才建立。Preset 不自动创建 `node_id`、编号体系或未来影子 authority。

## Canonical Patterns

```text
<subject>.<operation>.command.ts
<subject>.command-context.ts
<subject>.<operation>.use-case.ts
<subject>.<read-purpose>.query.ts
<subject>.<capability>.port.ts
<subject>.transaction.port.ts
<subject>.idempotency.port.ts
<subject>.<capability>.<provider>.live.ts
<subject>.<capability>.memory.fake.ts
<subject>.public.ts
<subject>.wiring.ts
<subject>.http.contract.ts
<subject>.http.handlers.ts
<subject>.client.ts
<subject>.query.ts
<subject>.store.ts
<subject>.realtime.ts
<subject>.view-model.ts
<subject>.surface.tsx
```

不机械生成完整后缀套装。框架保留文件名可以例外，但 adapter 应保持薄。

## Import Boundaries

- `*.policy.ts` 不依赖 HTTP、DB、SDK 或 live adapter。
- `*.use-case.ts` 不依赖 `*.live.ts` 或 transport handler。
- `*.port.ts` 不泄露 provider SDK / ORM 类型。
- `*.http.*.ts` 只 decode/map/call use case，不直接写数据库。
- 普通业务 module 不 import `*.wiring.ts`。
- `*.fake.ts` 不能无提示进入 production composition。
- 本地 store 不镜像 remote projection；host root 组装 live client 与资源。
- Harness 不得绕过正式 use-case/materialization path。

## Promotion Ladder

```text
lexical cluster -> private submodule -> workspace package -> deployable process
```

每次晋升都需要真实压力；目录或 package 本身不授予事实写入权。

## Profiles

- `agent-entry`
- `monorepo-core`
- `typescript-node`
- `react`
- `effect`
- `effect-httpapi-v4`
- `verification-core`
- `headless-product-harness`
- `ui-product-harness`
