# Schnittstellen und Verträge

## Zweck

Dieser Bereich beschreibt allgemeine, technologieübergreifende Regeln für Schnittstellen zwischen Providern und Consumern.

Eine Schnittstelle ist dabei nicht primär ein Transport oder Dateiformat, sondern eine beobachtbare Zusage:

> Ein Contract beschreibt, was ein Consumer erwarten darf und worauf sich ein Provider dauerhaft festlegt.

## Scope

Der Bereich behandelt insbesondere:

- Consumer-/Provider-Sicht;
- Wahl eines passenden Interaktions- und Vertragsstils;
- Request-, Response-, Message- und Schema-Semantik;
- HTTP APIs;
- GraphQL-Verträge und Schemaevolution;
- RPC-/IDL-/Protobuf-Verträge;
- Event- und Async-Contracts;
- Webhooks und Callbacks;
- Fehler-, Retry-, Idempotenz- und Concurrency-Semantik;
- Auth-, Scope- und Tenant-Grenzen im Contract;
- Source-, Wire- und semantische Kompatibilität;
- Versionierung, Deprecation und Sunset;
- maschinenlesbare Vertragsartefakte;
- unabhängige Contract- und Interface-Reviews.

## Nicht der Scope

- **Software Architecture:** entscheidet, warum eine Systemgrenze existiert und wo Verantwortung liegt.
- **Domain Modeling:** definiert fachliche Begriffe und Invarianten.
- **Datenbanken:** definieren interne Persistenzmodelle.
- **Data Engineering:** behandelt in `../Data-Engineering/` veröffentlichte Datasets und Datenprodukte mit Grain, Datenqualität, Freshness, Lineage, Replay und Data-Contract-Evolution. Ein Tabellen-/View-/File-/Topic-Vertrag für analytische oder systemübergreifend publizierte Daten gehört dort hin; der operative Message-/Eventvertrag zwischen Services bleibt hier.
- **Testing und QA:** verifizieren, ob Implementierungen den Vertrag einhalten.
- **Sicherheit:** behandelt Threat Models, Credential-Schutz, Angriffstechniken und Security Testing im Detail.
- **Framework-Implementierung:** FastAPI, Spring, ASP.NET, DRF, Express oder ähnliche Mechanik bleibt lokal.

## Contract-Modell

```text
fachliche Capability
→ Provider / Consumer
→ Interaktionsstil
→ Contract
→ maschinenlesbares Artefakt, falls sinnvoll
→ Implementierung
→ Contract Testing
→ Evolution / Deprecation
```

## Compatibility-Modell

Änderungen werden nicht nur syntaktisch bewertet.

```text
Source Compatibility
+ Wire Compatibility
+ Semantic Compatibility
+ reale Consumer-/Deploymentbedingungen
→ Change Verdict
```

Verdicts:

- `COMPATIBLE` – unter den bekannten Consumerannahmen belastbar rückwärtskompatibel;
- `ROLLOUT-SENSITIVE` – grundsätzlich kompatibel, aber nur unter kontrollierter Reihenfolge, Feature-Nutzung oder Migration;
- `BREAKING` – bekannte bestehende Consumer können durch die Änderung brechen oder andere Bedeutung beobachten;
- `UNVERIFIED` – Consumer, Baseline, Tooling oder Semantik reichen für ein belastbares Urteil nicht aus.

## Risikoklassen

### READ / REVIEW

Bestehenden Vertrag lesen, vergleichen oder prüfen.

### ADDITIVE

Neue Contract-Oberfläche oder additive Änderung nach begründetem Compatibility Check.

### COMPATIBILITY-SENSITIVE

Formal additive oder technisch kompatible Änderung mit möglichem Consumer-, Rollout- oder Bedeutungsrisiko.

### BREAKING / DEPRECATION

Inkompatible Änderung, Entfernung, Bedeutungswechsel oder Sunset. Benötigt explizite Migration, Consumer-Kommunikation und das lokale Human Gate.

## Operative Skills

- `interface-design` – eine Systemgrenze aus Consumer-/Provider-Sicht in einen expliziten Vertrag übersetzen;
- `http-api-design` – HTTP-basierte API-Verträge entwerfen;
- `event-contract-design` – asynchrone Event-/Message-Verträge entwerfen;
- `contract-change-review` – Änderungen auf Source-, Wire- und semantische Kompatibilität prüfen;
- `interface-review` – eine Schnittstelle unabhängig über die relevanten Prüfachsen auditieren.

GraphQL, RPC/IDL, Protobuf und Webhooks besitzen eigene Fachregeln, aber zunächst keine eigenen Skills. Ein anderes Vertragsformat allein ist noch keine neue Arbeitsdisziplin.

## Leitgedanke

> Gute Schnittstellen bleiben verständlich, testbar und evolvierbar, auch wenn ihre Implementierung sich ändert.