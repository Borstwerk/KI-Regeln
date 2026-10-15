"""Synthetic negative controls for the light public-entrypoint checks."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.check_public_entrypoints import ROOT, local_targets, validate_entries


class EntryPointTests(unittest.TestCase):
    def test_current_public_docs_have_usable_navigation(self):
        self.assertEqual(validate_entries(ROOT), [])

    def test_missing_local_link_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Example", encoding="utf-8")
            _, errors = local_targets(root, "README.md", "[Missing](not-here.md)")
            self.assertTrue(any("missing link target" in x for x in errors))

    def test_repo_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            root.mkdir()
            (root / "README.md").write_text("# Example", encoding="utf-8")
            _, errors = local_targets(root, "README.md", "[Oops](../../outside.md)")
            self.assertTrue(any("leaves repository" in x for x in errors))

    def test_external_https_link_is_not_mistaken_for_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Example", encoding="utf-8")
            targets, errors = local_targets(root, "README.md",
                                            "[Site](https://example.org/docs)")
            self.assertEqual(targets, set())
            self.assertEqual(errors, [])

    def test_local_fragment_link_resolves_to_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Example", encoding="utf-8")
            (root / "START-HERE.md").write_text("# Here", encoding="utf-8")
            targets, errors = local_targets(root, "README.md",
                                            "[Guide](START-HERE.md#examples)")
            self.assertEqual(targets, {"START-HERE.md"})
            self.assertEqual(errors, [])

    def test_missing_english_navigation_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for doc in ("README.md", "START-HIER.md", "START-HERE.md", "AGENTS.md",
                        "Dokumentation/Public-Entrypoints-und-Sprachpflege.md"):
                path = root / doc
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Example\n", encoding="utf-8")
            issues = validate_entries(root)
            self.assertTrue(any("README.md: required navigation link absent: START-HERE.md"
                                in issue for issue in issues))

    def test_unknown_scheme_must_not_escape_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Example", encoding="utf-8")
            _, errors = local_targets(root, "README.md", "[Unsafe](file:///etc/passwd)")
            self.assertTrue(any("unsupported URL scheme" in x for x in errors))

    def test_readme_length_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# " + "a" * 9000, encoding="utf-8")
            issues = validate_entries(root)
            self.assertTrue(any("above 8500 bytes" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
