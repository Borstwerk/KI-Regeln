# Claim Verification – Paired With-vs-Without Pilot v1

## Status

This directory defines the first controlled paired-skill pilot for `claim-verification`.

It does **not** record a behavioral pass. At the time this pilot definition was added, no isolated LLM runner was integrated into the repository harness and no A/B model responses were executed by this change.

The experiment asks one narrow question:

> Under the same prompt, same package-local evidence, same model and same runner conditions, does making the `claim-verification` skill instruction available change observable claim-verification behavior?

This is a pilot method check, not a public benchmark and not evidence for a Maturity or Eval Coverage promotion.

## Controlled variable

For every pair, the following stay constant:

- user prompt;
- subject-matter source files and their byte hashes;
- pinned target-skill repository commit;
- allowed read-only package interface;
- no web access;
- no repository access outside the prepared runner package;
- semantic judge contract and precommitted ground truth;
- model identity and model configuration, as far as the external runner can document them.

The intended independent variable is only:

- **baseline:** `claim-verification` is not present in the runner package;
- **skill:** the exact pinned `Recherche/Skills/claim-verification/SKILL.md` is present as the only additional instruction artifact.

The baseline is explicitly forbidden from reading the target skill. The skill treatment requires it. Ordinary harness route telemetry remains the source of technical evidence when the runner adapter can observe file reads.

## Case set

`experiment.yml` defines six precommitted cases:

1. exact support;
2. population/scope partial support;
3. unresolved comparable-source conflict;
4. wrong-version unsupported claim;
5. current primary source versus stale summary/secondary material;
6. insufficient evidence for a specific encryption algorithm.

All source documents are synthetic local fixtures. No live web lookup is needed or allowed.

The five skill classifications are used as an output contract for **both** treatments:

- `supported`;
- `partial`;
- `conflicting`;
- `unsupported`;
- `not-verified`.

Giving the baseline the same label vocabulary prevents a trivial advantage caused only by the skill defining the names of its verdict classes.

## Ground truth

Ground truth is stored in `experiment.yml` before model execution and includes per case:

- expected classification;
- decisive evidence;
- decisive reasoning;
- known traps;
- allowed uncertainty;
- hard failures.

Do not rewrite these fields after seeing model responses. A changed ground truth creates a new experiment version.

## Evaluation

The judge evaluates dimensions separately. There is intentionally no opaque aggregate percentage.

Core dimensions include:

- classification;
- decisive evidence use;
- source hierarchy;
- time/version scope;
- population/scope;
- conflict handling;
- missing evidence;
- uncertainty calibration;
- unsupported additions.

`overhead` is diagnostic only. A longer answer is not automatically worse, and a shorter answer is not automatically better.

Hard failures are evaluated independently from prose quality.

## Repetitions

The experiment recommends **three repetitions per case and treatment**.

With six cases this is:

- 6 cases;
- 3 paired repetitions per case;
- 18 A/B pairs;
- 36 model responses.

This is still a small pilot. Repetition is used to expose stochastic instability, not to manufacture statistical significance.

Each response must use a fresh isolated runner context. If the same known runner session is reused for both sides of a pair, blind pair packaging rejects it.

## Preparation

Prepare one pair with a coordinator-only blind seed:

```bash
python tools/behavioral_harness_pair.py prepare-pair CV-01-supported \
  --experiment Evals/Behavioral-Harness/experiments/claim-verification-v1/experiment.yml \
  --repetition 1 \
  --blind-seed <coordinator-secret> \
  --out Evals/Behavioral-Harness/prepared/CV-01-supported-r1
```

Then verify the prepared pair:

```bash
python tools/behavioral_harness_pair.py verify-pair \
  --paired Evals/Behavioral-Harness/prepared/CV-01-supported-r1
```

Prepared files are ignored by Git. The pair contains:

- `control.yml` – coordinator-only treatment mapping;
- `judge-contract.yml` – ground truth and dimension contract with opaque response IDs, but no treatment mapping;
- two response directories using ordinary Behavioral-Harness prepared-case files;
- self-contained runner packages containing the same subject sources;
- only the skill treatment additionally contains the pinned skill instruction.

Do not give `control.yml` to the runner or semantic judge.

## Runner execution

The repository harness still does not start an LLM runner itself.

Each opaque response runner package must therefore be executed by an external adapter that:

- creates a fresh context;
- uses the same model and model configuration for both responses in the pair;
- exposes no web access;
- exposes no repository access outside the runner package;
- keeps judge/control files hidden;
- records observable telemetry using the existing runner-adapter contract;
- does not self-report the treatment in the final answer.

Package each completed response with the existing command:

```bash
python tools/behavioral_harness.py package-run \
  --prepared <prepared-response-dir> \
  --adapter-result <adapter-result.yml> \
  --run-id <opaque-run-id> \
  --out Evals/Behavioral-Harness/runs
```

`package-run` and `verify-run` remain the canonical technical run-package path. The paired helper does not replace them.

## Blind judge package

After both ordinary run packages exist:

```bash
python tools/behavioral_harness_pair.py package-blind-pair \
  --paired Evals/Behavioral-Harness/prepared/CV-01-supported-r1 \
  --run <run-dir-for-first-opaque-response> \
  --run <run-dir-for-second-opaque-response> \
  --out <blind-judge-package-dir>
```

The blind package contains:

- precommitted ground truth;
- evaluation dimensions;
- parity information;
- two outputs under opaque response IDs;
- no baseline/skill mapping.

The helper refuses blind packaging if the output explicitly discloses the target skill ID or labels itself as a baseline/skill condition.

Only after semantic judging is complete should the coordinator unblind using `control.yml`.

## Known limitation: model configuration fingerprint

The current generic runner-adapter/run-manifest contracts record model identity but do not yet carry a normalized configuration fingerprint for temperature, seed, system prompt or provider-specific settings.

Therefore:

- model identity parity can be checked from run packages;
- prompt/source/runtime parity can be checked by the paired preparer;
- full model-configuration parity must remain **UNVERIFIED** unless the concrete external runner records it separately.

This limitation is intentionally documented instead of silently treating same model name as same configuration.

## Interpretation boundary

Even if every paired run later favors the skill treatment, this experiment would establish at most evidence about:

- this skill version;
- this controlled source corpus;
- the tested model/configuration;
- these six failure modes;
- this runner and judge procedure.

It would not establish model-independent skill effectiveness, general benchmark superiority, `stable` maturity or `core`/`broad` eval coverage.
