# Provenance, Evidence und Source of Truth

## Grundprinzip

> Eine Wissensaussage ohne nachvollziehbare Herkunft ist schwer prüfbar und schwer sicher zu aktualisieren.

## Provenance

Provenance beschreibt, woher eine Information stammt und wie sie entstanden ist.

Je nach Risiko können relevant sein:

- Quellreferenz;
- Autor oder verantwortliche Institution;
- Abruf-, Lern- oder Beobachtungszeitpunkt;
- Gültigkeitszeitraum;
- Transformations- oder Syntheseschritt;
- beteiligte Wissenseinheiten;
- Confidence oder Verifikationsstatus.

Nicht jede private Notiz braucht ein vollständiges Provenance-Ontologiemodell. Kritische Claims brauchen jedoch genug Herkunft, um sie später zu prüfen.

## Claim-nahe Herkunft

Wenn eine Notiz mehrere externe Behauptungen enthält, reicht ein allgemeiner Quellenblock häufig nicht.

Wichtige oder veränderliche Claims sollten so mit Quellen verbunden sein, dass später erkennbar bleibt, welche Quelle welchen Claim trägt.

## Source of Truth

Eine abgeleitete Wissensnotiz darf eine kanonische Quelle nicht stillschweigend ersetzen.

Beispiele:

```text
reales Repository / Spezifikation
> alte Projektzusammenfassung

Originalquelle
> aus ihr erzeugte KI-Zusammenfassung

aktueller bestätigter Stand
> ältere Synthese
```

## Fakten, Interpretation und Inferenz

Trennen:

- direkt aus Quelle belegte Information;
- eigene oder agentische Interpretation;
- Hypothese / Inferenz;
- offene Frage.

Inference darf nicht durch Wiederholung zu einem scheinbaren Fakt werden.

## Zeit

Bei veränderlichen Fakten mindestens unterscheiden:

- wann etwas in der Welt galt oder beobachtet wurde;
- wann die Wissensbasis davon erfahren hat.

Ein vollständiges bitemporales Modell ist optional, aber historische Zustände dürfen nicht mit aktuellen Zuständen vermischt werden.

## Derived Knowledge

Synthesen und Verdichtungen sollten auf ihre Quellen oder Eingabeeinheiten zurückführbar bleiben.

```text
Raw Source
→ Claim / Knowledge Unit
→ Synthesis
```

Der Rückweg soll nachvollziehbar sein.

## Leitgedanke

> Gute Provenance macht Wissen korrigierbar.