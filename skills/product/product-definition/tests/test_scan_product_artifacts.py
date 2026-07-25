from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_product_artifacts.py"
SPEC = importlib.util.spec_from_file_location("scan_product_artifacts", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ProductArtifactScannerTests(unittest.TestCase):
    def write(self, root: Path, relative: str, content: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def codes(self, result) -> set[str]:
        return {finding.code for finding in result.findings}

    def test_duplicate_id_across_artifacts_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "a.md", "# PDR-CORE-001: First\n")
            self.write(root, "b.md", "# PDR-CORE-001: Second\n")
            result = MODULE.scan(root)
            self.assertIn("PD-ID-DUPLICATE", self.codes(result))

    def test_frontmatter_and_heading_in_same_artifact_are_one_definition(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(
                root,
                "pdr.md",
                "---\ndecision_id: PDR-CORE-001\nstatus: accepted\n---\n# PDR-CORE-001: Decision\n",
            )
            result = MODULE.scan(root)
            self.assertNotIn("PD-ID-DUPLICATE", self.codes(result))


    def test_simple_two_segment_id_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "decision.md", "# PDR-001: Decision\n")
            self.write(root, "prd.md", "This requirement follows @PDR-001.\n")
            result = MODULE.scan(root)
            self.assertNotIn("PD-REF-UNRESOLVED", self.codes(result))
            self.assertIn("PDR-001", result.definitions)

    def test_unresolved_explicit_reference_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "prd.md", "This requirement follows @PDR-CORE-404.\n")
            result = MODULE.scan(root)
            self.assertIn("PD-REF-UNRESOLVED", self.codes(result))

    def test_resolved_explicit_reference_is_clean(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "decision.md", "# PDR-CORE-001: Decision\n")
            self.write(root, "prd.md", "This requirement follows @PDR-CORE-001.\n")
            result = MODULE.scan(root)
            self.assertNotIn("PD-REF-UNRESOLVED", self.codes(result))

    def test_missing_local_markdown_link_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "index.md", "[Missing](other.md)\n")
            result = MODULE.scan(root)
            self.assertIn("PD-LINK-MISSING", self.codes(result))

    def test_accepted_placeholder_is_warning(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "accepted.md", "---\nstatus: accepted\n---\n# Ready\nTODO decide owner\n")
            result = MODULE.scan(root)
            findings = [f for f in result.findings if f.code == "PD-ACCEPTED-PLACEHOLDER"]
            self.assertEqual(1, len(findings))
            self.assertEqual("warning", findings[0].severity)

    def test_draft_placeholder_is_not_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, "draft.md", "---\nstatus: draft\n---\n# Draft\nTODO decide owner\n")
            result = MODULE.scan(root)
            self.assertNotIn("PD-ACCEPTED-PLACEHOLDER", self.codes(result))


if __name__ == "__main__":
    unittest.main()
