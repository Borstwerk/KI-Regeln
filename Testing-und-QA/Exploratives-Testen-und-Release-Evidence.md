# Exploratives Testen und Release-Evidence

## Grundsatz

> Nicht jede wertvolle Prüfung muss vorab vollständig geskriptet sein. Aber auch exploratives Testen braucht Mission, Scope und nachvollziehbare Beobachtungen.

## Exploratives Testen

Geeignet insbesondere für:

- neue oder stark veränderte Nutzerflows;
- komplexe Interaktionen;
- unklare Failure Modes;
- Bereiche mit schwacher bestehender Spezifikation;
- ergänzende Prüfung nach automatisierten Tests;
- gezielte Untersuchung auffälliger Risiken.

## Test Charter

Vor einer Session möglichst festlegen:

```text
Mission
Scope
Risiken / Fragestellungen
relevante Personas / Daten
Heuristiken
Zeitbox
Umgebung
```

Danach dokumentieren:

- untersuchte Pfade;
- Beobachtungen;
- Defekte;
- überraschende Zustände;
- offene Fragen;
- neue Testideen;
- relevante Evidence.

Exploratives Testen ist nicht gleichbedeutend mit zufälligem Herumklicken.

## Release-Evidence

Testing kann für ein lokales Release-/Freigabe-Gate eine kompakte Qualitätsaussage liefern.

Mögliche Bestandteile:

- getesteter Scope / Build / Commit;
- relevante Risiken und deren Teststatus;
- ausgeführte Testebenen;
- aktuelle Ergebnisse;
- bekannte flaky/quarantined Tests;
- offene Defekte;
- nicht ausgeführte oder blockierte Prüfungen;
- Restunsicherheit;
- manuelle/explorative Findings;
- Abweichungen vom geplanten Testscope.

## Keine automatische Releaseentscheidung

Ein Testreport darf nicht aus sich selbst heraus behaupten:

> Release freigegeben.

außer das lokale Projekt hat diesem Prüfprozess ausdrücklich diese Entscheidungsbefugnis gegeben.

Normalfall:

```text
Testing
→ liefert Evidence + Restunsicherheit

lokales Projekt-/Human-Gate
→ trifft Releaseentscheidung
```

## Statussprache

Bevorzugt präzise Aussagen:

- `PASS` – definierter Nachweis aktuell bestanden;
- `FAIL` – definierter Nachweis aktuell nicht bestanden;
- `BLOCKED` – notwendiger Nachweis nicht ausführbar;
- `NOT RUN` – vorgesehen, aber nicht ausgeführt;
- `RISK ACCEPTANCE REQUIRED` – bekanntes Restrisiko benötigt lokale Entscheidung.

Nicht `PASS` schreiben, wenn der Nachweis nicht frisch ausgeführt wurde.