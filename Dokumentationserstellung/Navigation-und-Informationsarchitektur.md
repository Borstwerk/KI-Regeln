# Navigation und Informationsarchitektur

## Zweck

Dokumentation muss nicht nur korrekt sein. Nutzer müssen die richtige Information auch finden und erkennen können.

## Vom Nutzerweg denken

Struktur nicht nur nach interner Team- oder Codeorganisation aufbauen.

Fragen:

- Wo startet ein neuer Nutzer?
- Wo startet ein erfahrener Nutzer mit einer konkreten Aufgabe?
- Wo findet jemand Reference?
- Wo liegen Hintergrund- und Architekturerklärungen?
- Wie kommt man von einer Fehlermeldung zur passenden Lösung?

## Progressive Disclosure

Zeige zuerst die Informationen, die für den aktuellen Schritt nötig sind.

Detailtiefe kann über:

- Unterseiten;
- weiterführende Links;
- Reference-Seiten;
- Explanation-Seiten

ausgelagert werden.

## Stabile Einstiegspunkte

Typische Einstiegspunkte können sein:

- README;
- Quickstart;
- Installation;
- zentrale Docs-Startseite;
- Troubleshooting;
- API Reference.

Sie sollen klar erkennen lassen, wohin der Leser als Nächstes gehört.

## Links mit Zweck

Links sollen dem Leser sagen, was ihn erwartet.

Besser:

- `Konfigurationsoptionen anzeigen`
- `Hintergrund zur Authentifizierungsarchitektur`

statt:

- `hier`
- `mehr`
- `weitere Informationen`.

## Keine Navigationsduplikate ohne Grund

Wenn dieselbe fachliche Information an mehreren Stellen vollständig gepflegt wird, entsteht Drift.

Besser:

```text
kanonische Seite
← klare Links von anderen Dokumenten
```

statt mehrere fast identische Erklärungen parallel zu pflegen.

## Reference spiegelt Systemstruktur

Bei Nachschlagedokumentation kann es sinnvoll sein, die reale Systemstruktur abzubilden:

- Module;
- APIs;
- Commands;
- Konfigurationsbereiche;
- Entitäten;
- Ressourcen.

Das erleichtert Mapping zwischen Dokumentation und System.

## Dokumente klein genug halten

Ein Dokument sollte nicht allein deshalb wachsen, weil alles zum selben Produkt gehört.

Neue Seite erwägen, wenn:

- ein anderer Dokumentationsmodus beginnt;
- eine andere Zielgruppe angesprochen wird;
- ein Abschnitt einen eigenen stabilen Such- oder Linkzweck hat;
- Reference durch lange Explanation unübersichtlich wird;
- ein How-to durch Hintergrundwissen aus dem Arbeitsfluss gerät.

## Suchbegriffe und Terminologie

Verwende Begriffe, nach denen reale Nutzer wahrscheinlich suchen:

- Fehlermeldung;
- UI-Bezeichnung;
- API-Name;
- Fachbegriff;
- konkrete Aufgabe.

Nicht nur interne Projektnamen oder abstrakte Kategorien.

## Leitgedanke

> Gute Dokumentation beantwortet nicht nur Fragen – sie hilft dem Leser, die richtige Frage an der richtigen Stelle wiederzufinden.
