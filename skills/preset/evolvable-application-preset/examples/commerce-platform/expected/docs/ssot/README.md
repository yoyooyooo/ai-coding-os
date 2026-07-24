# SSoT

## Owns

- 当前事实、对象所有权与不变量

## Must Not Own

- 未来候选、目录规范、运行日志

## Boundary / Conflict

仓库当前权威优先；本层只拥有上面列出的语义。与其他层重复时，移动到唯一 owner 并保留必要链接。

## Promotion / Demotion

候选内容只有在被采用并与源码/合同对齐后才能晋升为当前权威；过期内容应降级为 source/report 或删除。

## Read Next

- [product-language.md](product-language.md)
- [authority-map.md](authority-map.md)
- [../standards/README.md](../standards/README.md)

## Authority Resolution

权威按 claim 类型解析，而不是使用一条无条件文件排序：

```text
host instructions and repository AGENTS.md
  -> adopted project authority for the claim
     current facts -> docs/ssot/**
     executable rules -> docs/standards/**
     accepted tradeoffs -> docs/adr/**
     wire compatibility -> project protocol/schema contract
  -> executable reality for implementation claims
     source, lockfiles, tests, command evidence
  -> unadopted Preset source/candidate
  -> specialist doctrine and router recommendation
```

已采用的 Preset 输出归入对应项目 docs layer，不是第二套 Preset authority。
项目 authority 与 executable reality 冲突时，记录 stale-doc 或 implementation-drift，
不能静默选择一方。
