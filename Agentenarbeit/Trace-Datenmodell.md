# Trace-Datenmodell für Agentenarbeit

## Zweck

Dieses Modell konkretisiert `Observability-und-Traceability.md` mit einer gemeinsamen, toolneutralen Struktur für relevante Agentenereignisse.

Es ist kein Zwang, jeden Workflow vollständig zu instrumentieren.

## Kernobjekte

```text
Task
→ Run
→ Skill / Workflow
→ Tool Event / Evidence
→ Gate / Decision
→ Artifact
→ Outcome
```

## Minimale IDs

Wo technische Observability genutzt wird, helfen stabile Referenzen:

- `task_id` – fachlicher Auftrag oder Task;
- `run_id` – konkreter Agentenlauf;
- `parent_run_id` – bei Subagenten / Delegation;
- `skill_id` – aktivierter Skill;
- `workflow_id` – optionales Recipe;
- `artifact_ref` – Diff, Datei, Report, Build oder anderes Ergebnis;
- `gate_id` – Freigabe-/Stop-Gate.

## Ereignistypen

Empfohlener Basissatz:

```text
TASK_STARTED
SKILL_ACTIVATED
WORKFLOW_PHASE_STARTED
TOOL_CALLED
TOOL_FAILED
EVIDENCE_RECORDED
VALIDATION_PASSED
VALIDATION_FAILED
GATE_REQUESTED
GATE_APPROVED
GATE_REJECTED
SCOPE_CHANGED
FALLBACK_USED
TASK_BLOCKED
TASK_COMPLETED
TASK_FAILED
```

Projekte dürfen ergänzen.

## Tool Event

Nicht zwingend Toolargumente und Ergebnisse vollständig loggen.

Oft reichen:

- Tooltyp;
- Operation;
- Zeitpunkt / Dauer;
- Status;
- Zielreferenz;
- ggf. redigierte Evidence-ID.

## Evidence

Evidence soll referenzierbar sein, beispielsweise:

```text
type: test-result
ref: ci://run/123
status: pass
```

oder:

```text
type: source
ref: https://example.org/source
claim: C-17
status: supported
```

## Gates

Gate-Ereignisse sollen mindestens erkennen lassen:

- welches Gate;
- welcher Scope;
- warum angefordert;
- Status;
- wer oder welcher definierte Prozess freigegeben hat;
- welches Artefakt damit freigegeben wurde.

Keine sensiblen Identitätsdaten erfassen, wenn eine technische Referenz genügt.

## Datenschutz

Vollständige Prompts, Completions, Toolargumente oder Toolresultate sind **kein Pflichtbestandteil** dieses Modells.

Sie können für Debugging nützlich, aber zugleich sensibel und sehr groß sein.

Bevorzugt:

```text
Metadaten standardmäßig
+ Inhaltsdaten nur bei begründetem Bedarf
+ Redaction
+ begrenzte Aufbewahrung
```

## Kompatibilität

Das Modell soll sich bei Bedarf auf Observability-Systeme wie OpenTelemetry abbilden lassen, ohne davon abhängig zu sein.

Insbesondere passen dazu Konzepte wie:

- Modell-/Operationserkennung;
- Toolcalls;
- Laufzeiten;
- Tokenmetriken;
- verschachtelte Spans;
- optionale Inhaltsaufzeichnung.

## Verhältnis zu Projektwahrheit

Ein Trace dokumentiert **was passiert ist**.

Er ersetzt nicht:

- Spezifikation;
- Architekturentscheidung;
- Source of Truth;
- kanonische Dokumentation.

## Leitgedanke

> Traceability verbindet Arbeitsschritte und Evidence – ohne die komplette Arbeitswelt in Logs zu kopieren.
