# PT-01 – Kleine interne Gegenhypothese (nur Experiment B)

**Status:** `EXPERIMENT ONLY`. Dies ist **kein** globaler Skill, keine
Änderung an KI-Regeln und kein importierter Ponytail-Text.

Für den konkreten Auftrag, **nach** gültigem KI-Regeln-Routing:

- **Implementieren (A):** Betroffene Aufrufer, aktuelle Helfer,
  Standardbibliothek und Plattformfunktionen prüfen; nur
  die kleinste **vollständige** Änderung wählen. Keine
  neue Dependency/Schicht, wenn vorhandene Arbeit reicht.
- **Diff-Review (B):** Konkreten Fehlerfall und indirekt
  betroffenen Aufrufer nachprüfen. Sicherheit, Datenverlust,
  erwartete Last, Tests vor Kompaktheit bewerten. Keine
  bloßen Stil-Findings.
- **Repository-Audit (C):** Entry Points und reale
  Datenflüsse risikoorientiert lesen. Befunde mit
  konkretem Source-Pfad, Zeile und reproduzierbarem
  Bruch priorisieren, keine spekulative „große Neuarchitektur“.
- **Technische Schulden (D):** Bewusste `shortcut:`-
  Quellcode-Kommentare als akzeptierte Grenzen lesen,
  fehlende Wiedervorlage markieren, Docs-Beispiele
  nicht als Code-Schulden melden.

**Nie wegoptimieren:** Nutzeranforderungen, freigegebene
Projektarchitektur, Safety, Validierung, Berechtigungen,
Datenhaltbarkeit, Accessibility, unabhängige Test-Evidence
oder KI-Regeln-Gates.

Ein Review ist read-only; ein Audit ist read-only.
Keine automatische Änderungen, Dependency-Installation
oder neue globale Anweisungen. `NOT RUN` bleibt `NOT RUN`.
