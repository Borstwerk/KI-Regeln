"""Portable input/construction controls; Linux exercises the actual descriptors."""
import json
import tempfile
import subprocess
import signal
import unittest
from pathlib import Path
from unittest import mock

from tools import b2_environment_transport as transport
from tools.b2_boundary import ConfinedInvocation
from tools import b2_separated_runtime as separated


class EnvironmentTransportContractTests(unittest.TestCase):
    def test_values_round_trip_as_data_without_shell_interpretation(self):
        value = "synthetic 'quotes' \"double\" $HOME $(touch planted)\nü\\text"
        self.assertEqual(json.loads(transport.encode_environment({'CANARY': value})), {'CANARY': value})

    def test_malformed_environment_is_refused_without_echoing_values(self):
        for value in ({'': 'SYNTHETIC-PRIVATE'}, {'A=B': 'SYNTHETIC-PRIVATE'},
                      {'NUL': 'SYNTHETIC-PRIVATE\0'}, {'A': True}, {1: 'value'},
                      {'A': '\ud800'}, [('A', 'value')]):
            with self.subTest(kind=type(value).__name__):
                with self.assertRaises(transport.EnvironmentTransportError) as caught:
                    transport.encode_environment(value)
                self.assertEqual(str(caught.exception), 'environment_transport_input_refused')

    def test_byte_and_entry_bounds_are_enforced(self):
        for value in ({'A': 'ü' * transport.MAX_BYTES},
                      {f'A{i}': '' for i in range(transport.MAX_ENTRIES + 1)}):
            with self.assertRaises(transport.EnvironmentTransportError):
                transport.encode_environment(value)

    def test_unavailable_runtime_does_not_fall_back_to_argv_or_a_disk_file(self):
        with mock.patch.object(transport.sys, 'platform', 'win32'):
            with self.assertRaisesRegex(transport.EnvironmentTransportError, 'requires_linux'):
                with transport.sealed_environment({'CANARY': 'synthetic'}):
                    self.fail('non-Linux transport was admitted')

    def test_exec_bootstrap_argv_contains_only_fixed_code_descriptor_and_target(self):
        argv = transport.environment_exec_argv(10, ('/usr/bin/python3', '-V'))
        self.assertEqual(argv[:3], ('/usr/bin/python3', '-I', '-c'))
        self.assertEqual(argv[-3:], ('10', '/usr/bin/python3', '-V'))
        compile(argv[3], '<trusted environment bootstrap>', 'exec')
        for fd in (3, -1, True, '10'):
            with self.assertRaises(transport.EnvironmentTransportError):
                transport.environment_exec_argv(fd, ('target',))

    def test_classic_invocations_have_no_descriptor_transfer_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            invocation = ConfinedInvocation(['fixed'], {}, Path(tmp) / 'marker')
            self.assertEqual(invocation.pass_fds, ())

    def test_timeout_and_interrupt_cleanup_only_the_session_the_executor_created(self):
        invocation = ConfinedInvocation(['fixed'], {}, Path('marker'), pass_fds=(10,))
        for failure in (subprocess.TimeoutExpired(['fixed'], 1, output='synthetic-private'), KeyboardInterrupt()):
            process = mock.Mock(pid=4242)
            process.communicate.side_effect = [failure, ('', '')]
            with mock.patch.object(separated.signal, 'SIGKILL', 9, create=True), mock.patch.object(separated.subprocess, 'Popen', return_value=process) as start, mock.patch.object(
                    separated.os, 'killpg', create=True) as kill:
                expected = KeyboardInterrupt if isinstance(failure, KeyboardInterrupt) else separated.SeparationError
                with self.assertRaises(expected) as caught:
                    separated.run_separated_invocation(invocation, timeout=1)
                self.assertNotIn('synthetic-private', str(caught.exception))
                kill.assert_called_once_with(4242, 9)
                self.assertTrue(start.call_args.kwargs['start_new_session'])
                self.assertEqual(start.call_args.kwargs['pass_fds'], (10,))

    def test_start_failure_and_missing_descriptor_are_fixed_errors_without_launch_fallback(self):
        invocation = ConfinedInvocation(['fixed'], {}, Path('marker'))
        with mock.patch.object(separated.subprocess, 'Popen') as start:
            with self.assertRaisesRegex(separated.SeparationError, 'descriptor_required'):
                separated.run_separated_invocation(invocation)
            start.assert_not_called()
        invocation = ConfinedInvocation(['fixed'], {}, Path('marker'), pass_fds=(10,))
        with mock.patch.object(separated.subprocess, 'Popen', side_effect=OSError('synthetic-private')):
            with self.assertRaisesRegex(separated.SeparationError, '^separated_runtime_start_failed$'):
                separated.run_separated_invocation(invocation)
