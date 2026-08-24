# Alerting und Actionability

## Zweck

Alerting soll relevante Betriebszustände rechtzeitig an die richtige Reaktion koppeln, ohne Menschen mit nicht handlungsrelevanten Signalen zu überlasten.

## Grundsatz

> Ein Alert ist kein Beweis für eine Ursache und keine automatische Autorisierung für eine Aktion.

## Vor jedem Alert

Klären:

- welches Reliability Objective, welcher kritische Flow oder welches betriebliche Risiko betroffen ist;
- welches beobachtbare Signal den Zustand repräsentiert;
- welche Reaktion erwartet wird;
- wie dringend diese Reaktion ist;
- wer beziehungsweise welches System reagieren soll;
- welche Evidence zur ersten Einordnung verfügbar sein muss.

## Symptom vor Ursache

Für menschenweckendes Paging ist normalerweise Nutzer-/Consumerwirkung oder ein unmittelbar bevorstehender relevanter Impact stärker als ein isolierter Ursachenindikator.

Beispiele für Ursachenindikatoren:

- CPU;
- Memory;
- Disk;
- Restart Count;
- einzelne Dependency-Warnung.

Solche Signale können für Diagnose, Capacity oder präventive Reaktion sehr wichtig sein. Sie sind aber nicht automatisch page-worthy.

Keine starre Regel ableiten:

```text
cause signal
=
niemals Alert
```

Ein Ursachen-Signal kann handlungsrelevant sein, wenn es zuverlässig einen drohenden Schaden ankündigt und eine zeitkritische Reaktion existiert.

## Actionability

Ein Alert sollte beantworten können:

```text
Was ist betroffen?
Wie relevant / dringend ist es?
Welche erste Aktion oder Entscheidung wird erwartet?
Wo liegt die passende Evidence / der Runbook-Einstieg?
```

Wenn über längere Zeit keine Reaktion aus einem Alert folgt, prüfen:

- ist der Alert unnötig?
- ist die Schwelle falsch?
- ist der Empfänger falsch?
- fehlt Ownership?
- fehlt ein Runbook?
- wird ein Ticket-/Dashboard-Signal fälschlich als Page behandelt?

## Thresholds und Fenster

Keine universellen Werte erfinden.

Schwellen können beispielsweise abgeleitet werden aus:

- SLO / Error Budget;
- lokaler Reliability-Policy;
- Baseline / historischem Verhalten;
- Capacity-/Saturation-Grenzen;
- fachlicher Deadline oder Freshness-Anforderung;
- bestätigter Nutzer-/Businesswirkung.

Zur Alertdefinition gehört auch das Auswertungsfenster beziehungsweise die notwendige Persistenz des Zustands.

Ein kurzer Spike und eine anhaltende Verschlechterung können unterschiedliche Bedeutung besitzen.

## SLO-/Burn-Rate-Alerting

Burn Rate kann ein starker Mechanismus sein, wenn ein geeignetes SLO und genügend Traffic/Ereignisse existieren.

Nicht zentral festlegen:

- feste Burn-Rate-Faktoren;
- feste Multiwindow-Kombinationen;
- feste Alertfenster;
- dass jedes SLO Burn-Rate-Alerts besitzen muss.

Bei Low-Traffic- oder seltenen Ereignissen kann ratio-basiertes Alerting zu wenig Signal liefern. Alternative Evidence oder längere/andere Bewertungsmodelle können nötig sein.

## Severity / Routing

Severity-Modelle, On-Call-Zuständigkeiten, Page-/Ticket-Klassen und Kommunikationsfristen bleiben lokal.

Zentral gilt nur:

- Dringlichkeit nach realer Wirkung und notwendiger Reaktionszeit begründen;
- keine Severity aus Tooldefaults übernehmen;
- Routing muss Ownership widerspiegeln;
- Security-, Datenschutz- oder Compliance-Incidents gegebenenfalls an deren Spezialprozess übergeben.

## Alert Noise

Warnsignale:

- häufige Alerts ohne Aktion;
- wiederkehrendes Acknowledge ohne Untersuchung;
- identische Ursachen erzeugen Alert-Stürme;
- ein einzelner Incident paged viele Teams ohne klare Ownership;
- Alertbedingungen reagieren auf normale Skalierung oder Deployments;
- flapping durch zu empfindliche Schwellen;
- Alerts ohne bekannte Aussage über Nutzer-/Systemwirkung.

Mögliche Gegenmaßnahmen:

- Threshold-/Window-Tuning;
- Deduplizierung;
- Gruppierung;
- Suppression/Inhibition mit Bedacht;
- Routing korrigieren;
- Alert in Ticket/Dashboard umstufen;
- obsolete Alerts entfernen;
- bessere SLI-/Health-Signale schaffen.

## Runbook-Verknüpfung

Ein Alert sollte, soweit sinnvoll, einen stabilen Einstieg zu Diagnose/Response liefern.

Der allgemeine Runbook-Skill liegt unter `../Dokumentationserstellung/Skills/runbook/SKILL.md`.

Alerting besitzt den Link und den erwarteten Reaktionskontext; Dokumentationserstellung besitzt die Qualität des Runbooks.

## Verifikation

Alertlogik selbst prüfen:

- Signal existiert tatsächlich;
- Unit/Dimension/Scope stimmen;
- Threshold-/Window-Logik entspricht der Absicht;
- erwarteter Empfänger wird erreicht;
- Deduplizierung/Suppression verdeckt keinen relevanten Fall;
- Runbook/Link funktioniert;
- Recovery-/Resolve-Verhalten ist sinnvoll.

Ein definierter Alert ist nicht automatisch ein verifizierter Alert.

## Reale Änderungen

Produktive Alertregeln, Routing oder Paging-Konfiguration zu verändern ist eine externe Betriebsaktion.

```text
Alert-Entwurf
→ Review
→ lokales Gate
→ Änderung
→ Test / Fresh Evidence
```

## Leitgedanke

> Ein guter Alert erzeugt eine begründete Reaktion. Ein schlechter Alert erzeugt Gewöhnung.