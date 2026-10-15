# Workflow – Software Feature

## Ziel

Ein Feature kontrolliert von Anforderung und Domänenverständnis bis zu verifizierter Änderung führen.

## Empfohlene Skill-Kette

```text
Anforderung / Projektwahrheit
→ optional domain-modeling
→ Planung / task-graph bei Komplexität
→ delegation-contract bei Delegation
→ tdd oder passende Implementierungsdisziplin
→ verification-loop
→ code-review
→ Human Gate für Commit/Push/Release gemäß Projektprozess
```

## 1. Anforderung

Vor Code klären:

- Was soll sich fachlich ändern?
- Was bleibt ausdrücklich unverändert?
- Welche Akzeptanzkriterien gelten?
- Welche Architektur-/Projektregeln sind bindend?

## 2. Domäne optional

`domain-modeling`, wenn Begriffe, Grenzen oder Fachmodell selbst unklar sind.

Nicht für jede kleine Änderung erzwingen.

## 3. Planung

Bei größeren Features `task-graph` nutzen.

Abhängigkeiten vor Parallelisierung klären.

## 4. Delegation optional

`delegation-contract` für eigenständige Agentenarbeit:

- Ziel;
- Scope;
- Rechte;
- Acceptance;
- Evidence;
- Stop-Gates.

## 5. Implementierung

`tdd`, wenn testgetriebener Slice sinnvoll ist.

Keine spekulativen Erweiterungen außerhalb des freigegebenen Scopes.

## 6. Verifikation

Vor der Ausführung **Verification Discovery** gemäß `../Testing-und-QA/Umgebungsabhaengige-Verifikation-und-Reports.md`: Projektvorgaben, betroffene Technologien, Betriebssystem/Runtime, vorhandene Testbefehle, Risiken und Berechtigungen tatsächlich prüfen. Die passende native Testumgebung wählen; kein pauschaler Python- oder CI-Zwang.

`verification-loop` führt die relevanten Checks frisch aus und trennt PASS, FAIL, BLOCKED, NOT_RUN und UNVERIFIED. Eine nicht vorhandene Runtime ist keine bestandene Prüfung. Ergebnisse möglichst mit Quellzustand und Evidence binden; der optionale Austauschvertrag liegt unter `../Schemas/verification-run.schema.json`.

Tests, Build, statische Checks und fachliche Akzeptanz soweit passend.

## 7. Unabhängiger Review

`code-review`

Mindestens zwei Achsen:

- entspricht die Änderung der Anforderung?
- entspricht sie den Repository-/Qualitätsregeln?

## Security

Neue mächtige Tools, externe Integrationen, Secrets, Netzwerk- oder Produktionsrechte zusätzlich sicherheitsprüfen.

## Release Gate

Ein grüner Implementierungsloop bedeutet nicht automatisch Freigabe für:

- Commit;
- Push;
- Merge;
- Release;
- Deploy.

Lokale Projektgates entscheiden.
