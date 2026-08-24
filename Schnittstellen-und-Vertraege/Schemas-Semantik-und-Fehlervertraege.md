# Schemas, Semantik und Fehlerverträge

## Schema ≠ Bedeutung

Ein Schema beschreibt Struktur und Validierungsregeln. Ein Contract muss zusätzlich die fachliche Bedeutung beobachtbarer Elemente festlegen.

Für relevante Felder klären:

- Name und fachliche Bedeutung;
- Typ und Format;
- required vs. optional;
- nullable vs. absent;
- Default und dessen Bedeutung;
- read-only / write-only;
- erlaubte Werte bzw. Erweiterbarkeit;
- Einheiten und Zeitzonen;
- Stabilität und Deprecation;
- sensible oder tenantgebundene Daten.

## Request und Response getrennt denken

Ein internes Modell oder eine gemeinsame DTO-Klasse ist nicht automatisch der richtige Vertrag für beide Richtungen.

Ein Feld kann zum Beispiel servergeneriert, nur lesbar, nur schreibbar oder in unterschiedlichen Zuständen gültig sein.

## Enums und offene Werte

Ein neuer Enum-Wert kann syntaktisch additiv sein und alte Consumer trotzdem brechen, wenn diese unbekannte Werte nicht behandeln.

Deshalb Erweiterbarkeit explizit dokumentieren und Change Review nicht auf Schema-Diff reduzieren.

## Fehler sind Teil des Contracts

Ein belastbarer Fehlervertrag trennt mindestens:

- maschinenlesbare Fehlerklasse oder Code;
- stabile Bedeutung;
- relevante strukturierte Metadaten;
- menschliche Erklärung;
- Retry-/Recovery-Hinweis, wenn relevant.

Freitext allein ist keine stabile Programmierschnittstelle.

Für HTTP kann RFC 9457 Problem Details ein interoperabler Ausgangspunkt sein. Andere Paradigmen können eigene standardisierte Fehlermodelle besitzen.

## Keine Interna leaken

Nicht als Contract veröffentlichen, wenn nicht bewusst erforderlich:

- Stack Traces;
- interne Exceptionnamen;
- Tabellen-/Spaltennamen;
- interne Hostnamen;
- Secrets oder Tokens;
- sensible Policy-Details.

## Leitgedanke

> Ein valides Payload ist noch kein eindeutiger Vertrag.