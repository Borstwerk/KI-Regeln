#!/usr/bin/env python3
"""Thin paired-experiment orchestration for the existing KI-Regeln behavioral harness.

This module does not define a second run/telemetry framework. It reuses the
existing behavioral_harness compile, prepared-case, run-package and integrity
contracts and adds only paired preparation, treatment-order control, method
evidence checks and treatment-blind judge packaging.
"""
from __future__ import annotations
import argparse
import copy
import difflib
import hashlib
import re
import shutil
from pathlib import Path
from typing import Any
try:
    from .behavioral_harness import HarnessError, assert_runner_package_clean, compile_case, dump_yaml, hash_file, hash_object, load_yaml, verify_prepared_integrity, verify_run_package, write_prepared_case
except ImportError:
    from behavioral_harness import HarnessError, assert_runner_package_clean, compile_case, dump_yaml, hash_file, hash_object, load_yaml, verify_prepared_integrity, verify_run_package, write_prepared_case
PAIR_CONTRACT = 'behavioral-paired-skill-eval/v1'
CONTROL_CONTRACT = 'behavioral-paired-control/v1'
BLIND_JUDGE_CONTRACT = 'behavioral-paired-blind-judge/v1'
BLIND_INPUT_CONTRACT = 'behavioral-paired-blind-input/v1'
METHOD_EVIDENCE_CONTRACT = 'behavioral-paired-run-method-evidence/v1'
# Runner contract boundaries for METHOD_EVIDENCE_CONTRACT (semantics only, no schema change).
# For paired remote-model runs, `network_disabled` means that no task-external network or data
# access is available for solving the task; only the technically necessary transport to the
# configured model provider may be permitted. It is not a claim that no packet leaves the process.
# `model_configuration_fingerprint` and `runtime_configuration_fingerprint` prove equality of the
# controllable and observable configuration only, never of invisible provider-internal state.
# A method-evidence `pass` therefore requires evidenced facts, not intent:
#   a set flag is not proven isolation;
#   a requested model is not an observed model;
#   a new session id is not a proven fresh context;
#   a missing fetch tool is not a missing external data path;
#   an identical intended config hash is not an identical effective run.
# Values a runner cannot observe stay TRI_UNKNOWN; they are never guessed or back-filled.
# See Evals/Behavioral-Harness/experiments/claim-verification-v1/README.md.
TREATMENTS = ('baseline', 'skill')
CLASSIFICATION_LABELS = {'supported', 'partial', 'conflicting', 'unsupported', 'not-verified'}
SUBJECT_FIXTURE_ROLES = {'authoritative-source', 'intentionally-incomplete', 'supporting-source', 'distractor', 'policy', 'runner-only'}
TRI_UNKNOWN = 'unknown'
# Ground-truth models. The key is optional on an experiment; its absence means
# GROUND_TRUTH_CLASSIFICATION, which reproduces the pre-4.2B behaviour exactly. An
# unknown value fails closed. Deliberately a small explicit dispatch, not a registry.
GROUND_TRUTH_CLASSIFICATION = 'classification/v1'
GROUND_TRUTH_CODE_REVIEW = 'code-review-findings/v1'
GROUND_TRUTH_MODELS = (GROUND_TRUTH_CLASSIFICATION, GROUND_TRUTH_CODE_REVIEW)
CODE_REVIEW_FIXTURE_ROLES = {'requirements', 'base-code', 'changed-code', 'change-diff', 'tests', 'ci-evidence', 'implementation-report', 'policy', 'intentionally-incomplete', 'distractor', 'runner-only'}
FIXTURE_ROLES_BY_MODEL = {GROUND_TRUTH_CLASSIFICATION: SUBJECT_FIXTURE_ROLES, GROUND_TRUTH_CODE_REVIEW: CODE_REVIEW_FIXTURE_ROLES}
DEFAULT_DOMAIN = 'Recherche'
DEFAULT_TASK_FAMILY = 'paired claim verification'
RUNNER_SOURCE_ROOT = 'sources'
# code-review-findings/v1 vocabularies
CHANGE_TYPES = ('modified', 'added', 'deleted')
FINDING_SEVERITIES = {'blocker', 'should-fix', 'note'}
FORBIDDEN_FINDING_OUTCOMES = {'false-positive', 'hard-failure'}
ACCEPTANCE_STATUSES = {'satisfied', 'partial', 'missing', 'not-checkable'}
RELEASE_VERDICTS = {'approved', 'approved-with-notes', 'not-approved', 'open-questions-remain'}
# A change set contains changed files; some of them are test files. The role says what
# kind of artifact it is, the change set says that it changed, so a `tests` fixture is
# valid on either side of a change-set entry.
CHANGE_ROLES_FOR_REF = {'diff_ref': {'change-diff'}, 'base_ref': {'base-code', 'tests'}, 'head_ref': {'changed-code', 'tests'}}
DIFF_CONTEXT_LINES = 3
NULL_DIFF_LABEL = '/dev/null'
# Precommitted judge policy for code-review-findings/v1. These are frozen before any
# execution: an experiment that omits or reshapes them is rejected rather than silently
# defaulted, because a policy invented after a response is exactly what the phase forbids.
FINDING_SCOPE_VALUE = 'exhaustive-for-review-significant-findings'
UNLISTED_RULE_OUTCOMES = {1: 'hard-failure', 2: 'false-positive', 3: 'ground_truth_incomplete / adjudication_required'}
UNLISTED_RULE_3_HANDLING_CONCEPTS = {'no spontaneous reward': ('reward',), 'no spontaneous penalty': ('penalty',), 'pair comparison must not be closed': ('must not be closed',)}
PER_FINDING_VALUES = {'hit', 'miss', 'false-positive', 'hard-failure', 'adjudication-required'}
PER_DIMENSION_VALUES = {'pass', 'partial', 'fail', 'unverifiable'}
FORBIDDEN_SCORING_CONCEPTS = {'aggregate score': ('aggregate',), 'weighted score': ('weighted',), 'ranking': ('ranking',), 'single-number overall score': ('single number', 'single-number')}
# Unambiguous experiment-disclosure markers. Deliberately narrow: an output may discuss
# a skill, a baseline or an instruction in ordinary subject-matter language without
# revealing that it is one arm of a controlled experiment. Only the pairing of an arm
# name with an experiment-design noun counts, plus the treatment instruction artifact
# itself and the pinned target-skill identifier.
DISCLOSURE_ARMS = ('skill', 'baseline', 'treatment', 'control')
DISCLOSURE_NOUNS = ('treatment', 'variant', 'condition', 'arm', 'group', 'instruction', 'instruction file')
# Nouns that turn a bare target-skill mention into an experimental-context disclosure even
# when an experiment opts into allowing the bare id. Short connectors are tolerated so
# that "code-review als Skill" is caught as well as "code-review skill".
DISCLOSURE_SKILL_NOUNS = DISCLOSURE_NOUNS + ('skill', 'skills', 'anweisung')
DISCLOSURE_CONNECTORS = ('als', 'as', 'the', 'a', 'an', 'den', 'die', 'das', 'dem', 'ein', 'eine', 'einen')
DISCLOSURE_PHRASES = (
    'treatment instruction', 'skill instruction', 'instruction artifact',
    'with-vs-without', 'with vs without', 'a/b test', 'ab test',
    'i was given the skill', 'i was not given the skill',
)
TREATMENT_INSTRUCTION_DIR = 'instructions/'


def _skill_id_noun_pattern(target_skill: str) -> re.Pattern[str]:
    """Match the target-skill id in skill-instruction or experiment-design context.

    Four shapes, all narrow and all anchored on a known disclosure noun:
    id + noun, id + connector + noun, id + hyphen/compound separator + noun, and the
    reversed noun + id. The bare id on its own is deliberately not matched here, so an
    opted-in experiment keeps ordinary domain vocabulary usable.
    """
    skill = re.escape(target_skill)
    connectors = '|'.join(re.escape(c) for c in DISCLOSURE_CONNECTORS)
    nouns = '|'.join(re.escape(n) for n in sorted(DISCLOSURE_SKILL_NOUNS, key=len, reverse=True))
    separator = r'[-\s]+'
    forward = rf'\b{skill}{separator}(?:(?:{connectors}){separator})?(?:{nouns})\b'
    reverse = rf'\b(?:{nouns})\s+{skill}\b'
    return re.compile(f'(?:{forward})|(?:{reverse})')


def _treatment_disclosed(text: str, target_skill: str, allow_bare_target_skill_id: bool = False) -> bool:
    """Detect an unambiguous disclosure of the experimental treatment in runner output.

    Narrow by design: ordinary use of the word "skill" or "baseline" is not a
    disclosure. An arm name combined with an experiment-design noun is, as are the
    treatment instruction artifact and the pinned target-skill identifier.

    With ``allow_bare_target_skill_id`` an experiment may opt into treating the bare
    target-skill id as ordinary subject-matter vocabulary, which a domain such as code
    review needs. The opt-in is narrow: the id in experimental or skill-instruction
    context still discloses, and every other rule is untouched. Default False, so an
    experiment that does not configure it behaves exactly as before.
    """
    lower = text.lower()
    skill = (target_skill or '').lower()
    if skill:
        if not allow_bare_target_skill_id:
            if skill in lower:
                return True
        elif _skill_id_noun_pattern(skill).search(lower):
            return True
    if TREATMENT_INSTRUCTION_DIR in lower or 'skill.md' in lower:
        return True
    if any(phrase in lower for phrase in DISCLOSURE_PHRASES):
        return True
    return any(f'{arm} {noun}' in lower for arm in DISCLOSURE_ARMS for noun in DISCLOSURE_NOUNS)


def _safe_rel(raw: str, label: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or '..' in path.parts or (not raw.strip()):
        raise HarnessError(f'{label} must be a safe repository-relative path: {raw!r}')
    return path

def _validate_tri(value: Any, label: str) -> bool | str:
    if value is True or value is False or value == TRI_UNKNOWN:
        return value
    raise HarnessError(f'{label} must be true, false or unknown')

def _tri_all(values: list[bool | str]) -> bool | str:
    if False in values:
        return False
    if TRI_UNKNOWN in values:
        return TRI_UNKNOWN
    return True

def _known_equal(values: list[str]) -> bool | str:
    if not values or any((not value or value == TRI_UNKNOWN for value in values)):
        return TRI_UNKNOWN
    return len(set(values)) == 1

def _ground_truth_model(experiment: dict[str, Any]) -> str:
    """Resolve the experiment's ground-truth model. Absent means the legacy model."""
    model = experiment.get('ground_truth_model', GROUND_TRUTH_CLASSIFICATION)
    if model not in GROUND_TRUTH_MODELS:
        raise HarnessError(f'unsupported ground_truth_model {model!r}; supported: {list(GROUND_TRUTH_MODELS)}')
    return str(model)

def _allowed_roles(model: str) -> set[str]:
    return FIXTURE_ROLES_BY_MODEL[model]

def _fixture_path(item: Any, case_id: str, roles: set[str] | None = None) -> str:
    if not isinstance(item, dict):
        raise HarnessError(f'{case_id}: each fixture must be a mapping with path and role')
    raw = item.get('path')
    role = item.get('role')
    if not isinstance(raw, str) or not raw.strip():
        raise HarnessError(f'{case_id}: fixture path must be a non-empty string')
    _safe_rel(raw, f'{case_id}.fixture.path')
    if role not in (SUBJECT_FIXTURE_ROLES if roles is None else roles):
        raise HarnessError(f'{case_id}: fixture role {role!r} is not a supported runner-visible Behavioral-Harness role')
    return raw

def _fixture_role(item: Any, case_id: str, roles: set[str] | None = None) -> str:
    _fixture_path(item, case_id, roles)
    return str(item['role'])

def _runner_path(item: Any, case_id: str) -> str | None:
    """Validate an optional explicit runner-package path for one fixture.

    Absent means the fixture keeps the numbered `sources/NN-<basename>` materialisation,
    so every experiment authored before 4.2B is unaffected. A declared path may only
    expose the natural artifact structure; it must never carry judge-only role
    information or anything about the treatment.
    """
    raw = item.get('runner_path')
    if raw is None:
        return None
    if not isinstance(raw, str) or not raw.strip() or raw != raw.strip():
        raise HarnessError(f'{case_id}: runner_path must be a non-empty unpadded string')
    rel = _safe_rel(raw, f'{case_id}.runner_path')
    parts = rel.parts
    if parts[0] != RUNNER_SOURCE_ROOT or len(parts) < 2:
        raise HarnessError(f'{case_id}: runner_path must live under {RUNNER_SOURCE_ROOT}/: {raw!r}')
    if raw.startswith(TREATMENT_INSTRUCTION_DIR) or TREATMENT_INSTRUCTION_DIR.rstrip('/') in parts:
        raise HarnessError(f'{case_id}: runner_path must not collide with {TREATMENT_INSTRUCTION_DIR}: {raw!r}')
    leaked = set(parts) & (SUBJECT_FIXTURE_ROLES | CODE_REVIEW_FIXTURE_ROLES | set(TREATMENTS))
    if leaked:
        raise HarnessError(f'{case_id}: runner_path must not encode a judge role or treatment: {sorted(leaked)}')
    return rel.as_posix()

def _runner_path_map(case: dict[str, Any], case_id: str) -> dict[str, str]:
    """Map declared fixture path -> runner path, rejecting duplicate runner paths."""
    mapping: dict[str, str] = {}
    for item in case['fixtures']:
        declared = _runner_path(item, case_id)
        if declared is None:
            continue
        if declared in mapping.values():
            raise HarnessError(f'{case_id}: duplicate runner_path {declared!r}')
        mapping[str(item['path'])] = declared
    return mapping

def _validate_classification(case_id: str, truth: dict[str, Any]) -> None:
    if 'expected_classification' in truth:
        raise HarnessError(f'{case_id}: expected_classification is deprecated for paired pilots; use ground_truth.classification')
    classification = truth.get('classification')
    if not isinstance(classification, dict):
        raise HarnessError(f'{case_id}: ground_truth.classification must be a mapping')
    preferred = classification.get('preferred')
    if preferred not in CLASSIFICATION_LABELS:
        raise HarnessError(f'{case_id}: invalid preferred classification {preferred!r}')
    alternatives = classification.get('accepted_alternatives', {})
    if not isinstance(alternatives, dict):
        raise HarnessError(f'{case_id}: accepted_alternatives must be a mapping')
    for label, spec in alternatives.items():
        if label not in CLASSIFICATION_LABELS:
            raise HarnessError(f'{case_id}: invalid alternative classification {label!r}')
        if label == preferred:
            raise HarnessError(f'{case_id}: preferred classification must not be repeated as an alternative')
        if not isinstance(spec, dict):
            raise HarnessError(f'{case_id}: alternative classification {label!r} must contain conditions')
        conditions = spec.get('conditions')
        if not isinstance(conditions, list) or not conditions or (not all((isinstance(item, str) and item.strip() for item in conditions))):
            raise HarnessError(f'{case_id}: alternative classification {label!r} requires at least one explicit condition')
    disallowed = classification.get('disallowed')
    if not isinstance(disallowed, list) or len(disallowed) != len(set(disallowed)) or any((label not in CLASSIFICATION_LABELS for label in disallowed)):
        raise HarnessError(f'{case_id}: classification.disallowed must contain unique known labels')
    accepted = {preferred, *alternatives.keys()}
    disallowed_set = set(disallowed)
    if accepted & disallowed_set:
        raise HarnessError(f'{case_id}: accepted and disallowed classification labels overlap')
    if accepted | disallowed_set != CLASSIFICATION_LABELS:
        missing = sorted(CLASSIFICATION_LABELS - accepted - disallowed_set)
        extra = sorted((accepted | disallowed_set) - CLASSIFICATION_LABELS)
        raise HarnessError(f'{case_id}: classification metadata must partition all known labels; missing={missing}, extra={extra}')

def _require(container: Any, keys: tuple[str, ...], label: str) -> None:
    if not isinstance(container, dict):
        raise HarnessError(f'{label} must be a mapping')
    for key in keys:
        if key not in container:
            raise HarnessError(f'{label} missing {key}')

def _nonempty_strings(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
        raise HarnessError(f'{label} must be a non-empty list of non-empty strings')
    return [str(x) for x in value]

def _validate_change_set(case_id: str, truth: dict[str, Any], fixture_roles: dict[str, str]) -> dict[str, Any]:
    """Structural validation of the declared change set. Content is checked at prepare time."""
    change_set = truth.get('change_set')
    _require(change_set, ('diff_ref', 'files'), f'{case_id}.change_set')

    def _ref(raw: Any, kind: str, where: str) -> str:
        if not isinstance(raw, str) or not raw.strip():
            raise HarnessError(f'{where}: {kind} must be a non-empty string')
        _safe_rel(raw, where)
        if raw not in fixture_roles:
            raise HarnessError(f'{where}: {kind} {raw!r} is not a fixture of this case')
        expected = CHANGE_ROLES_FOR_REF[kind]
        if fixture_roles[raw] not in expected:
            raise HarnessError(f'{where}: {kind} {raw!r} has role {fixture_roles[raw]!r}, expected one of {sorted(expected)}')
        return raw

    _ref(change_set['diff_ref'], 'diff_ref', f'{case_id}.change_set.diff_ref')
    files = change_set['files']
    if not isinstance(files, list) or not files:
        raise HarnessError(f'{case_id}.change_set.files must be a non-empty list')
    seen: set[str] = set()
    for entry in files:
        _require(entry, ('logical_path', 'change_type', 'base_ref', 'head_ref'), f'{case_id}.change_set.files[]')
        logical = entry['logical_path']
        if not isinstance(logical, str) or not logical.strip():
            raise HarnessError(f'{case_id}: logical_path must be a non-empty string')
        _safe_rel(logical, f'{case_id}.logical_path')
        if logical in seen:
            raise HarnessError(f'{case_id}: duplicate logical_path {logical!r}')
        seen.add(logical)
        change_type = entry['change_type']
        if change_type not in CHANGE_TYPES:
            raise HarnessError(f'{case_id}: change_type {change_type!r} must be one of {list(CHANGE_TYPES)}')
        where = f'{case_id}.change_set[{logical}]'
        for kind, required in (('base_ref', change_type in ('modified', 'deleted')), ('head_ref', change_type in ('modified', 'added'))):
            value = entry[kind]
            if required:
                _ref(value, kind, where)
            elif value is not None:
                raise HarnessError(f'{where}: {change_type} must not carry {kind}')
    return change_set

def _validate_findings(case_id: str, truth: dict[str, Any], fixture_paths: set[str]) -> None:
    ids: set[str] = set()

    def _claim_id(entry: Any, label: str) -> str:
        _require(entry, ('finding_id',), label)
        finding_id = entry['finding_id']
        if not isinstance(finding_id, str) or not finding_id.strip():
            raise HarnessError(f'{label}: finding_id must be a non-empty string')
        if finding_id in ids:
            raise HarnessError(f'{case_id}: duplicate finding id {finding_id!r}')
        ids.add(finding_id)
        return finding_id

    expected = truth.get('expected_findings')
    if not isinstance(expected, list) or not expected:
        raise HarnessError(f'{case_id}: expected_findings must be a non-empty list')
    for entry in expected:
        label = f'{case_id}.expected_findings[]'
        finding_id = _claim_id(entry, label)
        _require(entry, ('category', 'severity', 'required', 'locations', 'evidence', 'detection_criteria', 'rationale'), f'{case_id}.{finding_id}')
        if entry['severity'] not in FINDING_SEVERITIES:
            raise HarnessError(f'{case_id}.{finding_id}: severity {entry["severity"]!r} must be one of {sorted(FINDING_SEVERITIES)}')
        if entry['required'] is not True:
            raise HarnessError(f'{case_id}.{finding_id}: expected findings must be required: true')
        _nonempty_strings(entry['evidence'], f'{case_id}.{finding_id}.evidence')
        _nonempty_strings(entry['detection_criteria'], f'{case_id}.{finding_id}.detection_criteria')
        locations = entry['locations']
        if not isinstance(locations, list) or not locations:
            raise HarnessError(f'{case_id}.{finding_id}: locations must be a non-empty list')
        for location in locations:
            _require(location, ('fixture',), f'{case_id}.{finding_id}.locations[]')
            if location['fixture'] not in fixture_paths:
                raise HarnessError(f'{case_id}.{finding_id}: location {location["fixture"]!r} is not a fixture of this case')

    for entry in truth.get('acceptable_additional_findings') or []:
        finding_id = _claim_id(entry, f'{case_id}.acceptable_additional_findings[]')
        _require(entry, ('claim', 'evidence'), f'{case_id}.{finding_id}')
        _nonempty_strings(entry['evidence'], f'{case_id}.{finding_id}.evidence')
        band = entry.get('severity_band')
        if band is not None:
            for value in _nonempty_strings(band, f'{case_id}.{finding_id}.severity_band'):
                if value not in FINDING_SEVERITIES:
                    raise HarnessError(f'{case_id}.{finding_id}: severity_band value {value!r} is not a known severity')

    forbidden = truth.get('forbidden_findings')
    if not isinstance(forbidden, list) or not forbidden:
        raise HarnessError(f'{case_id}: forbidden_findings must be a non-empty list')
    for entry in forbidden:
        finding_id = _claim_id(entry, f'{case_id}.forbidden_findings[]')
        _require(entry, ('claim', 'why_wrong', 'severity_if_raised'), f'{case_id}.{finding_id}')
        if entry['severity_if_raised'] not in FORBIDDEN_FINDING_OUTCOMES:
            raise HarnessError(f'{case_id}.{finding_id}: severity_if_raised must be one of {sorted(FORBIDDEN_FINDING_OUTCOMES)}')

def _validate_code_review_truth(case_id: str, case: dict[str, Any], truth: dict[str, Any]) -> None:
    """Ground-truth validation for code-review-findings/v1."""
    if 'classification' in truth:
        raise HarnessError(f'{case_id}: classification is not part of code-review-findings/v1 ground truth')
    for key in ('change_set', 'expected_findings', 'acceptable_additional_findings', 'forbidden_findings', 'acceptance_criteria', 'release_calibration', 'known_traps', 'allowed_uncertainty', 'hard_failures'):
        if key not in truth:
            raise HarnessError(f'{case_id}: ground_truth missing {key}')
    roles = _allowed_roles(GROUND_TRUTH_CODE_REVIEW)
    fixture_roles = {_fixture_path(item, case_id, roles): _fixture_role(item, case_id, roles) for item in case['fixtures']}
    _validate_change_set(case_id, truth, fixture_roles)
    _validate_findings(case_id, truth, set(fixture_roles))

    criteria = truth['acceptance_criteria']
    if not isinstance(criteria, list) or not criteria:
        raise HarnessError(f'{case_id}: acceptance_criteria must be a non-empty list')
    seen: set[str] = set()
    for entry in criteria:
        _require(entry, ('criterion_id', 'expected_status', 'evidence'), f'{case_id}.acceptance_criteria[]')
        criterion_id = str(entry['criterion_id'])
        if criterion_id in seen:
            raise HarnessError(f'{case_id}: duplicate acceptance criterion {criterion_id!r}')
        seen.add(criterion_id)
        if entry['expected_status'] not in ACCEPTANCE_STATUSES:
            raise HarnessError(f'{case_id}.{criterion_id}: expected_status {entry["expected_status"]!r} must be one of {sorted(ACCEPTANCE_STATUSES)}')
        _nonempty_strings(entry['evidence'], f'{case_id}.{criterion_id}.evidence')

    release = truth['release_calibration']
    _require(release, ('expected_verdict', 'forbidden_verdicts'), f'{case_id}.release_calibration')
    verdict = release['expected_verdict']
    if verdict not in RELEASE_VERDICTS:
        raise HarnessError(f'{case_id}: expected_verdict {verdict!r} must be one of {sorted(RELEASE_VERDICTS)}')
    forbidden_verdicts = release['forbidden_verdicts']
    if not isinstance(forbidden_verdicts, list) or len(forbidden_verdicts) != len(set(forbidden_verdicts)):
        raise HarnessError(f'{case_id}: forbidden_verdicts must be a list of unique verdicts')
    for value in forbidden_verdicts:
        if value not in RELEASE_VERDICTS:
            raise HarnessError(f'{case_id}: forbidden verdict {value!r} is not a known verdict')
    if verdict in set(forbidden_verdicts):
        raise HarnessError(f'{case_id}: expected_verdict must not also be forbidden')
    for key in ('known_traps', 'allowed_uncertainty', 'hard_failures'):
        if not isinstance(truth[key], list):
            raise HarnessError(f'{case_id}: {key} must be a list')

def reconstruct_change_diff(case: dict[str, Any], truth: dict[str, Any], repo_root: Path) -> str:
    """Rebuild the expected unified diff from the declared base/head artifacts.

    Deterministic and stdlib-only: the gate must not depend on an external diff binary.
    Files are emitted in sorted logical-path order; an added file's base side and a
    deleted file's head side are `/dev/null`, matching the declared change_type.
    """
    chunks: list[str] = []
    for entry in sorted(truth['change_set']['files'], key=lambda item: str(item['logical_path'])):
        logical = str(entry['logical_path'])
        base_ref, head_ref = entry['base_ref'], entry['head_ref']
        base_lines = (repo_root / _safe_rel(str(base_ref), 'base_ref')).read_text(encoding='utf-8').splitlines(keepends=True) if base_ref else []
        head_lines = (repo_root / _safe_rel(str(head_ref), 'head_ref')).read_text(encoding='utf-8').splitlines(keepends=True) if head_ref else []
        from_label = f'base/{logical}' if base_ref else NULL_DIFF_LABEL
        to_label = f'head/{logical}' if head_ref else NULL_DIFF_LABEL
        chunks.append(''.join(difflib.unified_diff(base_lines, head_lines, fromfile=from_label, tofile=to_label, n=DIFF_CONTEXT_LINES)))
    return ''.join(chunks)

def _assert_change_set_materialized(case_id: str, case: dict[str, Any], truth: dict[str, Any], repo_root: Path) -> None:
    """Prepare-time gate: the committed diff must match the declared change set exactly."""
    for entry in truth['change_set']['files']:
        logical, change_type = str(entry['logical_path']), str(entry['change_type'])
        for kind in ('base_ref', 'head_ref'):
            ref = entry[kind]
            if ref is None:
                continue
            if not (repo_root / _safe_rel(str(ref), kind)).is_file():
                raise HarnessError(f'{case_id}: {change_type} {logical}: {kind} {ref} is not a file')
    diff_path = repo_root / _safe_rel(str(truth['change_set']['diff_ref']), 'diff_ref')
    if not diff_path.is_file():
        raise HarnessError(f'{case_id}: diff_ref {diff_path} is not a file')
    actual = diff_path.read_text(encoding='utf-8')
    expected = reconstruct_change_diff(case, truth, repo_root)
    if actual != expected:
        raise HarnessError(f'{case_id}: change diff does not match the declared change set; the diff is stale or the change_set is wrong')

def _concepts_covered(entries: list[str], concepts: dict[str, tuple[str, ...]], label: str) -> None:
    """Each required concept must be carried by at least one entry. Structural, not prose-exact."""
    lowered = [entry.lower() for entry in entries]
    for name, tokens in concepts.items():
        if not any(any(token in entry for token in tokens) for entry in lowered):
            raise HarnessError(f'{label} must still record {name!r}')

def _validate_code_review_evaluation_policy(experiment: dict[str, Any]) -> None:
    """Fail closed on a missing or reshaped judge policy for code-review-findings/v1.

    The point is to freeze the declared precedence and scoring vocabulary before any
    execution. A code-review experiment without them must not load, let alone prepare.
    """
    scope = experiment.get('finding_scope')
    _require(scope, ('intended_ground_truth',), 'finding_scope')
    if scope['intended_ground_truth'] != FINDING_SCOPE_VALUE:
        raise HarnessError(f'finding_scope.intended_ground_truth must be {FINDING_SCOPE_VALUE!r} for this pilot')

    rules = experiment.get('unlisted_finding_rule')
    if not isinstance(rules, list) or len(rules) != len(UNLISTED_RULE_OUTCOMES):
        raise HarnessError(f'unlisted_finding_rule must contain exactly {len(UNLISTED_RULE_OUTCOMES)} rules')
    by_order: dict[int, dict[str, Any]] = {}
    for rule in rules:
        _require(rule, ('order', 'condition', 'outcome'), 'unlisted_finding_rule[]')
        order = rule['order']
        if order not in UNLISTED_RULE_OUTCOMES:
            raise HarnessError(f'unlisted_finding_rule order {order!r} must be one of {sorted(UNLISTED_RULE_OUTCOMES)}')
        if order in by_order:
            raise HarnessError(f'duplicate unlisted_finding_rule order {order}')
        by_order[order] = rule
    for order, outcome in UNLISTED_RULE_OUTCOMES.items():
        if by_order[order]['outcome'] != outcome:
            raise HarnessError(f'unlisted_finding_rule order {order} must have outcome {outcome!r}, not {by_order[order]["outcome"]!r}')
        if not str(by_order[order]['condition']).strip():
            raise HarnessError(f'unlisted_finding_rule order {order} must state a condition')
    handling = by_order[3].get('handling')
    if not isinstance(handling, list) or not handling:
        raise HarnessError('unlisted_finding_rule order 3 must carry handling')
    _concepts_covered(_nonempty_strings(handling, 'unlisted_finding_rule order 3 handling'), UNLISTED_RULE_3_HANDLING_CONCEPTS, 'unlisted_finding_rule order 3 handling')

    scoring = experiment.get('judge_scoring')
    _require(scoring, ('per_finding', 'per_dimension', 'forbidden'), 'judge_scoring')
    for key, expected in (('per_finding', PER_FINDING_VALUES), ('per_dimension', PER_DIMENSION_VALUES)):
        _require(scoring[key], ('values',), f'judge_scoring.{key}')
        values = scoring[key]['values']
        if not isinstance(values, list) or set(values) != expected or len(values) != len(expected):
            raise HarnessError(f'judge_scoring.{key}.values must be exactly {sorted(expected)}')
    _concepts_covered(_nonempty_strings(scoring['forbidden'], 'judge_scoring.forbidden'), FORBIDDEN_SCORING_CONCEPTS, 'judge_scoring.forbidden')

def _disclosure_opt_in(experiment: dict[str, Any]) -> dict[str, bool] | None:
    """Resolve the coordinator-only disclosure opt-in, rejecting non-boolean values.

    Truthiness would silently turn the string "false" into an enabled opt-in, which
    would weaken a blindness guard by typo. Absent means no key at all, so a pre-4.2B
    experiment produces a byte-identical control document.
    """
    disclosure = experiment.get('treatment_disclosure')
    if disclosure is None:
        return None
    if not isinstance(disclosure, dict):
        raise HarnessError('treatment_disclosure must be a mapping')
    value = disclosure.get('allow_bare_target_skill_id_in_output', False)
    if not isinstance(value, bool):
        raise HarnessError(f'treatment_disclosure.allow_bare_target_skill_id_in_output must be a boolean, got {type(value).__name__}: {value!r}')
    return {'allow_bare_target_skill_id_in_output': value}

def load_paired_experiment(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise HarnessError('paired experiment must be a mapping')
    if data.get('contract') != PAIR_CONTRACT:
        raise HarnessError(f'paired experiment contract must be {PAIR_CONTRACT}')
    for key in ('experiment_id', 'repository', 'pinned_commit', 'target_skill', 'evaluation_dimensions', 'cases'):
        if key not in data:
            raise HarnessError(f'paired experiment missing {key}')
    target = data.get('target_skill')
    if not isinstance(target, dict) or not target.get('id') or (not target.get('path')):
        raise HarnessError('target_skill must contain id and path')
    _safe_rel(str(target['path']), 'target_skill.path')
    dimensions = data.get('evaluation_dimensions')
    if not isinstance(dimensions, list) or not dimensions:
        raise HarnessError('evaluation_dimensions must be a non-empty list')
    model = _ground_truth_model(data)
    roles = _allowed_roles(model)
    if model == GROUND_TRUTH_CODE_REVIEW:
        _validate_code_review_evaluation_policy(data)
    _disclosure_opt_in(data)
    cases = data.get('cases')
    if not isinstance(cases, list) or not cases:
        raise HarnessError('paired experiment cases must be a non-empty list')
    seen: set[str] = set()
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            raise HarnessError(f'case[{index}] must be a mapping')
        for key in ('case_id', 'user_prompt', 'fixtures', 'ground_truth'):
            if key not in case:
                raise HarnessError(f'case[{index}] missing {key}')
        case_id = str(case['case_id'])
        if case_id in seen:
            raise HarnessError(f'duplicate paired case id {case_id}')
        seen.add(case_id)
        if not str(case['user_prompt']).strip():
            raise HarnessError(f'{case_id}: user_prompt must not be empty')
        fixtures = case.get('fixtures')
        if not isinstance(fixtures, list) or not fixtures:
            raise HarnessError(f'{case_id}: fixtures must be a non-empty list')
        fixture_paths = [_fixture_path(item, case_id, roles) for item in fixtures]
        if len(fixture_paths) != len(set(fixture_paths)):
            raise HarnessError(f'{case_id}: fixture paths must be unique')
        _runner_path_map(case, case_id)
        truth = case.get('ground_truth')
        if not isinstance(truth, dict):
            raise HarnessError(f'{case_id}: ground_truth must be a mapping')
        if model == GROUND_TRUTH_CODE_REVIEW:
            _validate_code_review_truth(case_id, case, truth)
        else:
            for key in ('classification', 'relevant_evidence', 'decisive_reason', 'known_traps', 'allowed_uncertainty', 'hard_failures'):
                if key not in truth:
                    raise HarnessError(f'{case_id}: ground_truth missing {key}')
            _validate_classification(case_id, truth)
    repetitions = int(data.get('recommended_repetitions', 1))
    if repetitions < 2:
        raise HarnessError('recommended_repetitions must be at least 2 for a paired stochastic pilot')
    return data

def _get_case(experiment: dict[str, Any], case_id: str) -> dict[str, Any]:
    matches = [case for case in experiment['cases'] if str(case.get('case_id')) == case_id]
    if len(matches) != 1:
        raise HarnessError(f'expected exactly one paired case {case_id}, found {len(matches)}')
    return copy.deepcopy(matches[0])

_MODEL_JUDGE_INSTRUCTION = {
    GROUND_TRUTH_CLASSIFICATION: 'Apply classification alternatives only when their precommitted conditions are explicitly satisfied.',
    GROUND_TRUTH_CODE_REVIEW: "Apply each precommitted finding's detection criteria and the precommitted unlisted-finding precedence exactly. Do not create new judging rules after seeing a response.",
}

def _opaque_response_id(experiment_id: str, case_id: str, repetition: int, treatment: str, blind_seed: str) -> str:
    payload = f'{experiment_id}|{case_id}|{repetition}|{treatment}|{blind_seed}'.encode('utf-8')
    return 'R-' + hashlib.sha256(payload).hexdigest()[:16]

def _treatment_order(experiment_id: str, case_id: str, repetition: int, blind_seed: str) -> tuple[str, str]:
    """Alternate treatments by repetition; blind seed deterministically selects which starts first."""
    payload = f'{experiment_id}|{case_id}|{blind_seed}|treatment-order-v1'.encode('utf-8')
    seed_bit = hashlib.sha256(payload).digest()[0] & 1
    first_index = (seed_bit + repetition - 1) % 2
    first = TREATMENTS[first_index]
    second = TREATMENTS[1 - first_index]
    return (first, second)

def _synthetic_matrix(experiment: dict[str, Any], case: dict[str, Any], response_id: str, treatment: str) -> dict[str, Any]:
    target = str(experiment['target_skill']['id'])
    skill_path = str(experiment['target_skill']['path'])
    case_id = str(case['case_id'])
    roles = _allowed_roles(_ground_truth_model(experiment))
    fixtures = [_fixture_path(item, case_id, roles) for item in case['fixtures']]
    if treatment == 'skill':
        fixtures.append(skill_path)
        primary = target
        forbidden: list[str] = []
    else:
        primary = 'none/direct-response'
        forbidden = [target]
    truth = case['ground_truth']
    return {'schema_version': 1, 'repository': str(experiment['repository']), 'pinned_commit': str(experiment['pinned_commit']), 'tests': [{'test_id': response_id, 'domain': str(experiment.get('domain', DEFAULT_DOMAIN)), 'aufgabenfamilie': str(experiment.get('task_family', DEFAULT_TASK_FAMILY)), 'testebenen': ['behavior', 'outcome'], 'schwierigkeit': case.get('difficulty', 'mittel'), 'nutzerprompt': case['user_prompt'], 'fixtures': fixtures, 'erwarteter_primaerskill': primary, 'erlaubte_secondary_skills': [], 'verbotene_skills': forbidden, 'erwarteter_workflow': 'none', 'erwartete_evidence': ['use only package-local source fixtures'], 'erwarteter_status': 'pass', 'output_kriterien': [str(item.get('id', item)) if isinstance(item, dict) else str(item) for item in experiment['evaluation_dimensions']], 'failure_modes': [str(x) for x in truth.get('hard_failures', [])], 'routing_kriterien': ['target skill is available only in the skill treatment' if treatment == 'skill' else 'target skill must remain unavailable in the baseline treatment'], 'bewertungsmethode': 'paired treatment-blind judge against precommitted ground truth', 'blindness_klasse': 'paired-treatment-blind'}]}

def _role_overrides(response_id: str, case: dict[str, Any], skill_path: str, treatment: str, roles: set[str] | None = None) -> dict[str, Any]:
    case_id = str(case['case_id'])
    case_roles: dict[str, Any] = {}
    for item in case['fixtures']:
        path = _fixture_path(item, case_id, roles)
        case_roles[path] = {'role': _fixture_role(item, case_id, roles), 'intentionally_missing_evidence': []}
    if treatment == 'skill':
        case_roles[skill_path] = {'role': 'skill-instruction', 'intentionally_missing_evidence': []}
    return {'cases': {response_id: case_roles}}

def _recompute_hashes(compiled: dict[str, Any]) -> None:
    compiled['hashes']['execution_view_hash'] = hash_object(compiled['execution_view'])
    compiled['hashes']['judge_view_hash'] = hash_object(compiled['judge_view'])

def _prepare_compiled_variant(experiment: dict[str, Any], case: dict[str, Any], response_id: str, treatment: str, repo_root: Path) -> dict[str, Any]:
    target = str(experiment['target_skill']['id'])
    skill_path = str(experiment['target_skill']['path'])
    roles = _allowed_roles(_ground_truth_model(experiment))
    declared_runner_paths = _runner_path_map(case, str(case['case_id']))
    matrix = _synthetic_matrix(experiment, case, response_id, treatment)
    compiled = compile_case(matrix, response_id, repo_root, repo_commit=str(experiment['pinned_commit']), role_overrides=_role_overrides(response_id, case, skill_path, treatment, roles))
    copy_plan: list[dict[str, str]] = []
    common_index = 0
    for exec_rec, judge_rec in zip(compiled['execution_view']['fixtures'], compiled['judge_view']['fixtures']):
        original = str(judge_rec['path'])
        if original == skill_path:
            runner_rel = f'instructions/{Path(skill_path).name}'
            kind = 'skill-instruction'
        elif original in declared_runner_paths:
            runner_rel = declared_runner_paths[original]
            kind = 'subject-source'
        else:
            common_index += 1
            runner_rel = f'sources/{common_index:02d}-{Path(original).name}'
            kind = 'subject-source'
        exec_rec['path'] = runner_rel
        copy_plan.append({'source': original, 'runner_path': runner_rel, 'kind': kind, 'fixture_id': str(exec_rec['fixture_id'])})
    compiled['execution_view']['runtime'] = {'fresh_runner_context_required': True, 'allowed_tools': 'package-read-only', 'network_access': False, 'repository_access': False, 'source_root': 'sources', 'skill_instruction': f'instructions/{Path(skill_path).name}' if treatment == 'skill' else None, 'runner_adapter_required': True}
    compiled['judge_view'].update({'experiment_id': str(experiment['experiment_id']), 'paired_case_id': str(case['case_id']), 'treatment': treatment})
    compiled['readiness'].update({'package_only_sources': True, 'network_disabled_by_contract': True, 'repository_access_disabled_by_contract': True})
    compiled['_copy_plan'] = copy_plan
    compiled['_treatment'] = treatment
    compiled['_target_skill'] = target
    _recompute_hashes(compiled)
    return compiled

def _subject_source_hashes(compiled: dict[str, Any]) -> dict[str, str]:
    return {item['runner_path']: compiled['hashes']['fixture_hashes'][item['fixture_id']] for item in compiled['_copy_plan'] if item['kind'] == 'subject-source'}

def _subject_role_map(compiled: dict[str, Any]) -> dict[str, str]:
    skill_paths = {item['source'] for item in compiled['_copy_plan'] if item['kind'] == 'skill-instruction'}
    return {str(record['path']): str(record['role']) for record in compiled['judge_view'].get('fixtures', []) if str(record['path']) not in skill_paths}

def _normalized_runtime(execution: dict[str, Any]) -> dict[str, Any]:
    runtime = copy.deepcopy(execution.get('runtime') or {})
    runtime.pop('skill_instruction', None)
    return runtime

def compile_paired_case(experiment: dict[str, Any], case_id: str, repo_root: Path, repetition: int, blind_seed: str) -> dict[str, Any]:
    if repetition < 1:
        raise HarnessError('repetition must be >= 1')
    if not blind_seed:
        raise HarnessError('blind_seed must not be empty')
    model = _ground_truth_model(experiment)
    roles = _allowed_roles(model)
    case = _get_case(experiment, case_id)
    if model == GROUND_TRUTH_CODE_REVIEW:
        _assert_change_set_materialized(case_id, case, case['ground_truth'], repo_root)
    response_ids = {treatment: _opaque_response_id(str(experiment['experiment_id']), case_id, repetition, treatment, blind_seed) for treatment in TREATMENTS}
    if len(set(response_ids.values())) != 2:
        raise HarnessError('opaque response id collision')
    compiled = {treatment: _prepare_compiled_variant(experiment, case, response_ids[treatment], treatment, repo_root) for treatment in TREATMENTS}
    prompt_hashes = {hash_object(compiled[t]['execution_view']['user_prompt']) for t in TREATMENTS}
    if len(prompt_hashes) != 1:
        raise HarnessError('paired variants do not have identical user prompts')
    common_source_hashes: dict[str, str] | None = None
    common_source_roles: dict[str, str] | None = None
    runtime_hashes: set[str] = set()
    for treatment in TREATMENTS:
        current_hashes = _subject_source_hashes(compiled[treatment])
        current_roles = _subject_role_map(compiled[treatment])
        runtime_hashes.add(hash_object(_normalized_runtime(compiled[treatment]['execution_view'])))
        if common_source_hashes is None:
            common_source_hashes = current_hashes
            common_source_roles = current_roles
        else:
            if current_hashes != common_source_hashes:
                raise HarnessError('paired variants do not have identical subject-source hashes')
            if current_roles != common_source_roles:
                raise HarnessError('paired variants do not have identical subject-source roles')
    if len(runtime_hashes) != 1:
        raise HarnessError('paired variants do not have identical prepared runtime contracts')
    target_skill_path = repo_root / _safe_rel(str(experiment['target_skill']['path']), 'target_skill.path')
    if not target_skill_path.is_file():
        raise HarnessError(f'target skill missing at {target_skill_path}')
    treatment_order = _treatment_order(str(experiment['experiment_id']), case_id, repetition, blind_seed)
    execution_order = [response_ids[treatment] for treatment in treatment_order]
    control = {'schema_version': 1, 'contract': CONTROL_CONTRACT, 'experiment_id': str(experiment['experiment_id']), 'case_id': case_id, 'repetition': repetition, 'blind_seed': blind_seed, 'blind_seed_hash': hash_object(blind_seed), 'pinned_commit': str(experiment['pinned_commit']), 'target_skill': str(experiment['target_skill']['id']), 'target_skill_path': str(experiment['target_skill']['path']), 'target_skill_hash': hash_file(target_skill_path), 'response_assignments': {response_ids[t]: t for t in TREATMENTS}, 'execution_order': execution_order, 'shared_user_prompt_hash': next(iter(prompt_hashes)), 'shared_subject_source_hashes': common_source_hashes or {}, 'shared_subject_source_roles': common_source_roles or {}, 'shared_runtime_contract_hash': next(iter(runtime_hashes)), 'independent_variable': 'availability of the target skill instruction only'}
    # Coordinator-only. Never copied into the blind judge contract: it would hint at the
    # treatment mechanism. Absent on an experiment means no key at all, so a pre-4.2B
    # control document is unchanged.
    disclosure = _disclosure_opt_in(experiment)
    if disclosure is not None:
        control['treatment_disclosure'] = disclosure
    judge_contract = {'schema_version': 1, 'contract': BLIND_JUDGE_CONTRACT, 'experiment_id': str(experiment['experiment_id']), 'case_id': case_id, 'response_ids': sorted(response_ids.values()), 'source_roles': [{'path': _fixture_path(item, case_id, roles), 'role': _fixture_role(item, case_id, roles)} for item in case['fixtures']], 'ground_truth': copy.deepcopy(case['ground_truth']), 'evaluation_dimensions': copy.deepcopy(experiment['evaluation_dimensions']), 'global_hard_failures': copy.deepcopy(experiment.get('global_hard_failures', [])), 'instructions': ['Judge each response independently against the precommitted ground truth before comparing them.', _MODEL_JUDGE_INSTRUCTION[model], 'Do not infer treatment or execution order from style, verbosity or response identifiers.', 'Report dimensions separately; do not collapse them into an opaque total score.', 'Flag any hard failure independently of prose quality.']}
    if model == GROUND_TRUTH_CODE_REVIEW:
        # The precommitted evaluation policy must reach the blind judge, not stay authoring
        # documentation. Legacy contracts gain no new keys.
        judge_contract['ground_truth_model'] = model
        _validate_code_review_evaluation_policy(experiment)
        judge_contract['evaluation_policy'] = {'finding_scope': copy.deepcopy(experiment['finding_scope']), 'unlisted_finding_rule': copy.deepcopy(experiment['unlisted_finding_rule']), 'judge_scoring': copy.deepcopy(experiment['judge_scoring'])}
    return {'control': control, 'judge_contract': judge_contract, 'compiled': compiled}

def write_paired_case(pair: dict[str, Any], repo_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=False)
    dump_yaml(pair['control'], out_dir / 'control.yml')
    dump_yaml(pair['judge_contract'], out_dir / 'judge-contract.yml')
    for treatment in TREATMENTS:
        compiled = pair['compiled'][treatment]
        response_id = str(compiled['execution_view']['test_id'])
        response_dir = out_dir / 'responses' / response_id
        write_prepared_case(compiled, response_dir)
        runner_dir = response_dir / 'runner-package'
        for item in compiled['_copy_plan']:
            src = repo_root / _safe_rel(item['source'], 'copy source')
            dst = runner_dir / item['runner_path']
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        adapter_path = runner_dir / 'adapter-request.yml'
        adapter = load_yaml(adapter_path)
        if not isinstance(adapter, dict):
            raise HarnessError(f'invalid adapter request at {adapter_path}')
        adapter['constraints'] = {'network_access': False, 'repository_access': False, 'readable_roots': ['sources'] + (['instructions'] if treatment == 'skill' else []), 'same_model_and_configuration_across_pair_required': True}
        adapter.setdefault('rules', []).extend(['Use only files inside this runner package; do not access the repository or the web.', 'Do not mention the experiment treatment, baseline/skill condition, or skill file name in the answer.', 'Use a fresh isolated runner context for this response.', 'If pair-method evidence is recorded, report unknown rather than inventing unavailable configuration or isolation evidence.'])
        dump_yaml(adapter, adapter_path)
        assert_runner_package_clean(runner_dir)
    pair_hashes = {'hash_algorithm': 'sha256/canonical-json-v1', 'control_hash': hash_object(pair['control']), 'judge_contract_hash': hash_object(pair['judge_contract']), 'response_prepared_hashes': {str(pair['compiled'][t]['execution_view']['test_id']): hash_object(pair['compiled'][t]['hashes']) for t in TREATMENTS}}
    dump_yaml(pair_hashes, out_dir / 'pair-hashes.yml')
    verify_paired_prepared(out_dir)

def verify_paired_prepared(pair_dir: Path) -> dict[str, Any]:
    control = load_yaml(pair_dir / 'control.yml')
    judge_contract = load_yaml(pair_dir / 'judge-contract.yml')
    pair_hashes = load_yaml(pair_dir / 'pair-hashes.yml')
    if not all((isinstance(x, dict) for x in (control, judge_contract, pair_hashes))):
        raise HarnessError('paired control/judge/hash documents must be mappings')
    if control.get('contract') != CONTROL_CONTRACT or judge_contract.get('contract') != BLIND_JUDGE_CONTRACT:
        raise HarnessError('paired contract mismatch')
    if hash_object(control) != pair_hashes.get('control_hash'):
        raise HarnessError('paired control hash mismatch')
    if hash_object(judge_contract) != pair_hashes.get('judge_contract_hash'):
        raise HarnessError('paired judge contract hash mismatch')
    assignments = control.get('response_assignments')
    if not isinstance(assignments, dict) or set(assignments.values()) != set(TREATMENTS) or len(assignments) != 2:
        raise HarnessError('paired response assignments must contain exactly baseline and skill')
    if set(judge_contract.get('response_ids', [])) != set(assignments):
        raise HarnessError('blind judge response ids do not match control assignments')
    execution_order = control.get('execution_order')
    if not isinstance(execution_order, list) or len(execution_order) != 2 or set(execution_order) != set(assignments):
        raise HarnessError('control execution_order must contain both opaque response ids exactly once')
    compiled_views: dict[str, dict[str, Any]] = {}
    common_hashes: dict[str, str] | None = None
    common_roles: dict[str, str] | None = None
    runtime_hashes: set[str] = set()
    for response_id, treatment in assignments.items():
        response_dir = pair_dir / 'responses' / response_id
        prepared = verify_prepared_integrity(response_dir)
        compiled_views[treatment] = prepared
        if prepared['execution'].get('user_prompt') is None:
            raise HarnessError(f'{response_id}: missing user prompt')
        runner_dir = response_dir / 'runner-package'
        runtime = prepared['execution'].get('runtime') or {}
        if runtime.get('network_access') is not False or runtime.get('repository_access') is not False:
            raise HarnessError(f'{response_id}: package-only runtime constraints missing')
        runtime_hashes.add(hash_object(_normalized_runtime(prepared['execution'])))
        source_map: dict[str, str] = {}
        for record in prepared['execution'].get('fixtures', []):
            rel = _safe_rel(str(record['path']), 'runner fixture path')
            actual = runner_dir / rel
            if not actual.is_file():
                raise HarnessError(f'{response_id}: runner fixture missing: {rel}')
            if hash_file(actual) != record.get('hash'):
                raise HarnessError(f'{response_id}: runner fixture hash mismatch: {rel}')
            if str(rel).startswith('sources/'):
                source_map[str(rel)] = str(record['hash'])
        subject_roles = {str(record['path']): str(record['role']) for record in prepared['judge'].get('fixtures', []) if str(record.get('role')) != 'skill-instruction'}
        if common_hashes is None:
            common_hashes = source_map
            common_roles = subject_roles
        else:
            if source_map != common_hashes:
                raise HarnessError('paired runner packages differ in subject-source content')
            if subject_roles != common_roles:
                raise HarnessError('paired runner packages differ in subject-source roles')
        instruction_records = [record for record in prepared['judge'].get('fixtures', []) if str(record.get('role')) == 'skill-instruction']
        instruction_files = [p for p in (runner_dir / 'instructions').glob('*') if p.is_file()] if (runner_dir / 'instructions').exists() else []
        if treatment == 'baseline':
            if instruction_files or instruction_records:
                raise HarnessError('baseline runner package unexpectedly contains skill instructions')
        elif len(instruction_files) != 1 or len(instruction_records) != 1:
            raise HarnessError('skill runner package must contain exactly one skill instruction')
        elif str(instruction_records[0].get('hash')) != str(control.get('target_skill_hash')):
            raise HarnessError('skill instruction hash does not match the coordinator-pinned target skill')
    baseline_exec = compiled_views['baseline']['execution']
    skill_exec = compiled_views['skill']['execution']
    if baseline_exec.get('user_prompt') != skill_exec.get('user_prompt'):
        raise HarnessError('paired user prompt mismatch')
    if baseline_exec.get('repo_commit') != skill_exec.get('repo_commit'):
        raise HarnessError('paired repo commit mismatch')
    if common_hashes != control.get('shared_subject_source_hashes'):
        raise HarnessError('paired common source hashes do not match control')
    if common_roles != control.get('shared_subject_source_roles'):
        raise HarnessError('paired common source roles do not match control')
    if len(runtime_hashes) != 1:
        raise HarnessError('paired prepared runtime contracts differ')
    if next(iter(runtime_hashes)) != control.get('shared_runtime_contract_hash'):
        raise HarnessError('paired runtime contract hash does not match control')
    blind_text = (pair_dir / 'judge-contract.yml').read_text(encoding='utf-8').lower()
    for forbidden in ('response_assignments', 'execution_order', 'baseline', 'skill treatment'):
        if forbidden in blind_text:
            raise HarnessError(f'treatment/order metadata leaked into blind judge contract: {forbidden}')
    return {'verified': True, 'experiment_id': control.get('experiment_id'), 'case_id': control.get('case_id'), 'repetition': control.get('repetition'), 'response_count': 2, 'prompt_parity': True, 'subject_source_parity': True, 'subject_role_parity': True, 'prepared_runtime_parity': True, 'treatment_mapping_hidden_from_judge_contract': 'response_assignments' not in judge_contract, 'execution_order_hidden_from_judge_contract': 'execution_order' not in judge_contract}

def load_method_evidence(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise HarnessError(f'paired method evidence must be a mapping: {path}')
    if data.get('schema_version') != 1:
        raise HarnessError(f'paired method evidence schema_version must be 1: {path}')
    if data.get('contract') != METHOD_EVIDENCE_CONTRACT:
        raise HarnessError(f'paired method evidence contract must be {METHOD_EVIDENCE_CONTRACT}')
    required = ('response_id', 'runner_type', 'runner_model', 'runner_session_id', 'model_configuration_fingerprint', 'runtime_configuration_fingerprint', 'fresh_context', 'network_disabled', 'repository_access_disabled', 'package_only_access')
    for key in required:
        if key not in data:
            raise HarnessError(f'paired method evidence missing {key}: {path}')
    for key in ('fresh_context', 'network_disabled', 'repository_access_disabled', 'package_only_access'):
        _validate_tri(data[key], f'{path}:{key}')
    for key in ('response_id', 'runner_type', 'runner_model', 'runner_session_id', 'model_configuration_fingerprint', 'runtime_configuration_fingerprint'):
        value = str(data[key])
        if not value:
            raise HarnessError(f'paired method evidence {key} must not be empty: {path}')
    for key in ('model_configuration_fingerprint', 'runtime_configuration_fingerprint'):
        value = str(data[key])
        if value != TRI_UNKNOWN:
            digest = value[7:] if value.startswith('sha256:') else ''
            if len(digest) != 64 or any((char not in '0123456789abcdefABCDEF' for char in digest)):
                raise HarnessError(f'paired method evidence {key} must be sha256:<64-hex> or unknown: {path}')
    return data

def _unknown_method_evidence(response_id: str) -> dict[str, Any]:
    return {'schema_version': 1, 'contract': METHOD_EVIDENCE_CONTRACT, 'response_id': response_id, 'runner_type': TRI_UNKNOWN, 'runner_model': TRI_UNKNOWN, 'runner_session_id': TRI_UNKNOWN, 'model_configuration_fingerprint': TRI_UNKNOWN, 'runtime_configuration_fingerprint': TRI_UNKNOWN, 'fresh_context': TRI_UNKNOWN, 'network_disabled': TRI_UNKNOWN, 'repository_access_disabled': TRI_UNKNOWN, 'package_only_access': TRI_UNKNOWN}

def _load_method_evidence_map(paths: list[Path] | None, expected_ids: set[str]) -> dict[str, dict[str, Any]]:
    result = {response_id: _unknown_method_evidence(response_id) for response_id in expected_ids}
    if not paths:
        return result
    seen: set[str] = set()
    for path in paths:
        evidence = load_method_evidence(path)
        response_id = str(evidence['response_id'])
        if response_id not in expected_ids:
            raise HarnessError(f'method evidence {path} has unexpected response id {response_id}')
        if response_id in seen:
            raise HarnessError(f'duplicate method evidence for response id {response_id}')
        seen.add(response_id)
        result[response_id] = evidence
    return result

def _method_parity(pair_status: dict[str, Any], control: dict[str, Any], runs: dict[str, dict[str, Any]], method_evidence: dict[str, dict[str, Any]]) -> dict[str, Any]:
    expected_ids = set(control['response_assignments'])
    manifests = {response_id: runs[response_id]['manifest'] for response_id in expected_ids}
    model_values = [str(manifests[response_id].get('runner_model', TRI_UNKNOWN)) for response_id in expected_ids]
    type_values = [str(manifests[response_id].get('runner_type', TRI_UNKNOWN)) for response_id in expected_ids]
    session_values = [str(manifests[response_id].get('runner_session_id', TRI_UNKNOWN)) for response_id in expected_ids]
    repo_values = [str(manifests[response_id].get('repo_commit', TRI_UNKNOWN)) for response_id in expected_ids]
    same_repo_commit: bool | str
    if any((value == TRI_UNKNOWN for value in repo_values)):
        same_repo_commit = TRI_UNKNOWN
    else:
        same_repo_commit = len(set(repo_values)) == 1 and repo_values[0] == str(control.get('pinned_commit'))
    sessions_distinct: bool | str
    if any((value == TRI_UNKNOWN for value in session_values)):
        sessions_distinct = TRI_UNKNOWN
    else:
        sessions_distinct = len(set(session_values)) == 2
    evidence_consistency: list[bool | str] = []
    for response_id in expected_ids:
        manifest = manifests[response_id]
        evidence = method_evidence[response_id]
        field_checks: list[bool | str] = []
        for key in ('runner_type', 'runner_model', 'runner_session_id'):
            evidence_value = str(evidence.get(key, TRI_UNKNOWN))
            manifest_value = str(manifest.get(key, TRI_UNKNOWN))
            if evidence_value == TRI_UNKNOWN or manifest_value == TRI_UNKNOWN:
                field_checks.append(TRI_UNKNOWN)
            else:
                field_checks.append(evidence_value == manifest_value)
        evidence_consistency.append(_tri_all(field_checks))
    model_config_values = [str(method_evidence[response_id]['model_configuration_fingerprint']) for response_id in expected_ids]
    runtime_config_values = [str(method_evidence[response_id]['runtime_configuration_fingerprint']) for response_id in expected_ids]
    fresh_context = _tri_all([_validate_tri(method_evidence[response_id]['fresh_context'], f'{response_id}.fresh_context') for response_id in expected_ids])
    network_disabled = _tri_all([_validate_tri(method_evidence[response_id]['network_disabled'], f'{response_id}.network_disabled') for response_id in expected_ids])
    repository_access_disabled = _tri_all([_validate_tri(method_evidence[response_id]['repository_access_disabled'], f'{response_id}.repository_access_disabled') for response_id in expected_ids])
    package_only_access = _tri_all([_validate_tri(method_evidence[response_id]['package_only_access'], f'{response_id}.package_only_access') for response_id in expected_ids])
    parity = {'schema_version': 1, 'technical_run_packages_verified': True, 'same_user_prompt': pair_status['prompt_parity'], 'same_subject_sources': pair_status['subject_source_parity'], 'same_subject_roles': pair_status['subject_role_parity'], 'same_prepared_runtime_contract': pair_status['prepared_runtime_parity'], 'same_repo_commit_and_pinned_version': same_repo_commit, 'target_skill_version_pinned': True, 'same_runner_model': _known_equal(model_values), 'same_runner_type': _known_equal(type_values), 'fresh_context_sessions_distinct': sessions_distinct, 'method_evidence_matches_run_manifest': _tri_all(evidence_consistency), 'model_configuration_parity': _known_equal(model_config_values), 'runtime_configuration_parity': _known_equal(runtime_config_values), 'fresh_context_reported': fresh_context, 'network_disabled_reported': network_disabled, 'repository_access_disabled_reported': repository_access_disabled, 'package_only_access_reported': package_only_access, 'treatment_disclosure_detected': False}
    required_keys = ['same_user_prompt', 'same_subject_sources', 'same_subject_roles', 'same_prepared_runtime_contract', 'same_repo_commit_and_pinned_version', 'target_skill_version_pinned', 'same_runner_model', 'same_runner_type', 'fresh_context_sessions_distinct', 'method_evidence_matches_run_manifest', 'model_configuration_parity', 'runtime_configuration_parity', 'fresh_context_reported', 'network_disabled_reported', 'repository_access_disabled_reported', 'package_only_access_reported']
    required_values = [parity[key] for key in required_keys]
    if False in required_values:
        method_status = 'fail'
    elif TRI_UNKNOWN in required_values:
        method_status = 'partial'
    else:
        method_status = 'pass'
    parity['method_evidence_status'] = method_status
    parity['comparison_eligible'] = method_status == 'pass'
    parity['status_note'] = 'pass means the pair is methodologically eligible for later A/B comparison; partial means technically executed but method evidence is incomplete; fail means a known parity/isolation requirement was violated. This is not a behavioral skill result.'
    return parity

def package_blind_pair(pair_dir: Path, run_dirs: list[Path], out_dir: Path, method_evidence_paths: list[Path] | None=None) -> Path:
    pair_status = verify_paired_prepared(pair_dir)
    control = load_yaml(pair_dir / 'control.yml')
    judge_contract = load_yaml(pair_dir / 'judge-contract.yml')
    assignments = control['response_assignments']
    expected_ids = set(assignments)
    if len(run_dirs) != 2:
        raise HarnessError('package-blind-pair requires exactly two run directories')
    runs: dict[str, dict[str, Any]] = {}
    for run_dir in run_dirs:
        verify_run_package(run_dir)
        manifest = load_yaml(run_dir / 'manifest.yml')
        if not isinstance(manifest, dict):
            raise HarnessError(f'invalid run manifest: {run_dir}')
        response_id = str(manifest.get('test_id'))
        if response_id not in expected_ids:
            raise HarnessError(f'run {run_dir} has unexpected response id {response_id}')
        if response_id in runs:
            raise HarnessError(f'duplicate run for response id {response_id}')
        runs[response_id] = {'dir': run_dir, 'manifest': manifest}
    if set(runs) != expected_ids:
        raise HarnessError('blind pair is missing a response run')
    target_skill = str(control.get('target_skill', ''))
    allow_bare = bool((control.get('treatment_disclosure') or {}).get('allow_bare_target_skill_id_in_output', False))
    disclosure: dict[str, bool] = {}
    for response_id, item in runs.items():
        text = (item['dir'] / 'runner-output.md').read_text(encoding='utf-8')
        disclosure[response_id] = _treatment_disclosed(text, target_skill, allow_bare)
    if any(disclosure.values()):
        raise HarnessError('treatment disclosure detected in runner output; blind judge packaging refused')
    method_evidence = _load_method_evidence_map(method_evidence_paths, expected_ids)
    parity = _method_parity(pair_status, control, runs, method_evidence)
    if out_dir.exists():
        raise HarnessError(f'blind judge package already exists: {out_dir}')
    out_dir.mkdir(parents=True)
    dump_yaml(judge_contract, out_dir / 'judge-contract.yml')
    responses_dir = out_dir / 'responses'
    responses_dir.mkdir()
    response_refs = []
    for response_id in sorted(runs):
        target = responses_dir / f'{response_id}.md'
        shutil.copy2(runs[response_id]['dir'] / 'runner-output.md', target)
        response_refs.append({'response_id': response_id, 'path': f'responses/{response_id}.md', 'hash': hash_file(target)})
    dump_yaml(parity, out_dir / 'parity.yml')
    blind_input = {'schema_version': 1, 'contract': BLIND_INPUT_CONTRACT, 'judge_contract': 'judge-contract.yml', 'parity': 'parity.yml', 'responses': response_refs, 'note': 'Treatment mapping and execution order are intentionally absent. A partial/fail method_evidence_status may be inspected but is not eligible as A/B comparison evidence. Unblind only after semantic judging is complete.'}
    dump_yaml(blind_input, out_dir / 'blind-judge-input.yml')
    hashes = {'hash_algorithm': 'sha256/file-bytes-v1', 'judge_contract': hash_file(out_dir / 'judge-contract.yml'), 'parity': hash_file(out_dir / 'parity.yml'), 'blind_judge_input': hash_file(out_dir / 'blind-judge-input.yml'), 'responses': {item['response_id']: item['hash'] for item in response_refs}}
    dump_yaml(hashes, out_dir / 'hashes.yml')
    return out_dir

def cli_prepare(args: argparse.Namespace) -> int:
    experiment_path = Path(args.experiment).resolve()
    experiment = load_paired_experiment(experiment_path)
    pair = compile_paired_case(experiment, args.case_id, Path(args.repo_root).resolve(), args.repetition, args.blind_seed)
    out = Path(args.out).resolve()
    write_paired_case(pair, Path(args.repo_root).resolve(), out)
    print(out)
    return 0

def cli_verify(args: argparse.Namespace) -> int:
    status = verify_paired_prepared(Path(args.paired).resolve())
    import yaml
    print(yaml.safe_dump(status, allow_unicode=True, sort_keys=False), end='')
    return 0

def cli_blind(args: argparse.Namespace) -> int:
    out = package_blind_pair(Path(args.paired).resolve(), [Path(item).resolve() for item in args.run], Path(args.out).resolve(), [Path(item).resolve() for item in args.method_evidence] if args.method_evidence else None)
    print(out)
    return 0

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prep = sub.add_parser('prepare-pair', help='Prepare one baseline/skill pair using the existing behavioral harness contracts')
    prep.add_argument('case_id')
    prep.add_argument('--experiment', required=True)
    prep.add_argument('--repo-root', default=str(Path(__file__).resolve().parents[1]))
    prep.add_argument('--repetition', type=int, required=True)
    prep.add_argument('--blind-seed', required=True, help='Coordinator-only seed used to derive opaque response IDs and deterministic counterbalanced treatment order')
    prep.add_argument('--out', required=True)
    prep.set_defaults(func=cli_prepare)
    verify = sub.add_parser('verify-pair', help='Verify pair parity, hashes, source roles and treatment isolation before execution')
    verify.add_argument('--paired', required=True)
    verify.set_defaults(func=cli_verify)
    blind = sub.add_parser('package-blind-pair', help='Create a treatment-blind judge package from two ordinary harness run packages')
    blind.add_argument('--paired', required=True)
    blind.add_argument('--run', action='append', required=True, help='Ordinary behavioral-harness run directory; pass exactly twice')
    blind.add_argument('--method-evidence', action='append', help='Optional pair-specific runner method-evidence YAML. Pass once per response when available; missing evidence remains unknown.')
    blind.add_argument('--out', required=True)
    blind.set_defaults(func=cli_blind)
    return parser

def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.func(args))
    except HarnessError as exc:
        import sys
        print(f'HARNESS_ERROR: {exc}', file=sys.stderr)
        return 2
if __name__ == '__main__':
    raise SystemExit(main())
