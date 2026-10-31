# Umsetzungsplan: vollständigerer Zugang zu Skill-Kandidaten

Stand: 30.10.2026. Planungsbasis; Umsetzungsevidence wird separat geführt.
Gelesene Codebasis: `6b80949fea00a427303a8dad9a612b59d7fd04ca`.
Bei Umsetzung zuerst aktuellen Branch, Änderungen und Integrationsbasis prüfen.

## Ziel und Grenzen

Agenten sollen für jeden Teiljob passende Skills auffinden, weitere Kandidaten
erreichen und bei hohem Vollständigkeitsbedarf alle kanonischen Beschreibungen
systematisch prüfen können. Der Maßstab bleibt nachvollziehbare Qualität bei
kleiner lokaler Infrastruktur.

Drei verschiedene Nachweise auseinanderhalten:

| Aussage | Nachweis |
| --- | --- |
| Alle Katalog-Skills sind verfügbar | Jede aktuelle kanonische ID ist genau einmal enthalten |
| Alle Beschreibungen wurden ausgeliefert bzw. geprüft | Vollständige Enumeration; tatsächliche fachliche Prüfung zusätzlich je ID dokumentieren |
| Alle relevanten Skills wurden gefunden | Nur für vorab annotierte Fälle messbar; keine allgemeine semantische Vollständigkeitsgarantie |

Der aktuelle Bestand umfasst 155 Skills in 165 Routing-Dokumenten. Die bisherige
native Evidence enthält drei erfolgreiche positive Entwicklungsfragen, einen
ADR-Fehlfall und einen erfolgreichen Leertrefferfall; Gesamturteil **PARTIAL**.
Sie bleibt unverändert: [bisheriger Bericht](../Evals/Onboarding/Local-Rule-Routing-2026-10-30.md).

Verbindliche Grenzen:

- Bestehenden Python-Controller, QMD-BM25-Worker und PowerShell-Einstieg erweitern.
- Keine neuen direkten Modell-APIs, Graphdatenbank, Dienste, Hintergrundjobs oder allgemeine Agentenplattform.
- Bestehende CLI-Abos nur für einen späteren ausdrücklich gestarteten Agenten-Probelauf; keine automatischen Modellaufrufe durch die Suche.
- Der getrennte 72-Dateien-Inhaltsmodus bleibt kompatibel. Keine pauschale Erweiterung auf alle Repository-Dateien.
- Suchbudgets bleiben 200 Dokumente, 256 KiB je Dokument und 1 MiB insgesamt; tatsächlichen abgeleiteten Suchtext ebenfalls prüfen.
- Pflicht-Discovery, kanonische Skill-Descriptions, Near-Misses und lokale Gates bleiben maßgeblich. Beziehungen aktivieren keine Skills.
- Graphify bleibt ein möglicher späterer Vergleichskandidat. In diesen Slices wird es nicht installiert oder eingebunden.

## Arbeitsweise und Skills

Der Rahmen ist [Software-Feature](../Workflows/Software-Feature.md).
`task-graph` strukturiert Abhängigkeiten, `delegation-contract`
die Agentenaufträge, `test-design` die Produktverträge und `agent-eval` die getrennte
Prüfung natürlicher Skill-Auswahl. Eine kompakte Tabelle reicht zur Darstellung.
`system-design` ist für diese begrenzte Erweiterung kein zusätzlicher Primärowner.
Bei der späteren Implementierung passende Verification und unabhängigen Review
neu routen; geladene Skills autorisieren keine Außenaktionen.

## Reihenfolge und Abhängigkeiten

```text
P0: Anforderungen, Schnittstellen, Fälle und Baseline festlegen
  → P1: Katalogtexte suchbar machen, Herkunft erhalten
      ├→ P2: Trefferseiten und vollständige Descriptor-Auflistung
      └→ P3: explizite Beziehungen als isolierten Baustein ableiten
          P2 + P3 → P4: integrieren und Agenten-Routing dokumentieren
                    → P5: Vergleich, Review und begrenzte Abnahme
```

P2 und P3 dürfen nach festgelegtem Quellen-/Ergebnisvertrag parallel laufen.
Der gemeinsame Controller, die JS-Bridge und das PowerShell-Script haben genau
einen Änderungsverantwortlichen. Einzelergebnisse werden vor Integration nicht
als fertige Gesamtlösung bezeichnet.

## P0 – Verträge und Messbasis

**Owner:** Integrator; Eval-Agent entwirft die Fälle, unabhängiger Reviewer prüft das Oracle.

Vor Codeänderungen festlegen:

- Suchdokument-/Quellenabbildung, Pagination, Descriptor-Ausgabe und Beziehungsformat;
- Fehlerverhalten bei stale, fehlenden Quellen, unklarer Herkunft und Budgetüberschreitung;
- einen kleinen Falldatensatz und Grader, dann unveränderliche Vorher-Baseline;
- ein gemeinsames eingefrorenes Quellenpaket für alte und neue Implementierung. Ein Checkoutwechsel allein trennt Code- und Quellenänderungen nicht sauber.

**Abnahme:** Erwartungen stammen aus kanonischen Descriptions und Near-Misses,
nicht aus aktuellen Suchtreffern. Jeder Fall hat Quellenbegründung und Hashbindung.
Unsichere Erwartungen vor der Implementierung klären. Ohne belastbare Baseline
keinen Verbesserungsclaim abgeben.

## P1 – Katalogtexte im bestehenden Suchdokument

**Owner:** Integrator; Tests aus dem vereinbarten Contract durch Eval-Agenten.

Pro Skill ein deterministisches Suchdokument am bisherigen relativen Pfad:
kanonischer Skill-Inhalt plus eindeutig abgeleitete Felder aus dem Katalog
(`id`, `area`, `purpose`). Description und Near-Miss bleiben im Original-Skill.
Keine zweite gepflegte Begriffsliste oder frei erfundene Alias-Registry.

Quellenhash und Suchdokumenthash getrennt halten. Die Abbildung bindet
Suchpfad, Suchtext-Hash, kanonischen Pfad, Originalhash und Kataloghash an denselben
Snapshot. Worker-Treffer gegen die tatsächlich indexierten Bytes prüfen und
anschließend die Quellenbindung validieren. Quellenexport und abgeleiteten Corpus
mit den bestehenden Auswahl-/Umfangsregeln prüfen. Ein Formatwechsel macht alte
Routing-Indizes sichtbar stale; keine stille Übernahme inkompatibler Snapshots.

Ein Treffer auf Katalogtext benennt dessen Herkunft. Generierte Ausschnitte sind
keine wörtlichen Originalzitate aus `SKILL.md`.

**Abnahme:** Ein ausschließlich im `purpose` vorhandener Begriff findet den
richtigen kanonischen Skill. Die ursprüngliche ADR-Frage wird unverändert erneut
ausgeführt. Manipulierte Ableitungen, Quellenänderungen und Teilindizes werden
zurückgewiesen. Der Inhaltsmodus behält seinen bisherigen Vertrag.

## P2 – Weitere Treffer und vollständige Beschreibungslisten

**Owner:** Integrator; abhängig von P1 und dem P0-Vertrag.

Bei dem begrenzten Bestand zuerst die gesamte vom BM25-Worker ermittelte
Treffermenge innerhalb des gültigen Corpus abrufen und prüfen. Globale Ordnung:
Score absteigend, kanonischer Pfad als eindeutiger Tie-Breaker. Danach Seiten
schneiden. Die tatsächliche Engine-Grenze mit einer Fixture über zehn Treffern
prüfen, bevor eine exakte Trefferzahl behauptet wird.

Ein Cursor bindet Quellenfingerprint, genaue Anfrage, Seitengröße und Position.
Keine serverseitigen Suchsessions erforderlich. Query-/Snapshotwechsel oder
manipulierte Cursor erzeugen einen sichtbaren Fehler. `has_more`, `next_cursor`
und Trefferzahl beschreiben ausschließlich diese BM25-Ergebnismenge.

Zusätzlich ein QMD-/Node-unabhängiger Pfad, der sämtliche Skills nach ID sortiert
aus den geprüften Gitquellen auflistet. Je Eintrag: ID, Description, `purpose`,
Pfad, Maturity, Eval-Coverage, Capabilities und `related`. Dieselbe Snapshotbindung
und begrenzte Seiten verwenden; keine Installation und kein Modellstart.

**Abnahme:** Seiten enthalten keine Dubletten oder Auslassungen. Über alle
Descriptor-Seiten erscheint jede Katalog-ID genau einmal, auch ohne QMD-Runtime.
Ausgeliefert heißt nicht geprüft. Der Agent liest bei einer gründlichen Prüfung
alle Seiten und dokumentiert pro ID/Teiljob geeignet, unpassend oder unklar;
für mögliche Owner und Zweifelsfälle folgen Original-Skill und Near-Miss.
Verbleibende ungeprüfte oder unklare Einträge verhindern einen vollständigen
fachlichen Prüfclaim. Bei fehlendem Cache-Schreibrecht bleibt direkter Dateizugriff.

## P3 – Explizite Beziehungen ohne Graphplattform

**Owner:** Beziehungs-Agent in eigenem Hilfsmodul mit separaten Tests;
Integrator ergänzt danach Quellenexport und Anbindung im Controller.

Eingabe sind ausschließlich geprüfte Snapshotbytes und kanonische IDs.
Ausgabe ist eine kleine lokale Beziehungsstruktur, beispielsweise als abgeleitetes
JSON neben dem vorhandenen Snapshot. Keine eigene persistente Graphdatenbank.

| Beziehung | Quelle | Bedeutung |
| --- | --- | --- |
| Skill → verwandter Skill | `skill-catalog.yml: related` | zusätzlichen Kandidaten prüfen |
| Checkpoint → Overlay-Skill | `routing-overlays.yml` | Description zum angegebenen Zeitpunkt prüfen |
| Workflow → genannter Skill | registrierte Workflow-Datei | Source-Verweis, keine automatische Pflichtaktivierung |

Jede Kante trägt Quellpfad, Feld bzw. Abschnitt und Hash. Bei Workflow-Nennungen
bleibt der Typ zunächst `mentions`. Ein Kern-/Pflichtclaim benötigt eine eindeutig
unterstützte ausdrückliche Markierung; aus beiläufigen Nennungen oder optionalen
Schritten wird kein `requires` erfunden. Die direkte Workflow-Prüfung bleibt bestehen.

Nur Workflows aus `workflow-index.yml` einlesen. Ihre konkreten Dateien werden
zusätzliche geprüfte und fingerprintete Quellenabhängigkeiten, keine weiteren
BM25-Dokumente. Auch eine Änderung nur am Workflow-Inhalt macht den abgeleiteten
Beziehungsstand stale. Unbekannte strukturierte Ziel-IDs oder fehlende registrierte
Dateien zurückweisen; uneindeutige Prosa nicht in Pflichtkanten umdeuten.

Zunächst direkte Nachbarn anbieten, dedupliziert und mit sichtbaren Umfangsgrenzen.
Hinweise getrennt von lexikalischen Treffern ausgeben; keinen BM25-Score für
Graphnachbarn erfinden. Keine rekursive automatische Expansion. Ein Graph ohne
Einstiegstreffer ersetzt weder Katalog-Fallback noch Descriptor-Prüfung.

**Abnahme:** Jede Kante ist zur Quelle rückführbar; optionale Erwähnungen werden
nicht verpflichtend; Zyklen erzeugen keine Schleife; Workflow-Änderungen invalidieren
den Stand. Suchbudgets und Anzahl indexierter Dokumente werden nicht erhöht.

## P4 – Integration und tatsächlicher Agentenpfad

**Owner:** Integrator; Dokumentations-Agent erst nach stabilem Verhalten.

CLI-Oberfläche für P2 und P3; die tatsächliche Agentennutzung bleibt separat zu prüfen:

```powershell
# normale Kandidatensuche, weitere Seiten bei Bedarf
.\Search-KI-Regeln.ps1 -Routing -Query 'Architekturentscheidungen Alternativen Konsequenzen'
.\Search-KI-Regeln.ps1 -Routing -Query 'Architekturentscheidungen Alternativen Konsequenzen' -Cursor '<next_cursor>'

# alle Beschreibungen abschnittsweise für eine gründliche Prüfung abrufen
.\Search-KI-Regeln.ps1 -Routing -ListSkills -Limit 25
.\Search-KI-Regeln.ps1 -Routing -ListSkills -Limit 25 -Cursor '<next_cursor>'

# belegte Beziehungen gezielt nachladen, ohne QMD-Index
.\Search-KI-Regeln.ps1 -Routing -Relations -SkillId 'context-engineering'
.\Search-KI-Regeln.ps1 -Routing -Relations -Workflow 'Workflows/Software-Feature.md'
.\Search-KI-Regeln.ps1 -Routing -Relations -Checkpoint 'pre-execution'
```

`AGENTS.md`, Master-Router und lokale Suchanleitung auf diesen Ablauf abstimmen:
Auftrag in Teiljobs zerlegen → suchen → weitere Seiten und Beziehungshinweise
prüfen → kanonische Descriptions/Near-Misses prüfen → bei hohem Vollständigkeitsbedarf
Descriptor-Prüfung → vorhandene Workflow-/Overlay-Gates. Für leere, unpassende
oder nicht verfügbare Suche bleibt der direkte Katalog-/Dateipfad verbindlich.

**Abnahme:** Bestehende Aufrufe funktionieren weiter. Ein mehrteiliger Auftrag
kann mehrere passende Owner erreichen; bloße Beziehungshinweise aktivieren nichts.
Kein Skill-/Near-Miss-Vertrag und kein Bootstrap-Gate wird im Suchcode dupliziert.

## P5 – Kleine, reproduzierbare Abnahme

**Owner:** Eval-Agent für Ergebnisse; unabhängiger Reviewer für Oracle und Claims;
Integrator für gemeinsame Regression und finale Scopeprüfung.

24 vorab festgelegte Fälle als Startumfang:

| Gruppe | Anzahl |
| --- | ---: |
| bisherige positive Entwicklungsfragen einschließlich ADR-Fehlfall | 4 |
| neue Formulierungen: Alltagssprache, DE/EN, Flexion, Komposita | 4 |
| Aufträge mit mehreren eigenständigen Jobs | 4 |
| Beziehungen: related, Workflow, Overlay, fehlender Einstiegstreffer | 4 |
| Near-Misses und negative Eingaben, einschließlich bisherigem Leertreffer | 4 |
| technische Verträge: Pagination, stale, ungültige Beziehung, Descriptor-Abdeckung | 4 |

Die vier technischen Verträge separat von Retrievalmetriken auswerten. Je
inhaltlichem Fall `required_skills`, zulässige Alternativgruppen und unpassende
Skills mit Quellenbegründung festlegen. Ein unpassender Suchkandidat ist zunächst
Rauschen; erst seine fachliche Aktivierung ist eine Fehlaktivierung.

Gleiche Fälle, Quellen, QMD-/Node-Version und Kandidatenbudgets für vorher/nachher.
Direkte Treffer unter den ersten zehn, vollständige Pagination und zusätzliche
Beziehungshinweise getrennt berichten. Ein erweitertes Budget mit Nachbarn wird
nur gegen dasselbe Gesamtbudget der Baseline verglichen. Ränge, Pflichtskill-
Abdeckung, Kandidatenzahl und Laufzeit pro Fall statt nur einer Gesamtnote erfassen.

Liefergates: Herkunfts-/Snapshot-/Budgetguards und vollständige Enumeration müssen
halten; keine Regression der bisher erfolgreichen Pflichtfälle; ADR-Zielfall muss
verbessert sein. Weitere nicht erfüllte Case-Erwartungen bleiben FAIL/PARTIAL.
Schwellen oder Erwartungen werden nicht nachträglich gelockert. Bleiben Lücken,
werden sie Grundlage eines separaten nächsten Slices statt eines allgemeinen PASS.

Eine JSON-Falldatei und eine begrenzte Erweiterung des vorhandenen nativen Treibers
reichen. Controller-Tests bleiben von echten QMD-Läufen getrennt. Für neue kritische
Guards kontrollierte kaputte Fixtures mit geprüftem Fehlergrund verwenden.
Vorhandenen lokalen Validation Harness nutzen; native Läufe nur ausdrücklich,
gegen fixierte Code-/Quellenstände und mit unveränderten historischen Berichten.

Optional danach wenige natürliche Agentenläufe über das vorhandene CLI-Abo:
Pflicht-Reads, Owner-Auswahl, Near-Misses, Paging und Fallback beobachten. Kein
LLM-Judge und keine neue Orchestrierung. Dieser Prozessnachweis bleibt vom
modellfreien Retrievalvergleich getrennt; wenn er entfällt, Auswahlqualität UNVERIFIED.

## Delegationsverträge und Dateieigentum

Maximal Integrator plus drei aktive Subagenten; Rollen bei Bedarf nacheinander
besetzen. Gemeinsame Quellen sind lesbar, veränderliche Arbeit bleibt getrennt.

| Rolle | Ergebnis und Dateiscope | Voraussetzung |
| --- | --- | --- |
| Integrator | P0-Verträge; Controller, JS, PowerShell; Integration | aktueller sauber eingeordneter Quellenstand |
| Eval-Agent | Falldatei, eigene Testdateien, begrenzte Erweiterung des nativen Treibers | Oracle vor Code; gemeinsame Schnittstellen vor parallelen Tests |
| Beziehungs-Agent | isoliertes Ableitungsmodul und eigene Tests | P0-Vertrag und P1-Quellenübergabe |
| Reviewer / später Dokumentations-Agent | read-only Review; anschließend nur benannte Dokumente | stabiler jeweiliger Slice; Rollen getrennt bewerten |

Keine parallelen Änderungen an denselben Dateien. Bei geteiltem Workspace
abweichende Dateiscopes technisch bzw. per Diff kontrollieren; für überlappende
Arbeit isolierte Checkouts/Worktrees einsetzen. Keine neue Agenten-Runtime bauen.

Jeder Auftrag enthält Ziel, erlaubte Dateien, Quellen, Rechte, Abnahme, Evidence,
Stop-Bedingungen und den abnehmenden Integrator. Subagenten liefern Ergebnis,
geänderte Dateien, tatsächliche Prüfstatus, Kriterienzuordnung und Unsicherheiten.
Neue Abhängigkeiten, zweifelhafte Herkunft, notwendige Gate-Abschwächung,
widersprüchliche Oracles oder Arbeiten außerhalb des Scopes an den Integrator geben.
Lokale Code-/Testrechte beinhalten keinen eigenen Push, Merge oder Release.

## Aktueller Status

P0 ist als Kriterien-/Quellenvertrag eingefroren. Der technische P1-Slice ist mit
getrenntem [Vorher/Nachher-Nachweis](../Evals/Onboarding/Rule-Routing-P0-P1.md)
geliefert: 13 → 15 von 16 Suchfällen, ohne Regression; Retrievalurteil PARTIAL.
P2-Trefferseiten und Descriptor-Auflistung sind implementiert; der getrennte
[P2-Nachweis](../Evals/Onboarding/Rule-Routing-P2.md) belegt die drei Vertragsfälle
mit echten QMD-Seiten und allen 155 Descriptions ohne Node/QMD. Die verbleibende
P1-Retrievallücke bleibt PARTIAL.
P3-Beziehungen sind gemäß [separatem Vertrag](../Evals/Onboarding/Rule-Routing-P3.md)
implementiert und **IN VERIFICATION**: direkte quellenbelegte Beziehungen,
QMD-unabhängige Selektoren, begrenzte Suchhinweise und explizite Checkpoints.
Der native P3-Nachweis steht noch aus. Die technische Suchanleitung und die
optionalen Agentenverweise werden dafür angepasst; die verbleibende natürliche
Agentenprüfung und Gesamtabnahme aus P4/P5 sind **NOT RUN**. Frühere Testresultate
belegen ausschließlich ihren jeweiligen Stand; dieser Plan selbst ist kein Qualitätsnachweis.
