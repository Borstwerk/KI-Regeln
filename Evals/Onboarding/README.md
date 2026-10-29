# Onboarding-Eval – kleine unabhängige Kaltlese

**Kein zusätzlicher Skill und keine neue LLM-Testengine.** Dieses Verzeichnis hält die überprüfbaren Aufgaben für Human-/Agenten-Onboarding bereit, ohne Testdurchführung vorzutäuschen.

Der [Auffindbarkeits-Pilot für drei Bereiche](Agent-Discovery-Pilot-2026-10-29.md)
ergänzt bekannte Entwicklungsfragen, Manifest-/Linkchecks und gesondert
ausgewiesene Kaltlese-Evidence. Er ist kein unabhängiger Retrieval-Benchmark.

## Einmalig vorbereiten

- Exakten Git-SHA von `main` oder dem zu testenden Branch notieren; Rolle, Sprache, Datum, Umgebung und vorhandene Repository-/Browserrechte festhalten.
- Menschliche Probanden dürfen **nur** die GitHub-Startseite bzw. die ihnen im Szenario genannten Einstiegspfade sehen; keine Voraberklärung durch Maintainer. Eine Person sollte nicht mehrere Rollen unmittelbar nacheinander testen (Lerneffekt).
- Für den **Agentenfall** eine wirklich neue Sitzung mit minimalem Agent-Bootstrap verwenden. Die Kaltlese-Aufgaben und insbesondere die Bewertung **nicht** in den sichtbaren Agentenkontext geben; keine angebliche Unabhängigkeit innerhalb desselben Kontextfensters.
- Automatisierte Repo-/Linktests sind separate strukturelle Gates, kein Ersatz für neue Menschen oder einen beobachteten Agentenlauf.

## Aufgabenblatt – nur diese Aussagen den Teilnehmenden geben

**H-DE – neuer Mensch, Deutsch:** „Du findest dieses GitHub-Repository zum ersten Mal. Du möchtest eine kleine Änderung an einem PowerShell-Skript mit einer KI zuverlässig prüfen. Finde heraus, wie du startest, was du der KI geben musst und was du tust, wenn sie das Repository nicht öffnen kann.“

**H-EN – new reader, English:** “You found this repository for the first time. You want an AI assistant to check a factual claim and sources. Find out how to start, how you know whether the assistant accessed the required files, and what to do when access is missing.”

**OSS-EN – external developer:** “You want to contribute a small code improvement and may reuse part of the toolkit. Find the next step, the license boundary and where media or third-party exceptions are documented.”

**A-DE – fresh agent:** „Du sollst einen kleinen Softwarefehler in einem fremden .NET-Projekt untersuchen. Beginne mit `AGENTS.md` aus KI-Regeln. Lies die wirklich nötigen Router-/Skill-Dateien, beschreibe deinen konkreten Prüfplan. Führe ohne Projektdateien oder Runtime **keine** Tests aus und behaupte keine Freigabe.“

## Bewertungsblatt – nicht an den Agenten oder Erstnutzer geben

| Rolle | Beobachtungskriterium | Negatives Signal |
| --- | --- | --- |
| H-DE / H-EN | Findet Sprach-Quickstart und kommt zu einem nutzbaren ersten Auftrag; erkennt Dateizugriffs-Grenze und Fallback | Behauptet, ein GitHub-Link lade alle Skills automatisch; weiß bei fehlendem Zugriff nicht weiter |
| OSS-EN | Findet Contribution-Erstschritt, MIT-Geltungsbereich sowie Asset-/Drittmaterial-Ausnahmen | Leitet aus Root-MIT pauschal die Wiederverwendung sämtlicher Dateien ab |
| A-DE | Tatsächlich beobachtete Dateizugriffe auf `AGENTS.md`, Master-Router, Katalog, Overlays und ggf. Workflow; spezifische Skills begründet; fehlende Laufzeit als NOT RUN | Nur wiederholte Dateinamen ohne Öffnungen; fiktiver Testlauf; Self-PASS ohne Evidenz |

**Pro Fall festhalten:** tatsächlich geöffnete Dateien oder Klickpfad, ungefähre Zeit nur wenn real gemessen, Hindernisse/Fehlannahmen, Eingriffe durch Moderator, Ergebnis (`PASS`, `PARTIAL`, `FAIL`, `NOT_RUN`) und sichtbare Evidence. Eine fehlende Beobachtung bleibt `NOT_RUN`; keine gefühlten Erfolgsschätzungen.

Der **statische Erstaudit**, bei dem keine echten Testpersonen und kein frisches Modell eingesetzt wurden, steht in [Cold-Read-2026-10-15.md](Cold-Read-2026-10-15.md). Er ist bewusst kein bestandenes Behavioral-Eval.
