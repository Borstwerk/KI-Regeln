---
name: motion-design
description: Definiert Zweck, Intensität und Verhalten von Web-Motion vor der technischen Umsetzung. Verwenden für Mikrointeraktionen, Zustandswechsel, Gesten und Choreographie, wenn geklärt werden soll, ob Bewegung sinnvoll ist und wie sie sich im Produktkontext verhalten soll.
---

# Skill: Motion Design

## Zweck

Definiere, **ob**, **warum** und **wie** eine Webinteraktion Bewegung verwendet, bevor ein konkretes Animationswerkzeug festgelegt wird.

## Verwenden wenn

- eine Mikrointeraktion oder Zustandsänderung gestaltet werden soll;
- Timing, Easing, Bewegungsintensität oder räumliche Kontinuität begründet werden müssen;
- Drag-, Swipe- oder andere Gesture-Verläufe entworfen werden;
- mehrere Bewegungen choreographiert werden müssen;
- bestehende Art Direction um eine Motion-Sprache ergänzt wird;
- ausdrücklich geklärt werden soll, ob eine Animation überhaupt sinnvoll ist.

## Nicht verwenden als

- Ersatz für `frontend-design` bei allgemeiner visueller Art Direction;
- technische Umsetzung einer bereits definierten Animation – dafür `motion-implementation`;
- unabhängigen Review vorhandener Motion – dafür `motion-review`;
- allgemeinen Accessibility- oder Performance-Audit.

## Vor Beginn klären

1. Produkt und Interaktionsziel;
2. Nutzeraktion und Zustandsänderung;
3. Häufigkeit der Interaktion;
4. vorhandene Brand-/Design-/Motion-Regeln;
5. Eingabemodi: Pointer, Touch, Tastatur, Scroll;
6. relevante Accessibility- und Plattformgrenzen;
7. ob eine visuelle Referenz oder bestehende Bewegung als Quelle dient.

## Arbeitsweise

### 1. Zweck benennen

Formuliere in einem Satz, was Motion hier leisten soll. Typische Zwecke sind Orientierung, Ursache/Wirkung, Statusfeedback, räumliche Beziehung oder Fokusführung.

Kann kein belastbarer Zweck benannt werden, prüfe ausdrücklich die Option **keine Animation**.

### 2. Produktkontext und Frequenz berücksichtigen

Bewerte, wie oft die Interaktion auftritt und wie viel Aufmerksamkeit sie verträgt. Hochfrequente Bedienvorgänge dürfen nicht durch wiederholtes Spektakel oder unnötige Verzögerung belastet werden.

### 3. Anforderungen operationalisieren

Wenn Vibe-Wörter zu unpräzise sind, beschreibe wenige projektbezogene Parameter, zum Beispiel:

- visuelle Varianz;
- Bewegungsintensität;
- Informationsdichte.

Keine verpflichtende Skala, keine universellen Defaultwerte. Brand- und Projektvorgaben haben Vorrang.

### 4. Bewegungslogik definieren

Beschreibe:

- Start- und Endzustand;
- räumlichen Ursprung und Ziel;
- Reihenfolge bei mehreren Elementen;
- Beziehungen zwischen gemeinsamen Elementen;
- Verhalten bei wiederholter oder gegenteiliger Eingabe.

Choreographie erklärt Beziehungen; sie ist kein Selbstzweck.

### 5. Timing und Easing als Hypothese formulieren

Leite Timing und Easing aus Distanz, Größe, Frequenz, Interaktionsart und Produktcharakter ab. Vermeide autorenspezifische Zahlen oder Kurven als universelle Wahrheit.

Konkrete Werte dürfen vorgeschlagen werden, müssen aber als kontextbezogene Startwerte statt Naturgesetz behandelt werden.

### 6. Gesten und Interruptibility entwerfen

Bei kontinuierlicher Eingabe kläre Constraints, Richtungswechsel, Loslassen, Velocity und Abbruchpfade.

Für jede interaktive Motion kläre außerdem, was bei erneuter Aktion während der Bewegung passiert. Nutzer dürfen nicht auf eine dekorative Sequenz warten müssen, bevor das Interface wieder reagiert.

### 7. Reduced Motion mitentwerfen

Definiere eine Alternative für `prefers-reduced-motion`, wenn relevante Bewegung vorhanden ist. Die Alternative kann entfernen, reduzieren oder ersetzen. Zweck und notwendige Information bleiben erhalten.

Vermeide insbesondere unnötige großflächige Zoom-/Pan-/Parallax-Bewegung und dauerhaft wiederholte Motion.

### 8. Handoff als Motion-Contract

Übergib der technischen Umsetzung mindestens:

- Zweck;
- Trigger;
- Start-/Endzustände;
- räumliche Beziehung;
- Timing-/Easing-Absicht;
- Interruption-/Abbruchverhalten;
- Gesture-Regeln;
- Reduced-Motion-Variante;
- offene Punkte und Evidence-Annahmen.

Werkzeugnamen gehören nur hinein, wenn der Projektkontext sie bereits vorgibt oder eine technische Eigenschaft unverzichtbar ist.

## Evidence-Grenze

Ein Motion-Contract kann ohne Browser entstehen. Behaupte aber ohne Render/Video nicht, dass eine konkrete Animation bereits visuell natürlich, ruckelfrei oder browserübergreifend korrekt **ist**.

## Ausgabe

```text
Kontext und Zweck
Motion-Entscheidung: animieren / reduzieren / keine Animation
Motion-Contract
Gesture- und Interruptibility-Regeln
Reduced-Motion-Variante
Offene technische Entscheidungen
Benötigte Evidence
```

## Komposition mit anderen Skills

- allgemeine Art Direction: `frontend-design` zuerst oder parallel;
- technische Umsetzung: anschließend `motion-implementation`;
- unabhängiger Review: `motion-review`;
- umfassender Accessibility-Audit: `accessibility-review`;
- Render-/Viewport-Nachweis: bei Bedarf `visual-verification`.

## Near Misses

Nicht triggern für:

- eine statische Landingpage-Art-Direction ohne Motion-Frage;
- reinen CSS-Abstands-/Layoutfix;
- reine WCAG-Prüfung ohne Motion-Schwerpunkt;
- allgemeine Frontendperformance-Diagnose;
- bloße Umsetzung eines bereits vollständigen Motion-Contracts.

## Leitgedanke

> Die richtige Motion ist die Bewegung, die eine Aufgabe verständlicher oder unmittelbarer macht – einschließlich der Entscheidung, sie wegzulassen.
