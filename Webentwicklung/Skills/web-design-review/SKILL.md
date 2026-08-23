# Skill: Web Design Review

## Zweck

Prüfe eine bestehende gerenderte Weboberfläche kritisch gegen Produktziel, lokale Designregeln, Informationshierarchie und typische generische AI-Designmuster.

## Verwenden wenn

- eine Website oder ein Screen vor Freigabe bewertet wird;
- ein Agent ein Design umgesetzt hat;
- visuelle Qualität unabhängig von der erzeugenden Instanz geprüft werden soll;
- ein bestehendes UI nach AI-Slop-Risiken untersucht werden soll.

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
4. Unterscheide Stilmittel mit Begründung von reflexartigen Defaults.
5. Priorisiere Funde nach Auswirkung.
6. Benenne Ursache und Wirkung statt nur kosmetische Vorlieben.
7. Schütze starke bestehende Entscheidungen vor unnötigem Redesign.
8. Erfinde keine neue Markenrichtung, wenn nur Review beauftragt ist.

## Typische Anti-Slop-Funde

- austauschbarer SaaS-Hero;
- Card-Raster ohne Hierarchie;
- Pill-/Badge-Übernutzung;
- dekorative Icon-Kacheln;
- Gradient/Glow/Glass ohne Produktbezug;
- monotone Abschnittsstruktur;
- Fake-KPIs/Testimonialblöcke;
- generische Marketingphrasen;
- Motion als Dekoration statt Orientierung.

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