# Designrichtung und Identität

## Zweck

Dieses Dokument beschreibt, wie vor der eigentlichen Frontend-Umsetzung eine eigenständige visuelle Richtung entwickelt wird.

Ziel ist nicht, künstlich originell zu wirken. Ziel ist, dass die Gestaltung nachvollziehbar aus Produkt, Inhalt, Publikum und Nutzungssituation entsteht.

## Grundregel

> Gestaltung ist eine Entscheidung über Wirkung, nicht das automatische Anwenden bekannter UI-Muster.

## 1. Ausgangspunkt: Produkt, Publikum, Aufgabe

Vor Farbwahl oder Komponentenbau klären:

- Was ist das Produkt oder die Seite?
- Wer nutzt sie?
- Was soll ein Nutzer hier verstehen oder tun?
- Welche Wirkung ist angemessen?
- Was wäre für dieses Thema offensichtlich unpassend?

Beispiel:

Eine juristische Dokumentationsplattform, ein Festivalportal und eine Kinderlernseite dürfen technisch ähnliche Komponenten besitzen, aber nicht automatisch dieselbe visuelle Sprache.

## 2. Eine konkrete Designrichtung formulieren

Vor der Umsetzung eine kurze Art-Direction festlegen.

Sie kann enthalten:

- gewünschte Wirkung;
- typografischen Charakter;
- Flächen- und Materiallogik;
- Farblogik;
- Dichte und Rhythmus;
- Bild- und Illustrationssprache;
- Interaktionscharakter;
- bewusste Ausschlüsse.

Nicht ausreichend:

> modern, clean, professionell

Hilfreicher:

> ruhig, redaktionell und präzise; starke Serifenschrift für Orientierungspunkte, neutrale UI-Schrift für Bedienung; große Weißräume, wenige aber deutliche Farbakzente; keine Glassurfaces und keine dekorativen KPI-Karten.

## 3. Eine Richtung statt Stil-Mischmasch

Nicht gleichzeitig versuchen, minimalistisch, brutalistisch, verspielt, luxuriös, futuristisch und editorial zu wirken.

Kontraste sind möglich, brauchen aber eine Hierarchie.

Frage:

> Welche ein bis zwei gestalterischen Entscheidungen sollen die Seite unverwechselbar machen?

## 4. Hero als These, nicht als Template

Ein Hero ist keine Pflichtkombination aus:

```text
Badge
→ riesige Headline
→ Subheadline
→ zwei Buttons
→ Dashboard-Screenshot
```

Der Einstieg soll die wichtigste Aussage oder Nutzungssituation der Seite tragen.

Mögliche Formen:

- klarer redaktioneller Einstieg;
- interaktive Demo;
- starke Produktansicht;
- Daten- oder Inhaltsausschnitt;
- visuelle Erzählung;
- direkte Aufgabenoberfläche.

Die Form folgt dem Inhalt.

## 5. Signature Elements bewusst wählen

Ein wiederkehrendes Gestaltungselement kann Identität schaffen, beispielsweise:

- markante Typografie;
- ungewöhnliche aber funktionale Rasterlogik;
- charakteristische Trennlinien oder Flächen;
- spezifische Bildbehandlung;
- eigenständige Navigationslogik;
- kontrollierte Motion-Sprache.

Nicht fünf Signature Elements gleichzeitig erzwingen.

## 6. Referenzen analysieren statt kopieren

Referenzen dienen zur Klärung von:

- Typografie;
- Rhythmus;
- Informationsdichte;
- Farbwirkung;
- Interaktion;
- Bildsprache.

Nicht übernehmen:

- ganze Kompositionen ohne Anpassung;
- fremde Markenmerkmale;
- dekorative Details ohne funktionalen Bezug;
- Fehler oder Inkonsistenzen der Vorlage.

## 7. AI-Slop-Risiko explizit benennen

Vor Umsetzung prüfen, ob die Richtung unbewusst in bekannte Modellmuster kippt:

- generischer SaaS-Hero;
- lila/blauer Gradient ohne Markenbezug;
- Card-Raster für jeden Inhalt;
- abgerundete Icon-Kachel über jeder Überschrift;
- übermäßige Pills und Badges;
- große Glow-/Blur-Flächen;
- künstlich futuristische Mikrotexte;
- dekorative Diagramme ohne echte Daten.

Diese Mittel sind nicht verboten. Sie brauchen nur eine konkrete Begründung.

## 8. DESIGN.md als lokale Quelle der Wahrheit

Für relevante Projekte empfiehlt sich eine projektspezifische `DESIGN.md` oder vergleichbare Datei.

Sie kann enthalten:

- Designrichtung;
- Typografie;
- Farbrollen;
- Spacing-Grundsätze;
- Radius- und Surface-Logik;
- Icon-/Bildsprache;
- Motion-Regeln;
- Anti-Patterns;
- responsive Besonderheiten.

Diese Datei ist lokale Produktwahrheit und gehört nicht in dieses zentrale Repository.

## Qualitätscheck

1. Ist die Designrichtung konkreter als „modern/clean“?
2. Lässt sie sich aus Produkt und Zielgruppe begründen?
3. Gibt es eine erkennbare visuelle Priorität?
4. Werden Stilmittel bewusst statt reflexartig eingesetzt?
5. Ist der Einstieg inhaltlich begründet?
6. Gibt es wenige klare Signature Elements?
7. Sind Anti-Slop-Risiken benannt?
8. Ist die Richtung lokal dokumentierbar?

## Leitgedanke

> Eine Website soll aussehen, als wäre sie für genau dieses Produkt gestaltet worden – nicht als hätte das Produkt nachträglich ein beliebiges UI-Template bekommen.