# Recovery-Ziele, RTO/RPO und Disaster Recovery

## Zweck

Dieser Bereich beschreibt die Reliability-Sicht auf Wiederherstellungsziele und Disaster-Recovery-Readiness, ohne Backup-/Restore-, Datenbank- oder Infrastrukturmechanik zu duplizieren.

## Drei unterschiedliche Zielarten

```text
SLO
→ akzeptable laufende Servicequalität über ein Messfenster

RTO – Recovery Time Objective
→ maximal akzeptable Wiederherstellungsdauer nach einem relevanten Recovery-Ereignis

RPO – Recovery Point Objective
→ maximal akzeptabler Recovery Point beziehungsweise Datenverlust
```

Diese Ziele dürfen nicht miteinander verwechselt werden.

## Source of Truth

Konkrete RTO-/RPO-Werte entstehen aus lokalem Business-, Produkt-, Compliance-, Vertrags- oder Risikokontext.

Reliability darf:

- Anforderungen operationalisieren;
- Inkonsistenzen sichtbar machen;
- technische Evidence dagegen prüfen;
- Recovery Gaps dokumentieren.

Reliability darf nicht:

- ohne Grundlage ein RTO/RPO erfinden;
- teure Multi-Region-/Active-Active-Architektur allein aus allgemeiner Best Practice verlangen;
- einen Backupplan als bewiesene Recovery Capability behandeln.

## Recovery Scope

„Service wiederhergestellt“ kann mehr umfassen als einen Datastore.

Je nach System prüfen:

- Anwendungsartefakte;
- Datenbanken / Storage;
- Konfiguration;
- Infrastructure Desired State;
- Secrets / Keys / Zertifikate;
- Identity / Access;
- DNS / Routing;
- Queues / Streams / Backlogs;
- externe oder nicht rekonstruierbare Zustände;
- abhängige Systeme;
- Monitoring / Alerting;
- Runbooks und Zugriff auf Recovery-Dokumentation.

Die konkrete Ownership verbleibt bei den jeweiligen Domänen.

## RTO operationalisieren

Ein RTO ist erst operational sinnvoll, wenn klar ist:

- ab welchem Ereignis die Zeit läuft;
- welcher Zielzustand als „recovered“ gilt;
- welche kritischen Flows enthalten sind;
- welche Dependencies verfügbar sein müssen;
- welche Recovery-/Failovermechanik vorgesehen ist;
- welche Evidence die Wiederherstellung bestätigt.

Gemessene Recovery-Zeit und gewünschtes RTO getrennt halten.

```text
RTO-Ziel
≠
behauptete Restore-Dauer
≠
gemessene End-to-End-Recovery-Zeit
```

## RPO operationalisieren

Ein RPO benötigt Klarheit über:

- welche Daten/Zustände gemeint sind;
- welche Schreib- und Replikationspfade existieren;
- welches Ereignis den Recovery Point bestimmt;
- wie Datenverlust oder -lücke gemessen wird;
- welche Daten nach Recovery nachverarbeitet oder rekonstruiert werden können;
- welche Daten irreversibel verloren gehen könnten.

Backupfrequenz allein beweist kein RPO.

## Backup ≠ Recovery

Ein vorhandenes Backup ist eine Voraussetzung, aber keine End-to-End-Recovery-Evidence.

Prüfen:

- ist das Backup erreichbar, wenn der Primär-Failure-Domain betroffen ist?
- sind benötigte Keys/Credentials verfügbar?
- ist die Recovery-Prozedur bekannt?
- wurde Restore technisch verifiziert?
- wurde Datenintegrität geprüft?
- wurde der Service danach in einem relevanten Flow frisch geprüft?
- wurde die benötigte Recovery-Zeit gemessen?

DB-spezifische Backup-/Restore-Regeln bleiben `../Datenbanken/`.

## Failover und Failback

Failover ist eine reale Infrastruktur-/Systemaktion und kann eigene Risiken besitzen.

Reliability prüft:

- gewünschte Recoverywirkung;
- benötigte Daten-/State-Konsistenz;
- erwartete Nutzerwirkung;
- Failure-Domain-Annahmen;
- Fresh Verification;
- offene Risiken für späteren Failback.

Die konkrete Ausführung bleibt bei Infra/DB/Architektur und lokalen Gates.

## Recovery Tests und Übungen

Mögliche Evidence:

- reproduzierbarer Restore-Test;
- Disaster-Recovery-Rehearsal;
- Failure Testing;
- Resilience Experiment / Game Day;
- dokumentierte reale Recovery.

Keine universelle Testfrequenz festlegen.

Testintervall folgt Risiko, Änderungsrate, Recovery-Komplexität und lokaler Governance.

## Nicht recoverable

Explizit dokumentieren, was nicht oder nur teilweise wiederhergestellt werden kann.

Das kann entscheidungsrelevanter sein als eine lange Liste vorhandener Backups.

## Leitgedanke

> Recovery Readiness ist nicht die Existenz eines Backups, sondern ein evidenzgestützter Pfad von einem relevanten Failure-Zustand zurück zu einem verifizierten Servicezustand.