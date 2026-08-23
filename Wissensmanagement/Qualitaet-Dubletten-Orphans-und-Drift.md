# Qualität, Dubletten, Orphans und Drift

## Content Health

Wissensqualität ist ein laufender Zustand.

Prüfachsen:

- einzigartige Identität statt schädlicher Dubletten;
- ausreichende Verständlichkeit;
- gültige Links und Beziehungen;
- korrekte Kernmetadaten;
- vorhandene Provenance;
- sinnvolle Granularität;
- Aktualitätsstatus;
- sichtbare Konflikte;
- Findability;
- Datenschutz und Sichtbarkeit.

## Dubletten

Nicht jede ähnliche Einheit ist eine Dublette.

Vor Merge prüfen:

- gleicher Wissensgegenstand?
- gleicher Scope?
- gleicher Zeitraum?
- unterschiedliche Zielgruppe oder Perspektive relevant?
- besitzt eine Einheit zusätzliche Provenance oder Historie?

Beim Merge Provenance, Aliase, eingehende Links und relevante Historie erhalten.

## Orphans

Eine verwaiste Wissenseinheit kann bedeuten:

- fehlende Verlinkung;
- falsche Granularität;
- veralteten Inhalt;
- echten eigenständigen Spezialfall.

Nicht automatisch löschen.

## Broken Links

Kaputte Referenzen sind mehr als kosmetische Fehler, wenn sie Provenance oder Navigation zerstören.

## Schema- und Taxonomie-Drift

Warnsignale:

- dasselbe Feld mit vielen Namen;
- Statuswerte wachsen unkontrolliert;
- Tags werden synonym oder widersprüchlich;
- neue Notiztypen entstehen ohne Modellentscheidung.

## Safe Repair

```text
Health Audit
→ Funde klassifizieren
→ kleine Repair-Slices
→ prüfen
→ erst dann größere Bereinigung
```

Bulk-Merges, massenhafte Rewrites oder Deletes brauchen expliziten Scope und gegebenenfalls Human Gate.

## Leitgedanke

> Pflege verbessert das Wissenssignal. Sie ist keine automatische Großsanierung.