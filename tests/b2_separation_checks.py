"""Credential-free child suite. Invoked explicitly by the integration wrapper."""
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.b2_auth_bootstrap import IDENTITY_PROBE, MINIMAL_ENV, assess_identity, prepare
from tools.b2_dry_run import MODIFICATIONS, seed_workspace
from tools.b2_separated_runtime import SeparationError, require_tools, separated_model_invocation, snapshot_workspace, run_separated_invocation
from tools.behavioral_harness_claude import B2_CONTROL_ENV, _child_env
from tools.behavioral_harness_core import hash_file
from tools import b2_environment_transport as transport
from tools import b2_separated_runtime as separated


class SeparationChecks(unittest.TestCase):
    def run_payload(self, program, source=None, extra_env=None):
        with tempfile.TemporaryDirectory() as tmp:
            task = Path(tmp)
            workspace = source or seed_workspace("B2-01-legitimate-product-fix", task / "source")
            env, _ = _child_env(MINIMAL_ENV, task / "config", B2_CONTROL_ENV)
            env.update(extra_env or {})
            with separated_model_invocation(["/usr/bin/python3", "-I", "-c", program],
                                            task_root=task, workspace=workspace, env=env) as invocation:
                done = run_separated_invocation(invocation, timeout=40)
                self.assertTrue(invocation.payload_started())
            self.assertEqual(done.returncode, 0, done.stderr)
            return done.stdout

    def test_payload_identity_and_only_private_writable_locations(self):
        program = IDENTITY_PROBE + """
import os
from pathlib import Path
status = dict(line.split(':',1) for line in Path('/proc/self/status').read_text().splitlines())
assert int(status['CapBnd'],16) == 0
for path in ('/workspace/allowed', '/scratch/allowed'):
    Path(path).write_text('allowed')
for path in ('/planted', '/tmp/planted', '/b2-bin/check', '/b2-runtime/b2_boundary.py', '/etc/planted'):
    try: Path(path).write_text('forbidden')
    except OSError: pass
    else: raise AssertionError('write escaped workspace/scratch')
for path in ('/home', '/root', '/var', '/mnt'):
    assert not Path(path).exists()
assert list(Path('/tmp').iterdir()) == []
assert list(Path('/oldroot').iterdir()) == []
try: os.setuid(0)
except PermissionError: pass
else: raise AssertionError('root identity regained')
"""
        observed = json.loads(self.run_payload(program).strip())
        self.assertEqual(observed["Uid"], [1000] * 4)
        self.assertEqual(observed["Gid"], [1000] * 4)
        self.assertEqual(assess_identity(observed)[1], [])

    def test_snapshot_has_new_ownership_and_never_changes_original(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = seed_workspace("B2-01-legitimate-product-fix", root / "source")
            def metadata():
                return {str(path.relative_to(source)): (path.stat().st_uid, path.stat().st_gid,
                        path.stat().st_mode, hash_file(path)) for path in source.rglob('*') if path.is_file()}
            before = metadata()
            copy = snapshot_workspace(source, root / "copy")
            for path in (copy, *copy.rglob('*')):
                self.assertEqual((path.stat().st_uid, path.stat().st_gid), (1000, 1000))
            (copy / "product/discount.py").write_text('isolated change')
            self.assertEqual(metadata(), before)

    def test_snapshot_rejects_links_special_files_and_privilege_bits(self):
        for kind in ('symlink', 'directory-symlink', 'hardlink', 'fifo', 'socket', 'setuid',
                     'root-symlink', 'parent-symlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / 'source'
                source.mkdir()
                outside = root / 'outside'
                outside.write_text('outside sentinel')
                planted = source / 'planted'
                selected = source
                if kind == 'symlink': planted.symlink_to(outside)
                elif kind == 'directory-symlink': planted.symlink_to(root, target_is_directory=True)
                elif kind == 'hardlink': os.link(outside, planted)
                elif kind == 'fifo': os.mkfifo(planted)
                elif kind == 'socket':
                    with socket.socket(socket.AF_UNIX) as bound:
                        bound.bind(str(planted))
                elif kind in ('root-symlink', 'parent-symlink'):
                    alias = root / 'alias'
                    alias.symlink_to(source if kind == 'root-symlink' else root, target_is_directory=True)
                    selected = alias if kind == 'root-symlink' else alias / 'source'
                else:
                    planted.write_text('x')
                    planted.chmod(0o4755)
                with self.assertRaises(SeparationError):
                    snapshot_workspace(selected, root / 'copy')
                self.assertEqual(outside.read_text(), 'outside sentinel')

    def test_file_replacement_during_copy_cannot_redirect_to_an_outside_inode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source'
            source.mkdir()
            original = source / 'file'
            original.write_text('allowed fixture bytes')
            outside = root / 'outside'
            outside.write_text('private outside sentinel')
            actual_open = os.open
            raced = False

            def replace_before_read(path, *args, **kwargs):
                nonlocal raced
                if str(path).startswith('/proc/self/fd/') and not raced:
                    raced = True
                    original.rename(root / 'saved-original')
                    original.symlink_to(outside)
                return actual_open(path, *args, **kwargs)

            with mock.patch.object(os, 'open', side_effect=replace_before_read):
                with self.assertRaises(SeparationError):
                    snapshot_workspace(source, root / 'copy')
            self.assertTrue(raced)
            self.assertEqual(outside.read_text(), 'private outside sentinel')
            copied = root / 'copy/file'
            if copied.exists():
                self.assertNotIn('private outside sentinel', copied.read_text())

    def test_nested_red_and_green_checks_use_the_same_product_seed(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = seed_workspace('B2-01-legitimate-product-fix', Path(tmp) / 'source')
            program = "import subprocess,json; p=subprocess.run(['check'],capture_output=True,text=True); print(json.dumps({'rc':p.returncode,'stdout':p.stdout,'stderr':p.stderr}))"
            red = json.loads(self.run_payload(program, source))
            self.assertEqual(red['rc'], 1, red)
            self.assertIn('test_bulk_bonus_is_capped', red['stdout'])
            MODIFICATIONS['product-fix'](source)
            green = json.loads(self.run_payload(program, source))
            self.assertEqual(green['rc'], 0, green)

    def test_nested_view_hides_evaluator_tools_credential_and_host_network(self):
        with tempfile.TemporaryDirectory() as tmp, socket.socket() as listener:
            root = Path(tmp)
            sentinel = root / 'evaluator-canary'
            sentinel.write_text('B2-PRIVATE-EVALUATOR-CANARY')
            listener.bind(('127.0.0.1', 0))
            listener.listen(4)
            port = listener.getsockname()[1]
            with socket.create_connection(('127.0.0.1', port), timeout=2):
                pass  # Positive network control: host endpoint really exists.
            source = seed_workspace('B2-01-legitimate-product-fix', root / 'source')
            (source / 'checks/validate.py').write_text("""
import json,os,socket
from pathlib import Path
canary = 'B2-SYNTHETIC-PROVIDER-CANARY'
assert canary not in str(dict(os.environ))
for fd in Path('/proc/self/fd').iterdir():
    try: target = os.readlink(fd)
    except OSError: continue
    assert 'memfd:b2-view-environment' not in target
status = dict(line.split(':',1) for line in Path('/proc/self/status').read_text().splitlines())
for key in ('Uid','Gid'):
    assert [int(value) for value in status[key].split()] == [1000] * 4
for key in ('CapInh','CapPrm','CapEff','CapAmb','CapBnd'):
    assert int(status[key],16) == 0
assert int(status['NoNewPrivs']) == 1
for path in ('/proc/1/environ', '/proc/self/environ'):
    try: body = Path(path).read_bytes()
    except OSError: body = b''
    assert canary.encode() not in body
for path in (%r, '/b2-bin/check', '/b2-runtime', '/home', '/root', '/oldroot'):
    assert not Path(path).exists(), path
assert sorted(p.name for p in Path('/etc').iterdir()) == ['alternatives']
try: Path('/etc/planted').write_text('forbidden')
except OSError: pass
else: raise AssertionError('inner runtime parent writable')
try: Path('/planted').write_text('forbidden')
except OSError: pass
else: raise AssertionError('inner root writable')
Path('/workspace/inner-write').write_text('allowed')
Path('/scratch/inner-write').write_text('allowed')
try: socket.create_connection(('127.0.0.1', %d), timeout=1)
except OSError: pass
else: raise AssertionError('host network endpoint reachable')
print(json.dumps({'checks':'passed','credential_seen':False,'network_blocked':True}))
""" % (str(sentinel), port))
            outer_program = """
import json,subprocess,os
from pathlib import Path
assert os.environ['B2_SYNTHETIC_PROVIDER'] == 'B2-SYNTHETIC-PROVIDER-CANARY'
try: Path(%r).read_bytes()
except OSError: pass
else: raise AssertionError('evaluator sentinel readable in outer view')
p = subprocess.run(['check'],capture_output=True,text=True)
assert p.returncode == 0, (p.returncode,p.stdout,p.stderr)
print(p.stdout)
""" % str(sentinel)
            output = self.run_payload(outer_program, source,
                                      {'B2_SYNTHETIC_PROVIDER': 'B2-SYNTHETIC-PROVIDER-CANARY'})
            self.assertEqual(json.loads(output)['checks'], 'passed')

    def test_separated_bootstrap_is_only_prepared_and_cli_startup_keeps_scrub_control(self):
        require_tools()
        report = prepare(separated_runtime=True)
        self.assertEqual(report['status'], 'PREPARED_ONLY', report['blockers'])
        self.assertFalse(report['may_start_authentication'])
        self.assertFalse(report['may_start_model_pilot'])
        program = """
import os,subprocess,json
assert os.environ['CLAUDE_CODE_SUBPROCESS_ENV_SCRUB'] == '1'
for flag in ('--version','--help'):
    p = subprocess.run(['claude',flag],capture_output=True,text=True,timeout=30)
    assert p.returncode == 0, ('startup failed',flag,p.returncode)
print(json.dumps({'startup':'passed','tool_scrub':'NOT RUN','authentication':'NOT RUN'}))
"""
        result = json.loads(self.run_payload(program))
        self.assertEqual(result['startup'], 'passed')
        self.assertEqual(result['tool_scrub'], 'NOT RUN')

    def test_transport_is_sealed_and_parent_descriptor_closes_on_all_context_exits(self):
        import fcntl
        for broken_context in (False, True):
            fd = -1
            try:
                with transport.sealed_environment({'CANARY': 'synthetic'}) as fd:
                    self.assertGreaterEqual(fd, 10)
                    self.assertFalse(os.get_inheritable(fd))
                    expected = fcntl.F_SEAL_WRITE | fcntl.F_SEAL_GROW | fcntl.F_SEAL_SHRINK | fcntl.F_SEAL_SEAL
                    self.assertEqual(fcntl.fcntl(fd, fcntl.F_GET_SEALS) & expected, expected)
                    for operation in (lambda: os.write(fd, b'x'), lambda: os.ftruncate(fd, 0),
                                      lambda: os.ftruncate(fd, transport.MAX_BYTES),
                                      lambda: fcntl.fcntl(fd, fcntl.F_ADD_SEALS, fcntl.F_SEAL_WRITE)):
                        with self.assertRaises(OSError):
                            operation()
                    if broken_context:
                        raise RuntimeError('controlled context interruption')
            except RuntimeError:
                self.assertTrue(broken_context)
            with self.assertRaises(OSError):
                os.fstat(fd)

    def test_receiver_rejects_missing_unsealed_and_malformed_descriptors_without_echo(self):
        import fcntl
        with tempfile.TemporaryDirectory() as tmp:
            marker = Path(tmp) / 'target-ran'
            target = ('/usr/bin/python3', '-I', '-c', f'from pathlib import Path; Path({str(marker)!r}).touch()')
            flags = fcntl.F_SEAL_WRITE | fcntl.F_SEAL_GROW | fcntl.F_SEAL_SHRINK | fcntl.F_SEAL_SEAL
            cases = ((b'{"CANARY":"SYNTHETIC-PRIVATE"}', 0, True),
                     (b'{"CANARY":"SYNTHETIC-PRIVATE"}', flags, False),
                     (b'not json SYNTHETIC-PRIVATE', flags, True),
                     (b'{"A":"x","A":"SYNTHETIC-PRIVATE"}', flags, True),
                     (b'{"A":"SYNTHETIC-PRIVATE\\u0000"}', flags, True),
                     (b'{"A":false}', flags, True), (b'\xff', flags, True),
                     (b'{"A=B":"SYNTHETIC-PRIVATE"}', flags, True),
                     (json.dumps({f'A{i}': '' for i in range(transport.MAX_ENTRIES + 1)}).encode(), flags, True),
                     (b'x' * (transport.MAX_BYTES + 1), flags, True))
            cases += tuple((b'{"CANARY":"SYNTHETIC-PRIVATE"}', flags & ~seal, True) for seal in
                           (fcntl.F_SEAL_WRITE, fcntl.F_SEAL_GROW, fcntl.F_SEAL_SHRINK, fcntl.F_SEAL_SEAL))
            for body, sealed, inherited in cases:
                with self.subTest(seals=sealed, inherited=inherited):
                    original = os.memfd_create(transport.FD_NAME, os.MFD_ALLOW_SEALING | os.MFD_CLOEXEC)
                    try:
                        fd = fcntl.fcntl(original, fcntl.F_DUPFD_CLOEXEC, 10)
                    finally:
                        os.close(original)
                    try:
                        os.write(fd, body)
                        if sealed:
                            fcntl.fcntl(fd, fcntl.F_ADD_SEALS, sealed)
                        result = subprocess.run(transport.environment_exec_argv(fd, target), env=MINIMAL_ENV,
                                                pass_fds=(fd,) if inherited else (), text=True,
                                                capture_output=True, timeout=10, check=False)
                        self.assertEqual(result.returncode, 125)
                        self.assertEqual(result.stdout, '')
                        self.assertEqual(result.stderr, 'B2_ENVIRONMENT_TRANSPORT_REFUSED\n')
                        self.assertFalse(marker.exists())
                    finally:
                        os.close(fd)

    def test_construction_faults_close_both_descriptors_and_partial_writes_preserve_data(self):
        import fcntl
        actual_create, actual_fcntl, actual_write = os.memfd_create, fcntl.fcntl, os.write
        for fault in ('duplicate', 'write', 'seal', 'partial-write'):
            observed = []

            def create(*args):
                fd = actual_create(*args)
                observed.append(fd)
                return fd

            def control(fd, operation, argument=0):
                if ((fault == 'duplicate' and operation == fcntl.F_DUPFD_CLOEXEC)
                        or (fault == 'seal' and operation == fcntl.F_ADD_SEALS)):
                    raise OSError('SYNTHETIC-PRIVATE-CONSTRUCTION-ERROR')
                result = actual_fcntl(fd, operation, argument)
                if operation == fcntl.F_DUPFD_CLOEXEC:
                    observed.append(result)
                return result

            def write(fd, data):
                if fault == 'write':
                    raise OSError('SYNTHETIC-PRIVATE-CONSTRUCTION-ERROR')
                return actual_write(fd, data[:max(1, len(data) // 2)])

            with self.subTest(fault=fault), mock.patch.object(os, 'memfd_create', side_effect=create), mock.patch.object(
                    fcntl, 'fcntl', side_effect=control), mock.patch.object(os, 'write', side_effect=write):
                if fault == 'partial-write':
                    with transport.sealed_environment({'CANARY': 'literal-synthetic'}) as fd:
                        self.assertEqual(json.loads(os.pread(fd, transport.MAX_BYTES, 0)), {'CANARY': 'literal-synthetic'})
                else:
                    with self.assertRaisesRegex(transport.EnvironmentTransportError, '^environment_transport_unavailable$'):
                        with transport.sealed_environment({'CANARY': 'literal-synthetic'}):
                            self.fail('construction fault admitted')
            for fd in observed:
                with self.assertRaises(OSError):
                    os.fstat(fd)

    def test_real_transport_delivers_literal_values_outside_argv_and_closes_before_payload(self):
        canary = "B2-SYNTHETIC-PRIVATE-'quote'-\"double\"-$(touch /workspace/planted)\nü\\literal"
        with tempfile.TemporaryDirectory() as tmp:
            task = Path(tmp)
            source = seed_workspace('B2-01-legitimate-product-fix', task / 'source')
            env, _ = _child_env(MINIMAL_ENV, task / 'config', B2_CONTROL_ENV)
            env['B2_SYNTHETIC_PROVIDER'] = canary
            program = """
import json,os
from pathlib import Path
targets = []
for path in Path('/proc/self/fd').iterdir():
    try: targets.append(os.readlink(path))
    except OSError: pass
assert not any('memfd:b2-view-environment' in target for target in targets)
assert not Path('/workspace/planted').exists()
print(json.dumps({'received':os.environ['B2_SYNTHETIC_PROVIDER']}))
"""
            with separated_model_invocation(['/usr/bin/python3', '-I', '-c', program], task_root=task,
                                            workspace=source, env=env) as invocation:
                self.assertNotIn(canary, str(invocation.argv))
                self.assertNotIn(canary, str(invocation.env))
                self.assertNotIn(canary, repr(invocation))
                self.assertEqual(len(invocation.pass_fds), 1)
                result = run_separated_invocation(invocation)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(invocation.payload_started())
                self.assertEqual(json.loads(result.stdout)['received'], canary)
            with self.assertRaises(OSError):
                os.fstat(invocation.pass_fds[0])

    def test_timeout_after_nonroot_handoff_leaves_no_live_monitor_init_or_parent_fd(self):
        with tempfile.TemporaryDirectory() as tmp:
            task = Path(tmp)
            source = seed_workspace('B2-01-legitimate-product-fix', task / 'source')
            env, _ = _child_env(MINIMAL_ENV, task / 'config', B2_CONTROL_ENV)
            env['B2_SYNTHETIC_PROVIDER'] = 'controlled-timeout-canary'
            program = """
import json,os,time
from pathlib import Path
assert os.getuid() == 1000
assert os.environ['B2_SYNTHETIC_PROVIDER'].startswith('controlled-timeout-')
for fd in Path('/proc/self/fd').iterdir():
    try: target = os.readlink(fd)
    except OSError: continue
    assert 'memfd:b2-view-environment' not in target
Path('/workspace/ready').write_text('nonroot-handoff-complete')
time.sleep(60)
"""
            actual_start = subprocess.Popen
            observed = []
            with separated_model_invocation(['/usr/bin/python3', '-I', '-c', program], task_root=task,
                                            workspace=source, env=env) as invocation:
                ready = Path(invocation.env['B2_WORKSPACE']) / 'ready'

                def start_and_observe(*args, **kwargs):
                    process = actual_start(*args, **kwargs)
                    observed.append(process.pid)
                    communicate = process.communicate

                    def after_ready(*, timeout):
                        if len(observed) == 1:
                            deadline = time.monotonic() + 8
                            while not ready.exists() and time.monotonic() < deadline and process.poll() is None:
                                time.sleep(0.02)
                            self.assertTrue(ready.exists(), 'fixed nonroot handoff did not become ready')
                            children = Path(f'/proc/{process.pid}/task/{process.pid}/children').read_text().split()
                            self.assertEqual(len(children), 1)
                            observed.append(int(children[0]))
                        return communicate(timeout=timeout)

                    process.communicate = after_ready
                    return process

                with mock.patch.object(separated.subprocess, 'Popen', side_effect=start_and_observe):
                    with self.assertRaisesRegex(SeparationError, '^separated_runtime_timed_out$'):
                        run_separated_invocation(invocation, timeout=0.1)
                self.assertEqual(ready.read_text(), 'nonroot-handoff-complete')
            self.assertEqual(len(observed), 2)
            for pid in observed:
                path = Path(f'/proc/{pid}/stat')
                if path.exists():
                    self.assertEqual(path.read_text().rsplit(')', 1)[1].split()[0], 'Z', 'live orphan remains')
                    self.assertEqual(list(Path(f'/proc/{pid}/fd').iterdir()), [])
            with self.assertRaises(OSError):
                os.fstat(invocation.pass_fds[0])


if __name__ == '__main__':
    unittest.main()
