---
name: web-design-review
description: Prüft gerenderte Weboberflächen kritisch gegen Produktziel, lokale Designregeln, Informationshierarchie und typische generische AI-Designmuster. Verwenden vor Freigaben, nach Agenten-Umsetzungen oder bei unabhängigen UI- und AI-Slop-Reviews.
---

# Skill: Web Design Review

## Zweck

Prüfe eine bestehende gerenderte Weboberfläche kritisch gegen Produktziel, lokale Designregeln, Informationshierarchie und typische generische AI-Designmuster.

## Verwenden wenn

- eine Website oder ein Screen vor Freigabe bewertet wird;
- ein Agent ein Design umgesetzt hat;
- visuelle Qualität unabhängig von der erzeugenden Instanz geprüft werden soll;
- ein bestehendes UI nach AI-Slop-Risiken untersucht werden soll.

## Nicht verwenden als

- detaillierten Review von Timing, Easing, Spatial Continuity, Gesture oder Interruptibility vorhandener Motion – dafür `motion-review`;
- allgemeine Accessibility- oder Performanceprüfung.

Offensichtlich unmotivierte oder störende Motion darf als Designproblem benannt werden. Der fachliche Motion-Craft-Review wird bei Bedarf an `motion-review` übergeben.

## Eingaben

- gerenderte Oberfläche oder aussagekräftige Screenshots;
- lokale Designquelle, sofern vorhanden;
- Produkt-/Seitenziel;
- Zielgruppe;
- relevante Content- und Responsive-Regeln.

## Arbeitsweise

1. Prüfe zuerst gegen lokale Design- und Produktregeln.
2. Bewerte getrennt:
   - Identität;
   - Informationshierarchie;
   - Typografie/Rhythmus;
   - Content;
   - Interaktion;
   - Responsive-Verhalten.
3. Suche explizit nach generischen AI-Mustern.
4. Bei referenzgetriebenen Entwürfen prüfe Reference-Overfit: abstrahierte Prinzipien versus faktische Reproduktion fremder Komposition/Markensignatur.
5. Prüfe das Novelty Budget: erfüllen auffällige 3D-, Parallax-, Scrolltelling-, Minigame- oder Motion-Elemente einen klaren Produktzweck oder konkurrieren sie nur um Aufmerksamkeit?
6. Bei immersiven Experiences prüfe, ob Core Content, Mobile/Touch, Reduced Motion und Capability-/Failure-Fallbacks definiert sind.
7. Unterscheide Stilmittel mit Begründung von reflexartigen Defaults.
8. Priorisiere Funde nach Auswirkung.
9. Benenne Ursache und Wirkung statt nur kosmetische Vorlieben.
10. Schütze starke bestehende Entscheidungen vor unnötigem Redesign.
11. Erfinde keine neue Markenrichtung, wenn nur Review beauftragt ist.
12. Wenn die Reviewfrage speziell reale Motion betrifft, komponiere mit `motion-review` statt Motion-Craft hier zu duplizieren.

## Typische Anti-Slop-Funde

- austauschbarer SaaS-Hero;
- Card-Raster ohne Hierarchie;
- Pill-/Badge-Übernutzung;
- dekorative Icon-Kacheln;
- Gradient/Glow/Glass ohne Produktbezug;
- monotone Abschnittsstruktur;
- Fake-KPIs/Testimonialblöcke;
- generische Marketingphrasen;
- Motion als Dekoration statt Orientierung;
- überfrachtete „Experience“-Seite, auf der mehrere Gimmicks um Aufmerksamkeit konkurrieren;
- 3D/WebGL/Parallax ohne erkennbaren Informations- oder Produktzweck;
- enge Referenzreproduktion ohne eigenständige Produktidentität;
- Signature Experience ohne brauchbaren Mobile-/Reduced-Motion-/Failure-Pfad.

## Ausgabe

```text
Gesamturteil
Blocker / hohe Funde
Mittlere Funde
Kleine Funde
Anti-Slop-Risiken
Starke Entscheidungen, die erhalten bleiben sollten
Offene Punkte / fehlende lokale Regeln
```

Jeder relevante Fund enthält:

- Fundstelle;
- Problem;
- Auswirkung;
- empfohlene Richtung.

## Stop-Regeln

Wenn lokale Designziele fehlen, keine subjektive Geschmacksrichtung als verbindliche Wahrheit einsetzen. Allgemeine Qualitätsprobleme dürfen weiterhin benannt werden.

## Leitgedanke

> Review bewertet, ob das Design seine Aufgabe erfüllt – nicht ob der Reviewer persönlich denselben Stil gewählt hätte.
