---
name: infrastructure-as-code
description: Entwirft oder präzisiert toolneutrale Infrastructure-as-Code-Konfigurationen und Desired-State-Modelle einschließlich Ownership, Inputs, Dependencies, State, Environments und Drift. Verwenden bei Terraform, OpenTofu, Pulumi, CloudFormation, Ansible oder vergleichbaren IaC-Aufgaben. Nicht für tatsächliches Apply/Deploy ohne separates Gate verwenden.
---

# Infrastructure as Code

## Ziel

Gewünschte Infrastrukturzustände reproduzierbar und reviewbar beschreiben, ohne Ausführung und Autorisierung zu vermischen.

## Eingaben

- lokale Architektur-/Plattformentscheidung;
- Zielumgebung und Ressourcenscope;
- vorhandener Desired State / State / Actual-State-Evidence;
- Tool-/Provider-/Versionskontext;
- Security-/Policy-/Ownership-Regeln.

## Arbeitsweise

1. Source of Truth und Ressourcenownership klären.
2. Desired State, Inputs und Abhängigkeiten modellieren.
3. Environment- und Secret-Grenzen explizit halten.
4. Wiederverwendung nur bei realem Nutzen abstrahieren.
5. Tool-/Provider-Versionen und externe Dependencies sichtbar machen.
6. State-/Import-/Ownership-Auswirkungen prüfen.
7. Validate und stärkste verfügbare Preview vorbereiten.
8. tatsächliche Änderung an `infrastructure-change-review` und lokales Gate übergeben.

## Nicht tun

- Provider-/Toolsyntax aus Erinnerung erfinden;
- manuelle Realität automatisch als falsch behandeln;
- Plan mit Apply gleichsetzen;
- Statefiles oder Secrets in normale Artefakte kopieren;
- eine große Plattformarchitektur nebenbei neu entwerfen.

## Ausgabe

```text
Desired State
Ownership
Inputs / Dependencies
Environment
State / Drift Notes
Validation
Preview Plan
Open Risks / Gates
```

## Related

- `infrastructure-change-review`
- `infrastructure-review`
- `tool-permission-review`
- `database-operations`