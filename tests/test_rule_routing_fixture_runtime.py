"""Fixture preparation guards; default tests never invoke Codex or a model."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
import uuid
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('routing_pilot', ROOT / 'Evals/Onboarding/run_rule_routing_p4.py')
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)


class FixtureRuntimeTests(unittest.TestCase):
    def ready_index(self):
        return {'status':'ready', 'mode':'bm25', 'documents':165,
                'revision':'a'*40, 'fingerprint':'b'*64}

    def ready_probe(self):
        return {'status':'ready', 'mode':'bm25', 'revision':'a'*40,
                'fingerprint':'b'*64, 'hits':[], 'total_matches':0}

    def test_real_python_import_keeps_sources_free_of_bytecode(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            control, fixed = folder/'control', folder/'fixed'
            control.mkdir(); fixed.mkdir()
            for target in (control, fixed):
                (target / 'fixture_module.py').write_bytes(b'VALUE = 17\n')
            before = dict(os.environ, PYTHONDONTWRITEBYTECODE='')
            before.pop('PYTHONPYCACHEPREFIX', None)
            child = [sys.executable, '-c',
                'import json,sys,fixture_module; print(json.dumps([fixture_module.VALUE,sys.dont_write_bytecode]))']
            bad = subprocess.run(child, cwd=control, env=before, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(bad.stdout), [17, False])
            self.assertTrue(list(control.rglob('*.pyc')))
            environment = pilot.fixture_environment(before)
            done = subprocess.run(child, cwd=fixed, env=environment, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(done.stdout), [17, True])
            self.assertEqual(list(fixed.rglob('*.pyc')), [])
            self.assertEqual(before['PYTHONDONTWRITEBYTECODE'], '')

    def test_sandbox_adapter_pins_profile_and_bytecode_policy(self):
        ready = SimpleNamespace(returncode=0, stdout='{"status":"ready"}', stderr='')
        for profile in (':workspace', ':read-only'):
            with self.subTest(profile=profile), patch.object(pilot.subprocess, 'run', return_value=ready) as run, \
                 patch.object(pilot, 'fixture_shell', return_value='fixture-pwsh', create=True):
                result = pilot.sandbox_json('fixture-cli', {'PYTHONDONTWRITEBYTECODE':'0'}, ROOT, profile, 'fixture-command')
                self.assertEqual(result, {'status':'ready'})
                argv = run.call_args.args[0]
                self.assertEqual(argv[argv.index('--permission-profile')+1], profile)
                self.assertIn(f'default_permissions="{profile}"', argv)
                self.assertIn('shell_environment_policy.set.PYTHONDONTWRITEBYTECODE="1"', argv)
                self.assertEqual(run.call_args.kwargs['env']['PYTHONDONTWRITEBYTECODE'], '1')
                self.assertNotIn('exec', argv)
                self.assertIn('fixture-pwsh', argv)
                self.assertNotIn('powershell.exe', argv)

    def test_preparation_uses_two_sandbox_processes_and_no_host_build(self):
        built, probe = self.ready_index(), self.ready_probe()
        with patch.object(pilot, 'sandbox_json', side_effect=[built, probe]) as native, \
             patch.object(pilot.search_rules, 'build', side_effect=AssertionError('Host build is forbidden')):
            self.assertEqual(pilot.prepare_index('fixture-cli', {}, ROOT, 'a'*40), {'build':built, 'probe':probe})
        self.assertEqual(native.call_count, 2)
        self.assertTrue(all(call.args[3] == ':workspace' for call in native.call_args_list))
        self.assertIn('-Build', native.call_args_list[0].args[4])
        self.assertIn('-Query', native.call_args_list[1].args[4])

    def test_preparation_rejects_partial_or_changed_probe(self):
        bad_pairs = [
            ({**self.ready_index(), 'documents':164}, self.ready_probe()),
            ({**self.ready_index(), 'revision':'c'*40}, self.ready_probe()),
            (self.ready_index(), {**self.ready_probe(), 'fingerprint':'c'*64}),
            (self.ready_index(), {**self.ready_probe(), 'revision':'c'*40}),
            (self.ready_index(), {**self.ready_probe(), 'hits':[{'path':'invented'}]}),
        ]
        for built, probe in bad_pairs:
            with self.subTest(built=built, probe=probe), patch.object(pilot, 'sandbox_json', side_effect=[built,probe]):
                with self.assertRaises(RuntimeError):
                    pilot.prepare_index('fixture-cli', {}, ROOT, 'a'*40)

    def test_command_errors_and_nonready_json_fail_closed(self):
        cases = [(1,'{"status":"ready"}'),(0,'{"status":"missing"}'),(0,'[]'),(0,'not JSON')]
        for code, stdout in cases:
            done = SimpleNamespace(returncode=code, stdout=stdout, stderr='controlled error')
            with self.subTest(code=code, stdout=stdout), patch.object(pilot.subprocess, 'run', return_value=done), \
                 patch.object(pilot, 'fixture_shell', return_value='fixture-pwsh', create=True):
                with self.assertRaisesRegex(RuntimeError, 'ready JSON'):
                    pilot.sandbox_json('fixture-cli', {}, ROOT, ':workspace', 'fixture-command')

    def test_missing_power_shell_stops_before_process_without_legacy_fallback(self):
        with patch.object(pilot.Path, 'is_file', return_value=False), patch.object(pilot.shutil, 'which', return_value=None), \
             patch.object(pilot.subprocess, 'run', side_effect=AssertionError('No shell may be started')) as run:
            with self.assertRaisesRegex(RuntimeError, 'PowerShell 7'):
                pilot.sandbox_json('fixture-cli', {}, ROOT, ':workspace', 'fixture-command')
            run.assert_not_called()

    def test_shell_selection_prefers_existing_cli_runtime(self):
        with patch.object(pilot.Path, 'is_file', return_value=True), patch.object(pilot.shutil, 'which') as which:
            self.assertIn('codex-primary-runtime', pilot.fixture_shell())
            which.assert_not_called()
        with patch.object(pilot.Path, 'is_file', return_value=False), patch.object(pilot.shutil, 'which', return_value='installed-pwsh'):
            self.assertEqual(pilot.fixture_shell(), 'installed-pwsh')


@unittest.skipUnless(os.name == 'nt' and os.environ.get('KI_REGELN_NATIVE_FIXTURE') == '1',
                     'Explicit Windows native fixture check; no model or installation')
class NativeFixtureRuntimeTests(unittest.TestCase):
    def test_host_negative_and_sandbox_positive_preserve_strict_gates(self):
        cli = shutil.which('codex')
        self.assertIsNotNone(cli, 'Existing Codex CLI is required')
        shell = pilot.fixture_shell()
        shell_version = subprocess.check_output([shell,'--version'],text=True,encoding='utf-8').strip()
        self.assertTrue(shell_version.startswith('PowerShell 7.'), shell_version)
        files = pilot.packet('c066cc3')
        self.assertEqual(len(files), 578)
        out = ROOT / '.validation' / ('fixture-runtime-check-' + uuid.uuid4().hex[:8])
        out.mkdir()
        environment = {k:v for k,v in os.environ.items() if not k.startswith(('GIT_', 'OPENAI_', 'ANTHROPIC_', 'CODEX_API_'))}
        environment['PYTHONDONTWRITEBYTECODE'] = ''
        environment.pop('PYTHONPYCACHEPREFIX', None)
        git_environment = dict(environment, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
            GIT_TERMINAL_PROMPT='0', GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000',
            GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000')

        def fixture(name):
            workspace = out/name; workspace.mkdir()
            for path,body in files.items():
                target = workspace/path; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(body)
            def git(*args):
                return subprocess.check_output(['git',*args],cwd=workspace,env=git_environment,stderr=subprocess.PIPE)
            git('init','--quiet','--object-format=sha1'); git('config','core.autocrlf','false')
            git('config','user.name','Fixture Runtime Check'); git('config','user.email','fixture@example.invalid')
            (workspace/'.gitignore').write_text('.validation/\n',encoding='utf-8',newline='\n')
            git('add','--all'); git('commit','--quiet','-m','Public product snapshot')
            state = workspace/'.validation'; state.mkdir()
            pilot.junction(state/'runtime',ROOT/'.validation/runtime')
            pilot.junction(state/'qmd-runtime',ROOT/'.validation/qmd-runtime')
            return workspace,git

        before,before_git = fixture('host-negative')
        host = pilot.search_rules.build(before,routing=True)
        old = subprocess.run([cli,'sandbox','--include-managed-config','--permission-profile',':workspace',
            '-c','windows.sandbox="elevated"','-C',str(before),'--',shell,'-NoProfile','-NonInteractive',
            '-Command',".\\Search-KI-Regeln.ps1 -Routing -Query 'zzfixturepreflight709c81' -Limit 1"],
            env=environment,capture_output=True,text=True,encoding='utf-8',timeout=120)
        negative = json.loads(old.stdout)
        self.assertNotEqual(old.returncode,0)
        self.assertEqual(negative['status'],'missing')
        self.assertTrue(list((before/'tools').rglob('*.pyc')))
        self.assertIn('tools/__pycache__/',before_git('status','--porcelain').decode())
        self.assertTrue(all((before/path).read_bytes()==body for path,body in files.items()))

        after,after_git = fixture('sandbox-positive')
        prepared = pilot.prepare_index(cli,environment,after,after_git('rev-parse','HEAD').decode().strip())
        self.assertEqual(prepared['build']['fingerprint'],host['fingerprint'])
        self.assertEqual(prepared['probe']['status'],'ready')
        self.assertEqual(after_git('status','--porcelain'),b'')
        self.assertEqual(list((after/'tools').rglob('*.pyc')),[])
        self.assertTrue(all((after/path).read_bytes()==body for path,body in files.items()))
        report = {'model_calls':0, 'profile':':workspace', 'shell':shell, 'shell_version':shell_version, 'source_files':len(files),
            'source_commit':pilot.search_rules.git(ROOT,'rev-parse','c066cc3').decode().strip(),
            'execution_commit':pilot.search_rules.git(ROOT,'rev-parse','HEAD').decode().strip(),
            'code_sha256':{name:pilot.sha((ROOT/name).read_bytes()) for name in
                           ('Evals/Onboarding/run_rule_routing_p4.py','tests/test_rule_routing_fixture_runtime.py')},
            'source_inventory_sha256':pilot.sha(json.dumps({name:pilot.sha(body) for name,body in sorted(files.items())},sort_keys=True).encode()),
            'host_negative':{'build':host,'query':negative,'query_exit':old.returncode,
                             'git_status':before_git('status','--porcelain').decode()},
            'sandbox_positive':prepared,'positive_git_status':'','positive_bytecode_files':[],
            'source_bytes_unchanged_in_both':True}
        pilot.dump(out/'result.json',report)
        print(json.dumps({'native_fixture_report':out.relative_to(ROOT).as_posix()+'/result.json'}),flush=True)


if __name__ == '__main__':
    unittest.main()
