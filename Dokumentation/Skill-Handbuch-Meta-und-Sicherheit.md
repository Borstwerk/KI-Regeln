# Skill-Handbuch – Skill Engineering und Sicherheit

Diese Ergänzung erklärt die Meta- und Security-Skills in verständlicher Form.

## `skill-authoring`

**Kurz gesagt:** Baut einen neuen Skill nach unseren zentralen Qualitätsregeln.

**Sinnvoll wenn:** ein wiederkehrender Arbeitsprozess als eigener Skill entstehen oder ein bestehender Skill grundlegend neu strukturiert werden soll.

**Nicht dafür:** konkrete Projektregeln einfach in einen zentralen Skill zu verwandeln.

**Typisches Ergebnis:** klare Verantwortung, Description/Trigger, Inputs/Outputs, Capabilities/Fallbacks, Evalfälle und vorgeschlagene Maturity.

## `skill-review`

**Kurz gesagt:** Unabhängiger Qualitätsreview für einen bestehenden Skill.

**Sinnvoll wenn:** ein Skill neu ist, wesentlich geändert wurde oder vor einer höheren Maturity geprüft werden soll.

**Nicht dafür:** automatisch den geprüften Skill umzuschreiben.

**Typisches Ergebnis:** priorisierte Funde zu Scope, Triggern, Verträgen, Capabilities, Komposition und Evalbarkeit plus Freigabeurteil.

## `skill-security-review`

**Kurz gesagt:** Sicherheitsreview speziell für Skills.

**Sinnvoll wenn:** ein Skill externe Quellen, Scripts, Netzwerk, Secrets, Schreib-/Ausführungsrechte oder externe Aktionen berührt.

**Nicht dafür:** allgemeine fachliche Qualität ohne Sicherheitswirkung zu beurteilen.

**Typisches Ergebnis:** Security Findings mit Severity, Evidence und Freigabeurteil.

## `prompt-injection-review`

**Kurz gesagt:** Prüft, ob fremder Inhalt versucht, vom Dateninhalt zur Agentenanweisung zu werden.

**Sinnvoll bei:** Webseiten, Dateien, E-Mails, Issues, Tooloutput oder Retrieval-Inhalten mit verdächtigen Instruktionen.

**Nicht dafür:** die gefundenen Instruktionen testweise auszuführen.

**Typisches Ergebnis:** Trust-Boundary-Analyse und sicherer Umgang mit der Quelle.

## `tool-permission-review`

**Kurz gesagt:** Prüft, ob ein Agent oder Skill wirklich genau die benötigten Rechte bekommt.

**Sinnvoll bei:** neuen Tools, Netzwerkzugriff, Schreibrechten, Codeausführung, Produktionszugriff oder externen Aktionen.

**Nicht dafür:** nur zu erklären, was ein Tool grundsätzlich kann.

**Typisches Ergebnis:** Capability-Matrix mit Purpose, minimalen Rechten, Fallback und Gate.

## Auswahlhilfe

```text
Neuen Skill bauen
→ skill-authoring

Bestehenden Skill fachlich/metodisch prüfen
→ skill-review

Skill auf Sicherheitsrisiken prüfen
→ skill-security-review

Verdächtige externe Instruktion analysieren
→ prompt-injection-review

Tool-/Berechtigungsmodell prüfen
→ tool-permission-review
```

## Zusammenspiel

Vor höherer Skill-Maturity kann ein sinnvoller Pfad sein:

```text
skill-authoring
→ skill-review
→ Evals
→ bei relevanten Capabilities skill-security-review
→ Maturity-Entscheidung
```
