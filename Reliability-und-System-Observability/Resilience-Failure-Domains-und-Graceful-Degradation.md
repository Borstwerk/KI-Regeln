# Resilience, Failure Domains und Graceful Degradation

## Zweck

Resilience beschreibt gewünschtes Systemverhalten, wenn Teile eines Systems gestört, langsam, überlastet oder nicht verfügbar sind.

## Reliability-Anforderung vor Pattern

Dieser Bereich beschreibt **welches Verhalten benötigt wird**.

Software Architecture entscheidet später **welche Struktur oder welches Pattern** dieses Verhalten sinnvoll erreicht.

Beispiel:

```text
Reliability:
Ausfall der Recommendation-Dependency darf Checkout nicht verhindern.

Software Architecture:
entscheidet über Timeout, Fallback, Cache, Bulkhead, Circuit Breaker,
asynchrone Entkopplung oder eine andere Lösung.
```

Keine Architekturpatterns aus Reliability automatisch vorschreiben.

## Failure Domains

Ein Failure Domain ist ein Bereich, dessen gemeinsamer Ausfall mehrere Komponenten gleichzeitig betreffen kann.

Je nach System beispielsweise:

- Prozess / Host / Node;
- Rack / Zone;
- Region / Rechenzentrum;
- Cluster;
- Netzwerksegment;
- Control Plane;
- Identity Provider;
- Datenbank / Storage;
- Queue / Stream / Partition;
- externe API / SaaS / Provider;
- gemeinsames Secret / Zertifikat / DNS;
- gemeinsame organisatorische oder manuelle Abhängigkeit.

Failure Domains nicht nur aus sichtbarer Deploymenttopologie ableiten. Gemeinsame versteckte Dependencies können den tatsächlichen Blast Radius vergrößern.

## Failure-Domain-Analyse

Für kritische Flows fragen:

1. Welche Komponenten/Dependencies sind zwingend?
2. Welche teilen einen Failure Domain?
3. Welche Fehler propagieren synchron weiter?
4. Welche Ressourcen oder Retries verstärken Last?
5. Welcher Zustand bleibt bei Teilfehlern erhalten?
6. Welche Funktion darf degradiert werden?
7. Welche Funktion muss geschützt bleiben?
8. Wie wird Recovery erkannt und verifiziert?

## Graceful Degradation

Graceful Degradation bedeutet, dass ein System bei Teilstörungen bewusst reduzierte Funktion oder Qualität bereitstellt, statt unnötig vollständig auszufallen.

Klären:

- welche Funktion kritisch ist;
- welche Funktion optional/degradierbar ist;
- welches reduzierte Verhalten Nutzer sehen;
- wie Konsistenz und Datenintegrität erhalten bleiben;
- wie lange der degradierte Modus akzeptabel ist;
- wie erkannt wird, dass Normalbetrieb wieder möglich ist.

Fallback ist nicht automatisch sicher.

Ein Fallback kann:

- selten getestet sein;
- veraltete Daten liefern;
- versteckte zweite Betriebsart erzeugen;
- zusätzliche Dependencies aktivieren;
- Daten-/Semantikunterschiede besitzen;
- Fehler kaschieren.

## Failure Isolation

Gewünschtes Ziel kann sein, einen Fehler in Scope und Wirkung zu begrenzen.

Mögliche Dimensionen:

- Tenant;
- Region;
- Shard / Partition;
- Feature;
- Dependency;
- Workload-/Jobklasse;
- Request-/Trafficklasse.

Die konkrete technische Isolation gehört zur Architektur/Infra.

## Cascading Failures

Besonders prüfen:

- ungebremste Retries;
- synchron gekoppelte Dependencies;
- Queue-/Backlog-Wachstum;
- Connection-/Thread-Pool-Saturation;
- Autoscaling gegen begrenzte Downstreams;
- Failover, der die verbliebene Capacity überlastet;
- langsame Dependencies, die Ressourcen binden;
- gemeinsame Limits / Quotas.

Interface-/Contractregeln für Retry und Idempotenz liegen in `../Schnittstellen-und-Vertraege/Idempotenz-Retry-und-Concurrency.md`.

Reliability prüft systemisch, ob das resultierende Verhalten unter Störung tragfähig bleibt.

## Resilience Evidence

Mögliche Evidence:

- Architektur-/Failure-Domain-Review;
- Failure Testing;
- Load-/Capacity-Evidence;
- Restore-/Recovery-Test;
- Resilience Experiment;
- reale Incident-Evidence;
- SLO-/Health-Verhalten während einer Störung.

Designabsicht allein beweist keine Resilience.

## Leitgedanke

> Resilience ist beobachtbares Verhalten unter Störung. Patterns sind Mittel, nicht das Ziel.