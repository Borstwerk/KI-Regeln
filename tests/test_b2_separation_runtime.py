"""Run the opt-in runtime controls in a credential-free process, even with A20 enabled."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools.b2_auth_bootstrap import MINIMAL_ENV


class SeparatedRuntimeIntegrationTests(unittest.TestCase):
    def test_credential_free_separation_controls(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(root / 'tests/b2_separation_checks.py'), '-v'],
                                    env={**MINIMAL_ENV, 'HOME': tmp}, cwd=tmp, text=True,
                                    capture_output=True, timeout=120, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
