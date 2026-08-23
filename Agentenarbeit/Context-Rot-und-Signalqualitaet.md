# Context Rot und Signalqualität

## Zweck

Großer Kontext ist nicht automatisch guter Kontext. Mit wachsender Menge können relevante Informationen schwerer nutzbar werden, besonders wenn ältere, doppelte, widersprüchliche oder irrelevante Inhalte dieselbe Aufmerksamkeit beanspruchen.

> Kontextqualität beschreibt nicht nur, ob Information vorhanden ist, sondern ob der Agent sie im richtigen Moment zuverlässig nutzen kann.

## Typische Ursachen von Context Rot

- veraltete Zwischenstände;
- widersprüchliche Zusammenfassungen;
- duplizierte Anforderungen oder Regeln;
- lange historische Tooloutputs ohne aktuellen Nutzen;
- zu viele gleichzeitig sichtbare Tools oder Skills;
- irrelevante Hintergrunddokumente;
- vermischte Hypothesen und bestätigte Fakten;
- unklare Source-of-Truth-Hierarchie;
- wiederholte Fehlversuche ohne Verdichtung;
- große Retrieval-Pakete ohne Priorisierung.

Context Rot besitzt keine universelle Token-Schwelle. Er ist ein Qualitätsrisiko, das sich abhängig von Modell, Aufgabe und Kontextstruktur unterschiedlich zeigt.

## Signalqualität erhöhen

Bevor zusätzlicher Kontext geladen wird, prüfen:

1. Welche Entscheidung oder Aktion steht jetzt an?
2. Welche Information ist dafür wirklich erforderlich?
3. Welche Quelle ist kanonisch und aktuell?
4. Kann Detailinformation just-in-time nachgeladen werden?
5. Gibt es alte oder widersprüchliche Versionen, die entfernt oder klar markiert werden sollten?
6. Reicht ein Verweis auf ein Artefakt statt dessen vollständigem Inhalt?

## Progressive Disclosure

Bevorzugt:

```text
leichte Orientierung
→ relevante Referenzen / IDs / Pfade
→ gezieltes Nachladen
→ tiefe Details nur bei Bedarf
```

Nicht vorsorglich alle potenziell relevanten Informationen in den aktiven Kontext kippen.

## Konflikte und Staleness

Wenn zwei Kontextteile widersprechen:

- Vorrangregeln anwenden;
- aktuelle kanonische Quelle bevorzugen;
- veralteten Stand nicht stillschweigend weiterführen;
- ungelösten Widerspruch sichtbar machen.

Zusammenfassungen und Handoffs sind abgeleitete Arbeitsartefakte. Sie dürfen eine aktuelle Source of Truth nicht überschreiben.

## Diagnosehinweise

Mögliche Signale für Context-Probleme:

- der Agent wiederholt bereits erledigte Arbeit;
- ignoriert kürzlich bestätigte Constraints;
- verwechselt alte und neue Zustände;
- ruft unnötig dieselben Quellen oder Tools erneut auf;
- beantwortet eine lokale Frage mit irrelevanter Historie;
- braucht deutlich mehr Schritte ohne zusätzlichen Erkenntnisgewinn.

Diese Signale sind Hinweise, keine automatische Kausalitätsdiagnose. Andere Ursachen wie Modellwahl, unklare Anforderungen oder schlechte Tools müssen mitgeprüft werden.

## Leitgedanke

> Nicht Information anhäufen, sondern das für den nächsten Schritt relevante Signal schützen.