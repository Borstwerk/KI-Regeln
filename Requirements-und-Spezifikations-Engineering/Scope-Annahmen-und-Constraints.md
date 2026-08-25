# Scope, Annahmen und Constraints

## Zweck

Unklare Grenzen erzeugen Anforderungen, die scheinbar präzise sind, aber für unterschiedliche Systeme, Nutzer oder Releases etwas anderes bedeuten.

## Scope explizit machen

Mindestens klären, soweit relevant:

- betrachtetes Produkt, System oder Feature;
- betroffene Nutzer-/Stakeholdergruppen;
- relevante Prozesse und Betriebsphasen;
- In-Scope und Out-of-Scope;
- Release-/Migrationsgrenzen;
- externe Systeme und Abhängigkeiten;
- bekannte Non-Goals.

Out-of-Scope ist keine Müllhalde. Ein ausgeschlossenes Thema sollte bei hoher Relevanz einen Grund oder einen Zielkontext besitzen.

## Annahmen

Annahmen sind keine Requirements.

Für entscheidungsrelevante Annahmen dokumentieren:

- Aussage;
- Grund beziehungsweise Evidence;
- Confidence oder Status;
- wer sie bestätigen kann;
- welche Entscheidung davon abhängt;
- was passiert, wenn sie falsch ist.

Annahmen dürfen nicht durch häufiges Wiederholen zu scheinbaren Fakten werden.

## Constraints

Constraints begrenzen den Lösungsraum. Beispiele:

- regulatorische oder vertragliche Vorgaben;
- vorhandene Plattform-/Integrationsgrenzen;
- Budget-/Zeit-/Ressourcenbedingungen;
- Kompatibilitäts- oder Migrationszwänge;
- vorgeschriebene beziehungsweise ausgeschlossene Technologien aufgrund lokaler Entscheidungen;
- Betriebs- oder Datenresidenzbedingungen.

Technische Constraints sind nicht automatisch schlechte Requirements. Entscheidend ist, ob sie eine reale, autorisierte Grenze abbilden oder lediglich eine unbegründete Lösungspräferenz.

## Dependencies

Abhängigkeiten getrennt erfassen:

- andere Teams/Owner;
- externe Provider;
- vorgelagerte Entscheidungen;
- Daten-/Contract-Verfügbarkeit;
- rechtliche, Security- oder Infrastrukturfreigaben.

Eine Dependency ist kein Versprechen, dass sie rechtzeitig verfügbar sein wird.

## Scope Creep vs. legitimer Change

Neue Erkenntnis ist nicht automatisch Scope Creep. Prüfen:

- korrigiert sie eine falsche Annahme?
- schließt sie eine echte Anforderungslücke?
- verändert sie ein Ziel oder einen Constraint?
- gehört sie in denselben Release-/Produkt-Scope?

Danach über `requirements-change-analysis` behandeln, statt Änderungen informell in bestehende Requirements hineinzuschreiben.

## Leitgedanke

> Ein Requirement ohne klare Grenze kann korrekt formuliert und trotzdem für das falsche System wahr sein.