# Context Budget und Token-Effizienz

## Zweck

Kontext ist eine begrenzte Arbeitsressource. Ziel ist nicht, möglichst wenige Tokens zu verbrauchen, sondern mit möglichst wenig unnötigem Kontext zuverlässig das gewünschte Ergebnis zu erreichen.

> Token-Effizienz optimiert Informationswert und Ergebnisqualität pro eingesetzter Kontextressource – nicht bloß die Tokenzahl.

## Context Budget

Ein Agentenkontext kann unter anderem bestehen aus:

- System- und Projektinstruktionen;
- Skill- und Toolbeschreibungen;
- aktuellen Nutzereingaben;
- Gesprächs- und Agentenhistorie;
- geladenen Dateien und Quellen;
- Toolergebnissen;
- Arbeitsnotizen und Handoffs;
- Retrieval-Ergebnissen;
- provider- oder runtimeabhängigen Kontextbestandteilen.

Nicht jeder verfügbare Bestandteil muss bei jedem Schritt aktiv geladen sein.

## Providerneutrale Metriken

Wenn verfügbar, beobachten:

- Input-Tokens;
- Output-Tokens;
- Cache-Read- und Cache-Write-Tokens;
- Anzahl und Größe von Toolergebnissen;
- relevante Kontextanteile nach Quelle oder Kategorie;
- Modell- und Toollatenz;
- Anzahl der Modell- und Toolaufrufe;
- Compaction-/Pruning-Ereignisse;
- Ergebnisqualität beziehungsweise Task Outcome.

Aus diesen Rohwerten können lokale Kennzahlen abgeleitet werden, zum Beispiel:

- Kontextwachstum pro Arbeitsschritt;
- Anteil wiederverwendeten oder gecachten Inputs;
- Anteil großer Tooloutputs;
- Tokenverbrauch pro erfolgreichem Task oder akzeptiertem Artefakt;
- Vorher-/Nachher-Vergleich einer Context-Optimierung.

Solche Kennzahlen sind Beobachtungs- und Vergleichshilfen, keine universellen Qualitätsgrenzen.

## Keine universellen Schwellenwerte

Nicht zentral festschreiben:

- maximale sinnvolle Kontextfenstergröße;
- feste Prozentgrenzen für „gesunden“ Kontext;
- konkrete Modellpreise;
- harte Tokenlimits für Compaction;
- universelle Zeichen-zu-Token-Formeln.

Diese Werte hängen von Modell, Provider, Runtime, Sprache, Tooling und Aufgabe ab.

Wenn exakte Tokendaten fehlen, dürfen Größen oder relative Anteile als Approximation verwendet werden. Die Approximation muss als solche gekennzeichnet bleiben.

## Optimierungsreihenfolge

Bei hohem Kontextverbrauch bevorzugt prüfen:

```text
unnötige oder veraltete Inputs?
→ doppelte Informationen?
→ zu große Tooloutputs?
→ Informationen just-in-time ladbar?
→ deterministisch außerhalb des Modells filterbar?
→ ältere Arbeit kompaktierbar?
→ stabile Präfixe cache-fähig?
→ erst danach Modell-/Budgetwechsel erwägen
```

Nicht Qualität opfern, nur um eine niedrigere Tokenzahl zu melden.

## Evidence

Eine Context-Optimierung gilt nicht allein deshalb als erfolgreich, weil weniger Tokens verbraucht wurden.

Mindestens vergleichen:

```text
Baseline
→ Änderung
→ Token-/Latenzsignal
→ Task Outcome / relevante Qualitätsprüfung
```

Eine Einsparung mit schlechterem Ergebnis ist keine automatische Verbesserung.

## Leitgedanke

> Kontextbudget ist ein Mittel. Erfolgreiche, belastbare Arbeit bleibt das Ziel.