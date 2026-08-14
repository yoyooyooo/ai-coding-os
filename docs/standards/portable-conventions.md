# Portable Conventions

> **Portable Defaults Standardize the Boring Choices.** 高能力 Agent 能发明一个有效结构，但跨项目工作仍需要低成本、可覆盖的稳定默认。

## Precedence

```text
1. accepted project authority
2. coherent adopted project convention
3. owning Skill's Portable Default
4. free invention
```

coherent project convention 必须让意义、scope、入口和例外可发现，并保护相关 invariant。

## Convention labels

### Invariant

无论工具或目录怎样变化都必须成立的语义、所有权或安全性质。

### Default

项目没有清楚本地选择时采用的兼容投影。Default 解决欠约束选择，不是 Universal Law。

### Conditional

只有出现明确 change、ownership、failure、lifetime、trust、reuse、navigation 或 machine-consumer pressure 时才加入的结构或机制。

### Project Override

保持 invariant、解释 local pressure 且可被未来读者发现的本地替代约定。

### Example

展示默认如何组合以及哪些角色被刻意省略，不是复制模板。

## Default projection index

| Concern | Portable Default | Owner |
| --- | --- | --- |
| Repository Agent entry | thin root `AGENTS.md` when durable local instructions exist | `$docs-governance` |
| Documentation | `docs/README.md`; reserved `product/`, `ssot/`, `standards/`, `architecture/`; conditional Homes by pressure | `$docs-governance` |
| Product knowledge | `docs/product/`, `docs/ssot/product-language.md`, selective capability documents | `$product-definition` |
| Application repository | single-host `src/` or multi-host `apps/`; `modules/`; conditional `workflows/`, `packages/`, hosts | `$evolvable-application-architecture` |
| TypeScript application naming | kebab-case semantic segments separated by dots；semantic roles 默认 co-locate，独立 pressure 出现后才拆文件 | `$evolvable-application-architecture` |
| Frontend source | `app/` or `host/`, `features/`, `shared/`; stable state-role suffixes | `$frontend-architecture` |
| Effect source | 在项目或 EAA source grammar 上投影 Service、Layer、Runtime、Queue、Stream、Actor 与 failure/resource mechanics，不建立第二套 application grammar | `$effect-best-practices` |
| Effect Server Module shape | private-first owning kernel；由真实 consumer 赢得窄 `*.public.ts`；Host bridge 拥有 config、transport、Runtime composition 与 lifetime | `$effect-server-module-design` |
| Verification | stable command roles; preferred `verify:affected` and `verify` aliases when practical | `$product-harness-system` |

## Deviating from a default

需要记录的 material deviation 说明：

```text
which invariant remains protected
which local pressure invalidates the default
what the alternative convention is
where future readers can discover it
```

不要求为每个 harmless local choice 创建 Exception Record。

## Avoid cargo-cult defaults

**Do Not Build Coconut Airports.** 不能因为某大厂、框架或旧版本使用某种形状就保留它。必须理解该形状降低了什么搜索、所有权、风险、反馈或工具成本，并在本地有相同压力。
