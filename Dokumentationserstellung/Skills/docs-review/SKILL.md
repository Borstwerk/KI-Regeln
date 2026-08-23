# Skill: docs-review

## Zweck

Dokumentation unabhängig auf fachliche Korrektheit, Dokumenttyp, Verifikation, Informationsarchitektur, Sprache und Drift prüfen.

## Vorgehen

1. Bestimme Review-Scope und Zielgruppe.
2. Klassifiziere Artefakttyp und Dokumentationsmodus.
3. Identifiziere relevante Sources of Truth.
4. Prüfe zuerst fachlich falsche, gefährliche oder veraltete Aussagen.
5. Prüfe fehlende Voraussetzungen, Schritte, Parameter oder wichtige Grenzen.
6. Verifiziere wichtige Beispiele, Befehle und Links, soweit möglich.
7. Prüfe Informationsarchitektur und Scanbarkeit.
8. Prüfe Terminologie, Klarheit und Stil.
9. Ordne Findings nach Schweregrad.
10. Bei beauftragter Verbesserung: korrigiere gezielt und führe betroffene Checks erneut aus.

## Ergebnisformat

Für relevante Findings:

- Dokument / Stelle;
- Schweregrad;
- Problem;
- Source of Truth oder Gegenbeleg;
- empfohlene Korrektur;
- Verifikationsstatus.

## Regeln

- Review ist nicht automatisch Rewrite.
- Keine Stil-Nits vor fachlichen Blockern priorisieren.
- Abweichung von einem Template ist nicht automatisch ein Fehler.
- Starke bestehende Struktur schützen.
- Fehlende Source of Truth als Unsicherheit melden, nicht kompensieren.

## Leitgedanke

> Dokumentation ist freigabefähig, wenn ihr Inhalt zuverlässig nutzbar ist – nicht wenn sie nur professionell klingt.
