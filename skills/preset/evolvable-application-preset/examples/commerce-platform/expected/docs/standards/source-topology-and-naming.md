# Source Topology and Naming

本文件是 Preset 生成的候选 Standard。它只在对应 owner 审阅并合入项目 Current Home 后生效；通用架构语义不预设语言文件布局。

## 语义边界晋升

```text
local lexical grouping
  -> private semantic module
  -> enforceable compilation/public-API boundary
  -> independently runnable host
  -> independently deployed boundary
```

每次晋升都需要 visibility、dependency、compile、ownership、lifecycle、trust 或 deployment 的真实压力；目录、package、crate 或 deployable 本身不授予事实 Authority。

## Monorepo Projection

- Repository mode: `monorepo`
- Deployable hosts: apps/web, apps/api, apps/worker
- Workspace packages: packages/contracts, packages/testkit
- apps、packages、tooling、docs 是所选仓库拓扑，不是跨语言 Doctrine。
- package 不得 import app internals；共享 package 不会授予事实写入权。

## TypeScript / Node Projection

目录表达 durable ownership；文件名表达 local subject、responsibility、implementation 与 proof role。

```text
<subject>[.<facet>...].<responsibility>[.<qualifier>...].<extension>
```

一个 segment 内使用 kebab-case，语义维度之间使用点号。重复前缀只是 lexical cluster，不自动形成 module/package/authority。

### Selected Filename Patterns

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

- `*.policy.ts` 不依赖 HTTP、DB、SDK 或 live adapter。
- `*.use-case.ts` 不依赖 `*.live.ts` 或 transport handler。
- `*.port.ts` 不泄露 provider SDK / ORM 类型。
- 普通业务 module 不 import `*.wiring.ts`。

## Frontend Projection

- 远端 projection 只有一个 owner；本地 store 不镜像 server truth，host root 组装 live clients 与资源。

## Effect Projection

- Effect API、Service、Layer、Runtime 与 Scope 规则服从已安装 major 和声明文件；使用 Effect 不自动创建 package。

## Verification

- Harness 不绕过正式 use-case/materialization path；静态、fake、real、restart、migration 与 production claim 保持不同上限。

## Documentation Shape

`docs/**` 的 layer、partition、identity 与 Current Home 由 `$docs-governance` 决定。未使用的 layer 可以省略；默认保持扁平，只在 durable ownership、安全、保留、生命周期、读者路由或重复导航压力下分区。

## Profiles

- `agent-entry`
- `application-core`
- `monorepo-core`
- `typescript-node`
- `react`
- `effect`
- `effect-httpapi-v4`
- `verification-core`
- `headless-product-harness`
- `ui-product-harness`
