# Quellen und Inspirationen

Dieser Bereich synthetisiert tool- und providerneutrale Reliability-/Observability-Prinzipien aus Primärquellen, Standards, Herstellerdokumentation und aktuellen Agent-Skills.

## Primär- und Standardquellen

### Google SRE Book / Workbook

https://sre.google/sre-book/service-level-objectives/
https://sre.google/workbook/implementing-slos/
https://sre.google/sre-book/monitoring-distributed-systems/
https://sre.google/workbook/alerting-on-slos/
https://sre.google/sre-book/managing-incidents/
https://sre.google/sre-book/postmortem-culture/
https://sre.google/sre-book/eliminating-toil/
https://sre.google/workbook/production-readiness/
https://sre.google/sre-book/addressing-cascading-failures/

Für SLI/SLO, Error Budgets, symptomorientiertes Monitoring, Alerting, Incident Management, Postmortems, Toil, Capacity, Cascading Failures und Production Readiness.

Die Google-Praxis ist eine starke Fachreferenz, aber kein formaler Standard. Organisationsspezifische Targets, Rollenmodelle, Burn-Rate-Werte oder Zeitbudgets werden nicht automatisch übernommen.

### Google SRE – aktuelle SLO-Reflexion

https://sre.google/resources/practices-and-processes/rethinking-slos/

Als Gegenprüfung gegen SLO-Proliferation und unkritische Verwendung von SLOs für jede Betriebsfrage.

### OpenTelemetry

https://opentelemetry.io/docs/concepts/signals/
https://opentelemetry.io/docs/specs/otel/versioning-and-stability/
https://opentelemetry.io/docs/specs/semconv/

Für vendorneutrale Telemetrie, Signaltypen, Interoperabilität, Stability und Semantic Conventions.

OpenTelemetry ist eine wichtige Referenz, aber keine Pflichtimplementierung und nicht die Definition von Observability insgesamt.

### CNCF Observability

https://glossary.cncf.io/observability/
https://github.com/cncf/tag-observability

Für Observability als Systemeigenschaft und die Ergänzung zwischen Monitoring und Observability.

### Principles of Chaos Engineering

https://principlesofchaos.org/

Für Steady State, Hypothesen, realistische Failure Variables und Blast Radius.

Die Empfehlung zu produktionsnahen, produktiven und kontinuierlich automatisierten Experimenten wird nicht als universelle Pflicht übernommen.

### ISO/IEC 25010:2023

https://www.iso.org/standard/78176.html

Als formale Hintergrundtaxonomie für Produktqualität und Reliability. Nicht als operatives SRE-Playbook verwendet.

## Hersteller-Gegenprüfungen

### Microsoft Azure Well-Architected Reliability

https://learn.microsoft.com/en-us/azure/well-architected/reliability/
https://learn.microsoft.com/en-us/azure/well-architected/reliability/design-patterns

Für Health Modeling, Graceful Degradation, Failure Isolation, Reliability-Maturity und Design Patterns als Architekturmechanismen.

Providerdetails bleiben lokal.

### AWS Builders' Library / Well-Architected

https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html

Für Overload, Retry Amplification, Backoff/Jitter, Load Shedding und Recovery-/Reliability-Abgrenzung.

Konkrete AWS-Dienste und Defaults werden nicht zur zentralen Regel.

## Skill-Inspirationen

### arjunprabhulal/agent-skills – slo-definition

https://github.com/arjunprabhulal/agent-skills/blob/main/skills/sre/slo-definition/SKILL.md

Nützliche kompakte Trennung von SLI/SLO/Error Budget und Fokus auf Nutzerwirkung. Nicht übernommen werden feste SLO-Anzahlen, Rolling-Window-Pflichten, pauschale SLA-Abstände oder automatisch bindende Error-Budget-Aktionen.

### arjunprabhulal/agent-skills – capacity-planning

https://github.com/arjunprabhulal/agent-skills/blob/main/skills/sre/capacity-planning/SKILL.md

Nützlicher Skill-Schnitt zwischen gemessener Belastungsgrenze und Capacity-Entscheidung. Konkrete Autoscaling-, Forecast- oder Headroom-Heuristiken bleiben lokal.

### addyosmani/agent-skills – observability-and-instrumentation

https://github.com/addyosmani/agent-skills/blob/main/skills/observability-and-instrumentation/SKILL.md

Nützlich für question-first Instrumentation, strukturierte Telemetrie, Cardinality- und Verifikationsdenken. Nicht übernommen werden OTel-Pflicht, feste Signal-/Severity-/Alertmodelle oder universelle RED-/USE-Vorgaben.

### Weitere gesichtete Skills

Öffentliche Incident-, Monitoring-, Disaster-Recovery- und SRE-Mega-Skills wurden als Gegenprobe verwendet.

Häufige problematische Muster:

- feste SEV1–SEV4-Modelle;
- feste Reaktions-/Kommunikationszeiten;
- pauschale „Restart ist low risk“-Tabellen;
- Tool-/Kubernetes-Kommandos als universelle Antwort;
- Monitoring + SLO + Alerting + Incidents + DR + Capacity in einem Mega-Skill;
- automatische Produktionshandlungen aus Incident-Dringlichkeit;
- feste Restore-/Chaos-Testintervalle;
- Providerdefaults als angebliche SRE-Best-Practice.

Diese Muster werden bewusst nicht zentral übernommen.

## Aktive Upstreams

Mutable Quellen, die lokale Regeln oder Skills direkt beeinflussen, werden in `../Dokumentation/upstream-sources.yml` gepflegt.

Geplant beziehungsweise aktiv relevant sind insbesondere:

- OpenTelemetry Signals;
- OpenTelemetry Semantic Conventions;
- `arjunprabhulal/agent-skills` `slo-definition`;
- `arjunprabhulal/agent-skills` `capacity-planning`;
- `addyosmani/agent-skills` `observability-and-instrumentation`.

Andere Quellen bleiben bewusst Fachreferenzen oder Discoveryquellen statt künstlicher Sync-Abhängigkeiten.

## Grundsatz

> Reliability-Prinzipien sollen reale Betriebsfragen besser beantworten. Tooldefaults, Organisationsrituale und populäre SRE-Slogans werden erst nach Prüfung ihrer tatsächlichen Allgemeingültigkeit übernommen.