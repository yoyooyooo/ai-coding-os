# Config / Schema 进阶（高级进阶）

适用范围：当你希望把“配置与输入校验”从零散的 `process.env`/手写校验，提升为可演进、可测试、可诊断的基础设施。

目标：让配置与输入解码具备三件事：
- 可组合（模块化、可注入）
- 可定位（错误信息稳定、可映射为 `INVALID_ARGS`）
- 可演进（默认值/新增字段不破坏旧调用）

## 触发条件

- 配置项变多：不同环境（dev/ci/prod）差异明显，排障成本上升。
- 输入来源变多：CLI args、stdin JSON、HTTP body、DB 记录都需要统一 schema。
- 你开始需要：更好的错误信息、统一的默认值策略、敏感信息治理。

## A 类不变量（需求无关）

### A1) 配置读取必须集中，不要散落 `process.env`

- 业务代码/库代码禁止直接读 `process.env`。
- 在入口（main/runner）集中读取 Config，并通过 Service/Layer 注入给业务模块。

理由：
- 可测试（测试里替换配置）
- 可诊断（能打印最终解析配置）
- 可演进（改 env 名/默认值不会到处改）

### A2) Schema 是“边界契约”，不是“内部类型装饰”

- Schema 应服务于边界：CLI 输入、HTTP 输入、外部数据。
- 内部类型可以更自由，但边界必须用 Schema 统一校验/解码/错误映射。

### A3) 错误必须可映射为稳定 code

- Config/Schema 解码错误必须能映射到稳定错误码（通常是 `INVALID_ARGS` 或 `INVALID_PAYLOAD`）。
- human 模式可以给更长的提示；`--json` 必须保持单行 envelope（见 `references/cli-contract.md`）。

### A4) 禁止混用 Schema 实现

- 在同一项目里，Schema 体系必须统一（例如只用 `effect/Schema`）。
- 混用会导致类型与解码行为分裂，错误信息难以统一。

## B 类因子（工程模板，建议固化）

### B1) Config 的优先级与可观测性

固化：
- `flags > env > default`
- 提供 `config print`（或等价）输出最终解析配置
- 对路径配置统一支持 `~` 展开并 `normalize`

### B2) Config 的“最小泄漏原则”

固化：
- 只把上层真正需要的配置注入到对应模块（ISP）。
- 不要注入一个“全量 Config 对象”到所有地方（会让依赖膨胀、难以测试）。

### B3) Schema 解码作为可复用函数

固化建议：
- 把 `decode` 封装为 `decodeX(input): Effect<Decoded, DecodeError, never>` 之类的纯逻辑函数。
- 在边界层捕获 DecodeError 并映射为 `CliError`/HTTP 错误。

### B4) 默认值策略（向前兼容）

固化：
- 新增字段是否默认或可选取决于边界兼容策略；破坏性变更必须显式版本化或迁移。
- 默认值应在“边界解码层”处理，而不是散落在业务逻辑里。

## C 类情境因子（按需启用）

### C1) Secret 管理

触发条件：你开始接触 token/password/密钥文件。

建议：
- 把 secret 作为独立配置源；日志/错误信息必须 redact。
- 对 secret 的缺失给出明确 hint（但不要在 message 里回显 secret 值）。

### C2) Schema 的错误信息质量

触发条件：用户/调用方经常输入错，且排查成本高。

建议：
- 错误信息要“指向字段 + 期望 + 实际摘要”，但保持稳定可测试。
- 对常见错用补充 hint（例如 “use '-' to read stdin”）。

### C3) 多来源输入融合

触发条件：同一数据既可能来自 CLI JSON，也可能来自 HTTP JSON。

建议：
- 共享 Schema；边界差异仅在“来源读取层”（stdin/body/params）。
- 统一 envelope 与错误码，以便上游统一处理。

## 常见坑（建议加入“禁止模式”）

- 业务逻辑里到处 `process.env.X ?? ...`（不可测、不可诊断）。
- Schema 只用来生成类型，不参与运行时解码（输入永远不可信）。
- 把 decode 错误直接 stringify 输出（既不稳定也难懂）。
