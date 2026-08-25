# Anforderungstypen und Artefaktformen

## Zweck

Requirement-Typ und Dokumentformat sind zwei unterschiedliche Entscheidungen. Ein PRD, SRS, Ticket oder Backlogeintrag kann mehrere Requirement-Typen enthalten.

## Praktische Typen

Je nach Projekt können unter anderem unterschieden werden:

- **funktionale Anforderungen** – beobachtbares Verhalten oder Capability;
- **Qualitätsanforderungen** – z. B. Performance, Availability, Accessibility, Security, Usability oder Maintainability;
- **Constraints** – verbindliche Begrenzungen des Lösungsraums;
- **Datenanforderungen** – fachliche Nutzung, Aufbewahrung oder Qualitätsbedarfe;
- **operative Anforderungen** – Betrieb, Support, Recovery oder Wartung;
- **Übergangsanforderungen** – Migration, Koexistenz, Schulung oder Ablösung;
- **Compliance-/Policy-Anforderungen** – soweit aus autoritativen Quellen abgeleitet.

Keine Taxonomie ist universell vollständig. Kategorien dienen Findability, Review und Coverage, nicht dem Selbstzweck.

## Artefaktformen

Mögliche Darstellungen:

- einzelne Requirement Statements;
- User Stories;
- Use Cases;
- Szenarien;
- Tabellen/Kataloge;
- PRD/BRD/SRS;
- Backlog Items oder Tickets;
- Modelle oder Diagramme;
- maschinenlesbare Spezifikationen, wenn passend.

Die Form muss zum Leser, Lifecycle und Änderungsprozess passen.

## User Story

`Als <Rolle> möchte ich <Capability>, damit <Wert>` kann Wert und Nutzerperspektive sichtbar machen. Es ersetzt jedoch nicht automatisch:

- notwendige Geschäftsregeln;
- Fehler-/Alternativfälle;
- Qualitätsziele;
- Constraints;
- Acceptance Criteria;
- Provenance.

## Use Case / Szenario

Szenarien sind besonders hilfreich, wenn Reihenfolge, Zustände, Rollen oder Fehlerpfade relevant sind. Nicht jeder Requirement-Satz braucht einen vollständigen Use Case.

## IDs

Stabile IDs helfen bei Traceability und Change. Das konkrete Schema bleibt lokal. IDs dürfen keine Semantik vortäuschen, die später nicht stabil gehalten werden kann.

## Leitgedanke

> Wähle die Form, die die benötigte Aussage am klarsten und wartbarsten trägt – nicht die Form, die ein Framework verlangt.