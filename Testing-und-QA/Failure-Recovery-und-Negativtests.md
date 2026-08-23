# Failure, Recovery und Negativtests

## Grundsatz

> Ein System ist nicht ausreichend getestet, wenn nur erfolgreiche Eingaben und verfügbare Abhängigkeiten geprüft wurden.

## Typische Failure Cases

Je nach System und Risiko:

- ungültige oder unvollständige Eingaben;
- Timeout;
- Dependency nicht erreichbar;
- fehlerhafte oder unerwartete Dependency-Antwort;
- Rate Limit / Backpressure;
- Teilfehler;
- Retry;
- doppelte Zustellung / Wiederholung;
- Idempotenz;
- Berechtigungsfehler;
- Disk-/Quota-/Ressourcenfehler;
- Abbruch zwischen mehreren Schritten;
- Rollback oder kompensierende Aktion.

## Recovery prüfen

Nicht nur erwarten, dass ein Fehler angezeigt wird.

Wenn relevant prüfen:

- bleibt der Zustand konsistent?
- kann sicher wiederholt werden?
- entstehen Duplikate?
- bleibt ein halbfertiger Zustand zurück?
- wird ein Retry begrenzt?
- funktioniert Rollback / Compensation?
- kann ein Nutzer oder Operator sinnvoll fortfahren?

## Fault Injection im Testscope

Kontrollierte Fehler können über Test Doubles, Netzwerkinterception, Clock-/Resource-Control oder geeignete Testumgebungen erzeugt werden.

Die injizierte Störung soll:

- klar definiert sein;
- zum getesteten Failure Mode passen;
- reproduzierbar sein;
- keine unerlaubten realen Schäden erzeugen.

## Grenze zu Chaos Engineering

Dieser Bereich behandelt gezielte, reproduzierbare Failure Cases innerhalb eines Testscopes.

Chaos Engineering beginnt dort, wo systemische Hypothesen über das Verhalten komplexer oder verteilter Systeme unter realistischen Störungen experimentell geprüft werden, insbesondere mit Steady-State-Metriken, kontrollierter Blast Radius und gegebenenfalls produktionsnahen oder produktiven Experimenten.

Das gehört in einen späteren Bereich `Reliability/`.

## Security-Grenze

Allgemeine Berechtigungs- und Fehlerfälle dürfen hier liegen.

Tiefgehende offensive Security-Tests, Exploitmethoden und Security-Testprogramme gehören in `Sicherheit/` und die dort gültigen Regeln.

## Leitgedanke

> Fehlerpfade sind Produktverhalten. Deshalb brauchen auch sie explizite Erwartungen und Evidence.