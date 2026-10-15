"""Sealed Linux environment transport for credential-free runtime preparation only.

This removes environment values from setup argv. It does not admit credentials or
protect against a privileged host, process-memory inspection, swap or core dumps.
"""
from __future__ import annotations

from collections.abc import Mapping
from contextlib import contextmanager
import json
import os
import re
import sys

from .b2_boundary import BoundaryError

MAX_BYTES = 64 * 1024
MAX_ENTRIES = 128
FD_NAME = "b2-view-environment"
CONTRACT = "sealed-memfd-environment/v1"


class EnvironmentTransportError(BoundaryError):
    pass


def encode_environment(environment: Mapping[str, str]) -> bytes:
    """Refuse malformed or oversized input with value-free diagnostics."""
    try:
        if not isinstance(environment, Mapping) or len(environment) > MAX_ENTRIES:
            raise ValueError
        entries = dict(environment)
        if any(type(key) is not str or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key)
               or type(value) is not str or "\0" in value for key, value in entries.items()):
            raise ValueError
        payload = json.dumps(entries, ensure_ascii=False, sort_keys=True).encode("utf-8")
        if len(payload) > MAX_BYTES:
            raise ValueError
    except (TypeError, ValueError, UnicodeError):
        raise EnvironmentTransportError("environment_transport_input_refused") from None
    return payload


@contextmanager
def sealed_environment(environment: Mapping[str, str]):
    payload = encode_environment(environment)
    if sys.platform != "linux":
        raise EnvironmentTransportError("environment_transport_requires_linux")
    fd = -1
    try:
        try:
            import fcntl
            original = os.memfd_create(FD_NAME, os.MFD_CLOEXEC | os.MFD_ALLOW_SEALING)
            try:
                # The mount provider uses descriptor 3 for its setup marker.
                fd = fcntl.fcntl(original, fcntl.F_DUPFD_CLOEXEC, 10)
            finally:
                os.close(original)
            remaining = memoryview(payload)
            while remaining:
                written = os.write(fd, remaining)
                if written <= 0:
                    raise OSError
                remaining = remaining[written:]
            seals = fcntl.F_SEAL_WRITE | fcntl.F_SEAL_GROW | fcntl.F_SEAL_SHRINK | fcntl.F_SEAL_SEAL
            fcntl.fcntl(fd, fcntl.F_ADD_SEALS, seals)
            if fcntl.fcntl(fd, fcntl.F_GET_SEALS) & seals != seals:
                raise OSError
        except (OSError, AttributeError, ImportError):
            raise EnvironmentTransportError("environment_transport_unavailable") from None
        yield fd
    finally:
        if fd >= 0:
            os.close(fd)


# This trusted code travels in argv; no environment values do. It uses only the
# fixed read-only system Python and stdlib, and runs *after* the privilege drop.
# The receiver validates the wire representation independently of the encoder.
EXEC_PROGRAM = r'''
import fcntl,json,os,re,stat,sys
fd = -1
try:
    fd = int(sys.argv[1])
    if fd < 10 or len(sys.argv) < 3:
        raise ValueError
    info = os.fstat(fd)
    seals = fcntl.F_SEAL_WRITE | fcntl.F_SEAL_GROW | fcntl.F_SEAL_SHRINK | fcntl.F_SEAL_SEAL
    if (not stat.S_ISREG(info.st_mode) or not 0 < info.st_size <= MAX_BYTES
            or fcntl.fcntl(fd, fcntl.F_GET_SEALS) & seals != seals):
        raise ValueError
    body = os.pread(fd, MAX_BYTES + 1, 0)
    if len(body) != info.st_size:
        raise ValueError
    def unique(pairs):
        result = {}
        for key,value in pairs:
            if key in result:
                raise ValueError
            result[key] = value
        return result
    environment = json.loads(body.decode('utf-8'), object_pairs_hook=unique)
    if type(environment) is not dict or len(environment) > MAX_ENTRIES:
        raise ValueError
    if any(type(key) is not str or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', key)
            or type(value) is not str or '\0' in value for key,value in environment.items()):
        raise ValueError
    os.close(fd)
    fd = -1
    os.execvpe(sys.argv[2], sys.argv[2:], environment)
except Exception:
    if fd >= 0:
        try: os.close(fd)
        except OSError: pass
    print('B2_ENVIRONMENT_TRANSPORT_REFUSED', file=sys.stderr)
    sys.exit(125)
'''.replace("MAX_BYTES", str(MAX_BYTES)).replace("MAX_ENTRIES", str(MAX_ENTRIES))


def environment_exec_argv(fd: int, argv) -> tuple[str, ...]:
    if type(fd) is not int or fd < 10 or not argv:
        raise EnvironmentTransportError("environment_transport_invocation_refused")
    return ("/usr/bin/python3", "-I", "-c", EXEC_PROGRAM, str(fd), *argv)
