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

Wenn externe Inspiration relevant ist, zuerst ein kleines Reference Board erstellen und die Vorlagen in übertragbare Prinzipien versus produktspezifische/geschützte Ausdrucksformen zerlegen. Keine einzelne Referenz als faktische Implementierungsvorlage behandeln.

Output:

- Produkt-/Zielgruppenfit;
- visuelle These;
- abstrahierte Referenzprinzipien, falls genutzt;
- Signature Elements;
- Novelty Budget;
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

Wenn eine Seite ihre Hauptaussage wesentlich über Scrolltelling, 3D oder eine andere immersive Signature Experience vermittelt, zusätzlich ein Experience Storyboard erstellen:

- narrative/inhaltliche Beats;
- Core Content pro Beat;
- Enhancement-Zweck;
- Mobile-/Touch-Pfad;
- Reduced-Motion-Pfad;
- Capability-/Failure-Fallback.

Erst freigeben, wenn die Struktur ohne visuelle Tricks verständlich bleibt und eine immersive Experience einen tragfähigen Kern besitzt.

### 4. Echter Content

`web-content`

Keine Fake-KPIs, Fake-Testimonials oder bedeutungsleere Template-Sektionen.

### 5. Implementierung

Technischen Stack aus dem Projekt übernehmen. Allgemeine Programmierregeln und bei Bedarf TDD/Code Review verwenden.

Aufwendige Experience-Layer nur aus einer bereits begründeten Design-/Storyboard-Entscheidung ableiten. Nicht GSAP, Three.js, WebGL, Canvas oder eine andere Library zuerst wählen und danach nach einem Zweck suchen.

Für relevante Signature Experiences den lokalen Progressive-Experience-Contract implementieren: Core, Enhanced, Mobile/Touch, Reduced Motion und Capability-/Failure-Fallback.

### 6. Qualitätsgates

- `accessibility-review`;
- `frontend-performance`;
- `visual-verification`.

Bei immersiven Experiences reicht der High-End-Desktop-Happy-Path nicht. Soweit lokal relevant, auch Mobile/Touch, Reduced Motion und dokumentierte Capability-/Failure-Fallbacks prüfen oder ehrlich als `NOT RUN`/`UNVERIFIED` markieren.

### 7. Unabhängiger Designreview

`web-design-review`

Der erzeugende Agent soll sein eigenes Ergebnis nicht allein freigeben.

## Gate

```text
Designidentität
+ Aufgabenfit
+ Reference-Originalität, falls externe Referenzen genutzt werden
+ begründetes Novelty Budget
+ echte Inhalte
+ Accessibility
+ Responsive Verhalten
+ Progressive-Experience-Fallbacks, falls relevant
+ Performance-Evidence
+ gerenderte Verifikation
+ unabhängiger Review
```

## Security

Neue externe Scripts, Tracking-, Analyse- oder Third-Party-Integrationen bei Bedarf mit `tool-permission-review` bzw. Security Review prüfen.
