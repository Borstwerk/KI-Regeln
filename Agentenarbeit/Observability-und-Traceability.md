# Observability und Traceability

## Zweck

Agentenarbeit soll nicht nur ausführbar, sondern später nachvollziehbar sein.

Observability bedeutet in diesem Bereich, dass relevante Zustände, Prüfungen und Agentenaktionen sichtbar werden. Traceability verbindet Auftrag, Agentenlauf, Ergebnis und Freigabe zu einer nachvollziehbaren Spur.

## Abgrenzung zu System-Observability

Diese Datei behandelt **Agenten- und Arbeitsprozess-Observability**.

`../Reliability-und-System-Observability/` behandelt dagegen die Runtime-Observability von laufenden Services, Jobs, Datenflüssen und technischen Dependencies.

```text
Agentenarbeit / Observability
→ Auftrag, Agentenlauf, Toolereignisse, Artefakte, Evidence, Gates

Reliability / System-Observability
→ Service Health, Nutzerwirkung, Runtime-Telemetrie, Dependencies, Incidents
```

Beide Bereiche können strukturierte Events, IDs, Logs oder Traces verwenden. Die fachliche Source of Truth und die zu beantwortenden Fragen sind jedoch unterschiedlich.

## Grundprinzip

> Ein nicht nachvollziehbarer Agentenerfolg ist schwächer als ein prüfbarer Agentenlauf.

Nicht jede interne Überlegung muss protokolliert werden. Relevant sind die beobachtbaren Entscheidungen, Aktionen, Artefakte und Nachweise, die für Review, Diagnose oder Verantwortung benötigt werden.

## Minimale Traceability-Kette

Für relevante Agentenarbeit sollte nach Möglichkeit nachvollziehbar bleiben:

```text
Intent / Requirement
→ Delegation / Plan
→ Agentenlauf
→ Tool- und Prüfereignisse
→ Artefakt / Diff
→ Evidence
→ Review
→ Freigabe
```

Die konkrete technische Umsetzung bleibt projektspezifisch.

## Was beobachtbar sein sollte

Je nach Risiko und Aufgabe beispielsweise:

- welcher Auftrag oder welche Requirement-ID bearbeitet wurde;
- welche kanonischen Quellen herangezogen wurden;
- welcher Scope freigegeben war;
- welche Dateien oder Artefakte verändert wurden;
- welche relevanten Tools oder Validatoren ausgeführt wurden;
- welche Tests bestanden oder fehlgeschlagen sind;
- wo eine Freigabe angefordert oder erteilt wurde;
- welche Stop- oder Eskalationsbedingung ausgelöst wurde;
- welche offenen Unsicherheiten zurückblieben.

## Keine Vollprotokollierung um ihrer selbst willen

Mehr Logs bedeuten nicht automatisch bessere Observability.

Nicht sinnvoll ist beispielsweise:

- jedes gelesene Token dauerhaft speichern;
- jede triviale Zwischenaktion protokollieren;
- sensible Daten in Logs kopieren;
- riesige Agententraces erzeugen, die niemand auswerten kann.

Beobachtbarkeit soll Fragen beantworten, nicht neue Datenhalden schaffen.

## Strukturierte Ereignisse bevorzugen

Wenn möglich, wichtige Agentenereignisse strukturiert erfassen.

Beispiel:

```text
TASK_STARTED
SCOPE_CONFIRMED
TEST_FAILED
GATE_REQUESTED
GATE_APPROVED
REPAIR_STARTED
VALIDATION_PASSED
TASK_COMPLETED
```

Zusätzlich können relevante IDs, Zeitpunkte, Artefakte oder Statuswerte gespeichert werden.

Damit lassen sich Abläufe später leichter filtern und prüfen als mit reinem Fließtext.

## Traceability zu Code und Artefakten

Bei Softwarearbeit können je nach Projekt sinnvoll sein:

- Requirement-ID in Commit oder Pull Request;
- Verweis auf Issue oder Plan;
- Link oder ID des Agentenlaufs;
- Test- oder CI-Nachweis;
- Build- oder Release-Artefakt;
- Reviewergebnis.

Die Agentensession selbst ist keine neue fachliche Quelle der Wahrheit. Sie erklärt den Weg, nicht den gültigen Sollzustand.

## Datenschutz und Geheimnisse

Observability darf keine unnötigen sensiblen Daten erzeugen.

Insbesondere prüfen:

- Secrets und Tokens nicht protokollieren;
- personenbezogene Daten nur bei tatsächlicher Notwendigkeit erfassen;
- Produktionsdaten nicht ungefiltert in Agentenlogs übernehmen;
- externe Tool-Ausgaben auf sensible Inhalte prüfen;
- Aufbewahrung und Zugriff an Risiko und Zweck anpassen.

## Observability für Loops

Bei wiederholten Agentenloops sollte erkennbar sein:

- wie viele Versuche erfolgt sind;
- welcher Fehler jeweils den nächsten Repair ausgelöst hat;
- ob Fortschritt entsteht oder derselbe Fehler nur variiert wird;
- welches Stop-Budget verbleibt;
- warum der Loop abgeschlossen oder eskaliert wurde.

Damit lässt sich unterscheiden zwischen produktiver Iteration und Endlosschleife.

## Observability für Multi-Agent-Systeme

Bei mehreren Agenten zusätzlich nachvollziehbar machen:

- welcher Agent welchen Graphknoten bearbeitet;
- welche Übergabe-Evidence vorlag;
- welche Workspaces oder Branches zugeordnet waren;
- welche Abhängigkeiten bereits erfüllt waren;
- wo Konflikte oder gemeinsame Ressourcen existierten.

## Qualitätscheck

Für einen Agentenworkflow prüfen:

1. Können Auftrag und Ergebnis später miteinander verbunden werden?
2. Sind relevante Tests, Gates und Fehlerzustände sichtbar?
3. Ist der tatsächliche Scope nachvollziehbar?
4. Kann ein Reviewer erkennen, warum ein Knoten als fertig gilt?
5. Sind Logs kompakt und strukturiert genug, um wirklich ausgewertet zu werden?
6. Werden Secrets oder unnötige personenbezogene Daten vermieden?
7. Ist klar, welche Information Prozesshistorie und welche Information kanonische Projektwahrheit ist?

## Leitgedanke

> Der Agent soll nicht gläsern sein. Der Arbeitsprozess soll nachvollziehbar sein.