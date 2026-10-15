#!/usr/bin/env python3
"""Render existing verification evidence to a standalone offline HTML report.

Presentation only: no test execution, no overall verdict inferred for portable
verification-run reports, and no replacement for native/behavioral verification.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STATUS_STYLE = {
    "PASS": "pass",
    "FAIL": "fail",
    "BLOCKED": "blocked",
    "NOT_RUN": "pending",
    "NOT RUN": "pending",
    "UNVERIFIED": "pending",
    "SKIP": "pending",
    "WARN": "warn",
    "INFO": "info",
}
LOCAL_STATUSES = {"PASS", "FAIL", "WARN", "INFO", "SKIP", "NOT RUN"}
LOCAL_SEVERITIES = {"error", "warning", "info"}

CSS = """
:root { color-scheme: dark; font: 16px/1.55 system-ui, -apple-system, Segoe UI, sans-serif;
  --bg:#0b1220; --panel:#131f32; --panel2:#18273a; --line:#304158; --muted:#adbed0; --text:#f0f5fc; }
* { box-sizing: border-box; }
body { margin:0; background:radial-gradient(circle at 92% -12%, #213b5e 0, transparent 36%),var(--bg);
  color:var(--text); min-height:100vh; }
main { width:min(1040px,calc(100% - 32px)); margin:0 auto; padding:42px 0 70px; }
h1 { font-size:clamp(1.65rem,4vw,2.5rem); line-height:1.12; letter-spacing:-.035em; margin:.25rem 0 .65rem; }
h2 { font-size:1.14rem; margin:0 0 14px; }
p { margin:.4em 0; } .muted { color:var(--muted); }
.eyebrow { color:#8cc4f8; letter-spacing:.13em; text-transform:uppercase; font-size:.75rem; font-weight:750; }
.lead { max-width:78ch; font-size:1.05rem; color:var(--muted); }
.panel { border:1px solid var(--line); background:var(--panel); padding:23px; border-radius:17px; margin:18px 0; }
.hero { border-left:4px solid #7199c5; } .hero.pass { border-left-color:#48d5a2; }
.hero.fail { border-left-color:#ff787e; } .hero.warn { border-left-color:#efc36e; }
.hero.pending { border-left-color:#a8b5c9; }
.grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin:20px 0; }
.metric { background:var(--panel); border:1px solid var(--line); padding:16px 18px; border-radius:14px; }
.metric strong { font-size:1.8rem; display:block; line-height:1.25; font-variant-numeric:tabular-nums; }
.metric span { font-size:.82rem; color:var(--muted); }
.tags { display:flex; flex-wrap:wrap; gap:7px; margin:14px 0 0; }
.tag { background:#223551; border:1px solid #3c5875; color:#dce8f5; border-radius:99px; padding:3px 11px; font-size:.8rem; }
.check { background:var(--panel2); border:1px solid var(--line); border-radius:11px; margin:8px 0; }
summary { padding:12px 15px; cursor:pointer; display:flex; align-items:center; gap:12px; list-style:none; }
summary::-webkit-details-marker { display:none; }
summary::before { content:"▸"; font-size:.85rem; color:var(--muted); }
details[open] summary::before { content:"▾"; }
summary .name { flex:1; overflow-wrap:anywhere; font-weight:620; }
.chip { border:1px solid currentColor; border-radius:7px; padding:1px 8px; font-size:.72rem; font-weight:800; letter-spacing:.02em; white-space:nowrap; }
.chip.pass { color:#6ce2b5; }.chip.fail { color:#ff9b9f; }
.chip.blocked { color:#ffd18b; }.chip.warn { color:#ffd18b; }
.chip.pending { color:#b9c5d5; }.chip.info { color:#acd1f8; }
.detail { padding:3px 17px 15px 35px; color:var(--muted); font-size:.9rem; overflow-wrap:anywhere; }
.detail p { margin:6px 0; }
code { font-family:ui-monospace,SFMono-Regular,Consolas,monospace; overflow-wrap:anywhere; }
.notice { border-left:3px solid #ffc37b; padding:10px 15px; background:#312b28; color:#ffe1b9; border-radius:4px; }
small { color:var(--muted); } footer { margin-top:28px; font-size:.83rem; color:var(--muted); }
@media(max-width:680px) { main { padding-top:25px; } .grid { grid-template-columns:repeat(2,minmax(0,1fr)); }
  .panel { padding:16px; } summary { padding:11px; } .detail { padding:5px 12px 15px 22px; } }
@media print { :root { color-scheme: light; --bg:#fff; --panel:#fff; --panel2:#f5f7fa;
  --line:#aaa; --muted:#555; --text:#111; } body { background:white; }
  main { width:100%; padding:0; } details { break-inside:avoid; } }
"""


class ReportError(ValueError):
    """Unsupported or structurally invalid report. No output should be written."""


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def need_mapping(value: Any, name: str) -> dict:
    if not isinstance(value, dict):
        raise ReportError(f"{name} must be an object")
    return value


def status_chip(status: str) -> str:
    if status not in STATUS_STYLE:
        raise ReportError("unsupported check status")
    return f'<span class="chip {STATUS_STYLE[status]}">{esc(status)}</span>'


def detect_kind(raw: dict, kind: str) -> str:
    if kind != "auto":
        return kind
    if "project" in raw and "source_state" in raw:
        return "verification-run"
    if "mode" in raw and "behavioral_validation" in raw:
        return "local-validation"
    raise ReportError("unknown input contract; set --kind only for supported formats")


def from_portable(raw: dict) -> dict:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise ReportError("jsonschema required for verification-run schema checking") from exc
    schema = json.loads((ROOT / "Schemas/verification-run.schema.json").read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(raw),
                    key=lambda x: str(x.path))
    if errors:
        raise ReportError(f"verification-run schema rejected input: {errors[0].message}")

    src = raw["source_state"]
    if src["kind"] == "git-clean":
        state = "Git revision " + src["revision"]
    elif src["kind"] == "git-dirty":
        state = "Git revision " + src["revision"] + " · uncommitted snapshot " + src["content_sha256"][:16]
    elif src["kind"] == "snapshot":
        state = "Snapshot " + src["content_sha256"][:16]
    else:
        state = "Source state unavailable"
    checks = []
    for c in raw["checks"]:
        checks.append({
            "name": c["id"], "status": c["status"], "code": c["type"],
            "meta": f'{c["tool"]} · {c["selection"]} · required={c["required_for_claim"]}',
            "reason": c.get("reason", ""), "command": c.get("command_display", ""),
            "evidence": c["evidence_refs"], "skipped": c["skipped"],
        })
    env = raw["environment"]
    return {
        "heading": raw["project"]["name"], "subtitle": raw["task"],
        "kind": "verification-run v1", "source": state,
        "environment": f'{env["location"]} · {env["os"]} · {env["runtime"]}',
        "overall": None,
        "interpretation": "Einzelprüfungen; der Vertrag enthält bewusst keine Gesamtfreigabe.",
        "checks": checks, "findings": [],
        "limits": ["Schema-konform bedeutet nicht unabhängig nachgewiesen.",
                   "Die Prüfung von Ausführung und Source-Digest ist Aufgabe des jeweiligen Adapters.",
                   "Keine automatische Freigabe und kein Nachweis einer Behavioral-Evaluation."],
    }


def from_local(raw: dict) -> dict:
    if raw.get("schema_version") != 1:
        raise ReportError("unsupported local-validation schema version")
    if raw.get("overall") not in ("PASS", "FAIL"):
        raise ReportError("invalid local-validation overall status")
    exit_code = raw.get("exit_code")
    if type(exit_code) is not int or exit_code not in (0, 1, 2):
        raise ReportError("invalid local-validation exit code")
    if (exit_code == 0) != (raw["overall"] == "PASS"):
        raise ReportError("inconsistent local-validation overall and exit code")
    if not isinstance(raw.get("checks"), list) or not raw["checks"]:
        raise ReportError("local-validation checks must be a nonempty list")
    if not isinstance(raw.get("findings"), list):
        raise ReportError("local-validation findings must be a list")
    if not isinstance(raw.get("mode"), str):
        raise ReportError("local-validation mode missing")
    checks = []
    for c in raw["checks"]:
        need_mapping(c, "local check")
        if not isinstance(c.get("name"), str) or c.get("status") not in LOCAL_STATUSES:
            raise ReportError("invalid local-validation check")
        if c["status"] == "FAIL" and raw["overall"] == "PASS":
            raise ReportError("local overall PASS contradicts a failed check")
        checks.append({
            "name": c["name"], "status": c["status"], "code": c.get("code") or "",
            "meta": f'mode {raw["mode"]}', "reason": c.get("message") or "",
            "command": "", "evidence": [], "skipped": 0,
        })
    findings = []
    for f in raw["findings"]:
        need_mapping(f, "local finding")
        if f.get("severity") not in LOCAL_SEVERITIES or not isinstance(f.get("code"), str):
            raise ReportError("invalid local-validation finding")
        findings.append({"severity": f["severity"], "code": f["code"],
                         "message": f.get("message") or "", "path": f.get("path") or ""})
    if raw["overall"] == "PASS" and any(f["severity"] == "error" for f in findings):
        raise ReportError("local overall PASS contradicts an error finding")
    behavior = raw.get("behavioral_validation", "UNVERIFIED")
    if behavior not in ("NOT RUN", "NOT_RUN", "UNVERIFIED"):
        raise ReportError("unsupported local behavioral validation marker")
    checks.append({"name": "Behavioral validation", "status": behavior, "code": "",
                   "meta": "Separate behavioral evals, not executed by local validation",
                   "reason": "", "command": "", "evidence": [], "skipped": 0})
    return {
        "heading": "KI-Regeln · Local Validation", "subtitle": f'Modus: {raw["mode"]}',
        "kind": "local-validation v1",
        "source": f'HEAD {raw.get("repository_head") or "unknown"}; uncommitted state not fingerprinted',
        "environment": "Windows / lokale portable Validierungsumgebung (laut Harness)",
        "overall": raw["overall"],
        "interpretation": "Vom lokalen Harness gemeldetes Strukturprüfungsergebnis, keine allgemeine Software- oder Agentenfreigabe.",
        "checks": checks, "findings": findings,
        "limits": ["Behavioral-Evals werden vom lokalen Validation Harness nicht ausgeführt.",
                   "Ein Git-HEAD allein bindet keine uncommitteten Änderungen.",
                   "Dieser Renderer ruft keine Prüfwerkzeuge auf."],
    }


def render_html(view: dict, include_messages: bool = False) -> str:
    """No script, assets, external links, log blobs, or inferred verdicts."""
    counts = Counter(c["status"] for c in view["checks"])
    pass_count = counts["PASS"]
    fail_count = counts["FAIL"]
    gap_count = sum(counts[s] for s in ("NOT RUN", "NOT_RUN", "BLOCKED", "UNVERIFIED", "SKIP"))
    warn_count = counts["WARN"]
    overall = view["overall"]
    if overall is None:
        headline = "Keine Gesamtfreigabe abgeleitet"
        cls = "pending"
    else:
        headline = f'Strukturprüfung laut Harness: {overall}'
        cls = STATUS_STYLE[overall]

    check_cards = []
    for c in view["checks"]:
        detail = [f'<p>{esc(c["meta"])}</p>']
        if c["code"]:
            detail.append(f'<p>Code / Typ: <code>{esc(c["code"])}</code></p>')
        if c["skipped"]:
            detail.append(f'<p>Übersprungen: {c["skipped"]}</p>')
        if c["evidence"]:
            detail.append(f'<p>Evidence-Referenzen: {len(c["evidence"])} (Pfade standardmäßig ausgeblendet)</p>')
        if include_messages:
            if c["reason"]:
                detail.append(f'<p>Begründung / Meldung: {esc(c["reason"])}</p>')
            if c["command"]:
                detail.append(f'<p>Befehl: <code>{esc(c["command"])}</code></p>')
            if c["evidence"]:
                detail.append(f'<p>Referenzen: {esc("; ".join(c["evidence"]))}</p>')
        check_cards.append(
            f'<details class="check"><summary><span class="name">{esc(c["name"])}</span>'
            f'{status_chip(c["status"])}</summary><div class="detail">{"".join(detail)}</div></details>'
        )

    findings = []
    for f in view["findings"]:
        info = f'<p>Severity: {esc(f["severity"])}</p>'
        if include_messages:
            info += f'<p>{esc(f["message"])}</p>'
            if f["path"]:
                info += f'<p>Pfad: <code>{esc(f["path"])}</code></p>'
        findings.append(
            f'<details class="check"><summary><span class="name">{esc(f["code"])}</span>'
            f'<span class="chip { "fail" if f["severity"]=="error" else "warn" if f["severity"]=="warning" else "info" }">'
            f'{esc(f["severity"].upper())}</span></summary><div class="detail">{info}</div></details>'
        )

    limit_items = "".join(f'<li>{esc(v)}</li>' for v in view["limits"])
    find_section = (f'<section class="panel"><h2>Findings ({len(findings)})</h2>{"".join(findings)}</section>'
                    if findings else "")
    privacy = ("Detailmeldungen und Referenzen eingeblendet: vor Weitergabe auf sensible Inhalte prüfen."
               if include_messages else
               "Datensparsame Ansicht: Meldungstexte, Befehle und Evidenzpfade sind ausgeblendet.")
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; connect-src 'none'">
<title>{esc(view["heading"])} – Prüfbericht</title>
<style>{CSS}</style>
</head>
<body>
<main>
<p class="eyebrow">KI-Regeln · Evidence Viewer · Offline</p>
<h1>{esc(view["heading"])}</h1>
<p class="lead">{esc(view["subtitle"])}</p>
<section class="panel hero {cls}" aria-label="Prüfstatus">
<p class="eyebrow">Prüfstand</p>
<h2>{esc(headline)}</h2>
<p class="muted">{esc(view["interpretation"])}</p>
<div class="tags"><span class="tag">{esc(view["kind"])}</span>
<span class="tag">{esc(view["environment"])}</span></div>
</section>
<div class="grid" aria-label="Statusanzahlen">
<div class="metric"><strong>{pass_count}</strong><span>PASS-Checks</span></div>
<div class="metric"><strong>{fail_count}</strong><span>FAIL-Checks</span></div>
<div class="metric"><strong>{gap_count}</strong><span>Offen / nicht ausgeführt</span></div>
<div class="metric"><strong>{warn_count}</strong><span>Warnungen</span></div>
</div>
<section class="panel">
<h2>Geprüfter Quellzustand</h2>
<p><code>{esc(view["source"])}</code></p>
</section>
<section class="panel" aria-label="Einzelprüfungen">
<h2>Prüfungen ({len(view["checks"])})</h2>
<p class="muted">Details über die jeweilige Zeile öffnen. Statuswerte werden unverändert aus dem Bericht übernommen.</p>
{"".join(check_cards)}
</section>
{find_section}
<section class="panel">
<h2>Grenzen der Aussage</h2>
<ul>{limit_items}</ul>
<p class="notice">{esc(privacy)}</p>
</section>
<footer>Statische Darstellung vorhandener Evidence. Keine Testausführung, kein semantisches Urteil,
kein unabhängiger Security-Review und keine Release-Freigabe. Keine externen Ressourcen.</footer>
</main>
</body>
</html>
"""


def render_report(raw: dict, kind: str = "auto", include_messages: bool = False) -> str:
    need_mapping(raw, "report")
    resolved = detect_kind(raw, kind)
    if resolved == "verification-run":
        view = from_portable(raw)
    elif resolved == "local-validation":
        view = from_local(raw)
    else:
        raise ReportError("unsupported input kind")
    return render_html(view, include_messages=include_messages)


def write_atomic(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=path.parent, prefix=".report-", suffix=".tmp",
                                         delete=False) as f:
            temp = Path(f.name)
            f.write(data)
        os.replace(temp, path)
    finally:
        if temp is not None and temp.exists():
            temp.unlink()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Existing JSON report")
    parser.add_argument("--output", required=True, type=Path, help="Standalone HTML destination")
    parser.add_argument("--kind", choices=["auto", "verification-run", "local-validation"],
                        default="auto")
    parser.add_argument("--include-messages", action="store_true",
                        help="Display untrusted messages/commands/paths (review before sharing)")
    args = parser.parse_args(argv)
    try:
        if args.input.resolve() == args.output.resolve():
            raise ReportError("input and output must be distinct")
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        html_doc = render_report(raw, args.kind, args.include_messages)
        write_atomic(args.output, html_doc)
    except (ReportError, OSError, ValueError) as exc:
        parser.exit(2, f"HTML report not generated: {exc}\n")
    print(f"HTML report created: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
