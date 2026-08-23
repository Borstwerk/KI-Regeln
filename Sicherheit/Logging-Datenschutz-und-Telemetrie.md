# Logging, Datenschutz und Telemetrie

## Grundsatz

Observability soll Fehler und Agentenverhalten nachvollziehbar machen, ohne unnötig sensible Inhalte zu sammeln.

> So viel Telemetrie wie für Diagnose und Governance nötig – so wenig Inhaltsdaten wie möglich.

## Sinnvolle Metadaten

Je nach System beispielsweise:

- Task-/Run-ID;
- verwendeter Skill / Workflow;
- Modell-/Agentenkennung;
- Tooltyp und Dauer;
- Erfolgs-/Fehlerstatus;
- Token-/Kostenmetriken;
- Gate-/Freigabestatus;
- Artefakt- oder Commitreferenz.

## Inhaltsdaten

Prompts, Antworten, Toolargumente, Toolresultate oder komplette Dateien können sehr sensibel sein.

Vor Speicherung prüfen:

- ist der Inhalt für das Ziel wirklich nötig?
- enthält er Secrets oder personenbezogene Daten?
- wer kann ihn lesen?
- wie lange wird er gespeichert?
- kann eine redigierte oder aggregierte Form genügen?

## Kein Debug-Logging als Datenfriedhof

Nicht pauschal:

- komplette Auth-Header;
- ganze E-Mails;
- vollständige Nutzerdokumente;
- ungefilterte Browserinhalte;
- Secrets;
- komplette Prompt-/Completion-Historien

persistieren, nur weil die Plattform es technisch kann.

## Traceability

Ein sinnvoller Trace verbindet möglichst:

```text
Task
→ Skill / Workflow
→ relevante Toolaktionen
→ Evidence
→ Gate / Entscheidung
→ Output / Artefakt
```

ohne automatisch jeden Inhalt vollständig mitzuschneiden.

## Opt-in für tiefe Inhaltsaufzeichnung

Wenn vollständige Inhalte zur Diagnose erforderlich sind, sollte diese Aufzeichnung möglichst bewusst, begrenzt und transparent aktiviert werden.

## Leitgedanke

> Beobachtbarkeit ist ein Sicherheitswerkzeug – solange die Beobachtung nicht selbst zum Datenschutzproblem wird.
