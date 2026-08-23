---
name: test-suite-review
description: Prüft eine bestehende Testsuite unabhängig auf Risikoabdeckung, Testebenen, Isolation, Flakiness, Test-Doubles, Wartbarkeit, Laufzeit und Aussagekraft. Verwenden für Qualitätsaudit oder vor größeren Testumbauten. Nicht ungefragt die Suite komplett neu schreiben.
---

# Test Suite Review

## Ziel

Die Qualität des Testsignals und die Eignung des Testportfolios unabhängig bewerten.

## Prüfachsen

1. **Risikoabdeckung**
   - kritische Pfade / Invarianten;
   - relevante Fehlerfälle;
   - bekannte Regressionen.
2. **Testportfolio**
   - passende Ebenen;
   - unnötige Doppelung;
   - fehlende Integrations-/Contract-/E2E-Evidence.
3. **Testdesign**
   - belastbare Oracles;
   - Verhalten vs. Implementierungsdetails;
   - Grenzen / Zustände / Negativfälle.
4. **Isolation**
   - Daten;
   - Reihenfolge;
   - Parallelität;
   - Zeit / Randomness;
   - Cleanup.
5. **Dependencies / Doubles**
   - Mock-Drift;
   - fehlendes reales Integrationsverhalten;
   - unnötig teure reale Dependencies.
6. **Flakiness und Diagnosefähigkeit**
7. **Laufzeit / CI-Fit**
8. **Coverage-/Mutation-Signale**, sofern vorhanden.
9. **Release-Evidence**
   - was kann die Suite tatsächlich belegen?
   - welche Unsicherheit bleibt?

## Ausgabe

Findings nach Schwere priorisieren:

- `BLOCKER` – Testsignal erlaubt keine belastbare Aussage für ein kritisches Risiko;
- `HIGH` – wesentliche Lücke / Flakiness / falsche Testebene;
- `MEDIUM` – relevante Wartbarkeits- oder Coverage-Lücke;
- `LOW` – lokale Verbesserung.

Je Finding:

```text
Problem
Risiko
Evidence
empfohlene kleinste Änderung
```

## Regeln

- Review ≠ Rewrite;
- grüne Suite nicht automatisch als gute Suite bewerten;
- Coverage-Prozent nicht als alleinige Qualitätsmetrik verwenden;
- vorhandene starke Tests schützen;
- keine Tests lockern, nur um Laufzeit oder Grünstatus zu verbessern;
- Releaseentscheidung nicht selbst erteilen.

## Related

- `test-strategy`
- `flaky-test-diagnosis`
- `code-review`
- `verification-loop`