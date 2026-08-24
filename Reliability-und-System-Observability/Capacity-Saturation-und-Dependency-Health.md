# Capacity, Saturation und Dependency Health

## Zweck

Capacity Planning verbindet gemessene Systemgrenzen, reale Last, Wachstum, Failure-Domain-Risiken und Bereitstellungszeiten zu einer begründeten Kapazitätsentscheidung.

## Grenze zu Performance- und Load-Testing

```text
Performance / Load Testing
→ misst Verhalten und Belastungsgrenzen

Capacity Planning
→ entscheidet, wie weit ein System unter realen Betriebsannahmen von diesen Grenzen entfernt betrieben werden soll

Infrastruktur / DevOps
→ setzt Kapazitäts- und Scaling-Entscheidungen technisch um
```

Ein Capacity Plan ohne Messbasis kann nur Annahmen und offene Evidence-Gaps dokumentieren.

## Relevante Eingaben

Je nach System:

- aktuelle Last und Peaks;
- Traffic-/Workload-Form;
- bekannte Events / saisonale Peaks;
- Wachstum / Rückgang;
- gemessene Capacity-/Breaking-/Degradation-Punkte;
- Saturation-Signale;
- kritische Dependencies und Quotas;
- Failure Domains;
- Scaling-/Provisioning-Lead-Time;
- Cold Start / Warm-up;
- Recovery-/Failover-Anforderungen;
- Kosten und Quotas;
- SLO-/Reliability-Ziele.

## Peak statt Durchschnitt

Durchschnittswerte können relevante kurzzeitige Lastspitzen verdecken.

Capacity-Entscheidungen sollen die Zeitauflösung verwenden, in der reale Saturation oder Nutzerwirkung entsteht.

Keine universelle Peak-Granularität festlegen.

## Capacity Ceiling

„Ceiling“ nicht nur als Crashpunkt verstehen.

Relevant kann bereits der Punkt sein, an dem:

- Latenz/SLO deutlich degradiert;
- Queue/Lag unkontrolliert wächst;
- Connection-/Thread-/Worker-Pools sättigen;
- Rate Limits wirken;
- Memory/GC/IO in einen instabilen Bereich geraten;
- Downstream-Dependencies überlastet werden;
- Fehlerraten oder Retries ansteigen.

Ein System kann technisch noch laufen und betrieblich bereits über seiner sinnvollen Kapazität liegen.

## Headroom

Headroom ist Abstand zwischen erwarteter Last und relevanter Kapazitätsgrenze.

Keine universelle Prozentzahl definieren.

Begründung abhängig von:

- Failure Cost;
- Lastvariabilität;
- Forecast-Unsicherheit;
- Scaling Lead Time;
- Quota-/Hardware-Beschaffungszeit;
- Failure-Domain-Verlust;
- Recovery-Verhalten;
- Downstream-Limits;
- Kosten.

## Constraint statt Lieblingsmetrik

CPU ist nicht automatisch der limitierende Faktor.

Prüfen können unter anderem:

- CPU;
- Memory / GC;
- Disk / IOPS;
- Netzwerk;
- Connection Pools;
- Threads / Workers;
- Queues;
- DB Connections / Locks;
- externe Rate Limits / Quotas;
- Providerlimits;
- Storage Growth;
- Lizenz-/Tenant-Grenzen;
- menschliche/operative Kapazität bei manuellen Prozessen.

Der erste relevante Engpass bestimmt oft die reale Capacity des Flows.

## Dependencies

Ein Service kann mehr eigene Instanzen bereitstellen und dadurch eine Dependency stärker überlasten.

Capacity Planning muss daher mindestens für kritische Flows fragen:

- welche Dependencies skalieren gemeinsam?
- welche besitzen feste Limits?
- welche besitzen andere Lead Times?
- kann Retry/Backlog zusätzlichen Druck erzeugen?
- welche Failure Domain reduziert verfügbare Capacity?

DB-spezifische Details bleiben `../Datenbanken/`.

## Autoscaling

Autoscaling ist ein Mechanismus, kein Ersatz für Capacity Planning.

Prüfen:

- welches Signal tatsächlich mit dem Constraint zusammenhängt;
- Reaktionszeit / Cooldown / Warm-up;
- minimale sichere Baseline;
- maximale Capacity / Quotas / Kosten;
- Downstream-Folgen;
- Verhalten bei Mess-/Control-Plane-Ausfall;
- Scale-up und Scale-down als eigene Failure Modes.

Keine zentralen Scale-up-/Scale-down-Regeln oder CPU-Defaults festlegen.

## Failure Domains

Je nach Anforderung prüfen:

- Host/Node;
- Rack/Zone;
- Region/DC;
- Cluster;
- Storage-/DB-Replikat;
- Queue/Partition/Shard;
- Provider/API;
- gemeinsame Netzwerk-/Identity-/Control-Plane-Abhängigkeit.

Nicht automatisch N+1 oder Multi-Region fordern.

Die relevante Frage lautet:

> Welche Capacity bleibt verfügbar, wenn der lokal relevante Failure Domain ausfällt?

## Forecast und Unsicherheit

Forecasts sind Annahmen, keine Wahrheit.

Explizit dokumentieren:

- Datenbasis;
- Horizont;
- bekannte Events;
- Growth-Annahme;
- Konfidenz / Bandbreite;
- Review-Trigger.

Keine feste Historienlänge oder Forecastmethode zentral vorgeben.

## Kosten

Capacity besitzt einen Preis und Unterkapazität besitzt ein Risiko.

Output soll Trade-offs sichtbar machen, nicht pauschal „mehr Capacity“ empfehlen.

## Leitgedanke

> Capacity Planning fragt nicht nur, wie viel Last ein System aushält, sondern wie viel belastbare Reserve unter realen Failure-, Growth- und Lead-Time-Annahmen benötigt wird.