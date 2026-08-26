# Open-Source-Readiness – Phase 3 – 2026-08-25

## Scope

Dieser Bericht dokumentiert Hardening Phase 3 auf Basis von `bf99fef39519e292ea2412df66b91a5f686558f9`.

Er ist ein technischer und organisatorischer Readiness-Bericht, keine Rechtsberatung. Automatische Ähnlichkeits- oder Lizenzdetektion erzeugt Review-Evidence, aber keine juristische Entscheidung.

## Provenance-Audit

Die Upstream-Registry enthält 127 beobachtete Quellen:

- 65 konkrete GitHub-Artefakte;
- 62 Web-/Dokumentationsquellen.

### Nicht-GitHub-Quellen

62 Quellen wurden geprüft. 54 waren technisch textvergleichbar und zeigten in den registrierten lokalen Impact-Dateien weder exakte längere Zeilen noch 12-Wort-Shingle-Signale für konkrete Ausdrucksübernahme. Acht Quellen waren wegen HTTP-/Zugriffsgrenzen nicht textvergleichbar und wurden deshalb nicht künstlich als lizenzgeklärt bezeichnet.

### GitHub-Artefakte

Alle 65 GitHub-Artefakte wurden source-spezifisch geprüft.

Finale technische Provenance-Klassifikation:

- 61 × `reference/inspiration`, `review_status: assessed`, keine Redistributionsabhängigkeit;
- 4 × `adapted`, jeweils separat belegt und MIT-Notice-pflichtig;
- 0 × `needs-human/legal-review`.

Der automatische Ähnlichkeitscheck ist nur ein Signal. `assessed` wurde erst nach source-spezifischem Review vergeben; die Use-Class wurde nicht allein aus einer vorhandenen Lizenz abgeleitet.

### Bindung an den bewerteten Source-Snapshot

Jeder der 65 Provenance-Einträge hält den konkret bewerteten Snapshot selbst fest:

- Repository;
- Source Path;
- beobachteter Ref;
- beobachteter Blob-SHA.

Der dauerhafte Validator vergleicht diesen `source_snapshot` mit dem aktuellen `github-file`-Eintrag in `Dokumentation/upstream-sources.yml`. Ändert das Monitoring später Repository, Pfad, Ref oder `observed_sha`, schlägt die strukturelle Validierung fehl und verlangt einen expliziten erneuten Provenance-Review. Es gibt keine automatische Provenance-Synchronisation.

Die einmalige Phase-3-Migration wurde nur ausgeführt, nachdem bestätigt war, dass `Dokumentation/upstream-sources.yml` noch exakt denselben Blob (`3690a439169a134cf3bcc14473378db80bc288c1`) wie beim vollständigen 65er Audit hatte. Der dafür temporär benötigte Write-Workflow wurde anschließend wieder entfernt.

## Matt Pocock – vier getrennte Adaptionsentscheidungen

Für alle vier Fälle ist der jeweilige beobachtete Blob am Repository-Commit `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` nachgewiesen. Am selben Commit liegt `LICENSE` als MIT vor, Blob `f1dd2c09108dde1a5f56097cee8461b3ea834499`. Der Audit meldete für diese vier Artefakte keinen widersprechenden pfadspezifischen Lizenzhinweis.

### `mattpocock-tdd`

Beobachteter Blob: `8fc086710806190ee7c4baa32089cb877a75736a`.

Manuelle Adaptions-Evidence: Der lokale Skill bewahrt die markante Red/Green-Arbeit in kleinen Slices, behavior-over-internals, unabhängige erwartete Werte und die Ablehnung des Musters „erst alle Tests, dann gesamte Implementierung“.

### `mattpocock-diagnosing-bugs`

Beobachteter Blob: `061c25a524acaa93d4534e9e08a793c0a5fe45fd`.

Manuelle Adaptions-Evidence: Die lokale Diagnose folgt derselben charakteristischen Progression aus Feedback-Loop/Reproduktion, Minimierung, falsifizierbaren Hypothesen, gezielter Instrumentierung, Regressionstest vor Fix und Abschlussverifikation.

### `mattpocock-code-review`

Beobachteter Blob: `e28d7acbf7b3bb4d7817b7eb5d9c105af03f6ec4`.

Manuelle Adaptions-Evidence: Besonders starke strukturelle Nähe durch die explizite Zwei-Achsen-Logik: Upstream `Standards`/`Spec`, lokal `Code/Repository-Standards` und `Anforderung/Spezifikation`.

### `mattpocock-domain-modeling`

Beobachteter Blob: `9b97707e19ef1f590aada356f2b3f6bb881f91be`.

Manuelle Adaptions-Evidence: Der lokale Skill übernimmt als Struktur Glossarbegriffe challengen, kanonische Terminologie schärfen, konkrete Grenzszenarien prüfen, gegen Code abgleichen und ADRs nur für langlebige/überraschende Trade-offs einsetzen; die lokale Fassung erweitert dies deutlich um Scope- und Persistenzregeln.

Für alle vier Fälle steht der gemeinsame MIT-Notice in `THIRD-PARTY-NOTICES.md`.

## Neon – aufgelöster Provenance-Fall

Der zuvor offene Fall `neon-postgres-best-practices` wurde am 2026-08-26 source-spezifisch nachgeprüft.

Der registrierte Blob `43f3468765949e3db85a3782d90d4826b6c585bd` ist Bestandteil des Repository-Commits `0d9a967085c3bc137ab39ff9e3191c2eb3129d8c` in `neondatabase/postgres-skills`. Am exakt selben Commit liegt die Root-`LICENSE` als Apache License 2.0 mit Blob `b87eca9ebe930dd536fc479611af31e1110c7434`. Unter `skills/postgres-best-practices/` wurde in diesem Zustand keine abweichende `LICENSE`-, `COPYING`- oder `NOTICE`-Datei gefunden.

Die Lizenz wurde nicht als Abkürzung für die Use-Class verwendet. Der registrierte historische `SKILL.md`-Text wurde gegen jede der drei Local-Impact-Dateien einzeln mit demselben Long-Line-/12-Wort-Shingle-Verfahren wie im Phase-3-Audit verglichen. Ergebnis: kein exaktes Long-Line-Signal, kein 12-Wort-Shingle-Signal und kein expliziter Derivation-Marker. Die manuelle Gegenprüfung sieht nur generische Themenüberschneidungen wie Datenmodellierung, Indizes/Query-Optimierung und Migrationen; die lokalen Texte sind eigenständig deutsch formuliert und enthalten keine charakteristische übersetzte oder strukturelle Ausdrucksübernahme aus dem registrierten Upstream-Artefakt.

Finale Klassifikation:

- `review_status: assessed`;
- `use_class: reference/inspiration`;
- `material_scope: concepts/methods-only`;
- `redistribution_reliance: not-relied-on`;
- `redistribution_status: not-relied-on`;
- `license_spdx: Apache-2.0` als same-state historische Evidence, nicht als benötigte Redistributionsfreigabe.

Damit verbleibt kein `needs-human/legal-review`-Provenance-Record.

## Exposure-Audit

Der permanente Workflow `.github/workflows/open-source-exposure-audit.yml` prüft Current Tree und Reachable History read-only. Sein Dauerzustand verwendet `push` auf `main` und `hardening/**`, `pull_request` sowie `workflow_dispatch`; ein Phase-3-spezifischer Branchname ist nicht Teil des gemergten Workflowzustands.

Die Scanner-/Workflow-Schnittstelle für den History-Report ist auf die kanonischen Felder `commit_count` und `unique_reachable_blob_count` vereinheitlicht. Es wurden keine doppelten Kompatibilitätsfelder eingeführt.

Der Pre-Readiness-Scan auf `7829abf24e301d820047b6a3ccbca80b91fbe187` ergab:

- Current Tree: 0 potentielle Secret-Funde, 9 Kontext-Review-Marker, 0 Binärdateien;
- die 9 Kontextmarker wurden geprüft und sind erwartbare Begriffe in Governance-/Fachdokumentation, Evals beziehungsweise den Scanner-Patterns selbst, keine Secret-Funde;
- Reachable History: 691 erreichbare Commits, 900 eindeutige erreichbare Blobs, 0 potentielle Secret-Funde, 0 Kontext-Review-Funde.

Die History-Aussage gilt ausschließlich für Objekte, die aus den im Full-History-Checkout vorhandenen Refs erreichbar sind; unreachable/pruned Git-Objekte sind nicht Teil des Claims.

Nach dem Commit dieses Readiness-Stands müssen Current-Tree- und Reachable-History-Scan auf dem dadurch entstehenden finalen Branch-Head erneut erfolgreich laufen. Diese CI-Läufe sind die externe, nicht selbstreferenzielle Abschluss-Evidence; ihre Run-IDs werden im PR beziehungsweise Abschlussbericht festgehalten.

Auditberichte und CI-Ausgabe enthalten nur Finding-Metadaten wie Commit, Pfad, Zeile und Klasse; gefundene Secretwerte werden nicht ausgegeben.

## Projektlizenz

Der menschliche Decision Gate für die Projektlizenz wurde am 2026-08-26 ausdrücklich geschlossen: Das originäre KI-Regeln-Projektmaterial soll unter der **MIT License** veröffentlicht werden.

Die Root-`LICENSE` ist vorhanden und enthält den standardmäßigen MIT-Lizenztext mit der neutralen projektbezogenen Copyright-Zeile `Copyright (c) 2026 KI-Regeln contributors`.

Diese Root-MIT-Lizenz betrifft das originäre KI-Regeln-Projektmaterial. Sie relicensed kein Drittmaterial. Tatsächlich redistribution-relevante Fremdanteile bleiben unter ihren jeweils dokumentierten Lizenzen und Notice-/Attributionspflichten; `THIRD-PARTY-NOTICES.md` bleibt dafür maßgeblich.

Die vier Matt-Pocock-Adaptionsfälle behalten ihre same-state-MIT-Evidence und den dokumentierten MIT-Notice. `neon-postgres-best-practices` bleibt `assessed / reference/inspiration / concepts/methods-only / not-relied-on`; seine same-state Apache-2.0-Evidence ist historische Provenance-Evidence und keine benötigte Redistributionsfreigabe.

Der Licensing-Readiness-Bereich ist damit `ready`; die Projektlizenz ist kein offener Public-Release-Blocker mehr.

## Security Reporting

`SECURITY.md` ist vorhanden. Ein privater Vulnerability-Reporting-Kanal ist im aktuellen privaten Repositoryzustand noch nicht festgelegt.

Das wird nicht als technisch jetzt schon aktivierbare GitHub-Einstellung dargestellt: GitHub Private Vulnerability Reporting ist für öffentliche Repositories vorgesehen. Der zwingende Phase-4-Release-Schritt lautet daher: nach dem Visibility-Wechsel Private Vulnerability Reporting aktivieren, die Funktion praktisch prüfen und anschließend `SECURITY.md` bestätigen. Wird vorher ein anderer autorisierter privater Meldekanal festgelegt und dokumentiert, kann dieses Gate entsprechend früher geschlossen werden.

Bis einer dieser Wege tatsächlich verifiziert ist, bleibt Security Reporting ein Public-Release-Gate.

## Repository-Hygiene und Supply Chain

`README.md` enthält einen knappen Public Entry Path; `CHANGELOG.md` dokumentiert Hardening Phase 3 unter `Unreleased`. `CONTRIBUTING.md`, `SECURITY.md`, `ACKNOWLEDGEMENTS.md`, `THIRD-PARTY-NOTICES.md`, Pull-Request-Template, Dependabot-Konfiguration und die dokumentierte Branch-Protection-Empfehlung sind vorhanden.

Die permanenten CI-Workflows verwenden read-only `contents`-Permissions. `actions/checkout` und `actions/setup-python` sind auf konkrete geprüfte v7-Commit-SHAs gepinnt. Dependabot darf Review-PRs für GitHub Actions erzeugen; Auto-Merge, automatische Provenance-Synchronisierung und automatische Upstream-Synchronisierung existieren nicht.

## Release-Gate

Hardening Phase 3 ist technisch abgeschlossen, sobald auf demselben finalen Branch-Head der Repo-Validator, die reguläre Repo-CI, der Current-Tree-Exposure-Scan, der Reachable-History-Scan und der Base→Head-Diff-Audit erfolgreich geprüft wurden.

Das Repository selbst ist trotz erfolgreichem Phase-3-Hardening **noch nicht Public-Release-ready**, solange der verbleibende Release-Day-Gate offen ist:

1. privater Security-Reporting-Pfad: in Phase 4 nach dem Visibility-Wechsel GitHub Private Vulnerability Reporting aktivieren, Funktion prüfen und `SECURITY.md` bestätigen – oder vorher einen autorisierten alternativen privaten Kanal dokumentieren und verifizieren.

Der frühere Neon-Provenance-Blocker und der frühere Projektlizenz-Decision-Gate sind aufgelöst. Der verbleibende Security-Reporting-Gate darf nicht durch Automatisierung als erledigt markiert werden.
