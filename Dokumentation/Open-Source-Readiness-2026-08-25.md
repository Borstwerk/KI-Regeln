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

- 60 × `reference/inspiration`, `review_status: assessed`, keine Redistributionsabhängigkeit;
- 4 × `adapted`, jeweils separat belegt und MIT-Notice-pflichtig;
- 1 × `needs-human/legal-review` mit bewusst offenem `use_class: unclear`.

Der automatische Ähnlichkeitscheck ist nur ein Signal. `assessed` wurde erst nach Review vergeben; ein offener Zweifelsfall bleibt ausdrücklich offen.

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

## Offener Provenance-Fall

`neon-postgres-best-practices` bleibt `needs-human/legal-review`.

Der beobachtete Blob `43f3468765949e3db85a3782d90d4826b6c585bd` konnte beim Audit keinem historischen Repository-Commit zugeordnet werden. Dadurch wurde kein belastbarer same-state-Lizenzstand hergestellt und der historische Artefakttext konnte nicht gegen die lokalen Impact-Dateien verglichen werden.

Der Eintrag bleibt deshalb:

- `use_class: unclear`;
- `material_scope: unclear`;
- `redistribution_reliance: unclear`;
- `redistribution_status: unresolved`.

Das ist keine Redistributionsfreigabe und verhindert `provenance: ready`.

## Exposure-Audit

Ein vorläufiger Current-Tree-Scan fand keine potentiellen Secret-Werte und keine Binärdateien. Ein vorläufiger Reachable-History-Scan erfasste 662 erreichbare Commits und 874 eindeutige erreichbare Blobs und meldete null potentielle Secret-Funde sowie null Kontextfunde.

Die History-Aussage gilt ausschließlich für Objekte, die aus den im Full-History-Checkout vorhandenen Refs erreichbar sind; unreachable/pruned Git-Objekte sind nicht Teil des Claims.

**Vor Öffnen des Phase-3-PR müssen Current-Tree- und Reachable-History-Scan auf dem finalen Branch-Head erneut erfolgreich laufen.** Bis dahin bleibt `history_exposure.scan_complete: false`.

Auditberichte enthalten nur Finding-Metadaten wie Commit, Pfad, Zeile und Klasse; gefundene Secretwerte werden nicht ausgegeben.

## Projektlizenz

`Dokumentation/Lizenzentscheidung-Open-Source.md` empfiehlt MIT als Kandidat für die spätere Projektlizenz. Daraus wurde bewusst **keine** Root-`LICENSE` erzeugt.

Offener Blocker: Ein autorisierter Mensch muss den tatsächlichen Rights Holder / Copyright Holder für das Repository festlegen und die Projektlizenzentscheidung freigeben.

## Security Reporting

`SECURITY.md` ist vorhanden. Ein privater Vulnerability-Reporting-Kanal wurde jedoch nicht autorisiert oder konfiguriert.

Das bleibt ein Public-Release-Blocker. Es wurde keine E-Mail-Adresse oder andere Kontaktmöglichkeit erfunden.

## Supply Chain

Der Repository-Validator nutzt `contents: read`. `actions/checkout` und `actions/setup-python` sind auf konkrete geprüfte v7-Commit-SHAs gepinnt. Dependabot darf Review-PRs für GitHub Actions erzeugen; Auto-Merge oder automatische Upstream-Synchronisierung existieren nicht.

## Release-Gate

Hardening Phase 3 darf technisch per PR reviewt werden, sobald finaler Validator, Diff-Audit und CI auf demselben finalen Branch-Head grün sind.

Das Repository selbst ist trotz erfolgreichem Phase-3-Hardening **noch nicht Public-Release-ready**, solange mindestens diese menschlichen Blocker offen sind:

1. `neon-postgres-best-practices` – Provenance/Legal Review;
2. Rights-Holder-/Root-License-Entscheidung;
3. privater Security-Reporting-Kanal.

Keiner dieser Punkte darf durch Automatisierung als erledigt markiert werden.
