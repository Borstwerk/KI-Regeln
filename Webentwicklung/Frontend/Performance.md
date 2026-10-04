# Performance

## Inhalt

- Zweck
- Grundregel
- 1. Kritische Pfade priorisieren
- 2. Waterfalls vermeiden
- 3. Bundle bewusst halten
- 4. Bilder und Medien optimieren
- 5. Renderingkosten verstehen
- 6. Client-JavaScript begrenzen
- 7. Fonts bewusst laden
- 8. Immersive Experiences als eigene Kostenklasse
- 9. Performancebudgets lokal definieren
- 10. Messung reproduzierbar machen
- 11. Performance-Regressionen mechanisieren
- Qualitätscheck
- Leitgedanke

## Zweck

Dieses Dokument beschreibt Frontend-Performance als Nutzer- und Systemqualität.

Ziel ist nicht blindes Mikrotuning. Optimiert werden sollen reale Engpässe mit messbarer Wirkung.

## Grundregel

> Erst messen, dann den größten Engpass mit vertretbarem Aufwand verbessern.

## 1. Kritische Pfade priorisieren

Typische Hochwirkungsthemen:

- Netzwerk-Waterfalls;
- unnötig große Bundles;
- zu viel Client-JavaScript;
- langsame Serverantworten;
- blockierende Ressourcen;
- übergroße Bilder;
- unnötige Re-Renders;
- teure Initialisierung.

Nicht jede Optimierung ist gleich wichtig.

## 2. Waterfalls vermeiden

Unabhängige Daten oder Ressourcen nicht unnötig nacheinander laden.

Prüfen:

- können Requests parallel starten?
- kann Datenzugriff näher an den Server oder die Route?
- warten Komponenten unnötig aufeinander?
- erzeugt eine Abstraktion versteckte Sequenzialität?

## 3. Bundle bewusst halten

Neue Pakete und Imports auf tatsächlichen Nutzen prüfen.

Vermeiden:

- ganze Bibliotheken für eine kleine Funktion;
- Client-Bundles mit serverseitig ausreichenden Abhängigkeiten;
- mehrfach eingebundene Alternativen für dieselbe Aufgabe;
- schwergewichtige Komponenten auf jeder Route, obwohl sie nur selten benötigt werden.

Mögliche Mittel:

- Code Splitting;
- Dynamic Imports;
- kleinere Abhängigkeiten;
- Tree Shaking;
- serverseitige Ausführung, sofern passend.

## 4. Bilder und Medien optimieren

Prüfen:

- richtige Dimensionen;
- moderne Formate, sofern unterstützt;
- Responsive Images;
- Lazy Loading für nicht kritische Medien;
- Priorisierung wichtiger Hero-/Above-the-fold-Bilder;
- keine riesigen Assets für kleine Darstellungen.

## 5. Renderingkosten verstehen

Nicht jede State-Änderung darf unnötig große UI-Bereiche neu rendern.

Prüfen:

- unnötig hoch liegender State;
- instabile Props oder Funktionen;
- teure Berechnungen im Renderpfad;
- große Listen ohne sinnvolle Strategie;
- Layout Thrashing.

Memoisierung nur mit konkretem Grund einsetzen.

## 6. Client-JavaScript begrenzen

JavaScript kostet Download, Parse, Ausführung und Hydration.

Prüfen:

- muss diese Funktion clientseitig sein?
- reicht HTML/CSS?
- kann Logik auf dem Server erfolgen?
- wird eine komplette UI-Bibliothek wegen eines kleinen Effekts geladen?

## 7. Fonts bewusst laden

Prüfen:

- nur benötigte Schnitte;
- geeignete Subsets;
- sinnvolle Preloads;
- Fallbacks;
- Layout Shift durch Fontwechsel;
- Lizenz und Hostingmodell.

## 8. Immersive Experiences als eigene Kostenklasse

3D-, WebGL-, Canvas-, große Parallax-/Scrolltelling-Szenen und dauerhaft laufende visuelle Simulationen können andere Kostenprofile besitzen als normale DOM-Oberflächen.

Je nach konkreter Technik zusätzlich prüfen:

- Initial- und Route-Bundle;
- Modell-, Textur-, Shader- und Mediengrößen;
- CPU-/GPU-Arbeit;
- Main-Thread-Blockierung;
- Speicher und Layer-/Scene-Komplexität;
- laufende Renderloops, auch wenn die Szene nicht sichtbar ist;
- Energie-/Thermik auf mobilen Geräten;
- Lade- und Decode-Zeit;
- Verhalten bei langsamer Hardware oder fehlender Spezialfähigkeit.

Mögliche Strategien – nur bei gemessenem Bedarf:

- Lazy Loading / Dynamic Import;
- Qualitätsstufen oder reduzierte Szenen;
- statische Poster-/Content-Fallbacks;
- Renderloop pausieren, wenn nicht sichtbar;
- Assetkomplexität reduzieren;
- Experience nur dort laden, wo sie tatsächlich gebraucht wird.

„Low Poly“, `transform`, GPU oder WebGL sind **keine** automatische Performancegarantie.

## 9. Performancebudgets lokal definieren

Für relevante Projekte konkrete Ziele festlegen, beispielsweise:

- maximale JavaScript-Größe;
- Bildbudgets;
- Core-Web-Vitals-Ziele;
- Antwortzeiten kritischer Routen;
- Zeit bis zur wichtigsten Interaktion.

Zentrale Regeln geben keine universellen Zahlen vor.

## 10. Messung reproduzierbar machen

Vergleiche nur unter ausreichend ähnlichen Bedingungen.

Dokumentieren:

- Gerät/Browser;
- Netzwerkprofil;
- Route;
- Cache-Zustand;
- Messwerkzeug;
- relevante Datenmenge.

## 11. Performance-Regressionen mechanisieren

Wo sinnvoll:

- Bundle-Checks;
- Lighthouse/CI-artige Prüfungen;
- Web-Vitals-Monitoring;
- Performance-Tests kritischer Pfade;
- Alerting auf relevante Regressionen.

## Qualitätscheck

1. Wurde der Engpass gemessen?
2. Sind Waterfalls geprüft?
3. Ist Client-Bundle begründet?
4. Sind Bilder passend dimensioniert?
5. Gibt es unnötige Renderarbeit?
6. Wird Client-JavaScript bewusst eingesetzt?
7. Sind Fonts sinnvoll geladen?
8. Wurden immersive/3D-/Canvas-Kosten als eigene Risikoklasse betrachtet, falls vorhanden?
9. Gibt es projektlokale Budgets, wenn Performance kritisch ist?
10. Sind Vorher/Nachher-Messungen vergleichbar?
11. Können wichtige Regressionen automatisch erkannt werden?

## Leitgedanke

> Performancearbeit beginnt nicht mit Tricks, sondern mit Priorität, Messung und dem Entfernen unnötiger Arbeit.