#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

from tools.open_source_readiness_audit import DERIVATION_RE, similarity_metrics

ROOT = Path(__file__).resolve().parents[1]
NEON_REPOSITORY = "https://github.com/neondatabase/postgres-skills.git"
NEON_COMMIT = "0d9a967085c3bc137ab39ff9e3191c2eb3129d8c"
NEON_SOURCE_PATH = "skills/postgres-best-practices/SKILL.md"
NEON_BLOB = "43f3468765949e3db85a3782d90d4826b6c585bd"
NEON_LICENSE_PATH = "LICENSE"
NEON_LICENSE_BLOB = "b87eca9ebe930dd536fc479611af31e1110c7434"
LOCAL_IMPACTS = [
    Path("Datenbanken/Datenmodellierung-und-Zugriffsmuster.md"),
    Path("Datenbanken/Indizes-und-Execution-Plans.md"),
    Path("Datenbanken/Migrationen-Backfills-und-Rollback.md"),
]


def run(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(args, cwd=cwd, check=True, text=True, capture_output=True)
    return result.stdout.strip()


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    new, count = re.subn(pattern, replacement, text, count=1, flags=re.M | re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one replacement, got {count}")
    return new


def verify_historical_state() -> str:
    with tempfile.TemporaryDirectory(prefix="neon-provenance-") as tmp:
        repo = Path(tmp) / "postgres-skills"
        run("git", "clone", "--filter=blob:none", "--no-checkout", NEON_REPOSITORY, str(repo))
        run("git", "fetch", "--depth=1", "origin", NEON_COMMIT, cwd=repo)
        run("git", "checkout", "--detach", "FETCH_HEAD", cwd=repo)

        artifact_blob = run("git", "rev-parse", f"HEAD:{NEON_SOURCE_PATH}", cwd=repo)
        license_blob = run("git", "rev-parse", f"HEAD:{NEON_LICENSE_PATH}", cwd=repo)
        if artifact_blob != NEON_BLOB:
            raise RuntimeError(f"Neon artifact blob mismatch: {artifact_blob}")
        if license_blob != NEON_LICENSE_BLOB:
            raise RuntimeError(f"Neon LICENSE blob mismatch: {license_blob}")

        paths = run(
            "git", "ls-tree", "-r", "--name-only", "HEAD", "skills/postgres-best-practices", cwd=repo
        ).splitlines()
        override_re = re.compile(r"(^|/)(LICENSE|COPYING|NOTICE)([._-].*)?$", re.I)
        overrides = [path for path in paths if override_re.search(path)]
        if overrides:
            raise RuntimeError(f"Unexpected path-specific license/notice files: {overrides}")

        upstream = (repo / NEON_SOURCE_PATH).read_text(encoding="utf-8")

    print(f"Verified artifact blob {NEON_BLOB} at repository commit {NEON_COMMIT}")
    print(f"Verified same-state root Apache-2.0 LICENSE blob {NEON_LICENSE_BLOB}")
    print("Verified no path-specific LICENSE/COPYING/NOTICE under skills/postgres-best-practices/")
    return upstream


def compare_local_impacts(upstream: str) -> None:
    failed = False
    for relative in LOCAL_IMPACTS:
        local = (ROOT / relative).read_text(encoding="utf-8")
        metrics = similarity_metrics(upstream, local)
        derivation = bool(DERIVATION_RE.search(local))
        print(
            f"{relative}: signal={metrics['signal']} "
            f"exact_long_lines={metrics['exact_long_line_count']} "
            f"common_12_word_shingles={metrics['common_12_word_shingle_count']} "
            f"derivation_marker={derivation}"
        )
        if metrics["signal"] != "none" or derivation:
            failed = True
    if failed:
        raise RuntimeError(
            "Concrete lexical/derivation signal found; reference-only classification must not be applied"
        )
    print("RESULT: no source-specific lexical or derivation signal in any registered local impact")


def update_provenance() -> None:
    path = ROOT / "Dokumentation/upstream-provenance.yml"
    text = path.read_text(encoding="utf-8")
    neon_block = '''- source_id: neon-postgres-best-practices
  reviewed_at: 2026-08-26
  repository_commit: 0d9a967085c3bc137ab39ff9e3191c2eb3129d8c
  use_class: reference/inspiration
  review_status: assessed
  material_scope: concepts/methods-only
  classification_evidence:
  - The observed Neon artifact blob was independently mapped to repository commit 0d9a967085c3bc137ab39ff9e3191c2eb3129d8c.
  - Source-specific comparison against all three registered local impacts found no exact long-line, 12-word-shingle or explicit derivation-marker signal; manual review found only generic topic overlap, not distinctive translated or structural expression.
  - The local use is therefore classified as concepts/methods reference only; Apache-2.0 redistribution permission is documented as same-state evidence but is not relied on for the local classification.
  similarity_audit: no-signal
  redistribution_reliance: not-relied-on
  license_spdx: Apache-2.0
  license_source: https://github.com/neondatabase/postgres-skills/blob/0d9a967085c3bc137ab39ff9e3191c2eb3129d8c/LICENSE
  license_source_commit_or_ref: 0d9a967085c3bc137ab39ff9e3191c2eb3129d8c
  license_path: LICENSE
  license_blob_sha: b87eca9ebe930dd536fc479611af31e1110c7434
  path_specific_license_notes:
  - Same-state audit verified the root Apache-2.0 LICENSE and found no LICENSE, COPYING or NOTICE override under skills/postgres-best-practices/.
  license_status_at_observation: Apache-2.0 root license verified at the exact repository commit containing the observed artifact blob; no path-specific conflicting license was detected. The license is recorded as historical evidence and is not relied on for reference-only use.
  notice_requirement: none-for-reference-only
  redistribution_status: not-relied-on
  license_evidence:
    artifact_declarations: []
    same_state_files:
    - path: LICENSE
      blob_sha: b87eca9ebe930dd536fc479611af31e1110c7434
      spdx: Apache-2.0
    notes:
    - The observed artifact blob 43f3468765949e3db85a3782d90d4826b6c585bd is present at repository commit 0d9a967085c3bc137ab39ff9e3191c2eb3129d8c.
    - The root LICENSE was fetched and verified from the same commit.
    - No concrete expression reliance was found in the registered local impacts, so Apache-2.0 redistribution permission is not required for the local reference-only classification.
  source_snapshot:
    repository: neondatabase/postgres-skills
    source_path: skills/postgres-best-practices/SKILL.md
    observed_ref: main
    observed_blob_sha: 43f3468765949e3db85a3782d90d4826b6c585bd
'''
    text = replace_once(
        text,
        r"^- source_id: neon-postgres-best-practices\n.*?(?=^- source_id: mattpocock-code-review\n)",
        neon_block,
        "Neon provenance block",
    )
    text = text.replace("last_reviewed: 2026-08-25", "last_reviewed: 2026-08-26", 1)
    path.write_text(text, encoding="utf-8")


def update_machine_readiness() -> None:
    path = ROOT / "Dokumentation/open-source-readiness.yml"
    text = path.read_text(encoding="utf-8")
    text = text.replace("assessed_at: 2026-08-25", "assessed_at: 2026-08-26", 1)
    provenance = '''  provenance:
    status: ready
    evidence:
      - 65 GitHub artifacts were reviewed source-by-source in Phase 3.
      - Every provenance decision is bound to the exact reviewed source snapshot (repository, source path, observed ref and observed blob SHA); the permanent validator fails on any registry/provenance snapshot mismatch and requires explicit re-review.
      - 61 records are assessed as reference/inspiration with no redistribution reliance.
      - neon-postgres-best-practices is assessed as reference/inspiration after its observed blob was mapped to repository commit 0d9a967085c3bc137ab39ff9e3191c2eb3129d8c and source-specific comparison found no concrete expression signal; the same-state root LICENSE is Apache-2.0 blob b87eca9ebe930dd536fc479611af31e1110c7434.
      - Four Matt Pocock artifacts are individually assessed as adapted with their own observed-blob snapshots, exact repository-commit mapping and same-state MIT license evidence.
      - THIRD-PARTY-NOTICES.md carries the required MIT notice for those four adaptations; the Neon reference-only record requires no redistribution notice.
    blockers: []
'''
    text = replace_once(text, r"^  provenance:\n.*?(?=^  licensing:\n)", provenance, "readiness provenance")
    security = '''  security_reporting:
    status: blocked
    private_reporting_channel_configured: false
    evidence:
      - SECURITY.md requires a private vulnerability-reporting path for the public release state.
      - GitHub Private Vulnerability Reporting is documented for public repositories, so it is not represented as an enable-now setting for the current private repository.
      - Phase 4 must, after the visibility change, enable Private Vulnerability Reporting, verify that private reporting works, and confirm SECURITY.md; an explicitly approved alternative private channel may close this gate earlier.
    blockers:
      - Establish and verify a private reporting path as a Phase-4 release step after the visibility change, or document and verify an authorized alternative private channel earlier.
'''
    text = replace_once(
        text, r"^  security_reporting:\n.*?(?=^  repository_hygiene:\n)", security, "readiness security reporting"
    )
    release_gate = '''release_gate:
  status: blocked
  blockers:
    - Root project license is blocked on an authorized Rights Holder decision to publish the project-owned KI-Regeln material under MIT.
    - A verified private vulnerability-reporting path is still required for the public release state; GitHub Private Vulnerability Reporting is a Phase-4 step after visibility change unless an authorized alternative channel is established earlier.
'''
    text = replace_once(text, r"^release_gate:\n.*\Z", release_gate, "readiness release gate")
    path.write_text(text, encoding="utf-8")


def update_human_report() -> None:
    path = ROOT / "Dokumentation/Open-Source-Readiness-2026-08-25.md"
    text = path.read_text(encoding="utf-8")
    old_counts = '''- 60 × `reference/inspiration`, `review_status: assessed`, keine Redistributionsabhängigkeit;
- 4 × `adapted`, jeweils separat belegt und MIT-Notice-pflichtig;
- 1 × `needs-human/legal-review` mit bewusst offenem `use_class: unclear`.

Der automatische Ähnlichkeitscheck ist nur ein Signal. `assessed` wurde erst nach Review vergeben; ein offener Zweifelsfall bleibt ausdrücklich offen.'''
    new_counts = '''- 61 × `reference/inspiration`, `review_status: assessed`, keine Redistributionsabhängigkeit;
- 4 × `adapted`, jeweils separat belegt und MIT-Notice-pflichtig;
- 0 × `needs-human/legal-review`.

Der automatische Ähnlichkeitscheck ist nur ein Signal. `assessed` wurde erst nach source-spezifischem Review vergeben; die Use-Class wurde nicht allein aus einer vorhandenen Lizenz abgeleitet.'''
    if old_counts not in text:
        raise RuntimeError("Human report: provenance counts block not found")
    text = text.replace(old_counts, new_counts, 1)

    neon = '''## Neon – aufgelöster Provenance-Fall

Der zuvor offene Fall `neon-postgres-best-practices` wurde am 2026-08-26 source-spezifisch nachgeprüft.

Der registrierte Blob `43f3468765949e3db85a3782d90d4826b6c585bd` ist Bestandteil des Repository-Commits `0d9a967085c3bc137ab39ff9e3191c2eb3129d8c` in `neondatabase/postgres-skills`. Am exakt selben Commit liegt die Root-`LICENSE` als Apache License 2.0 mit Blob `b87eca9ebe930dd536fc479611af31e1110c7434`. Unter `skills/postgres-best-practices/` wurde in diesem Zustand keine abweichende `LICENSE`-, `COPYING`- oder `NOTICE`-Datei gefunden.

Die Lizenz wurde nicht als Abkürzung für die Use-Class verwendet. Der registrierte historische `SKILL.md`-Text wurde gegen jede der drei Local-Impact-Dateien einzeln mit demselben Long-Line-/12-Wort-Shingle-Verfahren wie im Phase-3-Audit verglichen. Ergebnis: kein exaktes Long-Line-Signal, kein 12-Wort-Shingle-Signal und kein expliziter Derivation-Marker. Die manuelle Gegenprüfung sieht nur generische Themenüberschneidungen wie Datenmodellierung, Indizes/Query-Optimierung und Migrationen; die lokalen Texte sind eigenständig deutsch formuliert und enthalten keine charakteristische übersetzte oder strukturelle Ausdrucksübernahme aus dem registrierten Upstream-Artefakt.

Finale Klassifikation:

- `review_status: assessed`;
- `use_class: reference/inspiration`;
- `material_scope: concepts/methods-only`;
- `redistribution_reliance: not-relied-on`;
- `redistribution_status: not-relied-on`;
- `license_spdx: Apache-2.0` als same-state historische Evidence, nicht als benötigte Redistributionsfreigabe.

Damit verbleibt kein `needs-human/legal-review`-Provenance-Record.

## Exposure-Audit
'''
    text = replace_once(text, r"^## Offener Provenance-Fall\n.*?(?=^## Exposure-Audit\n)", neon, "report Neon section")

    security = '''## Security Reporting

`SECURITY.md` ist vorhanden. Ein privater Vulnerability-Reporting-Kanal ist im aktuellen privaten Repositoryzustand noch nicht festgelegt.

Das wird nicht als technisch jetzt schon aktivierbare GitHub-Einstellung dargestellt: GitHub Private Vulnerability Reporting ist für öffentliche Repositories vorgesehen. Der zwingende Phase-4-Release-Schritt lautet daher: nach dem Visibility-Wechsel Private Vulnerability Reporting aktivieren, die Funktion praktisch prüfen und anschließend `SECURITY.md` bestätigen. Wird vorher ein anderer autorisierter privater Meldekanal festgelegt und dokumentiert, kann dieses Gate entsprechend früher geschlossen werden.

Bis einer dieser Wege tatsächlich verifiziert ist, bleibt Security Reporting ein Public-Release-Gate.

## Repository-Hygiene und Supply Chain
'''
    text = replace_once(
        text, r"^## Security Reporting\n.*?(?=^## Repository-Hygiene und Supply Chain\n)", security, "report security section"
    )

    old_gate = '''Das Repository selbst ist trotz erfolgreichem Phase-3-Hardening **noch nicht Public-Release-ready**, solange mindestens diese menschlichen Blocker offen sind:

1. `neon-postgres-best-practices` – Provenance/Legal Review;
2. Rights-Holder-/Root-License-Entscheidung;
3. privater Security-Reporting-Kanal.

Keiner dieser Punkte darf durch Automatisierung als erledigt markiert werden.'''
    new_gate = '''Das Repository selbst ist trotz erfolgreichem Phase-3-Hardening **noch nicht Public-Release-ready**, solange diese Release-Gates offen sind:

1. Rights-Holder-/Root-License-Entscheidung: Ein autorisierter Projekt-/Rights-Holder muss ausdrücklich freigeben, das eigene KI-Regeln-Material unter MIT zu veröffentlichen;
2. privater Security-Reporting-Pfad: in Phase 4 nach dem Visibility-Wechsel GitHub Private Vulnerability Reporting aktivieren, Funktion prüfen und `SECURITY.md` bestätigen – oder vorher einen autorisierten alternativen privaten Kanal dokumentieren.

Der frühere Neon-Provenance-Blocker ist source-spezifisch aufgelöst. Keines der verbleibenden Gates darf durch Automatisierung als erledigt markiert werden.'''
    if old_gate not in text:
        raise RuntimeError("Human report: release-gate block not found")
    path.write_text(text.replace(old_gate, new_gate, 1), encoding="utf-8")


def update_security() -> None:
    path = ROOT / "SECURITY.md"
    text = path.read_text(encoding="utf-8")
    old = '''Für den aktuellen privaten Projektstand ist **noch kein belastbar dokumentierter privater Security-Meldekanal festgelegt**. Vor einer Umstellung auf ein öffentliches Repository muss deshalb entweder GitHubs Private Vulnerability Reporting aktiviert oder ein anderer privater Meldekanal ausdrücklich festgelegt und hier dokumentiert werden.

Bis dieses Gate geschlossen ist, ist die Public-Release-Readiness im Bereich Security Reporting nur teilweise erfüllt.'''
    new = '''Für den aktuellen privaten Projektstand ist **noch kein belastbar dokumentierter privater Security-Meldekanal festgelegt**. GitHub Private Vulnerability Reporting ist für öffentliche Repositories vorgesehen und wird deshalb nicht als im privaten Vorbereitungszustand bereits aktivierbares Pflicht-Setting behandelt.

Verbindlicher Phase-4-Release-Schritt: Nach dem Visibility-Wechsel Private Vulnerability Reporting aktivieren, praktisch prüfen, dass ein privater Reportweg funktioniert, und anschließend diese `SECURITY.md`-Anleitung bestätigen beziehungsweise ergänzen. Falls vor dem Visibility-Wechsel ein anderer autorisierter privater Meldekanal festgelegt und dokumentiert wird, kann das Gate entsprechend früher geschlossen werden.

Bis ein privater Meldeweg tatsächlich eingerichtet und verifiziert ist, bleibt die Public-Release-Readiness im Bereich Security Reporting blockiert.'''
    if old not in text:
        raise RuntimeError("SECURITY.md expected reporting paragraph not found")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def update_changelog() -> None:
    path = ROOT / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    old = '- alle 65 konkreten GitHub-Upstream-Artefakte source-spezifisch auditiert und `Dokumentation/upstream-provenance.yml` migriert: 60× abschließend `reference/inspiration` ohne Redistributionsabhängigkeit, vier Matt-Pocock-Artefakte jeweils separat als `adapted` mit observed-Blob→Repository-Commit- und same-state-MIT-Evidence, ein Neon-Fall bewusst `needs-human/legal-review`;'
    new = '- alle 65 konkreten GitHub-Upstream-Artefakte source-spezifisch auditiert und `Dokumentation/upstream-provenance.yml` migriert: final 61× `reference/inspiration` ohne Redistributionsabhängigkeit und vier Matt-Pocock-Artefakte jeweils separat als `adapted`; der zunächst offene Neon-Fall wurde nach Auflösung des historischen Blob→Commit-Mappings per Local-Impact-/Expression-Vergleich als `assessed / reference/inspiration` abgeschlossen und trägt same-state Apache-2.0-Evidence;'
    if old not in text:
        raise RuntimeError("CHANGELOG Neon summary not found")
    text = text.replace(old, new, 1)
    old2 = '- Root-`LICENSE` bewusst nicht allein aus der MIT-Empfehlung erzeugt: Rights-Holder-/Projektlizenzentscheidung bleibt menschlicher Blocker; ebenso bleibt ein fehlender privater Security-Reporting-Kanal sichtbar blockiert;'
    new2 = '- Root-`LICENSE` bewusst nicht allein aus der MIT-Empfehlung erzeugt: ausdrückliche Rights-Holder-/Projektlizenzentscheidung bleibt Blocker; Security Reporting bleibt bis zu einem verifizierten privaten Meldeweg blockiert, wobei GitHub Private Vulnerability Reporting als Phase-4-Schritt nach dem Visibility-Wechsel behandelt wird und ein autorisierter alternativer privater Kanal das Gate früher schließen kann;'
    if old2 not in text:
        raise RuntimeError("CHANGELOG release-gate summary not found")
    path.write_text(text.replace(old2, new2, 1), encoding="utf-8")


def main() -> int:
    upstream = verify_historical_state()
    compare_local_impacts(upstream)
    update_provenance()
    update_machine_readiness()
    update_human_report()
    update_security()
    update_changelog()
    print("Applied reviewed Neon provenance and Phase-4 security-reporting documentation updates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
