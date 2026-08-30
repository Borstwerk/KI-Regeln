#!/usr/bin/env python3
"""Fixed-destination CONNECT guard for behavioral-runner egress.

Trusted runner infrastructure, not part of the evaluated model surface. The guard
listens on loopback only, accepts nothing but an HTTP CONNECT to exactly one
configured provider host and port, and tunnels that single destination through the
host-managed proxy. Everything else fails closed.

It never terminates TLS, never inspects payload after a tunnel opens, and never
records headers, credentials, proxy URLs or bodies. Only safe counters are kept.
"""
from __future__ import annotations

import argparse
import json
import re
import socket
import sys
import threading
from dataclasses import dataclass, field
from typing import Any, Mapping
from urllib.parse import urlsplit

PROVIDER_ENV = ("ANTHROPIC_BASE_URL",)
UPSTREAM_ENV = ("HTTPS_PROXY", "https_proxy")
ALLOWED_PORT = 443
MAX_REQUEST_BYTES = 8192
MAX_HOST_LENGTH = 255
REQUEST_LINE = re.compile(rb"^CONNECT ([!-~]{1,%d}) HTTP/1\.[01]$" % MAX_HOST_LENGTH)
PORT_PATTERN = re.compile(r"^[1-9][0-9]{0,4}$")
HOST_PATTERN = re.compile(r"^[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?(\.[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?)+$")
RELAY_CHUNK = 65536


class GuardError(RuntimeError):
    """Configuration or policy failure. Always fails closed."""


@dataclass(frozen=True)
class GuardTarget:
    host: str
    port: int


@dataclass
class GuardEvents:
    """Safe counters only. No header, payload, credential or URL is ever stored."""

    guard_started: bool = False
    listener_loopback_only: bool = False
    connect_allowed: int = 0
    connect_denied: int = 0
    upstream_connect_success: int = 0
    upstream_connect_denied: int = 0
    upstream_unavailable: int = 0
    malformed_requests: int = 0
    bytes_forwarded: bool = False
    shutdown_clean: bool = False
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def bump(self, name: str) -> None:
        with self._lock:
            setattr(self, name, getattr(self, name) + 1)

    def mark(self, name: str, value: bool = True) -> None:
        with self._lock:
            setattr(self, name, value)

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return {k: v for k, v in vars(self).items() if not k.startswith("_")}


def _normalize_host(raw: str) -> str:
    """Normalize an authority host, rejecting anything ambiguous."""
    if not raw or len(raw) > MAX_HOST_LENGTH:
        raise GuardError("host length out of range")
    if raw != raw.strip() or any(c in raw for c in "@/?#\\ \t[]:%_"):
        raise GuardError("host contains a disallowed character")
    try:
        host = raw.encode("idna").decode("ascii").lower() if not raw.isascii() else raw.lower()
    except UnicodeError as exc:
        raise GuardError("host is not IDNA-encodable") from exc
    if not HOST_PATTERN.fullmatch(host):
        raise GuardError("host is not a plain dotted DNS name")
    return host


def provider_target(env: Mapping[str, str]) -> GuardTarget:
    """Derive the single allowed destination from the controlled provider configuration."""
    raw = next((env[k] for k in PROVIDER_ENV if env.get(k)), "")
    if not raw:
        raise GuardError("provider endpoint configuration is missing")
    parts = urlsplit(raw.strip())
    if parts.scheme != "https":
        raise GuardError("provider endpoint must be https")
    if parts.username or parts.password:
        raise GuardError("provider endpoint must not carry userinfo")
    if not parts.hostname:
        raise GuardError("provider endpoint has no host")
    try:
        port = parts.port
    except ValueError as exc:
        raise GuardError("provider endpoint has an invalid port") from exc
    if port not in (None, ALLOWED_PORT):
        raise GuardError("provider endpoint port must be 443")
    return GuardTarget(_normalize_host(parts.hostname), ALLOWED_PORT)


def upstream_target(env: Mapping[str, str]) -> GuardTarget:
    """Derive the host-managed upstream proxy. Its value is never logged or reported."""
    raw = next((env[k] for k in UPSTREAM_ENV if env.get(k)), "")
    if not raw:
        raise GuardError("upstream proxy configuration is missing")
    parts = urlsplit(raw.strip())
    if parts.scheme not in ("http", "https"):
        raise GuardError("upstream proxy must be http or https")
    if not parts.hostname:
        raise GuardError("upstream proxy has no host")
    try:
        port = parts.port
    except ValueError as exc:
        raise GuardError("upstream proxy has an invalid port") from exc
    if port is None:
        raise GuardError("upstream proxy must name an explicit port")
    return GuardTarget(parts.hostname.lower(), port)


def parse_connect(request_line: bytes, allowed: GuardTarget) -> GuardTarget:
    """Accept only `CONNECT <allowed-host>:<allowed-port> HTTP/1.x` in authority form."""
    match = REQUEST_LINE.fullmatch(request_line)
    if not match:
        raise GuardError("only CONNECT in authority form is accepted")
    authority = match.group(1).decode("ascii")
    host_part, separator, port_part = authority.rpartition(":")
    if not separator or not host_part:
        raise GuardError("CONNECT authority must be host:port")
    if not PORT_PATTERN.fullmatch(port_part):
        raise GuardError("CONNECT port is not a plain decimal port")
    host = _normalize_host(host_part)
    if host != allowed.host or int(port_part) != allowed.port:
        raise GuardError("destination is not the single allowed provider target")
    return GuardTarget(host, allowed.port)


def _read_head(sock: socket.socket) -> bytes:
    """Read the request head, bounded. Headers are discarded, never parsed or stored."""
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        if len(buffer) > MAX_REQUEST_BYTES:
            raise GuardError("request head too large")
        chunk = sock.recv(RELAY_CHUNK)
        if not chunk:
            raise GuardError("client closed before completing the request head")
        buffer += chunk
    return buffer


def _relay(source: socket.socket, sink: socket.socket, events: GuardEvents) -> None:
    try:
        while True:
            data = source.recv(RELAY_CHUNK)
            if not data:
                break
            sink.sendall(data)
            events.mark("bytes_forwarded")
    except OSError:
        pass
    finally:
        for s in (source, sink):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass


class FixedDestinationGuard:
    """Loopback CONNECT guard bound to exactly one upstream destination."""

    def __init__(self, provider: GuardTarget, upstream: GuardTarget, *, timeout: float = 30.0):
        self.provider, self.upstream, self.timeout = provider, upstream, timeout
        self.events = GuardEvents()
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind(("127.0.0.1", 0))
        self._server.listen(8)
        self._stop = threading.Event()
        self._threads: list[threading.Thread] = []
        self._accept = threading.Thread(target=self._serve, daemon=True)

    @classmethod
    def from_env(cls, env: Mapping[str, str], **kwargs: Any) -> "FixedDestinationGuard":
        return cls(provider_target(env), upstream_target(env), **kwargs)

    @property
    def address(self) -> tuple[str, int]:
        return self._server.getsockname()[:2]

    @property
    def port(self) -> int:
        return self.address[1]

    def start(self) -> "FixedDestinationGuard":
        self.events.mark("guard_started")
        self.events.mark("listener_loopback_only", self.address[0] == "127.0.0.1")
        self._accept.start()
        return self

    def close(self) -> None:
        self._stop.set()
        try:
            self._server.close()
        except OSError:
            pass
        for t in list(self._threads):
            t.join(timeout=2.0)
        self.events.mark("shutdown_clean")

    def __enter__(self) -> "FixedDestinationGuard":
        return self.start()

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def _serve(self) -> None:
        while not self._stop.is_set():
            try:
                client, _ = self._server.accept()
            except OSError:
                break
            t = threading.Thread(target=self._handle, args=(client,), daemon=True)
            self._threads.append(t)
            t.start()

    def _deny(self, client: socket.socket, status: bytes) -> None:
        try:
            client.sendall(b"HTTP/1.1 " + status + b"\r\nContent-Length: 0\r\nConnection: close\r\n\r\n")
        except OSError:
            pass
        finally:
            client.close()

    def _handle(self, client: socket.socket) -> None:
        upstream: socket.socket | None = None
        try:
            client.settimeout(self.timeout)
            try:
                head = _read_head(client)
                parse_connect(head.split(b"\r\n", 1)[0], self.provider)
            except GuardError:
                self.events.bump("connect_denied")
                self.events.bump("malformed_requests")
                self._deny(client, b"403 Forbidden")
                return
            self.events.bump("connect_allowed")

            try:
                upstream = socket.create_connection((self.upstream.host, self.upstream.port), timeout=self.timeout)
            except OSError:
                self.events.bump("upstream_unavailable")
                self._deny(client, b"502 Bad Gateway")
                return

            authority = f"{self.provider.host}:{self.provider.port}".encode("ascii")
            upstream.sendall(b"CONNECT " + authority + b" HTTP/1.1\r\nHost: " + authority + b"\r\n\r\n")
            try:
                response = _read_head(upstream)
            except GuardError:
                self.events.bump("upstream_connect_denied")
                self._deny(client, b"502 Bad Gateway")
                return
            status = response.split(b"\r\n", 1)[0].split(b" ")
            if len(status) < 2 or not status[1].startswith(b"2"):
                self.events.bump("upstream_connect_denied")
                self._deny(client, b"502 Bad Gateway")
                return
            self.events.bump("upstream_connect_success")

            client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            client.settimeout(None)
            upstream.settimeout(None)
            pump = threading.Thread(target=_relay, args=(upstream, client, self.events), daemon=True)
            pump.start()
            _relay(client, upstream, self.events)
            pump.join(timeout=2.0)
        except Exception:  # fail closed on anything unexpected
            self.events.bump("connect_denied")
            try:
                client.close()
            except OSError:
                pass
        finally:
            for s in (client, upstream):
                if s is not None:
                    try:
                        s.close()
                    except OSError:
                        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-config", action="store_true",
                        help="Validate provider/upstream configuration without opening a listener")
    args = parser.parse_args()
    import os
    try:
        provider, upstream = provider_target(os.environ), upstream_target(os.environ)
    except GuardError as exc:
        print(f"GUARD_ERROR: {exc}", file=sys.stderr)
        return 2
    if args.check_config:
        # provider host is controlled configuration, not a secret; upstream is never printed
        print(json.dumps({"provider_host": provider.host, "provider_port": provider.port,
                          "upstream_configured": True}, sort_keys=True))
        return 0
    guard = FixedDestinationGuard(provider, upstream).start()
    print(json.dumps({"guard_port": guard.port, **guard.events.snapshot()}, sort_keys=True), flush=True)
    try:
        while True:
            threading.Event().wait(3600)
    except KeyboardInterrupt:
        guard.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
