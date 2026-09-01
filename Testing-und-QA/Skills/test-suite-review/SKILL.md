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
9. **Guardrail-Drift**
   - wurden Assertions, Tests oder relevante Pfade entfernt beziehungsweise abgeschwächt?
   - wurden Tests geskippt, quarantäniert oder durch Filter aus dem tragenden Lauf entfernt?
   - wurden Coverage-, Quality-, Security- oder andere Schwellen gesenkt?
   - wurde ein blocking Signal zu informational umklassifiziert?
   - wurden Ausnahmen ergänzt, die eine bekannte Regression nur unsichtbar machen?
10. **Release-Evidence**
   - was kann die Suite tatsächlich belegen?
   - welche Unsicherheit bleibt?
   - ist der aktuelle Qualitätsmaßstab mit der referenzierten Baseline noch vergleichbar?

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

Wenn der Qualitätsmaßstab selbst verändert wurde, diese Änderung separat vom Produktfix ausweisen. Ein neuer grüner Lauf ist nicht automatisch mit einer früheren Baseline vergleichbar, wenn Tests, Filter, Assertions oder Schwellen verändert wurden.

## Regeln

- Review ≠ Rewrite;
- grüne Suite nicht automatisch als gute Suite bewerten;
- Coverage-Prozent nicht als alleinige Qualitätsmetrik verwenden;
- vorhandene starke Tests schützen;
- keine Tests lockern, nur um Laufzeit oder Grünstatus zu verbessern;
- begründete Guard-Änderung ≠ verbotene Guard-Änderung, aber sie benötigt eigene Evidence und darf nicht als unsichtbarer Teil eines Produktfixes durchrutschen;
- Releaseentscheidung nicht selbst erteilen.

## Related

- `test-strategy`
- `flaky-test-diagnosis`
- `code-review`
- `verification-loop`
