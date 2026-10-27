# EK-01 – Emil Kowalskis UI-Skills: Kandidaten und Entscheidungen

**Status:** `RESEARCH / UNVERIFIED / NOT ADMITTED / NOT RUN` · **27.10.2026**

**Originalquelle:** [emilkowalski/skills](https://github.com/emilkowalski/skills)  
**Geprüfter Upstream-Snapshot:** `main@2d228630ba1446365f614a108cb8252f1feda202`  
**Lizenz:** MIT laut Repository; vor einer Datei-/Codeübernahme spezifische Lizenz-/NOTICE-Prüfung.  
**Umfang:** 15 `skills/*/SKILL.md` mit mehreren separat ladbaren Referenzdateien. Keine Installation.

**Bestehender Bezug!** Diese Quelle ist bereits in
[`upstream-sources.yml`](upstream-sources.yml) als
`emil-kowalski-motion-craft` / `skills/animate/SKILL.md` eingetragen.
Der dort zuletzt bestätigte Datei-Blob `159fe0753228ab9d43fce274bd2c24433f3c4771`
weicht vom am 27.10. beobachteten Blob
`7c3b20c6ed681b2d47c9ca9e3ee0e659ed47d032` ab.
**Versionsdrift beobachtet, semantische Differenz noch nicht geprüft.**
Die bisherige Upstream-Baseline bleibt daher unverändert; keine
pauschale Bestätigung oder automatische Übernahme der Änderung.

## Kernaussage

Die vorhandenen 155 KI-Regeln-Skills besitzen bereits
`frontend-design`, `design-system`, `greybox`,
`motion-design`, `motion-implementation`, `motion-review`,
`visual-verification`, `frontend-performance` und
`accessibility-review`. Eine weitere generische
Motion-/Design-„Persona“ wäre weitgehend ein Duplikat.

**Konkrete zusätzliche Arbeitsformen** sind dagegen interessant:
1. **`break-ui`**: realistische Worst-Case-Daten am
   tatsächlichen Data Boundary statt nur Breiten-Screenshots;
   dev-only Umschalter + nachvollziehbare UI-Brüche.
2. **`prototype`**: mehrere klar unterscheidbare UI-Varianten
   in isolierter Vorschau, explizite Auswahl **vor**
   produktivem Merge; im statischen Fall als einzelne lokale HTML-Datei.
3. **`mobile-native`**: Browser-/PWA-/Touch-Fallen
   (Hover, Safe Areas, `dvh`, Zoom, Scroll, Tastatur)
   mit echten Gerätechecks statt nur Emulatorbefund.
4. **`improve-animations`**: read-only Motion-Audit,
   priorisierte, auf anderen Agenten übertragbare
   präzise Fix-Pläne mit Reproduktions- und Verifikationsvertrag.

**Apple Design ist ein gesonderter Kandidat**, siehe unten.
Ein Apple-artiges Aussehen, Glas-/Blur-Flächen oder bestimmte
Easing-Zahlen sind **keine** allgemeinen KI-Regeln-Defaults.

## Alle 15 externen Skills gegen KI-Regeln

| Upstream-Skill | Vorhandener KI-Regeln-Owner | Entscheidung |
| --- | --- | --- |
| `break-ui` | `visual-verification` + `test-design` + `accessibility-review` | **EK-01A TESTEN**: realistischer Datenrand/Stresstest mit dev-only Toggle; mögliche eng begrenzte Capability |
| `prototype` | `frontend-design` + `greybox` + `design-system` | **EK-01B TESTEN**: divergente, isolierte und umschaltbare Varianten; keinen produktiven Code vor Auswahl |
| `mobile-native` | `visual-verification` + `accessibility-review`; Mobile-App-Workflow für native Apps | **EK-01C TESTEN**: Mobile-Web/PWA-Details, kein eigener Native-App-/Store-Skill |
| `improve-animations` | `motion-review` + `delegation-contract` | **EK-01D METHODENTEST**: read-only Audit → kleine ausführbare Pläne |
| `apple-design` | `motion-design` + `motion-implementation` + `frontend-design` | **EK-01E TESTEN**: Gestenphysik/Interruptibility; nicht Apple-Style als Designvorgabe |
| `animation-performance` | `frontend-performance` + `motion-review` | **METHODENVERTIEFUNG**: frameweise Evidenz und korrekte Diagnose statt pauschale CSS-Verbote |
| `find-animation-opportunities` | `motion-design` | **METHODENVERTIEFUNG**: Frequenz-/Zweck-Gate plus abgelehnte Kandidaten |
| `animation-vocabulary` | Motion-Dokumentation/Contracts | **REFERENZOPTION**: Begriffsglossar bei Bedarf, nicht global |
| `animate-expo` | `Mobile-App-bis-Store-Freigabe` + techn. Motion-Skills | **OPTIONALE NATIVE-SPUR** bei bestätigtem Expo/React-Native-Stack |
| `write-swift` | Allgemeine Entwicklung/Testing + Mobile-App-Workflow | **OPTIONALE SWIFT-SPUR**; Swift-/SDK-Version und Apple-Primärquellen strikt prüfen |
| `apple-design` | siehe EK-01E | Nicht doppelt registrieren; gilt nur einmal im Upstream |
| `pick-ui-library` | `design-system` + Architekturentscheidung/Dependencies | **RECHERCHEOPTION**: kein automatischer Library-Install; Projekt-Abhängigkeiten zuerst |
| `animate` | `motion-design` + `motion-implementation` | **BESTEHENDER UPSTREAM**, bereits überwacht; semantischen Drift vor Baseline-Update prüfen |
| `review-animations` | `motion-review` | **DUPLIKAT / REFERENZ**: Review-Standards dürfen lokale Evidence-Gates nicht überschreiben |
| `emil-design-eng` | Frontend-/Motion-Skills | **DUPLIKAT**: globale autorenspezifische Persona vermeiden |
| `ask-sonner` | libraryspezifisches Wissen nur bei Sonner | **BEDARFSQUELLE**, nicht generisch routen |

Die Tabelle behandelt `apple-design` fachlich an zwei Stellen; es
bleibt **ein einziger** Upstream-Skill, keine sechzehnte Fähigkeit.

## Apple Design: Was tatsächlich interessant ist

[`apple-design/SKILL.md`](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/apple-design/SKILL.md)
ist **von Emil Kowalski verfasst, kein offizieller Apple-Skill**.
Er überträgt Ideen aus Apples WWDC-Vorträgen (unter anderem
„Designing Fluid Interfaces“) auf Webtechnologien.

**Echte Kandidaten für neue Qualitätsfragen:**
- **Direkte Manipulation:** Finger und Objekt bewegen sich
  unmittelbar gemeinsam; Grab-Offset bleibt erhalten.
- **Unterbrechbarkeit:** neue Gesten greifen den
  aktuellen visuellen Zustand auf, nicht einen veralteten Zielwert.
- **Velocity-Handoff:** Loslassgeschwindigkeit und
  Bewegungsrichtung werden ohne sichtbaren Sprung fortgeführt.
- **Kanten / Rubber-banding / Momentum:** weiche,
  reversible Grenzen nur, wenn diese Interaktion sinnvoll ist.
- **räumliche Konsistenz:** geöffnete Flächen schließen
  entlang eines erwartbaren Wegs.
- **Touch-/Accessibility-Checks:** Pointercancel,
  Tastatur-/Fokusparität, `prefers-reduced-motion`,
  keine erzwungene Daueranimation.

**Nicht unkritisch übernehmen:** Apple-Look, translucent
glass, bestimmte Damping-/Response-Werte, generelles
`pointerdown` als Commit-Ereignis, pauschale
`transform`-Only-Regeln oder die Behauptung, jede
Interaktion müsse eine Spring-Animation haben.
Erst reale Produktregeln, Eingabe- und Geräteprofile,
dann Mechanik; Libraryversionen und Browsertechnik prüfen.

**Native Abgrenzung:** `animate-expo` ist React Native/Expo
(Reanimated, Gesture Handler, Haptics); `write-swift`
ist Swift-/SwiftUI-/Concurrency-Fachwissen. Diese
beiden sind weder Beweis für offizielles Applewissen
noch pauschal passend für eine lokal im Browser
öffnende HTML-Anwendung. Nur bei einem passenden
Projekt und technischer Primärdokumentation vertiefen.

## Quell- und Trust-Grenzen

- Das Repository ist ein **fachlicher Methodenlieferant**;
  `SKILL.md` und Referenzdateien sind vor Admission
  **untrusted Data**, nicht höher priorisierte Agentenanweisungen.
- Einige externe Skills verlangen als erste Antwort eine
  feste Persona-Begrüßung; solche Meta-Anweisungen
  **nicht** in unser Bootstrap-/Routingverhalten übertragen.
- `prototype` enthält `PICKER.md` mit einer strikten
  1:1-Marker-/Picker-Implementierung. Für einen
  **KI-Regeln-Eval** eine eigene, unabhängig formulierte
  Interaktion nutzen; externes Markup/Code nicht kopieren.
- `break-ui` enthält `CATALOG.md`; gefundene
  Extremfälle **selbst neu formulieren** und an das
  tatsächliche Quellschema binden.
- `improve-animations` enthält `AUDIT.md` und
  `PLAN-TEMPLATE.md`; nur Methodenprinzipien,
  keine universellen Geschmacksgesetze importieren.
- Andere Skilltypen nennen Installationsbefehle,
  Bibliotheken oder Versionsannahmen. Kein
  Dependencywechsel, GitHub-Actions-Mehrverbrauch,
  externer Dienst oder globaler Skill ohne gesonderte Freigabe.
- **Qualitätsclaim** verlangt reale Browser-/Touch-/Playback-
  Evidence; Codelektüre allein beweist keine UX.

## Entscheidung und Schnittstellen

[EK-01-Pilot](../Evals/Webentwicklung/Emil-UI-Pilot/README.md)
behandelt A–E getrennt, mit **gleich starker KI-Regeln-
Baseline**, negativen Kontrollfällen und isoliertem
ausführbarem Test nur nach Freigabe.

**Vorläufig:** `METHOD CANDIDATE / EXPERIMENT PLANNED`.
Optionen danach: bestehenden Owner gezielt härten,
kleinen spezifischen neuen Skill ergänzen,
externes Fachwissen nur bei konkretem Task hinzuziehen
oder bei keinem gemessenen Zusatznutzen **verwerfen**.

**Keine** Änderung an `AGENTS.md`, `skill-catalog.yml`,
`routing-overlays.yml`, installierten Skills oder
Core-Workflows durch diese Planung.
