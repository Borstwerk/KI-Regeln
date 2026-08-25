from __future__ import annotations

from datetime import date, datetime
import json
from pathlib import Path
from typing import Any, Callable

import yaml
from jsonschema import Draft202012Validator, FormatChecker


def _json_compatible(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _json_compatible(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_compatible(item) for item in value]
    return value


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _validate_schema(data: Any, schema_path: Path, label: str, err: Callable[[str, str], None]) -> None:
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:
        err("READINESS_SCHEMA", f"{label}: cannot load schema {schema_path}: {exc}")
        return
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for failure in sorted(validator.iter_errors(_json_compatible(data)), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in failure.path)
        err("READINESS_SCHEMA", f"{label}{f' [{location}]' if location else ''}: {failure.message}")


def validate_public_readiness(root: Path, err: Callable[[str, str], None], warn: Callable[[str, str], None]) -> tuple[int, int]:
    registry = _load_yaml(root / "Dokumentation/upstream-sources.yml") or {}
    provenance = _load_yaml(root / "Dokumentation/upstream-provenance.yml") or {}
    github_sources = {
        item.get("id"): item
        for item in registry.get("sources") or []
        if isinstance(item, dict) and item.get("kind") == "github-file"
    }
    entries = provenance.get("sources") or [] if isinstance(provenance, dict) else []

    by_id: dict[str, dict[str, Any]] = {}
    for item in entries:
        if not isinstance(item, dict):
            continue
        sid = item.get("source_id")
        if not isinstance(sid, str):
            continue
        if sid in by_id:
            err("PROVENANCE_ID", f"duplicate provenance source_id {sid}")
            continue
        by_id[sid] = item

    for sid in sorted(set(github_sources) - set(by_id)):
        err("PROVENANCE_MISSING", f"GitHub upstream has no provenance decision record: {sid}")
    for sid in sorted(set(by_id) - set(github_sources)):
        err("PROVENANCE_ID", f"provenance record has no GitHub upstream registry entry: {sid}")

    redistribution_relevant = 0
    legal_review = 0
    notices_required: set[str] = set()

    for sid in sorted(set(github_sources) & set(by_id)):
        entry = by_id[sid]
        use_class = entry.get("use_class")
        review_status = entry.get("review_status")
        material_scope = entry.get("material_scope")
        reliance = entry.get("redistribution_reliance")
        redistribution = entry.get("redistribution_status")
        license_spdx = entry.get("license_spdx")
        notice = entry.get("notice_requirement")

        if review_status == "needs-human/legal-review":
            legal_review += 1
            if redistribution not in ("unresolved", "not-redistributable", "not-relied-on"):
                err("PROVENANCE_REVIEW", f"{sid}: legal-review case may not be marked redistributable")
            if use_class == "unclear":
                if material_scope not in ("unclear", "concepts/methods-only", "concrete-expression"):
                    err("PROVENANCE_REVIEW", f"{sid}: unclear legal-review case has invalid material_scope")
                if reliance not in ("unclear", "not-relied-on", "required"):
                    err("PROVENANCE_REVIEW", f"{sid}: unclear legal-review case has invalid redistribution_reliance")
            elif use_class not in ("reference/inspiration", "adapted", "copied/vendored"):
                err("PROVENANCE_CLASS", f"{sid}: unknown use_class {use_class}")
            # A legal-review record intentionally preserves uncertainty. It never
            # receives the assessed class invariants and it always blocks readiness.
            continue

        if review_status != "assessed":
            err("PROVENANCE_REVIEW", f"{sid}: unknown review_status {review_status}")
            continue

        if use_class == "unclear":
            err("PROVENANCE_CLASS", f"{sid}: assessed record may not keep use_class=unclear")
            continue
        if material_scope == "unclear":
            err("PROVENANCE_CLASS", f"{sid}: assessed record may not keep material_scope=unclear")
        if reliance == "unclear":
            err("PROVENANCE_CLASS", f"{sid}: assessed record may not keep redistribution_reliance=unclear")
        if redistribution == "unresolved":
            err("PROVENANCE_LICENSE", f"{sid}: assessed record may not keep redistribution_status=unresolved")

        if use_class == "reference/inspiration":
            if material_scope != "concepts/methods-only":
                err("PROVENANCE_CLASS", f"{sid}: reference/inspiration requires concepts/methods-only")
            if reliance != "not-relied-on" or redistribution != "not-relied-on":
                err("PROVENANCE_CLASS", f"{sid}: reference-only material must not rely on upstream redistribution permission")
            if notice != "none-for-reference-only":
                err("PROVENANCE_NOTICE", f"{sid}: reference-only case must use notice_requirement=none-for-reference-only")
        elif use_class in ("adapted", "copied/vendored"):
            redistribution_relevant += 1
            if material_scope != "concrete-expression":
                err("PROVENANCE_CLASS", f"{sid}: {use_class} requires concrete-expression material scope")
            if reliance != "required":
                err("PROVENANCE_CLASS", f"{sid}: {use_class} requires redistribution_reliance=required")
            if license_spdx in (None, "UNKNOWN"):
                err("PROVENANCE_LICENSE", f"{sid}: assessed redistribution-relevant material requires a resolved license")
            if redistribution not in ("permitted", "permitted-with-notice", "not-redistributable"):
                err("PROVENANCE_LICENSE", f"{sid}: assessed redistribution-relevant material has invalid redistribution status")
            if notice not in ("none", "none-required", "required"):
                err("PROVENANCE_NOTICE", f"{sid}: redistribution-relevant notice requirement must be explicit")
            if notice == "required":
                notices_required.add(sid)

            evidence_fields = (
                entry.get("repository_commit"),
                entry.get("license_source"),
                entry.get("license_source_commit_or_ref"),
                entry.get("license_path"),
                entry.get("license_blob_sha"),
            )
            if not all(evidence_fields):
                err("PROVENANCE_LICENSE", f"{sid}: assessed redistribution-relevant material requires same-state license evidence")
            same_state = (entry.get("license_evidence") or {}).get("same_state_files") or []
            if not same_state:
                err("PROVENANCE_LICENSE", f"{sid}: assessed redistribution-relevant material requires same-state license file evidence")
        else:
            err("PROVENANCE_CLASS", f"{sid}: unknown use_class {use_class}")

    notice_path = root / "THIRD-PARTY-NOTICES.md"
    notice_text = notice_path.read_text(encoding="utf-8") if notice_path.is_file() else ""
    for sid in sorted(notices_required):
        if f"`{sid}`" not in notice_text:
            err("PROVENANCE_NOTICE", f"{sid}: required notice source_id missing from THIRD-PARTY-NOTICES.md")

    readiness_path = root / "Dokumentation/open-source-readiness.yml"
    if not readiness_path.is_file():
        err("READINESS", "Dokumentation/open-source-readiness.yml is missing")
        return redistribution_relevant, legal_review

    readiness = _load_yaml(readiness_path)
    _validate_schema(readiness, root / "Schemas/open-source-readiness.schema.json", str(readiness_path.relative_to(root)), err)

    required_hygiene = [
        "README.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "ACKNOWLEDGEMENTS.md",
        "THIRD-PARTY-NOTICES.md",
        "Dokumentation/Lizenzentscheidung-Open-Source.md",
        "Dokumentation/Branch-Protection-Empfehlung.md",
        ".github/dependabot.yml",
        ".github/pull_request_template.md",
    ]
    for relative in required_hygiene:
        if not (root / relative).is_file():
            err("READINESS_FILE", f"required public-readiness file missing: {relative}")

    categories = readiness.get("categories") or {} if isinstance(readiness, dict) else {}
    licensing = categories.get("licensing") or {} if isinstance(categories, dict) else {}
    provenance_readiness = categories.get("provenance") or {} if isinstance(categories, dict) else {}
    history_readiness = categories.get("history_exposure") or {} if isinstance(categories, dict) else {}
    security_readiness = categories.get("security_reporting") or {} if isinstance(categories, dict) else {}

    if licensing.get("status") == "ready" and not ((root / "LICENSE").is_file() or (root / "LICENSE.md").is_file()):
        err("READINESS_LICENSE", "licensing is marked ready but no root LICENSE exists")
    if licensing.get("status") == "blocked" and ((root / "LICENSE").is_file() or (root / "LICENSE.md").is_file()):
        warn("READINESS_LICENSE", "root LICENSE exists while licensing readiness is blocked; verify intentional state")
    if legal_review and provenance_readiness.get("status") == "ready":
        err("READINESS_PROVENANCE", "provenance is marked ready while legal-review provenance records remain")
    if history_readiness.get("status") == "ready" and history_readiness.get("scan_complete") is not True:
        err("READINESS_HISTORY", "history exposure is marked ready without a completed reachable-history scan")
    if security_readiness.get("status") == "ready" and security_readiness.get("private_reporting_channel_configured") is not True:
        err("READINESS_SECURITY", "security reporting is marked ready without a configured private reporting channel")

    return redistribution_relevant, legal_review
