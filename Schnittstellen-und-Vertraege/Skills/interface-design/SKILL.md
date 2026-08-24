---
name: interface-design
description: Entwirft oder präzisiert einen technologieübergreifenden Vertrag an einer bestehenden oder vorgesehenen Systemgrenze. Verwenden bei Consumer-/Provider-Fragen, Wahl von HTTP, GraphQL, RPC, Events oder Webhooks und beim Definieren der gemeinsamen Semantik. Nicht für große Systemzerlegung oder reine Implementierungsdetails verwenden.
---

# Interface Design

## Ziel

Eine fachliche Capability in einen expliziten, testbaren und evolvierbaren Consumer-/Provider-Vertrag übersetzen.

## Eingaben

- Capability / Use Case;
- bekannte Systemgrenze oder Architekturannahme;
- Provider und Owner;
- Consumer und Deploymentmodell;
- lokale Domain-/Security-/Stabilitätsanforderungen;
- bestehende Contracts, wenn Brownfield.

## Arbeitsweise

1. Provider, Consumer, Owner und Capability bestimmen.
2. Prüfen, ob die Grenze bereits Architekturentscheidung ist oder eine offene Architekturfrage eskaliert werden muss.
3. Consumer-Tasks, Stabilität und Deploymentkopplung erfassen.
4. Interaktionsform nach Bedarf wählen oder vorhandene Form respektieren: HTTP, GraphQL, RPC/IDL, Events, Webhook/Callback oder Kombination.
5. Contract-Semantik definieren: Operationen/Messages, Daten, Fehler, Auth, Timing, Idempotenz, Ordering/Delivery soweit relevant.
6. Compatibility- und Evolutionserwartung festlegen.
7. kanonisches Contract-Artefakt bestimmen.
8. offene Implementierungs- oder Architekturfragen sichtbar lassen.

## Nicht tun

- Services oder Bounded Contexts nebenbei neu schneiden;
- Transport nach Mode oder persönlicher Vorliebe wählen;
- Datenbankmodell als öffentliche API übernehmen;
- Frameworkdefaults zur Contract-Wahrheit erklären;
- bestehende Consumerannahmen ohne Change Review überschreiben.

## Ausgabe

```text
Capability
Provider / Owner
Consumer
Interaction Style
Contract Surface
Semantik / Fehler
Auth / Scope
Compatibility Policy
Contract Artifact
Open Questions / Gates
```

## Related

- `http-api-design`
- `event-contract-design`
- `contract-change-review`
- `interface-review`
- `domain-modeling`
- `contract-testing`