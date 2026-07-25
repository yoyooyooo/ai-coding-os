# Fact Authority Map Candidate

本文件是技术 fact writer 与 consistency boundary 的架构候选，不是全局 Authority Map；架构 owner 采纳前不得视为当前规则。

| Fact | Authority module | Writer host | Allowed entry | Forbidden path | Transaction / consistency |
| --- | --- | --- | --- | --- | --- |
| Order.status | Orders | apps/api | order.*.use-case.ts | apps/worker direct DB write | order consistency domain |
| PaymentAttempt.status | Billing | apps/api | payment-attempt.materialize.use-case.ts | provider webhook direct table update | payment-attempt consistency domain |
| UI checkout draft | Web checkout feature | apps/web | checkout.store.ts | backend projection cache | tab-local interaction lifetime |
