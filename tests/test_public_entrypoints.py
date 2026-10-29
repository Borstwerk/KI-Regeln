"""Synthetic negative controls for the light public-entrypoint checks."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.check_public_entrypoints import ROOT, PROJECT_CORE, local_targets, validate_entries, validate_project_manifest


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


class ProjectSearchTests(unittest.TestCase):
    """Source selection controls, not retrieval-quality or runtime-isolation tests."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in PROJECT_CORE:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Synthetic source\n", encoding="utf-8")
        self.data = {
            "schema_version": 1, "id": "ki-regeln", "kind": "collection",
            "entrypoints": {"overview": "PROJECT.md", "contents": "START-HIER.md",
                            "status": "README.md", "plan": "CONTRIBUTING.md"},
            "search": {"include": sorted(PROJECT_CORE), "exclude": []},
        }

    def check_manifest(self):
        (self.root / "mara-project.json").write_text(json.dumps(self.data), encoding="utf-8")
        return validate_project_manifest(self.root)

    def test_current_project_selection(self):
        errors, metrics = validate_project_manifest(ROOT)
        self.assertEqual(errors, [])
        self.assertGreater(metrics["documents"], 4)
        self.assertLessEqual(metrics["utf8_bytes"], 1024 * 1024)

    def test_synthetic_good_selection(self):
        errors, metrics = self.check_manifest()
        self.assertEqual(errors, [])
        self.assertEqual(metrics["documents"], len(PROJECT_CORE))

    def test_missing_source_and_missing_core_are_reported(self):
        (self.root / "README.md").unlink()
        self.data["search"]["include"].remove("AGENTS.md")
        errors, _ = self.check_manifest()
        self.assertTrue(any("missing or escaping file: README.md" in e for e in errors))
        self.assertTrue(any("required pilot entry absent: AGENTS.md" in e for e in errors))

    def test_unsafe_paths_non_markdown_and_globs_are_reported(self):
        for value in ("../outside.md", "/outside.md", "C:/outside.md", "docs\\x.md",
                      ".validation/report.md", "skill-catalog.yml", "**/*.md", "docs//x.md"):
            with self.subTest(value=value):
                self.data["search"]["include"] = sorted(PROJECT_CORE) + [value]
                errors, _ = self.check_manifest()
                self.assertTrue(any("expected explicit safe Markdown file" in e for e in errors))

    def test_excluded_eval_and_raw_sources_are_reported(self):
        for name in ("Evals/gold.md", "archive/old.md", "raw/source.md", "docs/other.md"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Not selected", encoding="utf-8")
        self.data["search"]["include"] += ["Evals/gold.md", "archive/old.md", "raw/source.md", "docs/other.md"]
        self.data["search"]["exclude"] = ["docs/**"]
        errors, _ = self.check_manifest()
        self.assertEqual(sum("excluded source selected" in e for e in errors), 4)

    def test_duplicates_are_case_insensitive(self):
        self.data["search"]["include"] += ["README.md"]
        errors, _ = self.check_manifest()
        self.assertTrue(any("duplicate file: README.md" in e for e in errors))

    def test_root_source_register_needs_explicit_root_exclude(self):
        # Keep fnmatch semantics aligned with the consumer: **/ needs a slash.
        name = "Quellen-und-Inspirationen.md"
        (self.root / name).write_text("# External source register", encoding="utf-8")
        self.data["search"]["include"].append(name)
        self.data["search"]["exclude"] = [name, "**/Quellen-und-Inspirationen.md"]
        errors, _ = self.check_manifest()
        self.assertTrue(any("excluded source selected: " + name in e for e in errors))

    def test_size_limits_detect_relevant_breakage(self):
        for index in range(4):
            name = f"large-{index}.md"
            (self.root / name).write_bytes(b"x" * (256 * 1024 + 1))
            self.data["search"]["include"].append(name)
        errors, _ = self.check_manifest()
        self.assertEqual(sum("file above 256 KiB" in e for e in errors), 4)
        self.assertTrue(any("total above 1 MiB" in e for e in errors))

    def test_document_limit_detects_relevant_breakage(self):
        for index in range(201):
            name = f"small-{index}.md"
            (self.root / name).write_text("# Source", encoding="utf-8")
            self.data["search"]["include"].append(name)
        errors, _ = self.check_manifest()
        self.assertTrue(any("more than 200 documents" in e for e in errors))

    def test_bad_shape_and_unsafe_excludes_are_reported(self):
        self.data["search"]["exclude"] = ["../**"]
        errors, _ = self.check_manifest()
        self.assertTrue(any("unsafe exclude pattern" in e for e in errors))
        self.data["search"] = []
        errors, _ = self.check_manifest()
        self.assertTrue(any("must be lists" in e for e in errors))

    def test_non_utf8_source_is_reported(self):
        (self.root / "README.md").write_bytes(b"\xff\xfe\x80")
        errors, _ = self.check_manifest()
        self.assertTrue(any("unreadable UTF-8: README.md" in e for e in errors))

    def test_symlink_is_rejected_when_supported(self):
        source = self.root / "real.md"
        source.write_text("# Source", encoding="utf-8")
        link = self.root / "linked.md"
        try:
            link.symlink_to(source)
        except OSError as error:
            self.skipTest(f"OS does not allow symlinks: {type(error).__name__}")
        self.data["search"]["include"].append("linked.md")
        errors, _ = self.check_manifest()
        self.assertTrue(any("symlink/junction not allowed: linked.md" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
