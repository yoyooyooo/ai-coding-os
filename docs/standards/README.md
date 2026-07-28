# Standards

## Owns

- 本项目 `docs/**` 与 `skills/**` 的当前绑定规则、Portable Default、命名和内容演进边界。

## Must Not Own

- Product meaning、架构事实、运行观察或单次工作状态。

## Current Standards

- [Docs Governance](docs-governance.md)
- [Source Topology and Naming](source-topology-and-naming.md)
- [Portable Conventions](portable-conventions.md)
- [Semantic Compression](semantic-compression.md)
- [Suite Evolution](suite-evolution.md)
- [Verification Policy](verification-policy.md)

## Rule admission

一条强约束至少满足一项：

```text
保护稳定语义、Authority、Safety 或 Ownership invariant
防止一个可复现、代价显著且更低层无法可靠阻止的失败
为重复出现的欠约束选择提供低成本跨项目默认
```

否则先改善项目知识、源码边界、类型、命令、测试、日志或工具。
