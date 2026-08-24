# Desired State und Infrastructure as Code

## Kern

Infrastructure as Code beschreibt einen gewünschten Infrastrukturzustand so, dass er reviewbar, reproduzierbar und möglichst automatisiert überprüfbar ist.

Das konkrete Tool kann deklarativ, imperativ oder hybrid arbeiten. Entscheidend ist die nachvollziehbare Beziehung zwischen:

```text
Konfiguration / Desired State
+ bekannter Ist-Zustand
→ geplante Wirkung
```

## Source of Truth

Ein Projekt muss festlegen, welche Artefakte für welche Ressourcen führend sind.

Nicht automatisch annehmen:

- Repository = vollständige Realität;
- Statefile = fachliche Wahrheit;
- Cloud Console = Source of Truth;
- Toolzustand = tatsächlicher Zustand.

Die Rollen müssen projektspezifisch benannt werden.

## Reproduzierbarkeit

IaC sollte nach Möglichkeit festhalten:

- Tool-/Provider-/Modulversionen;
- relevante Eingaben;
- Abhängigkeiten;
- Zielumgebung;
- externe Ressourcen/Imports;
- Ownership;
- sensitive Inputs getrennt vom normalen Quelltext.

## Module und Wiederverwendung

Abstraktion soll reale Wiederverwendung oder Governance verbessern, nicht nur Dateien verschieben.

Keine universelle Regel wie „ab der dritten Wiederholung Modul“ festschreiben.

## Drift

Manuelle Änderungen können legitim oder problematisch sein. Drift ist zunächst ein Befund, keine automatische Handlungsanweisung.

```text
Drift
→ Ursache / Autorität klären
→ Desired State anpassen
ODER
→ Actual State zurückführen
```

## Tooladapter

Terraform/OpenTofu, Pulumi, CloudFormation, Bicep, Ansible und ähnliche Werkzeuge dürfen projektspezifische Regeln ergänzen.

## Leitgedanke

> IaC ist nur dann verlässlich, wenn klar ist, welche Realität es beschreibt und welche Realität es verändern darf.