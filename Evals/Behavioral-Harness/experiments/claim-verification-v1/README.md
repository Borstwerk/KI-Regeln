# Claim Verification – Paired With-vs-Without Pilot v1

## Status

This directory defines the first controlled paired-skill pilot for `claim-verification`.

It records **method preparation only**. No isolated LLM A/B responses, semantic blind judgments or skill-effect results are created by this repository change.

The experiment asks:

> Under the same prompt, same package-local evidence, same model and same sufficiently evidenced runner conditions, does making the `claim-verification` skill instruction available change observable claim-verification behavior?

This is a pilot method check, not a public benchmark and not evidence for a Maturity or Eval Coverage promotion.

## Controlled variable

For each pair, the intended constants are:

- identical user prompt;
- identical subject-source files and byte hashes;
- identical subject-fixture roles;
- pinned repository/skill version;
- package-only read interface;
- no web access;
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

The repository harness still does not start an LLM runner.

A later external runner must execute each opaque response in a fresh context and keep control/judge data hidden. Ordinary run packaging remains canonical:

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

### Model configuration fingerprint

The later runner should normalize and hash all model-generation settings it can actually control or observe, for example:

- provider/model identifier or revision when exposed;
- temperature;
- top-p/top-k where applicable;
- max-output settings;
- deterministic seed when supported;
- reasoning/thinking mode and budget when applicable;
- stable system-instruction template **excluding the intended treatment artifact**.

Unavailable provider settings remain unknown; they are not reconstructed.

### Runtime configuration fingerprint

The later runner should normalize and hash the actual execution environment relevant to parity, for example:

- adapter/version;
- enabled tool/capability set;
- tool permission mode;
- network policy;
- repository/filesystem mount policy;
- other provider runtime controls that could change the response.

The baseline/skill package-content difference itself must not be folded into this fingerprint, because that is the independent variable.

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
