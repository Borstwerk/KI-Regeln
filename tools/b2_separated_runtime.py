"""Credential-free opt-in runtime: privileged setup, non-root payload, private snapshot.

Not connected to writable admission. In particular, the existing environment-in-argv
transport is not a secret transport; credential-bearing uses are explicitly refused.
"""
from __future__ import annotations

import errno
import os
import stat
import signal
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path

from .behavioral_harness_claude import SECRET_ENV, HOST_ONLY_AUTH_ENV, CREDENTIAL_CHANNEL_NAMES
from .b2_boundary import BoundaryError, confined_invocation
from .b2_model_confinement import model_view_spec
from .b2_boundary import VIEW_ENV
from .b2_environment_transport import environment_exec_argv, sealed_environment

PAYLOAD_IDENTITY = (1000, 1000)
RUNTIME_CONTRACT = "nonroot-unshare-view+userns-check/v1"


class SeparationError(BoundaryError):
    pass


def require_tools() -> None:
    if sys.platform != "linux" or os.geteuid() != 0:
        raise SeparationError("privileged_linux_evaluator_required")
    for name in ("setpriv", "bwrap"):
        try:
            path = Path("/usr/bin") / name
            info = path.stat()
            if (not stat.S_ISREG(info.st_mode) or info.st_uid != 0
                    or info.st_mode & (stat.S_ISUID | stat.S_ISGID | stat.S_IWGRP | stat.S_IWOTH)):
                raise SeparationError("runtime_tool_mode_refused")
            try:
                os.getxattr(path, "security.capability")
            except OSError as exc:
                if exc.errno != errno.ENODATA:
                    raise SeparationError("runtime_tool_capability_unverified") from None
            else:
                raise SeparationError("runtime_tool_file_capability_refused")
        except OSError:
            raise SeparationError("runtime_tool_unavailable") from None


def snapshot_workspace(source: Path, destination: Path) -> Path:
    """Copy through open directory/file descriptors; chown only exclusively new targets.

    No source path is followed after its parent directory is opened. Source symlinks,
    multiply linked files, special files and privilege bits are refused. The source is
    never chowned/chmodded; the evaluator owns the destination's inaccessible temp parent.
    """
    uid, gid = PAYLOAD_IDENTITY

    def copy_directory(source_fd: int, target: Path):
        target.mkdir(mode=0o700)
        target_fd = os.open(target, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            names = sorted(os.listdir(source_fd))
            for name in names:
                # O_PATH inspects an inode without opening a device/FIFO for I/O. Reopen
                # only a verified regular inode via our own kernel fd reference.
                child_fd = os.open(name, os.O_PATH | os.O_NOFOLLOW, dir_fd=source_fd)
                try:
                    before = os.fstat(child_fd)
                    if before.st_mode & (stat.S_ISUID | stat.S_ISGID):
                        raise SeparationError("snapshot_privilege_bits_refused")
                    if stat.S_ISDIR(before.st_mode):
                        directory_fd = os.open(".", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                               dir_fd=child_fd)
                        try:
                            copy_directory(directory_fd, target / name)
                        finally:
                            os.close(directory_fd)
                    elif stat.S_ISREG(before.st_mode) and before.st_nlink == 1:
                        content_fd = os.open(f"/proc/self/fd/{child_fd}", os.O_RDONLY | os.O_NONBLOCK)
                        try:
                            new_fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                             0o600, dir_fd=target_fd)
                        except BaseException:
                            os.close(content_fd)
                            raise
                        try:
                            opened = os.fstat(content_fd)
                            if (opened.st_dev, opened.st_ino, opened.st_mode) != (before.st_dev, before.st_ino, before.st_mode):
                                raise SeparationError("snapshot_source_changed")
                            remaining = before.st_size
                            while remaining:
                                chunk = os.read(content_fd, min(remaining, 1024 * 1024))
                                if not chunk:
                                    raise SeparationError("snapshot_source_changed")
                                remaining -= len(chunk)
                                view = memoryview(chunk)
                                while view:
                                    view = view[os.write(new_fd, view):]
                            after = os.fstat(child_fd)
                            if (os.read(content_fd, 1) or before.st_size != after.st_size
                                    or before.st_mtime_ns != after.st_mtime_ns
                                    or before.st_ctime_ns != after.st_ctime_ns or after.st_nlink != 1):
                                raise SeparationError("snapshot_source_changed")
                            os.fchmod(new_fd, 0o600 | (before.st_mode & 0o111))
                            os.fchown(new_fd, uid, gid)
                        finally:
                            os.close(content_fd)
                            os.close(new_fd)
                    else:
                        raise SeparationError("snapshot_unsafe_file_refused")
                finally:
                    os.close(child_fd)
            if names != sorted(os.listdir(source_fd)):
                raise SeparationError("snapshot_source_changed")
            os.fchown(target_fd, uid, gid)
        finally:
            os.close(target_fd)

    try:
        if not source.is_absolute() or ".." in source.parts:
            raise SeparationError("snapshot_absolute_source_required")
        # Do not follow a symlink in *any* source path component, including the root's
        # ancestors. Directory handles remain anchored across rename races.
        root_fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            for component in source.parts[1:]:
                next_fd = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                  dir_fd=root_fd)
                os.close(root_fd)
                root_fd = next_fd
        except BaseException:
            os.close(root_fd)
            raise
        try:
            if os.fstat(root_fd).st_mode & (stat.S_ISUID | stat.S_ISGID):
                raise SeparationError("snapshot_privilege_bits_refused")
            copy_directory(root_fd, destination)
        finally:
            os.close(root_fd)
    except OSError:
        raise SeparationError("snapshot_source_or_destination_refused") from None
    return destination


@contextmanager
def separated_model_invocation(argv, *, task_root: Path, workspace: Path, env,
                                claude_binary: str = "claude", timeout: int = 900):
    names = set(SECRET_ENV) | set(HOST_ONLY_AUTH_ENV) | set(CREDENTIAL_CHANNEL_NAMES)
    if any(os.environ.get(name) or env.get(name) for name in names):
        raise SeparationError("credential_free_runtime_required")
    require_tools()
    with tempfile.TemporaryDirectory(prefix="b2-separated-snapshot-") as tmp:
        snapshot = snapshot_workspace(workspace, Path(tmp) / "workspace")
        spec = model_view_spec(argv, task_root=task_root, workspace=snapshot, env=env,
                               claude_binary=claude_binary, timeout=timeout, separated_check=True)
        with sealed_environment(spec.env) as fd:
            spec = replace(spec, payload_identity=PAYLOAD_IDENTITY, private_tmp_mountpoint=True,
                           env=VIEW_ENV, argv=environment_exec_argv(fd, spec.argv))
            with confined_invocation(spec) as invocation:
                yield replace(invocation, pass_fds=(fd,))


def run_separated_invocation(invocation, *, timeout: float = 30):
    """Run the fixed preparation controls in their own session; bound cancellation.

    This is not a general supervisor for arbitrary model processes that deliberately
    detach their namespace init from the session. Such runs remain unadmitted.
    """
    if not invocation.pass_fds:
        raise SeparationError("separated_runtime_descriptor_required")
    try:
        process = subprocess.Popen(invocation.argv, env=invocation.env, cwd="/",
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                   start_new_session=True, pass_fds=invocation.pass_fds)
    except OSError:
        raise SeparationError("separated_runtime_start_failed") from None
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except BaseException as failure:
        # Only our successfully created session group is signalled. In particular,
        # setpriv's identity change cannot disable a host evaluator's killpg.
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        except OSError:
            raise SeparationError("separated_runtime_cleanup_failed") from None
        try:
            process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            process.stdout.close()
            process.stderr.close()
            raise SeparationError("separated_runtime_cleanup_unverified") from None
        except (OSError, ValueError, UnicodeError):
            raise SeparationError("separated_runtime_cleanup_unverified") from None
        if isinstance(failure, (KeyboardInterrupt, SystemExit)):
            raise
        code = ("separated_runtime_timed_out" if isinstance(failure, subprocess.TimeoutExpired)
                else "separated_runtime_execution_failed")
        raise SeparationError(code) from None
    return subprocess.CompletedProcess(invocation.argv, process.returncode, stdout, stderr)
