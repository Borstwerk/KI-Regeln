---
name: flaky-test-diagnosis
description: Diagnostiziert Tests, die bei unverändertem Code inkonsistent bestehen oder scheitern. Verwenden bei intermittierenden CI-Fehlern, Race Conditions, Reihenfolge-, Timing-, Parallelitäts- oder Umgebungsproblemen. Nicht einfach nur Retries erhöhen.
---

# Flaky Test Diagnosis

## Ziel

Die Ursache eines unzuverlässigen Testsignals reproduzierbar eingrenzen und beheben.

## Arbeitsweise

1. Flakiness mit wiederholbaren Läufen bestätigen; genaue Erfolgs-/Fehlerrate dokumentieren, wenn sinnvoll.
2. Failures nach Test, SUT, Framework, Dependency oder Infrastruktur klassifizieren.
3. Variablen sammeln:
   - Reihenfolge;
   - Parallelität;
   - Testdaten;
   - Zeit / Clock;
   - Random Seed;
   - Ressourcenlast;
   - Netzwerk / externe Services;
   - Browser / OS / Runtime.
4. Eine Hypothese nach der anderen kontrollieren.
5. Feste Sleeps und versteckten globalen Zustand besonders prüfen.
6. Root Cause korrigieren statt Retry-Zahl als Endlösung zu erhöhen.
7. Unter ursprünglichen problematischen Bedingungen erneut testen.
8. Quarantäne nur als sichtbare Übergangsmaßnahme verwenden.

## Evidence

```text
reproduzierter Flake
Variablen / Bedingungen
Hypothesen
isolierte Ursache
Fix
Wiederholung nach Fix
verbleibende Unsicherheit
```

## Regeln

- „CI ist manchmal komisch“ ist keine Diagnose;
- Retry-Pass nicht als vollständig gesunden Test melden;
- Test nicht einfach deaktivieren, wenn damit ein relevantes Risiko unbewacht bleibt;
- Produktdefekt und Testdefekt sauber unterscheiden.

## Related

- `diagnose`
- `test-suite-review`
- `verification-loop`