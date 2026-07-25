# Tooling

本目录保存 Suite source 的可执行支持：

- `suite_audit.py`：离线校验 grouped source、frontmatter/cross-Skill reference closure、Schema 正反例、`$skill-name` handoff、bundle-local links、Preset profile provenance/language closure/golden、Docs Governance compatibility、bounded subprocess、Effect Kit project-bound P3/timeout/structured rollback 与 release provenance。TypeScript compiler 可用时额外运行 generated-template typecheck；缺失时明确降低 claim，不阻塞纯 Core audit。
- `build_suite_release.py`：使用 `skills/VERSION` 构建 self-contained Core ZIP，要求 audit `source_tree_sha256` 与待打包源码完全一致，并输出去除绝对路径和 compiler-dependent 状态的 canonical audit sidecar，使 ZIP、audit、manifest 和 change report 可跨机器复现。
- `effect-api-app-kit/`：从明确 Change Spec 生成 P0-P3 Effect API capability slice
  的实验性原子 scaffolder。

从完整仓库或 Core ZIP 解压根目录运行：

```bash
python3 -m pip install -r skills/requirements-audit.txt
python3 skills/tooling/suite_audit.py --suite skills --out audit.json
python3 skills/tooling/build_suite_release.py --repo . --audit audit.json --out-dir dist
```
