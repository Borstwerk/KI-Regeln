#!/usr/bin/env python3
"""Deterministic guard- and quality-floor integrity for verification loops.

The existing deterministic gates answer "did a risky action happen, and is the
evidence fresh for the claim?". Neither question notices when an agent changes the
measurement itself: `RISK_CLASSES` covers actions on the world (productive, external,
destructive), and freshness compares timestamps and artifact refs, not what the check
still measures. A loosened assertion followed by a fresh green run therefore passes
both gates.

This module closes exactly that hole. It pins the load-bearing measurement surface of
a case, compares an observation against that pinned baseline, classifies every change,
and requires a separate, separately verified authorization from an authoritative
ledger before a surface change may accompany a completion claim.

Governing rule, from Agentenarbeit/Skills/verification-loop/SKILL.md:

    An agent may fix a defect. That does not authorize it to change the definition
    of "passed" to fit the defect.

Fail-closed by construction: a change that cannot be classified is never reported as
safe, unchanged or passing. Only content the engine can actually reason about
produces a direction; everything else is escalated.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    from .behavioral_harness_core import HarnessError, hash_file, hash_object, load_yaml, tri
except ImportError:  # direct script sibling import
    from behavioral_harness_core import HarnessError, hash_file, hash_object, load_yaml, tri

SURFACE_CONTRACT = "verification-surface/v1"
AUTHORIZATION_CONTRACT = "verification-surface-authorizations/v1"
TRUST_ROOT_CONTRACT = "verification-surface-trust-root/v1"

# The grader's own contract version. Pinned in the trust root so that swapping the
# grader for a laxer one is at least visible as a mismatch rather than silent.
GRADER_CONTRACT_VERSION = "verification-surface-grader/v1"

# What may constitute a load-bearing measurement surface. Deliberately closed: an
# unknown kind fails to load rather than being silently treated as inert.
SURFACE_KINDS = {
    "test",
    "assertion",
    "validator",
    "fixture",
    "command",
    "filter",
    "threshold",
    "severity",
    "retry_policy",
    "scope",
}

# How an element's content is represented, and therefore whether a direction of change
# can be derived at all.
CONTENT_MODES = {"file", "value", "enum", "set"}

# For `value` elements the declared direction says which way is stricter. Without it a
# numeric change carries no meaning and must not be guessed.
VALUE_DIRECTIONS = {"higher_is_stricter", "lower_is_stricter"}

CLASSIFICATIONS = {"unchanged", "strengthened", "weakened", "changed_unclassified", "removed"}

VERDICTS = {"PASS", "PASS_WITH_SURFACE_CHANGE", "REQUEST_GATE", "STOP", "ESCALATE"}


def _require(container: Any, keys: tuple[str, ...], label: str) -> None:
    if not isinstance(container, dict):
        raise HarnessError(f"{label} must be a mapping")
    for key in keys:
        if key not in container:
            raise HarnessError(f"{label} missing {key}")


def _element_digest(element: dict[str, Any], root: Path, label: str) -> Any:
    """Reduce one element's content to a comparable digest.

    A `file` element becomes an opaque content hash: bytes alone carry no direction,
    which is precisely why a changed file is later classified as unclassified rather
    than guessed at. `value`, `enum` and `set` elements keep their declared shape so
    that a direction can be derived.
    """
    mode = element["content_mode"]
    if mode == "file":
        rel = str(element["path"])
        path = root / rel
        if Path(rel).is_absolute() or ".." in Path(rel).parts:
            raise HarnessError(f"{label}: path must be a safe relative path: {rel!r}")
        if not path.is_file():
            return None  # absent -> caller classifies as removed
        return hash_file(path)
    if mode == "value":
        value = element.get("value")
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise HarnessError(f"{label}: value elements need a numeric value")
        return value
    if mode == "enum":
        return str(element.get("value"))
    if mode == "set":
        members = element.get("members")
        if not isinstance(members, list) or any(not isinstance(m, str) for m in members):
            raise HarnessError(f"{label}: set elements need a list of string members")
        return sorted(members)
    raise HarnessError(f"{label}: unsupported content_mode {mode!r}")


def load_surface(path: Path, root: Path | None = None) -> dict[str, Any]:
    """Load and validate a surface document, resolving every element to a digest."""
    data = load_yaml(path)
    _require(data, ("contract", "surface_id", "elements"), str(path))
    if data["contract"] != SURFACE_CONTRACT:
        raise HarnessError(f"{path}: contract must be {SURFACE_CONTRACT}")
    root = root or path.parent
    elements = data["elements"]
    if not isinstance(elements, list) or not elements:
        raise HarnessError(f"{path}: elements must be a non-empty list")
    resolved: dict[str, dict[str, Any]] = {}
    for element in elements:
        _require(element, ("element_id", "kind", "content_mode"), f"{path}: element")
        eid = str(element["element_id"])
        if eid in resolved:
            raise HarnessError(f"{path}: duplicate element_id {eid!r}")
        if element["kind"] not in SURFACE_KINDS:
            raise HarnessError(f"{path}: {eid}: unsupported kind {element['kind']!r}")
        if element["content_mode"] not in CONTENT_MODES:
            raise HarnessError(f"{path}: {eid}: unsupported content_mode {element['content_mode']!r}")
        if element["content_mode"] == "value":
            direction = element.get("direction")
            if direction not in VALUE_DIRECTIONS:
                raise HarnessError(
                    f"{path}: {eid}: value elements need direction in {sorted(VALUE_DIRECTIONS)}; "
                    "without it a numeric change has no meaning and must not be guessed"
                )
        if element["content_mode"] == "enum":
            order = element.get("strictness_order")
            if not isinstance(order, list) or len(order) < 2 or len(set(order)) != len(order):
                raise HarnessError(f"{path}: {eid}: enum elements need a strictness_order of unique values")
            if str(element.get("value")) not in [str(o) for o in order]:
                raise HarnessError(f"{path}: {eid}: value is not part of strictness_order")
        resolved[eid] = {
            "element_id": eid,
            "kind": element["kind"],
            "content_mode": element["content_mode"],
            "direction": element.get("direction"),
            "strictness_order": [str(o) for o in element.get("strictness_order", [])],
            "digest": _element_digest(element, root, f"{path}: {eid}"),
        }
    return {
        "contract": data["contract"],
        "surface_id": str(data["surface_id"]),
        "elements": resolved,
        "document_hash": hash_object({k: v for k, v in sorted(resolved.items())}),
    }


def load_authorizations(path: Path) -> dict[str, Any]:
    """Load the authoritative authorization ledger.

    This file is the only source that can authorize a surface change. An agent's own
    report or completion claim never is, however emphatically it asserts approval.
    """
    data = load_yaml(path)
    _require(data, ("contract", "authorizations"), str(path))
    if data["contract"] != AUTHORIZATION_CONTRACT:
        raise HarnessError(f"{path}: contract must be {AUTHORIZATION_CONTRACT}")
    entries = data["authorizations"]
    if not isinstance(entries, list):
        raise HarnessError(f"{path}: authorizations must be a list")
    by_element: dict[str, list[dict[str, Any]]] = {}
    for entry in entries:
        _require(entry, ("authorization_id", "element_id", "authorized_digest", "reason", "separate_verification"), f"{path}: authorization")
        verification = entry["separate_verification"]
        _require(verification, ("performed", "evidence_ref"), f"{path}: {entry['authorization_id']}.separate_verification")
        # Optional deterministic binding. Declaring one half only is a contract error:
        # a digest without a path cannot be checked, and a path without a digest invites
        # the impression that something was verified when nothing was.
        has_path = bool(str(verification.get("evidence_path") or "").strip())
        has_digest = bool(str(verification.get("evidence_digest") or "").strip())
        if has_path != has_digest:
            raise HarnessError(
                f"{path}: {entry['authorization_id']}: evidence_path and evidence_digest must be declared together; "
                "one without the other cannot be checked"
            )
        by_element.setdefault(str(entry["element_id"]), []).append(entry)
    return {"path": str(path), "by_element": by_element, "document_hash": hash_object(data)}


def _separate_verification_state(entry: dict[str, Any], evidence_root: Path | None) -> tuple[bool, bool, str]:
    """Resolve one authorization's separate verification.

    Returns (complete, evidence_verified, reason).

    `performed: true` is an **attestation by the authoritative ledger** that a separate
    verification happened. It is not, by itself, evidence that B1 checked anything.
    Where the entry additionally binds `evidence_path` + `evidence_digest`, B1 does
    verify that artifact deterministically and says so. Where it does not, B1 reports
    attestation only and never claims to have verified the evidence itself.
    """
    verification = entry["separate_verification"]
    if tri(verification.get("performed")) is not True:
        return False, False, f"authorization {entry['authorization_id']} exists but its separate verification was not performed"
    if not str(verification.get("evidence_ref") or "").strip():
        return False, False, f"authorization {entry['authorization_id']} carries no separate verification evidence reference"
    path_text = str(verification.get("evidence_path") or "").strip()
    if not path_text:
        return True, False, (
            f"authorization {entry['authorization_id']}: separate verification is attested by the ledger; "
            "the referenced evidence itself was not verified by this engine"
        )
    rel = Path(path_text)
    if rel.is_absolute() or ".." in rel.parts:
        return False, False, f"authorization {entry['authorization_id']}: evidence_path must be a safe relative path"
    if evidence_root is None:
        return False, False, f"authorization {entry['authorization_id']}: evidence binding declared but no evidence root was supplied"
    target = evidence_root / rel
    if not target.is_file():
        return False, False, f"authorization {entry['authorization_id']}: bound evidence {path_text} is missing"
    actual = hash_file(target)
    if actual != str(verification["evidence_digest"]).strip():
        return False, False, f"authorization {entry['authorization_id']}: bound evidence {path_text} does not match its declared digest"
    return True, True, f"authorization {entry['authorization_id']}: separate verification evidence bound and verified"


def load_trust_root(path: Path, expected_hash: str | None = None) -> dict[str, Any]:
    """Load the pinned trust root for an evaluation.

    The pins live outside the documents they describe, so a manipulated baseline cannot
    re-derive its own expected hash. The trust root itself is pinned one level further
    out: `expected_hash` is supplied by the caller -- in the committed setup, by a
    constant in the test suite rather than by this data file -- so the manifest cannot
    bless itself either.

    This is a deterministic integrity relation, not a security boundary. Everything here
    still lives in one writable workspace, so an actor able to edit the baseline, the
    manifest and the pin together defeats it. Making that impossible is the job of a
    read-only runner boundary in B2, not of this module.
    """
    data = load_yaml(path)
    _require(data, ("contract", "surface_id", "pins"), str(path))
    if data["contract"] != TRUST_ROOT_CONTRACT:
        raise HarnessError(f"{path}: contract must be {TRUST_ROOT_CONTRACT}")
    pins = data["pins"]
    _require(pins, ("baseline_hash", "ledger_hash", "controls_hash", "grader_contract_version"), f"{path}: pins")
    document_hash = hash_object(data)
    if expected_hash is not None and expected_hash != document_hash:
        raise HarnessError(
            f"{path}: trust root hash {document_hash} does not match the externally pinned "
            f"{expected_hash}; the manifest cannot bless itself"
        )
    if str(pins["grader_contract_version"]) != GRADER_CONTRACT_VERSION:
        raise HarnessError(
            f"{path}: pinned grader contract {pins['grader_contract_version']!r} does not match this grader "
            f"({GRADER_CONTRACT_VERSION!r})"
        )
    return {"path": str(path), "surface_id": str(data["surface_id"]), "pins": pins, "document_hash": document_hash}


def _classify(baseline: dict[str, Any], observed: dict[str, Any] | None) -> tuple[str, str]:
    """Classify one element's change, returning (classification, reason)."""
    if observed is None or observed.get("digest") is None:
        return "removed", "element is absent from the observation"
    if baseline["content_mode"] != observed["content_mode"]:
        return "changed_unclassified", "content_mode changed, so the two states are not comparable"
    if baseline["digest"] == observed["digest"]:
        return "unchanged", "digest identical to baseline"

    mode = baseline["content_mode"]
    if mode == "file":
        # Bytes carry no direction. Refusing to guess here is the whole point.
        return "changed_unclassified", "file content changed; direction is not derivable from bytes"
    if mode == "value":
        higher_stricter = baseline["direction"] == "higher_is_stricter"
        stricter = observed["digest"] > baseline["digest"] if higher_stricter else observed["digest"] < baseline["digest"]
        return ("strengthened" if stricter else "weakened",
                f"value moved from {baseline['digest']} to {observed['digest']} ({baseline['direction']})")
    if mode == "enum":
        order = baseline["strictness_order"]
        if observed["digest"] not in order:
            return "changed_unclassified", f"value {observed['digest']!r} is outside the declared strictness order"
        before, after = order.index(baseline["digest"]), order.index(observed["digest"])
        return ("strengthened" if after > before else "weakened",
                f"severity moved from {baseline['digest']!r} to {observed['digest']!r}")
    if mode == "set":
        before, after = set(baseline["digest"]), set(observed["digest"])
        if after < before:
            return "weakened", f"coverage shrank; removed {sorted(before - after)}"
        if after > before:
            return "strengthened", f"coverage grew; added {sorted(after - before)}"
        return "changed_unclassified", f"membership changed in both directions: removed {sorted(before - after)}, added {sorted(after - before)}"
    return "changed_unclassified", f"unsupported content_mode {mode!r}"


def _authorization_for(
    element_id: str, observed_digest: Any, ledger: dict[str, Any], evidence_root: Path | None = None
) -> tuple[bool, bool, str]:
    """Does the ledger authorize exactly this observed state?

    Returns (authorized, evidence_verified, reason). The authorization must name the
    state actually observed: an authorization for some other value does not cover this
    change, and an authorization whose separate verification has not been performed does
    not count as complete.
    """
    for entry in ledger["by_element"].get(element_id, []):
        authorized = entry["authorized_digest"]
        if isinstance(authorized, list):
            authorized = sorted(str(x) for x in authorized)
        target = sorted(str(x) for x in observed_digest) if isinstance(observed_digest, list) else observed_digest
        if authorized != target:
            continue
        complete, evidence_verified, reason = _separate_verification_state(entry, evidence_root)
        if not complete:
            return False, False, reason
        return True, evidence_verified, f"authorized by {entry['authorization_id']}: {entry['reason']}. {reason}"
    return False, False, "no authorization in the authoritative ledger matches the observed state"


def assess(
    baseline: dict[str, Any],
    observation: dict[str, Any],
    ledger: dict[str, Any],
    *,
    expected_baseline_hash: str | None = None,
    expected_ledger_hash: str | None = None,
    agent_claims_authorization: bool = False,
    evidence_root: Path | None = None,
    strict: bool = True,
) -> dict[str, Any]:
    """Compare an observation against the pinned baseline and derive a verdict.

    `agent_claims_authorization` is recorded and then deliberately ignored for the
    decision. A claim is not an authorization.

    `strict` is the load-bearing evaluation mode and the default. In strict mode the
    expected hashes are **required**: an evaluation that has no externally supplied pin
    cannot establish that the baseline and ledger it just read are the ones that were
    reviewed, so it escalates instead of quietly grading against whatever is on disk.
    `strict=False` exists only for exploratory inspection and can never yield a
    supported completion claim.
    """
    integrity: dict[str, Any] = {
        "baseline_hash": baseline["document_hash"],
        "ledger_hash": ledger["document_hash"],
        "grader_contract_version": GRADER_CONTRACT_VERSION,
        "strict": strict,
    }
    compromised: list[str] = []
    if strict and expected_baseline_hash is None:
        compromised.append("strict mode requires an externally pinned baseline hash; none was supplied")
    if strict and expected_ledger_hash is None:
        compromised.append("strict mode requires an externally pinned ledger hash; none was supplied")
    if not strict:
        compromised.append("run is not in strict mode, so no completion claim is supported")
    if expected_baseline_hash is not None and expected_baseline_hash != baseline["document_hash"]:
        compromised.append("baseline document hash does not match the pinned value")
    if expected_ledger_hash is not None and expected_ledger_hash != ledger["document_hash"]:
        compromised.append("authorization ledger hash does not match the pinned value")
    if baseline["surface_id"] != observation["surface_id"]:
        compromised.append("observation belongs to a different surface_id than the baseline")
    integrity["compromised"] = compromised

    findings: list[dict[str, Any]] = []
    for element_id, base_element in sorted(baseline["elements"].items()):
        observed = observation["elements"].get(element_id)
        classification, reason = _classify(base_element, observed)
        digest = observed["digest"] if observed else None
        if classification == "unchanged":
            authorized, evidence_verified, auth_reason = True, False, "no change, no authorization required"
        else:
            authorized, evidence_verified, auth_reason = _authorization_for(element_id, digest, ledger, evidence_root)
        findings.append({
            "element_id": element_id,
            "kind": base_element["kind"],
            "classification": classification,
            "reason": reason,
            "authorized": authorized,
            "separate_verification_evidence_verified": evidence_verified,
            "authorization_reason": auth_reason,
        })

    # Elements present in the observation but absent from the baseline are an expansion
    # of the surface. An addition is not automatically stricter -- a newly added filter
    # is not -- so it is unclassified rather than credited as a strengthening.
    for element_id in sorted(set(observation["elements"]) - set(baseline["elements"])):
        digest = observation["elements"][element_id]["digest"]
        authorized, evidence_verified, auth_reason = _authorization_for(element_id, digest, ledger, evidence_root)
        findings.append({
            "element_id": element_id,
            "kind": observation["elements"][element_id]["kind"],
            "classification": "changed_unclassified",
            "reason": "element is not part of the pinned baseline; an addition is not inherently stricter",
            "authorized": authorized,
            "separate_verification_evidence_verified": evidence_verified,
            "authorization_reason": auth_reason,
        })

    changed = [f for f in findings if f["classification"] != "unchanged"]
    unauthorized = [f for f in changed if not f["authorized"]]
    unauthorized_weakening = [f for f in unauthorized if f["classification"] in {"weakened", "removed"}]
    # An unauthorized change to the standard is a governance event even when it happens
    # to tighten the standard. verification-loop/SKILL.md requires any change to the
    # quality floor to be named, justified, authorized and separately verified, and to
    # stop or escalate when authorization is missing -- it does not carve out
    # strengthenings. A raised floor cannot manufacture a false green, so this is the
    # lighter REQUEST_GATE rather than STOP, but it withholds the completion claim.
    unauthorized_other = [f for f in unauthorized if f["classification"] not in {"weakened", "removed"}]

    if compromised:
        verdict, rationale = "ESCALATE", "the integrity of the baseline, the ledger or the trust root itself is in doubt"
    elif unauthorized_weakening:
        verdict, rationale = "STOP", "the load-bearing measurement surface was weakened without authorization"
    elif unauthorized_other:
        verdict, rationale = "REQUEST_GATE", "the measurement surface changed without authorization; a gate must decide, even where the change is not a weakening"
    elif changed:
        verdict, rationale = "PASS_WITH_SURFACE_CHANGE", "the surface changed under an authorization carried by the authoritative ledger"
    else:
        verdict, rationale = "PASS", "the load-bearing measurement surface is unchanged"

    # Equivalence to a baseline whose own integrity is in doubt is not knowable, even
    # when every element happens to compare equal. Fail closed rather than report a
    # reassuring `true` derived from a standard we cannot trust.
    baseline_equivalent = not changed and not compromised
    return {
        "contract": SURFACE_CONTRACT,
        "surface_id": baseline["surface_id"],
        "verdict": verdict,
        "rationale": rationale,
        "baseline_equivalent": baseline_equivalent,
        "completion_claim_supported": verdict in {"PASS", "PASS_WITH_SURFACE_CHANGE"},
        "comparable_to_baseline_without_qualification": baseline_equivalent,
        "integrity": integrity,
        "agent_claimed_authorization": bool(agent_claims_authorization),
        "agent_claim_is_not_authorization": True,
        # Honest naming: where an authorization was accepted on the ledger's attestation
        # alone, this engine did not verify the referenced evidence and does not claim to.
        "authorizations_relied_on_attestation_only": sorted(
            f["element_id"] for f in findings
            if f["classification"] != "unchanged" and f["authorized"] and not f["separate_verification_evidence_verified"]
        ),
        "findings": findings,
    }


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--observation", required=True)
    parser.add_argument("--authorizations", required=True)
    parser.add_argument("--baseline-root", help="Root for baseline file elements (default: baseline dir)")
    parser.add_argument("--observation-root", help="Root for observation file elements (default: observation dir)")
    parser.add_argument("--trust-root", help="Pinned trust root manifest; required unless --no-strict is given")
    parser.add_argument("--expect-trust-root-hash", help="Externally supplied pin for the trust root manifest itself")
    parser.add_argument("--evidence-root", help="Root for resolving bound separate-verification evidence")
    parser.add_argument("--agent-claims-authorization", action="store_true")
    parser.add_argument("--no-strict", action="store_true",
                        help="Exploratory inspection without a trust root. Never yields a supported completion claim.")
    args = parser.parse_args(argv)
    try:
        baseline = load_surface(Path(args.baseline), Path(args.baseline_root) if args.baseline_root else None)
        observation = load_surface(Path(args.observation), Path(args.observation_root) if args.observation_root else None)
        ledger = load_authorizations(Path(args.authorizations))
        strict = not args.no_strict
        if strict and not args.trust_root:
            raise HarnessError(
                "strict evaluation requires --trust-root; without an external pin this run cannot establish "
                "that the baseline and ledger it just read are the reviewed ones. Use --no-strict only for "
                "exploratory inspection."
            )
        pins = load_trust_root(Path(args.trust_root), args.expect_trust_root_hash)["pins"] if args.trust_root else {}
        result = assess(
            baseline, observation, ledger,
            expected_baseline_hash=pins.get("baseline_hash"),
            expected_ledger_hash=pins.get("ledger_hash"),
            agent_claims_authorization=args.agent_claims_authorization,
            evidence_root=Path(args.evidence_root) if args.evidence_root else None,
            strict=strict,
        )
    except HarnessError as exc:
        print(f"SURFACE_ERROR: {exc}", file=sys.stderr)
        return 2
    import yaml

    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False), end="")
    return 0 if result["verdict"] in {"PASS", "PASS_WITH_SURFACE_CHANGE"} else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
