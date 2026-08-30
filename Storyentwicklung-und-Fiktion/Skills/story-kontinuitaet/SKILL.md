---
name: story-kontinuitaet
description: Prüft fiktionale Szenen, Kapitel oder Serienstände auf Timeline-, Wissens-, Figuren-, Objekt-, Weltregel-, Setup/Payoff- und Story-State-Widersprüche. Verwenden bei Kontinuitätscheck oder Entwicklungsreview; standardmäßig read-only und ohne ungefragte Umschreibung.
---

# Story-Kontinuität

Dieser Skill nutzt `../../Story-Kontinuitaet-und-Zustandslogik.md` und vorhandene Projektquellen.

## Vorbedingung

Für belastbare Findings die relevanten Primärtexte und aktuellen Kanonquellen lesen. Zusammenfassungen allein reichen nicht, wenn sie mit dem Manuskript kollidieren könnten.

## Workflow

1. Prüfscope festlegen: Szene, Kapitel, Band oder ausgewählte Arcs.
2. Relevante Quellen und ihren Stand bestimmen.
3. Timeline und Orte prüfen.
4. Figurenstatus, Beziehungen und Fähigkeiten prüfen.
5. Figurenwissen und Informationswege separat prüfen.
6. wichtige Objektzustände und Besitz prüfen.
7. Weltregeln und etablierte Ausnahmen prüfen.
8. offene Fragen, Setup/Payoff und Arc-Zustände prüfen.
9. Findings als Widerspruch, Drift, Lücke, Unklarheit oder Planungsabweichung klassifizieren.
10. kleinsten sinnvollen Fix empfehlen, aber nicht ungefragt umschreiben.

## Nicht automatisch als Fehler werten

- Flashback;
- Traum oder Vision;
- Erinnerung;
- Lüge;
- Gerücht;
- unzuverlässige Perspektive;
- bewusst falsches Figurenwissen;
- posthume Erwähnung.

Wenn die Textfunktion nicht eindeutig ist, Unsicherheit markieren.

## Abgrenzung

Nicht verwenden, wenn ausschließlich Stil, Rhythmus oder Natürlichkeit geprüft werden sollen; dafür `stilreview` nutzen. Neue Plotplanung gehört zu `plot-und-storystruktur`, direkte Textrevision ohne vorherige Freigabe ist nicht Teil dieses read-only Reviews.

## Ausgabeformat

```markdown
## Urteil
<kurze Gesamtbewertung>

## Findings
### <Schweregrad / Typ> – <Kurzname>
- Evidence / Fundstellen:
- Konflikt:
- Auswirkung:
- kleinster sinnvoller Fix:

## Offene Unsicherheiten
- ...

## Empfohlener nächster Schritt
<Review abschließen, enger Fix, Replan oder Human Gate>
```

## Regeln

- Same-Model-Review nicht als unabhängig bezeichnen.
- Planabweichung nicht automatisch als Manuskriptfehler werten.
- Fehlende Evidence nicht mit plausibler Erinnerung füllen.
- Review ≠ Änderungsfreigabe.
- Bei lokalem Widerspruch keinen unnötigen Gesamtumbau empfehlen.

## Leitfrage

> Lässt sich jeder relevante Zustand aus dem bisher erzählten Verlauf nachvollziehbar herleiten?
