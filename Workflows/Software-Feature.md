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

`verification-loop`

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
