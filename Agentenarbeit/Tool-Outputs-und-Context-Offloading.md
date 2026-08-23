# Tool Outputs und Context Offloading

## Zweck

Toolaufrufe können mehr Kontext erzeugen als die eigentliche Aufgabe benötigt. Rohoutputs sollen deshalb nicht automatisch vollständig in den Modellkontext zurückfließen.

> Das Modell soll die relevanten Ergebnisse sehen – nicht zwangsläufig jeden Zwischenschritt, den ein Tool erzeugt hat.

## Typische Bloat-Quellen

- sehr lange Suchresultate;
- Datenbankabfragen mit vielen Zeilen;
- komplette Logdateien;
- große JSON-/API-Antworten;
- Build- oder Testausgaben mit Wiederholungen;
- Toolschemas zahlreicher aktuell irrelevanter Integrationen;
- wiederholte Rohoutputs desselben Artefakts.

## Deterministische Verarbeitung bevorzugen

Wenn Filtern, Sortieren, Aggregieren, Parsen oder einfache Berechnung deterministisch außerhalb des LLM erfolgen kann, bevorzugt dort ausführen.

Beispiel:

```text
50.000 Datensätze
→ Tool / Code filtert und aggregiert
→ relevante Treffer + Kennzahlen
→ Modell bewertet
```

Nicht automatisch:

```text
50.000 Datensätze
→ vollständig in den Kontext
→ Modell soll selbst filtern
```

## Evidence erhalten

Offloading darf Nachvollziehbarkeit nicht zerstören.

Wo relevant, erhalten:

- Quelle oder Tool;
- Filter-/Aggregationsregel;
- relevante Parameter;
- Anzahl Eingangsdaten und Ergebnisdaten;
- Referenz auf Rohartefakt, falls verfügbar und zulässig;
- Unsicherheiten oder ausgelassene Bereiche.

## Progressive Tool Discovery

Wenn die Runtime viele Tools, Plugins oder Skills besitzt, nicht alle Beschreibungen vorsorglich in jeden Lauf laden.

Bevorzugt:

```text
kleiner relevanter Toolraum
→ Bedarf erkennen
→ weitere Capability entdecken / laden
```

Sofern die Runtime progressive oder deferred discovery unterstützt, kann dies Kontext und Toolauswahl verbessern.

## Sicherheitsgrenze

Context Offloading ist keine Umgehung von Datenschutz-, Berechtigungs- oder Sicherheitsregeln.

- Secrets nicht in Zwischenartefakte schreiben, nur um Kontext zu sparen;
- ausgelagerte Daten benötigen passende Zugriffskontrolle;
- externe Inhalte bleiben untrusted Input;
- ein Tool darf nicht mehr Daten lesen als für seinen Auftrag nötig.

## Leitgedanke

> Reduziere Modellkontext durch bessere Datenwege, nicht durch Verlust von Evidence.