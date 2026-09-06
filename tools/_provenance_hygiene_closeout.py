from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one marker, found {count}")
    return text.replace(old, new, 1)


# ---------------------------------------------------------------------------
# skill-catalog.yml
# ---------------------------------------------------------------------------
path = "skill-catalog.yml"
text = read(path)
if "id: inhaltsprovenienz-review" not in text:
    marker = '  - {id: tool-permission-review, area: Sicherheit, path: Sicherheit/Skills/tool-permission-review/SKILL.md, maturity: experimental, eval_coverage: partial, purpose: "Tool- und Berechtigungsrechte gegen Least Privilege, Fallbacks und Gates prüfen.", capabilities: [capability-inventory-required], related: [skill-security-review]}'
    addition = marker + '\n' + '\n'.join([
        '  - {id: inhaltsprovenienz-review, area: Sicherheit, path: Sicherheit/Skills/inhaltsprovenienz-review/SKILL.md, maturity: experimental, eval_coverage: partial, purpose: "Vorhandene Dateien und Inhalte read-only auf belegbare Provenienz-, Metadaten- und Unicode-Signale sowie deren Evidence-Grenzen prüfen.", capabilities: [artifact-inspection-preferred], related: [metadaten-hygiene, natuerliches-schreiben, deutsche-typografie, tool-permission-review]}',
        '  - {id: metadaten-hygiene, area: Sicherheit, path: Sicherheit/Skills/metadaten-hygiene/SKILL.md, maturity: experimental, eval_coverage: partial, purpose: "Eigene oder autorisierte Dateien kontrolliert von konkret freigegebenen unnötigen oder sensiblen Metadaten bereinigen und den Endzustand erneut prüfen.", capabilities: [artifact-inspection-preferred, file-write-gated], related: [inhaltsprovenienz-review, natuerliches-schreiben, deutsche-typografie, tool-permission-review]}',
    ])
    text = replace_once(text, marker, addition, "skill catalog security insertion")
write(path, text)


# ---------------------------------------------------------------------------
# Dokumentation/Skill-Katalog.md
# ---------------------------------------------------------------------------
path = "Dokumentation/Skill-Katalog.md"
text = read(path)
text = replace_once(text, "Der Katalog enthält aktuell 148 zentrale Skills:", "Der Katalog enthält aktuell 150 zentrale Skills:", "human catalog total")
text = replace_once(text, "- Sicherheit: 3;", "- Sicherheit: 5;", "human catalog security count")
text = replace_once(text, "alle neun Finanz-Skills sowie `korrekturlektorat`", "alle neun Finanz-Skills, die beiden neuen Security-Skills sowie `korrekturlektorat`", "human catalog coverage sentence")
old_total = "Aktueller Gesamtstand: 148 Skills, davon 123× `partial` und 25× `none`, 0× `core`/`broad`; 123 Skill-Evalpacks mit insgesamt 640 definierten Cases."
new_total = """Der Inhaltsprovenienz-/Metadatenhygiene-Hardening-Lauf ergänzt im Bereich Sicherheit zwei neue Skills – `inhaltsprovenienz-review` und `metadaten-hygiene` – jeweils als `experimental` mit `partial` Evalabdeckung. Dafür sind zwei Evalpacks mit jeweils sechs Startfällen definiert, insgesamt 12. Diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**. Detector-Evasion, Watermark-Stealing und die Verschleierung verpflichtender Provenienz oder Disclosure bleiben ausdrücklich außerhalb des lokalen Produktziels.\n\nAktueller Gesamtstand: 150 Skills, davon 125× `partial` und 25× `none`, 0× `core`/`broad`; 125 Skill-Evalpacks mit insgesamt 652 definierten Cases."""
text = replace_once(text, old_total, new_total, "human catalog final totals")
write(path, text)


# ---------------------------------------------------------------------------
# Root README problem-first routing
# ---------------------------------------------------------------------------
path = "README.md"
text = read(path)
if "Provenienz-/Metadatensignale" not in text:
    marker = "| Wissen langfristig strukturieren und pflegen | Wissensmanagement |"
    addition = marker + "\n| Datei auf Provenienz-/Metadatensignale prüfen oder eigene Sharing-Kopie gezielt von sensiblen Metadaten bereinigen | Sicherheit |"
    text = replace_once(text, marker, addition, "README routing row")
write(path, text)


# ---------------------------------------------------------------------------
# upstream-sources.yml
# ---------------------------------------------------------------------------
path = "Dokumentation/upstream-sources.yml"
text = read(path)
if "guillaumemeyer-watermarks-remover-remove-ai-marks" not in text:
    text = text.replace("last_updated: '2026-09-01'", "last_updated: '2026-09-06'", 1)
    marker = "sources:\n"
    block = """sources:
  # ---------------------------------------------------------------------------
  # Sicherheit / Inhaltsprovenienz und Metadatenhygiene
  # ---------------------------------------------------------------------------
  - id: guillaumemeyer-watermarks-remover-remove-ai-marks
    area: Sicherheit
    kind: github-file
    repository: guillaumemeyer/watermarks-remover
    path: skills/remove-ai-marks/SKILL.md
    ref: main
    monitor_mode: exact-sha
    cadence: monthly
    observed_sha: 41193a86405589e542205bbfaa76414569e4dbae
    last_checked: 2026-09-06
    local_impact:
      - Sicherheit/Inhaltsprovenienz-und-Metadatenhygiene.md
      - Sicherheit/Skills/inhaltsprovenienz-review/SKILL.md
      - Sicherheit/Skills/metadaten-hygiene/SKILL.md
      - Workflows/Inhaltsprovenienz-und-Metadatenhygiene.md

  - id: guillaumemeyer-watermarks-remover-ethics
    area: Sicherheit
    kind: github-file
    repository: guillaumemeyer/watermarks-remover
    path: skills/remove-ai-marks/references/ethics.md
    ref: main
    monitor_mode: exact-sha
    cadence: monthly
    observed_sha: 7506562f2d37748fc5129ea89760dfe2c7c27cc4
    last_checked: 2026-09-06
    local_impact:
      - Sicherheit/Inhaltsprovenienz-und-Metadatenhygiene.md
      - Sicherheit/Skills/inhaltsprovenienz-review/SKILL.md
      - Sicherheit/Skills/metadaten-hygiene/SKILL.md
      - Sicherheit/Quellen-und-Inspirationen.md

"""
    text = replace_once(text, marker, block, "upstream source insertion")
write(path, text)


# ---------------------------------------------------------------------------
# upstream-provenance.yml
# ---------------------------------------------------------------------------
path = "Dokumentation/upstream-provenance.yml"
text = read(path)
if "source_id: guillaumemeyer-watermarks-remover-remove-ai-marks" not in text:
    text = text.replace("last_reviewed: '2026-09-01'", "last_reviewed: '2026-09-06'", 1)
    marker = "sources:\n"
    block = """sources:
- source_id: guillaumemeyer-watermarks-remover-remove-ai-marks
  reviewed_at: 2026-09-06
  repository_commit: d9e9590d94e19b39eb2794266292324bfec8249a
  use_class: reference/inspiration
  review_status: assessed
  material_scope: concepts/methods-only
  classification_evidence:
  - Source-specific review used Inspect-first, provenance-class separation, capability detection, before/after evidence and residual-risk concepts as methodological input.
  - Local skills were independently authored with a narrower purpose and explicitly reject detector-evasion, watermark-stealing, destructive purification and provenance-disclosure bypass as product goals.
  - Manual expression comparison found no substantive source sentence, template or runtime structure copied into the registered local impacts beyond generic technical terminology.
  similarity_audit: no-signal
  redistribution_reliance: not-relied-on
  license_spdx: MIT
  license_source: https://github.com/guillaumemeyer/watermarks-remover/blob/d9e9590d94e19b39eb2794266292324bfec8249a/LICENSE
  license_source_commit_or_ref: d9e9590d94e19b39eb2794266292324bfec8249a
  license_path: LICENSE
  license_blob_sha: 0a2436a2facf906e40b9807db070eba97630e0cf
  path_specific_license_notes:
  - Root MIT license was verified at the same reviewed repository commit; redistribution permission is not relied on because local use is concepts/methods-only reference.
  license_status_at_observation: verified-at-snapshot
  notice_requirement: none-for-reference-only
  redistribution_status: not-relied-on
  license_evidence:
    artifact_declarations: []
    same_state_files:
    - path: LICENSE
      blob_sha: 0a2436a2facf906e40b9807db070eba97630e0cf
      spdx: MIT
    notes:
    - License and reviewed source artifacts were observed at repository commit d9e9590d94e19b39eb2794266292324bfec8249a.
  source_snapshot:
    repository: guillaumemeyer/watermarks-remover
    source_path: skills/remove-ai-marks/SKILL.md
    observed_ref: main
    observed_blob_sha: 41193a86405589e542205bbfaa76414569e4dbae
- source_id: guillaumemeyer-watermarks-remover-ethics
  reviewed_at: 2026-09-06
  repository_commit: d9e9590d94e19b39eb2794266292324bfec8249a
  use_class: reference/inspiration
  review_status: assessed
  material_scope: concepts/methods-only
  classification_evidence:
  - Source-specific review used the ownership/authorization, disclosure and honest-reporting boundaries as one input to the local Privacy-/Provenance gates.
  - Local rules independently narrow the allowed job to read-only provenance review and authorized metadata hygiene; no upstream wording or executable material is redistributed.
  - Manual expression comparison found no substantive copied expression beyond unavoidable domain terms such as C2PA, metadata and provenance.
  similarity_audit: no-signal
  redistribution_reliance: not-relied-on
  license_spdx: MIT
  license_source: https://github.com/guillaumemeyer/watermarks-remover/blob/d9e9590d94e19b39eb2794266292324bfec8249a/LICENSE
  license_source_commit_or_ref: d9e9590d94e19b39eb2794266292324bfec8249a
  license_path: LICENSE
  license_blob_sha: 0a2436a2facf906e40b9807db070eba97630e0cf
  path_specific_license_notes:
  - Root MIT license was verified at the same reviewed repository commit; redistribution permission is not relied on because local use is concepts/methods-only reference.
  license_status_at_observation: verified-at-snapshot
  notice_requirement: none-for-reference-only
  redistribution_status: not-relied-on
  license_evidence:
    artifact_declarations: []
    same_state_files:
    - path: LICENSE
      blob_sha: 0a2436a2facf906e40b9807db070eba97630e0cf
      spdx: MIT
    notes:
    - License and reviewed ethics reference were observed at repository commit d9e9590d94e19b39eb2794266292324bfec8249a.
  source_snapshot:
    repository: guillaumemeyer/watermarks-remover
    source_path: skills/remove-ai-marks/references/ethics.md
    observed_ref: main
    observed_blob_sha: 7506562f2d37748fc5129ea89760dfe2c7c27cc4
"""
    text = replace_once(text, marker, block, "upstream provenance insertion")
write(path, text)


# ---------------------------------------------------------------------------
# CHANGELOG.md
# ---------------------------------------------------------------------------
path = "CHANGELOG.md"
text = read(path)
heading = "### Inhaltsprovenienz und Metadatenhygiene"
if heading not in text:
    marker = "Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.\n"
    section = """

### Inhaltsprovenienz und Metadatenhygiene

- Sicherheit um zwei klar getrennte Skills ergänzt: `inhaltsprovenienz-review` prüft Dateien und Inhalte read-only auf belegbare Provenienz-, Metadaten- und Unicode-Signale; `metadaten-hygiene` bereinigt ausschließlich eigene oder ausdrücklich autorisierte Artefakte innerhalb eines konkreten Remove-/Keep-Scopes;
- gemeinsame Fachgrundlage `Sicherheit/Inhaltsprovenienz-und-Metadatenhygiene.md` und Workflow `Workflows/Inhaltsprovenienz-und-Metadatenhygiene.md` ergänzt; Grundmuster ist Inspect → Evidence/Confidence → Erhaltungspflichten → optionales Change Set → Gate → Clean → Re-Inspection → Residual Risk;
- `guillaumemeyer/watermarks-remover` am Repository-Commit `d9e9590d94e19b39eb2794266292324bfec8249a` mit MIT-Lizenz als aktiv beobachtete methodische Referenz aufgenommen; konkrete `remove-ai-marks`- und Ethics-Artefakte sind per Blob-SHA in Upstream-Registry und Provenance dokumentiert, ohne Runtime-, Plugin-, Service- oder Sync-Abhängigkeit;
- bewusst nicht übernommen: Detector-Evasion und „human score“-Optimierung, statistische Rewrite-Rezepte zur Watermark-Reduktion, Watermark-Stealing, Secret-Key-Rekonstruktion, destructive Pixel-/Audio-/Video-Purification als allgemeine Fähigkeit sowie das Entfernen verpflichtender Attribution-, Provenienz- oder Disclosure-Signale;
- Unicode-Hygiene gegen False Positives geschärft: ungewöhnliche Spaces, Bidi-, Zero-width- oder andere Unicode-Zeichen sind nicht automatisch Watermarks; aggressive Normalisierung benötigt konkreten Zweck und Nebenwirkungsprüfung;
- zwei neue Evalpacks mit jeweils sechs Startfällen ergänzt, insgesamt 12 definierte Cases zu read-only Provenienzprüfung, unsupported Markerklassen, Unicode-False-Positives, GPS-/Privacy-Hygiene, verpflichtender Attribution, sichtbaren Watermark-Near-Misses, Detector-Evasion und Residual Risk; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- aktueller Gesamtstand damit 150 Skills, 125× `partial`, 25× `none`, 0× `core`/`broad`, 125 Skill-Evalpacks und 652 definierte Cases; keine Maturity hochgestuft, keine Behavioral-Eval-Ergebnisse erfunden und kein Tag oder Release erzeugt.
"""
    text = replace_once(text, marker, marker + section, "changelog insertion")
write(path, text)

print("provenance hygiene closeout patches applied")
