# Source Topology and Naming

本文件是当前项目生效的 resolved standard。通用理论来自 Suite Skills；本文件记录本仓库采用结果。

## Repository Topology

- Repository mode: `monorepo`
- Deployable hosts: apps/web, apps/api, apps/worker
- Workspace packages: packages/contracts, packages/testkit
- 后端默认从 `apps/api/src/modules/<capability>` 的私有 capability module 开始。
- 跨 module 普通调用只使用 `<subject>.public.ts`；host composition 可额外使用 `<subject>.wiring.ts`。
- package 不得 import app internals；module 不因使用 Effect 自动成为 package。

## Bounded Semantic Flatness

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

## Canonical Patterns

```text
order.create.use-case.ts
order.by-id.query.ts
order.repository.port.ts
order.repository.postgres.live.ts
order.repository.memory.fake.ts
order.http.contract.ts
order.http.handlers.ts
order.public.ts
order.wiring.ts
channel.client.browser.live.ts
channel.query.ts
channel.store.ts
channel.realtime.ts
channel.view-model.ts
channel.surface.tsx
order.checkout.retry.harness.ts
```

不机械生成完整后缀套装。框架保留文件名可以例外，但 adapter 应保持薄。

## Import Boundaries

- `*.policy.ts` 不依赖 HTTP、DB、SDK 或 live adapter。
- `*.use-case.ts` 不依赖 `*.live.ts` 或 transport handler。
- `*.port.ts` 不泄露 provider SDK / ORM 类型。
- `*.http.*.ts` 只 decode/map/call use case，不直接写数据库。
- 普通业务 module 不 import `*.wiring.ts`。
- `*.fake.ts` 不能无提示进入 production composition。
- Harness 不得绕过正式 use-case/materialization path。

## Promotion Ladder

```text
lexical cluster -> private submodule -> workspace package -> deployable process
```

每次晋升都需要真实压力；目录或 package 本身不授予 accepted-fact 写入权。

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
