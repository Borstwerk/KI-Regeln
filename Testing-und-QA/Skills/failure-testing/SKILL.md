---
name: failure-testing
description: Plant oder prüft kontrollierte Tests für Fehler-, Negativ- und Recovery-Pfade wie Timeouts, Teilfehler, Retries, Idempotenz oder Dependency-Ausfälle. Verwenden für reproduzierbare Failure Modes innerhalb eines Testscopes. Nicht für systemische Chaos-Experimente verwenden.
---

# Failure Testing

## Ziel

Erwartbare Fehlerzustände und Recovery-Verhalten gezielt und reproduzierbar verifizieren.

## Arbeitsweise

1. Relevanten Failure Mode und erwartetes Verhalten definieren.
2. Störung mit kleinstem sicheren Mechanismus erzeugen:
   - Stub/Fake;
   - Netzwerkinterception;
   - kontrollierte Dependency;
   - Clock/Resource-Control;
   - geeignete Testumgebung.
3. Prüfen:
   - sichtbares Fehlerverhalten;
   - Daten-/Zustandskonsistenz;
   - Retry-Grenzen;
   - Idempotenz / Duplikate;
   - Rollback / Compensation;
   - Wiederanlauf / Fortsetzung.
4. Sicherstellen, dass die Störung keine unerlaubten realen Schäden verursacht.
5. Nachweis und verbleibendes Risiko dokumentieren.

## Grenze

Nicht als Chaos Engineering ausführen.

Wenn Ziel eine systemische Steady-State-Hypothese unter realistischen Störungen, kontrolliertem Blast Radius, Observation, Abort und Recovery ist, an `resilience-experiment` aus `Reliability-und-System-Observability/` übergeben.

## Regeln

- Happy-Path-Assertions nicht als Recovery-Evidence verkaufen;
- Failure Mode nicht durch beliebige andere Störung ersetzen;
- produktive Störungen benötigen explizite lokale Autorisierung;
- Security-Exploitmethoden nicht aus diesem Skill ableiten.

## Related

- `integration-testing`
- `transaction-review`
- `resilience-experiment`