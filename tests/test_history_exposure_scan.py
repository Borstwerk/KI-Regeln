from __future__ import annotations

import subprocess
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

from tools import history_exposure_scan as scan


class HistoryExposureScanTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        init = subprocess.run(
            ["git", "init", "--quiet"],
            cwd=self.root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if init.returncode:
            self.fail(f"git init failed: {init.stderr}")

        blob = subprocess.run(
            ["git", "hash-object", "-w", "--stdin"],
            cwd=self.root,
            text=True,
            input="history-exposure-regression\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if blob.returncode:
            self.fail(f"git hash-object failed: {blob.stderr}")
        self.blob_id = blob.stdout.strip()

    def tearDown(self):
        self.tmp.cleanup()

    def test_large_batch_terminates_and_counts_blobs(self):
        # 20k requests produce substantially more data than typical pipe buffers
        # in both directions. The old write-all-then-read Popen pattern can deadlock
        # here; subprocess.run(..., input=...) communicates concurrently.
        object_count = 20_000
        simulated_rev_list = "".join(f"{self.blob_id} path-{i}\n" for i in range(object_count))

        with mock.patch.object(scan, "ROOT", self.root), mock.patch.object(
            scan, "run", return_value=simulated_rev_list
        ):
            started = time.monotonic()
            count = scan.unique_reachable_blob_count()
            elapsed = time.monotonic() - started

        self.assertEqual(count, object_count)
        self.assertLess(elapsed, 15.0, "large cat-file batch did not terminate promptly")

    def test_cat_file_failure_is_reported(self):
        failed = subprocess.CompletedProcess(
            args=["git", "cat-file"],
            returncode=2,
            stdout="",
            stderr="synthetic cat-file failure",
        )
        with mock.patch.object(scan, "run", return_value=f"{self.blob_id}\n"), mock.patch.object(
            scan.subprocess, "run", return_value=failed
        ):
            with self.assertRaisesRegex(SystemExit, "git cat-file failed: synthetic cat-file failure"):
                scan.unique_reachable_blob_count()

    def test_cat_file_timeout_is_bounded_and_reported(self):
        timeout = subprocess.TimeoutExpired(
            cmd=["git", "cat-file"],
            timeout=scan.CAT_FILE_TIMEOUT_SECONDS,
        )
        with mock.patch.object(scan, "run", return_value=f"{self.blob_id}\n"), mock.patch.object(
            scan.subprocess, "run", side_effect=timeout
        ):
            with self.assertRaisesRegex(
                SystemExit,
                rf"git cat-file timed out after {scan.CAT_FILE_TIMEOUT_SECONDS}s",
            ):
                scan.unique_reachable_blob_count()


if __name__ == "__main__":
    unittest.main()
