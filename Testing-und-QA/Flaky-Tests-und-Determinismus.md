# Flaky Tests und Determinismus

## Grundsatz

> Ein Test, der bei unverändertem Code unterschiedliche Ergebnisse liefert, ist selbst ein Qualitätsproblem.

## Retry ist kein Fix

Retries können helfen:

- Flakiness sichtbar zu machen;
- Diagnoseartefakte zu sammeln;
- kurzfristig CI-Ausfälle zu klassifizieren.

Sie reparieren aber nicht die Ursache.

Ein Test, der erst nach Retry besteht, soll nicht still als vollständig gesund gelten.

## Typische Ursachen

### Zustand

- globaler mutable State;
- gemeinsam genutzte Testdaten;
- fehlendes Cleanup;
- Reihenfolgenabhängigkeit.

### Timing

- feste Sleeps;
- Race Conditions;
- asynchrone Operationen ohne beobachtbare Synchronisation;
- echte Uhrzeit ohne Kontrolle.

### Parallelität

- gemeinsam genutzte Ports, Dateien, Accounts oder Datenbanken;
- nicht threadsichere Testfixtures;
- Ressourcenknappheit.

### Umgebung

- Netzwerk;
- externe Services;
- CPU-/Speicherdruck;
- Versionsdrift;
- Browser-/OS-Unterschiede.

### Test selbst

- zu breite Assertions;
- fragile Selektoren;
- nicht deterministische Daten;
- falsche Annahmen über Reihenfolge oder Eventual Consistency.

## Diagnoseprozess

```text
Flake bestätigen
→ reproduzierbare Variablen sammeln
→ Test / SUT / Framework / Infrastruktur trennen
→ Hypothese
→ Variable kontrollieren
→ wiederholen
→ Ursache beheben
→ erneut unter ursprünglichen Bedingungen prüfen
```

## Quarantäne

Quarantäne kann kurzfristig sinnvoll sein, wenn ein Flake die gesamte Pipeline blockiert.

Aber:

- sichtbar markieren;
- Owner festlegen;
- keine dauerhafte Unsichtbarkeit;
- fachlich kritische Tests nicht einfach aus dem Release-Gate entfernen, ohne das Risiko explizit zu behandeln.

## Signalvertrauen

Eine Testsuite mit vielen ignorierten oder häufig flaky Tests verliert ihren Wert als Entscheidungsinstrument.

Flakiness deshalb nicht nur als lästige CI-Kosten behandeln, sondern als Defekt am Qualitätssignal.