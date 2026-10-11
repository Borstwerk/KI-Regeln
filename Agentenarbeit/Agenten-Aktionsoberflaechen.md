# Strukturierte Beobachtungs- und Aktionsoberflächen

## Zweck

Bei Agenten, die wiederholt Werkzeuge bedienen, ist eine begrenzte, überprüfbare Aktionsoberfläche häufig robuster als die freie Übersetzung von Prosatext in beliebige Toolaufrufe.

Einordnung:

```text
beobachtbarer Zustand
→ erlaubte Aktionen + Preconditions
→ begrenzte Ausführung
→ beobachtbares Resultat
→ Acceptance / Recovery
```

Diese Oberfläche ist ein **Runtime- und Toolvertrag**, kein neues Fachskill und keine zusätzliche Agentenrolle.

## Beobachtung (Observation)

Eine Observation soll, soweit verfügbar, kenntlich machen:

- `state_ref`: Referenz/Version des beobachteten Zustands;
- `timestamp` oder Sequenz (falls vorhanden);
- relevante Zustandsfelder mit Einheiten und Quellprovenienz;
- erkennbare Unsicherheit / fehlende Daten;
- `allowed_actions` für diesen Zustand;
- `evidence_refs` auf prüfbare Artefakte.

Visuelle, geometrische und textuelle Beobachtungen dürfen koexistieren. Ein Screenshot allein ist **nicht** die vollständige Systemwahrheit; Zeitpunkt, Kontext und sichtbare Grenzen gehören dazu.

## Aktionen

Jede angebotene Aktion sollte erklären:

| Feld | Aussage |
|---|---|
| `action_id` | konkrete, aufrufbare Aktion |
| `action_class` | READ, WRITE oder ACTION |
| `preconditions` | wann zulässig / sinnvoll |
| `scope` | erlaubte Ziele / Parametergrenzen |
| `effect` | erwartete Veränderung |
| `authorization` | vorhandene Freigabe oder erforderliches Human Gate |
| `idempotency` | ob Wiederholung sicher ist |
| `failure_contract` | Fehlercode / Retry- oder Escalation-Regel |

**Allowed Action ≠ Authorized Action.** Ein vom Interface angebotener Befehl erteilt dem Agenten keine neue Berechtigung. Sicherheits- und Projektgates bleiben vorgelagert.

## Closed Loop und Nachweis

```text
Observation O1 + Version
→ begrenzte Aktion A1
→ Toolreceipt / Fehlercode
→ Observation O2
→ Prüfe Zielinvariante + erlaubte Wirkung
→ PASS, PARTIAL, BLOCKED oder nächste begrenzte Aktion
```

Wenn die Beobachtung veraltet ist, darf eine zustandsabhängige Aktion nicht blind auf Basis von O1 wiederholt werden. Vor neuer Ausführung State-Ref erneut prüfen oder re-observe.

Ein erfolgreicher API-/Toolcall beweist weder Zielerreichung noch fachliche Korrektheit. Für riskante Wirkungen unabhängige Acceptance Evidence anfordern.

## Grenzen des Musters

- Nicht jede kleine Text- oder Leseaufgabe braucht ein Aktionspanel.
- Bei unstrukturierten Werkzeugen ein Adapter-Envelope statt künstlich erfundener Zustandsdetails.
- Keine versteckte zweite Entscheidungsschicht, die fachliche Skill-Trigger ersetzt.
- Die Oberfläche darf Toolrechte nicht erweitern und keine Rohdaten als vertrauenswürdige Instruktion behandeln.

## Inspiration und Transfer

[RoboHarness (BinceQu)](https://github.com/BinceQu/RoboHarness) koppelt visuelle Keypoints, geometrische Constraints, primitive Aktionen und zurückgemeldeten Zustand. Für KI-Regeln wird **nur das allgemeine Interface-Muster** übernommen: Beobachtung, erlaubte Aktion, gemessene Wirkung, Gate. Kein Robotik-Framework, keine Simulations- oder GPU-Dependency.

Weitere Verträge: `../Skill-Engineering/Agent-Tool-Vertraege.md` und `Observability-und-Traceability.md`.
