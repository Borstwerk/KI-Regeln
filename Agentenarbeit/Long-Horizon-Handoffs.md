# Long-Horizon Handoffs

## Zweck

Ein Handoff übergibt einen Arbeitszustand an einen neuen Agenten, eine neue Session oder einen späteren Arbeitslauf, ohne vorauszusetzen, dass der ursprüngliche Verlauf verfügbar oder vollständig gelesen wird.

> Ein gutes Handoff ist ein eigenständig nutzbarer Fortsetzungszustand, kein Chatprotokoll.

## Compaction und Handoff unterscheiden

```text
Compaction
→ derselbe Arbeitsstrom benötigt weniger aktiven Kontext

Handoff
→ eine andere oder frische Arbeitsinstanz benötigt ausreichenden Fortsetzungszustand
```

Beide können dieselben Verdichtungsprinzipien nutzen, erfüllen aber unterschiedliche Verträge.

## Minimaler Handoff-Vertrag

Je nach Aufgabe enthalten:

- Auftrag und Ziel;
- aktueller Scope;
- relevante Vorrangregeln;
- kanonische Sources of Truth;
- bestätigte Entscheidungen;
- aktueller Arbeits-/Artefaktzustand;
- geänderte oder erzeugte Artefakte;
- ausgeführte Evidence und deren Ergebnis;
- offene Fehler, Risiken und Blocker;
- bekannte relevante Sackgassen;
- Gate-/Freigabestatus;
- nächster sinnvoller prüfbarer Schritt.

## Referenz vor Kopie

Große Artefakte nicht vollständig in ein Handoff duplizieren, wenn sie zuverlässig adressierbar sind.

Bevorzugt:

```text
Artefakt / Datei / Commit / Dokument
→ stabile Referenz
→ kurze Erklärung, warum sie relevant ist
```

Handoffs dürfen aber nicht so knapp werden, dass ein neuer Agent die Bedeutung der Referenzen erraten muss.

## Standalone-Test

Ein Handoff ist gut, wenn eine frische Arbeitsinstanz ohne den alten Chat:

1. Ziel und Scope korrekt versteht;
2. wichtige Constraints nicht verliert;
3. den aktuellen Zustand lokalisieren kann;
4. offene Risiken erkennt;
5. den nächsten Arbeitsschritt plausibel und regelkonform bestimmen kann.

Wenn dafür zwingend der alte Verlauf benötigt wird, ist das Handoff unvollständig.

## Keine stillen Statusänderungen

Ein Handoff darf nicht:

- unbestätigte Hypothesen zu Fakten machen;
- ungeprüfte Arbeit als bestanden markieren;
- Freigaben erfinden;
- offene Blocker aus Platzgründen entfernen;
- neue Architektur- oder Produktentscheidungen einführen.

## Längere Arbeitsketten

Bei vielen Übergaben Drift vermeiden:

- kanonische Quellen referenzieren;
- Handoff nicht als neue dauerhafte Wahrheitsschicht missbrauchen;
- bestätigte Zustände regelmäßig gegen reale Artefakte prüfen;
- alte Handoffs archivieren oder eindeutig als historisch markieren.

## Leitgedanke

> Übergib den Zustand, den die nächste Instanz zum Weiterarbeiten braucht – nicht die Geschichte darüber, wie er entstanden ist.