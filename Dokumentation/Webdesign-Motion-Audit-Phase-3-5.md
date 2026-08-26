# Webdesign & Motion Audit – Hardening Phase 3.5

Stand: 2026-08-26  
Base: `36b55acb51c3a98f72e340c03f2af75788c65e7f`

## Zweck

Dieser Audit hält den kalten Web-Bestand, die externe Quellenprüfung und die daraus abgeleitete Integrationsentscheidung fest. Er ist kein Qualitätsranking von Autoren und kein Lizenzgutachten. Technische Aussagen werden gegenüber Primärdokumentation priorisiert; Autorengeschmack wird nicht zur allgemeinen KI-Regel.

## 1. Kalter Capability-Bestand vor Quellenlektüre

| Dimension | Bestand vor Phase 3.5 | Befund |
| --- | --- | --- |
| Informationsarchitektur | stark vorhanden | Greyboxing, Seitenhierarchie und Contentstruktur sind explizit getrennt. |
| Layout | stark vorhanden | Layout, Rhythmus und responsives Verhalten sind etablierte Webdesign-Dimensionen. |
| Responsive Design | stark vorhanden | Breakpoints werden aus Inhalt/Verhalten statt Geräteklassen abgeleitet. |
| Typografie | stark vorhanden | Rolle, Hierarchie, Lesbarkeit und lokale Markenwahrheit sind dokumentiert. |
| Farbe | stark vorhanden | Rollen, Kontrast und Systematik sind dokumentiert. |
| Designsystem | stark vorhanden | Tokens, Komponentenverträge und lokale Wahrheit sind eigener Intent. |
| visuelle Identität | stark vorhanden | `frontend-design` trennt Art Direction von Komponentenbau. |
| Anti-Slop | stark vorhanden | generische AI-Muster und Content-Slop werden explizit geprüft. |
| Accessibility | stark vorhanden | eigener Review-Intent mit Evidence-Grenzen. |
| Frontend Performance | stark vorhanden | eigener Performance-/Jank-Intent mit Mess- und Profiling-Grenzen. |
| Visual Verification | stark vorhanden | gerenderte Browser-Evidence ist eigener Verifikationspfad. |
| Interaction Design | teilweise vorhanden | Zustände, Fokus, Pointer/Touch und Feedback existieren, aber ohne Motion-Craft-Modell. |
| Motion / Animation | echte Lücke | nur Nebenregeln; kein eigenständiger Entwurfs-, Implementierungs- oder Reviewpfad. |
| Microinteractions | echte Lücke | Feedback ist erwähnt, aber Zweck/Frequenz/Timing/Interruptibility sind nicht systematisch modelliert. |
| Gesture / Drag | echte Lücke | kein eigener Motion-Entscheidungsrahmen. |
| Scroll Animation | echte Lücke | keine lokale Auswahl- oder Reviewlogik. |
| Timeline / Choreography | echte Lücke | keine lokale Choreographie- oder Sequenzlogik. |
| Reduced Motion | teilweise vorhanden | Pflichtdimension bekannt; semantische Reduktionsstrategie fehlt. |
| Animation Performance | teilweise vorhanden | allgemeine Frontend-Performance vorhanden, aber keine Motion-spezifische Tool-/Rendering-Entscheidung. |
| Motion Review | echte Lücke | `web-design-review` deckt visuelle Qualität allgemein ab, aber nicht Motion-Vertrag, Timing, Interruptibility oder Toolfit. |
| Animation Reverse Engineering | echte Lücke | keine systematische Video-/Frame-/Timing-Rekonstruktion. |
| Toolwahl CSS / WAAPI / Motion / GSAP / Lottie / Rive / WebGL | echte Lücke | keine problemorientierte Motion-Werkzeugwahl. |

Der Befund wurde vor der externen Motion-Quellenanalyse festgehalten. Die Lücken sind daher nicht aus den Kandidatenquellen rückwärts konstruiert.

## 2. Verbindlich geprüfte Skillquellen

### Emil Kowalski – `emilkowalski/skills`

Bewerteter Repository-Zustand: `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7`.

Relevantes Artefakt: `skills/animate/SKILL.md`, beobachteter Blob `159fe0753228ab9d43fce274bd2c24433f3c4771`.

Same-state Root-Lizenz: MIT, Blob `57b46f1fd11dc62351ea548104a88aa3f659c11b`. Im bewerteten Skillpfad wurde kein abweichender Lizenzhinweis festgestellt.

Stärken: Zweck vor Motion, Frequenz, räumliche Kontinuität, Enter/Exit, Easing, Interruptibility, Microinteractions.

Nicht als universelle Wahrheit übernommen werden feste Dauergrenzen, pauschale Keyboard-Verbote, pauschale Easing-Verbote oder vereinfachte Performanceaussagen.

**Integrationsrolle:** verwendet als `reference/inspiration` für Motion Craft; keine Text-/Strukturübernahme.

### mblode – `mblode/agent-skills`

Bewerteter Repository-Zustand: `e97a3b383f5944f90d41eb92b24b4fb3b917a7f9`.

Relevantes Artefakt: `skills/ui-animation/SKILL.md`, beobachteter Blob `9c771273462e5ad42687e8d7240ef786e115fd71`.

Same-state Root-Lizenz: MIT (`LICENSE.md`), Blob `c5a1d56c6d623c72d077f8aab56b31d7dc371cbb`. Kein abweichender pfadspezifischer Lizenzhinweis im bewerteten UI-Animation-Pfad festgestellt.

Zusätzlicher Wert: Gesture/Drag, Choreographie, Reviewmodus, Screenrecording-/Frameanalyse und Reverse Engineering.

Abhängigkeitsbefund: Mehrere Motion-Craft-Heuristiken sind sehr nah an Emil-spezifischen Mustern (unter anderem Frequenz/Keyboard, kurze Routine-Motion, Easing und Interruptibility). Für diese Regeln wird mblode **nicht** als unabhängiger zweiter Konsensbeleg gezählt. Der eigenständige Mehrwert liegt vor allem in Gesture-/Choreography-/Measurement-/Reverse-Engineering-Arbeit.

**Integrationsrolle:** verwendet als `reference/inspiration` für Gesture, Choreographie und Evidence-basierte Motionanalyse; keine Text-/Strukturübernahme.

### UI UX Pro Max – `nextlevelbuilder/ui-ux-pro-max-skill`

Bewerteter Repository-Zustand: `e4f45473691e4b389519ee4bc359a3d6df666c26`.

Relevantes Artefakt: `.claude/skills/ui-ux-pro-max/SKILL.md`, beobachteter Blob `41f8e2fd7f8c568228d0b55186ebe3f7b4007377`. Root-Lizenz im bewerteten Zustand: MIT.

Stärken: breite Style-/Produkt-/Typografie-/Palette-/Chart-Taxonomie und Design-System-Auswahl.

Lokaler Befund: Der bestehende KI-Regeln-Webbereich deckt den größten Teil dieser Felder bereits fokussierter ab. Ein monolithischer Import würde Routing verschlechtern.

Design-Dials-Genealogie: Die Commit-Historie dokumentiert am 2026-07-01 ausdrücklich, dass `--variance`, `--motion` und `--density` von Taste Skills `DESIGN_VARIANCE`, `MOTION_INTENSITY` und `VISUAL_DENSITY` inspiriert wurden. UI UX Pro Max und Taste sind für diese Achsen daher keine unabhängigen Konsensbelege.

**Integrationsrolle:** Vergleichsquelle; keine eigenständige lokale Regelquelle in Phase 3.5.

### Taste Skill – `Leonxlnx/taste-skill`

Bewerteter Repository-Zustand: `ccbc15639c97057cbfcf32ecebc38ef716e4bb37`.

Relevantes Artefakt: `skills/taste-skill/SKILL.md`, beobachteter Blob `b72132fcd466da605623ffe96e370b3991fc5285`. Root-Lizenz im bewerteten Zustand: MIT.

Stärken: explizite Designrichtung und der Versuch, schwammige Vibe-Anforderungen über mehrere Achsen operationalisierbar zu machen.

Nicht übernommen werden Defaultwerte, Skalen, Font-/Layout-Geschmacksurteile oder Aussagen wie „mehr Varianz ist bei schöner Website automatisch richtiger“.

**Integrationsrolle:** verwendet als `reference/inspiration` ausschließlich für das abstrakte Konzept mehrerer expliziter Designparameter; lokale Namen, Semantik und Skalen werden eigenständig formuliert.

### GreenSock – `greensock/gsap-skills`

Bewerteter Repository-Zustand: `aed9cfd3277740755f6bfc1155c7aa645403b760`.

Beispielartefakt: `skills/gsap-core/SKILL.md`, beobachteter Blob `98639432f4112b664aa5e53cf5d8ea1a4697eff9`. Same-state Root-Lizenz: MIT.

Das Repository zerlegt GSAP sinnvoll in Core, Timelines, ScrollTrigger, React, Plugins, Performance und Utilities. Diese Taxonomie ist jedoch **kein** Grund, lokal mehrere GSAP-Skills zu erzeugen.

**Integrationsrolle:** Vergleichsquelle für Toolabdeckung. GSAP bleibt Werkzeug innerhalb `motion-implementation`; technische Toolwahrheit stammt aus GreenSock-Dokumentation, nicht aus einem lokalen GSAP-Meta-Skill.

### mthines – `mthines/agent-skills`

Bewerteter Repository-Zustand: `9b71eb1970bfad0c43cbf7be583855a754e1d185`.

Relevantes Artefakt: `skills/design/animations/SKILL.md`, beobachteter Blob `683d82f55cea4fc2e5acbe32c3d1201dbe700e2a`. Same-state Root-Lizenz: MIT, Blob `83a7bca2028ffa5d1f29e8a23a497d0b3ff9945c`.

Stärken: moderne Plattform-APIs, Interaction-Feedback, Motion/Lottie/Rive/3D und Toolbreite.

Kritik: mehrere Aussagen sind zu absolut, z. B. Composite-/GPU-Aussagen und ein starres First-Match-Toolranking. Diese Aussagen werden nicht als technische Wahrheit übernommen.

**Integrationsrolle:** Vergleichsquelle; keine eigenständige lokale Regelquelle in Phase 3.5.

## 3. Zusätzliche Vergleichsquellen

### Vercel Labs – `web-animation-design`

Das öffentlich verfügbare `web-animation-design`-Material erklärt selbst, dass es auf Emil Kowalskis „Animations on the Web“ basiert. Es ist deshalb für Emil-nahe Timing-/Frequency-/Easing-Regeln **kein unabhängiger Konsensbeleg**. Es bleibt Vergleichsmaterial und wird nicht als zusätzliche lokale Quellbasis gezählt.

### Rich Tabor – `motion-design`

Als zusätzliche Motion-Craft-Perspektive geprüft. Der Skill bestätigt Zweck- und Kontextdenken, enthält aber ebenfalls konkrete Easing-/Dauerpräferenzen. Er blieb Vergleichsmaterial; keine lokale Regel wurde allein daraus abgeleitet.

## 4. Perspektiven statt Autorenzahl

| Perspektive | Belastbare Synthese |
| --- | --- |
| Motion Craft | Motion braucht einen Zweck; räumliche Kontinuität, Feedback und nachvollziehbare Zustandsänderung sind starke Gründe. Timing/Easing/Frequenz sind kontextabhängig. Interruptibility ist bei wiederholbarer oder gestengesteuerter Motion wichtig. |
| Produktkontext | Productivity/SaaS bevorzugt meist geringe Reibung und häufigere Zurückhaltung; Marketing/Creative kann stärkere Choreographie tragen; Content/Editorial darf Lesefluss nicht stören; Kinder-/Entertainment-Produkte können höhere Bewegungsintensität tragen, aber Accessibility bleibt gleichrangig. |
| Technik | Einfache Zustandsübergänge brauchen meist keine große Library. CSS, WAAPI, View Transitions, Scroll-driven APIs, Motion, GSAP, Lottie, Rive und WebGL lösen unterschiedliche Problemklassen. Kein starres Ranking. |
| Accessibility | Reduced Motion ist eine semantische Alternative: nicht pauschal alles auf 0 ms setzen, sondern vestibulär problematische Bewegung reduzieren/ersetzen und Zustandsinformation erhalten. |
| Performance | Layout, Paint, Composite, Layerkosten, Main Thread, DOM-Größe, parallele Animationen und Hardware zählen. Eigenschaftsnamen allein beweisen keine gute Performance. |
| Review | Zweck, Kontext, Timing/Easing, Konsistenz, Interruptibility, Accessibility, Performance, Toolfit und Evidence getrennt prüfen. Review ist nicht automatisch Reparatur. |
| Reverse Engineering | Video/Screenrecording kann Timing, Sequenz, räumliche Wege und ungefähre Kurven rekonstruierbar machen; ohne Render-/Video-Evidence keine visuelle Behauptung erfinden. |

## 5. Konsens, Heuristik und Meinung

| Aussage | Einordnung | Lokale Konsequenz |
| --- | --- | --- |
| Motion soll Funktion/Orientierung/Feedback dienen oder bewusstes Delight begründen | breit gestützter Konsens | als Grundprinzip verwenden |
| „Keine Animation“ kann die beste Entscheidung sein | breit gestützter Konsens | explizite Option in Design und Review |
| Exakte Dauerobergrenzen wie 240/300 ms | kontextabhängige Heuristik | keine universelle Grenze; Frequenz, Distanz, Größe, Kontext und Tests berücksichtigen |
| Springs sind natürlicher | Autor-/Kontextheuristik | für Gesten/physikalische Modelle möglich, nicht Default |
| CSS ist immer besser | technisch fragwürdig | Problem, Kontrolle, Browserunterstützung und Profiling entscheiden |
| GSAP ist immer besser | toolspezifische Präferenz | kein Default; passend für komplexe Timeline-/Scroll-/Choreographieprobleme |
| Motion ersetzt GSAP | toolspezifisch/fragwürdig | kein universeller Ersatzanspruch |
| `transform`/`opacity` sind pauschal kostenlos | technisch falsch vereinfacht | compositor-friendly bevorzugen, aber Layer-/Paint-/Memory-/Elementzahl messen |
| `filter` ist pauschal kostenlos | technisch fragwürdig | Effekte messen, besonders große/animierte Filterflächen |
| `will-change` verbessert Performance | nur gezielte Optimierungsheuristik | erst nach konkretem Bedarf; Übergebrauch vermeiden |
| Reduced Motion = alle Animationen deaktivieren | technisch/semantisch zu grob | entfernen, reduzieren oder ersetzen; Funktion/Zustand erhalten |
| Scroll Reveal ist grundsätzlich schlecht | Designpräferenz | Kontext, Wiederholung, Lesefluss, A11y und Performance entscheiden |
| mehr Motion = moderner / weniger Motion = professioneller | Geschmacksdogma | nicht übernehmen |
| Inter ist langweilig und sollte ersetzt werden | Autorenpräferenz | lokale Brand-/Produktwahrheit entscheidet |

## 6. Technische Primärwahrheit

Für die lokale Motion-Dokumentation werden insbesondere folgende Primärquellen bevorzugt:

- MDN/Web Platform zu `prefers-reduced-motion`;
- MDN Web Animations API / `Element.animate()`;
- MDN View Transition API;
- MDN `@starting-style`;
- MDN CSS Scroll-driven Animations / `animation-timeline`;
- MDN `will-change`;
- Motion-Dokumentation für Motion-spezifische APIs;
- GreenSock-Dokumentation für GSAP;
- Rive-/Lottie-Dokumentation, wenn diese Runtimes konkret eingesetzt werden.

Primärdoku-Befunde, die lokale Mythen vermeiden:

- `prefers-reduced-motion` beschreibt das Entfernen, Reduzieren **oder Ersetzen** nicht notwendiger Bewegung; großflächiges Scaling/Panning kann vestibulär problematisch sein.
- WAAPI bietet Browser-Playback-/Timingkontrolle und ist nicht bloß „JavaScript = main-thread animation“.
- View Transitions sind eine Plattformoption für Zustands-/Dokumentübergänge, aber kein universeller Ersatz für andere Motion-Modelle.
- Scroll-driven Animations sind echte Plattformprimitive, deren Browserunterstützung je Feature geprüft werden muss.
- `will-change` ist ein Rendering-Hinweis für konkrete Probleme und keine vorsorgliche Standardregel; Übergebrauch kann Speicher-/Renderingkosten erhöhen.

## 7. Designparameter

Die abstrakte Idee expliziter Designachsen ist nützlich, wenn Stakeholder nur „modern, aber nicht verspielt“ formulieren. Lokal werden daraus **keine** Taste-/UI-UX-Pro-Max-Slider kopiert.

Projektbezogene Parameter können beispielsweise sein:

- **visuelle Varianz** – wie stark Layout, Formen und Komposition vom neutralen Systemraster abweichen dürfen;
- **Bewegungsintensität** – wie häufig, räumlich stark und choreographiert Motion eingesetzt werden darf;
- **Informationsdichte** – wie kompakt Inhalt und Interaktion auf einer Fläche organisiert werden.

Die Parameter haben keine universellen Defaultwerte. Produkt, Brand, Zielgruppe, Aufgabe, Nutzungshäufigkeit und Accessibility bestimmen die Richtung.

## 8. Lokales Motion-Kompetenzmodell

Der Audit bestätigt drei eigenständige Intents:

1. **`motion-design`** – entscheidet *ob, warum und wie intensiv* Bewegung sinnvoll ist; definiert Motion-Vertrag, Timing-/Easing-Charakter, räumliche Kontinuität, Microinteractions, Gesture-Verhalten und Reduced-Motion-Semantik.
2. **`motion-implementation`** – setzt eine definierte Motion technisch um und wählt CSS/WAAPI/View Transitions/Motion/GSAP/Lottie/Rive/WebGL problemorientiert; Profiling und Browserunterstützung sind Gates.
3. **`motion-review`** – prüft bestehende Motion unabhängig auf Zweck, Kontext, Timing, Konsistenz, Interruptibility, Accessibility, Performance, Toolfit und Evidence; Review ist nicht automatisch Redesign oder Implementierung.

Ein vierter Intent `motion-reverse-engineering` wird **nicht** angelegt. Reverse Engineering aus Video/Screenrecording ist eine spezialisierte Evidence-/Analyseform innerhalb `motion-review`; bei tatsächlicher Implementierung kann das Ergebnis anschließend an `motion-implementation` übergeben werden. Damit entsteht kein künstlicher Routingzweig für eine seltenere Unteraufgabe.

## 9. Schutz bestehender Web-Intents

- visuelle Identität / Art Direction bleibt `frontend-design`;
- Designsystem/Tokens bleiben `design-system`;
- statische Designqualität bleibt `web-design-review`;
- Accessibility ohne Motion-Fokus bleibt `accessibility-review`;
- allgemeines Jank-/Frontend-Performanceproblem bleibt `frontend-performance`;
- Render-/Screenshot-/Browser-Evidence bleibt `visual-verification`;
- Motion-Design, Motion-Implementierung und Motion-Review werden daneben eng geroutet.

## 10. Integrationsentscheidung

Tatsächlich als lokale methodische Quellen verwendet werden:

- Emil Kowalski `skills/animate/SKILL.md` – Motion Craft;
- mblode `skills/ui-animation/SKILL.md` – Gesture/Choreographie/Reverse Engineering;
- Taste `skills/taste-skill/SKILL.md` – abstraktes Konzept mehrerer expliziter Designparameter.

UI UX Pro Max, GreenSock Skills, mthines, Vercel `web-animation-design` und Rich Tabor bleiben Vergleichsquellen bzw. technische Radar-/Toolquellen. Technische GSAP-/Motion-/Web-API-Aussagen werden über Primärdokumentation verifiziert.

Alle drei tatsächlich verwendeten GitHub-Artefakte werden vor der Motion-Regelintegration source-spezifisch in `Dokumentation/upstream-sources.yml` und `Dokumentation/upstream-provenance.yml` gebunden. Die geplante lokale Nutzung ist `reference/inspiration`, `concepts/methods-only`, `not-relied-on`; es wird kein Fremdtext vendort und keine Redistributionslizenz für die lokalen Formulierungen benötigt.
