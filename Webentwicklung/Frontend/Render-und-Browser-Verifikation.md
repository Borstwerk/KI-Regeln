# Render- und Browser-Verifikation

## Zweck

Dieses Dokument beschreibt die Prüfung einer Website im tatsächlich gerenderten Zustand.

Code, Tests und statische Analyse sind notwendig, reichen für Weboberflächen aber nicht aus. Viele Fehler werden erst sichtbar, wenn die Seite in einem Browser mit realen Daten und Viewports gerendert wird.

## Grundregel

> Eine Weboberfläche ist nicht verifiziert, solange nur ihr Quellcode geprüft wurde.

## 1. Relevante Seiten wirklich rendern

Mindestens die geänderten oder kritischen Seiten/Zustände öffnen.

Prüfen:

- Layout;
- Typografie;
- Bilder;
- Navigation;
- Formulare;
- Dialoge;
- Datenzustände;
- Fehlermeldungen;
- responsive Verhalten.

## 2. Desktop und Mobile prüfen

Nicht nur eine Standardbreite verwenden.

Mindestens:

- Desktop;
- Mobile;
- relevante Zwischenbreiten bei komplexen Layouts.

Bei projektspezifischen Anforderungen zusätzliche Geräte/Browserszenarien.

## 3. Nicht nur Happy Path

Wichtige Zustände rendern:

- leer;
- loading;
- success;
- error;
- lange Inhalte;
- große Datenmengen;
- deaktivierte Controls;
- geöffnete Menüs/Dialoge;
- Fokuszustände.

## 4. Screenshot oder visuelle Evidence

Bei relevanten UI-Änderungen kann die Evidence enthalten:

- Screenshots;
- visuelle Regressionstests;
- DOM-/Accessibility-Snapshots;
- Video/Interaction Capture;
- dokumentierte Browserprüfung.

Ein Screenshot allein beweist keine Interaktionskorrektheit.

## 5. Visual Regression gezielt nutzen

Snapshot-basierte visuelle Tests sind sinnvoll für stabile kritische Oberflächen.

Aber:

- bewusst aktualisieren;
- nicht jede Pixelabweichung blind akzeptieren;
- dynamische Inhalte kontrollieren;
- neue Baseline nicht als Beweis verwenden, dass die Änderung richtig ist.

## 6. Browserkonsole und Netzwerk prüfen

Bei geänderten Flows auf:

- JavaScript-Fehler;
- React/Vue/Framework-Warnungen;
- fehlgeschlagene Requests;
- 404/500;
- unnötige Requests;
- CORS-/Security-Probleme;
- Hydration-Warnungen;
- Assetfehler

achten.

## 7. Tastatur und Fokus praktisch testen

Nicht nur Code lesen.

Mindestens bei relevanten Interaktionen:

- Tab-Reihenfolge;
- Enter/Space;
- Escape;
- Fokus bei Dialogöffnung;
- Fokus nach Dialogschließung;
- sichtbare Focus Styles.

## 8. Text und echte Daten testen

Gerenderte Verifikation mit realistischen Inhalten durchführen:

- lange Namen;
- lange Überschriften;
- Übersetzungen;
- leere Daten;
- große Zahlen;
- viele Listenelemente.

## 9. Unterschiede zwischen Browsern risikobasiert prüfen

Nicht jede kleine Seite muss manuell in zehn Browsern getestet werden.

Breitere Prüfung bei:

- neuen CSS-Funktionen;
- komplexen Form Controls;
- Media APIs;
- Canvas/WebGL;
- Drag-and-Drop;
- Dateiupload;
- projektspezifisch geforderten Browsern.

## 10. Review gegen Designbrief

Nach technischer Korrektheit zusätzlich prüfen:

- entspricht die Umsetzung der freigegebenen Designrichtung?
- ist die Informationshierarchie erhalten?
- sind Abstände/Typorollen kohärent?
- entstanden neue AI-Slop-Muster während der Umsetzung?

## Evidence-Ausgabe

Empfohlen:

```text
Geprüfte Seiten/Zustände
Geprüfte Viewports/Browser
Automatisierte Checks
Manuelle Interaktionschecks
Screenshots/visuelle Evidence
Konsole/Netzwerk
Bekannte Abweichungen
Offene Risiken
```

## Leitgedanke

> Der Browser ist für Weboberflächen ein Teil der Wahrheit. Eine plausible Komponente im Code ist noch keine funktionierende Seite.