# Architecture

## Owns

- 当前实际系统拓扑、运行视图与接受的 seam

## Must Not Own

- 强制标准、产品事实、未来候选

## Boundary / Conflict

仓库当前权威优先；本层只拥有上面列出的语义。与其他层重复时，移动到唯一 owner 并保留必要链接。

## Promotion / Demotion

候选内容只有在被采用并与源码/合同对齐后才能晋升为当前权威；过期内容应降级为 source/report 或删除。

## Read Next

- [repository-topology.md](repository-topology.md)
- [../ssot/README.md](../ssot/README.md)
- [../ssot/authority-map.md](../ssot/authority-map.md)
- [../standards/source-topology-and-naming.md](../standards/source-topology-and-naming.md)
