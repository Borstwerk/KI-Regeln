# Coverage, Mutation und Testwirksamkeit

## Grundsatz

> Coverage zeigt, was ausgeführt wurde. Sie beweist nicht, dass relevantes Fehlverhalten erkannt wird.

## Coverage sinnvoll verwenden

Coverage kann helfen:

- unberührte kritische Bereiche sichtbar zu machen;
- Regressionen in der Testabdeckung zu erkennen;
- gezielte Reviewfragen auszulösen.

Sie ist kein universeller Qualitätswert.

Keine zentrale Regel wie:

- „80 % ist gut“;
- „100 % ist notwendig“;
- „Coverage gestiegen = Qualität gestiegen“.

## Unterschiedliche Coverage-Signale

Je nach Sprache/Tool:

- Statement / Line;
- Branch;
- Condition;
- Function / Method;
- Requirement / Risk Coverage.

Für fachliche Qualität kann Risk-/Requirement-Coverage wichtiger sein als reine Codezeilenabdeckung.

## Mutation Testing

Mutation Testing verändert Produktionslogik kontrolliert und prüft, ob Tests die Änderung erkennen.

Es beantwortet eher:

> Würde dieser Test bei plausiblem Fehlverhalten tatsächlich rot?

als:

> Wurde diese Zeile ausgeführt?

## Selektiv einsetzen

Mutation Testing kann teuer sein.

Besonders sinnvoll für:

- kritische Fachlogik;
- Validierungs- und Berechtigungsregeln;
- Berechnungen;
- Invarianten;
- Bereiche mit hoher Coverage, aber zweifelhafter Testaussage.

Nicht jeder triviale Codepfad braucht einen hohen Mutation Score.

## Brechprobe als kleine Form

Eine gezielte manuelle Brechprobe kann denselben Grundgedanken im Kleinen anwenden:

1. Schutzbedingung kontrolliert verletzen.
2. Erwarteten Test rot sehen.
3. Mutation vollständig zurücknehmen.
4. aktuellen Endstand erneut grün prüfen.

## Weitere Wirksamkeitssignale

- bekannte Defekte werden von passenden Tests erkannt;
- Tests bleiben bei Refactoring stabil;
- Fehlermeldungen sind diagnostizierbar;
- Laufzeit ist angemessen;
- Flake-Rate ist niedrig;
- kritische Risiken haben explizite Evidence;
- Tests erkennen tatsächliche Vertragsverletzungen.

## Leitgedanke

> Gute Tests maximieren nicht Metriken. Sie erhöhen die Wahrscheinlichkeit, relevante Fehler früh und zuverlässig zu erkennen.