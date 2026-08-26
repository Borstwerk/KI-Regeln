---
name: motion-review
description: Prüft vorhandene Web-Motion unabhängig auf Zweck, Produktkontext, Timing, räumliche Kontinuität, Interruptibility, Accessibility, Performance und Toolangemessenheit. Verwenden für Reviews bestehender Animationen; Video-/Frameanalyse ist dabei ein Evidence-Modus, kein eigener Designauftrag.
---

# Skill: Motion Review

## Zweck

Prüfe vorhandene Web-Motion unabhängig und evidenzbezogen, ohne aus einem Review ungefragt ein Redesign oder eine Reimplementation zu machen.

## Verwenden wenn

- eine bestehende Animation oder Mikrointeraktion bewertet werden soll;
- Motion vor Freigabe unabhängig geprüft wird;
- Timing, Easing, Spatial Continuity oder Choreographie auffällig wirken;
- Gesture-/Drag-/Interruptibility-Verhalten geprüft werden soll;
- Reduced Motion, Fokus oder Motion-spezifische Accessibility Teil der Frage ist;
- ein Video, eine Framefolge oder Browseraufnahme zur Rekonstruktion vorhandener Motion analysiert wird;
- die Angemessenheit der technischen Mechanik beurteilt werden soll.

## Nicht verwenden als

- allgemeine Art Direction – dafür `frontend-design`;
- Entwurf einer neuen Motion ohne bestehenden Gegenstand – dafür `motion-design`;
- automatische technische Umsetzung der Funde – dafür nur bei separatem Auftrag `motion-implementation`;
- vollständigen Accessibility- oder Performance-Audit der gesamten Anwendung.

## Evidence zuerst

Kläre, welche Evidenz tatsächlich vorliegt:

- laufender Browser / reproduzierbare Interaktion;
- Video oder Screenrecording;
- Framefolge;
- Screenshots;
- Quellcode;
- Motion-Spezifikation oder Designquelle;
- Performanceprofil.

Ein statischer Screenshot beweist keine Timing-, Easing- oder Interruptibility-Eigenschaft. Quellcode beweist nicht automatisch das gerenderte Verhalten. Ohne erforderliche visuelle oder Laufzeit-Evidence bleibt der betroffene Reviewteil `partial` oder offen.

## Arbeitsweise

### 1. Reviewgegenstand und Produktkontext fixieren

Notiere Interaktion, Nutzerziel, Häufigkeit, Plattform/Input und vorhandene Design-/Motion-Regeln. Wenn lokale Regeln existieren, haben sie Vorrang vor persönlichen Vorlieben des Reviewers.

### 2. Zweck prüfen

Frage für jede relevante Bewegung:

- Welchen Zustand oder Zusammenhang erklärt sie?
- Gibt sie hilfreiches Feedback?
- Führt sie Aufmerksamkeit mit einem legitimen Produktzweck?
- Oder ist sie bloß dekorative Verzögerung?

`Keine Animation` ist ein zulässiger Reviewbefund, aber kein reflexartiger Minimalismus.

### 3. Craft getrennt bewerten

Prüfe nachvollziehbar:

- Timing und Easing im konkreten Kontext;
- Spatial Continuity zwischen Quelle und Ziel;
- Choreographie und Priorität mehrerer Bewegungen;
- Konsistenz verwandter Interaktionen;
- Frequenz und wiederholte Nutzung;
- Microinteraction-Feedback.

Keine autorenspezifische Dauer, Kurve oder Geschmacksregel als universelle Norm verwenden.

### 4. Interruptibility und Gesten prüfen

Bei ausführbarer Evidence teste:

- erneute Eingabe während der Bewegung;
- gegenteilige Eingabe;
- Drag-Richtungswechsel und Loslassen;
- Abbruch, Navigation oder Unmount;
- plausiblen Zwischenzustand;
- Touch-/Pointer- sowie Fokus-/Tastaturpfade.

Fehlt ausführbare Evidence, benenne diese Punkte als unverified statt sie aus Code oder Video zu erfinden.

### 5. Accessibility prüfen

Motion-spezifisch mindestens betrachten:

- `prefers-reduced-motion` und sinnvolle Alternative;
- großflächiges Panning, Zooming, Parallax oder starke Skalierung;
- dauerhaft wiederholte Animationen;
- Information, die nur durch Bewegung vermittelt wird;
- Focus/Keyboard;
- Touch/Pointer;
- häufig wiederholte Interaktionen.

Für eine vollständige Accessibility-Prüfung mit `accessibility-review` komponieren.

### 6. Performance nur mit passender Evidence bewerten

Quellcode kann Risiken zeigen, aber kein reales Jank beweisen. Keine Performanceursache allein aus Librarywahl oder animierter Property ableiten.

Bei Performanceclaims berücksichtige unter anderem Layout, Paint, Composite, Layer-Speicher, Main Thread, Scroll, Elementzahl, DOM-Größe und Hardware. Definitive Aussagen benötigen Messung/Profiling; bei breiter Diagnose mit `frontend-performance` komponieren.

### 7. Toolangemessenheit prüfen

Bewerte, ob die gewählte Mechanik zur Aufgabe und zum Projekt passt. Keine Library pauschal bevorzugen.

- Eine einfache Transition kann mit einer schweren neuen Abhängigkeit überkonstruiert sein.
- Eine komplexe Timeline kann eine bewusst gewählte Orchestrierungslösung rechtfertigen.
- Bestehende Projektintegration, Browserziele, Wartbarkeit und Accessibility zählen mit.

Review der Toolwahl ist nicht automatisch Auftrag zum Austausch der Technik.

## Reverse Engineering als Evidence-Modus

Video-/Frameanalyse ist ein Modus dieses Skills, wenn eine bestehende Motion rekonstruiert werden soll.

Arbeite dann beobachtungsnah:

1. Trigger und sichtbare Zustände identifizieren.
2. Bewegungsreihenfolge und räumliche Beziehungen beschreiben.
3. beobachtbare Dauer-/Verlaufseigenschaften nur soweit die Aufnahme sie trägt ableiten;
4. Unterbrechung oder Reduced Motion nur bewerten, wenn entsprechende Evidence vorhanden ist;
5. Beobachtung, Interpretation und technische Vermutung klar trennen.

Ein Video beweist nicht automatisch, welche Library oder CSS-Eigenschaft verwendet wurde.

## Ausgabe

```text
Review-Scope und Evidence
Gesamturteil
Hohe / mittlere / kleine Funde
Motion Craft
Gesture / Interruptibility
Accessibility
Performance-Evidence
Toolangemessenheit
Starke Entscheidungen, die erhalten bleiben sollten
Unverified / fehlende Evidence
```

Jeder relevante Fund enthält:

- Fundstelle oder Interaktion;
- Beobachtung;
- Auswirkung;
- Evidenz;
- empfohlene Richtung.

## Stop-Regeln

- Keine visuelle Freigabe ohne passende Render-/Video-Evidence behaupten.
- Keine Performanceursache ohne Messung als bewiesen darstellen.
- Keine technische Library aus einem Video erraten.
- Kein ungefragtes Redesign oder Reimplementation beginnen.
- Keine Autorenpräferenz als universelle Qualitätsnorm behandeln.

## Komposition mit anderen Skills

- Browser-/Viewport-Nachweis: `visual-verification`;
- umfassende Accessibility: `accessibility-review`;
- breite Performanceanalyse: `frontend-performance`;
- neue Motion gestalten: `motion-design`;
- bestätigten Fix implementieren: `motion-implementation`.

## Near Misses

Nicht triggern für:

- allgemeine Landingpage-Art-Direction;
- statisches Layoutreview ohne Motionfrage;
- reine WCAG-Prüfung;
- allgemeines Performanceprofiling ohne Motionbezug;
- Auftrag, eine bereits spezifizierte Animation lediglich zu implementieren.

## Leitgedanke

> Motion Review trennt Beobachtung, Bewertung und technische Vermutung – und ändert erst etwas, wenn Änderung wirklich beauftragt ist.
