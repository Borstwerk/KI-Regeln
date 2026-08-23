# Accessibility

## Zweck

Dieses Dokument beschreibt Accessibility als Qualitätsanforderung der Webentwicklung, nicht als nachträgliche Checkliste.

## Grundregel

> Eine visuell starke Oberfläche ist nicht fertig, wenn wesentliche Nutzer sie nicht zuverlässig bedienen oder verstehen können.

## 1. Semantik vor ARIA-Reparatur

Bevorzugt native HTML-Elemente korrekt verwenden:

- `button` für Aktionen;
- `a` für Navigation;
- echte Überschriftenhierarchie;
- `label` für Formulare;
- Listen, Tabellen und Landmarken semantisch passend.

ARIA ergänzt Semantik. Es soll falsche Grundelemente nicht unnötig kaschieren.

## 2. Tastaturbedienung

Prüfen:

- alle relevanten Aktionen erreichbar;
- sichtbarer Fokus;
- logische Fokusreihenfolge;
- keine Keyboard Traps;
- Dialoge und Menüs korrekt betreten und verlassen;
- Escape-Verhalten, wo passend.

## 3. Fokus ist ein eigener Zustand

Focus Styles nicht aus Designgründen entfernen.

Der Fokus muss ausreichend sichtbar sein und darf nicht nur über Farbe mit minimalem Unterschied kommuniziert werden.

## 4. Kontrast und Lesbarkeit

Prüfen:

- Textkontrast;
- UI-Kontrast relevanter Controls;
- Zustände wie Disabled, Error und Focus;
- Text auf Bildern oder Gradients;
- Dark Mode, sofern vorhanden.

Kontrast ist nicht nur eine Zahl: Lesbarkeit hängt auch von Größe, Gewicht, Hintergrund und realer Nutzung ab.

## 5. Formulare

Jedes Feld braucht eine verständliche Bezeichnung.

Prüfen:

- Labels;
- Pflichtfeldkennzeichnung;
- Fehlermeldungen;
- Zuordnung von Fehlern zum Feld;
- Hilfe- und Beschreibungstexte;
- sinnvolle Autocomplete-Attribute;
- Datenverlust bei Validierungsfehlern.

Placeholder ersetzt kein Label.

## 6. Bilder und Medien

Alt-Texte nach Funktion wählen:

- informative Bilder beschreiben relevante Information;
- dekorative Bilder entsprechend behandeln;
- komplexe Visualisierungen brauchen gegebenenfalls zusätzliche Textalternativen;
- Videos benötigen je nach Kontext Untertitel oder weitere Alternativen.

Nicht jedes Bild braucht eine wortreiche Beschreibung.

## 7. Farbe nie als einziges Signal

Fehler, Status oder Auswahl nicht ausschließlich über Farbe darstellen.

Zusätzliche Mittel können sein:

- Text;
- Icon mit verständlicher Semantik;
- Form;
- Position;
- Beschriftung.

## 8. Motion und Bewegung

Nutzerpräferenzen wie `prefers-reduced-motion` berücksichtigen.

Vermeiden:

- unnötige Dauerbewegung;
- starke Parallaxeffekte;
- blinkende oder flackernde Inhalte;
- Animation als einzige Erklärung eines Zustands.

## 9. Zoom und Reflow

Oberflächen sollen auch bei Vergrößerung und kleinen Viewports verständlich bleiben.

Nicht verhindern:

- Browserzoom;
- Textvergrößerung;
- notwendiges Reflow.

## 10. Screenreader-nahe Prüfung

Automatisierte Checks sind hilfreich, aber nicht ausreichend.

Bei relevanten Oberflächen prüfen:

- Landmarken;
- Überschriftenstruktur;
- Formularnamen;
- Button-/Linknamen;
- Dialoge;
- dynamische Statusmeldungen;
- sinnvolle Lesereihenfolge.

## 11. Accessibility als Regressionstest

Wiederkehrende Fehler möglichst mechanisieren:

- Linter;
- automatisierte Accessibility-Tests;
- Komponentenchecks;
- Browser-/E2E-Tests.

Automatisierung ersetzt keine manuelle Bedienprüfung, senkt aber Wiederholungsfehler.

## Qualitätscheck

1. Wird native Semantik genutzt?
2. Funktioniert die Kernaufgabe per Tastatur?
3. Ist Fokus sichtbar und logisch?
4. Sind Kontraste ausreichend?
5. Sind Formulare korrekt beschriftet?
6. Haben Medien angemessene Alternativen?
7. Wird Farbe nie als einziges Signal verwendet?
8. Werden Motion-Präferenzen respektiert?
9. Funktioniert Zoom/Reflow?
10. Wurden automatisierte und manuelle Checks kombiniert?

## Leitgedanke

> Accessibility ist kein Sondermodus der Website. Sie ist Teil der normalen Definition von funktionierender Weboberfläche.