# Skill: Frontend Performance

## Zweck

Untersuche und verbessere Frontend-Performance anhand realer Messungen und priorisierter Engpässe.

## Verwenden wenn

- Ladezeit oder Interaktion langsam ist;
- Bundlegröße auffällig ist;
- neue schwere UI-Funktionen eingeführt wurden;
- Performance vor Release geprüft werden soll.

## Eingaben

- betroffene Route oder Flow;
- Messwerte/Profiling, sofern vorhanden;
- Bundle-/Netzwerkdaten;
- lokale Performanceziele;
- relevante Geräte-/Browserprofile.

## Arbeitsweise

1. Reproduziere das Performanceproblem.
2. Messe unter dokumentierten Bedingungen.
3. Priorisiere zuerst Hochwirkungsthemen:
   - Netzwerk-Waterfalls;
   - unnötiges Client-JavaScript;
   - große Bundles;
   - langsame Serverantworten;
   - große Medien;
   - teure Renderingpfade.
4. Formuliere eine konkrete Ursache oder Hypothese.
5. Ändere den kleinsten sinnvollen Bereich.
6. Messe erneut unter vergleichbaren Bedingungen.
7. Prüfe auf funktionale oder visuelle Regressionen.
8. Mechanisiere wiederkehrende Budgets, wenn sinnvoll.

## Regeln

- Nicht vor Messung mikrotunen.
- Memoisierung ist kein Standardheilmittel.
- Neue Abhängigkeiten gegen Bundle- und Architekturkosten prüfen.
- Unabhängige Requests nicht unnötig sequenziell laden.
- Client-JavaScript nur dort einsetzen, wo Browserinteraktion es rechtfertigt.
- Vorher/Nachher-Werte müssen ausreichend vergleichbar sein.

## Ausgabe

```text
Ausgangsmessung
Engpass / Ursache
Änderung
Nachmessung
Auswirkung
Regressionchecks
verbleibende Risiken
```

## Stop-Regeln

Stoppe, wenn:

- keine reproduzierbare Messung möglich ist;
- eine breite Architekturänderung nötig wäre;
- lokale Performanceziele fehlen und dadurch keine Priorisierung möglich ist;
- der vermutete Gewinn nur spekulativ ist.

## Leitgedanke

> Performance optimiert man dort, wo echte Arbeit und echte Wartezeit entstehen – nicht dort, wo der Code besonders clever aussehen könnte.