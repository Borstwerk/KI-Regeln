"""Controller contracts with real Git/filesystem boundaries and a fake QMD worker.

These tests do not install QMD or establish retrieval quality or engine behavior.
Git mutations are confined to disposable repositories under .validation/tmp.
"""
from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import search_rules
from tools.check_public_entrypoints import PROJECT_CORE, ROOT, validate_project_manifest


@unittest.skipUnless(shutil.which("git"), "Git is required for the controller integration tests")
class RuleSearchTests(unittest.TestCase):
    def setUp(self):
        tmp_parent = ROOT / ".validation" / "tmp"
        tmp_parent.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix="rule-search-test-", dir=tmp_parent)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git_env = {
            **{key: value for key, value in os.environ.items() if not key.startswith("GIT_")},
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
        }
        git_environment = patch.dict(os.environ, self.git_env, clear=True)
        git_environment.start()
        self.addCleanup(git_environment.stop)
        self.git("init", "--quiet", "--object-format=sha1")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "user.name", "Rule Search Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.selected = {
            name: (f"# Fixture {name}\n\nCanonical rule text.\n").encode("utf-8")
            for name in sorted(PROJECT_CORE | {"docs/extra.md"})
        }
        for name, body in self.selected.items():
            self.write(name, body)
        self.manifest = {
            "schema_version": 1,
            "id": "ki-regeln",
            "kind": "collection",
            "entrypoints": {
                "overview": "PROJECT.md", "contents": "START-HIER.md",
                "status": "README.md", "plan": "CONTRIBUTING.md",
            },
            "search": {"include": sorted(self.selected), "exclude": []},
        }
        self.write_manifest()
        self.write(".gitignore", b".validation/\nignored/\n.env\n")
        self.write("Evals/tracked.md", b"# PRIVATE_FIXTURE_CANARY_DO_NOT_EXPORT\n")
        self.commit("initial fixture")
        self.head = self.git("rev-parse", "HEAD").decode().strip()
        self.requests = []

    def git(self, *args, data=None):
        result = subprocess.run(
            ["git", *args], cwd=self.root, env=self.git_env, input=data,
            capture_output=True, check=False, timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode(errors="replace"))
        return result.stdout

    def write(self, name, body):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)

    def write_manifest(self):
        self.write("mara-project.json", json.dumps(self.manifest).encode("utf-8"))

    def commit(self, message):
        self.git("add", "--all")
        self.git("commit", "--quiet", "--message", message)

    def change_source(self, *, commit=False):
        name = "docs/extra.md"
        self.selected[name] = b"# Changed rule\nNew committed or working-tree content.\n"
        self.write(name, self.selected[name])
        if commit:
            self.commit("change selected rule")

    def good_worker(self, node, request):
        """Inspect the actual export, then imitate only the documented seam."""
        self.assertEqual(node, "fixture-node")
        self.requests.append(dict(request))
        self.assertIn(request["action"], ("build", "search"))
        self.assertEqual(request["paths"], sorted(self.selected))
        corpus = Path(request["corpus"])
        exported = {
            path.relative_to(corpus).as_posix(): path.read_bytes()
            for path in corpus.rglob("*") if path.is_file()
        }
        self.assertEqual(exported, self.selected)
        db = Path(request["db"])
        self.assertTrue(db.resolve().is_relative_to(
            (self.root / ".validation" / "rule-search").resolve()))
        if request["action"] == "build":
            db.parent.mkdir(parents=True, exist_ok=True)
            db.touch()
            return {"paths": sorted(exported), "skipped": 0}
        name = "docs/extra.md"
        return {"hits": [{
            "path": name, "score": 0.8, "snippet": "Canonical rule text.",
            "content_sha256": hashlib.sha256(exported[name]).hexdigest(),
        }]}

    def build(self, worker=None):
        return search_rules.build(
            self.root, node="fixture-node", worker=worker or self.good_worker)

    def search(self, query="rule", worker=None):
        return search_rules.search(
            self.root, query, node="fixture-node", worker=worker or self.good_worker)

    def assert_rejected(self, action):
        with self.assertRaises(search_rules.SearchError) as raised:
            action()
        self.assertIsInstance(raised.exception.status, str)
        self.assertTrue(raised.exception.status)
        return raised.exception

    def assert_not_ready(self):
        result = search_rules.status(self.root)
        self.assertIsInstance(result, dict)
        self.assertIn(result["status"], {"missing", "stale", "busy", "error"})

    def test_valid_fixture_and_snapshot_hashes_are_bound_to_full_head(self):
        self.assertEqual(validate_project_manifest(self.root)[0], [])
        metadata, files = search_rules.read_snapshot(self.root)
        self.assertEqual(metadata["revision"], self.head)
        self.assertEqual(files, self.selected)
        self.assertEqual(metadata["files"], {
            name: hashlib.sha256(body).hexdigest() for name, body in self.selected.items()
        })
        self.assertRegex(metadata["fingerprint"], r"\A[0-9a-f]{64}\Z")
        self.assertEqual(search_rules.read_snapshot(self.root)[0], metadata)

    def test_snapshot_uses_head_blobs_even_when_clean_checkout_has_crlf(self):
        self.git("config", "core.autocrlf", "true")
        for name, body in self.selected.items():
            self.write(name, body.replace(b"\n", b"\r\n"))
        self.git("diff", "--quiet")
        _, files = search_rules.read_snapshot(self.root)
        self.assertEqual(files, self.selected)
        self.assertNotEqual((self.root / "README.md").read_bytes(), files["README.md"])

    def test_archive_export_substitution_is_rejected_as_noncanonical_source(self):
        self.write("docs/extra.md", b"# Export substitution fixture\n$Format:%H$\n")
        self.write(".gitattributes", b"docs/extra.md export-subst\n")
        self.commit("enable archive content substitution")
        self.assert_rejected(lambda: search_rules.read_snapshot(self.root, revision="HEAD"))

    def test_explicit_revision_exports_old_blobs_after_head_and_worktree_change(self):
        before, old_files = search_rules.read_snapshot(self.root, revision=self.head)
        self.change_source(commit=True)
        self.write("README.md", b"# Additional uncommitted change\n")
        after, files = search_rules.read_snapshot(self.root, revision=self.head)
        self.assertEqual(after, before)
        self.assertEqual(files, old_files)

    def test_dirty_selected_source_blocks_before_worker(self):
        self.write("README.md", b"# Uncommitted rule\n")
        self.assert_rejected(lambda: search_rules.read_snapshot(self.root))
        self.assert_rejected(self.build)
        self.assertEqual(self.requests, [])

    def test_missing_index_does_not_implicitly_invoke_worker(self):
        self.assertEqual(search_rules.status(self.root)["status"], "missing")
        self.assert_rejected(self.search)
        self.assertEqual(self.requests, [])

    def test_worker_corpus_excludes_tracked_evals_ignored_and_untracked_secrets(self):
        for name in ("Evals/untracked.md", "ignored/private.md", ".env", "untracked.md"):
            self.write(name, b"PRIVATE_FIXTURE_CANARY_DO_NOT_EXPORT\n")
        self.assertIsInstance(self.build(), dict)
        self.assertEqual(search_rules.status(self.root)["status"], "ready")
        result = self.search()
        self.assertEqual(result["hits"][0]["path"], "docs/extra.md")
        self.assertEqual([request["action"] for request in self.requests], ["build", "search"])

    def test_manifest_is_validated_against_head_materialization(self):
        self.write("Status.md", b"# Committed entrypoint, not a search document\n")
        self.manifest["entrypoints"]["status"] = "Status.md"
        self.write_manifest()
        self.commit("add nonselected entrypoint")
        revision = self.git("rev-parse", "HEAD").decode().strip()
        (self.root / "Status.md").unlink()
        _, files = search_rules.read_snapshot(self.root, revision=revision)
        self.assertEqual(files, self.selected)

    def test_missing_committed_selected_file_blocks_before_worker(self):
        (self.root / "README.md").unlink()
        self.commit("remove required document without fixing manifest")
        self.assert_rejected(self.build)
        self.assertEqual(self.requests, [])

    def test_git_symlink_mode_is_rejected_without_os_symlink_privileges(self):
        name = "docs/link.md"
        self.write(name, b"README.md")
        self.manifest["search"]["include"].append(name)
        self.write_manifest()
        self.git("add", "--all")
        blob = self.git("hash-object", "-w", "--stdin", data=b"README.md").decode().strip()
        self.git("update-index", "--add", "--cacheinfo", f"120000,{blob},{name}")
        self.git("commit", "--quiet", "--message", "commit symlink mode")
        revision = self.git("rev-parse", "HEAD").decode().strip()
        self.assert_rejected(lambda: search_rules.read_snapshot(self.root, revision=revision))
        self.assert_rejected(self.build)
        self.assertEqual(self.requests, [])

    def test_partial_skipped_extra_and_duplicate_active_paths_cannot_be_ready(self):
        expected = sorted(self.selected)
        for report in (
            {"paths": expected[:-1], "skipped": 0},
            {"paths": expected, "skipped": 1},
            {"paths": expected + ["Evals/tracked.md"], "skipped": 0},
            {"paths": expected + [expected[0]], "skipped": 0},
        ):
            with self.subTest(report=report):
                def worker(node, request):
                    self.good_worker(node, request)
                    return report
                self.assert_rejected(lambda: self.build(worker))
                self.assert_not_ready()
                calls = len(self.requests)
                self.assert_rejected(self.search)
                self.assertEqual(len(self.requests), calls)

    def test_committed_source_change_invalidates_previous_hits_before_worker(self):
        self.build()
        before, _ = search_rules.read_snapshot(self.root)
        self.change_source(commit=True)
        after, _ = search_rules.read_snapshot(self.root)
        self.assertNotEqual(before["fingerprint"], after["fingerprint"])
        self.assertEqual(search_rules.status(self.root)["status"], "stale")
        self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), 1)

    def test_uncommitted_selected_change_invalidates_previous_hits_before_worker(self):
        self.build()
        self.change_source()
        self.assert_not_ready()
        self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), 1)

    def test_manifest_withdrawal_never_returns_an_old_selected_hit(self):
        self.build()
        self.manifest["search"]["include"].remove("docs/extra.md")
        self.write_manifest()
        self.commit("withdraw source from search")
        self.assertEqual(search_rules.status(self.root)["status"], "stale")
        self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), 1)

    def test_dirty_manifest_is_not_silently_replaced_by_committed_selection(self):
        self.build()
        self.manifest["search"]["include"].remove("docs/extra.md")
        self.write_manifest()
        self.assert_not_ready()
        self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), 1)

    def test_failed_rebuild_revokes_previously_ready_index(self):
        self.build()
        def fail(node, request):
            self.good_worker(node, request)
            raise RuntimeError("controlled worker failure")
        self.assert_rejected(lambda: self.build(fail))
        self.assert_not_ready()
        calls = len(self.requests)
        self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), calls)

    def test_search_rejects_unselected_escaping_and_wrong_hash_hits(self):
        for path, digest in (
            ("Evals/tracked.md", "0" * 64),
            ("../outside.md", "0" * 64),
            ("C:/outside.md", "0" * 64),
            ("docs/extra.md", "0" * 64),
        ):
            with self.subTest(path=path):
                self.build()
                def worker(node, request):
                    result = self.good_worker(node, request)
                    result["hits"][0].update(path=path, content_sha256=digest)
                    return result
                self.assert_rejected(lambda: self.search(worker=worker))

    def test_redirected_database_is_rejected_before_worker(self):
        self.build()
        self.search()
        calls = len(self.requests)
        db = Path(self.requests[-1]["db"])
        original = db.read_bytes()
        redirected = self.root / "outside-cache.sqlite"
        redirected.write_bytes(b"Synthetic database outside the index cache")
        db.unlink()
        try:
            db.symlink_to(redirected)
        except (OSError, NotImplementedError):
            # A missing DB would be a different failure: restore it before
            # simulating only this path's OS redirect classification.
            db.write_bytes(original)
            is_symlink = Path.is_symlink
            def classify(path):
                return path == db or is_symlink(path)
            with patch.object(Path, "is_symlink", classify):
                self.assert_rejected(self.search)
        else:
            self.assertTrue(db.is_symlink())
            self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), calls)

    def test_source_commit_during_build_prevents_ready_publication(self):
        def worker(node, request):
            result = self.good_worker(node, request)
            self.change_source(commit=True)
            return result
        self.assert_rejected(lambda: self.build(worker))
        self.assert_not_ready()
        self.assert_rejected(self.search)
        self.assertEqual(len(self.requests), 1)

    def test_source_edit_during_search_discards_otherwise_valid_hits(self):
        self.build()
        def worker(node, request):
            result = self.good_worker(node, request)
            self.change_source()
            return result
        self.assert_rejected(lambda: self.search(worker=worker))
        self.assert_not_ready()

    def test_exclusive_lock_reports_busy_for_reentrant_build_and_search(self):
        def worker(node, request):
            self.assertEqual(search_rules.status(self.root)["status"], "busy")
            for action in (self.build, self.search):
                error = self.assert_rejected(action)
                self.assertEqual(error.status, "busy")
            return self.good_worker(node, request)
        self.build(worker)
        self.assertEqual(search_rules.status(self.root)["status"], "ready")
        self.assertEqual(len(self.requests), 1)

    def test_query_length_500_is_accepted_and_501_rejected(self):
        self.build()
        self.assertEqual(self.search("x" * 500)["hits"][0]["path"], "docs/extra.md")
        self.assertEqual(self.requests[-1]["query"], "x" * 500)
        calls = len(self.requests)
        self.assert_rejected(lambda: self.search("x" * 501))
        self.assertEqual(len(self.requests), calls)

    def test_empty_whitespace_and_control_queries_block_before_worker(self):
        self.build()
        calls = len(self.requests)
        for query in ("", "   ", "\x00", "a\nb", "a\rb", "a\tb", "a\x1fb", "a\x7fb"):
            with self.subTest(query=repr(query)):
                self.assert_rejected(lambda: self.search(query))
        self.assertEqual(len(self.requests), calls)


class RuleSearchRuntimeTests(unittest.TestCase):
    """Resolve existing paths only; fixture files are never executed."""

    def setUp(self):
        tmp_parent = ROOT / ".validation" / "tmp"
        tmp_parent.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix="rule-runtime-test-", dir=tmp_parent)
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name) / "home"
        self.home.mkdir()
        home = patch.object(Path, "home", return_value=self.home)
        home.start()
        self.addCleanup(home.stop)
        processes = patch.object(subprocess, "Popen", side_effect=AssertionError(
            "Runtime path resolution must not launch a process"))
        processes.start()
        self.addCleanup(processes.stop)

    def executable(self, directory):
        target = directory / ("node.exe" if os.name == "nt" else "node")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"Synthetic executable fixture; never run")
        target.chmod(0o755)
        return target.resolve()

    def bundled_node(self):
        return self.executable(self.home / ".cache" / "codex-runtimes" /
                               "codex-primary-runtime" / "dependencies" / "node" / "bin")

    def test_node_on_path_is_preferred_over_existing_bundled_runtime(self):
        self.bundled_node()
        expected = self.executable(Path(self.tmp.name) / "path-bin")
        with patch.dict(os.environ, {"PATH": str(expected.parent)}):
            resolved = search_rules.resolve_node()
        self.assertTrue(Path(resolved).is_absolute())
        self.assertEqual(Path(resolved), expected)

    def test_missing_path_node_uses_existing_bundled_runtime(self):
        expected = self.bundled_node()
        with patch.object(shutil, "which", return_value=None):
            resolved = search_rules.resolve_node()
        self.assertTrue(Path(resolved).is_absolute())
        self.assertEqual(Path(resolved), expected)

    def test_missing_explicit_node_is_never_replaced_by_available_bundle(self):
        self.bundled_node()
        missing = str(Path(self.tmp.name) / "missing-node.exe")
        with patch.object(shutil, "which", return_value=None):
            with self.assertRaises(search_rules.SearchError) as raised:
                search_rules.resolve_node(explicit=missing)
        self.assertEqual(raised.exception.status, "runtime-missing")
        self.assertTrue(str(raised.exception))

    def test_no_path_or_bundled_node_reports_runtime_missing(self):
        with patch.object(shutil, "which", return_value=None):
            with self.assertRaises(search_rules.SearchError) as raised:
                search_rules.resolve_node()
        self.assertEqual(raised.exception.status, "runtime-missing")
        self.assertTrue(str(raised.exception))

    def test_empty_explicit_node_does_not_select_available_path_or_bundle(self):
        bundled = self.bundled_node()
        with patch.object(shutil, "which", return_value=str(bundled)) as which:
            with self.assertRaises(search_rules.SearchError) as raised:
                search_rules.resolve_node(explicit="")
        self.assertEqual(raised.exception.status, "runtime-missing")
        which.assert_not_called()


class RuleSearchCliTests(unittest.TestCase):
    def test_leading_dash_query_is_forwarded_exactly_after_option_separator(self):
        with (
            patch("sys.argv", ["search_rules.py", "--node", "fixture-node", "search", "--", "-Quick"]),
            patch.object(search_rules, "search", return_value={"status": "ready", "hits": []}) as search,
            patch("sys.stdout", new_callable=io.StringIO) as output,
        ):
            exit_code = search_rules.main()
        self.assertEqual(exit_code, 0)
        search.assert_called_once_with(search_rules.ROOT, "-Quick", "fixture-node")
        self.assertEqual(json.loads(output.getvalue())["status"], "ready")


if __name__ == "__main__":
    unittest.main()
