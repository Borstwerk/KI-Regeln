# Contributing

KI-Regeln wird evidence-basiert gepflegt: allgemeine Arbeitsweise ist zentral, konkrete fachliche Wahrheit bleibt lokal.

## Änderungen einbringen

1. Von einem aktuellen `main` einen thematisch engen Branch erstellen.
2. Nur den notwendigen Scope ändern.
3. Relevante Sources of Truth, bestehende Regeln und lokale Entscheidungen beachten.
4. `python tools/repo_validator.py` ausführen.
5. Änderungen per Pull Request nach `main` einbringen.
6. CI und Review abwarten; ein grüner Validator ersetzt keinen fachlichen Review.

Direkte Änderungen an `main` sind für den späteren öffentlichen Betriebsmodus nicht vorgesehen.

## Skills, Workflows und Evals

Neue Skills oder Workflows brauchen einen konkreten wiederverwendbaren Bedarf. Vor einer neuen Datei prüfen, ob ein vorhandener Skill oder Workflow bereits ausreicht.

Bei neuen oder verhaltensändernden Skills:

- Discovery-Metadaten und Abgrenzung eindeutig halten;
- `skill-catalog.yml` konsistent pflegen;
- passende Evals ergänzen oder bewusst dokumentieren, warum noch keine formale Coverage besteht;
- Maturity oder Eval Coverage nicht aus Plausibilität hochstufen;
- bestehende Behavioral-Smokes nicht als unabhängigen Benchmark umdeuten.

Neue Workflows müssen im `workflow-index.yml` erfasst werden.

## Externe Quellen und Provenance

Keine fremden Texte, Skills, Templates, Tabellen, Codefragmente oder sonstigen Ausdrucksformen übernehmen, bevor Herkunft und Nutzungsrecht geklärt sind.

- Referenzen und Inspirationen sauber als solche dokumentieren.
- Konkrete GitHub-Upstreams in den vorhandenen Source-/Provenance-Registern nachführen, wenn sie lokale Regeln materiell beeinflussen.
- Bei Adaption, Kopie oder Vendoring die konkrete Lizenz am tatsächlich verwendeten Stand prüfen.
- Eine heutige Repository-Root-Lizenz ist kein automatischer Nachweis für einen historischen Blob oder Unterpfad.
- Unklare Fälle nicht durch automatische Umformulierung als rechtlich geklärt darstellen.

## Sicherheit und vertrauliche Daten

Keine Secrets, Zugangsdaten, produktiven Connection Strings, vertraulichen internen Inhalte, personenbezogenen Daten, echten Patienten-/Kundendaten oder proprietären Konfigurationen committen.

Wenn ein sensibler Fund bereits in Git-History gelangt ist, reicht das Löschen im aktuellen Tree nicht aus. Der Fund muss sicher rotiert bzw. remediated und die History separat bewertet werden.

## Pull Requests

Ein PR sollte knapp nennen:

- Ziel und Scope;
- relevante Sources of Truth;
- ausgeführte Prüfungen;
- offene Annahmen oder Gates;
- externe Quellen-/Provenance-Änderungen;
- bei Fachtextänderungen die betroffenen Skills/Regeln.

Kein CLA wird durch dieses Dokument eingeführt.
