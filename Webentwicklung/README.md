# Webentwicklung

Dieser Bereich beschreibt allgemeine Regeln für die Gestaltung und Entwicklung von Websites und Weboberflächen mit generativer KI.

Ziel ist nicht, möglichst schnell eine technisch funktionierende oder oberflächlich moderne Seite zu erzeugen. Ziel ist eine Website, die:

- zum tatsächlichen Produkt, Inhalt und Publikum passt;
- eine erkennbare visuelle Identität besitzt;
- Informationen sinnvoll priorisiert;
- echten Inhalt statt generischer Fülltexte trägt;
- auf unterschiedlichen Geräten funktioniert;
- zugänglich, performant und technisch nachvollziehbar ist;
- im gerenderten Zustand geprüft wurde.

## Grundprinzip

> Erst Identität und Informationsstruktur, dann Designsystem und Code.

Ein guter Webprozess trennt mindestens:

```text
Produkt / Zielgruppe
→ Information und Content
→ Designrichtung
→ Designsystem
→ Greybox / Informationsarchitektur
→ echter Content
→ Frontend-Implementierung
→ Accessibility und Performance
→ gerenderte Verifikation
→ unabhängiger Design-Review
```

## Warum ein eigener Bereich?

Generative Systeme können sehr schnell visuell plausible Websites erzeugen. Gerade deshalb entstehen häufig ähnliche Muster:

- austauschbare SaaS-Heros;
- unnötige Kartenraster;
- beliebige Gradients;
- dekorative Icon-Kacheln ohne Informationswert;
- übermäßige Glas-, Glow- oder Blur-Effekte;
- identische Typografie und Abstände über völlig unterschiedliche Produkte hinweg;
- erfundene Kennzahlen und Testimonials;
- generische Marketingphrasen;
- Animationen ohne funktionalen Zweck.

Das Problem ist nicht, dass eines dieser Mittel grundsätzlich verboten wäre. Das Problem entsteht, wenn Gestaltung aus Modellgewohnheit statt aus Produkt, Inhalt und Nutzungssituation entsteht.

## Bereiche

### Webdesign

`Webdesign/` beschreibt:

- Designrichtung und visuelle Identität;
- Informationsarchitektur und Greyboxing;
- Typografie, Farbe und Rhythmus;
- Content und Anti-Slop-Regeln;
- responsive Gestaltung und Interaktion;
- unabhängiges Webdesign-Review.

### Frontend

`Frontend/` beschreibt:

- Komponentenarchitektur;
- Accessibility;
- Performance;
- responsive Implementierung;
- Render- und Browser-Verifikation.

## Anti-Slop-Grundsatz

> Jedes visuelle Element soll Information, Hierarchie, Interaktion oder Identität tragen. Sonst braucht es einen guten Grund, überhaupt vorhanden zu sein.

Keine Technik ist automatisch schlecht. Gradient, Card, Pill, Shadow, Blur oder Animation sind Werkzeuge. Sie werden problematisch, wenn sie ohne semantische oder gestalterische Begründung reflexartig eingesetzt werden.

## Design und Engineering getrennt prüfen

Eine schöne Website kann technisch schlecht sein.

Eine technisch saubere Website kann gestalterisch beliebig sein.

Darum werden mindestens zwei Qualitätsachsen getrennt betrachtet:

```text
Designqualität
- Identität
- Hierarchie
- Typografie
- Content
- Interaktion
- visuelle Kohärenz

Engineeringqualität
- Semantik
- Accessibility
- Komponentenstruktur
- Performance
- Responsive-Verhalten
- Browser- und Renderkorrektheit
```

Erst beide zusammen ergeben ein belastbares Ergebnis.

## Skills

Unter `Skills/` liegen kompakte Arbeitsdisziplinen:

- `frontend-design` – eine konkrete visuelle Richtung aus Produkt, Publikum und Inhalt ableiten;
- `design-system` – Tokens, Typografie, Farben, Flächen, Abstände und Komponentenprinzipien definieren;
- `greybox` – Seitenstruktur und Informationshierarchie vor visueller Ausgestaltung prüfen;
- `web-content` – echten Webinhalt mit klarer Informationsfunktion statt KI-Fülltext entwickeln;
- `web-design-review` – bestehende Oberfläche kritisch auf Identität, Hierarchie und Anti-Slop prüfen;
- `accessibility-review` – Bedienbarkeit, Semantik, Kontrast, Fokus und assistive Nutzung prüfen;
- `frontend-performance` – relevante Performance-Risiken gezielt untersuchen;
- `visual-verification` – gerenderte Oberfläche auf Desktop, Mobile und relevante Zustände prüfen.

## Verhältnis zu anderen Bereichen

- `Schreiben/` liefert Regeln für natürlichen und glaubwürdigen Content.
- `Bildarbeit/` ergänzt wiederkehrende visuelle Entitäten und Bildreferenzen.
- `Programmieren/` liefert Entwicklungsprozess, Diagnose, TDD und Code-Review.
- `Agentenarbeit/` liefert Context Engineering, Delegation, Verification Loops und Human Gates.

Webentwicklung kombiniert diese Bereiche, ersetzt sie aber nicht.

## Projektlokale Wahrheit

Zentral gehören hierher:

- allgemeine Design- und Entwicklungsprinzipien;
- wiederverwendbare Reviewmethoden;
- Anti-Pattern-Regeln;
- allgemeine Skills.

Lokal im Projekt bleiben:

- Marke und konkrete Designidentität;
- Zielgruppenbeschreibung;
- Produktbotschaft;
- tatsächlicher Content;
- Informationsarchitektur des Produkts;
- Framework und Architektur;
- Browser- oder Geräteanforderungen;
- konkrete Performancebudgets;
- Release- und Deploymentregeln.

> Allgemeine Webarbeitsweise zentral, konkrete Produkt- und Designwahrheit lokal.