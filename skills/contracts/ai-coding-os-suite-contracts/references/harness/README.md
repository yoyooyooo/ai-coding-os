# AI Coding OS Harness Contracts

这些轻量合同让 Harness 可发现、让结果可解释，同时不引入中央验证流程。

- **Harness Descriptor**：说明可运行入口、可观察内容和覆盖边界。
- **Harness Result**：记录 observations、受支持的有界结论和相邻 `not_proven`。

跨提交复用、CI、发布或审计场景可附加 provenance；普通本地验证使用与 claim
匹配的最小结果即可。

## Examples

- `examples/order-checkout-retry.descriptor.yaml`
- `examples/order-checkout-retry.result.yaml`

Suite audit 会用共享 schema 校验这些示例。
