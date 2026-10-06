# Explorative A/B-Notiz – Visual Answer

Datum: 2026-10-06

Status: **explorative Human-Evidence, kein Behavioral Benchmark**

## Fragestellung

Verbessert eine visuell strukturierte HTML-Antwort gegenüber einer inhaltlich parallelen Markdown-Fassung die schnelle menschliche Erfassbarkeit komplexer Informationen?

## Testklassen

### Test 1 – Architektur / Überblick

Inhalt:

- mehrere HypeRadar-Funde;
- unterschiedliche Entscheidungen wie Übernehmen, Testen, Beobachten und Außen-vor;
- kurze Begründungen und Prioritäten.

Beobachtung:

- HTML-Fassung vom Reviewer bevorzugt.

### Test 2 – Mehrkriterien-Entscheidung

Inhalt:

- drei Optionen für visuelle Antworten in KI-Regeln;
- Kriterien wie Methodenfit, Portabilität, Aufwand, Nutzermehrwert und Lock-in;
- Empfehlung plus Trade-offs.

Beobachtung:

- HTML-Fassung vom Reviewer bevorzugt.

### Test 3 – Review / viele Findings

Inhalt:

- 14 synthetische Findings;
- Severity-Stufen;
- Finding, Auswirkung und Fix;
- Merge-/Prioritätsgate.

Beobachtung:

- HTML-Fassung vom Reviewer bevorzugt;
- explizites Feedback: Das Wichtige ließ sich **auf den ersten Blick innerhalb kurzer Zeit** erfassen.

## Vorläufige Interpretation

Der beobachtete Nutzen lag nicht in zusätzlichem fachlichem Inhalt.

Er lag in:

- visueller Hierarchie;
- räumlicher Gruppierung;
- Priorisierung;
- schnellerem Erfassen von Status und Handlungsschwerpunkten.

Das stützt als Arbeitshypothese:

> Bei komplexen strukturierten Antworten kann eine visuelle Darstellung die Time-to-Signal für Menschen reduzieren.

## Grenzen

- ein Reviewer;
- nicht verblindet;
- keine randomisierte Reihenfolge;
- keine gemessene Zeit;
- keine Recall- oder Fehlerquote;
- keine Gegenprobe mit weiteren Personen;
- HTML direkt erzeugt, nicht mit dem originalen Upstream-Renderer;
- keine Token-, Kosten- oder Laufzeitmessung.

## Konsequenz

Die Evidence ist ausreichend, um `visual-answer` als **experimental** mit formalen Evalfällen zu führen.

Sie ist nicht ausreichend für:

- `candidate` oder `stable`;
- Aussagen über universelle Überlegenheit von HTML;
- Token-/Kosten-/Speed-Claims;
- Pflichtnutzung eines bestimmten Renderers.
