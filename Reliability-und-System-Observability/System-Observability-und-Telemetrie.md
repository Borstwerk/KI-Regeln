# System-Observability und Telemetrie

## Zweck

System-Observability soll relevante Betriebsfragen über ein laufendes System mit belastbarer Evidence beantwortbar machen.

Kernidee:

> Telemetrie sind beobachtbare Signale. Observability ist die Fähigkeit, daraus relevante Systemzustände und Zusammenhänge zu verstehen.

## Grenze zur Agenten-Observability

Dieser Bereich behandelt Runtime-Systeme, Services, Jobs, Pipelines, Datenflüsse und technische Dependencies.

`../Agentenarbeit/Observability-und-Traceability.md` behandelt dagegen Nachvollziehbarkeit von Agentenläufen, Tools, Gates, Artefakten und Evidence.

Beide Bereiche können ähnliche Mechanismen wie strukturierte Ereignisse oder Korrelation nutzen, besitzen aber unterschiedliche fachliche Sources of Truth.

## Question First

Nicht mit einem Tool oder einer Signalpflicht beginnen.

```text
kritischer Flow / Reliability Objective
→ Betriebsfrage
→ benötigte Evidence
→ Signalquelle
→ Korrelation / Kontext
→ Speicherung / Zugriff / Kosten / Datenschutz
→ Verifikation
```

Typische Fragen:

- Ist der Service aus Nutzer-/Consumer-Sicht gesund?
- Welche kritischen Flows sind betroffen?
- Seit wann und in welchem Scope?
- Welche Dependency oder Ressourcengrenze korreliert mit der Wirkung?
- Kann ein konkreter Fall über Systemgrenzen verfolgt werden?
- Hat eine Änderung den Zustand beeinflusst?
- Fehlt uns Evidence, um die Frage zu beantworten?

## Signaltypen

Je nach System können unter anderem relevant sein:

- Metriken;
- Logs;
- Traces;
- Events;
- Profiles;
- synthetische Messungen;
- Client-/Edge-Telemetrie;
- Business-/Domain-Signale;
- Queue-/Lag-/Freshness-Signale;
- Dependency- und Ressourcenstatus.

Kein Signaltyp ist allein Observability.

Auch das verbreitete Modell „Metrics + Logs + Traces“ ist eine nützliche Orientierung, aber keine vollständige oder universelle Definition.

## Health-Modell

Komponentenstatus und Servicegesundheit trennen.

```text
Prozess läuft
≠
Dependency funktioniert
≠
kritischer Nutzerflow funktioniert
```

Ein Health-Modell kann mehrere Evidenzebenen verbinden:

- Nutzer-/Consumerwirkung;
- Geschäfts-/Domainresultat;
- kritische Systemflows;
- Dependencies;
- Ressourcen/Saturation;
- interne Komponenten.

Die konkrete Aggregation und Zustandsklassifikation bleiben lokal.

## Symptom und Ursache

Observability sollte beide Fragen unterstützen:

```text
Was ist aus Nutzersicht kaputt oder degradiert?
→ Symptom / Wirkung

Warum passiert es?
→ Ursache / beitragender Faktor / Diagnose
```

Symptom-Signale sind besonders wichtig für Health und Paging. Ursachen-Signale bleiben wichtig für Diagnose, Capacity und frühe Warnungen.

## Korrelation

Wenn ein relevanter Flow mehrere Grenzen überschreitet, muss nach Möglichkeit nachvollziehbar sein, welche Ereignisse zusammengehören.

Mögliche Mechanismen:

- Request-/Correlation-/Trace-IDs;
- Operation-/Job-/Message-IDs;
- Version-/Deploy-/Change-Marker;
- Tenant-/Region-/Shard-Kontext, wenn zulässig und nötig;
- stabile fachliche Eventnamen.

Keine konkrete Header-, SDK- oder ID-Implementierung zentral erzwingen.

## Cardinality und Kosten

Telemetrie besitzt Kosten und technische Grenzen.

Insbesondere prüfen:

- unbeschränkte Dimensionen/Labels;
- hochkardinale Identifikatoren;
- Retention;
- Sampling;
- Speicher- und Querykosten;
- Übertragungsvolumen;
- zusätzliche Laufzeitlast;
- Nutzen pro Signal.

Hohe Kardinalität ist nicht grundsätzlich verboten. Sie muss zum Signaltyp, Backend und konkreten Debug-/Analysebedarf passen.

## Datenschutz und Sicherheit

Die Regeln aus `../Sicherheit/Logging-Datenschutz-und-Telemetrie.md` gelten weiterhin.

Insbesondere keine pauschale Aufnahme von:

- Secrets und Tokens;
- vollständigen Request-/Response-Bodies;
- personenbezogenen Daten;
- Auth-Headern;
- vertraulichen Dokumenten;
- produktiven Nutzdaten ohne Zweck und Freigabe.

## Telemetrie ist fehlbar

Mögliche Fehler:

- Instrumentierung fehlt auf Teilpfaden;
- falsche Units;
- unvollständige Labels/Attribute;
- Sampling blendet relevante Fälle aus;
- Zeitstempel oder Clocks sind inkonsistent;
- Pipeline/Collector/Backend verliert Daten;
- Query oder Dashboard aggregiert falsch;
- synthetische Checks repräsentieren reale Consumer nicht.

Darum gilt:

> Kein Signal ohne Überlegung, wie seine eigene Glaubwürdigkeit geprüft werden kann.

## Tool- und Providerneutralität

OpenTelemetry ist eine wichtige offene Interoperabilitäts- und Semantikreferenz, aber keine Pflichtarchitektur.

Prometheus, Grafana, Datadog, Elastic, Splunk, New Relic, CloudWatch, Azure Monitor, Google Cloud Operations oder andere Produkte bleiben Implementierungsadapter.

## Output eines Observability-Designs

Mindestens sichtbar machen:

```text
Critical Flows / Objectives
Operational Questions
Health Model
Required Evidence
Signal Sources
Correlation Needs
Coverage / Blind Spots
Privacy / Security
Cardinality / Cost Risks
Verification
Implementation Gaps
```

## Leitgedanke

> Instrumentiere nicht, um Telemetrie zu besitzen. Instrumentiere, damit wichtige Betriebsfragen verlässlich beantwortbar werden.