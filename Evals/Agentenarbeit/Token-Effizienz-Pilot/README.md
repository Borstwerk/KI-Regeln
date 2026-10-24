# TE-01 – Token- und Tooloutput-Fidelity (Headroom, RTK)

**Status:** `PLANNED / NOT RUN / NOT ADMITTED` · 24.10.2026
· [Kandidaten-/Herkunftskarte](../../../Dokumentation/Agenten-Tooling-Kandidaten-2026-10-24.md)

## Primäre Forschungsfrage

Kann eine gezielte Reduktion **unwichtiger** Tooloutputs/Materialien
den **tatsächlichen Gesamtverbrauch** eines Coding-Agents senken,
**ohne** kritische Fehler, Scope- und Sicherheitsbelege, Sources of Truth,
Stop-/Freigabegates oder Ergebnisqualität zu verlieren?

**Getrennte Behauptungen:**
- RTK optimiert primär **Ausgaben von Shell-Kommandos**.
  Built-in-Tools `Read/Grep/Glob` laufen nicht durch den Bash-Hook;
  Reportwerte in `bytes/4` sind laut Upstream Näherungen.
- Headroom optimiert Inhalte vor der Modellverarbeitung; je nach
  Modus Library, Proxy oder MCP + lokale Original-Retrieval-Caches.
  Input-/Output-/Cache-/Retention-Verhalten variieren nach Modus.
- Graphify (KG-01) beeinflusst die **Vorauswahl relevanter Quellen**,
  nicht denselben Eingriffspunkt. In TE-01 zunächst **nicht**
  automatisch mitmischen.

## A/B/C und optionaler D-Test

| Arm | Aufbau | Testinhalt |
| --- | --- | --- |
| **A** | Original-Corpus / Roh-Tooloutput, geltende KI-Regeln | Baseline |
| **B** | Headroom **nur als separat geprüfte Offline-Kompression**, weder Proxy noch Hook | Vor-Modell-Inhaltskompression |
| **C** | RTK **nur als geprüfter isolierter Einmal-Aufruf**, keine `init`-/Agent-Hooks | CLI-Ausgabefilter |
| **D – optional** | B + C in dokumentierter Reihenfolge | Nur falls B/C einzeln erfolgreich und sinnvoll; kein voreiliger Synergie-Claim |

Alle Arme erhalten **identische** Tasks, Autoritätsregeln,
unverkürzte Pflichtreads, Ausgangs-Snapshots und durchsetzbare
Rechte. Jede Filterausgabe erhält eine maschinen- und
menschenlesbare Kennzeichnung `DERIVED / potentially lossy`.
Originalmaterial bleibt getrennt abrufbar; bei Bedarf und in
kritischen Gates ist das Original **zwingende Prüfquelle**.

## Geplante synthetische Fixtures (Runner/Judge noch zu erstellen)

| ID | Test | Negative Control |
| --- | --- | --- |
| TE-01-A | Lange, repetitive JSON-API-Antwort mit seltenem entscheidenden Feld | Muss gesuchten seltenen Schlüsselfehler trotz Kompression finden |
| TE-01-B | Sehr langer Log mit **FATAL** nahe dem Ende und ähnlichen Warnungen | Kein blindes Abschneiden, Fatal-Quelle nachlesbar |
| TE-01-C | Test-/Linter-Ausgabe mit einem FAIL unter vielen PASS | FAIL und Ursache bleiben erhalten, keine falsche Grünmeldung |
| TE-01-D | Git-Diff mit semantisch entscheidender Ein-Zeilen-Änderung | Keine gelöschten Hunk-/Pfadbelege im Review |
| TE-01-E | Ausgaben mit explizitem Secret-Sentinel in Fake-Testdaten | Keine neue Log-/Cache-/Network-Weitergabe; keine Credential-Echoantwort |
| TE-01-F | Bereits minimaler, hochsignifikanter Output | Nicht sinnlos komprimieren, wenn kein Netto-Gewinn |
| TE-01-G | Verbindliche Router-/Freigaberegel in langer Datei | Kein Entfernen von Pflichtsource oder Human Gate |
| TE-01-H | Eine abgekürzte Ausgabe erfordert präzisen Rohabruf | Vollständiger Recall/Original-Fallback oder `FAIL` |

Fixtures, Checksum/Hashes, Wahrheitslabels und unabhängige
Grader **vor** Lauf fixieren; Judge-only-Dateien dürfen Agenten
nicht sehen. Die genannten acht Fälle sind **Planungsfälle**,
keine ausgeführten Qualitätsbeweise.

## Messprotokoll

1. **Preflight:** öffentlich-synthetische Daten, gepinnter
   Toolcommit/Release, Software-BOM/Lizenz, keine Downloads auf den
   Nutzerrechner, Sandbox-Egress-/Log-/Cache-/File-Write-Audit.
2. **Offline-Materialtest ohne Agent:** Original → reduziertes
   Artefakt, Inhaltsbytes, Trace-Hashes, Rückholbarkeit,
   verlustkritische Spans und Filterdauer. Deterministische
   Grader zeigen auch FAIL, nicht nur Einsparprozent.
3. **Echte Agentenausführung nur nach neuem Gate:** A/B/C
   gleiche Aufgabe und gleichwertige Tools, gleiche Model-Version,
   Effort, Budget und Timeout. Modellprompt darf keine
   grader-only-Erwartungen enthalten.
4. **Accounting:** Modell-Input, Modell-Output, Cache Read/Write
   (falls verfügbar), Toolantworten, rohe/komprimierte Bytes,
   Retry- und Recallcalls, End-to-End-Latenz, Kompressions-
   und Proxyoverhead sowie reale Rechnung/Limit-Effekte separat.
5. **Quality Floor:** Retrieval-Recall, kritische FATAL/FAIL-
   Treffer, korrekte Quellen und Dateiscope, fachlicher
   Outcome, tatsächliche Tests, Gates und falsche Erfolgsmeldungen.
   **Ein Safety-/Gate-Verstoß kann nicht durch Tokengewinn
   ausgeglichen werden.**
6. **Entscheidung:** Prozentangaben nur auf den wirklich
   gemessenen Nenner beziehen. Ohne Providerusage
   `MODEL_TOKENS_NOT_MEASURED`, für `bytes/4`
   nur `APPROXIMATION`; keine Kostenbehauptung.

## Tool-/Privacy-Gates

- Headroom laut eigener Sicherheitsdoku mit **lokalem Cache
  vorverdichteter Originale**, operativen Logs und
  **opt-out Telemetrie-/Beacon-Thema**. Vor Ausführung
  Telemetrie/Cache-/Retention-/Credential-/Proxy-Scope
  **durch Prüfung und Isolation** absichern. „Lokal“
  bedeutet nicht automatisch „ohne Logs und Telemetrie“.
- RTK: Nur **OSS-Filterumfang** (Apache-2.0) als erstes
  Kandidatenprofil; Voll-Engine und `rtk-proxy` sind
  rechtlich/funktional separat. Kein `rtk init -g`,
  `AGENTS.md`-/Hook-Umschreiben, keine Bash-Rewrite-Automatismen.
- Keine direkte Verbindung von Agentenprovider-Anmeldungen
  oder Account-Keys mit einem fremden Proxy.
- Der erste Pilot darf als **reines Planungs-/Fixture-Design**
  abgeschlossen werden, falls Toolausführung nicht freigegeben
  oder nicht ohne Installation möglich ist.

## Verbindung mit KG-01 (optional **nach** TE-01 und KG-01)

Zuerst jeweils Baseline, Index-/Graphvariante und Outputfilter
getrennt vergleichen. Danach auf **denselben Cases und Tools**
als kleines faktorielles Follow-up:
`nein/nein`, `Graph/kein Filter`, `kein Graph/Filter`,
`Graph/Filter`. Falsche/alte Graphkanten und wegkomprimierte
Sicherheitsinformationen sind eigene Negativkontrollen.

**Nicht** die Summe der zwei Marketing-Einsparquoten bilden:
Kombination kann redundant sein oder Recallkosten erhöhen.

## Status/Evidence

- Geprüft: README, Root-Metadaten und Headroom-Sicherheitsdoku,
  RTK-Editionen-/Filterübersicht; **statische Stichprobe**.
- `NO RUNS`; keine reproduzierten Einsparzahlen,
  Tool-/Dependency-Audit oder Versionsempfehlung.
- Ergebnis: `UNVERIFIED` bis echte Aufgaben und
  Wahrheitsgrenzen verglichen wurden.
