# Claude Code Runner Adapter – Phase 4.2A-R2/R3-a

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

The adapter only relies on required capabilities that the concrete binary reports through `--help`. Required capabilities are:

- headless/print mode;
- `--output-format` with `stream-json`;
- explicit model selection;
- `--tools` to restrict built-in tools to `Read`;
- allowed-tool permission control;
- denied-tool control, including `mcp__*`.

`--allowedTools` is **not** treated as tool isolation. It only pre-approves the requested `Read` tool. The actual built-in tool boundary is requested with `--tools Read`; MCP tools are separately denied and an empty MCP config is requested where supported.

Optional defense-in-depth controls are used only when the concrete binary reports them, including:

- `--restricted` for its documented working-directory file boundary where supported;
- `--safe-mode` to keep customizations (CLAUDE.md, skills, plugins, hooks, MCP, commands, agents) from loading — **required**, see below;
- `--disable-slash-commands`, which does not touch the independent variable because the treatment is a read fixture, not a slash command;
- `--include-hook-events`, so that the absence of hook activity is observable rather than merely assumed;
- `--no-chrome` where supported;
- explicit session IDs;
- session-persistence control;
- MCP config isolation;
- controlled system prompt support.

The probe also detects context-extending options (`--add-dir`, `--plugin-dir`, `--plugin-url`, `--agents`, `--fallback-model`, `--fork-session`). The adapter never passes them, and the launch policy records structurally that neither a context-extending nor a session-carryover flag reached the argv.

None of the remaining R3-a additions are required capabilities. On an older binary that does not report them the adapter still runs, and the facts they would have proved stay `unknown` instead of being assumed.

`--resume` and `--continue` are never used. The adapter does not assume that `--restricted` or any other optional flag exists on an unprobed binary.

### `--bare` is not used; `--safe-mode` is required

`--bare` never reads Claude Code's managed authentication. On a host-managed platform that made every run fail with a non-zero exit before `system/init`, with no observable evidence at all. The adapter therefore **never passes `--bare`**, even when the probe reports the capability: `bare_requested` is always `false`, and `bare_capability_available` records only that the binary has it.

`--safe-mode` takes over as the central isolation control and is consequently **required**. A binary that does not report it makes the adapter fail before any model process; there is no fallback to `--bare` and no weaker runtime. `--safe-mode` closes the same customization sources as `--bare` — CLAUDE.md, skills, plugins, hooks, MCP servers, custom commands, agents, output styles, workflows, auto memory — and additionally does not load managed plugins, managed skills, managed CLAUDE.md or policy-configured MCP servers.

What `--bare` additionally suppressed and `--safe-mode` does not document is background prefetch and plugin sync. That is non-task background traffic, not a prompt, memory or settings source, so it is recorded as `background_prefetch_or_sync_absent: unknown` in the runtime preimage and is a question for network observation, never a hidden fresh-context source.

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

### Environment policy

The child process no longer inherits the parent environment. It receives an explicit allowlist covering process start, locale/encoding, authentication, provider transport and the adapter's own documented controls, plus:

```text
CLAUDE_CODE_DISABLE_CLAUDE_MDS=1
CLAUDE_CODE_SKIP_PROMPT_HISTORY=1
DISABLE_UPDATES=1
DISABLE_AUTOUPDATER=1
DISABLE_TELEMETRY=1
DISABLE_ERROR_REPORTING=1
DISABLE_BUG_COMMAND=1
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

Every other `CLAUDE_*`, `CLAUDE_CODE_*` and `ANTHROPIC_*` variable is dropped unless explicitly allowlisted, because an inherited value such as `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD`, `CLAUDE_ADDITIONAL_DIRECTORIES` or `CLAUDE_EFFORT` would silently change the run. Evidence records the inherited names and the removed agent/generation names; values of authentication variables are never persisted.

An allowlisted variable still changes the effective run, so the non-secret transport settings (proxy, provider region/profile, CA bundle, Bedrock/Vertex selection) enter the runtime fingerprint as presence plus hash:

```yaml
transport_configuration:
  HTTPS_PROXY:
    present: true
    value_hash: sha256:...
  AWS_PROFILE:
    present: false
    value_hash: unknown
```

Two responses whose effective transport configuration differs therefore cannot share a runtime fingerprint. Authentication variables keep presence/absence only — they are neither hashed nor stored — so rotating a key does not change the fingerprint and never reaches an artifact. Endpoint configuration keeps its existing presence-plus-hash form.

### Authentication preflight

Bare mode does not read OAuth credentials or the system keychain, so a run without a supported credential fails inside the model process rather than at startup. The adapter therefore classifies the authentication path from the effective child environment *before* launching:

| `auth_mode` | Recognised when |
| --- | --- |
| `anthropic-api-key` | `ANTHROPIC_API_KEY` is present in the child environment |
| `bedrock` | `CLAUDE_CODE_USE_BEDROCK=1` is explicitly set |
| `vertex` | `CLAUDE_CODE_USE_VERTEX=1` is explicitly set |
| `claude-managed-auth` | none of the above, on the non-bare path: Claude Code uses its own managed authentication |
| `unsupported-or-missing` | none of the above, and bare mode was requested |

Present AWS or Google credentials never imply Bedrock or Vertex on their own; only the explicit selector counts.

`claude-managed-auth` asserts only that the non-bare process may use the authentication Claude Code manages itself. It asserts nothing about the credential value, its transport, or whether the runtime will actually authenticate, so it carries `credential_present: unknown` and `runtime_authenticated: unknown`. Only a model process that exits zero with a usable stream upgrades the latter to `true`; there is no credential fail-fast on this path, and a runtime authentication failure is classified afterwards as `authentication_failed` without a retry.

The `unsupported-or-missing` abort therefore remains reserved for a bare-mode request, which the productive path no longer makes.

Host-internal credential channels — `CLAUDE_CODE_OAUTH_TOKEN_FILE_DESCRIPTOR` and its siblings — are neither added to the environment allowlist nor treated as a proven bare-mode authentication path. When such a variable exists in the parent environment, evidence records only that its name was seen and ignored.

Evidence carries the mode and a presence boolean:

```yaml
authentication:
  mode: anthropic-api-key
  credential_present: true
  host_only_channels_ignored: []
```

The mode enters the runtime fingerprint, so two responses authenticated through different paths cannot share one. Rotating a secret within the same mode does not change the fingerprint, because no credential value is stored or hashed.

The auth preflight is not a model run, not method evidence and not behavioral evidence.

### Managed-policy preflight

Managed settings survive `--restricted`, `--bare` and `--safe-mode` by documented design, and server-managed settings arrive over the network, so a local file check alone cannot clear them. Before the model launch the adapter therefore observes, without any model task:

- the platform's managed settings file, managed settings drop-in directory and managed MCP file;
- the remote managed-settings status line reported by `claude doctor`.

An unreadable or unparsable status is recorded as `unknown`. It is never read as "no policy".

A temporary directory alone is **not** an OS/container sandbox. Without a verified stronger file boundary, it does not prove that the process cannot read other host paths.

When the concrete binary proves `--restricted` is available and the run actually launches with that flag, the adapter may treat the documented working-directory confinement as filesystem-boundary evidence only if the observed tool set is exactly `Read`, observed MCP servers are empty and no outside-package/external access was observed. Without that combination the affected fields remain `unknown` or become `false` on a known violation.

## Failure diagnosis

A non-zero Claude Code exit is a single-attempt runner's most expensive event, so the adapter extracts a safe diagnosis instead of discarding everything. stdout is parsed as `stream-json` **in memory only** and reduced to a category drawn from a fixed allowlist:

```text
authentication_failed  oauth_org_not_allowed  billing_error  rate_limit  overloaded
invalid_request  model_not_found  server_error  max_output_tokens  unknown
```

A category is accepted only when it appears as a structured field value (`error`, `error_type` or `subtype`) and is on that list. Anything else, including an unrecognised category name and unparsable output, normalizes to `unknown`; the unrecognised name itself is not carried over.

The raised error names the exit code, the category, the structured event count, whether stdout contained malformed lines, and the stdout/stderr hashes. Raw stdout, raw stderr, `result` text, the prompt and any credential information are never persisted or echoed:

```text
Claude Code process failed with exit code 1; failure_category=authentication_failed;
structured_event_count=2; malformed_stdout_lines=False;
stdout_sha256=sha256:...; stderr_sha256=sha256:...
```

No output directory is created on a failed run, so a failure can never leave partial evidence behind.

## Tool and data policy

The requested built-in task tool set is exactly `Read`.

The adapter additionally denies at least:

- all MCP tools via `mcp__*`;
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

The runtime fingerprint includes Claude Code version, adapter version/code hash, normalized CLI controls, allowlisted environment controls, requested/observed tool policy, MCP/plugin/hook observations, session/memory controls, filesystem policy and network policy.

Per-response session IDs, temporary paths, task prompt text and the intentional baseline/skill package-content difference are normalized out of the runtime fingerprint. The treatment difference is therefore not allowed to create fingerprint inequality by construction.

## Fresh-context evidence

`fresh_context` is derived, not configured. It becomes `true` only when every required fact below is simultaneously known and satisfied, `false` as soon as one is known to be violated, and `unknown` whenever one is unproven.

Configured and structural:

- new process per response;
- explicit session ID requested;
- no resume, continue or fork flag in the argv;
- session persistence disabled by flag and prompt history disabled by environment;
- own ephemeral config directory;
- CLAUDE.md and auto memory disabled by environment plus `--bare`;
- no context-extending flag in the argv;
- `--restricted`, `--safe-mode` and `--disable-slash-commands` requested;
- controlled system prompt;
- strict MCP config with an empty MCP file;
- environment allowlist applied.

Preflight-observed:

- no local managed policy file, drop-in directory or managed MCP file;
- no remote managed settings reported by `claude doctor`.

Runtime-observed:

- exactly one `system/init` event;
- observed session ID equal to the requested one;
- observed tools exactly the allowed policy;
- no MCP servers and no MCP server errors;
- no plugins and no plugin errors;
- no loaded hook configuration (`no_loaded_hooks`);
- no hook lifecycle events, with `--include-hook-events` actually in force;
- no plugin-install events.

Loaded hooks and hook activity are separate facts and both are required. `no_hook_lifecycle_events` covers a hook that actually ran. `no_loaded_hooks` covers configuration that was loaded but stayed silent — and its value does **not** necessarily come from an `init.hooks` field, because safe mode on the observed runtime reports no such field at all:

| `system/init` hook state | result |
| --- | --- |
| present and empty | `true` |
| present and non-empty | `false` |
| absent or uninterpretable | `true` **only** when `safe_mode_requested`, `managed_policy_absent is True`, `hook_events_observable` and zero hook lifecycle events all hold; otherwise `unknown` |

The substitute chain is the safe-mode contract, plus the absence of a managed-policy exception path, plus an active runtime hook observation that stayed silent. A missing field is never read as an empty hook list on its own. A reported state always wins: an explicitly non-empty `init.hooks` is `false` regardless of safe mode, and an observed hook lifecycle event keeps `fresh_context` away from `true` through its own check.

Managed policy stays a separate mandatory gate. Safe mode does not make it irrelevant — policy-configured hooks are precisely why that gate exists.

The assessment is persisted with each individual check plus the `violated` and `unproven` lists, so a `partial` pair shows exactly which fact is missing. It currently holds 25 checks: 14 configured/structural, 1 preflight-observed and 10 runtime-observed. R3-b0.3 replaced `no_observed_hooks` with `no_loaded_hooks` rather than adding a check, so the number is unchanged. The number is a consistency anchor for the test suite, not a quality statement.

## Method-evidence boundary

The adapter does not infer proof from configuration intent.

The conservative default without a proved restricted file boundary is:

```yaml
network_disabled: unknown
repository_access_disabled: unknown
package_only_access: unknown
```

Known violations can become `false`. For example an observed MCP/external data path makes `network_disabled: false`, and an observed successful file access outside the task package makes `package_only_access: false`.

If the concrete Claude Code binary proves and accepts `--restricted`, and runtime observation also shows exactly `Read`, zero MCP servers and no outside-package/external access, `repository_access_disabled` and `package_only_access` may become `true` from that documented file boundary. This does not upgrade `fresh_context` or `network_disabled`.

The adapter still never emits `network_disabled: true`. R3-a adds no OS- or container-level egress enforcement, and under the paired contract a clean observed tool surface does not prove that no task-external data path was *available*: the absence of one fetch tool is not the absence of every external path, and disabling model-visible retrieval does not prove that provider transport is the sole egress. Reaching `true` would require an egress-enforcement layer that is deliberately out of scope here.

Consequently a first real smoke pair can now reach `fresh_context: true` when the runtime observations support it, but remains methodologically `partial` overall as long as `network_disabled` stays `unknown`.

`fresh_context: true` also stays a statement about the *runner* context. Provider-internal state such as prompt caching or server-side history remains unobservable and is not claimed.

## Tests

`tests/test_behavioral_harness_claude.py` uses synthetic process/stream fixtures and makes no real Claude calls. It covers the requested success/error/evidence cases, including model/session mismatch, unexpected tools/MCPs, malformed streams, secret handling, launch-policy enforcement, conservative isolation evidence and fingerprint invariance across the treatment package difference.

R3-b0.3 adds coverage for the runtime switch: `--safe-mode` present in the argv and `--bare` absent even when the capability exists, a missing `--safe-mode` capability aborting before any model process, the adapter version in the runtime fingerprint, the seven hook cases from the table above (including a unit-level check of the substitute chain), the managed authentication path and its `runtime_authenticated` upgrade, AWS or Google credentials alone still not selecting a provider, the host OAuth channel staying outside the allowlist, and a replay of the observed non-bare stream shape reaching `fresh_context: true` while `network_disabled` stays `unknown`.

R3-b0.1 adds coverage for the authentication preflight (API key allows the launch; a missing credential aborts before any model process; AWS credentials alone are not Bedrock; explicit Bedrock and Vertex are recognised; a host OAuth channel is neither allowlisted nor accepted; the auth mode moves the runtime fingerprint while a rotated secret does not) and for the failure classification (authentication, model-not-found and rate-limit categories, malformed stdout, an unlisted category normalising to `unknown`, and no model text, prompt or secret in the error message).

R3-a.1 adds coverage for loaded hooks versus hook activity (empty plus no events, loaded hooks without events, unknown hook state, an event without loaded hooks), for transport-configuration parity (identical configuration keeps the runtime fingerprint; a changed proxy, region, CA bundle or Vertex region changes it), for transport values being hashed rather than stored, for a rotated secret neither reaching an artifact nor moving the fingerprint, and for the check count.

R3-a adds coverage for the environment allowlist and the removal of unlisted agent/generation variables, the generation-environment sensitivity of the model fingerprint, safe-mode capability present versus absent, hook/plugin/MCP/plugin-install/second-init observations forcing `fresh_context: false`, local and remote managed policy preventing `true`, an unreadable managed-policy status staying `unknown`, missing runtime evidence staying `unknown`, complete evidence reaching `true`, and `network_disabled` never becoming `true` through R3-a. The managed-policy paths are redirected into a temporary directory so the suite never depends on the host's real policy files.
