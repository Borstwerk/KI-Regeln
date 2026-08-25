# Elicitation und Konfliktklärung

## Zweck

Elicitation bedeutet, entscheidungsrelevante Bedarfe und Constraints aus geeigneten Quellen systematisch zu gewinnen, zu prüfen und offene Konflikte sichtbar zu machen.

## Technik nach Informationsproblem wählen

Mögliche Techniken:

- Interview oder fokussiertes Gespräch;
- Workshop;
- Beobachtung / Contextual Inquiry;
- Dokument-, Ticket-, Log- oder Systemanalyse;
- Prototyp, Beispiel oder Szenario als Klärungshilfe;
- Survey bei vielen verteilten Stakeholdern;
- bestehende Daten-/Prozessanalyse;
- Event Storming, Story Mapping oder andere strukturierende Workshops, wenn passend.

Keine Technik ist Pflicht. Die Auswahl folgt Frage, Stakeholderzugang, Risiko und vorhandener Evidence.

## Progressive Klärung

Nicht alle denkbaren Fragen auf einmal stellen. Priorisieren:

1. Scope- oder Zielunklarheiten, die viele Folgefragen beeinflussen;
2. verbindliche Constraints und verbotene Zustände;
3. kritische Nutzer-/Business-Flows;
4. Qualitätsziele mit Architektur-/Betriebswirkung;
5. Edge-/Failure Cases mit hohem Risiko;
6. Details, die später reversibel geklärt werden können.

Wenn Quellen bereits ausreichend antworten, nicht aus Ritual erneut fragen.

## Fragen sollen Entscheidungen ermöglichen

Statt:

> Soll es schnell sein?

besser:

> Für welchen Flow ist Reaktionszeit kritisch, in welchem Betriebszustand und welche Grenze beziehungsweise heutige Baseline ist dafür relevant?

Statt technische Lösung vorzugeben:

> Brauchen wir Kafka?

zuerst:

> Welche Producer/Consumer müssen mit welcher Latenz-, Ausfall- und Delivery-Erwartung entkoppelt werden?

## Inferenz

Aus Dokumenten oder Systemverhalten dürfen Requirement Candidates abgeleitet werden. Dann Quelle und Inferenz explizit markieren.

```text
Beobachtung / Source
→ abgeleitete Candidate-Aussage
→ INFERRED
→ Stakeholder-/Owner-Validation
```

Nicht aus dem Ist-System automatisch ableiten, dass jedes historische Verhalten weiterhin gewollt ist.

## Konfliktklärung

Bei Konflikten:

- Konflikttyp bestimmen: Ziel, Scope, Semantik, Priorität, Constraint, Zeitstand oder Verantwortlichkeit;
- gemeinsame Begriffe klären;
- Konsequenzen der Alternativen sichtbar machen;
- lokale Entscheidungskompetenz respektieren;
- ungelöste Konflikte als Blocker oder offene Entscheidung weitergeben.

## Abschluss

Elicitation ist ausreichend, wenn die aktuelle nächste Entscheidung mit transparentem Restwissen getroffen werden kann. Eine künstliche Vollständigkeit von 100 Prozent ist kein realistisches Ziel.

## Leitgedanke

> Frage nicht möglichst viel – frage das, was die nächste relevante Unsicherheit auflöst.