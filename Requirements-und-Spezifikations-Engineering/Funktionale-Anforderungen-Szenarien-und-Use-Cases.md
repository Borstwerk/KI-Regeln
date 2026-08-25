# Funktionale Anforderungen, Szenarien und Use Cases

## Zweck

Funktionale Anforderungen beschreiben, welches beobachtbare Verhalten oder welche Capability für einen relevanten Actor oder Prozess erforderlich ist.

## Vom Ziel zum Verhalten

```text
Ziel / Bedarf
→ Actor / Auslöser / Kontext
→ erwartetes Systemverhalten
→ sichtbares Ergebnis / Zustand
→ relevante Alternativ- und Fehlerfälle
```

Nicht jede Funktion braucht dieselbe Detailtiefe. Kritische oder mehrdeutige Flows brauchen mehr Szenario-Evidence als einfache, gut verstandene CRUD-Funktionen.

## Szenarioelemente

Je nach Fall hilfreich:

- Actor oder auslösendes System;
- Preconditions;
- Trigger;
- Hauptfluss;
- alternative Pfade;
- Fehler-/Abbruchverhalten;
- Postconditions;
- fachlich relevante Zustandsänderung;
- relevante Berechtigungs-/Scope-Grenzen;
- Acceptance Criteria.

## Edge Cases

Nicht mechanisch jede theoretische Kombination dokumentieren. Priorisieren nach:

- fachlicher Invariante;
- Datenverlust oder irreversibler Wirkung;
- Security/Privacy;
- hoher Nutzerwirkung;
- relevanter Betriebs-/Integrationswirkung;
- bekannter historischer Fehlerklasse.

## Fachlogik

Requirements können Geschäftsregeln referenzieren, aber der Domain-Modeling-Prozess besitzt die kanonische fachliche Begriffs- und Invariantenarbeit. Widersprüche werden nicht durch neue Requirement-Formulierungen verdeckt.

## UI- und Implementierungsdetails

UI-Verhalten kann ein Requirement sein, wenn die Interaktion selbst Teil der benötigten Nutzerwirkung oder Accessibility ist. Pixel-, Framework- oder Komponentenentscheidungen gehören dagegen normalerweise nicht in Requirements.

## Leitgedanke

> Beschreibe den relevanten beobachtbaren Flow so konkret wie nötig – nicht so ausführlich wie möglich.