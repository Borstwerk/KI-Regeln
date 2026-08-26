---
name: motion-implementation
description: Setzt eine definierte Web-Motion technisch um und wählt dafür kontextabhängig zwischen CSS, Webplattform-APIs und passenden Libraries. Verwenden bei konkreter Implementierung von Transitions, Timelines, Gesten, Layout- oder Scroll-Animationen, nicht für allgemeine Art Direction oder reinen Review.
---

# Skill: Motion Implementation

## Zweck

Übersetze einen begründeten Motion-Contract in eine wartbare technische Umsetzung, ohne ein Animationswerkzeug zum Dogma zu machen.

## Verwenden wenn

- eine bereits definierte Animation implementiert werden soll;
- CSS Transition/Animation, WAAPI, View Transitions oder Scroll-driven Animations konkret gegeneinander abgewogen werden müssen;
- Motion, GSAP oder eine andere vorhandene Library technisch passend eingesetzt werden soll;
- Gesture-, Timeline-, Layout- oder Scroll-Choreographie umgesetzt wird;
- eine bestehende Motion-Implementierung gezielt technisch korrigiert werden soll.

## Nicht verwenden als

- allgemeine Art Direction – dafür `frontend-design`;
- Entwurf von Zweck und Verhalten einer noch undefinierten Motion – dafür `motion-design`;
- unabhängigen Review – dafür `motion-review`;
- allgemeine Frontendperformance-Diagnose ohne konkrete Motion-Aufgabe.

## Eingaben

Bevorzugt liegt ein Motion-Contract vor mit:

- Trigger und Zuständen;
- Zweck;
- räumlicher Beziehung;
- Timing-/Easing-Absicht;
- Interruption-/Gesture-Regeln;
- Reduced-Motion-Variante;
- Browser-/Stack-/Dependency-Grenzen.

Fehlt ein Detail, erfinde keine Produktentscheidung. Implementiere nur den ausreichend definierten Teil oder markiere die offene Designentscheidung.

## Arbeitsweise

### 1. Projektkontext zuerst

Prüfe vorhandenen Stack, Dependencies, Browserziele, Komponentenmodell und bestehende Motion-Konventionen. Eine bereits gut integrierte Lösung kann wichtiger sein als eine theoretisch kleinere neue Dependency.

### 2. Einfachste ausreichende Mechanik wählen

Es gibt **kein starres Toolranking**. Prüfe die Aufgabe gegen ihre tatsächlichen Anforderungen.

Mögliche Kandidaten:

- CSS Transitions für einfache deklarative Zustandswechsel;
- CSS Animations für deklarative Keyframe-Sequenzen;
- `@starting-style` für unterstützte Eintritts-/Initialzustände;
- Web Animations API, wenn JavaScript Playback, Timing oder Laufzeitkontrolle braucht;
- View Transition API für passende Zustands-/Navigationsübergänge;
- CSS Scroll-driven Animations für passende scrollgebundene Timelines;
- Motion bei Aufgaben, die von dessen vorhandener Projektintegration, Layout-/Gesture-Abstraktionen oder Orchestrierung profitieren;
- GSAP bei Aufgaben, die von dessen Timeline-/Scroll-Orchestrierung oder bestehender Projektintegration profitieren;
- spezialisierte Asset-/Rendering-Runtimes nur, wenn das Medien- oder Interaktionsmodell sie tatsächlich benötigt.

Eine einfache Hover- oder State-Transition rechtfertigt nicht automatisch eine zusätzliche Library. Eine komplexe Timeline ist umgekehrt kein Anlass, dogmatisch CSS-only zu bleiben.

### 3. Primärdokumentation für technische Behauptungen

Wenn eine Implementierung von konkretem API-Verhalten, Browserunterstützung oder Library-Funktionalität abhängt, prüfe aktuelle Primärdokumentation.

Für den Webplattform-Scope dieses Skills sind insbesondere relevant:

- MDN Web Animations API;
- MDN `@starting-style`;
- MDN View Transition API;
- MDN CSS scroll-driven animations;
- MDN `prefers-reduced-motion`.

Bei Motion oder GSAP gelten die jeweiligen offiziellen Dokumentationen als technische Referenz. Agent-Skills sind dafür keine technische Source of Truth.

### 4. Zustands- und Interaktionslogik schützen

Die Animation darf die fachliche Zustandsmaschine nicht ersetzen oder verdecken.

Prüfe:

- Start-/Endzustand auch ohne Animation korrekt;
- erneute oder gegenteilige Eingabe während der Bewegung;
- Cleanup bei Unmount, Navigation oder Abbruch;
- Fokus- und Tastaturzustand;
- Touch-/Pointerpfade;
- keine Blockade wichtiger Interaktion nur für dekorative Sequenzen.

### 5. Reduced Motion implementieren

Implementiere eine sinnvolle Reduced-Motion-Variante. Das kann Entfernen, Reduzieren oder Ersetzen bedeuten; notwendige Information und Zustandsfeedback bleiben erhalten.

Keine pauschale `0ms`-Regel anwenden, wenn dadurch Orientierung, Fokuswechsel oder Statusverständnis schlechter werden.

### 6. Performance hypothesengeleitet behandeln

Vermeide Kurzformeln wie:

- GPU = schnell;
- `transform` = kostenlos;
- `filter` = billig;
- `will-change` überall;
- CSS = immer schneller;
- JavaScript = langsam;
- GSAP = immer besser;
- Motion = immer kleiner oder besser.

Relevante Kosten können Layout, Paint, Composite, Layer-Speicher, Main Thread, Scroll, Elementzahl, DOM-Größe und Hardware betreffen.

Wenn Performance Teil des Auftrags ist:

1. reales Problem reproduzieren;
2. relevante Interaktion messen;
3. Ursache im Profiler lokalisieren;
4. Änderung durchführen;
5. erneut messen.

Ohne Messung keine definitive Performanceverbesserung behaupten. Für breitere Diagnose mit `frontend-performance` komponieren.

### 7. Browser-/Visual-Evidence prüfen

Code-Inspection beweist nicht automatisch das gerenderte Ergebnis.

Für nichttriviale Motion sollten, sofern Capability vorhanden:

- relevante Interaktionen ausgeführt werden;
- normale und Reduced-Motion-Zustände geprüft werden;
- Unterbrechung/repeated input getestet werden;
- relevante Viewports betrachtet werden.

Wenn Browser-/Renderzugriff fehlt, Implementation als Codezustand liefern und visuelle Verifikation ausdrücklich offenlassen.

## Ausgabe

```text
Motion-Contract / Annahmen
Gewählte Mechanik und Begründung
Implementierungsänderungen
Reduced-Motion-Pfad
Interruption-/Cleanup-Verhalten
Technische Primärquellen bei API-Claims
Ausgeführte Verifikation
Offene Render-/Performance-Evidence
```

## Komposition mit anderen Skills

- fehlender Motion-Contract: `motion-design`;
- unabhängige Bewertung des Ergebnisses: `motion-review`;
- allgemeine Performanceursache: `frontend-performance`;
- Browser-/Viewport-Evidence: `visual-verification`;
- umfassende WCAG-Prüfung: `accessibility-review`.

## Near Misses

Nicht triggern für:

- allgemeine Landingpage-Gestaltung;
- statische Layout-/Typografieentscheidung;
- reine WCAG-Prüfung;
- allgemeine „Seite ist langsam“-Diagnose ohne Motionbezug;
- reine Beurteilung vorhandener Animation ohne Änderungsauftrag.

## Leitgedanke

> Wähle Technik nach Motion-Contract, Projektkontext und nachweisbaren Anforderungen – nicht nach Library-Loyalität.
