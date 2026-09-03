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
        return f"sha256:{hash_file(path)}"
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
        by_element.setdefault(str(entry["element_id"]), []).append(entry)
    return {"path": str(path), "by_element": by_element, "document_hash": hash_object(data)}


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


def _authorization_for(element_id: str, observed_digest: Any, ledger: dict[str, Any]) -> tuple[bool, str]:
    """Does the ledger authorize exactly this observed state, and was it verified?

    The authorization must name the state actually observed. An authorization for some
    other value does not cover this change, and an authorization whose separate
    verification has not been performed does not count as complete.
    """
    for entry in ledger["by_element"].get(element_id, []):
        authorized = entry["authorized_digest"]
        if isinstance(authorized, list):
            authorized = sorted(str(x) for x in authorized)
        target = sorted(str(x) for x in observed_digest) if isinstance(observed_digest, list) else observed_digest
        if authorized != target:
            continue
        verification = entry["separate_verification"]
        if tri(verification.get("performed")) is not True:
            return False, f"authorization {entry['authorization_id']} exists but its separate verification was not performed"
        if not str(verification.get("evidence_ref") or "").strip():
            return False, f"authorization {entry['authorization_id']} carries no separate verification evidence"
        return True, f"authorized by {entry['authorization_id']}: {entry['reason']}"
    return False, "no authorization in the authoritative ledger matches the observed state"


def assess(
    baseline: dict[str, Any],
    observation: dict[str, Any],
    ledger: dict[str, Any],
    *,
    expected_baseline_hash: str | None = None,
    expected_ledger_hash: str | None = None,
    agent_claims_authorization: bool = False,
) -> dict[str, Any]:
    """Compare an observation against the pinned baseline and derive a verdict.

    `agent_claims_authorization` is recorded and then deliberately ignored for the
    decision. A claim is not an authorization.
    """
    integrity: dict[str, Any] = {"baseline_hash": baseline["document_hash"], "ledger_hash": ledger["document_hash"]}
    compromised: list[str] = []
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
            authorized, auth_reason = True, "no change, no authorization required"
        else:
            authorized, auth_reason = _authorization_for(element_id, digest, ledger)
        findings.append({
            "element_id": element_id,
            "kind": base_element["kind"],
            "classification": classification,
            "reason": reason,
            "authorized": authorized,
            "authorization_reason": auth_reason,
        })

    # Elements present in the observation but absent from the baseline are an expansion
    # of the surface. An addition is not automatically stricter -- a newly added filter
    # is not -- so it is unclassified rather than credited as a strengthening.
    for element_id in sorted(set(observation["elements"]) - set(baseline["elements"])):
        digest = observation["elements"][element_id]["digest"]
        authorized, auth_reason = _authorization_for(element_id, digest, ledger)
        findings.append({
            "element_id": element_id,
            "kind": observation["elements"][element_id]["kind"],
            "classification": "changed_unclassified",
            "reason": "element is not part of the pinned baseline; an addition is not inherently stricter",
            "authorized": authorized,
            "authorization_reason": auth_reason,
        })

    changed = [f for f in findings if f["classification"] != "unchanged"]
    unauthorized_weakening = [f for f in changed if f["classification"] in {"weakened", "removed"} and not f["authorized"]]
    unauthorized_unclassified = [f for f in changed if f["classification"] == "changed_unclassified" and not f["authorized"]]

    if compromised:
        verdict, rationale = "ESCALATE", "the integrity of the baseline or the authorization ledger itself is in doubt"
    elif unauthorized_weakening:
        verdict, rationale = "STOP", "the load-bearing measurement surface was weakened without authorization"
    elif unauthorized_unclassified:
        verdict, rationale = "REQUEST_GATE", "the measurement surface changed in a way this engine cannot classify; a gate must decide"
    elif changed:
        verdict, rationale = "PASS_WITH_SURFACE_CHANGE", "the surface changed under authorization that was separately verified"
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
        "findings": findings,
    }


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--observation", required=True)
    parser.add_argument("--authorizations", required=True)
    parser.add_argument("--baseline-root", help="Root for baseline file elements (default: baseline dir)")
    parser.add_argument("--observation-root", help="Root for observation file elements (default: observation dir)")
    parser.add_argument("--expect-baseline-hash")
    parser.add_argument("--expect-ledger-hash")
    parser.add_argument("--agent-claims-authorization", action="store_true")
    args = parser.parse_args(argv)
    try:
        baseline = load_surface(Path(args.baseline), Path(args.baseline_root) if args.baseline_root else None)
        observation = load_surface(Path(args.observation), Path(args.observation_root) if args.observation_root else None)
        ledger = load_authorizations(Path(args.authorizations))
        result = assess(
            baseline, observation, ledger,
            expected_baseline_hash=args.expect_baseline_hash,
            expected_ledger_hash=args.expect_ledger_hash,
            agent_claims_authorization=args.agent_claims_authorization,
        )
    except HarnessError as exc:
        print(f"SURFACE_ERROR: {exc}", file=sys.stderr)
        return 2
    import yaml

    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False), end="")
    return 0 if result["verdict"] in {"PASS", "PASS_WITH_SURFACE_CHANGE"} else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
