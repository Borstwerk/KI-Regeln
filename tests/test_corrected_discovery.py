"""Offline guards for the one fixed discovery case; never starts Codex."""
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('corrected_discovery', ROOT / 'Evals/Onboarding/run_corrected_discovery.py')
case = importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)


class CorrectedDiscoveryTests(unittest.TestCase):
    def test_exact_gate_rejects_whitespace_changes_and_same_length_corruption(self):
        source = b'X\x00\n\r\n\xc3\xa4\xff\n'
        self.assertTrue(case.exact_bytes(source, source))
        for changed in (source + b'\n', source + b'\r\n', source.rstrip(), source.replace(b'\n', b' '), b'Y' + source[1:]):
            with self.subTest(changed=changed):
                self.assertFalse(case.exact_bytes(changed, source))
        with self.assertRaises(TypeError):
            case.exact_bytes('X', b'X')

    def test_historical_bad_canary_stays_rejected(self):
        old = json.loads((ROOT / 'Evals/Onboarding/Discovery-Read-Followup-2026-10-29.json').read_text(encoding='utf-8'))
        source = (old['canary']['content'] + '\n').encode('utf-8')
        answer = old['sessions'][0]['response']['answer'].encode('utf-8')
        self.assertFalse(case.exact_bytes(answer, source))
        self.assertEqual(old['summary']['strict_byte_gate'], 'FAIL')

    def test_actual_registered_descriptors_and_missing_source_controls(self):
        files = {n: (ROOT / n).read_text(encoding='utf-8').encode('utf-8')
                 for n in ('skill-catalog.yml', 'routing-overlays.yml')}
        catalog = case.yaml.safe_load(files['skill-catalog.yml'])
        paths = {s['id']: s['path'] for s in catalog['skills']}
        for overlay in case.yaml.safe_load(files['routing-overlays.yml'])['overlays']:
            path = paths[overlay['skill']]
            files[path] = (ROOT / path).read_text(encoding='utf-8').encode('utf-8')
        self.assertEqual(len(case.check_overlays(files)), 6)
        for missing in case.EXTRA:
            broken = dict(files)
            del broken[missing]
            with self.assertRaisesRegex(ValueError, 'Missing canonical descriptor: ' + missing):
                case.check_overlays(broken)
        invalid = dict(files)
        invalid[case.EXTRA[0]] = b'---\nname: wrong-owner\ndescription: Present but wrong\n---\n'
        with self.assertRaisesRegex(ValueError, 'Invalid canonical descriptor'):
            case.check_overlays(invalid)

    def test_write_denial_is_bound_to_started_attempt_and_exact_target(self):
        target = ROOT / 'synthetic-denied.txt'
        event = {'stage': 'target_write', 'outcome': 'permission_denied', 'target': str(target),
                 'error_type': 'System.UnauthorizedAccessException'}
        self.assertTrue(case.denied_target_write(17, event, target, False))
        for code, changed, exists in ((1, None, False), (17, dict(event, stage='setup'), False),
                                      (17, dict(event, target=str(ROOT / 'unrelated-state')), False),
                                      (17, dict(event, error_type='System.IO.IOException'), False),
                                      (17, event, True)):
            self.assertFalse(case.denied_target_write(code, changed, target, exists))

    def test_failure_metadata_distinguishes_auth_config_transport_and_redacts(self):
        self.assertEqual(case.failure_diagnostic('', '401 Unauthorized')['category'], 'AUTH')
        self.assertEqual(case.failure_diagnostic('', 'config error in TOML')['category'], 'CONFIG')
        self.assertEqual(case.failure_diagnostic('', 'TLS connection failed')['category'], 'TRANSPORT')
        detail = case.failure_diagnostic('', '401 Unauthorized C:\\Users\\Example\\cache Bearer synthetic-token sk-synthetic-secret')
        self.assertNotIn('synthetic-token', detail['stderr_excerpt'])
        self.assertNotIn('sk-synthetic-secret', detail['stderr_excerpt'])
        self.assertNotIn('Example', detail['stderr_excerpt'])
        for prefix in ('Bearer ', 'sk-'):
            secret = 'synthetic' * 150
            detail = case.failure_diagnostic('', '401 ' + prefix + secret)
            self.assertNotIn('synthetic', detail['stderr_excerpt'])
            self.assertIn('<credential-redacted>', detail['stderr_excerpt'])

    def test_remaining_questions_use_separate_prompts_without_judge_hints(self):
        base = json.loads((ROOT / 'Evals/Onboarding/Discovery-Corrected-2026-10-29.json').read_text(encoding='utf-8'))['protocol']['prompt']
        cases = case.remaining_cases(base)
        self.assertEqual([c['questions'] for c in cases], [['D2', 'D4', 'D6'], ['D7'], ['D8']])
        for control in cases[1:]:
            self.assertNotIn('Beginne mit AGENTS.md', control['prompt'])
            self.assertNotIn('tool-permission-review', control['prompt'])
            self.assertNotIn('Keine Tools', control['prompt'])
        self.assertNotIn('Zugriffe', cases[2]['prompt'])

    def test_limit_diagnostic_keeps_structured_failure_separate_from_prewarm_warning(self):
        self.assertEqual(case.failure_diagnostic('', 'You have hit your usage limit')['category'], 'RATE_LIMIT')
        stdout = json.dumps({'type': 'turn.failed', 'error': {'message': '401 Unauthorized'}})
        detail = case.failure_diagnostic(stdout, 'Prewarm failed: usage limit')
        self.assertEqual(detail['category'], 'AUTH')
        self.assertEqual(detail['stderr_category'], 'RATE_LIMIT')
        self.assertEqual(detail['stdout_error_count'], 1)
        stdout = json.dumps({'type': 'error', 'message': '429 UsageLimitExceeded Bearer ' + 'synthetic'*150})
        detail = case.failure_diagnostic(stdout, '')
        self.assertEqual(detail['category'], 'RATE_LIMIT')
        self.assertNotIn('synthetic', detail['stdout_error_excerpt'])
        self.assertIn('<credential-redacted>', detail['stdout_error_excerpt'])

    def test_each_case_starts_fresh_workspace_without_previous_artifacts(self):
        workspaces = []
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            def start(argv, **kwargs):
                workspace = Path(argv[argv.index('--cd') + 1])
                workspaces.append(str(workspace))
                self.assertEqual((workspace / 'AGENTS.md').read_text(encoding='utf-8'), '# Synthetic bootstrap')
                self.assertFalse((workspace / 'prior-session.txt').exists())
                (workspace / 'prior-session.txt').write_text('must not reach next session', encoding='utf-8')
                target = Path(argv[argv.index('--output-last-message') + 1])
                def communicate(prompt, timeout):
                    target.write_text(json.dumps({'answer': 'offline control'}), encoding='utf-8')
                    return json.dumps({'type': 'item.completed', 'item': {'type': 'agent_message'}}), ''
                return SimpleNamespace(returncode=0, communicate=communicate)
            with mock.patch.object(case.subprocess, 'Popen', side_effect=start):
                for item in case.remaining_cases('Header\n\n1. old'):
                    case.run_one('synthetic-cli', {}, {'AGENTS.md': b'# Synthetic bootstrap'},
                                 item['prompt'], out, prefix=item['id']+'-', deadline=item['deadline'])
        self.assertEqual(len(set(workspaces)), 3)


if __name__ == '__main__':
    unittest.main()
