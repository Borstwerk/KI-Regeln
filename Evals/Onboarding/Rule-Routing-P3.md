# Routing-Suche P3: explizite Beziehungen mit Quellenbeleg

Vorabvertrag vom 30.10.2026. Basis `a2d8147` nach Merge von P2/PR #114.
Scope: P3 des [Umsetzungsplans](../../Dokumentation/Skill-Routing-Suche-Umsetzungsplan.md).
Die fünf eingefrorenen P3-Fälle in [rule-routing-cases.json](rule-routing-cases.json)
bleiben unverändert. Natürliche Agentenauswahl ist ein späterer eigener Nachweis.

## Ableitung und Herkunft

Ein kleines reines Modul `tools/rule_relations.py` besitzt
`derive_relations(catalog, overlays, workflow_sources, source_hashes)`.
Eingabe sind Daten desselben geprüften Git-Snapshots; Workflowwerte sind UTF-8-Bytes.
Rückgabe ist eine deterministisch sortierte Liste von Kanten. Fehler im
strukturierten Inventar ergeben `ValueError`, im Controller einen sichtbaren SearchError.

Kantenform:

```json
{"type":"related","from":"skill:bewertungsanalyse","to":"skill:unternehmensanalyse",
 "target_path":"Finanzen/Skills/unternehmensanalyse/SKILL.md",
 "source":{"path":"skill-catalog.yml","sha256":"...","field":"skills[bewertungsanalyse].related"}}
```

- `related`: gerichtete deklarierte Katalogbeziehung, keine implizite Gegenrichtung oder transitive Expansion.
- `mentions`: registrierter Workflow → ausdrücklich als einfacher Inline-Code genannte bekannte Skill-ID. Fenced Codeblöcke werden ausgelassen. Wiederholte Nennungen werden zu einer Kante mit sortierten 1-basierten `source.lines` zusammengefasst. Keine Pflicht-/Kerninterpretation aus Prosa.
- `checkpoint`: registrierter Checkpoint → Overlay-Skill, mit Registry-Feld und `phase` aus der Quelle. Kein Trigger- oder Aktivierungsentscheid.
- Jede Kante hat `type`, `from`, `to`, kanonischen `target_path`, Quellpfad und SHA256; deklarierte Felder oder Workflowzeilen begründen die Kante.
- Unbekannte strukturierte Skill-Ziele, doppelte IDs/Einträge, ungültige Listen und nicht vorhandene registrierte Workflowquellen stoppen die Ableitung. Unbekannte freie Inline-Tokens sind keine strukturierten Zieldeklarationen und werden ignoriert.
- Overlay-Phasen und Checkpoints müssen den kanonischen Schemawerten entsprechen; Checkpointlisten sind nichtleer und eindeutig. Das ist Formvalidierung, keine zusätzliche Triggerentscheidung.
- Alle Workflowdateien aus `workflow-index.yml` werden regulär geprüft, exportiert und fingerprintet. Sie bleiben Quellenabhängigkeiten, keine zusätzlichen BM25-Dokumente.
- Workflow-Abhängigkeiten sind zusätzlich auf 256 KiB je Datei und 1 MiB insgesamt begrenzt. Bestehende Suchbudgets und der 72-Dateien-Inhaltsmodus bleiben unverändert.
- `routing_format: 3`, `routing_relations` und erweiterte `routing_dependencies` binden die Ableitung. P2-Indizes werden sichtbar stale; ein fehlgeschlagener Neubau veröffentlicht keinen Teilstand.

## Abruf

QMD-unabhängige API:

`list_relations(root, skill_id=None, workflow=None, checkpoint=None, limit=None, cursor=None)`

Genau ein Selektor ist erforderlich:

- `skill_id`: ausgehende related-Kanten und eingehende Workflow-Nennungen dieses Skills;
- `workflow`: Nennungen dieses registrierten Workflows;
- `checkpoint`: Kandidaten dieses registrierten Checkpoints.

Antwort `mode: relations`, `relations`, `total_relations`, Revision/Fingerprint,
P2-Seitenfelder, `candidates_only: true`, `assessment_performed: false` und Router-Verweise.
Default 25 Einträge, explizit 1–50. Unbekannte Selektoren werden zurückgewiesen.
Gültige Skill-IDs und registrierte Workflows ohne Kanten liefern eine leere Seite;
Inventarmitgliedschaft wird unabhängig von vorhandenen Kanten geprüft.
Die vorhandene Cursorbindung schützt Quelle, Aktion, Selektor, Größe und Ergebnis.
Kein Node, QMD-Index, Secret-/Sessiondienst oder Graphserver nötig.

```powershell
.\Search-KI-Regeln.ps1 -Routing -Relations -SkillId 'context-engineering'
.\Search-KI-Regeln.ps1 -Routing -Relations -Workflow 'Workflows/Software-Feature.md'
.\Search-KI-Regeln.ps1 -Routing -Relations -Checkpoint 'pre-execution'
```

Python-Aktion `relations` mit `--routing` und genau einem von `--skill-id`,
`--workflow`, `--checkpoint`. Limit/Cursor wie bei P2. Ungültige Kombinationen
stoppen vor Installation oder Indexmutation.

## Suchhinweise

Routing-Suche ergänzt `routing_hints`: `items`, `total_relations`, `limit: 20`
und `truncated`. Hinweise werden aus den Skill-Treffern der sichtbaren Seite
abgeleitet: ausgehendes related und eingehende Workflow-Nennungen. Andere Skill-
Nennungen eines gefundenen Workflows kann der Agent bewusst über den Workflow-
Selektor nachladen. Keine rekursive automatische Expansion.

Optional `checkpoint` in der Search-API bzw. `-Checkpoint` im Query-Aufruf ergänzt
Kandidaten genau dieses explizit angegebenen Checkpoints. Der Wert ist im Suchcursor
gebunden. Er beschreibt den vom Aufrufer angegebenen Arbeitszustand; die Description
entscheidet weiter über Relevanz. Ohne Seed und ohne expliziten Checkpoint bleiben
die Hinweise leer. Ein Graph erfindet keine Einstiegstreffer.

Hinweise bleiben von `hits`, BM25-Scores, Ranking und `total_matches` getrennt.
Sie aktivieren nichts und ersetzen weder Original-Descriptions/Near-Misses noch
Workflow-Reads und Katalog-Fallback. Bei Kürzung den konkreten Selektor paginieren.

## Prüfnachweise

Modultests: Typen/Herkunft/Zeilen, explizite Richtungen, Wiederholungen, Zyklen,
optionale Nennungen ohne requires, Fenced-Code-Ausschluss und ungültige Ziel-IDs.
Integration: registrierte Workflowdateien als Abhängigkeiten, gleicher Corpus,
alte Cursor nach Workflowänderung ungültig, unbekannte Ziele vor Worker blockiert,
fehlgeschlagener Build unbereit, QMD-unabhängiger Abruf und begrenzte Hinweise.

Die fünf P3-Fälle werden separat geprüft: related-Bewertung→Unternehmensanalyse;
Architekturworkflow→Trade-off/ADR; expliziter pre-completion-Checkpoint→Citation-Audit;
kein Seed→keine erfundenen Treffer; unbekanntes strukturiertes Ziel→Fehler.
Technische Beziehungsabdeckung ist keine bereits geprüfte semantische Skill-Auswahl.

Status vor Umsetzung: **NOT IMPLEMENTED / NOT RUN**. Keine neuen Abhängigkeiten,
direkten Modell-APIs oder Maturity-Hochstufungen.
