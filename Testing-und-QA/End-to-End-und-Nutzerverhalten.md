# End-to-End und Nutzerverhalten

## Grundsatz

> End-to-End-Tests prüfen wichtige Gesamtflüsse dort, wo kleinere Tests das relevante Risiko nicht zuverlässig abdecken können.

## Auswahl

E2E-Tests bevorzugt für:

- geschäftskritische Nutzerflüsse;
- Systemgrenzen, deren Zusammenspiel zentral ist;
- wichtige Berechtigungs-/Rollenpfade;
- ausgewählte Fehlerklassen;
- Risiken, die nur im Gesamtsystem sichtbar werden.

Nicht jeden Detailfall als E2E abbilden.

## Nutzerbeobachtbares Verhalten

Bei UI-Flows möglichst über sichtbare oder anderweitig zugesicherte Interaktionen und Ergebnisse prüfen:

- Rolle / Accessible Name;
- sichtbarer Text;
- URL / Navigation;
- fachliches Ergebnis;
- persistierter Zustand, wenn relevant.

Private Komponentenstruktur, CSS-Klassen oder interne Methoden nur prüfen, wenn sie selbst Teil des Vertrags sind.

## Testdaten und Umgebung

- Testzustand reproduzierbar herstellen;
- Testdaten möglichst ephemer halten;
- echte Produktionsdaten vermeiden;
- Abhängigkeiten und Versionen dokumentieren;
- keine Seiteneffekte auf reale Kundensysteme erzeugen.

## Warten auf Zustände

Bevorzugt auf beobachtbare Zustände warten statt feste Schlafzeiten einzubauen.

```text
schlecht:
warte 5 Sekunden

besser:
warte bis der erwartete fachliche oder UI-Zustand erreicht ist
```

Framework-native Auto-Waiting-/Retry-Mechanismen nutzen, wenn sie zur Semantik des Tests passen.

## Debug-Evidence

Bei komplexen E2E-Tests geeignete Diagnoseartefakte vorsehen:

- Logs;
- Trace;
- Screenshots;
- Netzwerkfehler;
- relevante Testdaten-IDs;
- reproduzierbare Seeds/Zeitpunkte.

## Grenze zur visuellen Verifikation

Ein E2E-Test kann beweisen, dass ein Flow fachlich funktioniert, ohne zu beweisen, dass das UI visuell korrekt ist.

Für Layout, Responsiveness, Fokus, visuelle Zustände und Designabweichungen zusätzlich `Webentwicklung/Skills/visual-verification` verwenden.