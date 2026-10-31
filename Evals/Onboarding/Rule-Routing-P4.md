# P4 – Natürlicher Agentenpfad

Vorabvertrag vom 31.10.2026, Basis `e815a0b` (Merge von P3 / PR #115).
Owner: Integrator; unabhängiger Reviewer für Oracle, Traces und begrenzte Claims.
Methoden: `agent-eval`, `test-design`, `delegation-contract`, `verification-loop`.

## Fester Umfang vor den Modellläufen

Drei frische Codex-CLI-Sessions über das vorhandene ChatGPT-Abo, kein API-Key,
keine direkte Modell-API, keine Installation. Gleiche vorhandene CLI und Modell-
/Reasoning-Einstellung wie im früheren Discovery-Pilot: `gpt-6.1-sol`, `high`.
Je Fall höchstens 240 Sekunden, genau ein Versuch, kein Resume oder Nachprompten.
Rate-Limit, Auth-, Transport- oder Laufzeitfehler bleiben BLOCKED; keine stille
Ausweichruntime und keine Wiederholung zur Auswahl des besten Ergebnisses.

Die [Falldatei](rule-routing-p4-cases.json) enthält Prompts und Oracle getrennt.
Sessions erhalten ausschließlich ihren Prompt und denselben kanonischen
Produktsnapshot; keine Fälle, Evals, Tests, alten Antworten oder Bewertungsregeln.
Normale Repo-Instruktionen bleiben erhalten. Keine erwarteten Skill-IDs oder
Suchqueries werden in die Aufgaben injiziert. Kein LLM-Judge und kein neuer
allgemeiner Agentenrunner.

| Fall | Produkt-/Auswahlerwartung | Prozesserwartung |
| --- | --- | --- |
| development | eigenständige Jobs für Entwicklung, abhängige Agentenarbeit, Kontextauswahl und QA; passende Skills mit begründeter Phase | echte Router-Reads, Software-Workflow und aktuelle Original-Descriptions; keine pauschale Aktivierung aller verwandten Skills |
| fallback | `acceptance-criteria-design` und `test-design` für zwei getrennte Outputs | ohne optionale QMD-Runtime über Katalog/Dateien fortfahren; keine Installation, kein `none` aus Suchfehlschlag |
| trivial | ausschließlich `eins, zwei` | trivialer Direktpfad; kein künstlicher Skill-/Suchlauf |

Für development werden `task-graph`, `delegation-contract`, `context-engineering`
und `code-review` sowie die Implementierungs-/Verifikationsdisziplin aus dem
Software-Workflow geprüft. Code-Review, Testdesign, TDD und Verification dürfen
als spätere Phasen geplant sein: Ein Plan ist keine bereits durchgeführte
Implementierung oder Verifikation. Der Workflow erlaubt TDD **oder eine passende
Implementierungsdisziplin**; ein nach Description-Prüfung begründeter Ersatz ist
zulässig und kein Fehler allein wegen fehlender TDD-Aktivierung.
Konkrete Testfälle besitzen einen eigenen Job (`test-design`). Quellen: aktuelle
kanonische Descriptions und `Workflows/Software-Feature.md`. Fallback verwendet den
bekannten P1-Fehlraum; kein neuer Held-out-Fall oder unabhängiger Generalisierungsnachweis.

## Laufzeit und Isolation

Der kleine [Treiber](run_rule_routing_p4.py) exportiert den fixierten Gitstand in
drei lokale Wegwerf-Arbeitsverzeichnisse und legt dort eine eigene Gitbasis an.
Quellinventar/-hashes und Promptdigests werden vor Modellstart protokolliert.
Evaluator-Artefakte, Tests, GitHub-Konfiguration und der Umsetzungsplan fehlen darin.
Die bestehende portable Python-Runtime wird lokal wiederverwendet; nur development
erhält zusätzlich Zugriff auf die vorhandene gepinnte QMD-Runtime und einen vorab
gebauten Index. Fallback hat ausdrücklich keine QMD-Runtime. Keine Snapshotquelle
wird dazu editiert.

Die CLI läuft ohne User-Konfiguration und mit deaktivierter Websuche. Externe
Toolnutzung ist untersagt und wird anhand der tatsächlich aufgezeichneten Items
geprüft; die Konfigurationsflags allein beweisen keine vollständige Abschottung. Development
darf seinen lokalen abgeleiteten Suchcache schreiben; Quellenänderungen und
weitere Außenaktionen sind untersagt. Die grobe Workspace-Sandbox allein erzwingt
keine Cache-only-Grenze: Der Treiber prüft danach Gitstatus und alle Quellbytes und
weist diese Grenze als nachträglich geprüft aus. Andere Fälle laufen read-only.
Kein Claim einer technisch vollständigen Dateisystem- oder Oracle-Abschottung.
Auch das Root-Tooling für den Indexvorbau wird gegen die fixierten Snapshotbytes
geprüft und separat gehasht; spätere lokale Codeänderungen dürfen nicht unbemerkt
einen Index für den älteren Produktsnapshot erzeugen.

Vor dem ersten Modellaufruf muss die vorhandene Byte-/Read-only-Gegenprobe aus
dem Discovery-Pilot bestehen. Environment-API-Keys und Provider-/Endpointoverrides
werden entfernt; ChatGPT-Login wird geprüft und erzwungen. Tokenusage und Laufzeit
sind Beobachtungen, kein belegter Token-Spar-Lift.

## Auswertung und Stop

Produkt und Prozess separat je Fall bewerten. Ein Modelltext, der einen Read
behauptet, genügt nicht: ausgeführte Toolkommandos, Exitcodes und passende Outputs
gegen die fixierten Quellen prüfen. Ein bezeichneter Skill ohne gelesene Description
ist kein vollständiger Routingnachweis. Optionale Such-/Relations-/Pagingnutzung
wird beobachtet, nicht durch zusätzliche Promptanweisungen erzwungen. Nicht genutzte
Pfade bleiben NOT RUN; ihr technischer P2/P3-Nachweis wird nicht als Agentennutzung
umetikettiert. Es wird kein vollständiger Katalogscan verlangt.

Ein unabhängiger Reviewer prüft Rubrik und später Evidence. Kontrolliert defekte
Bewertungsproben müssen fehlende Pflicht-Reads beziehungsweise fälschlich aktivierte
Skills im trivialen Fall sichtbar scheitern lassen. Historische Evals, Erwartungen
und Suchcode bleiben unverändert. Befunde bleiben FAIL/PARTIAL; Reparaturen an
Produktregeln wären ein eigener nachgelagerter Slice mit neuer Evidence.

Status vor Lauf: **NOT RUN**. Kein A/B-Lift, keine Erfolgsquote über alle Aufgaben,
keine Maturity-Hochstufung und keine Garantie universeller Agentenbefolgung.

## Technische Protokollkorrektur vor Modellstart

Die erste Batch (`15fb68a`, `.validation/routing-p4-20261031`) bleibt **BLOCKED**:
Die CLI lehnte `default_permissions=":workspace-write"` nach 0,03 Sekunden als
unbekanntes Built-in-Profil ab. Null Command-Items, null Usage und keine Antwort;
die übrigen beiden Sessions wurden nicht gestartet. Byte-/Read-only-Gate bestand.
Dieser Start ist keine schlechte Agentenantwort und wird nicht als PASS gewertet.

Vor einem getrennten zweiten technischen Start wird ausschließlich die
CLI-Konfiguration auf `--sandbox workspace-write` beziehungsweise `read-only`
korrigiert, entsprechend [offizieller CLI-Referenz](https://learn.chatgpt.com/docs/developer-commands?surface=cli).
Aufgaben, Oracle, Modell, Budget und Produktsnapshot bleiben unverändert. Batch v2
hat ein eigenes Verzeichnis; die ursprünglichen Artefakte werden nicht überschrieben.
Dies ist eine explizite Korrektur eines Fehlers **vor** Modell-/Antwortauswertung,
keine Wiederholung zur Auswahl einer besseren Antwort. Weiter maximal ein
Modellversuch je Fall; weitere Laufzeitfehler bleiben ohne Wiederholung BLOCKED.

## Ergebnis vom 31.10.2026

Die korrigierte Batch wurde mit Protokollcommit `9aad1e8` genau einmal ausgeführt.
Alle drei Sessions endeten mit Exit 0. Die [kompakte Evidence](Rule-Routing-P4.json)
enthält Prompts, Code-/Quellen-/Protokollhashes, Antworten, ausgeführte Kommandos,
Outputdigests und belegte Description-Reads. Lokale Rohberichte bleiben unter
`.validation/routing-p4-20261031-v2`; Nutzer-/Repositorypfade sind im öffentlichen
Bericht ersetzt. Reasoning und Threadkennungen werden nicht veröffentlicht.

```powershell
# Nur vorbereiten, kein Modellaufruf:
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_p4.py
# Expliziter Live-Pilot mit vorhandenen lokalen Runtimes und CLI-Abo:
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_p4.py --run
```

Vor Live-Ausführung unter Windows `TEMP` und `TMP` auf den beschreibbaren lokalen
Pfad `.validation/tmp` setzen. Der fest benannte Lauf wird nicht überschrieben;
eine bereits gestartete Batch stoppt vor weiteren Modellaufrufen.

| Fall | Produkt | Prozess | Beobachtung |
| --- | --- | --- | --- |
| development | PASS im Fallumfang | PASS im Fallumfang | alle erwarteten Owner samt Original-Descriptions gefunden; Phasen, zwei Dateieigentümer, unabhängiger Review und Nachladeplan getrennt |
| fallback | PASS im Fallumfang | PASS im Fallumfang | Acceptance- und Testdesign getrennt; Grenzwerte und Dublettenfälle mit offenen Fachregeln; direkter Katalog-/Dateipfad |
| trivial | PASS im Fallumfang | PASS im Fallumfang | exakt `eins, zwei`; null Toolkommandos, null Skill-Reads |

Die qualitative Bewertung stammt vom Integrator und einem unabhängigen
Review-Agenten, nicht von menschlicher Blindabnahme oder einer automatischen
Judge-Pipeline. Mechanische Checks prüfen separat tatsächliche Routeroutputs,
kanonische Descriptions, benannte Owner, Quellintegrität und den trivialen Direktpfad.
Die Bewertung vergleicht gegen die vorab fixierten Fälle und ist keine allgemeine
Zertifizierung der Agentenqualität.

Beide nichttrivialen Fälle lesen Master-Router, Katalog, Workflowindex, einen
passenden Workflow sowie Overlay-Registry und Original-Descriptions tatsächlich.
Späte Overlay-Prüfung ist durch weitere Registry-/Description-Reads belegt. Zwei
Kommandos endeten mit Exit 1, weil ihre jeweils letzte `rg --files`-Suche keine
Zielanwendung fand. Die zuvor im selben Kommando ausgeführten Reads waren in den
Outputs vorhanden; das ist kein fehlgeschlagener Owner-Read. Code, Tests und Review
der geplanten Zielanwendung wurden ausdrücklich nicht als durchgeführt behauptet.

Alle 578 Quellen wurden nach jeder Session erneut gehasht und vom unabhängigen
Reviewer geprüft; alle drei Gitstatus waren leer. Beobachtet wurden ausschließlich
lokale `command_execution`- und Antwort-Items, keine Installation, Delegation oder
Außenaktion. Die Byte-/Read-only-Gegenprobe bestand in beiden technischen Batches.

Zwei kontrollierte Änderungen ausschließlich an Kopien der aufgezeichneten
Evidence werden erkannt: Entfernen des tatsächlichen Master-Router-Reads und
Einfügen künstlicher Skill-/Toolnutzung in den trivialen Fall. Die realen Daten
bestehen denselben begrenzten mechanischen Check. Das sind Gegenproben des
Prüfpfads, keine zusätzlichen Modellläufe und kein unabhängiger semantischer Judge.

| Beobachtung | development | fallback | trivial |
| --- | ---: | ---: | ---: |
| Laufzeit in Sekunden | 116,38 | 59,44 | 4,14 |
| Toolkommandos | 12 | 19 | 0 |
| gemeldete Inputtokens | 268867 | 195894 | 15666 |
| darin gemeldete Cached-Inputtokens | 212480 | 143616 | 0 |
| gemeldete Outputtokens | 4044 | 2135 | 57 |

Diese Usage ist die CLI-Meldung über mehrere Modellschritte, keine Messung
einmaliger Kontextgröße und kein Nachweis einer Einsparung. Große beziehungsweise
doppelte Katalog-/Routerausgaben wurden beobachtet; ohne gleiche Kontrollbedingung
werden daraus weder ein Lift noch eine allgemeine Context-Skill-Reparatur abgeleitet.

**Wichtige Grenze:** Auch development nutzte trotz bereitstehendem Index nur
direkte Datei-/Katalogzugriffe. BM25-Suche, Relationsabruf, Pagination und
Descriptorlisting bleiben als **natürliche Agentenpfade NOT RUN**. Die technischen
P2/P3-Nachweise bleiben davon getrennt. Fallback prüft eine angekündigt fehlende
Runtime, keine Erholung nach unerwartetem Runtimefehler. Es gibt keine A/B-Baseline,
keine Wiederholungsstatistik und keinen Held-out-/Vollständigkeitsclaim.

Acht bestehende Discovery-/CLI-Kontrolltests bestehen; `py_compile` und lokaler
Harness werden zusätzlich ausgeführt. Ein erster Kontrolltestlauf nutzte einen
nicht beschreibbaren Standard-Temp-Pfad; nach expliziter Wahl von `.validation/tmp`
bestand derselbe unveränderte Check. Kein Guard oder Oracle wurde abgeschwächt.

P4 liefert damit einen kleinen positiven Prozessnachweis für die direkte natürliche
Skill-Discovery. Die spezielle natürliche Suchfunktionsnutzung und allgemeine
semantische Abdeckung bleiben offen. Der bekannte P1-Retrievalfehlfall aus P3 wird
nicht als behoben dargestellt. Keine Produktregeln, Suchlogik oder Maturity geändert.
