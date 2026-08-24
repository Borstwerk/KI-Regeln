# Operational Readiness

## Zweck

Operational Readiness prüft vor Launch, größerem Release, Ownership-Übergang oder relevanter Betriebsänderung, ob genügend Evidence für einen verantwortbaren Betrieb vorhanden ist.

Operational Readiness ist **kein einzelner Skill**, sondern eine zusammengesetzte fachliche Sicht und ein Workflow.

## Warum kein Mega-Skill

Readiness kombiniert mehrere eigenständige Disziplinen:

```text
Requirements / Critical Journeys
+ Reliability Objectives
+ Observability
+ Alerting
+ Capacity / Dependencies
+ Recovery
+ Runbooks
+ Testing
+ Deployment / Rollback
+ Security / Permissions
+ Ownership / On-Call
→ Review
→ lokales Go / No-Go
```

Die Reihenfolge und Tiefe hängen von Risiko und System ab.

## Prüfachsen

### 1. Scope und Ownership

- Welcher Service, Flow oder Release wird geprüft?
- Wer besitzt Betrieb, technische Änderungen und Eskalation?
- Welche lokalen Sources of Truth gelten?

### 2. Reliability Objectives

- Sind kritische Nutzer-/Consumerflows bekannt?
- Existieren passende SLI-/SLO-/Reliability-Ziele oder ist deren Fehlen bewusst akzeptiert?
- Sind Zielwerte autorisiert statt erfunden?

### 3. Observability

- Können relevante Health- und Diagnosefragen beantwortet werden?
- Gibt es Blind Spots?
- Ist Telemetrie selbst verifiziert?
- Sind Datenschutz und Kosten berücksichtigt?

### 4. Alerting

- Welche Zustände benötigen zeitkritische Reaktion?
- Sind Alerts actionable und geroutet?
- Existiert passende erste Response-/Runbook-Evidence?
- Wurden neue Alerts tatsächlich getestet?

### 5. Capacity und Dependencies

- Sind reale Peaks und relevante Grenzen bekannt?
- Welche Dependency limitiert den kritischen Flow?
- Welche Failure Domains reduzieren Capacity?
- Gibt es Quota-/Scaling-/Lead-Time-Risiken?

### 6. Recovery

- Welche RTO-/RPO-/Recovery-Anforderungen gelten?
- Welche Daten/Zustände sind recoverable beziehungsweise nicht recoverable?
- Existiert gemessene oder glaubwürdige Restore-/Recovery-Evidence?
- Sind Failover/Failback und irreversible Nebenwirkungen verstanden?

### 7. Runbooks und Response

- Existieren passende Runbooks für bekannte kritische Störungen?
- Sind Zugriff, Ownership und Eskalation geklärt?
- Können Responders die nötige Evidence erreichen?

Der allgemeine Runbook-Skill bleibt `../Dokumentationserstellung/Skills/runbook/SKILL.md`.

### 8. Testing und Resilience

- Sind relevante Happy-, Failure- und Recovery-Pfade getestet?
- Braucht der Scope systemische Resilience-Evidence?
- Sind offene Testlücken sichtbar?

Testing Strategy bleibt `../Testing-und-QA/`.

### 9. Deployment und Rollback

- Sind Build, Deploy und Release getrennt verstanden?
- Existieren Promotion/Pause/Abort-Kriterien?
- Ist Rollback realistisch und sind nicht reversible Effekte bekannt?

Die Mechanik bleibt `../Infrastruktur-und-DevOps/`.

### 10. Security und Permissions

- Sind Produktionsrechte minimal und bekannt?
- Gibt es kritische Secret-/Credential-/Trust-Boundary-Risiken?
- Sind externe Aktionen und Human Gates klar?

Security Review bleibt `../Sicherheit/`.

### 11. Betriebsübergang

- Sind Owner erreichbar und geschult?
- Sind bekannte Risiken dokumentiert?
- Gibt es offene manuelle Schritte oder Toil?
- Ist klar, welche Evidence nach Launch/Promotion frisch geprüft wird?

## Readiness-Verdict

Ein Review kann beispielsweise berichten:

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

Diese Werte sind Reviewstatus, keine automatische Release- oder Deployautorisation.

Das konkrete Go/No-Go-Modell bleibt lokal.

## Keine Checklistenmagie

Alle Kästchen grün bedeutet nicht automatisch produktionsreif.

Readiness muss Risiken, Missing Evidence und Systemkontext berücksichtigen.

Umgekehrt braucht ein kleines risikoarmes System nicht zwangsläufig dieselbe Prozessbreite wie ein kritischer verteilter Service.

## Workflow

Siehe `../Workflows/Operational-Readiness-Review.md`.

## Leitgedanke

> Operational Readiness ist die begründete Aussage, dass Menschen, System und Evidence zusammen ausreichen, um einen Scope verantwortbar zu betreiben – nicht die Existenz einer langen Checkliste.