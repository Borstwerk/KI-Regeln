# Capture, Ingest und Triage

## Grundregel

> Vor dem Erzeugen neuen Wissens zuerst prüfen, was bereits existiert.

Blindes Append-only-Wachstum erzeugt Dubletten, widersprüchliche Wahrheiten und Retrieval-Rauschen.

## Capture

Beim Aufnehmen einer Quelle oder Erfahrung mindestens klären:

- Was ist die Quelle?
- Wann wurde sie erzeugt oder beobachtet?
- Warum ist sie relevant?
- Welche Teile sind Rohinformation, welche bereits Interpretation?
- Enthält sie sensible oder nur taskbezogene Informationen?

## Search before Create

Vor einer neuen Wissenseinheit nach vorhandenen Einheiten suchen über:

- Titel und Aliase;
- Schlüsselbegriffe;
- Metadaten;
- verknüpfte Entitäten;
- semantische Suche, wenn verfügbar.

Nicht aus Erinnerung oder fehlendem ersten Treffer auf Abwesenheit schließen.

## Triage

Ein Ingest darf mehrere Ergebnisse haben:

```text
verwerfen
→ nicht dauerhaft relevant oder nicht vertrauenswürdig genug

nur Raw Source speichern
→ Quelle soll erhalten, aber noch nicht als Wissen verdichtet werden

bestehende Einheit aktualisieren
→ neues Material ergänzt oder korrigiert vorhandenes Wissen

neue Einheit anlegen
→ wirklich neuer Wissensgegenstand

Konflikt / Quarantäne
→ widersprüchliche oder ungeklärte Information sichtbar halten
```

## Aktualisieren statt Duplizieren

Wenn neues Material denselben Wissensgegenstand betrifft:

1. bestehende Einheit öffnen;
2. neue Claims gegen vorhandene prüfen;
3. ergänzen, korrigieren oder zeitlich einordnen;
4. Provenance erhalten;
5. widersprochene Altstände nicht stillschweigend löschen, wenn ihre Historie relevant ist.

## Capture im Arbeitsfluss

Wissen möglichst dort erfassen, wo es entsteht oder verwendet wird. Späte Rekonstruktion verliert oft Kontext und Herkunft.

Das bedeutet nicht, jede Chatnachricht dauerhaft zu speichern. Capture und Triage bleiben getrennte Schritte.

## Bulk-Ingest

Bei großen Mengen zuerst Stichprobe und Regeln prüfen:

```text
kleines Sample
→ Struktur / Provenance / Dublettenverhalten prüfen
→ erst danach größere Menge
```

Massenschreibvorgänge, automatische Rewrites oder Löschungen benötigen passende lokale Gates.

## Leitgedanke

> Ingest ist ein Merge-Problem, kein Kopierproblem.