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

## Ergebnis vom 31.10.2026

Vorabvertrag: `cf7ce3a`; Implementierung und fester nativer Treiber: `a33e367`.
Die [maschinenlesbare Evidence](Rule-Routing-P3.json) bindet ausgeführte
Checkoutbytes, Gitblobs, unveränderte Fälle, Protokolle und Rohberichte per SHA256.
CRLF/LF-Äquivalenz ist ausdrücklich ausgewiesen. Historische Berichte bleiben unverändert.

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_p3_native.py --run
```

Der [feste Treiber](run_rule_routing_p3_native.py) benötigt einen committeten
Quellstand und die vorhandene optionale QMD-Runtime; er installiert nichts.
Er prüft fünf technische Entwicklungsfälle, keinen gehaltenen Agentenbenchmark.

| Kriterium | Beobachtetes Ergebnis |
| --- | --- |
| related | `bewertungsanalyse` direkt gefunden; gerichteter Hinweis auf `unternehmensanalyse` mit Katalogherkunft |
| Workflow | expliziter Architekturworkflow liefert beide erforderlichen Skill-Nennungen; zusätzlich liefert die unveränderte natürliche Query `adr` und `architecture-tradeoff-analysis` direkt |
| Overlay | `research-synthesis` direkt gefunden; explizit übergebener `pre-completion`-Checkpoint liefert `citation-audit` |
| kein Einstiegstreffer | unveränderte Nonsense-Query: null Treffer und null Hinweise ohne Checkpoint |
| ungültiges Ziel | unbekannte related- und Overlay-ID vor Worker zurückgewiesen; kein bereiter Teilstand |

**5/5 technische Verträge PASS.** Der Workflowselektor wurde vom Evaluator aus
dem eingefrorenen Fall vorgegeben. Sein Erfolg allein beweist keine selbstständige
Workflowentdeckung. Die zusätzlich beobachteten direkten Treffer bleiben ein
einzelner bekannter Entwicklungsfall.

Der Corpus bleibt bei 165 Dokumenten einschließlich aller 155 Skills. 50
registrierte Workflows ergänzen die drei bisherigen Quellenabhängigkeiten, nicht
die BM25-Dokumentmenge. Abgeleitet wurden 512 related-, 229 mentions- und sieben
Checkpointkanten. QMD-freie Selektoren wurden über Seiten der Größe zwei geprüft;
Node-, Worker- und Ready-Index-Aufrufe waren dabei durch verbotene Stubs gesperrt.
Alle geprüften Zeilen, Zielpfade und Quellenhashes stimmen mit dem Snapshot überein.

Eine echte native Fixture bestätigt: Änderung ausschließlich einer Workflowquelle
ergibt stale; nach Rebuild werden alte Such- und Relationscursor als invalid-cursor
abgewiesen. Dokument- und Suchdokumenthashes bleiben dabei gleich. Ungültige
Quellen erreichen den Worker nicht. Originalbytes blieben in allen geprüften
Quellen unverändert.

103 relevante lokale Tests: OK, davon ein bestehender Windows-Symlink-Skip.
Die 18 neuen Modul-/Integrationsmethoden prüfen Ableitung, Herkunft, Budgets,
Quellenwechsel, Selektoren, begrenzte Hinweise und CLI-Grenzen. Zwei ausschließlich
im Speicher entfernte Guards werden von den zugehörigen Tests erkannt:
unbekannte related-ID und Nennungen innerhalb eines Fenced-Codeblocks. Jeweils
eine Assertion, null Testfehler; Produktionsbytes unverändert. Danach neun
Modultests erneut grün. Unabhängiger Code-/Treiber-/Artefaktreview: keine erkannten
P1/P2-Blocker.

PowerShell wurde mit normalem Machine-/User-PATH geprüft: alle drei Selektoren
funktionieren mit ausdrücklich ungültigem Node-Pfad; die Checkpoint-Query liefert
Research-Seed und Citation-Hinweis über die vorhandene Node-Fallbackruntime.

Der eingefrorene P1-Regressionstest bleibt bei **15/16, PARTIAL**, mit identischen
Fallstatus. `Akzeptanzkriterien beobachtbar` findet weiterhin den erforderlichen
Skill nicht. Der historische Kernpaket-Hash bleibt gleich; alle registrierten
Workflowabhängigkeiten wurden für Format 3 separat ergänzt und separat gehasht.
Querys, Oracle und Trefferbudget wurden nicht verändert. Exit 2 dieses Treibers
kennzeichnet den offenen Fall und wird nicht als allgemeiner PASS ausgegeben.

P3 ist technisch nachgewiesen. Natürliche Agentenentscheidungen aus P4/P5 bleiben
**NOT RUN**, allgemeine semantische Vollständigkeit **UNVERIFIED**. Keine neuen
Abhängigkeiten, direkten Modell-APIs oder Maturity-Hochstufungen.
