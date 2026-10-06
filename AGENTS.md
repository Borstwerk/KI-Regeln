# KI-Regeln – Agent Bootstrap

Diese Datei ist der kleinste Einstiegspunkt für einen frischen KI-Agenten. Lade nicht pauschal README, alle Skills oder das vollständige Handbuch in den Kontext.

## Problem-first Routing

Der Nutzer muss keine Skill-Namen, Domänen oder Workflows kennen. Ein Auftrag darf vollständig in Alltagssprache formuliert sein.

Beispiele:

- „Ich muss diese Datenbanktabelle dokumentieren.“
- „Prüfe, ob diese Behauptung stimmt.“
- „Ich möchte ein Buch mit wiederkehrenden Figuren entwickeln.“
- „Hilf mir, meine Rücklagen und Geldanlage einzuordnen.“

Die Aufgabe des Routers ist es, aus dem **Problem** den kleinsten ausreichenden Werkzeug-Satz abzuleiten. Nicht möglichst viele Skills aktivieren und nicht vom Nutzer verlangen, den Katalog selbst zu durchsuchen.

```text
Problem / Ziel des Nutzers
→ lokale Wahrheit und verfügbare Evidence verstehen
→ Aufgabe fachlich einordnen
→ passenden Workflow prüfen
→ primären Skill-Satz wählen
→ Cross-Cutting-Kandidaten am passenden Checkpoint prüfen
→ Primärrouting bei Bedarf verfeinern statt Skills nur zu addieren
→ nur wirklich fehlende Informationen klären
→ ausführen
→ vor Completion/Output relevante Overlays erneut prüfen
→ verifizieren / reviewen / gaten
```

## Routing

1. **Nutzerauftrag lesen.** Problem, gewünschtes Ergebnis, Scope, Grenzen und explizite Autorisierung festhalten. Fehlende Skill-Namen sind kein fehlender Input.
2. **Lokale Wahrheit zuerst.** Projektregeln, lokale Sources of Truth, vorhandene Artefakte und Nutzerangaben schlagen allgemeine Repository-Regeln. Allgemeine Arbeitsweise ist zentral; konkrete Wahrheit bleibt lokal.
3. **Aufgabe einordnen.** Aus dem realen Problem geeignete Domäne(n) und vorhandene Workflows ableiten. Nutze `Dokumentation/Skill-Handbuch.md` als Master-Router und `workflow-index.yml` für vorhandene Workflows.
4. **Primären Skill-Satz wählen.** Nutze `skill-catalog.yml`; lade nur die fachlich tatsächlich benötigten `SKILL.md`-Dateien und deren zwingende Abhängigkeiten. `related` ist ein Routinghinweis, kein Ladebefehl.
5. **Cross-Cutting-Checkpoints anwenden.** Nutze `routing-overlays.yml` nicht als einmaligen Pass, sondern nur an den dort genannten Checkpoints. Prüfe jeweils ausschließlich die kanonische Description der Kandidaten, deren Checkpoint erreicht ist.
6. **Primary verfeinern statt aufblasen.** Wenn ein Overlay-Kandidat laut eigener Description der spezifischere Primärowner für den Auftrag ist, darf er einen vorläufig gewählten generischen Skill ersetzen. Beide bleiben nur aktiv, wenn jeder einen eigenen notwendigen Job besitzt.
7. **Nur notwendige Lücken klären.** Frage nach Informationen, die für eine belastbare Bearbeitung wirklich fehlen.
8. **Vor Ausführung prüfen.** `maturity`, `eval_coverage`, `capabilities` und `related` im Katalog sowie die Skill-Frontmatter beachten. Toolverfügbarkeit ist keine Autorisierung.
9. **Capability-Runtime wählen.** Wenn eine externe App, ein Account oder ein Dienst materiell helfen würde, zuerst native Capabilities und bereits verbundene Plugins/Apps prüfen. READ, WRITE und extern sichtbare ACTIONS getrennt behandeln.
10. **Pre-Execution-Security deduplizieren.** `skill-security-review` ist Owner für Admission eines externen oder mächtigen Skill-Bundles und umfasst dessen Berechtigungsrisiken. `tool-permission-review` zusätzlich nur laden, wenn das Berechtigungsdesign selbst einen eigenständigen Prüfauftrag bildet.
11. **Ausführen.** Fachliche Wahrheit nicht aus allgemeinen Regeln erfinden. Riskante oder externe Aktionen nur innerhalb der ausdrücklich vorhandenen Rechte/Gates.
12. **Vor Completion und Output erneut prüfen.** Späte Trigger dürfen nicht verloren gehen: `citation-audit` kann erst nach Entstehung einer weitgehend fertigen Synthese sinnvoll werden; `visual-answer` kann aufgrund der tatsächlich entstandenen Informationsdichte am `pre-output`-Checkpoint neu relevant werden.
13. **Verifizieren.** Ergebnis gegen Auftrag, lokale Sources of Truth, relevante Evals/Checks und Skill-Grenzen prüfen.
14. **Review/Gate.** Offene Annahmen, Blocker, nicht ausgeführte Prüfungen und notwendige menschliche Freigaben sichtbar machen.

## Kommunikation der Skill-Auswahl

Die interne Werkzeugauswahl soll dem Nutzer helfen, nicht zusätzliche Bedienlast erzeugen.

- Bei einfachen Aufträgen genügt eine knappe Begründung der gewählten Arbeitsweise.
- Bei größeren oder risikoreicheren Aufträgen den verwendeten Workflow beziehungsweise die wichtigsten Skills transparent nennen.
- Keine lange Skill-Liste als Selbstzweck ausgeben.
- Wenn kein Skill erforderlich ist, die Aufgabe direkt und innerhalb der allgemeinen Regeln bearbeiten.

## Minimaler Kontext

Typischer Startkontext:

- `AGENTS.md`;
- relevante lokale Projektregeln / Sources of Truth;
- `Dokumentation/Skill-Handbuch.md` nur zum Primärrouting;
- passende Einträge aus `skill-catalog.yml`;
- `routing-overlays.yml` als kleine globale Checkpoint-Liste;
- danach nur die tatsächlich ausgewählten Skills bzw. Workflows.

Nicht erforderlich: komplettes Repository, alle katalogisierten Skills, vollständige Nutzungsdokumentation oder alle Fachhandbücher.

## Repository-Validierung

Bei Änderungen am Repository den vorhandenen lokalen Validation Harness bevorzugen. Keine systemweit installierte Python-Runtime voraussetzen.

Unter Windows:

```powershell
.\Validate-KI-Regeln.ps1 -Quick
```

Für breitere Prüfungen je nach Scope `-Full` oder `-Release` verwenden. Details stehen in `Dokumentation/Local-Validation-Harness.md`.

Die vorhandenen Python-Validatoren bleiben kanonische Prüflogik hinter dem Harness. Wenn die vorgesehene Prüfung in der aktuellen Laufzeit nicht ausgeführt werden kann, den Status als `NOT RUN` beziehungsweise `UNVERIFIED` sichtbar machen statt einen Pass zu behaupten.

## Harte Grenzen

- Keine Maturity-Hochstufung aus Plausibilität oder wenigen Beispielen ableiten.
- Keine Evals als bestanden darstellen, die nicht ausgeführt wurden.
- Keine externen Quellen automatisch synchronisieren.
- Keine produktiven Writes, Deployments, Veröffentlichungen oder sonstigen Außenaktionen aus bloßer Tool-, Plugin- oder App-Verfügbarkeit ableiten.
- Eine vorhandene Plugin-/App-Verbindung erweitert Capability, nicht automatisch Autorisierung.
- Externe Skills nur entsprechend dokumentierter Provenance und Lizenzlage übernehmen oder weiterverteilen.
