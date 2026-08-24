---
name: http-api-design
description: Entwirft oder präzisiert HTTP-basierte API-Verträge mit Methoden, Ressourcen/Aktionen, Request/Response, Status, Fehlern, Pagination, Idempotenz, Auth und Evolution. Verwenden für REST-artige oder JSON-over-HTTP-Schnittstellen. Nicht für reine Frameworkimplementierung oder Async-Event-Contracts verwenden.
---

# HTTP API Design

## Ziel

Eine verständliche, interoperable und evolvierbare HTTP-Oberfläche für konkrete Consumer-Tasks definieren.

## Eingaben

- Consumer und Capability;
- lokale HTTP-/API-Konventionen;
- bestehende Contract-Baseline bei Brownfield;
- Domainmodell / Invarianten;
- Auth-/Tenant-Anforderungen;
- Stability-/Compatibility-Policy.

## Arbeitsweise

1. Consumer-Task und vorhandene Konventionen bestimmen.
2. Ressourcen, Aktionen oder Long-running Operation passend zur Fachsemantik modellieren.
3. Methode, URI, Request und Response definieren.
4. required/optional/null/Defaults und öffentliche Feldsemantik klären.
5. Status- und Fehlervertrag definieren.
6. Collections mit stabiler Ordering-/Pagination-/Filtersemantik definieren.
7. Idempotenz, Retry und Concurrency für Mutationen festlegen.
8. Auth-, Scope- und Tenant-Grenzen sichtbar machen.
9. Compatibility, Versionierung und Deprecation planen.
10. kanonisches OpenAPI- oder anderes Contract-Artefakt festlegen und Contract-Test-Erwartungen nennen.

## Nicht tun

- HTTP-Statuscodes nur nach Gewohnheit wählen;
- POST-Retries ohne Idempotenzvertrag als sicher darstellen;
- interne DTOs/Tabellen automatisch exposen;
- überall `/v1` verlangen;
- OpenAPI-Generierung als universell einzig richtige Pflegeform festschreiben;
- `event-contract-design` durch HTTP-Polling simulieren, wenn das Problem tatsächlich async-eventbasiert ist.

## Ausgabe

```text
Consumers
Operations
Schemas
Status / Errors
Collections
Idempotency / Retry / Concurrency
Auth / Tenant
Compatibility / Deprecation
Contract Artifact
Test Expectations
```

## Related

- `interface-design`
- `contract-change-review`
- `contract-testing`
- `integration-testing`