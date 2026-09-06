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

## `inhaltsprovenienz-review`

**Kurz gesagt:** Prüft eine konkrete Datei oder einen Inhalt read-only auf belegbare Provenienz- und Metadatensignale.

**Sinnvoll bei:** C2PA/Content Credentials, EXIF/XMP, Dokumenteigenschaften, Generator-/Softwarefeldern, ungewöhnlichen Unicode-Artefakten oder der Frage, welche Herkunftshinweise tatsächlich im Artefakt stecken.

**Nicht dafür:** Marker zu entfernen, menschliche Urheberschaft zu beweisen oder Detector-Scores zu optimieren.

**Typisches Ergebnis:** Befunde nach Evidence-Klasse, Confidence, False-Positive-Grenzen, nicht prüfbare Klassen und Residual Risk.

## `metadaten-hygiene`

**Kurz gesagt:** Bereinigt eigene oder ausdrücklich autorisierte Dateien gezielt von unnötigen oder sensiblen Metadaten.

**Sinnvoll bei:** GPS-/Geräteinformationen, unbeabsichtigten Autor-/Softwarefeldern oder anderen konkreten Privacy-/Sharing-Metadaten, nachdem Remove-/Keep-Scope und Erhaltungspflichten klar sind.

**Nicht dafür:** sichtbare Fremd-Watermarks, Detector-Evasion, statistische Text-Watermark-Zerstörung oder das Entfernen verpflichtender Attribution/Disclosure.

**Typisches Ergebnis:** begrenztes Change Set, bereinigte Kopie soweit möglich, Re-Inspection und Residual-Risk-Bericht.

## Auswahlhilfe

```text
Neuen Skill bauen
→ skill-authoring

Bestehenden Skill fachlich/methodisch prüfen
→ skill-review

Skill auf Sicherheitsrisiken prüfen
→ skill-security-review

Verdächtige externe Instruktion analysieren
→ prompt-injection-review

Tool-/Berechtigungsmodell prüfen
→ tool-permission-review

Welche Provenienz-/Metadatensignale stecken in dieser Datei?
→ inhaltsprovenienz-review

Eigene/autorisierte Datei gezielt für Privacy/Sharing bereinigen
→ erst bei Bedarf inhaltsprovenienz-review
→ metadaten-hygiene
```

Bei kombiniertem Review + Clean ist `Workflows/Inhaltsprovenienz-und-Metadatenhygiene.md` der bevorzugte Ablauf.

## Zusammenspiel

Vor höherer Skill-Maturity kann ein sinnvoller Pfad sein:

```text
skill-authoring
→ skill-review
→ Evals
→ bei relevanten Capabilities skill-security-review
→ Maturity-Entscheidung
```

Für Datei-Provenienz gilt zusätzlich:

```text
inhaltsprovenienz-review
→ Evidence + Grenzen
→ autorisiertes Remove/Keep-Set
→ metadaten-hygiene
→ re-inspect
```

Review erweitert keine Änderungsautorisierung. Fehlende oder entfernte Metadaten sind kein Beweis für menschliche Urheberschaft oder vollständige Provenienzfreiheit.
