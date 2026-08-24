# Analytische Datenmodellierung und Grain

## Zweck

Analytische Modelle strukturieren Daten für Auswertung, Reporting, Exploration oder nachgelagerte Datenprodukte. Ihr Kern ist nicht ein bestimmtes Schema-Pattern, sondern eine eindeutige Bedeutung auf einem definierten Grain.

## Grain zuerst

Vor Spaltenlisten und Joins klären:

> Was repräsentiert genau eine Zeile beziehungsweise ein Datenelement?

Beispiele:

- eine Bestellung;
- eine Bestellposition;
- ein Kontostand pro Konto und Geschäftstag;
- ein Messwert pro Gerät und Event-Zeitpunkt;
- ein aggregierter KPI pro Region und Kalendermonat.

Ohne Grain sind Schlüssel, Measures, Aggregationen und Deduplizierung nicht belastbar definierbar.

## Modellierungsfragen

Mindestens prüfen:

- fachliche Entitäten und Ereignisse;
- Grain und stabile Identität;
- Measures und ihre Aggregierbarkeit;
- Dimensionen / beschreibende Attribute;
- Zeitbezug und Gültigkeit;
- Historisierungsbedarf;
- Unknown-/Not-applicable-/Missing-Semantik;
- Änderungsverhalten von Referenzdaten;
- Consumerabfragen und erwartete Joinpfade;
- Performance-/Storage-Trade-offs als lokale Folge, nicht als fachliche Wahrheit.

## History

Historisierung braucht eine ausdrückliche fachliche Entscheidung:

- Current State genügt;
- Änderungen sollen nachvollziehbar bleiben;
- Gültigkeitsintervalle sind relevant;
- Ereignisse sind bereits append-only;
- Korrekturen sollen frühere Wahrheit ersetzen oder als neue Version sichtbar bleiben.

SCD-Typen sind mögliche Umsetzungsmuster, keine zentrale Pflichtsprache.

## Measures

Bei Kennzahlen klären:

- Einheit;
- Numerator / Denominator;
- erlaubte Aggregationen;
- Filter und Population;
- Zeitbezug;
- Umgang mit Storno/Korrektur;
- Rundung und Währung, falls relevant.

Ein Spaltenname wie `revenue`, `active` oder `count` ist keine ausreichende Definition.

## Star, Snowflake, Wide Table, Data Vault, One Big Table

Diese und andere Muster können lokal sinnvoll sein. Keines ist universell vorgeschrieben.

Die Entscheidung folgt unter anderem:

- Consumer- und Querymuster;
- Änderungsfrequenz;
- Governance-/Ownershipmodell;
- Tooling;
- Performance und Kosten;
- Reuse-/Semantic-Layer-Bedarf.

## Grenze zu Datenbanken

`database-design` modelliert primär operative Persistenz und Zugriffsmuster innerhalb eines Datenspeichers.

`analytical-data-modeling` modelliert veröffentlichte oder abgeleitete analytische Daten mit Grain, Historie, Measures und Consumersemantik.

## Nicht tun

- Star Schema automatisch erzwingen;
- operative Tabellen 1:1 als gutes Analyticsmodell ausgeben;
- Grain aus Primärschlüsseln erraten;
- historisierte Daten ohne Gültigkeitssemantik entwerfen;
- additive Measures ungeprüft über alle Dimensionen summieren;
- semantische Definitionen nur in Dashboardlogik verstecken.