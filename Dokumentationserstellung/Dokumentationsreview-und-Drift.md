# Dokumentationsreview und Drift

## Zweck

Dokumentation soll nicht nur stilistisch geprüft werden, sondern auf fachliche Korrektheit, Nutzbarkeit und Veraltung.

## Review-Reihenfolge

Priorität:

1. fachlich falsch oder gefährlich;
2. falsche Zielgruppe oder falscher Dokumenttyp;
3. fehlende oder widersprüchliche Information;
4. nicht funktionierende Beispiele, Befehle oder Links;
5. schlechte Informationsarchitektur;
6. unklare Sprache oder Terminologie;
7. Format- und Stilpolitur.

Ein Kommafehler darf keinen veralteten Produktionsbefehl überdecken.

## Review gegen Sources of Truth

Nicht nur den Text intern auf Plausibilität prüfen.

Je nach Dokument:

- Code oder Tests;
- Schema;
- Konfiguration;
- UI;
- ADRs;
- Releaseinformationen;
- Betriebsabläufe

als Gegenbasis verwenden.

## Drift-Arten

### Fachliche Drift

Beschriebenes Verhalten stimmt nicht mehr.

### Terminologie-Drift

Produkt, UI oder Fachbegriffe wurden umbenannt.

### Navigations-Drift

Links und Pfade existieren nicht mehr oder führen zu veralteten Seiten.

### Beispiel-Drift

Code, Befehle oder Ausgaben passen nicht mehr.

### Prozess-Drift

Runbooks, Onboarding oder Freigabewege entsprechen nicht mehr der Realität.

### Struktur-Drift

Dokumentation folgt noch einer alten Architektur oder Produktstruktur.

## Audit-Modus und Rewrite trennen

Wenn nur Review beauftragt ist:

- Findings melden;
- Schweregrad nennen;
- Quelle oder Gegenbeleg nennen;
- konkrete Korrektur vorschlagen.

Nicht stillschweigend alles neu schreiben.

Wenn Verbesserung beauftragt ist:

```text
Audit
→ Findings priorisieren
→ gezielte Änderungen
→ betroffene Checks erneut durchführen
```

## Mögliche Schweregrade

- **BLOCKER** – gefährlich, fachlich wesentlich falsch oder nicht ausführbar;
- **HOCH** – stark veraltet, irreführend oder wichtige Lücke;
- **MITTEL** – Verständlichkeit, Struktur oder Wartbarkeit merklich beeinträchtigt;
- **NIEDRIG** – Stil, Konsistenz oder kleine Politur.

## Starke bestehende Dokumentation schützen

Nicht jede Abweichung von einem allgemeinen Template ist ein Fehler.

Eine bestehende Struktur soll nur geändert werden, wenn:

- der Nutzerweg besser wird;
- fachliche Fehler reduziert werden;
- Wartbarkeit steigt;
- lokale Regeln oder Zielgruppe es verlangen.

## Review-Evidence

Bei wichtigen Findings möglichst angeben:

```text
Dokument / Stelle
→ behaupteter Inhalt
→ Source of Truth
→ Abweichung
→ empfohlene Änderung
```

## Leitgedanke

> Dokumentationsreview prüft nicht, ob der Text professionell aussieht, sondern ob Menschen ihm zuverlässig folgen können.
