# Product Harness

## Owns

- 稳定 Harness descriptor/scenario 引用、coverage 与 lifecycle

## Must Not Own

- 产品事实、可执行测试源码、原始日志、Goal progress

## Boundary / Conflict

仓库当前权威优先；本层只拥有上面列出的语义。与其他层重复时，移动到唯一 owner 并保留必要链接。

## Promotion / Demotion

候选内容只有在被采用并与源码/合同对齐后才能晋升为当前权威；过期内容应降级为 source/report 或删除。

## Read Next

- [coverage.yaml](coverage.yaml)
- [../standards/verification-policy.md](../standards/verification-policy.md)
