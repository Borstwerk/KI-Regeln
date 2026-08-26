---
name: visual-verification
description: Prüft implementierte Weboberflächen im Browser auf tatsächliche visuelle, responsive und interaktive Korrektheit. Verwenden nach UI-Änderungen oder Design-/Greybox-Implementierungen sowie wenn gerenderte Evidence für Review oder Freigabe benötigt wird.
---

# Skill: Visual Verification

## Zweck

Prüfe eine implementierte Weboberfläche im Browser auf tatsächliche visuelle, responsive und interaktive Korrektheit.

## Verwenden wenn

- UI-Code umgesetzt oder verändert wurde;
- ein Design oder Greybox implementiert wurde;
- gerenderte Evidence für Review oder Freigabe benötigt wird;
- ein anderer Review-Skill Browser-/Interaktions-Evidence benötigt.

## Nicht verwenden als

- Ersatz für `motion-review` bei der fachlichen Bewertung von Timing, Easing, Spatial Continuity, Gesture oder Interruptibility;
- Ersatz für die allgemeine Design-, Accessibility- oder Performancebewertung.

Bei Motion liefert dieser Skill reproduzierbare Browser-/Viewport-/Interaktions-Evidence; die Motion-Craft-Bewertung bleibt bei `motion-review`.

## Eingaben

- lokale Design-/Produktregeln;
- betroffene Seiten oder Flows;
- laufende Anwendung;
- relevante Viewports/Browser;
- vorhandene Screenshots oder Referenzen.

## Arbeitsweise

1. Starte die Anwendung in einer geeigneten isolierten Umgebung.
2. Öffne alle geänderten oder kritischen Seiten.
3. Prüfe mindestens Desktop und Mobile sowie problematische Zwischenbreiten.
4. Prüfe relevante Zustände:
   - loading;
   - empty;
   - success;
   - error;
   - lange Inhalte;
   - Dialoge/Menüs;
   - Fokuszustände.
5. Prüfe Browserkonsole und fehlgeschlagene Requests.
6. Bediene relevante Flows per Tastatur.
7. Vergleiche gegen Greybox, Designbrief oder freigegebene Referenz.
8. Sammle geeignete Evidence: Screenshots, visuelle Tests, DOM-/Accessibility-Snapshots, Video/Screenrecording oder dokumentierte Interaktionsprüfung.
9. Bei relevanter Motion prüfe auf Anforderung normale und Reduced-Motion-Zustände sowie wiederholte/unterbrochene Interaktion; liefere die Beobachtung an `motion-review` oder den beauftragenden Skill.
10. Benenne Abweichungen offen.

## Regeln

- Code gelesen ≠ UI verifiziert.
- Screenshot ≠ Interaktion verifiziert.
- Video ≠ technische Implementierung oder Library bewiesen.
- neue visuelle Baseline ≠ Änderung automatisch korrekt.
- ungeprüfte Viewports nicht als bestanden melden.
- reale oder realistische Inhalte verwenden.

## Ausgabe

```text
Geprüfte Seiten/Flows
Viewports/Browser
Geprüfte Zustände
Konsole/Netzwerk
Tastatur/Fokus
visuelle Evidence
Abweichungen
offene Risiken
```

## Stop-Regeln

Stoppe oder melde eingeschränkte Evidence, wenn:

- die Anwendung nicht zuverlässig startbar ist;
- notwendige Daten/Zustände nicht reproduzierbar sind;
- relevante Browser oder Geräteanforderungen unbekannt sind;
- eine Abweichung eine neue Design- oder Produktentscheidung erfordert.

## Leitgedanke

> Frontendqualität wird im Browser erlebt. Deshalb muss sie dort auch geprüft werden.
