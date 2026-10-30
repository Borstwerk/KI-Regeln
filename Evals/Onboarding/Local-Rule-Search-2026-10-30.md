# Eigenständige QMD-Regelsuche: begrenzter nativer Nachweis

## Vorab festgelegter Scope

Öffentliche Engine `@tobilu/qmd` 2.8.3, Node.js 24.22.1 auf Windows,
eigener Index über die explizite Git-Auswahl dieses Repositories. Der getestete
Quellencommit und die Code-/Lockfile-Hashes werden bei Ausführung festgehalten.
Nur QMD-Indexierung und BM25 `searchLex`; keine Modelle, Embeddings, Expansion,
Reranker, APIs, privaten Projektinhalte oder Anwendung eines externen Skills.

Reproduzierbarer, ausdrücklich gestarteter Aufruf nach lokaler Einrichtung:
`python Evals/Onboarding/run_rule_search_native.py --run` mit der vorhandenen
Harness-Python-Runtime. Der [feste Prüflauf](run_rule_search_native.py) installiert
nichts und erzeugt je Aufruf einen neuen lokalen Bericht, ohne alte zu überschreiben.

Die vier ersten Suchbegriffe wurden schon während der Entwicklung erprobt.
Sie sind bekannte Entwicklungsfälle und keine unabhängigen Held-out-Fragen.
Ihre jetzige Wiederholung prüft die endgültige Einrichtung und Quellbindung.

| Suchbegriff | Erwartung innerhalb der höchstens fünf Treffer |
| --- | --- |
| `Skill Verbesserung Fehler` | `Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md` oder `Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md` |
| `Teststrategie Grenzwerte` | `Testing-und-QA/Skills/test-design/SKILL.md` oder `Testing-und-QA/README.md` |
| `MCP Berechtigungen` | `Sicherheit/MCP-und-externe-Tools.md` oder `Sicherheit/Skills/tool-permission-review/SKILL.md` |
| `Workflow beitragen` | `CONTRIBUTING.md` oder `PROJECT.md` |
| `zzretrievalcanaryf72ea4bd` | leere Trefferliste; synthetische Canary liegt nur in ignoriertem lokalen Arbeitsbestand |

Zusätzlich mit echten, ausschließlich synthetischen temporären Git-Repositories
und derselben QMD-Engine prüfen:

1. vollständiger Build und Treffer für eine bekannte Quelle mit Unicode-Dateiname;
2. geänderte ausgewählte Quelldatei macht den Index unbrauchbar, keine alten Treffer;
3. leere ausgewählte Markdown-Datei wird von QMD ausgelassen: der Controller muss
   den Teilindex anhand der aktiven Pfadmenge zurückweisen, auch ohne OS-Lesefehler;
4. nach diesem fehlgeschlagenen Neubau bleibt der Index unbereit.

Vorher-/Nachher-Hashes der ausgewählten Originaldateien vergleichen. Setup separat
aus leerem Paketordner mit unverändertem Lockfile und `--ignore-scripts` prüfen.
Unit-Tests mit injiziertem Worker und kontrollierte Brechproben tragen nur den
Controllervertrag; echte SDK-Läufe werden davon getrennt erfasst.

## Aussagegrenzen

Ein positiver Suchfall beweist Auffindbarkeit für genau diese Begriffe, keinen
allgemeinen Qualitätsgewinn oder semantisches Verständnis. Scores sind native
BM25-Rangwerte, keine Wahrscheinlichkeit fachlicher Richtigkeit. Vollständigkeit
bezieht sich auf die Manifestauswahl, nicht auf alle Repository-Dateien.

Keine Registry-/Maturity-/Gate-Hochstufung und keine Übernahme privater Inhalte.
Nicht erprobte Plattformen und semantische Pfade bleiben `NOT RUN`.

## Ergebnis

Der vor Ausführung veröffentlichte Quellen-/Codecommit ist
`60dd0f7613393b40c59b5da38ade76247b0dbd5b`. Die
[maschinenlesbare Evidence](Local-Rule-Search-2026-10-30.json) bindet ihn an
Code-/Lockfile-Hashes, Protokoll, native Ergebnisse und Gegenproben.

| Teil | Beobachtung | Status |
| --- | --- | --- |
| Frisches Setup | leerer Paketordner; pnpm 11.25.0, festes Lockfile, `--ignore-scripts`; QMD 2.8.3 geladen | PASS lokal Windows |
| Nativer Index | 72 ausgewählte Dokumente; vollständige aktive Pfadmenge, keine übersprungene Datei | PASS |
| Vier bekannte Entwicklungsfragen | jeweils erwartete Quelle unter den höchstens fünf Treffern | PASS für diese Begriffe |
| Ausgeschlossene Canary | leere Trefferliste | PASS |
| Unicode-Dateiname im synthetischen Repo | bekannte Quelle exakt gefunden | PASS |
| Geänderte synthetische Quelle | `stale`, null Worker-Aufrufe, keine alten Treffer | PASS |
| Leere ausgewählte Datei | echte QMD-Auslassung trotz `skipped: 0`; aktive Pfadmenge unvollständig, Build zurückgewiesen | PASS Gegenprobe |
| Nach fehlgeschlagenem Neubau | Status `missing`, kein alter Index bereit | PASS |
| Originaldateien | alle ausgewählten Rohbytes vor/nach dem Lauf unverändert | PASS |

Die PowerShell-Grenzprobe `-Query '-Quick'` gelangt als Suchtext bis zur
Engine und liefert eine gültige leere Trefferliste; sie wird nicht mehr als
Python-Option interpretiert. Ein leerer Treffer ist kein Retrieval-Erfolg.

24 Controller-Testmethoden und die benachbarten bestehenden Prüfungen ergeben
zusammen 52 Tests: OK mit einem bestehenden Windows-Symlink-Skip. Die
Controller-Tests verwenden echte Git-/Dateisystemgrenzen und einen injizierten
Worker; sie sind getrennt vom oben ausgeführten QMD-Nachweis. Zwei tatsächliche
frühe REDs (DEL-Zeichen und nicht gekapselte Worker-Exception) wurden korrigiert.
Die beim Review gefundenen CLI-/DB-Redirect-Grenzen sind regressionsgeprüft.

Zwei ausschließlich im Speicher kontrolliert entfernte Guards wurden von den
jeweiligen Tests erkannt: Trefferbindung mit vier Assertions, vollständige aktive
Pfadmenge mit drei Assertions. Das ist synthetische Wirksamkeitsevidence für die
Controller-Guards; der Produktionscode wurde dafür nicht verändert.

Getrennte Reviews prüften Plan, Code, Paket-/SDK-Grenzen, Provenance und das
Fehler-Orakel. Keine offenen P1/P2 im abschließend geprüften Scope. Andere
Plattformen, semantische Suche, allgemeines Ranking und Agentenantworten sind
nicht durch diese Beispiele verifiziert. Maturity und Gates bleiben unverändert.
