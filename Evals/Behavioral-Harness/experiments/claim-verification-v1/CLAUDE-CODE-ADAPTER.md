# Claude Code Runner Adapter – Phase 4.2A-R2

## Status

This document describes the narrow Claude Code bridge for the controlled `claim-verification` paired pilot.

The adapter executes **one already prepared opaque response**. It does not create pairs, ground truth, judge packages or behavioral conclusions. The existing Behavioral Harness remains canonical.

```text
prepared response / runner-package
        ↓
tools/behavioral_harness_claude.py
        ↓
adapter-result.yml + canonical runner artifacts
        ↓
tools/behavioral_harness.py package-run
        ↓
ordinary Behavioral-Harness run package
```

No real A/B response was executed as part of R2.

## CLI

Probe the concrete installed binary first:

```bash
python tools/behavioral_harness_claude.py probe \
  --claude-binary claude
```

Execute one prepared response:

```bash
python tools/behavioral_harness_claude.py run \
  --prepared-response <prepared-response-dir> \
  --claude-binary claude \
  --model <full-model-id> \
  --out <adapter-output-dir>
```

Common model aliases such as `sonnet`, `opus` or `haiku` are rejected. The caller must provide an explicit full model identifier.

The adapter only relies on capabilities that the concrete binary reports through `--help`. Required capabilities are:

- headless/print mode;
- `--output-format` with `stream-json`;
- explicit model selection;
- allowed-tool control;
- denied-tool control.

Optional controls are used only when the concrete binary reports them, including explicit session IDs, session-persistence control, MCP config isolation and controlled system prompt support. `--resume` and `--continue` are never used. No `--restricted` capability is assumed.

## Runtime shape

For every response the adapter creates a new temporary runtime:

```text
temporary-runtime/
    task/           # copied runner-package only
    claude-config/  # own CLAUDE_CONFIG_DIR
    empty-mcp.json
    adapter-output/
```

The actual Claude process runs with `task/` as its working directory. Package files are made read-only where the host filesystem permits it. A `CLAUDE.md` inside the copied runner package is rejected before model execution.

This is **not an OS/container sandbox**. A different CWD plus copied files does not prove that the process cannot read other host paths. Therefore filesystem-isolation facts remain `unknown` unless later runtime evidence proves more.

## Tool and data policy

The requested task tool set is `Read` only. The adapter denies at least:

- Bash;
- Edit;
- Write;
- WebSearch;
- WebFetch;
- NotebookEdit;
- Task.

An empty MCP config is requested when supported, with strict MCP config when that flag is also supported. Requested policy and observed `system/init` state are stored separately.

Unexpected tools, MCP servers, plugins or hooks are not normalized away. They remain visible in runtime evidence. An observed external capability or executed external action prevents `network_disabled: true`; the current adapter reports `false` for a known external path and otherwise `unknown` unless stronger transport/egress evidence exists.

## Outputs

The output directory contains:

- `adapter-result.yml` – existing Behavioral-Harness runner-adapter contract;
- `runner-output.md` – final model response;
- `trace.yml` – existing trace contract;
- `actions.yml` – observed tool actions;
- `evidence.yml` – structured launch/runtime evidence;
- `method-evidence.yml` – existing paired method-evidence sidecar;
- `model-configuration-preimage.yml` – normalized model fingerprint preimage;
- `runtime-configuration-preimage.yml` – normalized runtime fingerprint preimage.

Raw stream JSON, raw stdout and raw stderr are **not persisted**. Their hashes and line counts are retained in evidence. Authentication values are never stored; only allowlisted presence booleans are recorded. Endpoint configuration is represented by presence plus hashes, not raw values.

## Requested vs observed

The adapter deliberately distinguishes intent from runtime evidence. Examples include:

- requested model vs observed model;
- requested tool policy vs observed tools;
- requested empty MCP config vs observed MCP servers;
- generated/passed session ID vs observed session ID;
- intended package-only execution vs observable file/tool activity.

`runner_model` in `adapter-result.yml` is the observed model when Claude Code reports it. Missing runtime values remain `unknown`.

## Fingerprints

The model fingerprint includes the controllable/observable model state such as requested/observed model, provider selection, system-prompt hash and explicit `not_exposed` markers for unavailable generation parameters.

The runtime fingerprint includes Claude Code version, adapter version/code hash, normalized CLI controls, allowlisted environment controls, requested/observed tool policy, MCP/plugin/hook observations, persistence/memory controls, filesystem policy and network policy.

Per-response session IDs, temporary paths, task prompt text and the intentional baseline/skill package-content difference are normalized out of the runtime fingerprint. The treatment difference is therefore not allowed to create fingerprint inequality by construction.

## Method-evidence boundary

R2 intentionally does not infer proof from configuration intent.

With the current non-sandboxed runtime, the expected conservative values are normally:

```yaml
fresh_context: unknown
network_disabled: unknown
repository_access_disabled: unknown
package_only_access: unknown
```

Known violations can become `false`. For example an observed MCP/external data path makes `network_disabled: false`, and an observed successful file access outside the task package makes `package_only_access: false`.

The adapter currently does **not** emit `true` for these isolation fields merely because flags, a fresh UUID, a temporary directory or an empty config were requested. Consequently its first real smoke pair is expected to be methodologically `partial` unless a stronger sandbox/evidence layer is added.

## Tests

`tests/test_behavioral_harness_claude.py` uses synthetic process/stream fixtures and makes no real Claude calls. It covers the requested success/error/evidence cases, including model/session mismatch, unexpected tools/MCPs, malformed streams, secret handling and fingerprint invariance across the treatment package difference.
