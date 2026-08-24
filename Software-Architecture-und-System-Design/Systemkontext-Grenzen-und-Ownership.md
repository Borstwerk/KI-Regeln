# Systemkontext, Grenzen und Ownership

## Zweck

Systemdesign beginnt mit einer klaren Außengrenze: Wer nutzt das System, welche externen Systeme existieren, welche Verantwortung gehört hinein und welche ausdrücklich nicht?

## Kontextfragen

- Welche Akteure oder Systeme lösen Verhalten aus?
- Welche Ergebnisse oder Effekte verlassen die Grenze?
- Welche externen Systeme sind authoritative, welche nur Consumer?
- Welche Daten oder Entscheidungen besitzt das System selbst?
- Welche Verantwortung gehört bewusst zu einem Nachbarsystem?
- Welche Trust-, Tenant-, Netzwerk- oder Organisationsgrenzen sind relevant?

## Ownership

Für jede wesentliche Capability und jeden autoritativen Zustand sollte eine primäre Verantwortung erkennbar sein.

```text
Capability / Zustand
→ verantwortlicher Systemteil
→ erlaubte Leser / Schreiber
→ öffentliche Grenze
→ relevante Invarianten
```

Mehrere Komponenten dürfen zusammenarbeiten. Unklare oder konkurrierende Ownership muss jedoch als Risiko sichtbar werden.

## Context vor Container

Bevor Module, Services, Queues oder Datenbanken vorgeschlagen werden, den Systemkontext schließen. Ein Architekturdiagramm mit vielen internen Kästen ist wertlos, wenn unklar bleibt, wo die Verantwortung des Systems beginnt und endet.

## C4 als optionale View-Sprache

C4 ist eine nützliche Referenz für unterschiedliche Abstraktionsebenen:

- System Context;
- Container;
- Component;
- Code.

Nicht jede Aufgabe benötigt alle Ebenen. Die View wird nach Informationsbedarf gewählt, nicht nach Vollständigkeitsritual.

## Grenzen zu Nachbardomänen

- Fachbegriffe und Invarianten → `domain-modeling`;
- konkrete API-/Eventverträge → Schnittstellen und Verträge;
- konkrete DB-Ownership innerhalb eines Speichers → Datenbanken;
- Dataset-Ownership und Lineage → Data Engineering;
- Trust-/Threat-Grenzen → Sicherheit.

## Anti-Regeln

- Systemgrenzen nicht aus Repo-Ordnern allein ableiten;
- Deployable Unit nicht automatisch mit Bounded Context gleichsetzen;
- Teamgrenze nicht automatisch zu Servicegrenze machen;
- Shared Database weder pauschal verbieten noch pauschal akzeptieren;
- externe Systeme nicht in die eigene Verantwortung hineinmodellieren, nur weil sie technisch eng gekoppelt sind.

## Leitgedanke

> Eine gute Grenze macht Verantwortung klarer, nicht nur das Diagramm ordentlicher.