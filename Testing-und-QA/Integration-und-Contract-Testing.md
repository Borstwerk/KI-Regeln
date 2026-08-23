# Integration und Contract Testing

## Grundsatz

> Integrationstests prüfen Zusammenarbeit. Contract Tests prüfen Vereinbarkeit an einer definierten Grenze.

## Integrationstests

Integrationstests sind sinnvoll, wenn reales Zusammenwirken selbst Teil des Risikos ist.

Typische Ziele:

- Datenzugriff gegen die reale Engine-Art;
- Framework- und DI-Konfiguration;
- Serialisierung / Deserialisierung;
- Message Broker und Queues;
- Transaktions- oder Persistenzverhalten;
- interne Servicegrenzen;
- Adapter zu Betriebssystem oder Dateisystem.

Integrationstests sollen möglichst isolierte und reproduzierbare Umgebungen nutzen.

## Contract Tests

Ein Contract beschreibt beobachtbare Erwartungen zwischen Consumer und Provider.

Mögliche Vertragsbestandteile:

- Endpoint / Event;
- Request- und Response-Schema;
- Pflichtfelder;
- Status-/Fehlersemantik;
- Versionierungsregeln;
- Eventtypen;
- relevante Headers oder Metadaten.

## Consumer-/Provider-Perspektive

Consumer-Driven Contracts sind besonders nützlich, wenn der Provider wissen muss, welche konkrete Schnittstellenoberfläche reale Consumer tatsächlich benötigen.

Ein Contract Test soll aber nicht zum vollständigen Functional Test des Providers werden.

## Contract ≠ komplette Fachlogik

```text
Provider-Test
→ tut der Provider fachlich das Richtige?

Contract-Test
→ bleibt die gemeinsame Schnittstelle kompatibel?

E2E
→ funktioniert ein wichtiger Gesamtflow über mehrere Grenzen?
```

## Schema allein reicht nicht immer

Ein formal gültiges Schema kann semantisch inkompatibel sein.

Beispiele:

- Feld bleibt String, Bedeutung ändert sich;
- Statuscode bleibt gleich, Fehlerverhalten ändert sich;
- Feld bleibt optional, Consumer setzt es real voraus.

Deshalb Contracts an tatsächlichen Consumer-Erwartungen ausrichten.

## Versionierung

Bei Contract-Änderungen prüfen:

- ist Änderung backward compatible?
- existieren alte Consumer?
- ist Parallelbetrieb nötig?
- gibt es Deprecation-/Migrationspfad?

Die konkrete API-/Schnittstellenarchitektur gehört später zusätzlich in den Bereich `Schnittstellen-und-Vertraege/`.