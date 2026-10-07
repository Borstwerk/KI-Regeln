# Run Replay und Reproduzierbarkeit

## Zweck

Ein gespeicherter Agentenlauf soll später überprüfbar sein, ohne still einen neuen Lauf mit neuen Modellantworten, verändertem Toolzustand oder anderer Umgebung als denselben Run auszugeben.

Der zentrale Unterschied lautet:

```text
gespeicherten Run prüfen
≠
gespeicherten Zustand fortsetzen
≠
Aufgabe erneut mit einem Modell ausführen
```

Diese drei Fälle brauchen getrennte Begriffe und Evidence.

## Drei Replay-Klassen

### 1. Audit Replay

Ein Audit Replay liest ausschließlich bereits gespeicherte Run-Artefakte und prüft deren Integrität, Reihenfolge und Beziehungen.

Typische Inputs:

- Manifest;
- Artefakt- und Fixture-Hashes;
- Trace;
- Actions;
- Evidence;
- gespeicherte Outputs;
- optional gespeicherter Workspace-/State-Snapshot.

Harte Grenze:

> Ein Audit Replay ruft kein Modell, kein externes Tool und keinen veränderlichen Providerzustand erneut auf.

Es kann beantworten:

- welcher Run geprüft wird;
- welche Artefakte unverändert vorliegen;
- welche Actions und Reads beobachtet wurden;
- welche Evidence gespeichert wurde;
- welche Gates technisch nachweisbar waren;
- welche Informationen fehlen.

Es kann **nicht** beweisen, dass ein heutiges Modell denselben Output erzeugen würde.

### 2. State Replay

Ein State Replay stellt einen gespeicherten, ausreichend vollständigen Laufzustand wieder her und rekonstruiert oder setzt einen deterministischen Abschnitt fort.

Dafür müssen die für den behaupteten Wiederherstellungsumfang relevanten Zustände eingefroren sein, beispielsweise:

- Konfiguration;
- Versions-/Runtime-Fingerprint;
- Input-/Fixture-Snapshot oder Hash;
- persistenter Working State;
- Checkpoint;
- Reihenfolge bereits abgeschlossener Entscheidungen;
- Zufallszustand, falls relevant;
- bereits abgeschlossene externe Antworten, falls deren Wiederverwendung fachlich zulässig ist.

Ein State Replay darf gespeicherte abgeschlossene Entscheidungen wiederverwenden. Sobald für einen noch offenen Schritt erneut ein Modell oder eine externe volatile Quelle aufgerufen wird, beginnt ein **neuer Ausführungsabschnitt** und muss als solcher markiert werden.

### 3. Fresh Re-execution

Eine Fresh Re-execution führt denselben oder einen äquivalenten Auftrag erneut aus.

Sie ist wichtig für:

- Behavioral Evals;
- Stabilitätsmessung;
- Regressionen;
- Modell-/Runtime-Vergleiche;
- pass^k oder wiederholte Runs.

Sie ist **kein Replay des alten Laufs**.

Auch bei gleichem Prompt, Modellnamen und Seed können sich ändern:

- Modellversion;
- Toolantworten;
- Web-/API-Zustand;
- Plugin-/Skill-Versionen;
- nicht kontrollierte Runtime-Details;
- Scheduling;
- Providerverhalten.

Deshalb:

```text
Audit Replay
→ Was ist im gespeicherten Run nachweisbar?

State Replay
→ Welchen gespeicherten Zustand kann ich ohne neue Entscheidung reproduzieren?

Fresh Re-execution
→ Wie verhält sich das System bei einer neuen Ausführung?
```

## Minimaler Run-Vertrag

Für einen prüfbaren Run sollen, soweit fachlich und datenschutzrechtlich sinnvoll, mindestens referenzierbar sein:

- `run_id`;
- `task_id` oder äquivalenter Auftrag;
- Repository-/Projektstand;
- Runner-/Harness-Version;
- angeforderte und soweit beobachtbar tatsächliche Modell-/Runtime-ID;
- Konfigurations- oder Execution-View-Hash;
- Fixture-/Input-Hashes;
- Trace-/Action-/Evidence-Artefakte;
- erzeugte Artefakte und deren Hashes;
- Status;
- bekannte Missingness / nicht beobachtbare Felder.

Für State Replay zusätzlich:

- `checkpoint_ref`;
- `state_ref`;
- `runtime_fingerprint`;
- Zufallszustand oder explizite Aussage, dass keiner relevant ist;
- Versionen zustandsprägender Tools;
- Regeln zur Wiederverwendung bereits abgeschlossener Tool-/Providerantworten.

## Reihenfolge und Commit-Grenzen

Ein Replay benötigt nicht jede interne Modellüberlegung. Wichtig sind stabile Commit-Grenzen.

Bevorzugt:

```text
Input / Observation gespeichert
→ Entscheidung oder Toolcall gespeichert
→ Ergebnis / Action gespeichert
→ fachlicher Zustand atomar committed
→ Checkpoint
```

Wenn ein Prozess zwischen zwei Commit-Grenzen abbricht, muss erkennbar sein:

- welcher Zustand definitiv gespeichert ist;
- welche Aktion eventuell extern stattgefunden hat;
- was sicher erneut ausgeführt werden darf;
- wo Idempotenz oder Human Review nötig ist.

Ein lokaler Checkpoint kann keine Idempotenz eines externen Providers garantieren.

## Request-/Response-Wiederverwendung

Bereits abgeschlossene Tool- oder Providerantworten dürfen nur dann als Replay-Evidence wiederverwendet werden, wenn mindestens klar ist:

- welcher exakte Request beziehungsweise Request-Hash dazu gehört;
- welche Response beziehungsweise Response-Hash gespeichert wurde;
- ob der Providerzustand für die spätere Aussage relevant ist;
- ob die Wiederverwendung fachlich zulässig ist.

Ein ähnlicher Request reicht nicht.

## Runtime Fingerprint

Eine reine Modellbezeichnung ist kein vollständiger Runtime-Fingerprint.

Je nach Aufgabe können relevant sein:

- Modell-ID;
- Runner-/CLI-Version;
- Harness-Version;
- Plugin-/Skill-Snapshot;
- Tool-/Adapter-Versionen;
- Interpreter-/Runtime-Version;
- Betriebssystem / Architektur;
- determinismusrelevante Flags;
- externe Engine-Versionen.

Nur speichern, was für die behauptete Reproduzierbarkeit tatsächlich relevant ist.

## Replay und deterministische Tools

Deterministische Tools verbessern Replaybarkeit, aber nur unter dokumentierten Bedingungen.

```text
gleicher Input
+ gleiche Toolversion
+ gleiche relevante Runtime
+ eingefrorene externe Inputs
→ reproduzierbarer Tooloutput möglich
```

Nicht automatisch:

```text
Tool heißt deterministisch
→ Ergebnis ist fachlich korrekt
```

Korrektheit bleibt am Acceptance Gate und an Evidence gebunden.

## Replay und externe Aktionen

Writes und externe Actions benötigen zusätzliche Vorsicht.

Ein Audit Replay darf sie **nicht erneut auslösen**.

Ein State Replay darf eine bereits ausgeführte externe Aktion nicht wiederholen, nur weil der lokale Checkpoint vor deren Bestätigung lag.

Dafür können nötig sein:

- Idempotency Keys;
- externe Action-/Receipt-IDs;
- gespeicherte Providerantworten;
- Reconciling gegen den aktuellen externen Zustand;
- Human Gate bei Ambiguität.

## Datenschutz

Replayfähigkeit ist kein Auftrag zur Vollprotokollierung.

Standard:

- Metadaten und Hashes bevorzugen;
- sensible Inhalte nur bei begründetem Bedarf speichern;
- Secrets verbieten;
- personenbezogene Daten minimieren;
- Aufbewahrungs- und Zugriffskonzept beachten;
- vollständige Prompts/Tooloutputs nur opt-in.

## Behavioral Harness

Der Behavioral Harness dieses Repositories unterstützt einen **Audit-Replay** für bereits paketierte Runs.

Der Audit-Replay:

- verifiziert zuerst Paket- und Artefakt-Hashes;
- liest ausschließlich gespeicherte Run-Artefakte;
- ruft kein Modell auf;
- ruft keine externen Tools auf;
- erzeugt keine neue Behavioral Evidence;
- rekonstruiert nur technisch beobachtbare Fakten aus dem gespeicherten Paket.

Eine erneute Golden-Task-Ausführung ist dagegen eine Fresh Re-execution.

## Qualitätscheck

Vor einer Replay-/Reproduzierbarkeitsbehauptung prüfen:

1. Welche Replay-Klasse ist gemeint?
2. Welche Zustände sind wirklich eingefroren?
3. Welche Artefakte sind hashgebunden?
4. Welche Versionsinformationen sind relevant?
5. Würde der Replay ein Modell, Netzwerk oder externe Aktion aufrufen?
6. Sind Commit-Grenzen und unklare Zwischenzustände sichtbar?
7. Sind bereits ausgeführte externe Aktionen gegen Doppelwirkung geschützt?
8. Welche Teile bleiben ausdrücklich nicht reproduzierbar?

## Leitgedanke

> Ein guter Replay wiederholt nicht blind die Welt. Er macht präzise sichtbar, welcher gespeicherte Zustand erneut prüfbar ist und wo eine neue Ausführung beginnt.
