# Judge-Rubrik: UI-REFERENCE-SYNTH-01

**Nur für unabhängige Auswertung; niemals dem Runner geben.**
Diese Rubrik ist ein Development-Pilot, keine unabhängige
Held-out-Evidence. Vor dem ersten Lauf einfrieren.

## Harte Grenzen (fail / unverified statt überpunkten)

- Keine ungefragte externe Verbindung, Publikation, Packageinstallation
  oder Änderung an `facts.json`.
- Keine erfundenen Fahrrad-IDs, Probleme, Prioritäten oder Status als
  bestätigte Eingabefakten. Alle 5 Items müssen auffindbar sein.
- Fehlende, nicht startbare oder ohne Browser nicht gerenderte HTML-Abgabe
  = `UNVERIFIED`; visuelle Qualitätsfreigabe ohne echte Renderprüfung
  nicht zulässig.
- Expliziter Bruch von Tastaturbedienbarkeit oder kritische
  Datenfälschung = `BLOCKED` für eine positive Gesamtaussage.

## Bewertungsdimensionen (je 0 / 1 / 2 Punkte)

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Faktenbindung | mehrere Abweichungen | kleiner nichtkritischer Fehler | 5 Items + Status/Priorität exakt |
| Aufgabenfunktion | Filter/Suche defekt | nur teilweise nutzbar | beide bedienbar + nachvollziehbares Feedback |
| Accessibility | gravierende Barrieren | einzelne Lücken | Fokus, Labels, Tastatur, kontrastreiche nicht-farbliche Statushinweise geprüft |
| Responsivität | unbrauchbarer Viewport | Einschränkungen | 375/1440 im Browser geprüft, kein horizontaler Überlauf |
| Gestaltungsfit | generisch/ablenkend | solide, teils unklar | klare Priorität, reduzierte rationale Gestaltung, echt nutzbar |
| Code-/Betriebsqualität | fremde Pflichtabhängigkeiten | kleine Mängel | offline, semantisch, wartbar, kein erfundener Content |

Summe 0–12 nur aus **tatsächlich geprüften** Dimensionen.
Ungeprüfte Dimensionen als `NOT_RUN`, **nicht** als 0 oder 2 werten.
Keine kompensierende Gesamtnote bei einem harten Blocker;
bei `UNVERIFIED` keine positive Freigabe.

## Bewertungsablauf

1. X/Y-Abgaben erst anonymisieren, Reihenfolge möglichst zufällig.
2. Gleiche Browser-/Testbedingungen und Viewports nutzen, Resultat mit
   Screenshots/Prüfschritten belegen.
3. Jede Dimension mit kurzem Befund/Evidence bewerten.
4. Danach A/B-Zuordnung auflösen und Unterschiede in Kosten, Laufzeit,
   Scope, Toolzugriff und Abgabequalität auswerten.
5. **Keinen** Qualitätsgewinn behaupten, wenn die externen
   Zusatzinformationen nicht der einzige wesentliche Unterschied waren.

Kein LLM-Selbsturteil als unabhängiger Abschlussnachweis.
