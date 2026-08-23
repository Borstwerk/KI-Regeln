# Toolanforderungen und Fallbacks

## Grundprinzip

Ein Skill darf Fähigkeiten der Laufzeit nicht stillschweigend voraussetzen.

Vor der Ausführung unterscheiden:

- **requires** – ohne diese Fähigkeit ist der Skill nicht sinnvoll ausführbar;
- **optional** – verbessert den Workflow;
- **forbidden unless approved** – riskante Fähigkeit, die nicht automatisch genutzt werden darf.

## Typische Capabilities

Beispiele:

- Dateien lesen;
- Dateien schreiben;
- Webzugriff;
- Browser-/Renderzugriff;
- Shell / Codeausführung;
- GitHub lesen oder schreiben;
- Subagents / Parallelisierung;
- Screenshots;
- Netzwerkzugriff;
- externe Aktionen.

## Capability Detection

```text
bevorzugter Weg
→ Capability vorhanden?
   ├─ ja → verwenden
   └─ nein
        ↓
      definierter Fallback vorhanden?
        ├─ ja → transparent degradieren
        └─ nein → blocked / unverified melden
```

## Gute Fallbacks

Fallbacks erhalten möglichst die fachliche Disziplin.

Beispiele:

- keine Subagents → Research-Threads sequenziell statt parallel bearbeiten;
- kein Browser → visuelle Verifikation ausdrücklich als nicht durchgeführt markieren;
- kein ausführbarer Test → keine bestandene Verifikation behaupten;
- kein GitHub-Schreibzugriff → Patch/Änderungsvorschlag liefern statt Commit behaupten.

## Kein Capability-Theater

Nicht behaupten:

- einen Browser geprüft zu haben, wenn nur Code gelesen wurde;
- parallel delegiert zu haben, wenn keine Delegation verfügbar war;
- Tests ausgeführt zu haben, wenn nur Testcode betrachtet wurde;
- eine Quelle geöffnet zu haben, wenn nur ein Suchsnippet vorlag.

## Rechte und Least Privilege

Ein Skill soll nur die Rechte verlangen, die sein Auftrag wirklich benötigt.

Lesen und Bewerten benötigt nicht automatisch Schreib-, Netzwerk- oder Ausführungsrechte.

Riskante, irreversible oder extern sichtbare Aktionen bleiben an vorhandene Freigaberegeln gebunden.

## Portabilität

Toolnamen oder Clientmechanik nicht unnötig mit der fachlichen Logik vermischen.

Bevorzugt:

```text
Capability: Webzugriff
```

statt:

```text
muss Tool X mit Parameter Y verwenden
```

sofern die konkrete Plattform nicht selbst Gegenstand des Skills ist.

## Leitgedanke

> Ein portabler Skill beschreibt benötigte Fähigkeiten und ehrliche Fallbacks – nicht eine erfundene Idealumgebung.
