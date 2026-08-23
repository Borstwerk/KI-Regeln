# Testdaten, Isolation und Hermetik

## Grundsatz

> Ein Test soll seinen relevanten Ausgangszustand kontrollieren und unabhängig reproduzierbar sein.

## Isolation

Tests sollen möglichst nicht heimlich abhängen von:

- Reihenfolge anderer Tests;
- gemeinsam veränderlichem globalem Zustand;
- vorher erzeugten Daten;
- persistenten Sessions;
- Uhrzeit oder Zeitzone ohne Kontrolle;
- zufälligen Seeds ohne Reproduzierbarkeit;
- fremden CI-Jobs;
- dauerhaft gemeinsam genutzten Testumgebungen.

## Testdaten

Testdaten sollen:

- minimal für das Testziel sein;
- relevante Edge Cases sichtbar machen;
- deterministisch erzeugbar sein;
- keine unnötigen echten personenbezogenen oder produktiven Daten enthalten;
- nach dem Test isoliert entfernt oder durch kurzlebige Umgebung verworfen werden können.

Factories, Builder oder Fixtures dürfen Lesbarkeit und Konsistenz verbessern, dürfen aber wichtige fachliche Werte nicht so stark verstecken, dass der Test unverständlich wird.

## Hermetik

Ein vollständig hermetischer Test kontrolliert alle für sein Ergebnis relevanten Abhängigkeiten.

Hermetik ist wertvoll für Reproduzierbarkeit, aber kein Selbstzweck.

Wenn reales Verhalten einer Dependency Teil des Testziels ist, kann ein isolierter echter Service die bessere Form der kontrollierten Umgebung sein.

## Zeit und Zufall

Bei zeit- oder zufallsabhängigem Verhalten möglichst:

- Clock/RNG kontrollierbar machen;
- Zeitzonen explizit testen;
- Seed bei Fehlern dokumentieren;
- nicht auf reale Wartezeiten setzen, wenn ein beobachtbarer Zustand oder eine kontrollierte Zeitquelle existiert.

## Parallelisierung

Tests, die parallel laufen können, dürfen nicht dieselben veränderlichen Ressourcen ohne Isolation teilen.

Geeignete Strategien:

- eindeutige Test-IDs / Namespaces;
- eigene Datenbanken/Schemas;
- transaktionale Isolation, sofern fachlich korrekt;
- kurzlebige Container;
- separate Accounts oder Tenants.

## Cleanup

Cleanup muss auch bei fehlgeschlagenen Tests funktionieren.

Bevorzugt kurzlebige Ressourcen, deren gesamter Lebenszyklus an den Testlauf gebunden ist, statt komplexer nachträglicher Bereinigung gemeinsam genutzter Zustände.

## Flakiness-Signal

Ein Test, der nur bei bestimmter Reihenfolge oder nach mehrfacher Wiederholung besteht, gilt nicht als zuverlässig isoliert.