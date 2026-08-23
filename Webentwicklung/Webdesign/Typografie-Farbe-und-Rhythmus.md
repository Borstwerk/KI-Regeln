# Typografie, Farbe und Rhythmus

## Zweck

Dieses Dokument beschreibt die visuellen Grundsysteme einer Website: Typografie, Farbe, Spacing, Flächen und Rhythmus.

Ziel ist ein kohärentes System mit erkennbarer Priorität – nicht das Ansammeln vieler einzelner hübscher Entscheidungen.

## 1. Typografie trägt Hierarchie

Typografie soll erkennen lassen:

- was primär ist;
- was sekundär ist;
- was interaktiv ist;
- was erklärend oder ergänzend ist;
- was zusammengehört.

Nicht jede Hierarchie braucht eine zusätzliche Card, Farbe oder Linie.

## 2. Schriftwahl bewusst treffen

Schriftwahl ist Teil der Identität.

Prüfen:

- Passt die Schrift zum Produktcharakter?
- Ist sie in allen benötigten Schnitten verfügbar?
- Funktioniert sie für lange Texte und kleine UI-Größen?
- Unterstützt sie benötigte Sprachen und Zeichen?
- Sind Performance- und Lizenzanforderungen geklärt?

Default-Systemschriften oder häufige Webfonts sind nicht verboten. Sie sollten nur nicht automatisch gewählt werden, wenn eine andere typografische Richtung besser passt.

## 3. Typografische Skala statt Einzelfallwerte

Definiere nachvollziehbare Rollen, beispielsweise:

- Display;
- H1/H2/H3;
- Body;
- Small/Meta;
- Label/Button.

Größe, Gewicht, Zeilenhöhe und Tracking sollen zusammen gedacht werden.

## 4. Lesbarkeit vor Effekt

Vermeiden:

- zu geringe Kontraste;
- extrem kleine Fließtexte;
- überbreite Textzeilen;
- zu enge Zeilenhöhen;
- Versalien für lange Texte;
- Text direkt auf unruhigen Bildern ohne ausreichende Trennung.

## 5. Farbe hat Rollen

Farben nicht nur als Palette, sondern als semantische Rollen definieren:

- Hintergrund;
- Surface;
- Text primär/sekundär;
- Accent;
- Link;
- Fokus;
- Erfolg/Warnung/Fehler;
- deaktivierte Zustände.

Damit bleibt das System stabiler als bei zufälligen Hex-Werten pro Komponente.

## 6. Akzentfarbe nicht überall verwenden

Eine Akzentfarbe verliert Wirkung, wenn sie jede Fläche, jeden Icon-Hintergrund und jede Überschrift einfärbt.

Akzente sollen Priorität oder Identität tragen.

## 7. Gradient, Glow und Blur nur mit Aufgabe

Diese Mittel können passen, wenn sie:

- Marke oder Thema tragen;
- räumliche Hierarchie unterstützen;
- einen klaren Fokus setzen;
- in einer bewussten visuellen Sprache verankert sind.

Nicht als automatisches Synonym für „modern“ einsetzen.

## 8. Spacing als System

Abstände sollen Beziehungen ausdrücken.

Beispiel:

```text
innerhalb einer Gruppe < zwischen Gruppen < zwischen großen Abschnitten
```

Nicht jede Lücke einzeln nach Gefühl festlegen.

## 9. Rhythmus statt Gleichförmigkeit

Eine gute Website braucht Wiederholung und Variation.

Wiederholung schafft Kohärenz:

- Raster;
- Typorollen;
- Spacing;
- Flächenlogik.

Variation schafft Fokus:

- unterschiedliche Abschnittsdichte;
- bewusste Full-Bleed-Momente;
- wechselnde Text-/Medienbalance;
- besondere Schlüsselbereiche.

Dauerhafte Gleichförmigkeit wirkt schnell wie ein Komponenten-Katalog.

## 10. Radius- und Surface-Logik begrenzen

Nicht automatisch jede Ebene abrunden und verschachteln.

Card-in-Card-in-Card erzeugt visuelles Rauschen.

Prüfen:

- Muss diese Fläche eigenständig sein?
- Ist ein Rahmen nötig?
- Reicht Abstand oder Hintergrundwechsel?
- Gibt es zu viele Radiusgrößen?

## 11. Design Tokens als lokale Quelle

Relevante Projekte sollten zentrale Tokens besitzen, beispielsweise für:

- Farben;
- Typografie;
- Spacing;
- Radius;
- Schatten;
- Z-Index;
- Motion-Dauer und Easing.

Tokens sollen echte Wiederverwendung abbilden, nicht jede mögliche Zahl in eine Variable verwandeln.

## Qualitätscheck

1. Trägt Typografie die Informationshierarchie?
2. Ist die Schriftwahl begründet?
3. Sind Fließtexte gut lesbar?
4. Haben Farben semantische Rollen?
5. Werden Akzente sparsam und gezielt eingesetzt?
6. Ist Spacing systematisch?
7. Gibt es Rhythmus statt monotone Wiederholung?
8. Sind Surfaces und Radien begrenzt?
9. Werden dekorative Effekte funktional begründet?

## Leitgedanke

> Ein Designsystem soll Entscheidungen konsistent machen – nicht die Seite in eine uniforme Komponentenmaschine verwandeln.