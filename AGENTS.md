# KI-Regeln – Agent Bootstrap

Diese Datei ist der kleinste Einstiegspunkt für einen frischen KI-Agenten. Lade nicht pauschal README, alle Skills oder das vollständige Handbuch in den Kontext.

## Routing

1. **Nutzerauftrag lesen.** Scope, gewünschtes Ergebnis, Grenzen und explizite Autorisierung festhalten.
2. **Lokale Wahrheit zuerst.** Projektregeln, lokale Sources of Truth, vorhandene Artefakte und Nutzerangaben schlagen allgemeine Repository-Regeln. Allgemeine Arbeitsweise ist zentral; konkrete Wahrheit bleibt lokal.
3. **Domäne oder Workflow wählen.** Nutze `Dokumentation/Skill-Handbuch.md` als Master-Router und `workflow-index.yml` für vorhandene Workflows.
4. **Kleinsten ausreichenden Skill-Satz wählen.** Nutze `skill-catalog.yml`; lade nur die tatsächlich benötigten `SKILL.md`-Dateien und deren zwingende Abhängigkeiten.
5. **Vor Ausführung prüfen.** `maturity`, `eval_coverage`, `capabilities` und `related` im Katalog sowie die Skill-Frontmatter beachten. Toolverfügbarkeit ist keine Autorisierung. Ein Eval-Pfad oder definierte Fälle bedeuten nicht, dass Evals bestanden wurden.
6. **Ausführen.** Fachliche Wahrheit nicht aus allgemeinen Regeln erfinden. Riskante oder externe Aktionen nur innerhalb der ausdrücklich vorhandenen Rechte/Gates.
7. **Verifizieren.** Ergebnis gegen Auftrag, lokale Sources of Truth, relevante Evals/Checks und Skill-Grenzen prüfen.
8. **Review/Gate.** Offene Annahmen, Blocker, nicht ausgeführte Prüfungen und notwendige menschliche Freigaben sichtbar machen.

## Minimaler Kontext

Typischer Startkontext:

- `AGENTS.md`;
- relevante lokale Projektregeln / Sources of Truth;
- `Dokumentation/Skill-Handbuch.md` nur zum Routing;
- passende Einträge aus `skill-catalog.yml`;
- danach nur die ausgewählten Skills bzw. Workflows.

Nicht erforderlich: komplettes Repository, alle 128 katalogisierten Skills, vollständige Nutzungsdokumentation oder alle Fachhandbücher.

## Harte Grenzen

- Keine Maturity-Hochstufung aus Plausibilität oder wenigen Beispielen ableiten.
- Keine Evals als bestanden darstellen, die nicht ausgeführt wurden.
- Keine externen Quellen automatisch synchronisieren.
- Keine produktiven Writes, Deployments, Veröffentlichungen oder sonstigen Außenaktionen aus bloßer Toolverfügbarkeit ableiten.
- Externe Skills nur entsprechend dokumentierter Provenance und Lizenzlage übernehmen oder weiterverteilen.
