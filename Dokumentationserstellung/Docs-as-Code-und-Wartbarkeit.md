# Docs as Code und Wartbarkeit

## Zweck

Dokumentation soll denselben Änderungs- und Reviewfluss nutzen können wie das Produkt, das sie beschreibt.

## Grundidee

Docs as Code bedeutet typischerweise:

- Plain-Text-Formate wie Markdown;
- Versionskontrolle;
- Issues oder Tasks;
- Review über Diffs;
- automatisierte Prüfungen;
- gemeinsame Ownership von Entwicklern und Dokumentationsverantwortlichen.

## Dokumentation mit Änderungen koppeln

Bei jeder relevanten Produktänderung prüfen:

```text
Feature / Fix / Architekturänderung
        ↓
ändert sich dokumentiertes Verhalten?
        ↓
ja → betroffene Doku im selben Arbeitskontext aktualisieren
```

Nicht darauf vertrauen, dass eine spätere separate Doku-Runde die Änderung irgendwann entdeckt.

## Dokumentationspflicht als Teil von Done

Je nach Projekt kann „Done“ beinhalten:

- README aktualisiert;
- Reference aktualisiert;
- Changelog ergänzt;
- ADR erstellt oder superseded;
- Runbook angepasst;
- Beispiele erneut geprüft.

Nicht jedes Commit braucht Doku. Die Prüfung, **ob** Doku betroffen ist, sollte aber bewusst stattfinden.

## Ownership

Für wichtige Dokumenttypen sollte klar sein, wer Aktualität verantwortet.

Beispiele:

- API-Doku → API-/Produktteam;
- Runbook → Betrieb / On-Call-Team;
- README → Repository-Maintainer;
- ADR → Architektur-/Entscheidungsverantwortliche;
- Onboarding → Teamverantwortliche.

Ownership bedeutet nicht, dass nur diese Person schreiben darf.

## Review-Cadence nach Risiko

Nicht jede Doku altert gleich schnell.

Mögliche Trigger:

- nach jeder relevanten Releaseänderung;
- nach Incident;
- nach Architekturänderung;
- bei UI-Redesign;
- periodisch für Onboarding und Runbooks;
- bei gemeldeten Nutzerproblemen.

Starre globale Fristen sind weniger wichtig als passende Änderungs- und Reviewtrigger.

## Automatisierbare Checks

Wo sinnvoll:

- Broken-Link-Check;
- Markdown-Linting;
- Prose-Linting;
- Terminologieprüfung;
- Codebeispiele testen;
- OpenAPI-/Schema-Validierung;
- Spellcheck;
- veraltete interne Links erkennen.

Automatisierung darf fachliche Prüfung nicht ersetzen.

## Vale als mögliches Harness

Ein Prose-Linter wie Vale kann projektlokale Regeln technisch prüfen, etwa:

- Terminologie;
- verbotene oder unerwünschte Formulierungen;
- Stilkonventionen;
- Schreibweisen;
- Formatmuster.

Dabei gilt derselbe Grundsatz wie beim allgemeinen Harness Engineering:

> Was zuverlässig automatisch überprüfbar ist, sollte möglichst nicht nur als Textregel existieren.

Linterregeln nicht abschalten oder verwässern, nur um einen Agentenlauf grün zu bekommen.

## Doku-Diff wie Produkt-Diff behandeln

Beim Review fragen:

- Was wurde fachlich geändert?
- Warum?
- Welche Quelle trägt die Änderung?
- Wurde eine alte Aussage entfernt oder widerspricht sie jetzt an anderer Stelle?
- Sind Links, Beispiele und Begriffe weiterhin konsistent?

## Leitgedanke

> Dokumentation ist versioniertes Produktwissen – kein Nebenprodukt, das nach dem Release zufällig gepflegt wird.
