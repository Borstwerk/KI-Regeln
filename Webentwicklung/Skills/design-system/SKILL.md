---
name: design-system
description: Verdichtet eine freigegebene Designrichtung in ein konsistentes System aus Tokens, Typografie, Farben, Flächen, Abständen und Komponentenprinzipien. Verwenden bei mehreren Seiten oder Komponenten mit wiederkehrenden visuellen Entscheidungen oder beim Aufbau einer dokumentierten UI-Grundlage.
---

# Skill: Design System

## Zweck

Verdichte eine freigegebene Designrichtung in ein konsistentes, lokal dokumentierbares System aus Tokens, Typografie, Farben, Flächen, Abständen und Komponentenprinzipien.

## Verwenden wenn

- mehrere Seiten oder Komponenten konsistent aufgebaut werden sollen;
- dieselben visuellen Entscheidungen wiederkehren;
- eine `DESIGN.md`, Token-Datei oder UI-Grundlage vorbereitet wird.

## Nicht verwenden als

- Ersatz für eine noch ungeklärte Designrichtung;
- Anlass, jede mögliche Zahl und Variante zu abstrahieren;
- Lizenz für ein überdimensioniertes Komponentenframework;
- Ersatz für den Entwurf von Motion-Zweck, Gesten oder Choreographie – dafür `motion-design`.

## Eingaben

- freigegebene Designrichtung;
- vorhandene Marke/Referenzen;
- relevante Accessibility-Anforderungen;
- vorhandene Komponenten oder Tokens;
- technische Stylingkonventionen des Projekts;
- freigegebene Motion-Prinzipien oder Motion-Contracts, wenn Motion systematisiert werden soll.

## Arbeitsweise

1. Inventarisiere wiederkehrende visuelle Entscheidungen.
2. Definiere semantische Rollen statt nur rohe Werte.
3. Lege Typorollen mit Größe, Gewicht, Zeilenhöhe und Einsatz fest.
4. Lege Farbrollen einschließlich Fokus-, Fehler- und Disabled-Zuständen fest.
5. Definiere Spacing- und Surface-Logik.
6. Begrenze Radius-, Shadow- und freigegebene Motionvarianten auf begründete Mengen.
7. Definiere Basiskomponenten nur dort, wo echte Wiederverwendung besteht.
8. Prüfe Kontrast und lesbare Defaultzustände.
9. Dokumentiere bewusst erlaubte Ausnahmen.
10. Konserviere bei Motion nur bereits begründete wiederkehrende Entscheidungen; neue Motion-Sprache wird mit `motion-design` entwickelt.

## Ausgabe

Mindestens:

```text
Designprinzipien
Typorollen
Farbrollen
Spacing-System
Surface-/Radius-/Shadow-Logik
Motion-Grundwerte
Basiskomponenten und Varianten
Accessibility-Grundsätze
bewusste Ausnahmen
```

## Qualitätsregeln

- Semantische Tokens vor zufälligen Einzelwerten.
- Hierarchie primär durch Typografie und Abstand lösen, nicht immer durch zusätzliche Cards.
- Keine Varianten nur für hypothetische Zukunftsfälle.
- Designsystem soll Identität stabilisieren, nicht jede Seite uniform machen.
- Motion-Tokens dokumentieren freigegebene Systementscheidungen; sie sind kein Ersatz für kontextbezogenes Motion-Design.

## Stop-Regeln

Stoppe, wenn:

- die zugrunde liegende Designrichtung noch nicht freigegeben ist;
- lokale Marken- oder Frameworkregeln fehlen und dadurch Grundentscheidungen offen sind;
- eine neue externe Design-/UI-Bibliothek eingeführt werden müsste.

## Leitgedanke

> Ein Designsystem konserviert gute Entscheidungen. Es ersetzt nicht das Designurteil.
