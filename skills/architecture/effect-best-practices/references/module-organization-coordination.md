# 模块组织与项目架构协同

目标：说明 `$effect-best-practices` 与 `$meta-project-architecture` 在“目录结构、命名语义、Effect 映射”上的分工，避免两边各写一套标准。

## 1) 谁负责什么

### `$meta-project-architecture` 负责

- 仓库级骨架：
  - `apps/` / `packages/` / `docs/`
- `src/` 顶层默认放什么：
  - 对外入口
  - 框架强约定目录
  - `internal/`
- 前端与非前端的默认组织策略：
  - 前端以 `features/` 为主，`app/` / `pages/` / `routes/` 作为入口壳
  - 非前端以直系子模块 + `internal/` 为主
- `internal/<module>/` 默认平铺，复杂度上来再目录化
- 哪些命名语义应该长期稳定

### `$effect-best-practices` 负责

- 把上述组织语义映射到 Effect：
  - `Context.Service`
  - `Layer`
  - `Scope`
  - `runtime`
- CLI / HttpApi / 资源生命周期 / 测试门禁 / 错误通道
- `repo.live`、`runtime` 这类 Effect 常见落法的边界与职责

结论：

- 项目骨架先看 `$meta-project-architecture`
- Effect 代码如何落地再看 `$effect-best-practices`

## 2) 推荐的稳定命名语义

这里不要求所有项目都长成同样目录树，但建议固定少量长期语义：

- `repo`
  - 稳定边界契约
  - 常见于数据访问、查询、外部能力抽象
- `live`
  - 生产实现
  - 常见于真实 IO、真实 Layer、真实外部依赖接线
- `runtime`
  - 装配与生命周期
  - 负责依赖组装、运行入口、资源释放、宿主接线

其余词例如 `domain`、`application`、`ports`、`adapters`，更适合作为分析语义与模块内部分层，而不是所有项目都必须存在的顶层目录名。

## 3) Effect 映射

### `repo`

推荐落法：

- `Context.Service`
- 最小 `interface`

职责：

- 暴露上层真正需要的最小能力
- 不透出 DB client / HTTP client / transport 细节

### `live`

推荐落法：

- `Layer`
- 生产适配实现

职责：

- 实现某个 `repo` / `gateway` / `publisher` 边界
- 把 infra 细节与异常映射到稳定错误语义

### `runtime`

推荐落法：

- `Layer.mergeAll(...)`
- `Effect.provide(...)`
- `Effect.scoped(...)`
- `runPromise` / `listen` / `mount` / `hydrate`

职责：

- 选择注入哪个实现
- 收口 Scope 与资源生命周期
- 提供最终运行边界

## 3.1) 包边界 runtime-bound facade

当一个子包内部需要 Effect DI，但外部 consumer 不应感知 Effect 时，推荐把包出口设计成 runtime-bound facade：

```text
internal service graph
  repo / gateway / transport Service
  live / fake Layer
  Scope / timeout / retry / typed error

package factory
  normalize host deps once
  build closed Layer
  create ManagedRuntime

public package API
  createXClient(config)
  Promise-returning methods
  subscription facade
  dispose / close when resources exist
```

这不是“保持纯函数”口径。`createXClient(config)` 是 runtime composition root。它允许内部 Effect-native，同时避免 React / feature / 普通调用方 import Effect runtime、Service key 或 Layer。

禁止把 containment 做成参数隧道：

```text
request helper receives config + fetchImpl each call
websocket helper receives WebSocketImpl each call
operation input carries host deps
```

host deps 应只在 factory / Layer boundary 归一化一次；operation helper 只接收业务 input，从 Service 获取依赖。

若某个包面向 Effect-native consumer，可以额外暴露单独的 Effect API，但 package root 的默认 facade 不应强迫普通前端消费 Effect 类型。

## 3.2) 外层骨架与内层纯函数边界

当项目已经决定“总体运行时骨架采用 Effect”时，推荐默认规则如下：

- 边界层默认使用 Effect
- 纯计算层默认保持普通函数

### 边界层默认使用 Effect

通常包括：

- CLI / MCP / HTTP 入口
- query orchestration
- repo / gateway / publisher 调用
- provider 选择与 fallback
- timeout / retry / cache / queue
- 资源生命周期
- 文件系统 / 网络 / 子进程 IO

原因：

- 这些位置天然有副作用、失败路径、依赖注入与资源释放问题
- 用 Effect 收口更稳定，便于 agent 大规模实施时保持一致风格

### 纯计算层默认保持普通函数

通常包括：

- parser
- mapper
- normalizer
- locator
- ranker
- manifest merge
- canonical ref 拼装
- 纯字符串或对象转换

推荐返回：

- 普通值
- `Option`
- `Either`
- 显式 `ParseResult`

只有在这些步骤需要被外层运行时编排、或需要统一错误通道时，再提升到 Effect。

### 常见判断法

可以用一条简单规则判断：

- 涉及 IO、时序、资源、外部依赖、降级路径时，优先 Effect
- 只做确定性数据变换时，优先普通函数

### 对 Agent 实施的意义

这条边界对 Agent 很重要，因为它能同时避免两种坏结果：

- 到处写 Promise / try-catch，导致运行时边界散掉
- 到处包 `Effect.succeed`，导致纯计算代码过度 ceremony

推荐结果是：

- 外层 service / handler / command 用 Effect
- 内层 mapper / parser / normalizer 用普通函数

## 4) 不要机械提升为目录名

以下词经常是正确的分析语言，但不建议一律提升为 `src` 顶层目录：

- `domain`
- `application`
- `ports`
- `adapters`

更稳的做法是：

- 先把它们用于文档、评审、ADR
- 只有在某个模块内部真的长大后，再把它们放进 `internal/<module>/` 下面做二级分层

## 5) 命名语法

推荐统一语法：

```text
subject.semantic[.variant].ts
```

例如：

- `user.repo.ts`
- `user.repo.live.ts`
- `cli.runtime.ts`
- `mcp.runtime.ts`

进入子目录后，若目录已经表达了该语义，可以适度去重，但要保留主体词。

例如：

```text
internal/catalog/repo/
├── catalog.ts
└── catalog.live.ts
```

## 6) 通用案例

以下结构只是说明“项目架构基线 + Effect 映射”如何配合：

```text
src/
├── index.ts
├── cli/
├── mcp/
└── internal/
    └── catalog/
        ├── catalog.repo.ts
        ├── catalog.repo.live.ts
        ├── query.flow.ts
        ├── locator.ts
        ├── envelope.ts
        ├── cli.runtime.ts
        └── mcp.runtime.ts
```

其中：

- `cli/`、`mcp/` 代表入口子模块
- `internal/<module>/` 承接复杂实现
- `repo / live / runtime` 通过文件名表达稳定语义
- 后续若复杂度上来，再把 `internal/<module>/` 内部目录化

若按“骨架用 Effect，局部保持纯函数”落地，可继续细分为：

```text
internal/<module>/
├── <module>.repo.ts       # Tag / interface
├── <module>.repo.live.ts  # Layer / IO
├── query.flow.ts          # Effect 编排
├── locator.ts             # 纯函数
├── envelope.ts            # 纯函数
├── cli.runtime.ts         # Effect runtime
└── mcp.runtime.ts         # Effect runtime
```

其中：

- `query.flow.ts` 可负责跨 repo、cache、provider 的运行时编排
- `locator.ts`、`envelope.ts` 更适合作为纯转换模块
