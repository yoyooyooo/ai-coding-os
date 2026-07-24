# Authority Map

本文件记录当前 accepted facts 与 writer 权威。未知项不得凭 Preset 推断。

| Fact | Authority module | Writer host | Allowed entry | Forbidden path | Transaction / consistency |
| --- | --- | --- | --- | --- | --- |
| Order.status | Orders | apps/api | order.*.use-case.ts | apps/worker direct DB write | order consistency domain |
| PaymentAttempt.status | Billing | apps/api | payment-attempt.materialize.use-case.ts | provider webhook direct table update | payment-attempt consistency domain |
| UI checkout draft | Web checkout feature | apps/web | checkout.store.ts | backend projection cache | tab-local interaction lifetime |
