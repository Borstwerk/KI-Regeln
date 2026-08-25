# Traceability, Provenance und Coverage

## Zweck

Traceability macht nachvollziehbar, warum ein Requirement existiert, welche Artefakte davon abhängen und welche Folgen eine Änderung haben kann.

## Typische Links

```text
Stakeholder / Source / Ziel
→ Requirement
→ Acceptance Criteria / Verification Intent
→ Architecture / ADR
→ Interface / Data / Security / Reliability Design
→ Tests / Evidence
→ Release / Betrieb, soweit lokal benötigt
```

Nicht jedes Projekt braucht jede Linkart. Traceability folgt Risiko und Änderungsbedarf.

## Provenance

Für relevante Requirements sollte der Ursprung erkennbar bleiben:

- Source oder Stakeholder;
- Quellversion/Stand;
- abgeleitete Annahmen;
- Bestätigungsstatus;
- Entscheidung oder Konfliktdisposition.

Ein kopierter Requirement-Satz ohne Herkunft verliert wichtige Evidence.

## Coverage

Coverage beantwortet eine konkrete Frage, zum Beispiel:

- welche bestätigten Ziele haben noch kein Requirement?
- welche Requirements besitzen keine Acceptance Criteria?
- welche Requirements wurden noch keinem Design-/Testartefakt zugeordnet?
- welche Tests referenzieren supersedete Requirements?

Eine Prozentzahl ist nur sinnvoll, wenn Linktyp, Scope und Nenner definiert sind. `100 % Traceability` beweist weder Korrektheit noch Vollständigkeit des Requirements-Sets.

## Bidirektionale Wirkung

Links sollen Impact Analysis ermöglichen:

```text
Requirement geändert
→ Downstream Impact suchen

Test / Design ohne Requirement-Bezug
→ prüfen, ob Requirement fehlt, Artefakt obsolete ist oder Link fehlt
```

## IDs und Versionen

Stabile IDs erleichtern Traceability. Das konkrete ID-/Versionierungsschema bleibt lokal. Inhaltliche Änderungen dürfen nicht durch stille Wiederverwendung einer scheinbar unveränderten ID unsichtbar werden.

## Toolneutralität

Jira, Azure DevOps, GitHub Issues, ReqIF, Doors, Markdown, YAML oder Tabellen sind mögliche Speicher-/Linkmechanismen. Kein Tool ist Voraussetzung für Requirements Traceability.

## Leitgedanke

> Traceability ist ein Navigationsnetz für Begründung und Impact – kein Qualitätszertifikat.