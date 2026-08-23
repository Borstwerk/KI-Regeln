# Bildarbeit mit generativer KI

Dieser Bereich beschreibt allgemeine Regeln für die Planung, Erzeugung, Prüfung, Korrektur und Freigabe konsistenter Bildserien mit generativer KI.

Ziel ist nicht, möglichst schnell möglichst viele schöne Einzelbilder zu erzeugen. Ziel ist eine **konsistente visuelle Produktion**, in der wiederkehrende Figuren, Objekte, Orte, Stil, Größenverhältnisse, Zustände und Szenenlogik zuverlässig zusammenpassen.

## Grundprinzip

> Konsistenz vor Zufall. Aussage vor Effekt. Referenz vor Neuerfindung.

Ein visuell spektakuläres Bild ist kein guter Produktionsstand, wenn es die falsche Figur, einen falschen Zustand, eine falsche Szene oder einen ungewollten Stilbruch zeigt.

## Vier getrennte Konsistenzachsen

Bei Bildserien werden vier Fragen getrennt geprüft:

1. **Identitätskonsistenz** – ist es dieselbe Figur, dasselbe Objekt oder derselbe Ort?
2. **Stilkonsistenz** – gehört das Bild sichtbar zur selben visuellen Welt?
3. **Struktur- und Kompositionskonsistenz** – ist die Bildorganisation kontrolliert und passend zur Szene?
4. **Kontinuitätskonsistenz** – stimmt der sichtbare Zustand zum richtigen Zeitpunkt innerhalb der Serie?

Diese Achsen beeinflussen sich, sind aber nicht dasselbe.

## Bausteine

### Quellen und Prioritäten

Bildarbeit benötigt eine klare Hierarchie der Quellen der Wahrheit. Aktueller Auftrag und kanonische Projektdokumentation stehen über älteren Referenzen oder zufälligen Generierungen.

Siehe `Quellen-und-Prioritaeten.md`.

### Stil und Referenzsysteme

Stil-, Struktur- und Identitätsreferenzen haben unterschiedliche Aufgaben. Referenzen sind Anker, keine automatischen Kopiervorlagen.

Siehe `Stil-und-Referenzsysteme.md`.

### Charaktere, Objekte und Orte

Wiederkehrende Entitäten erhalten stabile Produktionsreferenzen mit Pflichtmerkmalen, zulässigen Variationen und bekannten Ausschlüssen.

Siehe `Charaktere-Objekte-und-Orte.md`.

### Szenenplanung und Komposition

Vor jeder Generierung werden konkreter Moment, Bildaussage, Perspektive, sichtbare Elemente, Kontinuität und Ausschlüsse festgelegt.

Siehe `Szenenplanung-und-Komposition.md`.

### Kontinuität und Zustandsmatrix

Zeitabhängige Änderungen werden vor Serienproduktion sichtbar geplant, damit Zustände nicht zu früh, zu spät oder inkonsistent erscheinen.

Siehe `Kontinuitaet-und-Zustandsmatrix.md`.

### Bildprüfung und Freigabe

Nach jeder Generierung wird zwischen Keeper, lokalem Feinschliff, kontrolliertem Neubau und vollständigem Neubau unterschieden. Ein angenommener Keeper wird nicht ohne Grund kaputtoptimiert.

Siehe `Bildpruefung-und-Freigabe.md`.

### Serienproduktion und Abschlussaudit

Eine Bildserie wird nicht nur bildweise, sondern zusätzlich als Gesamtfolge geprüft.

Siehe `Serienproduktion-und-Abschlussaudit.md`.

## Produktionsfluss

```text
Quellen und Kanon
→ visuelle Planung
→ Referenzsystem
→ Szenen-Pre-Brief
→ Generierung
→ Review
→ gezielte Korrektur oder Keeper
→ Serienaudit
→ Abschluss
```

## Leitgedanken

- Wiederkehrende Entitäten werden nicht in jeder Generation neu erfunden.
- Nicht freigegebene Zufallsdetails werden nicht automatisch kanonisch.
- Stilreferenz, Strukturreferenz und Identitätsreferenz sind unterschiedliche Werkzeuge.
- Ein Bild soll einen klaren Moment erzählen, keine Mischung mehrerer Zeitpunkte.
- Zeitabhängige Merkmale werden über eine Zustandsmatrix gesichert.
- Wiederholte gleiche Fehler führen zu einer geänderten Strategie statt zum identischen Prompt.
- Ein neueres Bild ist nicht automatisch besser als seine Vorversion.
- Kleine Restfehler können akzeptabel sein, wenn weitere Generierung das Gesamtergebnis wahrscheinlicher verschlechtert.
- Die Serie als Ganzes ist das Produkt, nicht nur die Summe einzelner Bilder.

## Skills

Unter `Skills/` liegen kompakte Arbeitsdisziplinen:

- `bild-prebrief` – ein einzelnes Bild vor der Generierung sauber definieren;
- `entitaetsbibel` – stabile Referenzregeln für wiederkehrende Figuren, Objekte oder Orte aufbauen;
- `serien-kontinuitaetscheck` – mehrere Bilder auf Zustands-, Identitäts- und Stildrift prüfen;
- `bildreview` – entscheiden, ob ein Bild behalten, lokal korrigiert oder neu gebaut werden sollte.

Projektkonkrete Figurenmerkmale, Weltregeln und Kanon bleiben im jeweiligen Projekt.