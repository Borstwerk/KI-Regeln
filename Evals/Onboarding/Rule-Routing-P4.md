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

Die CLI läuft ohne User-Konfiguration, Websuche und externe Tools. Development
darf seinen lokalen abgeleiteten Suchcache schreiben; Quellenänderungen und
weitere Außenaktionen sind untersagt. Die grobe Workspace-Sandbox allein erzwingt
keine Cache-only-Grenze: Der Treiber prüft danach Gitstatus und alle Quellbytes und
weist diese Grenze als nachträglich geprüft aus. Andere Fälle laufen read-only.
Kein Claim einer technisch vollständigen Dateisystem- oder Oracle-Abschottung.

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
