# Upstream-Audit – Trustworthy Runtime Contracts – 2026-10-07

## Zweck

Dieser Audit prüft aktuelle HypeRadar-Funde gegen den bestehenden Stand von KI-Regeln.

Geprüft wurden:

- BootLoops Toolkit + Skills;
- trustworthy-agent-simulation;
- catbus;
- HyperFrames;
- hello-agent-system als breite Gegencheckliste.

Ziel war ausdrücklich **nicht**, neue Vendor-Skills zu sammeln. Übernommen werden nur Konzepte, die im lokalen Regelwerk noch eine reale Lücke schließen.

## Kurzurteil

| Upstream | Relevanter Fund | Lokale Entscheidung |
|---|---|---|
| BootLoops | Tool Stewardship + Acceptance vor Vertrauen | **übernehmen als allgemeinen Agent-Tool-Vertrag** |
| trustworthy-agent-simulation | persistenter Runzustand + modellfreier Replay | **übernehmen als Run-Replay-Vertrag** |
| catbus | stabile JSON-/Fehler-/Retry-/Capability-Verträge | **übernehmen als Agent-Tool-Interface-Muster** |
| HyperFrames | deterministische codebasierte Video-Runtime + versionierte Skills | **bestehenden Motion-Workflow härten, keinen neuen Skill bauen** |
| hello-agent-system | breite Produktionsschichten | **keine neue Abstraktion; vorhandene Bereiche decken den Stoff bereits ab** |

## 1. BootLoops

Repositories:

- https://github.com/BootLoops-ai/bootloops
- https://github.com/BootLoops-ai/skills

Geprüfter Stand:

- Toolkit: `66b680ce742e654cfe86da4f072a69061fe182b1`;
- Skills: `ca892277dcf0468d995f0036f3bd6d753a8afe7d`;
- Lizenz: MIT für Code/Skills am geprüften Stand.

### Bereits vorhanden

KI-Regeln hatte vor diesem Audit bereits:

- falsifizierbare Verification;
- Positive-/Negative-Control-Idee;
- held-out/independent Evidence;
- Capability Detection;
- Script Dependency Contract;
- Inputs/Outputs/Evidence;
- Fresh Evidence.

### Tatsächlich neuer Hebel

`tool-stewardship` macht aus einem Tool nicht nur eine Capability, sondern einen **vertrauensfähigen Agentenvertrag**:

```text
wann passt das Tool?
→ was bedeutet der Output?
→ wie sieht Failure aus?
→ welchen Test muss das Resultat bestehen?
```

Zusätzlich nützlich:

```text
use as-is
→ patch/extend
→ wrap
→ erst dann neu bauen
```

Das wird lokal nicht als neuer Skill kopiert, sondern in `Skill-Engineering/Agent-Tool-Vertraege.md` generalisiert.

## 2. trustworthy-agent-simulation

Repository:

https://github.com/apromisedland/trustworthy-agent-simulation

Geprüfter Stand:

- Commit: `5c504f5bd9faf380dd7ace97d72899f92d16d132`;
- Lizenz: Apache-2.0.

### Bereits vorhanden

KI-Regeln hatte:

- Trace-/Action-/Evidence-Modelle;
- Run Packages;
- Hash-Integrität;
- Working State / Checkpoints als Konzept;
- Behavioral Fresh Re-execution.

### Tatsächlich neuer Hebel

Der Upstream trennt persistente Runwahrheit sehr sauber:

```text
Observation journaled
→ Decision journaled
→ Resolution
→ State + Metrics atomar committed
→ Checkpoint
```

Besonders wichtig:

- Replay liest committed Snapshots;
- Replay ruft kein Modell neu auf;
- Config und relevante RNG-Zustände werden gespeichert;
- bereits gespeicherte Entscheidungen können Recovery tragen;
- identische abgeschlossene Providerantworten dürfen nur zum exakt passenden Request wiederverwendet werden.

Lokal wird daraus die Trennung:

```text
Audit Replay
≠ State Replay
≠ Fresh Re-execution
```

Der Behavioral Harness bekommt deshalb einen modellfreien `replay-run`.

Nicht übernommen:

- AgentScope;
- Mesa;
- Town-Simulation;
- SQLite als Pflichtpersistenz.

## 3. catbus

Repository:

https://github.com/cv-cat/catbus

Geprüfter Stand:

- Commit: `8c09a0c540dc69bb0ef4a45100063623cfaf2f66`;
- Lizenz: MIT.

### Bereits vorhanden

KI-Regeln hatte:

- Error Contracts;
- READ / WRITE / ACTION;
- Human Gates;
- Capability Routing;
- Least Privilege;
- Machine-readable Contracts.

### Tatsächlich neuer Hebel

catbus zeigt eine besonders agentenfreundliche Kombination:

- ein stabiles Ergebnis-Envelope;
- stabile Fehlercodes;
- Exitcodes als grobe Maschinenklasse;
- `hint` für Recovery;
- Capability Registry als Source of Truth;
- IDs/URLs zum Chaining;
- `NOT_IMPLEMENTED` versus `UNSUPPORTED`;
- Auth-/Risk-Control-Fehler mit anderer Retry-Semantik;
- gefährliche Aktionen brauchen explizite Bestätigung.

Lokal wird daraus kein catbus-Adapter, sondern der allgemeine `Agent-Tool-Vertrag`.

Nicht übernommen:

- Plattformautomation;
- Credentials/Auth-Implementierung;
- Browser-Fingerprinting;
- Scraping-/Social-API-Verhalten.

## 4. HyperFrames

Repository:

https://github.com/heygen-com/hyperframes

Geprüfter Stand:

- Commit: `1e711b087dca254fa021f0c16006197c138d1884`;
- Lizenz: Apache-2.0.

### Bereits vorhanden

Der lokale Workflow `Workflows/Codebasierte-Motion-Graphics-und-Video.md` nennt HyperFrames bereits als mögliche Runtime und enthält:

- seekbares Timing;
- Renderpfad;
- Frame-/Snapshot-QA;
- Playback-QA;
- Canonical-/Derived-Media-Verträge;
- Provenienz;
- Render-/Publishing-Gates.

### Tatsächlich neuer Hebel

Der Upstream macht deutlich, dass für Reproduzierbarkeit getrennt betrachtet werden müssen:

- CLI-/Runtime-Version;
- Plugin-Version;
- Skill-Snapshot;
- mutable Marketplace-/Branch-Updatepfad;
- Node-/FFmpeg-/Projektabhängigkeiten.

Eine gepinnte CLI beweist keinen gepinnten Skillinhalt, wenn Skill-/Marketplace-Inhalte separat aktualisiert werden.

Lokal wird deshalb nur das optionale HyperFrames-Runtime-Profil im bestehenden Workflow ergänzt.

Nicht übernommen:

- die 21 HyperFrames-Skills;
- Marketplace-Installationszwang;
- HyperFrames als universelle Video-Runtime.

## 5. hello-agent-system

Repository:

https://github.com/heaven999b/hello-agent-system

Geprüfter Stand:

- Commit: `857823c11d790be44509300e6c333d3fcf226ffa`;
- Lizenz: MIT.

Der Kurs/Referenzstack deckt sehr breit ab:

- Tools;
- Context/Memory;
- Orchestration;
- Reliability;
- Security;
- Observability;
- Evals;
- Distributed Execution;
- Costs;
- RAG;
- Release Ops.

Der Gap-Check ergab keine zentrale fehlende lokale Abstraktion. Die Themen sind bereits auf mehrere bewusst getrennte KI-Regeln-Bereiche verteilt.

Entscheidung:

> keine neue Skill-/Framework-Schicht nur wegen eines vollständigen Lehrplans.

## Warum keine neuen Skills entstehen

Die Upstreams liefern überwiegend **Runtime-/Harness-Prinzipien**, keine neuen fachlichen Jobs.

Deshalb:

```text
Agent-Tool-Vertrag
→ Skill-Engineering / Runtime Contract

Run-Replay-Vertrag
→ Agentenarbeit / Harness

HyperFrames
→ vorhandener Motion-Workflow / Runtime-Profil

hello-agent-system
→ Gap-Check, keine neue lokale Abstraktion
```

Neue Skills würden hier eher Ownership verdoppeln.

## Upstream-Monitoring

Keiner der geprüften Repositories wird durch diesen Audit zu einer harten laufenden Dependency von KI-Regeln.

Die lokalen Regeln sind bewusst generalisiert und commitbezogen dokumentiert.

Deshalb werden die Repositories **nicht automatisch** als aktiv zu synchronisierende mutable Upstreams behandelt. Wenn später konkrete Adapter, Plugins oder kopierte Skill-Inhalte direkt von einem Upstream abhängen, ist diese Entscheidung neu zu prüfen.

## Leitgedanke

> Gute Upstream-Recherche endet nicht mit mehr Abhängigkeiten. Sie endet mit einer kleineren Zahl besserer lokaler Verträge.
