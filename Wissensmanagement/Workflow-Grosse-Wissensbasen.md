# Workflow für große Wissensbasen

## Ziel

Dieser Workflow verbindet Wissensmanagement und Context Engineering für große persistente Wissensbasen.

Er soll verhindern, dass mit wachsender Wissensbasis automatisch auch der aktive Agentenkontext wächst.

> Die Wissensbasis darf groß werden. Der aktive Kontext soll nur so groß werden, wie es der konkrete Auftrag erfordert.

Der Workflow ist toolneutral. Lokale Markdown-/PDF-Wikis, Obsidian-Vaults, Dokumentablagen, RAG-Systeme oder andere Wissensbasen können ihn unterschiedlich implementieren.

## Verwenden wenn

- eine Wissensbasis aus vielen Dateien oder großen Quellen besteht;
- ein Agent sonst große Teile der Basis vorsorglich laden würde;
- Retrievalergebnisse zu viel irrelevanten Detailinhalt in den Kontext ziehen;
- dieselben Raw Sources wiederholt vollständig gelesen werden;
- Kontextmenge, Latenz oder Signalverlust mit der Größe der Basis steigen;
- aus einer großen Basis ein kleines belastbares Kontextpaket für einen konkreten Auftrag erzeugt werden soll.

## Rollen der vorhandenen Skills

- `knowledge-query` findet und bewertet relevante Wissenseinheiten für die konkrete Frage.
- `context-engineering` bestimmt daraus den kleinsten ausreichenden aktiven Kontext.
- `knowledge-distill` verdichtet dauerhaft nützliches Rohmaterial in wiederverwendbare Wissenseinheiten.
- `knowledge-synthesis` verbindet mehrere vorhandene Wissenseinheiten zu einem höheren Erkenntnisbild.
- `context-audit` untersucht Context Bloat, Duplikate, Altstände und unnötige Rohoutputs.
- `context-compaction` verdichtet gewachsenen Laufzeitkontext, ohne wichtige Entscheidungen und Evidence zu verlieren.
- `knowledge-maintenance` und `knowledge-base-review` halten die persistente Basis auffindbar, aktuell und frei von unnötiger Drift.

## Kernworkflow

```text
Auftrag / Frage
→ Scope, Zeitbezug und benötigte Evidence klären
→ Index / MOC / Metadaten / Summary als Einstieg
→ Retrieval-Kandidaten bestimmen
→ wenige relevante Wissenseinheiten öffnen
→ Provenance, Aktualität und Widersprüche prüfen
→ kleinstes ausreichendes Kontextpaket bilden
→ Details oder Raw Source nur just-in-time nachladen
→ Aufgabe bearbeiten / grounded antworten
→ dauerhaft neues Wissen bei Bedarf distillieren oder mergen
→ bei Context Pressure auditieren oder kompaktieren
```

## 1. Einstiegsschicht statt Vollbestand

Beginne bei großen Basen nicht mit dem vollständigen Datei- oder Quellenbestand.

Bevorzugte Einstiegspunkte sind:

- Maps of Content / Themenindizes;
- stabile Metadaten;
- Titel, Aliase und Pfade;
- kurze Summaries oder Abstracts;
- bekannte Beziehungen und Links;
- zeitliche oder fachliche Filter.

Diese Einstiegsschicht dient der Navigation und Kandidatenauswahl. Sie ist nicht automatisch Source of Truth.

## 2. Tiered Retrieval

Nutze progressive Auswahl:

```text
Index / Metadaten / Summary
→ relevante Wissenseinheiten
→ relevante Detailabschnitte
→ Raw Source / Evidence nur bei Bedarf
```

Nicht jede gefundene Datei wird automatisch Teil des aktiven Kontexts.

Ein Retrievaltreffer ist zunächst nur ein Kandidat. Erst Relevanz, Provenance, Aktualität und konkrete Aufgabenabhängigkeit rechtfertigen das Nachladen.

## 3. Kontextpaket bilden

Nach dem Retrieval übernimmt `context-engineering`.

Das Kontextpaket soll nach Möglichkeit unterscheiden:

```text
MUSS AKTIV
- Auftrag und harte Constraints
- relevante aktuelle Wissenseinheiten
- notwendige Sources of Truth

JUST-IN-TIME
- Detailabschnitte
- größere Tabellen oder Anhänge
- Raw Sources / PDFs
- selten benötigte Hintergrundinformationen

NUR REFERENZ
- bekannte Fundstellen
- ältere oder alternative Fassungen
- reproduzierbare Rohoutputs
- Evidence, die bei Bedarf erneut geöffnet werden kann
```

Referenzierbare Information soll nicht allein deshalb vollständig dupliziert werden, weil sie verfügbar ist.

## 4. Detail und Evidence just-in-time laden

Öffne größere Quellen erst dann vollständig oder abschnittsweise, wenn die aktuelle Aufgabe sie tatsächlich benötigt.

Typische Gründe:

- eine Aussage muss gegen die Primärquelle verifiziert werden;
- eine Summary reicht für die Entscheidung nicht aus;
- ein Widerspruch muss aufgelöst werden;
- exakte Zahlen, Formulierungen, Tabellen oder Seitenbezüge werden benötigt.

Wenn eine Quelle erneut zuverlässig auffindbar ist, darf sie außerhalb des aktiven Kontexts bleiben.

## 5. Persistenz statt wiederholter Rohlektüre

Wenn aus einer Raw Source dauerhaft wiederverwendbares Wissen entsteht, verwende `knowledge-distill`.

Dabei:

1. zuerst vorhandene passende Wissenseinheiten suchen;
2. bestehende Einheiten bevorzugt enrich/mergen;
3. Provenance und Fundstelle erhalten;
4. belegte Aussage, Interpretation und Inferenz trennen;
5. Raw Source nicht unnötig in eine zweite Vollkopie verwandeln.

Ziel ist weniger wiederholte Rohlektüre, nicht mehr Dateien um ihrer selbst willen.

## 6. Context Pressure behandeln

Wenn ein Lauf trotz gezieltem Retrieval wächst:

```text
Context Pressure
→ context-audit
→ unnötige Wiederholungen, Altstände und Raw Outputs identifizieren
→ referenzierbares Material aus dem aktiven Kontext nehmen
→ bei Bedarf context-compaction
→ mit stabilem Working State fortsetzen
```

Compaction pflegt den Laufzeitkontext. Sie ersetzt nicht die Pflege der persistenten Wissensbasis.

## Markdown-/PDF-Adapter ohne zusätzliche Software

Für lokale Wissensbasen aus Markdown und PDF kann der Workflow bereits mit Dateisystem, vorhandener Suche und Markdown-Struktur umgesetzt werden.

### Markdown

Markdown-Dateien eignen sich bevorzugt für:

- Wissenseinheiten;
- MOCs / Themenindizes;
- Synthesen;
- Metadaten und Status;
- Links auf Quellen und andere Einheiten.

### PDF

PDFs können als Raw Sources erhalten bleiben.

Für häufig genutzte oder große PDFs kann eine kleine Markdown-Sidecar-Datei sinnvoll sein, zum Beispiel mit:

- Titel und Quelle;
- Themen / Tags;
- kurzer Inhaltsbeschreibung;
- relevanten Seiten oder Abschnitten;
- daraus abgeleiteten Wissenseinheiten;
- Aktualitäts- oder Statushinweisen.

Die Sidecar-Datei ist Navigations- und Retrievalhilfe, keine vollständige Kopie des PDFs und nicht automatisch Source of Truth.

Beispiel:

```text
Quellen/
├── SQL-Performance-Guide.pdf
└── SQL-Performance-Guide.md

Wissen/
├── SQL-Parallelism.md
├── SQL-IO-Diagnose.md
└── SQL-Memory.md
```

Eine Wissensabfrage kann dadurch zuerst die kleine Markdown-Struktur nutzen und das PDF nur an der tatsächlich benötigten Fundstelle öffnen.

## Stop-Regeln

Retrieval und Nachladen dürfen stoppen, wenn:

- die entscheidungsrelevanten Teilfragen ausreichend getragen sind;
- notwendige Sources of Truth geprüft wurden;
- verbleibende Lücken transparent sind;
- zusätzliche Quellen überwiegend bereits bekannte Evidence wiederholen;
- weiterer Kontext die Antwort voraussichtlich nicht materiell verbessert.

Nicht vorsorglich weiterladen, nur weil noch Kontextfenster verfügbar ist.

## Qualitätscheck

Vor Abschluss prüfen:

- Wurde der Vollbestand unnötig geladen?
- Sind nur auftragsrelevante Wissenseinheiten aktiv?
- Sind Raw Sources überwiegend referenziert und just-in-time erreichbar?
- Sind Provenance, Aktualität und Widersprüche sichtbar?
- Wurde neues dauerhaft nützliches Wissen sinnvoll distilliert oder gemergt?
- Kann der nächste Schritt ohne erneutes Laden des gesamten Bestands fortgesetzt werden?

## Leitgedanke

> Große Wissensbasen skalieren durch progressive Auswahl und gezieltes Nachladen, nicht durch immer größere Prompt-Pakete.