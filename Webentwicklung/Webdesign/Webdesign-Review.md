# Webdesign-Review

## Zweck

Dieses Dokument beschreibt einen unabhängigen Review einer bestehenden Website oder Weboberfläche.

Der Review prüft nicht nur, ob die Seite „schön“ aussieht. Er bewertet, ob Design, Inhalt und Interaktion zur tatsächlichen Aufgabe passen und ob typische generische KI-Muster die Produktidentität überdecken.

## Grundregel

> Review die gerenderte Oberfläche, nicht nur den Prompt oder den Code.

## 1. Gegen die lokale Designquelle prüfen

Wenn vorhanden, zuerst lesen:

- Produktbeschreibung;
- Zielgruppenbeschreibung;
- `DESIGN.md` oder vergleichbare Designregeln;
- Inhalts- und Markenregeln;
- relevante Referenzen;
- akzeptierte Greyboxes oder Mockups.

Ohne lokale Designquelle darf der Review allgemeine Qualitätsprobleme benennen, aber keine eigene Markenidentität erfinden.

## 2. Reviewachsen getrennt bewerten

### Identität

- Wirkt die Seite spezifisch für dieses Produkt?
- Gibt es erkennbare gestalterische Entscheidungen?
- Oder könnte derselbe Screen fast unverändert für zehn andere SaaS-Produkte stehen?

### Informationshierarchie

- Ist klar, was zuerst verstanden werden soll?
- Sind Haupt- und Nebenaktionen unterscheidbar?
- Werden Informationen sinnvoll gruppiert?

### Typografie und Rhythmus

- Trägt Typografie die Hierarchie?
- Sind Textlängen und Zeilenbreiten lesbar?
- Ist das Layout rhythmisch oder monoton?

### Content

- Sind Aussagen konkret?
- Gibt es erfundene Beweise oder Füllinhalte?
- Haben Abschnitte einen echten Zweck?

### Interaktion

- Sind Zustände verständlich?
- Ist Navigation nachvollziehbar?
- Funktioniert die Oberfläche auch ohne dekorative Motion?

### Responsive Qualität

- Bleibt Priorität auf kleinen Screens erhalten?
- Werden komplexe Elemente sinnvoll transformiert?

## 3. Anti-Slop-Check

Auffällige Muster ausdrücklich prüfen:

- generischer Hero-Aufbau;
- übermäßige Cards;
- Pills/Badges ohne Funktion;
- Icon-Kachel über jeder Überschrift;
- Gradient/Glow/Blur als Default;
- Card-in-Card-Verschachtelung;
- unmotivierte Scroll-Reveals;
- erfundene KPI-/Testimonial-Blöcke;
- generische Marketingphrasen;
- Sci-Fi- oder Managementsprache ohne Produktgrund.

Ein Fund ist noch kein automatischer Fehler. Entscheidend ist, ob das Stilmittel funktional oder identitätsbildend begründet ist.

## 4. Funde priorisieren

Nicht hundert gleichgewichtete Designmeinungen auflisten.

Bevorzugte Prioritäten:

- **Blocker** – Aufgabe, Verständlichkeit oder Bedienung scheitert;
- **hoch** – starke Fehlhierarchie, unpassende Identität oder schwerer Konsistenzbruch;
- **mittel** – relevante Qualitätsminderung;
- **niedrig** – lokaler Feinschliff.

## 5. Ursache statt kosmetischem Symptom benennen

Schwach:

> Die Card könnte weniger Radius haben.

Stärker:

> Fünf verschachtelte Flächen konkurrieren um dieselbe Hierarchie. Zwei Ebenen können durch Abstand und Typografie ersetzt werden.

## 6. Nicht redesignen, wenn Review gefragt ist

Ein Review benennt:

- Problem;
- Auswirkung;
- Fundstelle;
- mögliche Richtung zur Korrektur.

Es soll nicht ungefragt eine komplett neue Designrichtung einführen.

## 7. Vorversionen und Referenzen vergleichen

Wenn mehrere Versionen vorhanden sind:

- nicht automatisch die neueste bevorzugen;
- stärkere Hierarchie und Identität höher gewichten als Neuheit;
- Regressionen ausdrücklich benennen.

## Review-Ausgabe

Empfohlen:

```text
Gesamturteil

Blocker / hohe Funde
- Fundstelle
- Problem
- Wirkung
- empfohlene Richtung

Mittlere / kleine Funde
...

Anti-Slop-Risiken
...

Was bereits stark ist und nicht unnötig umgebaut werden sollte
...
```

## Leitgedanke

> Ein guter Designreview schützt sowohl vor generischer Beliebigkeit als auch vor unnötigem Redesign funktionierender Lösungen.