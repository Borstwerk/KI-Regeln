# Incident Response und Koordination

## Zweck

Dieser Bereich beschreibt die kontrollierte Bearbeitung eines aktiven Produktions- oder Betriebsincidents.

Ziel ist zuerst, reale Wirkung zu verstehen, den Zustand zu stabilisieren und Recovery belastbar zu verifizieren. Vollständige Ursachenanalyse und langfristiges Lernen folgen danach.

## Incident ≠ Alert

Ein Alert ist ein Signal.

Ein Incident ist ein betrieblicher Zustand mit relevanter tatsächlicher oder drohender Wirkung, der koordinierte Reaktion benötigt.

Vor Eskalation möglichst klären:

- ist das Signal real?
- welche Nutzer, Consumer, Regionen, Datenflüsse oder Geschäftsprozesse sind betroffen?
- ist die Wirkung aktuell, vergangen oder nur potenziell?
- welche Evidence trägt diese Einschätzung?

## Grundablauf

```text
Signal / Report
→ Incident bestätigen oder widerlegen
→ Impact / Scope
→ Ownership / Rollen
→ Incident State
→ aktuelle Evidence
→ Stabilisierung / Mitigation priorisieren
→ technische Diagnose und Fachskills gezielt einsetzen
→ reale Aktion nur mit gültiger Autorisierung
→ Fresh Recovery Evidence
→ Kommunikation / Handoff
→ Abschluss
→ Postmortem-Kriterium prüfen
```

## Rollen und Verantwortungen

Je nach Größe kann ein Incident getrennte Verantwortungen benötigen für:

- Koordination / Entscheidungsfluss;
- technische Operations / Diagnose;
- Kommunikation;
- Planung, Timeline und offene Punkte.

Die konkreten Rollennamen bleiben lokal.

Wichtig ist die Funktionstrennung:

> Wer den Incident koordiniert, besitzt nicht automatisch technische Administratorrechte oder Freigabe für jede Mitigation.

## Incident State

Ein gemeinsamer Incident State sollte nach Möglichkeit enthalten:

- Start / Erkennungszeitpunkt;
- aktueller Impact und Scope;
- bestätigte Fakten;
- offene Hypothesen klar als Hypothesen;
- relevante Änderungen vor dem Incident;
- laufende Maßnahmen und Owner;
- Entscheidungen / Gates;
- aktuelle Health-/Recovery-Evidence;
- nächste geplante Aktion;
- Kommunikationsstatus.

Kein verborgenes Parallelwissen als einzige Entscheidungsbasis verwenden.

## Stabilisieren vor vollständiger Erklärung

Während relevanter Nutzerwirkung ist Mitigation oft wichtiger als vollständige Root-Cause-Analyse.

Beispiele möglicher Mitigationen:

- Traffic reduzieren/umleiten;
- Feature deaktivieren;
- Rollback;
- Scale/Capacity ändern;
- Dependency isolieren;
- Failover;
- kontrollierter Restart;
- Workload pausieren.

Diese Beispiele sind **keine Risikoklassifikation und keine Ausführungsfreigabe**.

Die technische Eignung, Nebenwirkungen und Autorisierung müssen im konkreten System geprüft werden.

## Diagnose

Die generische technische Ursachenanalyse bleibt beim bestehenden Skill `../Programmieren/Skills/diagnose/SKILL.md` beziehungsweise bei passenden Fachskills wie Datenbank-, Infrastruktur- oder Interface-Diagnose.

Incident Response koordiniert:

- welche Frage jetzt beantwortet werden muss;
- welche Evidence benötigt wird;
- wer die Diagnose übernimmt;
- welche Mitigation daraus folgt.

Incident Response erfindet keine Root Cause, wenn Evidence fehlt.

## Autorisierung und Gates

Incident-Dringlichkeit erweitert keine Tool- oder Produktionsberechtigung.

```text
Mitigation vorgeschlagen
≠
Mitigation autorisiert
≠
Mitigation erfolgreich
```

Besonders prüfen bei:

- Restart / Kill;
- Rollback;
- Restore;
- Failover / Failback;
- Traffic Switch;
- Scaling mit Kosten-/Dependencywirkung;
- Datenänderungen;
- Feature-/Config-Änderungen;
- Credential-/Permission-Änderungen;
- Destructive Operations.

Bestehende Regeln aus `../Agentenarbeit/Human-Gates-und-Freigaben.md` und `../Sicherheit/Externe-Aktionen-und-Bestaetigung.md` gelten weiter.

## Kommunikation

Kommunikation soll bestätigte Fakten, Unsicherheit und nächste Schritte unterscheiden.

Mindestens:

```text
Status
Impact / Scope
Was wissen wir sicher?
Was wird gerade getan?
Was ist noch unklar?
Wann beziehungsweise bei welchem Ereignis folgt ein Update?
```

Keine universellen Updateintervalle oder Severitymodelle zentral festlegen.

## Handoff

Bei Wechsel des Responders oder Teams weitergeben:

- kurze Incident-Zusammenfassung;
- aktueller Impact;
- bestätigte Evidence;
- bisherige Aktionen und Resultate;
- offene Hypothesen;
- aktuelle Risiken;
- nächster sinnvoller Schritt;
- erforderliche Rechte/Gates;
- Links zu Dashboards, Logs, Traces, Runbooks und Incident State.

## Recovery-Verifikation

Ein Incident ist nicht abgeschlossen, nur weil eine Mitigation ausgeführt wurde.

Fresh Evidence prüfen, zum Beispiel:

- kritischer Nutzer-/Consumerflow funktioniert wieder;
- relevantes SLI/Health-Modell erholt sich;
- Error-/Latency-/Freshness-/Business-Signal normalisiert sich;
- Dependencies sind stabil;
- Queue/Backlog wird kontrolliert abgebaut;
- Datenintegrität ist nicht ungeprüft;
- kein neuer Failure Mode durch die Mitigation entstanden.

Die konkrete Stabilitätsdauer bleibt lokal und evidenzbasiert.

## Security Incidents

Wenn Hinweise auf Kompromittierung, Credential Leakage, Forensikbedarf, Chain of Custody oder regulatorische Meldepflicht bestehen, an den Security-Prozess übergeben.

Generische Koordinationsmechanik kann weiterverwendet werden, Security-spezifische Entscheidungen gehören nicht hierher.

## Leitgedanke

> Im Incident zählt zuerst kontrollierte Wiederherstellung. Schnelligkeit ist wichtig, aber sie ersetzt weder Evidence noch Autorisierung.