# Workflow – Website-Neuentwicklung

## Ziel

Eine Website mit klarer Produktidentität, belastbarer Informationsarchitektur, echtem Content und verifizierter Frontendqualität entwickeln.

## Skill-Kette

```text
frontend-design
→ design-system
→ greybox
→ web-content
→ Implementierung
→ accessibility-review
→ frontend-performance
→ visual-verification
→ web-design-review
```

## Phasen

### 1. Art Direction

`frontend-design`

Output:

- Produkt-/Zielgruppenfit;
- visuelle These;
- Signature Elements;
- bewusste Anti-Patterns.

### 2. Designsystem

`design-system`

Stabile Typo-, Farb-, Spacing-, Surface- und Interaktionsregeln.

### 3. Greybox

`greybox`

- Seitenzweck;
- Informationshierarchie;
- Navigation;
- Hauptaktionen;
- Mobile-Logik.

Erst freigeben, wenn die Struktur ohne visuelle Tricks funktioniert.

### 4. Echter Content

`web-content`

Keine Fake-KPIs, Fake-Testimonials oder bedeutungsleere Template-Sektionen.

### 5. Implementierung

Technischen Stack aus dem Projekt übernehmen. Allgemeine Programmierregeln und bei Bedarf TDD/Code Review verwenden.

### 6. Qualitätsgates

- `accessibility-review`;
- `frontend-performance`;
- `visual-verification`.

### 7. Unabhängiger Designreview

`web-design-review`

Der erzeugende Agent soll sein eigenes Ergebnis nicht allein freigeben.

## Gate

```text
Designidentität
+ Aufgabenfit
+ echte Inhalte
+ Accessibility
+ Responsive Verhalten
+ Performance-Evidence
+ gerenderte Verifikation
+ unabhängiger Review
```

## Security

Neue externe Scripts, Tracking-, Analyse- oder Third-Party-Integrationen bei Bedarf mit `tool-permission-review` bzw. Security Review prüfen.
