# Publish, Retention und Datenlebenszyklus

## Zweck

Ein Dataset wird durch Veröffentlichung zu einer Consumeroberfläche. Deshalb müssen Publish, Retention, Korrekturen und Löschung als bewusste Lifecycle-Entscheidungen behandelt werden.

## Publish

Vor Publish klären:

- welches Dataset beziehungsweise welche Version sichtbar wird;
- welcher Grain und Contract gelten;
- welche Quality-/Reconciliation-Evidence erforderlich ist;
- ob Publish atomar, partitioniert, appendend oder schrittweise erfolgt;
- ob Consumer einen Zwischenzustand sehen können;
- wie fehlerhafte Publishes zurückgenommen oder korrigiert werden;
- welches lokale Gate eine reale Veröffentlichung autorisiert.

Ein erfolgreicher Materialisierungsschritt ist nicht automatisch Publishfreigabe.

## Immutability und Korrekturen

Append-only, immutable, overwrite oder merge sind keine universellen Qualitätsstufen.

Die Wahl hängt davon ab, ob:

- fachliche Korrekturen erlaubt oder erforderlich sind;
- historische Wahrheit erhalten bleiben soll;
- Consumer Updates verarbeiten können;
- Audit-/Regelanforderungen gelten;
- Storage- und Querykosten relevant sind.

## Retention

Retention braucht lokale Grundlage:

- Consumerbedarf;
- Reprocessing-/Replayfenster;
- Audit-/Regelanforderungen;
- Datenschutz und Löschpflichten;
- Kosten;
- Source-Verfügbarkeit.

„Für immer aufheben“ und „nach 30 Tagen löschen“ sind ohne Kontext gleichermaßen unbegründet.

## Löschung und Right-to-Delete

Wenn Quelldaten gelöscht oder korrigiert werden müssen, ist zu klären, welche abgeleiteten Datasets, Snapshots, Backups, Caches oder Exporte betroffen sind.

Data Engineering koordiniert die technische Datenflusswirkung; rechtliche Anforderungen und Security-/Privacy-Policy bleiben lokale beziehungsweise zuständige Sources of Truth.

## Partitionen und Lifecycle

Partitionierung kann Lifecycle und Reprocessing erleichtern, ist aber keine rein technische Optimierung. Sie beeinflusst:

- Delete-/Overwrite-Radius;
- Backfillgrenzen;
- Late Data;
- Kosten;
- Queryverhalten;
- Retention.

## Nicht tun

- Publish automatisch an Job-Erfolg koppeln;
- Retentionwerte zentral erfinden;
- historische Daten still löschen, nur um Kosten zu sparen;
- immutable als universelle Pflicht erklären;
- Consumerwirkung bei Replace/Overwrite ignorieren;
- Löschungen oder Retentionänderungen ohne lokale Freigabe ausführen.