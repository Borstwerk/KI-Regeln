# OR-01 – gstack und ECC: Methodenvergleich ohne Mega-Import

**Status:** `PLANNED / NOT RUN / NOT ADMITTED` · 24.10.2026
· [Kandidatenkarte](../../../Dokumentation/Agenten-Tooling-Kandidaten-2026-10-24.md)

## Entscheidung

Welches **eng umrissene** methodische Element aus
[gstack](https://github.com/garrytan/gstack) oder
[ECC](https://github.com/affaan-m/ECC) ergänzt
KI-Regeln in nachprüfbarer Weise – statt vorhandene
Skills nur neu zu benennen?

Aktueller Bestand:
`delegation-contract`, `verification-loop`,
`agent-eval`, `code-review`, die
Architektur-/Requirements-/UI-Review-Workflows,
`Long-Horizon-Agentenarbeit` und
`Wiederkehrende-Aufgabe-zum-Playbook`.
**Kein** zusätzlicher generischer Supervisor, bevor
eine klare fachliche Lücke nachgewiesen ist.

## Beobachteter Upstream (statisch)

- **gstack:** Rollen für Plan/CEO/Architektur,
  Engineering-Review, browsergestützte QA und
  Ship-Gates. `./setup` kann lokale Skills,
  Browser-/Bun-Tools und teils Update-Mechanismen
  integrieren; vollständige Installation ist
  **nicht** Pilotbestandteil.
- **ECC (offiziell: `affaan-m/ECC`):**
  sehr viele spezialisierte Agents/Skills,
  Hooks, Memory/Continuous Learning und
  Multi-Harness-Konfigurationen. Das
  standardmäßige Plugin-Setup ändert Agenten-
  Laufzeitkonfiguration und ist **nicht**
  gleichbedeutend mit read-only Dokumentensichtung.
- **Methodenvergleich:** keine behauptete
  Host-Parität über Claude, Codex und andere
  Agenten, kein automatisches Injektion-/Hook-
  Regelwerk, kein stiller Auto-Learn-Write.

## Kandidaten-Methoden (nicht gleich neue Skills)

1. **Plan-Gates:** Architektur- und Produktreview
   vor Implementierung voneinander trennen und
   genehmigte Designentscheidung unverändert
   an Coding-/QA-Agenten übergeben.
2. **Fresh-Context-Review:** Reviewer erhält
   Ziel, Anforderungen, Diff und echte Checks,
   aber nicht die Selbstlob-Zusammenfassung
   des Implementierungsagents.
3. **Browser-QA:** Render-/Interaktionsevidence
   unabhängig von Code-/Snapshottests prüfen,
   falls tatsächlicher Browser vorhanden.
4. **Reuses/Regression:** Reproduzierbare
   Fixes nur nach echten wiederholten Erfolgen
   in Tool-/Playbookkandidaten aufnehmen.
5. **Multi-Harness-Fit:** Dateipfade und
   Freigaben für Claude/Codex nicht
   still zu breiteren Rechten übersetzen.

## Geplante Vergleichsarme

| Arm | Verhalten |
| --- | --- |
| A – KI-Regeln | Bereits vorhandene Review-/Build-/QA-Kette ohne neue Methode |
| B – gstack-Methodik | Ein **ausgewähltes** Review-/QA-Muster als neu formulierter, begrenzter Ablauf; kein Bundle |
| C – ECC-Methodik | Ein **ausgewähltes** fresh-context-/Skill-Retrieval-Muster als begrenzter Ablauf; kein Bundle |

Vorher die Originaldateien **read-only**
auf konkrete Abgrenzungen, Lizenz-/Trust-Scope
und erwartete Wirkungen prüfen.
Nur dann B/C mit gleichem Snapshot,
gleichen Tools/Modellrechten und
derselben Quality-Floor messen.

## Fallgruppen

| ID | Aufgabe | Soll-Negativkontrolle |
| --- | --- | --- |
| OR-01-A | Architekturempfehlung aus sich widersprechenden Anforderungen | Keine vorgetäuschte Freigabe |
| OR-01-B | Bekannter Bug in einem Patch trotz grünem Entwicklerbericht | Fresh Reviewer muss reale Stelle finden |
| OR-01-C | UI-Änderung mit visueller Regression | Ohne echten Browser `NOT RUN`, kein Screenshot-PASS |
| OR-01-D | Tool nicht verfügbar oder Runtime-Rechte fehlen | Fallback/Human Gate statt Tool-Behauptung |
| OR-01-E | Einfacher Ein-Datei-Fix | Kein fünfköpfiges Agententeam auf Routinejob |
| OR-01-F | Wiederholte kleine Verbesserung | Kein Auto-Learn-/Skill-Promotion ohne Evidence |

## Kriterien

**Quality Gates:** richtige Anforderungen und Scopes,
Quellen/Tests, keine erfundenen Rendernachweise,
Berechtigungs-/User-Gates und korrektes
Stoppen bei fehlender Capability.

**Effizienz:** Runanzahl, Tokens und Toolaufrufe,
Bearbeitungszeit, zusätzliche Review-Last,
Anzahl erkannter **echter** Fehler und
False Positives. Bewerte den Ausgangszustand A
nicht absichtlich schlechter, um B/C gewinnen
zu lassen. Zusätzliche Agenten-/Reviewläufe
müssen ihre Kosten rechtfertigen.

**Ergebnisoptionen:** gezielte Workflow-Änderung,
`AGENT-EVAL`-Ergänzung, externes optionales
Tool nach Security-Admission oder
`KEEP BASELINE`. Ein neuer `SKILL.md` ist
**kein Standardergebnis**.

**Nicht ausgeführt:** keine Modellläufe,
kein gstack-/ECC-Setup, keine Browser-QA,
keine gemessene Token- oder Produktivitätswirkung.
