# Workflow – Bestehende Website Review

## Ziel

Eine bestehende Website getrennt auf Design, Accessibility, Performance, gerendertes Verhalten und gegebenenfalls Content-Slop prüfen.

## Empfohlene Skill-Kette

```text
visual-verification
→ accessibility-review
→ frontend-performance
→ web-design-review
→ optional web-content
→ optional code-review
```

## 1. Ist-Zustand erfassen

`visual-verification`

Mindestens soweit relevant:

- Desktop;
- Mobile;
- Zwischenbreiten;
- Loading / Empty / Error / Success;
- Navigation, Menüs, Dialoge;
- Tastatur und Fokus;
- Konsole / Netzwerk.

## 2. Accessibility

`accessibility-review`

Accessibility-Funde nicht durch starke visuelle Wirkung relativieren.

## 3. Performance

`frontend-performance`

Messung vor Optimierung. Lab- und Felddaten nicht vermischen.

## 4. Designreview

`web-design-review`

Prüft:

- Identität;
- Informationshierarchie;
- Typografie / Rhythmus;
- Interaktion;
- responsive Gestaltung;
- generische oder unmotivierte AI-Patterns.

## 5. Content optional separat

`web-content`, wenn Fake-Daten, generische Marketingprosa oder UI-Copy ein relevanter Teil des Problems sind.

## 6. Code Review optional

Wenn konkrete Änderungen bereits vorliegen, `code-review` gegen den tatsächlichen Diff einsetzen.

## Ausgabe

Funde nach Wirkung und Achse strukturieren. Nicht alle Design-, Accessibility- und Performanceprobleme zu einer einzigen Geschmacksnote vermischen.

## Gate

Ein statischer Screenshot oder Quellcode allein reicht nicht für die Aussage, dass eine interaktive Website vollständig geprüft wurde.
