# Repository Topology Candidate

本文件是基于 overlay 的拓扑候选；架构 owner 采纳前不证明当前实际拓扑，也不重新定义标准。

## Deployables

- `apps/web` — 浏览器产品 host
- `apps/api` — accepted business facts 的主要 writer host
- `apps/worker` — reconciliation 与异步工作 host；通过公开 command 写入

## Packages

- `packages/contracts` — wire schemas 与生成合同
- `packages/testkit` — 业务中立测试原语

## Authority Modules

- `apps/api/src/modules/orders` — Order authority cell
- `apps/api/src/modules/billing` — PaymentAttempt authority cell

## Workflows

- `apps/api/src/workflows/checkout` — 跨 Orders/Billing 的应用编排，不拥有两者事实
- `apps/worker/src/workflows/payment-reconciliation` — 处理 provider observation 并发出正式 materialization command

## Boundary Notes

- Checkout 是 workflow，不是 authority module。
- Worker 可以发出 Orders/Billing command，但不能直接写 authority tables。
- packages/contracts 是 wire compatibility boundary，不是共享 domain authority。
