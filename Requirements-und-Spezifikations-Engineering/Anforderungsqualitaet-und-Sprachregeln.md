# Anforderungsqualität und Sprachregeln

## Zweck

Eine Anforderung soll so formuliert sein, dass relevante Stakeholder dieselbe beabsichtigte Aussage verstehen und später belastbar beurteilt werden kann, ob sie erfüllt ist.

## Qualitätsachsen

Je nach Scope prüfen:

- notwendig und auf Quelle/Ziel zurückführbar;
- eindeutig im relevanten Kontext;
- atomar genug für unabhängige Bewertung, ohne künstliche Fragmentierung;
- vollständig genug für die beabsichtigte Entscheidung;
- konsistent mit anderen gültigen Requirements und Begriffen;
- realistisch beziehungsweise als Feasibility-Risiko sichtbar;
- verifizierbar oder mit klarer Verifikationsabsicht;
- traceable;
- frei von unbegründeter Lösungsfestlegung;
- mit sichtbaren Annahmen, Conditions und Scope-Grenzen.

## Sprache

Vage Begriffe nur verwenden, wenn ihre Bedeutung lokal geklärt ist. Typische Risikosignale:

- schnell, performant, intuitiv, sicher, robust, flexibel;
- angemessen, ausreichend, möglichst, normalerweise;
- relevante, geeignete oder übliche Werte ohne Definition;
- `und/oder`, wenn die Logik unklar bleibt;
- versteckte Ausnahmen wie `falls nötig` oder `bei Bedarf`.

Nicht jedes Signal ist automatisch ein Fehler. Entscheidend ist, ob mehrere vernünftige Interpretationen zu unterschiedlicher Umsetzung oder Abnahme führen können.

## Aktiv und beobachtbar formulieren

Bevorzugt beschreiben:

- wer oder was betroffen ist;
- unter welcher Bedingung;
- welches beobachtbare Verhalten oder Ergebnis erforderlich ist;
- welche Grenze oder Toleranz gilt, wenn sie entscheidungsrelevant bestätigt ist.

## Keine erfundene Präzision

`< 200 ms`, `99.99 %`, `10.000 Nutzer` oder `7 Jahre Retention` sind nur dann Requirements, wenn sie aus einer autoritativen Quelle, bestätigten Entscheidung oder belastbaren Ableitung stammen.

Fehlt ein notwendiger Zielwert:

```text
Requirement Candidate
→ Zielwert fehlt
→ OPEN / UNVERIFIED
→ Quelle / Entscheidung benennen
```

Nicht einen plausiblen Industriestandard einsetzen und danach so tun, als habe der Stakeholder ihn verlangt.

## Lösungsneutralität mit Augenmaß

Requirements sollten das `was/warum` schützen, wenn die Lösung noch offen ist. Ein technischer Constraint ist jedoch legitim, wenn er selbst eine autorisierte Anforderung darstellt.

Unbegründete Präferenz:

> Das System muss Kafka verwenden.

Reale Grenze:

> Die Lösung muss mit dem verbindlich vorgegebenen zentralen Messaging-Service X integrierbar sein.

## Leitgedanke

> Präzise klingt nicht automatisch präzise – jede Zahl und jede Muss-Aussage braucht eine Herkunft.