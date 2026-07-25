# Verification Policy Candidate

> Preset 候选：verification owner 采纳前不构成当前项目规则。

## Proposed Ownership

- 可发现的 Harness command/descriptor 约定。
- `surface_kind` 与 `dependency_reality` 的正交标识；纯静态证明使用 `[none]`。
- 必要时记录 `environment_class`、`proof_focus` 和 `claim_ceiling`。
- 结构化结果中的 `observed`、`supports`、`not_proven`。

## Must Not Own

- 产品事实或第二套业务算法。
- Agent 的固定修复循环、重试次数或模型角色。
- 原始运行日志的长期文档副本。

## Commands

项目命令以 `AGENTS.md` 和 `package.json` 为准。推荐提供 `verify:list`、`verify:affected` 与 `verify` 等可发现入口，但不要求统一工具。

## Claim Boundary

Harness 只支持实际 Proof Surface 对应的结论。Browser 不表示真实后端；fixture/fake/replay/local/external 依赖必须独立声明。
