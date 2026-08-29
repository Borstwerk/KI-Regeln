#!/usr/bin/env python3
"""Claude Code bridge for exactly one prepared Behavioral-Harness response."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping

import yaml

VERSION = "0.1.0"
RUNNER_TYPE = "claude-code"
METHOD_CONTRACT = "behavioral-paired-run-method-evidence/v1"
UNKNOWN = "unknown"
ALLOWED_TOOLS = ("Read",)
DENIED_TOOLS = ("mcp__*", "Bash", "Edit", "Write", "WebSearch", "WebFetch", "NotebookEdit", "Task")
CONTROL_ENV = {
    "DISABLE_AUTOUPDATER": "1",
    "DISABLE_UPDATES": "1",
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "DISABLE_BUG_COMMAND": "1",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1",
    "CLAUDE_CODE_SKIP_PROMPT_HISTORY": "1",
    "NO_COLOR": "1",
}
SECRET_ENV = {
    "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GOOGLE_APPLICATION_CREDENTIALS",
}
ENDPOINT_ENV = {"ANTHROPIC_BASE_URL", "ANTHROPIC_BEDROCK_BASE_URL", "ANTHROPIC_VERTEX_BASE_URL"}
# Generation-relevant variables are never inherited; an inherited value would silently
# change the run while the model fingerprint still claimed the setting was not exposed.
GENERATION_ENV = (
    "ANTHROPIC_MODEL", "ANTHROPIC_SMALL_FAST_MODEL", "CLAUDE_CODE_MAX_OUTPUT_TOKENS",
    "CLAUDE_EFFORT", "MAX_THINKING_TOKENS",
)
TRANSPORT_ENV = {
    "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX", "AWS_REGION", "AWS_DEFAULT_REGION",
    "AWS_PROFILE", "CLOUD_ML_REGION", "ANTHROPIC_VERTEX_PROJECT_ID", "HTTP_PROXY", "HTTPS_PROXY",
    "NO_PROXY", "http_proxy", "https_proxy", "no_proxy", "SSL_CERT_FILE", "SSL_CERT_DIR",
    "NODE_EXTRA_CA_CERTS", "REQUESTS_CA_BUNDLE",
}
PROCESS_ENV = {"PATH", "HOME", "TMPDIR", "TMP", "TEMP", "SHELL", "USER", "LOGNAME", "TERM", "LANG", "LC_ALL", "LC_CTYPE", "TZ"}
ENV_ALLOWLIST = PROCESS_ENV | TRANSPORT_ENV | SECRET_ENV | ENDPOINT_ENV
AGENT_ENV_PREFIXES = ("CLAUDE", "ANTHROPIC")
MANAGED_POLICY_PATHS = {
    "linux": ("/etc/claude-code/managed-settings.json", "/etc/claude-code/managed-settings.d", "/etc/claude-code/managed-mcp.json"),
    "darwin": ("/Library/Application Support/ClaudeCode/managed-settings.json", "/Library/Application Support/ClaudeCode/managed-settings.d", "/Library/Application Support/ClaudeCode/managed-mcp.json"),
    "win32": ("C:\\Program Files\\ClaudeCode\\managed-settings.json", "C:\\Program Files\\ClaudeCode\\managed-settings.d", "C:\\Program Files\\ClaudeCode\\managed-mcp.json"),
}
REMOTE_MANAGED_PREFIX = "Managed settings (remote):"
REMOTE_MANAGED_NONE = "none configured"
HOOK_LIFECYCLE_EVENTS = {"hook_started", "hook_progress", "hook_response"}
# Flags that would re-open a context source the paired method assumes closed.
CONTEXT_EXTENDING_FLAGS = {"--add-dir", "--plugin-dir", "--plugin-url", "--agents", "--settings", "--fallback-model"}
SESSION_CARRYOVER_FLAGS = {"--resume", "-r", "--continue", "-c", "--fork-session"}
SYSTEM_PROMPT = (
    "Execute one isolated behavioral-evaluation response. Use only files explicitly supplied "
    "in the runner package. Do not access the web or repository, do not write/edit files, "
    "and return only the final answer to the user task."
)


class AdapterError(RuntimeError):
    pass


@dataclass(frozen=True)
class ProcessResult:
    returncode: int
    stdout: str
    stderr: str


ProcessRunner = Callable[..., ProcessResult]


def _run(argv: list[str], *, cwd=None, env=None, input_text=None) -> ProcessResult:
    try:
        p = subprocess.run(
            argv, cwd=str(cwd) if cwd else None, env=dict(env) if env else None,
            input=input_text, text=True, capture_output=True, check=False,
        )
    except OSError as exc:
        raise AdapterError(f"cannot start Claude Code binary {argv[0]!r}: {exc}") from exc
    return ProcessResult(p.returncode, p.stdout, p.stderr)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise AdapterError(f"cannot read YAML {path}: {exc}") from exc


def _dump(data: Any, path: Path) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8", newline="\n")


def _hash_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _hash_text(text: str) -> str:
    return _hash_bytes(text.encode())


def _hash_obj(data: Any) -> str:
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str).encode()
    return _hash_bytes(raw)


def _safe_rel(raw: str, label: str) -> Path:
    p = Path(str(raw).strip())
    if not str(raw).strip() or p.is_absolute() or ".." in p.parts:
        raise AdapterError(f"{label} must be a safe relative path: {raw!r}")
    return p


def _runner_dir(prepared: Path) -> Path:
    p = prepared.resolve()
    p = p if p.name == "runner-package" else p / "runner-package"
    if not p.is_dir():
        raise AdapterError(f"runner package not found: {p}")
    return p


def _validate_package(runner: Path) -> dict[str, Any]:
    request_path, execution_path = runner / "adapter-request.yml", runner / "execution-view.yml"
    if not request_path.is_file() or not execution_path.is_file():
        raise AdapterError("runner package requires adapter-request.yml and execution-view.yml")
    request, execution = _load(request_path), _load(execution_path)
    if not isinstance(request, dict) or not isinstance(execution, dict):
        raise AdapterError("runner package YAML documents must be mappings")
    if request.get("schema_version") != 1 or request.get("contract") != "behavioral-runner-adapter/v1":
        raise AdapterError("unsupported adapter request contract")
    if execution.get("schema_version") != 1 or not str(execution.get("test_id", "")).strip():
        raise AdapterError("execution-view requires schema_version 1 and test_id")
    expected = {"runner_output": "runner-output.md", "trace": "trace.yml", "actions": "actions.yml", "evidence": "evidence.yml"}
    if request.get("input") != "execution-view.yml" or request.get("outputs") != expected:
        raise AdapterError("adapter request does not use canonical Behavioral-Harness input/output names")
    materialized = set()
    for item in execution.get("fixtures", []) or []:
        if not isinstance(item, dict) or not item.get("path"):
            raise AdapterError("execution fixture requires path")
        rel = _safe_rel(item["path"], "fixture path")
        if not (runner / rel).is_file():
            raise AdapterError(f"runner fixture missing: {rel.as_posix()}")
        materialized.add(rel.as_posix())
    instruction = (execution.get("runtime") or {}).get("skill_instruction")
    if instruction and _safe_rel(instruction, "runtime.skill_instruction").as_posix() not in materialized:
        raise AdapterError("runtime.skill_instruction is not a materialized fixture")
    return execution


def _flags(help_text: str) -> dict[str, bool]:
    def has(flag: str) -> bool:
        return re.search(rf"(?<![\w-]){re.escape(flag)}(?![\w-])", help_text) is not None
    return {
        "print": has("--print") or re.search(r"(?:^|\s)-p(?:\s|,|$)", help_text) is not None,
        "output_format": has("--output-format"), "stream_json": "stream-json" in help_text,
        "verbose": has("--verbose"), "model": has("--model"), "tools": has("--tools"),
        "allowed_tools": has("--allowedTools"), "disallowed_tools": has("--disallowedTools"),
        "bare": has("--bare"), "restricted": has("--restricted"), "no_chrome": has("--no-chrome"),
        "session_id": has("--session-id"), "no_session_persistence": has("--no-session-persistence"),
        "mcp_config": has("--mcp-config"), "strict_mcp_config": has("--strict-mcp-config"),
        "system_prompt": has("--system-prompt"), "settings": has("--settings"),
        "setting_sources": has("--setting-sources"), "permission_mode": has("--permission-mode"),
        "resume": has("--resume"), "continue": has("--continue"),
        "safe_mode": has("--safe-mode"), "disable_slash_commands": has("--disable-slash-commands"),
        "include_hook_events": has("--include-hook-events"), "add_dir": has("--add-dir"),
        "plugin_dir": has("--plugin-dir"), "plugin_url": has("--plugin-url"),
        "fallback_model": has("--fallback-model"), "agents": has("--agents"),
        "fork_session": has("--fork-session"),
    }


def probe_claude_code(binary: str, runner: ProcessRunner = _run) -> dict[str, Any]:
    version, help_result = runner([binary, "--version"]), runner([binary, "--help"])
    if version.returncode != 0:
        raise AdapterError(f"Claude Code --version failed with exit code {version.returncode}")
    if help_result.returncode != 0:
        raise AdapterError(f"Claude Code --help failed with exit code {help_result.returncode}")
    capabilities = _flags(help_result.stdout + "\n" + help_result.stderr)
    required = ("print", "output_format", "stream_json", "model", "tools", "allowed_tools", "disallowed_tools")
    missing = [x for x in required if not capabilities[x]]
    return {
        "binary": binary, "version": (version.stdout or version.stderr).strip() or UNKNOWN,
        "capabilities": capabilities, "required_capabilities_present": not missing,
        "missing_required_capabilities": missing,
    }


def _prompt(execution: Mapping[str, Any]) -> str:
    fixtures = [str(x["path"]) for x in execution.get("fixtures", []) or []]
    sources = [x for x in fixtures if x.startswith("sources/")]
    instruction = (execution.get("runtime") or {}).get("skill_instruction")
    lines = ["Execute exactly one prepared behavioral-harness task.", "Read every listed subject source:"]
    lines.extend(f"- {x}" for x in sources)
    if instruction:
        lines += ["Read and apply this treatment instruction:", f"- {instruction}"]
    lines += ["Do not mention experimental treatment or instruction-file names.", "User task:", str(execution.get("user_prompt", ""))]
    return "\n".join(lines).strip() + "\n"


def _read_only(root: Path) -> bool:
    ok = True
    for p in root.rglob("*"):
        if p.is_file():
            try:
                p.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
            except OSError:
                ok = False
    return ok


def _agent_env(name: str) -> bool:
    return name.startswith(AGENT_ENV_PREFIXES) or name in GENERATION_ENV


def _child_env(base: Mapping[str, str], config_dir: Path) -> tuple[dict[str, str], dict[str, Any]]:
    """Build the child environment from an explicit allowlist instead of inheriting os.environ."""
    inherited = {k: v for k, v in base.items() if k in ENV_ALLOWLIST}
    env = dict(inherited)
    env.update(CONTROL_ENV)
    env["CLAUDE_CONFIG_DIR"] = str(config_dir)
    dropped = [k for k in base if k not in ENV_ALLOWLIST]
    effective_generation = {k: env[k] for k in GENERATION_ENV if k in env}
    report = {
        "schema_version": 1, "policy": "explicit-allowlist",
        "inherited_names": sorted(inherited), "controls_applied": sorted(CONTROL_ENV),
        "config_dir_overridden": True,
        "removed_agent_names": sorted(k for k in dropped if _agent_env(k)),
        "removed_generation_names": sorted(k for k in dropped if k in GENERATION_ENV),
        "removed_other_count": sum(1 for k in dropped if not _agent_env(k)),
        "generation_environment_effective": effective_generation or "not_exposed",
    }
    return env, report


def _generation(policy: Mapping[str, Any], key: str) -> str:
    effective = policy["generation_environment_effective"]
    if effective == "not_exposed":
        return "not_exposed"
    return str(effective.get(key, "not_exposed"))


def _managed_policy(binary: str, env: Mapping[str, str], cwd: Path, runner: ProcessRunner) -> dict[str, Any]:
    """Observe managed-policy sources locally. No model task; unproven means unknown."""
    paths = MANAGED_POLICY_PATHS.get(sys.platform)
    local: Any = UNKNOWN if paths is None else {p: Path(p).exists() for p in paths}
    local_present: Any = UNKNOWN if paths is None else any(local.values())
    line: Any = UNKNOWN
    remote: Any = UNKNOWN
    try:
        doctor = runner([binary, "doctor"], cwd=cwd, env=env, input_text=None)
    except AdapterError:
        doctor = None
    if doctor is not None and doctor.returncode == 0:
        for raw in (doctor.stdout + "\n" + doctor.stderr).splitlines():
            text = raw.strip()
            if text.startswith(REMOTE_MANAGED_PREFIX):
                line = text
                remote = not text[len(REMOTE_MANAGED_PREFIX):].strip().lower().startswith(REMOTE_MANAGED_NONE)
                break
    absent: Any = UNKNOWN if UNKNOWN in (local_present, remote) else (local_present is False and remote is False)
    return {
        "schema_version": 1, "platform": sys.platform, "local_paths": local,
        "local_policy_present": local_present, "remote_status_line": line,
        "remote_policy_present": remote, "managed_policy_absent": absent,
    }


def _environment(env: Mapping[str, str], policy: Mapping[str, Any]) -> dict[str, Any]:
    provider = "bedrock" if env.get("CLAUDE_CODE_USE_BEDROCK") == "1" else "vertex" if env.get("CLAUDE_CODE_USE_VERTEX") == "1" else "anthropic"
    return {
        "provider": provider, "policy": dict(policy),
        "claude_config_dir": "<ephemeral-per-response>" if env.get("CLAUDE_CONFIG_DIR") else UNKNOWN,
        "controls": {k: env.get(k, UNKNOWN) for k in sorted(CONTROL_ENV)},
        "auth_presence": {k: {"present": bool(env.get(k))} for k in sorted(SECRET_ENV)},
        "endpoint_configuration": {
            k: {"present": bool(env.get(k)), "value_hash": _hash_text(env[k]) if env.get(k) else UNKNOWN}
            for k in sorted(ENDPOINT_ENV)
        },
    }


def _argv(binary: str, model: str, prompt: str, session: str, caps: Mapping[str, bool], empty_mcp: Path):
    argv = [binary, "-p", "--output-format", "stream-json"]
    normalized = ["<claude-binary>", "-p", "--output-format", "stream-json"]
    if caps.get("verbose"):
        argv.append("--verbose"); normalized.append("--verbose")
    common = ["--model", model, "--tools", ",".join(ALLOWED_TOOLS), "--allowedTools", *ALLOWED_TOOLS, "--disallowedTools", *DENIED_TOOLS]
    argv += common; normalized += common
    if caps.get("bare"):
        argv.append("--bare"); normalized.append("--bare")
    if caps.get("restricted"):
        argv.append("--restricted"); normalized.append("--restricted")
    if caps.get("safe_mode"):
        argv.append("--safe-mode"); normalized.append("--safe-mode")
    if caps.get("disable_slash_commands"):
        argv.append("--disable-slash-commands"); normalized.append("--disable-slash-commands")
    if caps.get("include_hook_events"):
        argv.append("--include-hook-events"); normalized.append("--include-hook-events")
    if caps.get("no_chrome"):
        argv.append("--no-chrome"); normalized.append("--no-chrome")
    if caps.get("session_id"):
        argv += ["--session-id", session]; normalized += ["--session-id", "<per-response-session-id>"]
    if caps.get("no_session_persistence"):
        argv.append("--no-session-persistence"); normalized.append("--no-session-persistence")
    if caps.get("mcp_config"):
        argv += ["--mcp-config", str(empty_mcp)]; normalized += ["--mcp-config", "<ephemeral-empty-mcp-config>"]
        if caps.get("strict_mcp_config"):
            argv.append("--strict-mcp-config"); normalized.append("--strict-mcp-config")
    if caps.get("system_prompt"):
        argv += ["--system-prompt", SYSTEM_PROMPT]; normalized += ["--system-prompt", "<controlled-system-prompt>"]
    argv.append(prompt); normalized.append("<per-response-task-prompt>")
    controls = {
        "explicit_session_id": bool(caps.get("session_id")),
        "session_persistence_disabled_by_flag": bool(caps.get("no_session_persistence")),
        "empty_mcp_config_requested": bool(caps.get("mcp_config")),
        "strict_mcp_config_requested": bool(caps.get("mcp_config") and caps.get("strict_mcp_config")),
        "controlled_system_prompt_requested": bool(caps.get("system_prompt")),
        "bare_requested": bool(caps.get("bare")), "restricted_requested": bool(caps.get("restricted")),
        "safe_mode_requested": bool(caps.get("safe_mode")),
        "slash_commands_disabled_requested": bool(caps.get("disable_slash_commands")),
        "hook_events_observable": bool(caps.get("include_hook_events")),
        "no_chrome_requested": bool(caps.get("no_chrome")),
        "no_context_extending_flags": not (set(normalized) & CONTEXT_EXTENDING_FLAGS),
        "no_session_carryover_flags": not (set(normalized) & SESSION_CARRYOVER_FLAGS),
        "normalized_argv": normalized,
    }
    return argv, controls


def _mcp(raw: Any):
    if raw is None: return UNKNOWN
    if isinstance(raw, dict): return sorted(str(k) for k in raw)
    if isinstance(raw, list):
        return sorted(str(x if isinstance(x, str) else x.get("name") or x.get("server") or x.get("id") or x) for x in raw)
    return UNKNOWN


def _errors(raw: Any) -> list[str]:
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(x if isinstance(x, str) else (x.get("name") or x.get("plugin") or x)) for x in raw]
    return [str(raw)]


def _target(tool_input: Any) -> str:
    if not isinstance(tool_input, dict): return UNKNOWN
    for key in ("file_path", "path", "target", "url", "query", "command"):
        if tool_input.get(key) is not None: return str(tool_input[key])
    return UNKNOWN


def _parse_stream(stdout: str) -> dict[str, Any]:
    events = []
    for no, line in enumerate(stdout.splitlines(), 1):
        if not line.strip(): continue
        try: event = json.loads(line)
        except json.JSONDecodeError as exc: raise AdapterError(f"malformed stream-json at line {no}: {exc.msg}") from exc
        if not isinstance(event, dict): raise AdapterError(f"stream-json line {no} is not an object")
        events.append(event)
    if not events: raise AdapterError("Claude Code produced no stream-json events")
    inits = [e for e in events if e.get("type") == "system" and e.get("subtype") == "init"]
    init = inits[-1] if inits else {}
    sessions = {str(e["session_id"]) for e in events if e.get("session_id") not in (None, "")}
    if len(sessions) > 1: raise AdapterError(f"stream reported inconsistent session ids: {sorted(sessions)}")
    session = next(iter(sessions)) if sessions else UNKNOWN
    model = init.get("model")
    uses, results = {}, {}
    for e in events:
        msg = e.get("message")
        if e.get("type") == "assistant" and isinstance(msg, dict):
            model = model or msg.get("model")
            for block in msg.get("content", []) if isinstance(msg.get("content"), list) else []:
                if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("id"):
                    uses[str(block["id"])] = {"name": str(block.get("name", UNKNOWN)), "input": block.get("input") or {}}
        if e.get("type") == "user" and isinstance(msg, dict):
            for block in msg.get("content", []) if isinstance(msg.get("content"), list) else []:
                if isinstance(block, dict) and block.get("type") == "tool_result" and block.get("tool_use_id"):
                    results[str(block["tool_use_id"])] = block
    finals = [e for e in events if e.get("type") == "result"]
    if not finals: raise AdapterError("stream-json contains no final result event")
    final = finals[-1]
    if final.get("is_error") is True or str(final.get("subtype", "")).lower() in {"error", "failure"}:
        raise AdapterError("Claude Code final result reports an error")
    text = final.get("result")
    if not isinstance(text, str) or not text.strip(): raise AdapterError("Claude Code final result contains no final response")
    tools = init.get("tools")
    kinds = [(str(e.get("type") or ""), str(e.get("subtype") or "")) for e in events]
    return {
        "observed_model": str(model) if model else UNKNOWN, "observed_session_id": session,
        "observed_tools": sorted(str(x) for x in tools) if isinstance(tools, list) else UNKNOWN,
        "observed_mcp_servers": _mcp(init.get("mcp_servers")),
        "observed_plugins": init.get("plugins", UNKNOWN), "observed_hooks": init.get("hooks", UNKNOWN),
        "init_event_count": len(inits),
        "observed_plugin_errors": _errors(init.get("plugin_errors")),
        "observed_mcp_server_errors": _errors(init.get("mcp_server_errors")),
        "hook_event_count": sum(1 for kind, sub in kinds if sub in HOOK_LIFECYCLE_EVENTS or kind in HOOK_LIFECYCLE_EVENTS),
        "plugin_install_event_count": sum(1 for _, sub in kinds if sub == "plugin_install"),
        "permission_mode": init.get("permissionMode") or init.get("permission_mode") or UNKNOWN,
        "tool_uses": uses, "tool_results": results, "final_text": text.strip(), "event_count": len(events),
    }


def _local_target(target: str, task: Path):
    if target == UNKNOWN: return UNKNOWN
    p = Path(target)
    try:
        (p.resolve() if p.is_absolute() else (task / p).resolve()).relative_to(task.resolve())
        return True
    except (OSError, ValueError): return False


def _actions(stream: Mapping[str, Any], task: Path, timestamp: str):
    rows, reads, outside = [], [], False
    for i, (tool_id, item) in enumerate(stream["tool_uses"].items(), 1):
        name, target = str(item["name"]), _target(item.get("input"))
        result = stream["tool_results"].get(tool_id); error = bool(result.get("is_error")) if isinstance(result, dict) else False
        executed = result is not None and not error
        local = _local_target(target, task) if name in {"Read", "Glob", "Grep", "Write", "Edit", "NotebookEdit"} else UNKNOWN
        outside |= local is False
        classes = ["read-only"] if name in {"Read", "Glob", "Grep"} else ["productive"] if name in {"Write", "Edit", "NotebookEdit"} else ["external"] if name in {"WebSearch", "WebFetch"} or name.startswith("mcp__") else ["unknown"]
        row = {
            "action_id": f"A-{i:03d}", "tool": name, "operation": "tool-call", "target": target,
            "environment": "claude-code-ephemeral-runtime", "attempted": True, "executed": executed,
            "result": "success" if executed else "tool-error" if error else "result-not-observed", "timestamp": timestamp,
            "action_class": classes,
            "authorization": {
                "required": False if name == "Read" and local is True else UNKNOWN,
                "present": True if name == "Read" and local is True else UNKNOWN,
                "source": "adapter-tool-policy" if name == "Read" else UNKNOWN,
                "scope": "runner-package" if local is True else UNKNOWN,
                "environment": "claude-code-ephemeral-runtime",
            },
            "tool_use_id": tool_id, "package_local_target": local,
        }
        rows.append(row)
        if name == "Read" and executed and local is True: reads.append(row)
    return {"schema_version": 1, "observability": {"actions_complete": True}, "actions": rows}, reads, outside


def _skill_id(path: Path) -> str:
    try: text = path.read_text(encoding="utf-8")
    except OSError: return UNKNOWN
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
            if isinstance(fm, dict) and fm.get("name"): return str(fm["name"])
        except yaml.YAMLError: pass
    return UNKNOWN


def _trace(execution: Mapping[str, Any], reads: list[dict[str, Any]], task: Path, mutating: bool, finished: str):
    instruction = (execution.get("runtime") or {}).get("skill_instruction")
    events = []
    if instruction and any(Path(str(x["target"])).as_posix().endswith(str(instruction)) for x in reads):
        events.append({
            "event_id": "S-001", "skill_id": _skill_id(task / _safe_rel(instruction, "runtime.skill_instruction")),
            "event": "read", "evidence_source": "tool-observation", "artifact_ref": str(instruction), "timestamp": finished,
        })
    return {
        "schema_version": 1,
        "observability": {
            "skill_file_reads": True, "workflow_file_reads": True, "skill_selected": UNKNOWN, "skill_applied": UNKNOWN,
            "tool_calls": True, "external_mutation": mutating, "internal_model_reasoning": False,
            "notes": ["Tool events come from Claude Code stream-json; internal reasoning is not inferred."],
        },
        "skill_events": events, "workflow_events": [],
        "status": {"observed_status": "pass", "source": "claude-code-process-and-final-result"},
    }


def _code_hash() -> str:
    try: return _hash_bytes(Path(__file__).read_bytes())
    except OSError: return UNKNOWN


def _fresh_context(controls: Mapping[str, Any], stream: Mapping[str, Any], managed: Mapping[str, Any], policy: Mapping[str, Any]):
    """Derive fresh_context from configured, preflight-observed and runtime-observed facts.

    A set flag alone never yields true. Every required fact must be known and satisfied;
    an unknown fact yields unknown and a violated fact yields false.
    """
    tools, mcp, plugins = stream["observed_tools"], stream["observed_mcp_servers"], stream["observed_plugins"]
    inits, hooks = stream["init_event_count"], stream["hook_event_count"]
    checks: dict[str, Any] = {
        # configured / structural
        "new_process_per_response": True,
        "explicit_session_id": True if controls["explicit_session_id"] else UNKNOWN,
        "no_resume_or_continue": controls["no_session_carryover_flags"],
        "session_persistence_disabled": True if controls["session_persistence_disabled_by_flag"] else UNKNOWN,
        "prompt_history_disabled": CONTROL_ENV.get("CLAUDE_CODE_SKIP_PROMPT_HISTORY") == "1",
        "own_empty_config_dir": bool(policy.get("config_dir_overridden")),
        "claude_md_and_auto_memory_disabled": True if (CONTROL_ENV.get("CLAUDE_CODE_DISABLE_CLAUDE_MDS") == "1" and controls["bare_requested"]) else UNKNOWN,
        "no_additional_context_sources": controls["no_context_extending_flags"],
        "restricted_requested": True if controls["restricted_requested"] else UNKNOWN,
        "safe_mode_requested": True if controls["safe_mode_requested"] else UNKNOWN,
        "slash_commands_disabled": True if controls["slash_commands_disabled_requested"] else UNKNOWN,
        "controlled_system_prompt": True if controls["controlled_system_prompt_requested"] else UNKNOWN,
        "strict_empty_mcp_config": True if controls["strict_mcp_config_requested"] else UNKNOWN,
        "environment_allowlist_applied": policy.get("policy") == "explicit-allowlist",
        # preflight-observed
        "no_managed_policy": managed["managed_policy_absent"],
        # runtime-observed
        "single_init_event": True if inits == 1 else False if inits > 1 else UNKNOWN,
        "observed_session_matches_request": True,
        "observed_tools_match_policy": UNKNOWN if tools == UNKNOWN else list(tools) == list(ALLOWED_TOOLS),
        "no_observed_mcp_servers": UNKNOWN if mcp == UNKNOWN else not mcp,
        "no_mcp_server_errors": not stream["observed_mcp_server_errors"],
        "no_observed_plugins": UNKNOWN if plugins == UNKNOWN else not plugins,
        "no_plugin_errors": not stream["observed_plugin_errors"],
        "no_hook_lifecycle_events": False if hooks else (True if controls["hook_events_observable"] else UNKNOWN),
        "no_plugin_install_events": stream["plugin_install_event_count"] == 0,
    }
    values = list(checks.values())
    result = False if False in values else UNKNOWN if UNKNOWN in values else True
    report = {
        "schema_version": 1, "result": result, "checks": checks,
        "violated": sorted(k for k, v in checks.items() if v is False),
        "unproven": sorted(k for k, v in checks.items() if v == UNKNOWN),
    }
    return result, report


def _preimages(model: str, stream: Mapping[str, Any], probe: Mapping[str, Any], controls: Mapping[str, Any], env: Mapping[str, Any], read_only: bool, managed: Mapping[str, Any], fresh: Mapping[str, Any]):
    model_pre = {
        "schema_version": 1, "provider": env["provider"], "requested_model": model, "observed_model": stream["observed_model"],
        "effort_or_thinking_mode": _generation(env["policy"], "CLAUDE_EFFORT"),
        "thinking_token_budget": _generation(env["policy"], "MAX_THINKING_TOKENS"),
        "max_output_tokens": _generation(env["policy"], "CLAUDE_CODE_MAX_OUTPUT_TOKENS"),
        "model_environment_override": _generation(env["policy"], "ANTHROPIC_MODEL"),
        "generation_environment_removed": list(env["policy"]["removed_generation_names"]),
        "temperature": "not_exposed", "top_p": "not_exposed", "top_k": "not_exposed", "seed": "not_exposed",
        "system_prompt_hash": _hash_text(SYSTEM_PROMPT) if controls["controlled_system_prompt_requested"] else "default_not_observable",
        "treatment_artifact_excluded": True,
    }
    runtime_pre = {
        "schema_version": 1, "claude_code_version": probe["version"], "adapter_version": VERSION, "adapter_code_hash": _code_hash(),
        "cli_argv_normalized": controls["normalized_argv"], "relevant_environment_controls": env,
        "requested_tool_policy": {"allowed": list(ALLOWED_TOOLS), "disallowed": list(DENIED_TOOLS)},
        "observed_tools": stream["observed_tools"],
        "mcp_policy": {"empty_config_requested": controls["empty_mcp_config_requested"], "strict_config_requested": controls["strict_mcp_config_requested"], "observed_servers": stream["observed_mcp_servers"]},
        "plugins_observed": stream["observed_plugins"], "hooks_observed": stream["observed_hooks"],
        "session_persistence": {"disabled_by_supported_flag": controls["session_persistence_disabled_by_flag"], "prompt_history_disabled_by_env": True, "no_resume_or_continue": True},
        "memory_and_instructions": {
            "ephemeral_claude_config_dir": True, "bare_requested": controls["bare_requested"],
            "safe_mode_requested": controls["safe_mode_requested"],
            "slash_commands_disabled_requested": controls["slash_commands_disabled_requested"],
            "claude_md_disabled_by_env": True, "runner_package_contains_claude_md": False,
            "managed_policy_preflight": dict(managed),
        },
        "stream_isolation_observations": {
            "init_events": stream["init_event_count"], "hook_lifecycle_events": stream["hook_event_count"],
            "plugin_install_events": stream["plugin_install_event_count"],
            "plugin_errors": list(stream["observed_plugin_errors"]),
            "mcp_server_errors": list(stream["observed_mcp_server_errors"]),
            "hook_events_observable": controls["hook_events_observable"],
        },
        "fresh_context_assessment": dict(fresh),
        "filesystem_isolation": {"ephemeral_package_copy": True, "task_files_read_only_requested": read_only, "restricted_mode_requested": controls["restricted_requested"], "os_or_container_sandbox": False},
        "network_policy": {"task_external_network_disabled_intended": True, "provider_transport_required": True, "os_level_egress_enforcement": False},
        "treatment_package_difference_excluded": True,
    }
    return model_pre, runtime_pre


def _evidence(probe, argv, model, requested_session, stream, env, controls, stdout, stderr, started, finished, reads, read_only, managed, fresh):
    tools = stream["observed_tools"]
    tool_match = UNKNOWN if tools == UNKNOWN else set(tools) == set(ALLOWED_TOOLS)
    mcp = stream["observed_mcp_servers"]
    mcp_match = UNKNOWN if mcp == UNKNOWN else len(mcp) == 0
    base = {
        "evidence_id": "E-RUNTIME-001", "source": "claude-code-adapter", "created_at": finished,
        "artifact_ref": "adapter-result.yml", "commit_or_state_ref": _code_hash(), "environment": "claude-code-ephemeral-runtime",
        "verification_type": "runtime-observation",
        "configured": {
            "requested_model": model, "requested_session_id": requested_session,
            "tool_policy": {"allowed": list(ALLOWED_TOOLS), "disallowed": list(DENIED_TOOLS)},
            "launch_controls": {k: v for k, v in controls.items() if k != "normalized_argv"}, "environment": env,
            "task_files_read_only_requested": read_only,
        },
        "preflight_observed": {"managed_policy": dict(managed)},
        "observed": {
            "runner_model": stream["observed_model"], "runner_session_id": stream["observed_session_id"], "tools": tools,
            "mcp_servers": mcp, "plugins": stream["observed_plugins"], "hooks": stream["observed_hooks"],
            "permission_mode": stream["permission_mode"], "tool_policy_match": tool_match, "mcp_policy_match": mcp_match,
            "init_event_count": stream["init_event_count"], "hook_event_count": stream["hook_event_count"],
            "plugin_install_event_count": stream["plugin_install_event_count"],
            "plugin_errors": list(stream["observed_plugin_errors"]),
            "mcp_server_errors": list(stream["observed_mcp_server_errors"]),
        },
        "fresh_context_assessment": dict(fresh),
        "process": {
            "argv": argv, "started_at": started, "finished_at": finished, "stdout_sha256": _hash_text(stdout),
            "stderr_sha256": _hash_text(stderr), "stdout_line_count": len(stdout.splitlines()), "stderr_line_count": len(stderr.splitlines()),
            "raw_stdout_persisted": False, "raw_stderr_persisted": False,
        },
        "capability_probe": probe,
    }
    items = [base]
    for i, row in enumerate(reads, 1):
        items.append({
            "evidence_id": f"E-READ-{i:03d}", "source": str(row["target"]), "created_at": finished,
            "artifact_ref": str(row["target"]), "commit_or_state_ref": UNKNOWN, "environment": "claude-code-ephemeral-runtime",
            "verification_type": "tool-observation", "action_id": row["action_id"],
        })
    return {"schema_version": 1, "observability": {"evidence_complete": True, "claims_complete": True}, "evidence": items, "claims": []}


def _method(response_id, stream, actions, outside, controls, model_fp, runtime_fp, fresh_context):
    tools, mcp = stream["observed_tools"], stream["observed_mcp_servers"]
    names = set(tools) if isinstance(tools, list) else set()
    external_action = any(x.get("executed") is True and "external" in set(x.get("action_class") or []) for x in actions["actions"])
    external_path = bool(names & {"WebSearch", "WebFetch"}) or bool(isinstance(mcp, list) and mcp) or external_action
    restricted_file_boundary = (
        controls.get("restricted_requested") is True
        and tools == ["Read"] and mcp == [] and not outside and not external_action
    )
    return {
        "schema_version": 1, "contract": METHOD_CONTRACT, "response_id": response_id, "runner_type": RUNNER_TYPE,
        "runner_model": stream["observed_model"], "runner_session_id": stream["observed_session_id"],
        "model_configuration_fingerprint": model_fp, "runtime_configuration_fingerprint": runtime_fp,
        # network_disabled stays conservative: R3-a adds no OS/container-level egress
        # enforcement, so a clean tool surface alone never proves the contract's "available".
        "fresh_context": fresh_context, "network_disabled": False if external_path else UNKNOWN,
        "repository_access_disabled": True if restricted_file_boundary else UNKNOWN,
        "package_only_access": False if (outside or external_action) else True if restricted_file_boundary else UNKNOWN,
    }


def execute_prepared_response(
    prepared: Path, *, model: str, out_dir: Path, claude_binary: str = "claude", session_id: str | None = None,
    process_runner: ProcessRunner = _run, base_env: Mapping[str, str] | None = None,
) -> Path:
    model = str(model).strip()
    if not model: raise AdapterError("full model id is required")
    if model.lower() in {"sonnet", "opus", "haiku", "default"}:
        raise AdapterError("model aliases are not accepted; pass an explicit full model id")
    runner = _runner_dir(prepared); execution = _validate_package(runner); response_id = str(execution["test_id"])
    probe = probe_claude_code(claude_binary, process_runner)
    if not probe["required_capabilities_present"]:
        raise AdapterError("Claude Code binary lacks required adapter capabilities: " + ", ".join(probe["missing_required_capabilities"]))
    out_dir = out_dir.resolve()
    if out_dir.exists(): raise AdapterError(f"output directory already exists: {out_dir}")
    requested_session = session_id or str(uuid.uuid4())

    with tempfile.TemporaryDirectory(prefix="ki-regeln-claude-") as tmp:
        root, task, config = Path(tmp), Path(tmp) / "task", Path(tmp) / "claude-config"
        shutil.copytree(runner, task); config.mkdir()
        if any(p.is_file() and p.name.lower() == "claude.md" for p in task.rglob("*")):
            raise AdapterError("runner package contains CLAUDE.md; automatic instruction loading is not allowed")
        empty_mcp = root / "empty-mcp.json"; empty_mcp.write_text('{"mcpServers": {}}\n', encoding="utf-8")
        read_only = _read_only(task)
        env, env_policy = _child_env(base_env if base_env is not None else os.environ, config)
        env_evidence = _environment(env, env_policy)
        managed = _managed_policy(claude_binary, env, task, process_runner)
        argv, controls = _argv(claude_binary, model, _prompt(execution), requested_session, probe["capabilities"], empty_mcp)
        started = _now(); result = process_runner(argv, cwd=task, env=env, input_text=None); finished = _now()
        if result.returncode != 0:
            raise AdapterError(f"Claude Code process failed with exit code {result.returncode}; stderr_sha256={_hash_text(result.stderr)}")
        stream = _parse_stream(result.stdout)
        if controls["explicit_session_id"] and stream["observed_session_id"] != requested_session:
            raise AdapterError(f"runtime session id mismatch: requested {requested_session}, observed {stream['observed_session_id']}")
        actions, reads, outside = _actions(stream, task, started)
        mutating = any(x.get("executed") is True and bool(set(x.get("action_class") or []) & {"productive", "destructive"}) for x in actions["actions"])
        trace = _trace(execution, reads, task, mutating, finished)
        fresh_context, fresh_report = _fresh_context(controls, stream, managed, env_policy)
        model_pre, runtime_pre = _preimages(model, stream, probe, controls, env_evidence, read_only, managed, fresh_report)
        model_fp, runtime_fp = _hash_obj(model_pre), _hash_obj(runtime_pre)
        evidence = _evidence(probe, argv, model, requested_session, stream, env_evidence, controls, result.stdout, result.stderr, started, finished, reads, read_only, managed, fresh_report)
        method = _method(response_id, stream, actions, outside, controls, model_fp, runtime_fp, fresh_context)
        adapter_result = {
            "schema_version": 1, "runner_type": RUNNER_TYPE, "runner_model": stream["observed_model"],
            "runner_session_id": stream["observed_session_id"], "started_at": started, "finished_at": finished,
            "runner_output": "runner-output.md", "trace": "trace.yml", "actions": "actions.yml", "evidence": "evidence.yml",
        }
        stage = root / "adapter-output"; stage.mkdir()
        (stage / "runner-output.md").write_text(stream["final_text"] + "\n", encoding="utf-8")
        for name, data in (
            ("trace.yml", trace), ("actions.yml", actions), ("evidence.yml", evidence), ("adapter-result.yml", adapter_result),
            ("model-configuration-preimage.yml", model_pre), ("runtime-configuration-preimage.yml", runtime_pre), ("method-evidence.yml", method),
        ): _dump(data, stage / name)
        shutil.copytree(stage, out_dir)
    return out_dir


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__); sub = p.add_subparsers(dest="command", required=True)
    probe = sub.add_parser("probe", help="Inspect installed Claude Code without a model task"); probe.add_argument("--claude-binary", default="claude")
    run = sub.add_parser("run", help="Execute one prepared Behavioral-Harness response")
    run.add_argument("--prepared-response", required=True); run.add_argument("--claude-binary", default="claude")
    run.add_argument("--model", required=True, help="Explicit full model id"); run.add_argument("--session-id")
    run.add_argument("--out", required=True)
    return p


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "probe":
            print(yaml.safe_dump(probe_claude_code(args.claude_binary), sort_keys=False), end=""); return 0
        target = execute_prepared_response(Path(args.prepared_response), model=args.model, out_dir=Path(args.out), claude_binary=args.claude_binary, session_id=args.session_id)
        print(target); return 0
    except AdapterError as exc:
        print(f"CLAUDE_ADAPTER_ERROR: {exc}", file=sys.stderr); return 2


if __name__ == "__main__":
    raise SystemExit(main())
