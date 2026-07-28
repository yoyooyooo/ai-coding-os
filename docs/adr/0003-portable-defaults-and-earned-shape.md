# ADR-0003: Portable Defaults and Earned Shape

## Context

仅保留思想会让每个项目重新发明 `docs/` Homes、文件名、源码后缀、Feature 形状和验证命令；恢复完整 Preset、Profile 和模板家族又会制造空结构和 Cargo Cult。

## Decision

区分 Invariant、Portable Default、Conditional Addition、Project Override 和 Example。稳定默认值由正确语义 Owner 持有，在项目沉默时采用；结构扩张仍必须由真实压力赚得。

优先级：

```text
accepted project authority
> coherent adopted project convention
> owning Skill's Portable Default
> free invention
```

## Alternatives

- 所有项目统一完整树：过度结构化，忽略项目已有形状。
- 完全自由发明：跨项目漂移、搜索和工具成本持续增加。
- 中央 Preset/Generator：让默认值物化系统重新成为额外 Owner。

## Consequences

- 恢复文档一级 Home、命名、源码语法、前端和 Effect 后缀、验证命令角色等低成本默认。
- 不要求创建空目录、全后缀家族或所有模板。
- Project Override 只需在 material 地影响搜索、所有权、公共契约或工具时记录。
- 强 Agent 可推断一个有效答案，不自动使 Default 过期。

## Invalidates when

某项默认不再降低跨项目熵，或持续与主流生态、真实项目形状和工具产生更高成本。
