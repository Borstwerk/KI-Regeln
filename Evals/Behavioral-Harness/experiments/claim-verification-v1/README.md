# Claim Verification – Paired With-vs-Without Pilot v1

## Status

This directory defines the first controlled paired-skill pilot for `claim-verification`.

The pilot has since been executed in part. `METHOD-RESULT.md` in this directory is the canonical closing record; the summary is:

| | |
| --- | --- |
| Experiment prepared | yes |
| Runner implemented | yes |
| Real behavioral smoke | exactly 2 responses (CV-01-supported, repetition 1) |
| Full 36-response execution | not run |
| Method evidence | `partial` |
| Comparison eligible | `false` |
| Semantic judge | not run |
| Unblinding | not run |
| Skill effect | unknown |

Two real isolated LLM responses therefore exist, but **no** semantic blind judgment, **no** unblinding, **no** behavioral comparison and **no** skill-effect result. The single unproven method fact is `network_disabled`, which stays `unknown`.

The experiment asks:

> Under the same prompt, same package-local evidence, same model and same sufficiently evidenced runner conditions, does making the `claim-verification` skill instruction available change observable claim-verification behavior?

This is a pilot method check, not a public benchmark and not evidence for a Maturity or Eval Coverage promotion. That question is **not** answered by the executed part of the pilot.

## Controlled variable

For each pair, the intended constants are:

- identical user prompt;
- identical subject-source files and byte hashes;
- identical subject-fixture roles;
- pinned repository/skill version;
- package-only read interface;
- no task-external network or data access;
- no repository access outside the prepared package;
- identical model identity and generation configuration;
- identical runner/tool/runtime configuration;
- fresh isolated contexts;
- identical semantic judge contract and precommitted ground truth.

The intended independent variable is only:

- **baseline:** no `claim-verification` instruction artifact;
- **skill:** the exact pinned `Recherche/Skills/claim-verification/SKILL.md` as the only treatment-specific instruction artifact.

Both treatments receive the same five verdict labels in the user prompt, so the skill does not win merely by defining vocabulary.

## Fixture roles

Every subject fixture declares an explicit role using the existing Behavioral-Harness vocabulary rather than a new paired-eval taxonomy:

- `authoritative-source`;
- `intentionally-incomplete`;
- `supporting-source`;
- `distractor`;
- `policy`;
- `runner-only`.

`evaluator-only` and `unknown` are not valid subject-fixture roles for this executable pilot.

The treatment-only skill file is generated separately as `skill-instruction`; it is not a subject-source role.

For `CV-05-primary-vs-summary`, the current API reference is `authoritative-source`, while the search summary and community guide are `supporting-source`. This prevents harness metadata from flattening deliberately different source authority.

## Precommitted classification ground truth

Each case contains structured classification metadata:

```yaml
classification:
  preferred: partial
  accepted_alternatives:
    unsupported:
      conditions:
        - explicit precommitted condition
  disallowed:
    - supported
    - conflicting
    - not-verified
```

Rules:

- exactly one `preferred` label;
- alternatives exist only when explicitly declared before execution;
- every accepted alternative requires at least one explicit condition;
- all five known labels must be partitioned into preferred/accepted versus disallowed;
- unknown labels are rejected;
- the legacy one-value `expected_classification` field is rejected for paired pilots.

`CV-02` accepts `unsupported` only when the response explicitly distinguishes Enterprise 30 seconds from Standard 60 seconds and explains why the universal claim is false.

`CV-06` accepts `partial` only when generic at-rest encryption is kept separate from the unverified AES-256-GCM mechanism.

The full classification contract remains in the treatment-blind judge contract.

## Case set

`experiment.yml` defines six synthetic local cases:

1. exact support;
2. population/scope partial support;
3. unresolved comparable-source conflict;
4. wrong-version unsupported claim;
5. current primary source versus stale summary/secondary material;
6. insufficient evidence for a specific encryption algorithm.

No live web lookup is required or allowed.

## Treatment order

A coordinator-only blind seed selects the starting treatment deterministically for each experiment/case. Repetitions then alternate the first treatment.

That yields:

- reproducible order for the same experiment/case/seed/repetition;
- counterbalancing across repetitions;
- no hard-coded baseline-first assumption;
- no post-result manual order adjustment.

`control.yml` stores the opaque response execution order. `judge-contract.yml`, `parity.yml` and the blind judge package do **not** expose treatment mapping or execution order.

## Repetitions

The experiment recommends three paired repetitions per case:

- 6 cases;
- 18 A/B pairs;
- 36 responses.

Repetition exposes stochastic instability; it does not manufacture statistical significance.

## Preparation

```bash
python tools/behavioral_harness_pair.py prepare-pair CV-01-supported \
  --experiment Evals/Behavioral-Harness/experiments/claim-verification-v1/experiment.yml \
  --repetition 1 \
  --blind-seed <coordinator-secret> \
  --out Evals/Behavioral-Harness/prepared/CV-01-supported-r1
```

Verify before execution:

```bash
python tools/behavioral_harness_pair.py verify-pair \
  --paired Evals/Behavioral-Harness/prepared/CV-01-supported-r1
```

Prepared output contains:

- coordinator-only `control.yml`;
- treatment-blind `judge-contract.yml`;
- two ordinary Behavioral-Harness prepared response directories;
- identical subject sources;
- one treatment-only skill instruction file.

Prepared/run directories remain ignored by Git.

## Runner execution

The generic `behavioral_harness.py` still starts no LLM runner itself; that separation is unchanged. Execution is the job of a concrete runner adapter, and this pilot now has one: `tools/behavioral_harness_claude.py`, documented in `CLAUDE-CODE-ADAPTER.md`. It has been executed against a real Claude Code runtime for the CV-01 smoke described in `METHOD-RESULT.md`.

Any runner adapter must execute each opaque response in a fresh context and keep control/judge data hidden. Ordinary run packaging remains canonical:

```bash
python tools/behavioral_harness.py package-run \
  --prepared <prepared-response-dir> \
  --adapter-result <adapter-result.yml> \
  --run-id <opaque-run-id> \
  --out Evals/Behavioral-Harness/runs
```

`behavioral_harness_pair.py` does not replace compile, telemetry, `package-run` or `verify-run`.

## Pair-specific method evidence

Technical run packaging and methodological A/B eligibility are deliberately separate.

A concrete external runner may provide one pair-method evidence sidecar per response:

```yaml
schema_version: 1
contract: behavioral-paired-run-method-evidence/v1
response_id: R-...
runner_type: <must match run manifest>
runner_model: <must match run manifest>
runner_session_id: <must match run manifest>
model_configuration_fingerprint: sha256:<normalized runner/model config>
runtime_configuration_fingerprint: sha256:<normalized tool/runtime config>
fresh_context: true
network_disabled: true
repository_access_disabled: true
package_only_access: true
```

For unavailable evidence use the existing Harness tri-state value `unknown`; do not guess.

### Isolation semantics for remote-model runners

A paired run executed against a remote model provider still needs an honest reading of the isolation facts. For paired remote-LLM runs the following definition is binding:

> `network_disabled` means that **no task-external network or data access is available for solving the task**. Only the technically necessary transport to the configured model provider may be permitted.

It therefore does **not** claim that no network packet leaves the process. It does claim:

- no web search, fetch or other retrieval capability usable by the model;
- no further API, package index, database or remote filesystem reachable as task input;
- no provider-side retrieval or tool augmentation adding content beyond the prepared package;
- the provider transport carries only the prepared task material and the run's own output.

If a task-external data path is known to exist, `network_disabled` is `false`. If such a path can neither be excluded nor demonstrated as excluded, the value is `unknown`. The value is `true` only where the runner can evidence that the provider transport is the sole permitted egress.

`repository_access_disabled` and `package_only_access` keep their literal meaning: the repository working tree lies outside the runtime the model can read, and the prepared runner package is the only task data area.

### Model configuration fingerprint

The runner should normalize and hash all model-generation settings it can actually control or observe, for example:

- provider/model identifier or revision when exposed;
- temperature;
- top-p/top-k where applicable;
- max-output settings;
- deterministic seed when supported;
- reasoning/thinking mode and budget when applicable;
- stable system-instruction template **excluding the intended treatment artifact**.

Unavailable provider settings remain unknown; they are not reconstructed.

`model_configuration_fingerprint` proves equality of the **controllable and observable** model/runner configuration across the two responses of a pair.

It does **not** prove equality of invisible provider-internal state, for example undisclosed serving revisions, routing or fallback between backends, provider-side default changes, capacity-dependent behaviour, or hidden system-prompt fragments injected by the provider.

### Runtime configuration fingerprint

The runner should normalize and hash the actual execution environment relevant to parity, for example:

- adapter/version;
- enabled tool/capability set;
- tool permission mode;
- network policy;
- repository/filesystem mount policy;
- other provider runtime controls that could change the response.

The baseline/skill package-content difference itself must not be folded into this fingerprint, because that is the independent variable.

`runtime_configuration_fingerprint` proves the same kind of fact for the execution environment: equality of the controllable and observable runner configuration. It does not prove equality of provider-internal runtime state, and it does not prove that a declared policy was actually enforced — enforcement requires its own isolation evidence.

Values a runner cannot read stay `unknown`. Fabricating, defaulting or back-filling an unobserved value invalidates the fingerprint and therefore the pair.

## Method-validity gate

`package-blind-pair` accepts technically verified run packages even when method evidence is incomplete or a known parity mismatch exists. Such a pair can be stored and inspected.

The blind package records tri-state parity facts and derives `method_evidence_status` using the repository's existing status vocabulary:

- `pass` – all required parity/isolation evidence is known and satisfied;
- `partial` – run packages exist, but at least one required method fact is `unknown`;
- `fail` – at least one required parity/isolation fact is known false.

Only:

```yaml
method_evidence_status: pass
comparison_eligible: true
```

is valid input for a later With-vs-Without skill-effect comparison.

`partial` and `fail` are **not behavioral skill results**. They describe only method evidence.

Required method facts include:

- same prompt;
- same subject sources;
- same subject roles;
- same prepared runtime contract;
- same pinned repository version;
- pinned target-skill version;
- same known runner model;
- same known runner type;
- distinct sessions;
- sidecar identity consistent with the canonical run manifest;
- same model-configuration fingerprint;
- same runtime-configuration fingerprint;
- fresh-context evidence;
- network disabled;
- repository access disabled;
- package-only access.

### What a `pass` must not be inferred from

`method_evidence_status: pass` requires the adapter to actually evidence those facts. Specifically:

- **a set flag is not proven isolation** – a CLI flag or config key documents intent; the run must additionally show the effect (for example the observed tool set, an absent capability, a denied access);
- **a requested model is not an observed model** – `runner_model` must reflect what the runtime reported back, not what was asked for; if the runtime reports no model identity, the value is `unknown`;
- **a new session UUID is not a proven fresh context** – a fresh identifier alone does not exclude carried-over memory, resumed transcripts, user/project instruction files or provider-side history;
- **the absence of one fetch capability is not the absence of every external data path** – excluding a single web tool says nothing about other tools, MCP servers, plugins or provider-side retrieval;
- **an identical intended configuration hash is not an identical effective run** – the fingerprint covers the requested configuration; that both responses actually ran under it must follow from observed runtime evidence.

Where such proof is missing, the affected fact stays `unknown` and the pair is `partial`. `partial` is a valid, storable result; a wrongly claimed `pass` is not.

## Claude Code runner evidence requirements

This section defines the **minimum evidence** a Claude Code based runner adapter must emit so that its pairs can be assessed against the method-validity gate at all. It was written before the adapter existed; the adapter now exists as `tools/behavioral_harness_claude.py` and has been run against a real Claude Code runtime, so the requirements below are the contract it is held to rather than a forward-looking wish list.

### No dependency on undocumented CLI capabilities

The adapter contract must not require any Claude Code capability that is neither documented in the current official CLI reference nor demonstrated on the concretely installed version. In particular, no method fact may depend on an assumed blanket restriction flag such as `--restricted`.

Every capability the adapter relies on is verified against the installed binary at adapter build time. Anything not verifiable there is recorded as `unknown` instead of assumed. If the installed version does offer additional restriction flags, they may be used as defense in depth; they are never a necessary component of a method `pass` and never replace observed runtime evidence.

### Launch evidence

Recorded at process start, per response:

- the concrete Claude Code version, as reported by the installed binary;
- the complete CLI argument vector, verbatim;
- the relevant environment configuration (at minimum config directory, memory/`CLAUDE.md` handling, session-persistence and telemetry/update controls);
- the requested model, as the full model name passed to the run;
- the session id passed to the run.

### Runtime evidence

Read back from the machine-readable event stream (`system`/`init` and later records), as far as the runtime actually reports it:

- observed model;
- available tools;
- MCP servers;
- plugins;
- session id as reported by the runtime.

Anything the runtime does not report is `unknown`. Where observed and requested values diverge — the model above all — the observed value governs and the divergence is recorded rather than smoothed over.

### Isolation evidence

Isolation must not rest on the model's self-report. The adapter evidences:

- a fresh runtime per response;
- an own config directory per response;
- no resume/continue use;
- session persistence disabled;
- `CLAUDE.md`/memory loading disabled;
- the repository located outside the runtime accessible to the model;
- the runner package as the only task data area;
- a minimal tool set;
- MCP servers disabled;
- task-external network access prevented;
- provider transport permitted separately.

For each item the adapter records both the configured intent (flag, environment variable, mount) and an observable confirmation (for example the reported tool list, an empty config directory, a directory listing the runtime cannot produce). Where only intent exists, the corresponding method fact stays `unknown`.

## Blind judge package

After both ordinary run packages exist:

```bash
python tools/behavioral_harness_pair.py package-blind-pair \
  --paired Evals/Behavioral-Harness/prepared/CV-01-supported-r1 \
  --run <run-dir-1> \
  --run <run-dir-2> \
  --method-evidence <method-evidence-1.yml> \
  --method-evidence <method-evidence-2.yml> \
  --out <blind-judge-package-dir>
```

Method evidence arguments are optional. Missing evidence remains `unknown`, which makes the method status `partial` rather than silently valid.

The blind package contains:

- precommitted ground truth;
- explicit source roles;
- evaluation dimensions;
- method parity facts/status;
- two outputs under opaque response IDs;
- no baseline/skill mapping;
- no execution order.

Treatment disclosure in runner output still prevents blind packaging.

Only after semantic judging is complete may the coordinator unblind with `control.yml`.

## Interpretation boundary

Even a later `method_evidence_status: pass` says only that the A/B **method conditions were sufficiently evidenced**. It does not say the skill passed.

Even if later paired responses favor the skill, conclusions remain limited to:

- this skill version;
- this controlled source corpus;
- the tested model/configuration;
- these six failure modes;
- this runner and judge procedure.

It does not establish model-independent effectiveness, benchmark superiority, `stable` maturity or `core`/`broad` Eval Coverage.
