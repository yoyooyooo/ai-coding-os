# Documentation Router

## Owns

- 当前文档入口与层级路由

## Must Not Own

- 产品事实、架构标准或执行进度本身

## Boundary / Conflict

仓库当前权威优先；本层只拥有上面列出的语义。与其他层重复时，移动到唯一 owner 并保留必要链接。

## Promotion / Demotion

候选内容只有在被采用并与源码/合同对齐后才能晋升为当前权威；过期内容应降级为 source/report 或删除。

## 最短阅读路径 / 下一步阅读

- [product/README.md](product/README.md)
- [ssot/README.md](ssot/README.md)
- [standards/README.md](standards/README.md)
- [architecture/README.md](architecture/README.md)
- [adr/README.md](adr/README.md)
