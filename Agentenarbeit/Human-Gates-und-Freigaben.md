# Human Gates und Freigaben

## Zweck

Agenten können viele Arbeitsschritte selbstständig durchführen. Bestimmte Entscheidungen sollen trotzdem bewusst außerhalb des autonomen Loops bleiben.

Ein Human Gate ist ein definierter Punkt, an dem ein Mensch oder eine ausdrücklich benannte Freigabeinstanz entscheidet, ob der nächste Schritt erlaubt ist.

## Grundprinzip

> Autonomie ist kein Ersatz für Verantwortung.

Ein Agent kann analysieren, planen, implementieren, testen und Vorschläge machen. Die Verantwortung für risikoreiche oder irreversible Entscheidungen bleibt bei der vorgesehenen Freigabeinstanz.

## Why Loop und How Loop

Für agentische Arbeit ist eine Trennung zwischen zwei Ebenen hilfreich:

### Why Loop

Der äußere Loop klärt:

- welches Problem gelöst werden soll;
- welches Ergebnis tatsächlich gewünscht ist;
- welche Risiken akzeptabel sind;
- welche Architektur- oder Produktentscheidungen gelten;
- ob Scope verändert werden darf;
- wann ein Ergebnis freigegeben wird.

Diese Ebene bleibt bei Mensch, Team oder einer ausdrücklich definierten Governance.

### How Loop

Der innere Agentenloop klärt innerhalb des freigegebenen Rahmens:

- wie ein bestätigtes Ziel technisch erreicht wird;
- welche kleine Implementierungsreihenfolge sinnvoll ist;
- wie ein Fehler innerhalb des Scopes diagnostiziert und repariert wird;
- welche erlaubten Werkzeuge eingesetzt werden.

Der Agent darf im How Loop selbstständig sein. Er darf damit aber nicht unbemerkt den Why Loop übernehmen.

## Human on the Loop

Menschliche Kontrolle muss nicht bedeuten, jede einzelne Agentenaktion freizugeben.

Ein guter Prozess hält Menschen oder eine definierte Freigabeinstanz **auf dem äußeren Loop**:

```text
Ziel / Intent
→ Grenzen und Gates definieren
→ Agent arbeitet autonom innerhalb des Rahmens
→ Evidence und Observability
→ Review
→ Entscheidung über nächsten äußeren Schritt
```

Das reduziert Mikromanagement, ohne Verantwortungsübergänge unsichtbar zu machen.

## Typische Human Gates

Eine ausdrückliche Freigabe ist besonders sinnvoll vor:

- Änderungen mit Datenverlust- oder Migrationsrisiko;
- Änderungen an Sicherheits- oder Berechtigungsregeln;
- neuen externen Abhängigkeiten;
- Architekturentscheidungen mit großer Reichweite;
- Änderungen öffentlicher Schnittstellen oder persistierter Formate;
- Push, Merge, Release oder Deployment, sofern nicht ausdrücklich automatisiert freigegeben;
- Aktionen gegen Produktionssysteme;
- Veröffentlichung externer Inhalte;
- Scope-Erweiterungen, die nicht Teil des ursprünglichen Auftrags waren.

Die konkrete Liste bleibt projektspezifisch.

## Ein Gate braucht einen definierten Eingang

Eine Freigabe soll nicht auf einem bloßen „fertig“ basieren.

Vor einem Gate sollten je nach Aufgabe vorliegen:

- Ausgangsanforderung oder Ziel;
- tatsächlicher Diff oder erzeugtes Artefakt;
- Testergebnisse und andere Nachweise;
- Evidence Bundle, wenn für die Delegation vorgesehen;
- offene Risiken;
- verbleibende manuelle Prüfungen;
- Abweichungen vom Plan;
- explizite Unsicherheiten.

## Keine implizite Freigabe

Schweigen, ein grüner Test oder das erfolgreiche Ende eines Agentenlaufs sind keine automatische Zustimmung für den nächsten risikoreichen Schritt.

Wenn der Prozess eine Freigabe verlangt, muss sie erkennbar erteilt werden.

## Agent stoppt bei neuer Entscheidung

Ein Agent soll nicht eigenmächtig weiterarbeiten, wenn während eines freigegebenen Schritts eine neue Entscheidung nötig wird.

Beispiele:

- bestehende Architektur reicht nicht aus;
- Requirement ist widersprüchlich;
- notwendige Migration war nicht geplant;
- Fix erfordert eine öffentliche API-Änderung;
- Scope muss deutlich erweitert werden;
- eine neue zentrale Abstraktion oder externe Abhängigkeit würde eingeführt.

Dann gilt:

```text
Fund
→ Auswirkungen beschreiben
→ Optionen nennen
→ Gate / neue Planung
```

## Innerer Loop und äußerer Loop

Der innere Agentenloop optimiert innerhalb eines freigegebenen Bereichs.

Der äußere Loop entscheidet, **ob** dieser Bereich verändert oder verlassen werden darf.

```text
Mensch / äußere Steuerung
        ↓
 freigegebener Scope
        ↓
   Agentenloop
        ↓
      Evidence
        ↓
 Review / Human Gate
```

## Automatisierte Freigaben

Nicht jedes Gate muss zwingend manuell sein.

Ein Gate kann automatisiert werden, wenn:

- Kriterien vollständig und zuverlässig maschinenprüfbar sind;
- Risiken verstanden sind;
- Fehlentscheidungen begrenzt und reversibel sind;
- die Automatisierung ausdrücklich Teil des Prozesses ist.

Eine stillschweigende Automatisierung ist keine definierte Freigabe.

## Qualitätscheck

Vor einem autonomen Workflow prüfen:

1. Welche Entscheidungen gehören in den Why Loop und welche darf der How Loop selbst treffen?
2. Welche Schritte darf der Agent selbstständig ausführen?
3. Welche Aktionen sind irreversibel oder extern sichtbar?
4. Wo darf Scope eigenständig erweitert werden – falls überhaupt?
5. Welche Nachweise müssen vor einem Gate vorliegen?
6. Wer oder was erteilt die Freigabe?
7. Was passiert, wenn eine neue Entscheidung während des Loops auftaucht?
8. Muss ein Mensch jede Aktion kontrollieren oder reicht eine gute Kontrolle des äußeren Loops?

## Leitgedanke

> Der Agent darf im inneren Loop schnell sein. Der äußere Loop entscheidet, wohin gefahren wird.