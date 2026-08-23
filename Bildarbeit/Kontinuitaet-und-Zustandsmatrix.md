# Kontinuität und Zustandsmatrix

## Zweck

Serienbilder zeigen Zustände zu bestimmten Zeitpunkten. Dauerhafte oder temporäre Veränderungen müssen deshalb so geplant werden, dass sie nicht zu früh, zu spät oder widersprüchlich sichtbar werden.

## Zustandsmatrix

Vor längeren Bildserien wird für zeitabhängige Merkmale eine kompakte Matrix angelegt.

Typische Einträge:

- Kleidung, Schmuck und Ausrüstung;
- Verletzungen, Narben, Schäden und Reparaturen;
- verlorene oder neu erhaltene Gegenstände;
- sichtbare Verschmutzung oder Alterung;
- anwesende und noch nicht anwesende Figuren;
- Zustand eines Orts oder Gebäudes;
- Tageszeit, Wetter oder besondere Lichtlage;
- Zustand eines Produkts oder Fahrzeugs;
- andere irreversible oder chronologisch relevante Veränderungen.

Beispiel:

| Merkmal | Szene 01 | Szene 02 | Szene 03 | Szene 04 |
|---|---|---|---|---|
| Figur A – Anhänger | vorhanden | vorhanden | verloren | fehlt |
| Objekt B – Schaden | intakt | beschädigt | beschädigt | repariert |
| Figur C | abwesend | abwesend | erstmals sichtbar | sichtbar |
| Ort D – Wetter | trocken | Regen beginnt | Regen | danach nass |

## Matrix ist Produktionshilfe, keine zweite Wahrheit

Die Matrix fasst bereits festgelegte Zustände zusammen. Sie darf keine neue Handlung oder neue Projektregel erfinden.

Bei Widerspruch gilt die kanonische Quelle des Projekts.

## Zustandswechsel als Ereignis behandeln

Ein Merkmal wechselt nicht irgendwann vage, sondern an einem definierten Punkt:

```text
vor Ereignis
→ Ereignis / Übergang
→ nach Ereignis
```

Damit wird verhindert, dass ein neuer Zustand schon in früheren Bildern auftaucht.

## Referenzen nach Zuständen trennen

Wenn eine Entität mehrere dauerhafte Zustände hat, können getrennte Referenzen sinnvoll sein:

- Zustand A – vor Schaden;
- Zustand B – beschädigt;
- Zustand C – repariert.

Eine ältere Referenz wird nicht blind weiterverwendet, wenn der sichtbare Zustand inzwischen dauerhaft verändert ist.

## Kontinuitätsdrift erkennen

Typische Drift:

- Accessoire erscheint und verschwindet ohne Ereignis;
- Narbe wechselt Seite;
- Objekt ist plötzlich unbeschädigt;
- Größenrelationen ändern sich zwischen Bildern;
- Ort verändert seine Grundgeometrie;
- Wetter oder Licht springt unmotiviert;
- Figur taucht vor ihrem vorgesehenen Auftreten auf.

Solche Abweichungen werden als Kontinuitätsfehler behandelt, nicht als kreative Variation.

## Zustandsprüfung vor jeder Generierung

Vor einem Bild kurz prüfen:

1. Welche zeitabhängigen Merkmale sind in dieser Szene relevant?
2. Welcher Zustand gilt jetzt?
3. Welche früheren Referenzen sind für diesen Zustand noch gültig?
4. Gibt es Merkmale, die ausdrücklich noch nicht sichtbar sein dürfen?
5. Muss nach dieser Szene eine Referenz oder Matrix aktualisiert werden?

## Qualitätscheck für eine Serie

Nach mehreren Bildern prüfen:

- bleiben dauerhafte Merkmale nach ihrer Einführung erhalten?
- erscheinen temporäre Merkmale nur im richtigen Zeitraum?
- bleiben Seiten, Positionen und Größen stabil?
- stimmen sichtbare Schäden, Reparaturen und Besitzstände?
- passen Ort, Wetter und Licht zur vorgesehenen Chronologie?

## Leitgedanke

> Visuelle Kontinuität ist gespeicherter Zustand, nicht Erinnerung aus dem Bauchgefühl.