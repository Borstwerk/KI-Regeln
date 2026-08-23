# Monitoring und Diagnose

## Zweck

Datenbankprobleme sollen aus beobachtbaren Symptomen, Metriken und realen Workloads diagnostiziert werden.

## Grundprinzip

> Diagnose beginnt mit einem konkreten Symptom und überprüfbarer Evidence – nicht mit einer Tuning-Checkliste.

## Typische Signale

Je nach Engine können relevant sein:

- Query-Latenz und Durchsatz;
- langsame / häufige Query-Shapes;
- CPU, Speicher, I/O;
- Cache-/Buffer-Verhalten;
- aktive und wartende Connections;
- Locks, Waits, Deadlocks;
- Replikations-/Durability-Lag;
- Speicher-/Datenwachstum;
- Fehler-, Timeout- und Retry-Raten;
- Backup-/Recovery-Status.

Keine universellen Schwellenwerte ohne Projektkontext festlegen.

## Diagnoseablauf

```text
Symptom
→ Zeitraum / betroffene Pfade
→ relevante Metriken
→ Query-/Workload-Evidence
→ Hypothese
→ gezielte Verifikation
→ kleinste Änderung
→ Wirkung messen
```

## Korrelation statt Einzelmetrik

Beispiel:

```text
hohe Query-Latenz
+ Pool-Wartezeit
+ hohe Connection-Zahl
```

kann eine andere Ursache haben als:

```text
hohe Query-Latenz
+ wenige Connections
+ viele gescannte Datensätze
```

Deshalb Signale gemeinsam betrachten.

## Slow Queries priorisieren

Nicht nur nach „langsamster Query“ sortieren.

Impact kann abhängen von:

- Laufzeit;
- Häufigkeit;
- betroffenen Nutzern / Pfaden;
- Ressourcenverbrauch;
- Locking;
- Geschäftsrelevanz.

Eine 300-ms-Query mit Millionen Aufrufen kann wichtiger sein als ein seltener 5-Sekunden-Adminreport.

## Diagnose nicht mit Reparatur vermischen

Zuerst Ursache und Evidence möglichst sauber erfassen.

Dann Reparaturvorschlag.

Sonst verändert eine vorschnelle Tuningmaßnahme den Zustand, bevor die Ursache verstanden ist.

## Produktionszugriff

Für Diagnose bevorzugen:

- read-only Metadaten;
- aggregierte Metriken;
- Query-Pläne mit kontrolliertem Risiko;
- kleine Samples;
- bestehende Monitoring-/Slow-Log-Daten.

Keine ungefragten Writes oder teuren Vollscans als „Diagnose“.

## Abschluss-Evidence

```text
Problem
Baseline
Ursachenhypothese
Verifikation
Änderung
Post-Change-Messung
Restrisiko
```

## Leitgedanke

> Datenbankdiagnose ist Ursachenarbeit. Tuning ohne Diagnose ist Konfigurationsroulette.