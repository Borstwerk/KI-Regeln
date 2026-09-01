---
name: ci-pipeline-design
description: Entwirft oder prüft CI/CD-Pipelines hinsichtlich Triggern, Jobs, Abhängigkeiten, Parallelität, Caching, Artefakten, Credentials, Environment-Grenzen und Gates. Verwenden bei GitHub Actions, GitLab CI, Azure DevOps, Jenkins oder ähnlichen Pipelines. Nicht zur Festlegung der eigentlichen Teststrategie verwenden.
---

# CI Pipeline Design

## Ziel

Automationspipelines so strukturieren, dass Evidence reproduzierbar, nachvollziehbar und mit minimal nötigen Rechten erzeugt und weitergegeben wird.

## Eingaben

- Pipelineziel;
- lokale Test-/Security-/Releaseanforderungen;
- Tool/Runner/Environment;
- Jobs und Abhängigkeiten;
- Artefakt- und Credentialmodell.

## Arbeitsweise

1. Trigger und Trust Boundary bestimmen.
2. Jobs nach echten Abhängigkeiten ordnen; unabhängige Arbeit parallelisieren.
3. Inputs/Outputs und Artefaktübergaben definieren.
4. Caches nur als Optimierung einbauen und korrekt invalidieren.
5. Teststrategie aus `Testing-und-QA/` übernehmen statt neu erfinden.
6. Credentials pro Job/Environment minimal schneiden.
7. blocking vs. informational Checks explizit machen.
8. Build-/Promotion-/Deploy-Gates trennen.
9. Failure Evidence und Reproduzierbarkeit planen.
10. Änderungen an Checks, Gate-Severity, Filtern oder Schwellenwerten als eigene Pipelineänderung sichtbar machen, wenn sie die Aussagekraft des Qualitätsnachweises verändern.

## Quality Floors und Gate-Integrität

Checks und Gates sind Teil des lokalen Qualitätsvertrags einer Pipeline, nicht bloß austauschbare Implementierungsdetails.

Ein Agent darf einen Produktfehler nicht dadurch „beheben“, dass er ohne separate Begründung beispielsweise:

- einen failing Test aus dem relevanten Job entfernt oder skippt;
- einen blocking Check auf informational setzt;
- Coverage-, Security-, Lint- oder andere Quality-Schwellen senkt;
- relevante Pfad-/Branch-/Testfilter so verengt, dass der Fehler nicht mehr geprüft wird;
- eine Ausnahme ergänzt, die nur den aktuellen Verstoß unsichtbar macht.

Eine solche Änderung kann lokal sinnvoll sein, wenn der bisherige Guard falsch oder überholt ist. Dann gilt sie aber als **Änderung des Qualitätsmaßstabs** und benötigt eigene Evidence sowie die lokal erforderliche Entscheidung beziehungsweise Freigabe.

Ein grüner Lauf nach geändertem Quality Floor ist nicht automatisch mit einem früheren grünen Lauf unter dem alten Maßstab gleichwertig.

## Nicht tun

- universelle Unit→Integration→E2E-Reihenfolge erzwingen;
- Retry verwenden, um Flakiness unsichtbar zu machen;
- Fork-/PR-Code mit mächtigen Secrets ausführen;
- Pipeline-Grün als automatische Merge-/Deploy-Freigabe behandeln;
- Quality Gates still abschwächen, nur damit eine Änderung grün wird.

## Ausgabe

```text
Triggers
Jobs / DAG
Artifacts / Cache
Credentials
Checks / Gates
Quality-Floor-Änderungen, falls vorhanden
Environment Boundaries
Failure Evidence
Open Risks
```

## Related

- `test-strategy`
- `verification-loop`
- `container-build`
- `deployment-strategy`
- `tool-permission-review`
