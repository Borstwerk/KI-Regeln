# Agent-Tool-Verträge

## Zweck

Ein wiederverwendbares Tool für Agenten braucht mehr als einen Funktionsnamen und ein Eingabeschema.

Der Agent muss zuverlässig erkennen können:

- **wann** das Tool passt;
- **welche Capability** es wirklich bietet;
- **welche Wirkung** ein Aufruf hat;
- **was** sein Output bedeutet;
- **wie Fehler** maschinenlesbar behandelt werden;
- **wann** ein Ergebnis belastbar genug ist, um darauf weiterzuarbeiten.

Ein Agent-Tool-Vertrag verbindet deshalb Capability-, Schnittstellen-, Sicherheits- und Verification-Disziplin.

## Wann dieser Vertrag sinnvoll ist

Besonders sinnvoll für:

- wiederverwendbare CLI-/Script-Tools;
- Runtime-Adapter;
- Plugins / MCP-Server / Apps;
- Validatoren und Renderer;
- deterministische Berechnungswerkzeuge;
- Tools, deren Ergebnis weitere Agentenschritte steuert;
- Tools mit Write-/Action-Wirkung.

Nicht jede einmalige Hilfsfunktion braucht einen vollständigen Vertrag.

## Die acht Fragen

Ein agentenfreundliches Tool soll möglichst acht Fragen beantworten:

1. **Was tut es?**
2. **Wann soll der Agent es verwenden?**
3. **Wann gerade nicht?**
4. **Was darf der Aufruf verändern?**
5. **Wie sieht ein erfolgreicher Output aus?**
6. **Wie sehen Failure und Recovery aus?**
7. **Welche Prüfung muss das Ergebnis bestehen, bevor es als belastbar gilt?**
8. **Welche Version/Runtime hat dieses Ergebnis erzeugt?**

## Capability vor Toolname

Bevorzugt:

```text
Capability: exact-arithmetic
Action class: READ / local compute
Verification: known-answer self-test + independent cross-check
```

statt:

```text
Benutze immer Tool X
```

Toolnamen gehören in den Runtime-Adapter, wenn die Plattform nicht selbst Teil der fachlichen Aufgabe ist.

## Selection Contract

Ein Agent soll nicht aus dem Toolnamen erraten müssen, wann es passt.

Mindestens beschreiben:

- `use_when`;
- `near_miss` beziehungsweise angrenzende Fälle;
- relevante Preconditions;
- benötigte Capabilities / Dependencies.

Ein Capability-Index oder eine Registry ist stärker als eine lose Sammlung nicht auffindbarer Scripts.

## Action Class und Wirkung

Mindestens zwischen folgenden Wirkungen unterscheiden:

- `READ` – liest oder berechnet ohne persistente externe Änderung;
- `WRITE` – verändert persistenten Zustand;
- `ACTION` – löst extern sichtbare oder geschäftlich wirksame Wirkung aus.

Zusätzlich sinnvoll:

- mutating ja/nein;
- idempotent ja/nein/conditional;
- benötigt Human Gate;
- externe Kosten;
- Netzwerk;
- Secret-/Credential-Bedarf.

Ein Tool darf seine Wirkung nicht hinter einem harmlosen Namen verstecken.

## Machine-readable Output

Agentenwerkzeuge profitieren von einem stabilen, maschinenlesbaren Ergebnisvertrag.

Ein mögliches neutrales Muster:

```json
{
  "ok": true,
  "status": "complete",
  "data": {},
  "evidence": [],
  "error": null
}
```

Bei Fehler:

```json
{
  "ok": false,
  "status": "blocked",
  "data": null,
  "evidence": [],
  "error": {
    "code": "AUTH_REQUIRED",
    "message": "Anmeldung erforderlich",
    "retry": "human-required",
    "hint": "Führe den dokumentierten Login-Schritt aus.",
    "detail": {}
  }
}
```

Das exakte Envelope ist projektspezifisch. Wichtig sind stabile Semantik und maschinenlesbare Felder.

Freitext kann ergänzen, aber nicht der einzige Fehlervertrag sein.

## Fehler- und Retry-Semantik

Ein Toolfehler soll nicht nur sagen, **dass** etwas fehlgeschlagen ist.

Empfohlene Recovery-Klassen:

- `never` – derselbe Aufruf soll nicht automatisch wiederholt werden;
- `safe` – Retry unter denselben Bedingungen ist zulässig;
- `conditional` – Retry erst nach benannter Bedingung;
- `human-required` – Nutzer-/Operatorhandlung nötig;
- `unsupported` – Capability fehlt; nicht durch Wiederholung heilbar.

Beispiele:

```text
RISK_CONTROL
→ retry: never / conditional
→ nicht in Schleife hämmern

AUTH_REQUIRED
→ retry: human-required

NOT_IMPLEMENTED
→ retry: unsupported

TRANSIENT_NETWORK
→ retry: safe oder conditional mit Budget
```

Retry-Klasse ist Teil des Contracts, nicht spontane Agentenintuition.

## Chaining

Wenn Toolresultate weitere Toolaufrufe speisen sollen, stabile Referenzen bevorzugen:

- IDs;
- URLs;
- Artefaktrefs;
- Cursor;
- Versionen;
- Evidence-Refs.

Nicht den Agenten zwingen, eine wichtige Referenz aus Fließtext zurückzuparsen.

## Determinismus richtig benennen

Ein Tool kann unter bestimmten Bedingungen deterministisch sein.

Dann dokumentieren:

- relevante Input-Hashes;
- Tool-/Runtime-Version;
- determinismusrelevante Parameter;
- externe Inputs;
- Seed, falls vorhanden;
- welche Teile trotzdem volatil bleiben.

```text
deterministisch
≠
korrekt
≠
vollständig
≠
autorisiert
```

Ein deterministischer Fehler bleibt ein Fehler.

## Verification Class

Das Tool soll benennen, **welche Art von Prüfung** für sein Ergebnis passt.

Mögliche Klassen:

- `schema` – Struktur/Typen;
- `known-answer` – Fall mit bekanntem Ergebnis;
- `negative-control` – absichtlich falscher Fall muss scheitern;
- `independent-route` – zweiter ausreichend unabhängiger Prüfweg;
- `bounded-numeric` – Fehler-/Toleranzgrenze;
- `contract-test` – Consumer-/Provider-Vertrag;
- `external-state` – Abgleich mit realem externem Zustand;
- `human-review` – semantische/visuelle Prüfung;
- `none` – kein eigener belastbarer Validator verfügbar; Ergebnis bleibt entsprechend unverified.

Mehrere Klassen können kombiniert werden.

## Acceptance Gate vor Vertrauen

Wenn ein Toolresultat eine relevante Claim-, Release- oder Entscheidungsgrundlage bildet, soll vor dem Vertrauen klar sein:

- welcher Check gilt;
- welcher Status als Pass zählt;
- welche Evidence erwartet wird;
- ob der Check tatsächlich scheitern kann.

Besonders starke Kontrollen:

- Known-good / positive control;
- Known-bad / negative control;
- held-out Evidence;
- unabhängiger Prüfweg.

Ein Validator, der nie nachweislich einen falschen Fall abgelehnt hat, liefert schwächere Evidence.

## Known-answer Self-Test

Neue oder wesentlich geänderte Tools sollten nach Möglichkeit zuerst auf einem kleinen Fall mit bekanntem Ergebnis laufen.

Das prüft gleichzeitig:

- Installation;
- Interface-Verständnis;
- Toolzustand;
- offensichtliche Drift;
- Ergebnisinterpretation.

Ein erfolgreicher Self-Test beweist nicht jede spätere Eingabe, ist aber stärker als ein ungetesteter erster Produktivlauf.

## Capability Registry

Bei vielen Tools eine Registry bevorzugen, aus der nach Möglichkeit erzeugt oder geprüft werden:

- Capability-Liste;
- Help/Reference;
- Status `implemented | partial | planned | unavailable`;
- Action Class;
- Auth-/Permission-Bedarf;
- Output Contract;
- Version.

So wird vermieden, dass Help, Agent-Skill und Implementierung still auseinanderlaufen.

## Contract und Runtime trennen

Der portable fachliche Kern kann fordern:

```text
Capability: deterministic-render
Verification: frame + playback
Action class: local-write
```

Der Runtime-Adapter kann konkret binden:

```text
HyperFrames 1.x
Node 22
FFmpeg ...
```

Damit bleibt der Skill portabel und der Toolvertrag trotzdem prüfbar.

## Sicherheitsgrenzen

Ein maschinenlesbarer Vertrag ist keine Autorisierung.

Weiterhin gilt:

```text
Capability vorhanden
≠
Write erlaubt
≠
Action erlaubt
≠
Human Gate erfüllt
```

Credentials, Login, externe Veröffentlichung und risikoreiche Aktionen behalten ihre eigenen Regeln.

## Anti-Patterns

Nicht ausreichend:

- Erfolg und Fehler nur als Freitext;
- Exitcode 0 trotz fehlgeschlagener Prüfung;
- Tooloutput ohne Einheiten/Status;
- `retry` ohne Budget und Failure-Klasse;
- generisches `ERROR` für jeden Zustand;
- Write-/Action-Wirkung ohne explizite Kennzeichnung;
- „deterministisch“ ohne Bedingungen/Version;
- Tool wird durch seinen eigenen Output zertifiziert;
- Agent darf Acceptance-Kriterien nach Sicht des Ergebnisses passend machen.

## Leitgedanke

> Ein agentenfreundliches Tool macht nicht nur die richtige Aktion möglich. Es macht Auswahl, Wirkung, Fehler und Vertrauen explizit.
