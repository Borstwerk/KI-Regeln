# Claudex: begrenzter Read-only-Cross-Review an PR #88

**Stand 17.10.2026: PLAN_ONLY / CLAUDE_REVIEW_NOT_RUN.** Dieser Eintrag dokumentiert die Auswahl und den konkreten reproduzierbaren Versuch; er ist **kein** ausgeführter Claude-/Claudex-Lauf, kein Cross-Model-PASS und keine Freigabe für eine allgemeine Agentenplattform.

## Entscheidung und Quellen

- **Testobjekt:** bereits gemergter [KI-Regeln PR #88](https://github.com/Borstwerk/KI-Regeln/pull/88), *GT-01-Produktqualität*: Codex-authored Pilot/Treiber, eingefrorene SQL-Fixtures, neun Produktkriterien und gespeicherte Antworten. Unveränderliches Diff: Basis `620f6643cb898c915b4b1d3eb8c00d984e6dcf44`, Ziel/Merge `2e64d9c90b19a6b375360d27e1155b1fce9c3097`.
- **Externer Kandidat:** [chaseai-yt/claudex-loop](https://github.com/chaseai-yt/claudex-loop), gesichteter Upstream-Commit `53cddc42e39346fb8c6d5d612281a3b1add14e66`. Relevante Quellen: [`skills/claudex-loop/SKILL.md`](https://github.com/chaseai-yt/claudex-loop/blob/53cddc42e39346fb8c6d5d612281a3b1add14e66/skills/claudex-loop/SKILL.md), [`references/runtime.md`](https://github.com/chaseai-yt/claudex-loop/blob/53cddc42e39346fb8c6d5d612281a3b1add14e66/skills/claudex-loop/references/runtime.md), [`scripts/runner.py`](https://github.com/chaseai-yt/claudex-loop/blob/53cddc42e39346fb8c6d5d612281a3b1add14e66/skills/claudex-loop/scripts/runner.py). Externe Lizenz [MIT mit Third-Party-Hinweisen](https://github.com/chaseai-yt/claudex-loop/blob/53cddc42e39346fb8c6d5d612281a3b1add14e66/LICENSE). **Kein Upstream-Code ins KI-Regeln-Repo übernommen.**
- **Methode:** genau **eine** frische Claudex-`inspect`-Sitzung mit **Claude als Prüfer** des durch Codex erstellten PR-Diffs. Keine Änderung am PR, keine Implementierungsphase, keine Iterationsschleife. Die historische Codex-Autor-/Selbstprüfung ist **keine unabhängige Codex-Judge-Baseline**; deshalb nur „neue Claude-Findings gegenüber dokumentiertem Codex-Stand“, nicht „bewiesener zweifach unabhängiger Review-Vergleich“.

## Prüffrage und vorher festgelegte Kriterien

Findet der zweite Anbieter einen **neuen, konkret nachvollziehbaren Defekt** im eingefrorenen PR #88, der in den bisherigen Pilot- und PR-Berichten nicht erfasst ist? Bewertet werden:

| Dimension | Akzeptanz/Beobachtung |
| --- | --- |
| Quellentreue | GT-01-Originalantworten und JSON-Evidence werden nicht still ersetzt; Pins und eingefrorene Kriterien geprüft |
| Testtreiber | Nur bestehender Subscription-Login; feste Zwei-Sitzungsgrenze; Read-only und keine stillen Wiederholungen/Providerwechsel |
| Auftragsgrenze | Keine Judge-Metadaten im Agentenprompt; kein versehentliches `AGENTS.md`-Routing als natürlicher Routing-Pass behauptet |
| Findings | Jeder Defekt mit Pfad/Zeile, Ursache, reproduzierbarem Negativfall und minimaler Korrekturrichtung; positive/negative Fälle werden getrennt |
| Fehlsignale | Falschpositive, unklare Hinweise, außerhalb des Scopes liegende Ideen und nicht prüfbare Empfehlungen explizit zählen |
| Aufwandsbilanz | CLI-Versionen, tatsächlicher Modell-/Kontokontext soweit beobachtbar, Laufzeit, mögliche Usage, Fehler und benötigte Human-Arbeit dokumentieren |

**Anerkennung:** Ein sprachlich plausibles `APPROVED` ist **kein** Qualitätsbeweis. Ein behaupteter Bug zählt als `VERIFIED` nur nach unabhängiger lokaler Prüfung am eingefrorenen Code und überprüfbarer Gegenprobe; ohne diese `UNVERIFIED`. Der Test darf auch mit null neuen verifizierten Findings enden. Keine Erfolgspflicht, keine nachträgliche Änderung der Kriterien.

## Sicherheits- und Umfangsgrenzen

- Vorhandene **Claude-Code- und Codex-CLI-Abos** benutzen, keine API-Keys, keine direkten Modell-APIs, kein modell- oder providerübergreifender Fallback. Auth-Status vorab prüfen; fehlender Zugriff → `BLOCKED`.
- Es geht nur um **öffentlichen** Repo-Code/den angeführten PR. Keine privaten lokalen Projekte, Credentials, untracked privaten Dateien, sensitiven Logs oder Chatverläufe zum Reviewer schicken.
- Upstream **vor Ausführung** an den obigen SHA pinnen und relevante Dateien (`SKILL.md`, Runner, Runtime-Kontrakt) im ausführenden Host reviewen. Nicht automatisiert installieren, kein `curl | sh`, keine Global-Konfiguration ändern.
- Reviewer `inspect` nutzt laut Upstream Claude `--safe-mode`, leeres MCP und nur Read/Glob/Grep; diese Beschränkung im tatsächlichen CLI-Protokoll verifizieren. Host-Rechte und CLI-interne Sitzungs-/Cache-Schreibvorgänge bleiben davon unberührt. **Read-only bezieht sich auf Projektmutationen, nicht auf fehlenden Netzwerkverkehr/Provider-Datenübertragung.**
- **Genau ein** Claude-Reviewversuch, vorgeschlagener Timeout 180 s, keine automatische Wiederholung, keine Build-/Fix-/Commit-/Push-/Merge-Aktion. Bei inkompatiblen Flags, Quota-Mangel, falschem Git-Stand oder verweigerten Rechten `BLOCKED`, keine Lockerung der Grenzen.
- Ausführungsartefakte (Prompt, CLI stdout/stderr, Result, IDs) ausschließlich lokal **außerhalb** des Checkouts und außerhalb der versionierten Projektdateien speichern. Vor Veröffentlichung redigieren; keinen Agenten-Reasoning-Trace oder Credentials committen.

## Operator-Rezept (nur auf dem vorhandenen autorisierten Entwicklungsrechner)

Die folgenden PowerShell-Zeilen sind ein **nach Review manuell** auszuführendes Rezept, **nicht** der Nachweis ihrer Ausführung. Benötigt einen lokalen KI-Regeln-Checkout inklusive beider PR-88-Commits, Git, Python 3.10+, eine installierte und angemeldete Claude-Code-CLI und ein überprüftes Claudex-Loop-Checkout. Keine Pakete werden von diesem Dokument automatisch installiert.

1. In deinem lokalen KI-Regeln-Checkout die benötigten SHAs überprüfen: `git cat-file -t 620f6643cb898c915b4b1d3eb8c00d984e6dcf44` und `git cat-file -t 2e64d9c90b19a6b375360d27e1155b1fce9c3097` müssen `commit` melden. Fehlt etwas, keinen anderen Ref substituieren.
2. Ein **separates, temporäres Git-Worktree** mit `git worktree add --detach <TEMP-PR88-WORKTREE> 2e64d9c90b19a6b375360d27e1155b1fce9c3097` anlegen; die aktiven Codex-Dateien und `main` nicht anfassen. Worktree-Status prüfen: HEAD exakt obiger Merge-Commit, `git status --short` leer.
3. Externes, eigens überprüftes Claudex-Loop-Checkout auf `53cddc42e39346fb8c6d5d612281a3b1add14e66` fixieren; `claude --version`, `claude auth status`, optional `codex --version`/`codex login status` ohne Modellaufruf prüfen. Wird ein benötigtes CLI-/Policy-Flag nicht unterstützt, abbrechen.
4. Einen **kurzen Review-Plan als UTF-8-Datei außerhalb des Worktrees** schreiben: „Prüfe nur den Diff von PR #88 gegen Basis 620f6643… auf reproduzierbare Code-, Test-, Evidence- und Rechtefehler. Keine Änderungen, kein Build, keine externen Aktionen. Melde auch Nichtbefunde, Coverage und Grenzen. Priorisiere echte Defekte; bisherige PR-Berichte sind Vergleichsmaterial, keine Wahrheit.“
5. Nach **konkreter Freigabe der einen Subscription-Review-Sitzung** folgenden festen Befehl ausführen, wobei Platzhalter echte lokale absolute Pfade sind:

```powershell
python '<CLAUDEX-CHECKOUT>\skills\claudex-loop\scripts\runner.py' inspect `
  --host codex --builder codex `
  --repo '<TEMP-PR88-WORKTREE>' `
  --plan '<PRIVATE-TEMP>\PR88-REVIEW-PLAN.md' `
  --base 620f6643cb898c915b4b1d3eb8c00d984e6dcf44 `
  --artifacts '<PRIVATE-TEMP>\claudex-artifacts' `
  --timeout 180
```

6. `result.json` und die im Artefakt erfassten Argumente kontrollieren: tatsächlicher Reviewer `claude`, Modus `inspect`, Basis-SHA, verwendete Tool-Policy, Zeit/Exit, Findings und Unvollständigkeiten. **Nicht** den Exitcode oder `APPROVED` allein als Nachweis übernehmen.
7. Jedes Finding gegen exakt denselben Diff manuell/mit vorhandenen **modellfreien** Checks prüfen. Codex-Protokoll/PR-#88-Reviewpunkte nur danach vergleichen. Keine automatische Reparatur. Human-Gate vor jeder zusätzlichen Sitzung oder Änderung.

## Ergebnistabelle – erst nach tatsächlichem Lauf ausfüllen

| Feld | Aktueller Stand |
| --- | --- |
| Quellstand/Upstream-Pin | Festgelegt wie oben |
| Runner/Reviewer-Preflight | `NOT RUN` |
| Claude-Review und Rohevidence | `NOT RUN` |
| Verifizierte zusätzliche Defekte | `NOT RUN` (nicht 0) |
| Nicht bestätigte/False-Positive-Findings | `NOT RUN` |
| Vergleich mit Codex-Autorbefunden | `NOT RUN` |
| Aufwand/Kontingent | `NOT RUN` |
| Agenten-/Skill-Maturity/B2-Gates | Unverändert |

**Entscheidungsregel:** Erst nach echtem Read-only-Review beurteilen, ob Claudex Loop als **optionaler externer Cross-Review-Workflow** Mehrwert bietet. Der Name oder ein grüner Dummy-Test ist keine Qualitäts- oder Security-Evidence. Kein Claudex-Skill automatisch in den Katalog übernehmen.
