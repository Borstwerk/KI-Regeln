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
→ kleinsten ausreichenden Skill-Satz wählen
→ nur wirklich fehlende Informationen klären
→ ausführen
→ verifizieren / reviewen / gaten
```

## Routing

1. **Nutzerauftrag lesen.** Problem, gewünschtes Ergebnis, Scope, Grenzen und explizite Autorisierung festhalten. Fehlende Skill-Namen sind kein fehlender Input.
2. **Lokale Wahrheit zuerst.** Projektregeln, lokale Sources of Truth, vorhandene Artefakte und Nutzerangaben schlagen allgemeine Repository-Regeln. Allgemeine Arbeitsweise ist zentral; konkrete Wahrheit bleibt lokal.
3. **Aufgabe einordnen.** Aus dem realen Problem geeignete Domäne(n) und vorhandene Workflows ableiten. Nutze `Dokumentation/Skill-Handbuch.md` als Master-Router und `workflow-index.yml` für vorhandene Workflows.
4. **Kleinsten ausreichenden Skill-Satz wählen.** Nutze `skill-catalog.yml`; lade nur die tatsächlich benötigten `SKILL.md`-Dateien und deren zwingende Abhängigkeiten. `related` ist ein Routinghinweis, kein Ladebefehl.
5. **Nur notwendige Lücken klären.** Frage nach Informationen, die für eine belastbare Bearbeitung wirklich fehlen. Keine vollständige Projekterhebung oder unnötige sensible Datensammlung nur deshalb durchführen, weil ein Skill sie theoretisch verwenden könnte.
6. **Vor Ausführung prüfen.** `maturity`, `eval_coverage`, `capabilities` und `related` im Katalog sowie die Skill-Frontmatter beachten. Toolverfügbarkeit ist keine Autorisierung. Ein Eval-Pfad oder definierte Fälle bedeuten nicht, dass Evals bestanden wurden.
7. **Ausführen.** Fachliche Wahrheit nicht aus allgemeinen Regeln erfinden. Riskante oder externe Aktionen nur innerhalb der ausdrücklich vorhandenen Rechte/Gates.
8. **Verifizieren.** Ergebnis gegen Auftrag, lokale Sources of Truth, relevante Evals/Checks und Skill-Grenzen prüfen.
9. **Review/Gate.** Offene Annahmen, Blocker, nicht ausgeführte Prüfungen und notwendige menschliche Freigaben sichtbar machen.

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
- `Dokumentation/Skill-Handbuch.md` nur zum Routing;
- passende Einträge aus `skill-catalog.yml`;
- danach nur die ausgewählten Skills bzw. Workflows.

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
- Keine produktiven Writes, Deployments, Veröffentlichungen oder sonstigen Außenaktionen aus bloßer Toolverfügbarkeit ableiten.
- Externe Skills nur entsprechend dokumentierter Provenance und Lizenzlage übernehmen oder weiterverteilen.
