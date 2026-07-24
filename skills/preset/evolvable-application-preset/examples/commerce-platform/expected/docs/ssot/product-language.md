# Product Language

本文件记录产品 canonical terms。它拥有产品词义，不拥有源码目录规则。

| Canonical term | Meaning | Kind | Not the same as |
| --- | --- | --- | --- |
| Order | 已被系统接受的购买流程事实 | authority | Checkout draft |
| Checkout | 用户跨 Orders/Billing 完成购买的交互与应用流程 | workflow | authority module |
| PaymentAttempt | 一次具有稳定 identity 的 provider 支付尝试 | authority | database transaction |
