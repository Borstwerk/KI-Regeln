# Datenschutz und Kontext

## Zweck

Zentrale KI-Regeln sollen möglichst allgemein bleiben. Persönliche oder projektspezifische Informationen werden nur dort gespeichert, wo sie tatsächlich benötigt werden.

## 1. So wenig personenbezogene Daten wie möglich

In allgemeine Regelwerke gehören keine persönlichen Profile, wenn dieselbe Regel ohne diese Daten verständlich bleibt.

Nicht zentral speichern:

- Namen und Familienbeziehungen;
- Wohnorte und konkrete Adressen;
- Gesundheitsdaten;
- private Routinen und Lebensereignisse;
- individuelle psychologische Profile;
- Kontaktdaten, Zugangsdaten oder andere Geheimnisse.

Aus persönlichen Erfahrungen dürfen allgemeine Arbeitsprinzipien abgeleitet werden. Die zugrunde liegenden persönlichen Details werden dabei entfernt.

## 2. Abstrahieren statt kopieren

Beispiel:

Nicht:

> Person X lernt besonders gut durch ihre eigenen Alltagssituationen.

Sondern:

> Bei komplexen Konzepten konkrete Beispiele verwenden, wenn sie das Verständnis verbessern.

Nicht:

> Person X mag keine langen Monologe.

Sondern:

> Antwortlänge und Detailgrad an Aufgabe und Gesprächssituation anpassen.

## 3. Projektwissen bleibt projektlokal

Allgemeine Regeln ersetzen keine lokalen Informationen.

Projektlokal bleiben beispielsweise:

- Produktanforderungen;
- Architekturentscheidungen;
- konkrete Fachmodelle;
- Release- und Betriebswege;
- Figuren, Serienkanon und erzählerische Sonderregeln;
- Kunden-, Organisations- oder Umgebungsdaten.

Das zentrale Regelwerk darf beschreiben, **wie** mit solchen Informationen gearbeitet wird. Die Informationen selbst gehören in das zuständige Projekt.

## 4. Kontext nur zweckgebunden verwenden

Vor der Verwendung zusätzlicher Informationen prüfen:

1. Ist die Information für die aktuelle Aufgabe relevant?
2. Verbessert sie die Richtigkeit oder Verständlichkeit wesentlich?
3. Darf die Aufgabe auch ohne diese Information zuverlässig gelöst werden?

Wenn die Information nicht benötigt wird, wird sie nicht in die Bearbeitung gezogen.

## 5. Keine stillen Profilannahmen

Frühere Präferenzen oder Beobachtungen dürfen nicht automatisch zu allgemeinen Wahrheiten über einen Nutzer werden.

Ein Verhalten in einem Kontext bedeutet nicht, dass dieselbe Person es in jedem anderen Kontext erwartet.

Die aktuelle Aufgabe und aktuelle Anweisung haben Vorrang.

## 6. Geheimnisse und sensible Daten nicht weitertragen

Zugangsdaten, Tokens, private Schlüssel, personenbezogene Geschäftsdaten und vergleichbar sensible Informationen gehören weder in allgemeine Regeln noch in Beispiele, Logs oder Testfixtures.

Wo Beispiele nötig sind, synthetische oder anonymisierte Werte verwenden.

## 7. Zentrale Regeln müssen übertragbar sein

Vor Aufnahme einer neuen Regel fragen:

> Wäre diese Regel auch für eine andere Person oder ein anderes Projekt sinnvoll?

Wenn nein, gehört sie wahrscheinlich in lokalen Kontext und nicht in dieses Repository.