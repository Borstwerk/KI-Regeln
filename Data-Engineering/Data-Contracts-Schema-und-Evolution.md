# Data Contracts, Schema und Evolution

## Zweck

Ein Data Contract beschreibt, was Consumer von einem veröffentlichten Dataset erwarten dürfen: Struktur, Bedeutung, Qualität, Serviceeigenschaften, Ownership und relevante Evolutionsregeln.

## Data Contract vs. Interface Contract

`Schnittstellen-und-Vertraege/` behandelt operative APIs, Requests, Messages und Event-Contracts.

Data Engineering behandelt Verträge für veröffentlichte Datasets wie Tabellen, Views, Files, Topics oder andere konsumierbare Datenprodukte.

Die Grenze folgt dem Consumervertrag, nicht dem Dateiformat.

## Mögliche Vertragsbestandteile

Je nach Kontext:

- Dataset-Identität und Version;
- Zweck und Consumer;
- Grain und Schlüssel;
- Felder, Typen und Semantik;
- Null-/Unknown-Semantik;
- Quality Rules;
- Freshness / Availability / Retention;
- Ownership;
- Classification / sensitive fields;
- Change-/Deprecation-Regeln;
- bekannte Limits und Exclusions.

Ein bestimmtes Format wie ODCS ist eine mögliche maschinenlesbare Repräsentation, keine Pflicht.

## Schema ist nicht Semantik

Eine kompatible Spaltenänderung kann semantisch brechen.

Beispiele:

- `status` behält den Typ, aber Werte bedeuten etwas anderes;
- `amount` wechselt von Cent auf Euro;
- ein Timestamp wechselt Zeitzone oder Ereignisbedeutung;
- Filterlogik ändert die Population;
- Grain wird von Bestellung auf Bestellposition geändert.

## Evolution

Änderungen mindestens prüfen auf:

- strukturelle Compatibility;
- semantische Compatibility;
- historische Vergleichbarkeit;
- Consumerwirkung;
- Backfill-/Reprocessing-Bedarf;
- Dual-Run-/Migrationserfordernis;
- Deprecation und Sunset;
- Versionierungsbedarf.

Mögliche Verdicts:

- `COMPATIBLE`;
- `ROLLOUT-SENSITIVE`;
- `BREAKING`;
- `UNVERIFIED`.

Diese Verdicts übernehmen die Denkweise aus Interface-Contracts, ohne Wire- und Dataset-Semantik gleichzusetzen.

## Contract Verification

Maschinenlesbare Contracts können Schema-, Quality- oder Service-Level-Checks ermöglichen. Ein grüner Contractcheck beweist aber nur die tatsächlich implementierten Prüfungen.

Dokumentierte, aber nicht maschinell überprüfte Zusagen müssen als solche erkennbar bleiben.

## Nicht tun

- Data Contract mit bloßem DDL gleichsetzen;
- additive Spalte automatisch als risikofrei bewerten;
- semantische Änderungen nur nach Datentyp beurteilen;
- unbekannte Consumer ignorieren;
- ODCS, dbt Contracts oder ein anderes Toolformat zentral erzwingen;
- Breaking Changes ohne lokale Migration und Freigabe publizieren.