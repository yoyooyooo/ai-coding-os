# ADR: next-app-router-files

- Status: proposed
- Date: 2026-07-23

## Context

`apps/web/src/app/**` 可能需要偏离通用 Preset 默认。

## Proposed Decision

建议在该 scope 内采用例外：Next.js-controlled filenames

## Consequences If Adopted

- 例外只适用于声明的 scope。
- 非框架/工具强制代码仍遵循项目采纳后的 source standard。
- 例外失去必要性时应删除并更新架构检查。

## Revisit Conditions

当框架约束、route topology 或生成方式变化时重新评估。
