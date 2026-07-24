# Verification Policy

## Owns

- 可发现的 Harness command/descriptor 约定。
- fixture、fake、replay、real-local、real-external 的明确标识。
- 结构化结果中的 `observed`、`supports`、`not_proven`。

## Must Not Own

- 产品事实或第二套业务算法。
- Agent 的固定修复循环、重试次数或模型角色。
- 原始运行日志的长期文档副本。

## Commands

项目命令以 `AGENTS.md` 和 `package.json` 为准。推荐提供 `verify:list`、`verify:affected` 与 `verify` 等可发现入口，但不要求统一工具。

## Claim Boundary

Harness 只支持实际执行表面对应的结论。Fake、Replay、Headless、Browser 与 External Runtime 必须明确区分。
