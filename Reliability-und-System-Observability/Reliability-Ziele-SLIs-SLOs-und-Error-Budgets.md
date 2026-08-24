# Reliability-Ziele, SLIs, SLOs und Error Budgets

## Zweck

Reliability-Ziele übersetzen lokale Erwartungen an einen laufenden Service in messbare, überprüfbare Aussagen.

## Reihenfolge

```text
kritischer Nutzer-/Consumer-Erfolg
→ Reliability-Anforderung
→ SLI-Spezifikation
→ Messimplementierung
→ SLO + Fenster
→ Error Budget, falls passend
→ lokale Entscheidungs-/Governance-Regel
```

Nicht mit einer beliebigen Prozentzahl beginnen.

## SLI-Spezifikation vor Messimplementierung

Die SLI-Spezifikation beschreibt, **welcher beobachtbare Erfolg** zählt.

Die Messimplementierung beschreibt, **wie und wo** dieser Erfolg gemessen wird.

Beispiel:

```text
SLI-Spezifikation:
Anteil gültiger Checkout-Versuche, die erfolgreich abgeschlossen werden.

Mögliche Messimplementierungen:
- serverseitige Request-/Business-Events;
- clientseitige Messung;
- synthetische Transaktion;
- Kombination mehrerer Evidenzquellen.
```

Die Implementierungen können unterschiedliche Coverage, Latenz, Bias, Kosten und Fehlerquellen besitzen.

## Geeignete SLI-Typen

Je nach System können unter anderem relevant sein:

- Verfügbarkeit / Erfolg;
- Latenz;
- Freshness;
- Durability;
- Correctness;
- Coverage / Completion;
- Queue-/Processing-Lag;
- andere lokal definierte Nutzer- oder Geschäftsresultate.

Nicht jedes System ist requestbasiert. Eine feste Golden-Signal- oder Good-Events/Total-Events-Schablone ist daher kein Zwang.

## SLO

Ein SLO benötigt mindestens:

- Scope;
- SLI-Spezifikation;
- Messimplementierung oder klaren Measurement Gap;
- Ziel;
- Messfenster;
- relevante Exclusions;
- Owner/Stakeholder;
- Reviewpunkt.

Ziel und Fenster müssen zusammen verstanden werden.

## Zielwerte

Keine universellen Werte erfinden.

Wenn keine autorisierte Anforderung existiert:

- aktuelle Baseline beschreiben;
- Nutzer-/Businesswirkung herausarbeiten;
- Kosten und Risiken verschiedener Kandidaten vergleichen;
- Unsicherheit und fehlende Evidence sichtbar machen;
- vorgeschlagene Werte ausdrücklich als **Kandidaten**, nicht als gültige Requirement markieren.

## 100 Prozent

100 % ist kein allgemeines Reliability-Ziel.

Ein höheres Ziel kann erhebliche Kosten, Komplexität und langsamere Änderungen verursachen. Ein zu niedriges Ziel kann reale Nutzer- oder Geschäftsrisiken ignorieren.

Die richtige Frage lautet nicht:

> Welche Anzahl Neunen ist professionell?

Sondern:

> Welches messbare Verhalten ist für diesen kritischen Flow unter seinen realen Anforderungen akzeptabel?

## Error Budget

Bei ratio-basierten SLOs kann das verbleibende tolerierte Fehlverhalten als Error Budget ausgedrückt werden.

Das Budget ist ein Entscheidungsinput, keine automatische Autorisierung.

```text
Error Budget vorhanden
≠
Deploy automatisch erlaubt

Error Budget verbraucht
≠
automatischer globaler Change Freeze
```

Eine Error-Budget-Policy muss lokal festlegen:

- welche Entscheidungen sie beeinflusst;
- für welchen Scope;
- wer entscheidet;
- welche Ausnahmen/Gates gelten;
- wie Konflikte mit Security, Compliance, Incident Recovery oder dringenden Fixes behandelt werden.

## SLO und SLA

SLO und SLA nicht gleichsetzen.

- SLO: operationales Ziel / Steuerungsinstrument;
- SLA: vertragliche Zusage mit lokal definierter Konsequenz.

Es gibt keine universelle Regel, welchen numerischen Abstand beide haben müssen.

## SLO und RTO/RPO

Nicht vermischen:

```text
SLO
→ laufende Servicequalität über ein Messfenster

RTO
→ akzeptable Wiederherstellungsdauer nach Recovery-Ereignis

RPO
→ akzeptabler Recovery Point / Datenverlust
```

RTO/RPO siehe `Recovery-Ziele-RTO-RPO-und-Disaster-Recovery.md`.

## Lifecycle

SLOs regelmäßig gegen Realität prüfen:

- misst das SLI noch den relevanten Nutzererfolg?
- ist die Messimplementierung glaubwürdig?
- ist der Zielwert entscheidungsrelevant?
- wird das SLO dauerhaft verfehlt oder mühelos übertroffen?
- haben Architektur, Traffic, Consumer oder Business-Anforderungen den Scope verändert?
- ist das SLO redundant geworden?

SLO-Proliferation ohne klare Entscheidung oder Ownership vermeiden.

## Leitgedanke

> Ein SLO ist nur dann nützlich, wenn klar ist, welchen Nutzererfolg es misst und welche Entscheidung daraus folgen darf.