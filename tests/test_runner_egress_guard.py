from __future__ import annotations

import socket
import threading
import unittest

from tools import runner_egress_guard as guard

PROVIDER = "api.example-provider.test"
BASE_ENV = {"ANTHROPIC_BASE_URL": f"https://{PROVIDER}", "HTTPS_PROXY": "http://127.0.0.1:1"}


class FakeUpstream:
    """Minimal upstream proxy: accepts one CONNECT, answers with `status`, then echoes."""

    def __init__(self, status: bytes = b"200 Connection Established"):
        self.status = status
        self.seen_connect: bytes | None = None
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind(("127.0.0.1", 0))
        self._sock.listen(4)
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()

    @property
    def target(self) -> guard.GuardTarget:
        host, port = self._sock.getsockname()[:2]
        return guard.GuardTarget(host, port)

    def _serve(self) -> None:
        while not self._stop.is_set():
            try:
                conn, _ = self._sock.accept()
            except OSError:
                return
            threading.Thread(target=self._handle, args=(conn,), daemon=True).start()

    def _handle(self, conn: socket.socket) -> None:
        try:
            head = b""
            while b"\r\n\r\n" not in head:
                chunk = conn.recv(4096)
                if not chunk:
                    return
                head += chunk
            self.seen_connect = head.split(b"\r\n", 1)[0]
            conn.sendall(b"HTTP/1.1 " + self.status + b"\r\n\r\n")
            if not self.status.startswith(b"2"):
                conn.close()
                return
            while True:  # echo, so the test can prove bidirectional transport
                data = conn.recv(4096)
                if not data:
                    return
                conn.sendall(data)
        except OSError:
            return
        finally:
            try:
                conn.close()
            except OSError:
                pass

    def close(self) -> None:
        self._stop.set()
        try:
            self._sock.close()
        except OSError:
            pass


def speak(port: int, request: bytes, *, payload: bytes = b"") -> tuple[bytes, bytes]:
    """Send a raw request to the guard; return (status line, echoed payload)."""
    with socket.create_connection(("127.0.0.1", port), timeout=5) as s:
        s.settimeout(5)
        s.sendall(request)
        head = b""
        while b"\r\n\r\n" not in head:
            chunk = s.recv(4096)
            if not chunk:
                break
            head += chunk
        status = head.split(b"\r\n", 1)[0]
        body = b""
        if payload and status.split(b" ")[1:2] == [b"200"]:
            s.sendall(payload)
            body = s.recv(4096)
        return status, body


def connect_request(authority: str) -> bytes:
    return f"CONNECT {authority} HTTP/1.1\r\nHost: {authority}\r\n\r\n".encode()


class GuardConfigTests(unittest.TestCase):
    def test_01_provider_target_comes_from_controlled_configuration(self):
        t = guard.provider_target(BASE_ENV)
        self.assertEqual(PROVIDER, t.host)
        self.assertEqual(443, t.port)

    def test_02_missing_provider_configuration_fails_closed(self):
        with self.assertRaisesRegex(guard.GuardError, "provider endpoint configuration is missing"):
            guard.provider_target({"HTTPS_PROXY": "http://127.0.0.1:1"})

    def test_03_missing_upstream_configuration_fails_closed(self):
        with self.assertRaisesRegex(guard.GuardError, "upstream proxy configuration is missing"):
            guard.upstream_target({"ANTHROPIC_BASE_URL": f"https://{PROVIDER}"})

    def test_04_non_https_or_userinfo_or_odd_port_provider_is_rejected(self):
        for value, reason in [
            (f"http://{PROVIDER}", "must be https"),
            (f"https://user:pw@{PROVIDER}", "userinfo"),
            (f"https://{PROVIDER}:8443", "port must be 443"),
            ("https://", "no host"),
        ]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(guard.GuardError, reason):
                    guard.provider_target({"ANTHROPIC_BASE_URL": value})

    def test_05_upstream_requires_explicit_port(self):
        with self.assertRaisesRegex(guard.GuardError, "explicit port"):
            guard.upstream_target({"HTTPS_PROXY": "http://proxy.internal"})

    def test_05a_http_upstream_with_explicit_port_is_accepted(self):
        t = guard.upstream_target({"HTTPS_PROXY": "http://proxy.internal:3128"})
        self.assertEqual(("proxy.internal", 3128), (t.host, t.port))

    def test_05b_https_upstream_fails_closed_because_no_tls_is_implemented(self):
        """The guard opens a plain socket and speaks CONNECT; https:// must not be accepted."""
        for value in ("https://proxy.internal:3128", "https://proxy.internal:443"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(guard.GuardError, "must be http"):
                    guard.upstream_target({"HTTPS_PROXY": value})
        with self.assertRaisesRegex(guard.GuardError, "must be http"):
            guard.FixedDestinationGuard.from_env(
                {"ANTHROPIC_BASE_URL": f"https://{PROVIDER}", "HTTPS_PROXY": "https://proxy.internal:3128"})


class ConnectParserTests(unittest.TestCase):
    allowed = guard.GuardTarget(PROVIDER, 443)

    def assert_denied(self, line: str):
        with self.assertRaises(guard.GuardError):
            guard.parse_connect(line.encode(), self.allowed)

    def test_06_exact_provider_and_port_is_accepted(self):
        t = guard.parse_connect(f"CONNECT {PROVIDER}:443 HTTP/1.1".encode(), self.allowed)
        self.assertEqual((PROVIDER, 443), (t.host, t.port))
        self.assertEqual(PROVIDER, guard.parse_connect(
            f"CONNECT {PROVIDER.upper()}:443 HTTP/1.0".encode(), self.allowed).host)

    def test_07_other_hosts_are_denied(self):
        for authority in ["example.com:443", f"{PROVIDER}.example.com:443",
                          f"example.com.{PROVIDER}:443", f"evil-{PROVIDER}:443",
                          f"sub.{PROVIDER}:443", f"{PROVIDER}.:443", "127.0.0.1:443",
                          "160.79.104.10:443", "[::1]:443", "localhost:443"]:
            with self.subTest(authority=authority):
                self.assert_denied(f"CONNECT {authority} HTTP/1.1")

    def test_08_other_ports_are_denied(self):
        for port in ["80", "8443", "0443", "443443", "4430", "0", "65536", "+443", "443 "]:
            with self.subTest(port=port):
                self.assert_denied(f"CONNECT {PROVIDER}:{port} HTTP/1.1")

    def test_09_other_methods_are_denied(self):
        for method in ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE", "PATCH", "connect"]:
            with self.subTest(method=method):
                self.assert_denied(f"{method} https://{PROVIDER}/ HTTP/1.1")

    def test_10_userinfo_scheme_and_path_forms_are_denied(self):
        for authority in [f"{PROVIDER}@example.com:443", f"user@{PROVIDER}:443",
                          f"https://{PROVIDER}:443", f"{PROVIDER}:443/path",
                          f"{PROVIDER}:443?q=1", f"{PROVIDER}:443#f", f"{PROVIDER}", ":443"]:
            with self.subTest(authority=authority):
                self.assert_denied(f"CONNECT {authority} HTTP/1.1")

    def test_11_whitespace_encoding_and_version_ambiguities_are_denied(self):
        for line in [f"CONNECT  {PROVIDER}:443 HTTP/1.1", f"CONNECT {PROVIDER}:443  HTTP/1.1",
                     f" CONNECT {PROVIDER}:443 HTTP/1.1", f"CONNECT {PROVIDER}:443 HTTP/2.0",
                     f"CONNECT {PROVIDER}:443", f"CONNECT {PROVIDER}%2e:443 HTTP/1.1",
                     f"CONNECT {PROVIDER}:443 HTTP/1.1 extra", f"CONNECT xn--{PROVIDER}:443 HTTP/1.1"]:
            with self.subTest(line=line):
                self.assert_denied(line)

    def test_12_oversized_and_non_ascii_request_lines_are_denied(self):
        self.assert_denied("CONNECT " + "a" * 300 + ":443 HTTP/1.1")
        with self.assertRaises(guard.GuardError):
            guard.parse_connect(f"CONNECT {PROVIDER}:443 HTTP/1.1".encode("utf-16"), self.allowed)
        with self.assertRaises(guard.GuardError):
            guard.parse_connect("CONNECT äpi.example.test:443 HTTP/1.1".encode("utf-8"), self.allowed)

    def test_13_idna_provider_configuration_normalises_once(self):
        t = guard.provider_target({"ANTHROPIC_BASE_URL": "https://xn--pi-fma.example.test"})
        self.assertTrue(t.host.startswith("xn--"))
        self.assertEqual(t.host, guard.parse_connect(f"CONNECT {t.host}:443 HTTP/1.1".encode(), t).host)


class GuardServerTests(unittest.TestCase):
    def setUp(self):
        self.upstream = FakeUpstream()
        self.addCleanup(self.upstream.close)

    def make_guard(self, upstream=None, status=None):
        if status is not None:
            self.upstream.close()
            self.upstream = FakeUpstream(status=status)
            self.addCleanup(self.upstream.close)
        g = guard.FixedDestinationGuard(guard.GuardTarget(PROVIDER, 443),
                                        upstream or self.upstream.target, timeout=5.0).start()
        self.addCleanup(g.close)
        return g

    def test_14_listener_is_loopback_only_and_ephemeral(self):
        g = self.make_guard()
        self.assertEqual("127.0.0.1", g.address[0])
        self.assertNotIn(g.address[0], ("0.0.0.0", "::"))
        self.assertGreater(g.port, 0)
        self.assertTrue(g.events.snapshot()["listener_loopback_only"])
        self.assertTrue(g.events.snapshot()["guard_started"])

    def test_15_positive_control_tunnel_and_bidirectional_bytes(self):
        g = self.make_guard()
        status, echoed = speak(g.port, connect_request(f"{PROVIDER}:443"), payload=b"ping-through-tunnel")
        self.assertEqual(b"HTTP/1.1 200 Connection Established", status)
        self.assertEqual(b"ping-through-tunnel", echoed)
        self.assertEqual(f"CONNECT {PROVIDER}:443 HTTP/1.1".encode(), self.upstream.seen_connect)
        snap = g.events.snapshot()
        self.assertEqual(1, snap["connect_allowed"])
        self.assertEqual(1, snap["upstream_connect_success"])
        self.assertEqual(0, snap["connect_denied"])
        self.assertTrue(snap["bytes_forwarded"])

    def test_16_denied_destinations_never_reach_the_upstream(self):
        g = self.make_guard()
        for request in [connect_request("example.com:443"), connect_request(f"{PROVIDER}:80"),
                        connect_request(f"{PROVIDER}:8443"), connect_request(f"sub.{PROVIDER}:443"),
                        connect_request("127.0.0.1:443"),
                        f"GET https://{PROVIDER}/ HTTP/1.1\r\nHost: {PROVIDER}\r\n\r\n".encode()]:
            with self.subTest(request=request[:40]):
                status, _ = speak(g.port, request)
                self.assertEqual(b"HTTP/1.1 403 Forbidden", status)
        self.assertIsNone(self.upstream.seen_connect)
        snap = g.events.snapshot()
        self.assertEqual(6, snap["connect_denied"])
        self.assertEqual(0, snap["connect_allowed"])
        self.assertEqual(0, snap["upstream_connect_success"])
        self.assertFalse(snap["bytes_forwarded"])

    def test_17_upstream_denial_opens_no_local_tunnel(self):
        g = self.make_guard(status=b"403 Forbidden")
        status, _ = speak(g.port, connect_request(f"{PROVIDER}:443"))
        self.assertEqual(b"HTTP/1.1 502 Bad Gateway", status)
        snap = g.events.snapshot()
        self.assertEqual(1, snap["connect_allowed"])
        self.assertEqual(1, snap["upstream_connect_denied"])
        self.assertEqual(0, snap["upstream_connect_success"])
        self.assertFalse(snap["bytes_forwarded"])

    def test_18_unreachable_upstream_fails_closed(self):
        dead = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dead.bind(("127.0.0.1", 0))
        port = dead.getsockname()[1]
        dead.close()
        g = self.make_guard(upstream=guard.GuardTarget("127.0.0.1", port))
        status, _ = speak(g.port, connect_request(f"{PROVIDER}:443"))
        self.assertEqual(b"HTTP/1.1 502 Bad Gateway", status)
        snap = g.events.snapshot()
        self.assertEqual(1, snap["upstream_unavailable"])
        self.assertFalse(snap["bytes_forwarded"])

    def test_19_oversized_request_head_fails_closed(self):
        g = self.make_guard()
        blob = b"CONNECT " + b"a" * 9000 + b":443 HTTP/1.1\r\n\r\n"
        status, _ = speak(g.port, blob)
        self.assertEqual(b"HTTP/1.1 403 Forbidden", status)
        self.assertIsNone(self.upstream.seen_connect)

    def test_20_events_snapshot_carries_no_sensitive_material(self):
        g = self.make_guard()
        speak(g.port, connect_request(f"{PROVIDER}:443"), payload=b"secret-payload-not-logged")
        speak(g.port, connect_request("example.com:443"))
        snap = g.events.snapshot()
        self.assertTrue(all(isinstance(v, (bool, int)) for v in snap.values()), snap)
        blob = repr(snap)
        for forbidden in ["secret-payload-not-logged", "Authorization", "Proxy-Authorization",
                          "Cookie", PROVIDER, "example.com", str(self.upstream.target.port), "http://"]:
            self.assertNotIn(forbidden, blob)

    def test_21_close_is_clean_and_idempotent(self):
        g = self.make_guard()
        g.close()
        g.close()
        self.assertTrue(g.events.snapshot()["shutdown_clean"])


if __name__ == "__main__":
    unittest.main()
