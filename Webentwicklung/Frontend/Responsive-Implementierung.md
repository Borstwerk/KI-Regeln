# Responsive Implementierung

## Zweck

Dieses Dokument beschreibt die technische Umsetzung responsiver Weboberflächen.

Es ergänzt die gestalterischen Regeln aus `Webdesign/Responsive-und-Interaktion.md`.

## 1. Layouts flexibel statt gerätespezifisch bauen

Bevorzugen:

- flexible Grids;
- relative Breiten;
- sinnvolle `min/max`-Grenzen;
- `flex`, `grid`, `clamp()` und vergleichbare Layoutwerkzeuge;
- inhaltsgetriebene Breakpoints.

Vermeiden:

- feste Pixelpositionierung als Hauptlayout;
- separate Layouts für jede bekannte Geräteklasse ohne echten Grund;
- horizontales Scrollen durch unbeabsichtigte Überbreite.

## 2. Mobile-first ist Werkzeug, kein Dogma

Mobile-first kann helfen, Priorität und progressive Erweiterung sauber zu halten.

Entscheidend ist jedoch:

- Anforderungen des Produkts;
- vorhandene Architektur;
- Informationsdichte;
- tatsächliche Nutzergeräte.

## 3. Breakpoints aus Bruchstellen ableiten

Ein Breakpoint sollte dort entstehen, wo:

- Inhalt nicht mehr lesbar ist;
- Navigation nicht mehr passt;
- ein Grid seine Funktion verliert;
- Bedienelemente zu dicht werden;
- wichtige Relationen zusammenbrechen.

## 4. Container und Textbreiten begrenzen

Nicht jede Oberfläche sollte auf großen Screens bis zur maximalen Breite wachsen.

Prüfen:

- sinnvolle Maximalbreite für Text;
- breite Datenansichten separat behandeln;
- Full-Bleed-Bereiche bewusst einsetzen;
- Randabstände skalieren.

## 5. Bilder und Medien responsiv implementieren

- Seitenverhältnisse stabil halten;
- passende Quellen pro Größe verwenden;
- Layout Shift vermeiden;
- `object-fit` und Fokusbereiche bewusst nutzen;
- Medien nicht nur per CSS verkleinern, wenn kleinere Assets verfügbar sind.

## 6. Tabellen brauchen eine echte Strategie

Mögliche Strategien:

- horizontales Scrollen mit klarer Führung;
- Spalten priorisieren;
- alternative Karten-/Detailansicht;
- progressive Disclosure;
- gestapelte Darstellung.

Nicht jede Tabelle darf automatisch in Cards zerfallen. Die Datenbeziehung muss erhalten bleiben.

## 7. Navigation technisch robust machen

Mobile Menüs und Dialoge brauchen:

- kontrollierten offenen Zustand;
- korrekte Fokusführung;
- Scroll-Locking nur wenn nötig;
- Escape/Close-Verhalten;
- Rückgabe des Fokus;
- semantisch passende Controls.

## 8. Inhalte nicht nur per CSS verstecken

Wenn große Inhaltsmengen mobil dauerhaft verborgen werden, prüfen, ob:

- sie wirklich sekundär sind;
- Nutzer sie weiterhin erreichen können;
- unnötige Daten trotzdem geladen werden;
- SEO oder Accessibility betroffen ist.

## 9. Reale Größen testen

Mindestens prüfen:

- schmale mobile Breite;
- typische mobile Breite;
- Tablet-/Zwischenbereich;
- normaler Desktop;
- breiter Desktop;
- Zoom und vergrößerte Schrift.

Nicht nur zwei Screenshots bei 375 und 1440 Pixeln.

## 10. Edge Cases

Prüfen:

- sehr lange Wörter;
- lange Übersetzungen;
- leere Zustände;
- volle Tabellen;
- viele Navigationseinträge;
- dynamische Inhalte;
- Browserzoom;
- Landscape Mobile.

## Qualitätscheck

1. Ist das Layout flexibel statt pixelhart?
2. Sind Breakpoints inhaltsgetrieben?
3. Bleiben Textbreiten lesbar?
4. Sind Medien responsiv und dimensionsstabil?
5. Haben Tabellen eine geeignete Strategie?
6. Funktioniert Navigation technisch korrekt?
7. Werden versteckte Inhalte bewusst behandelt?
8. Wurden Zwischenbreiten und Edge Cases geprüft?

## Leitgedanke

> Responsive Implementierung ist bestanden, wenn die Oberfläche zwischen den Demo-Breakpoints genauso zuverlässig funktioniert wie auf ihnen.