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

Vorabprotokoll; endgültige native Evidence folgt separat.
