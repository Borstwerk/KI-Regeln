# Dokumenttypen und Diátaxis

## Zweck

Dokumentation wird klarer, wenn zwei Fragen getrennt beantwortet werden:

1. **Welches Leserbedürfnis wird bedient?**
2. **Welcher Artefakttyp wird gepflegt?**

## Die vier Diátaxis-Modi

### Tutorial

Ziel: Lernen durch angeleitetes Tun.

Typisch:

- Anfänger oder neue Aufgabe;
- klare Lernstrecke;
- jeder Schritt erzeugt ein sichtbares Ergebnis;
- Erklärungen nur so weit wie für den Lernfluss nötig.

Nicht mit umfangreicher Reference oder Theorie überladen.

### How-to

Ziel: eine konkrete reale Aufgabe erledigen.

Typisch:

- Leser kennt das System grundsätzlich;
- Voraussetzungen sind knapp genannt;
- nummerierte Schritte;
- Varianten nur, wenn sie für die Aufgabe relevant sind;
- erwartetes Ergebnis am Ende.

Nicht als Lehrkapitel missbrauchen.

### Reference

Ziel: Fakten zuverlässig nachschlagen.

Typisch:

- wiederholbare Struktur;
- neutral und präzise;
- Parameter, Typen, Defaults, Zustände, Kommandos oder Schemas;
- leicht scanbar;
- möglichst nah an der Struktur des beschriebenen Systems.

Nicht mit langen Meinungs- oder Hintergrundabschnitten unterbrechen.

### Explanation

Ziel: Zusammenhänge und Gründe verstehen.

Typisch:

- Kontext;
- Designgedanken;
- Alternativen;
- Trade-offs;
- historische oder architektonische Einordnung.

Nicht in eine Schritt-für-Schritt-Anleitung kippen.

## Artefakttypen

Reale Dokumente sind beispielsweise:

- README;
- ADR;
- Runbook;
- API-Dokumentation;
- Installationsanleitung;
- Onboarding Guide;
- Changelog;
- Troubleshooting Guide;
- Knowledge-Base-Artikel.

Diese Artefakttypen sind nicht identisch mit Diátaxis-Modi.

## Beispiel README

Ein README kann klar getrennte Bereiche enthalten:

```text
Overview
→ Explanation

Quick Start
→ Tutorial / How-to

Installation
→ How-to

Configuration
→ Reference

Architecture
→ Explanation + Links zu ADRs
```

Die Modi dürfen im selben Artefakt vorkommen, sollen aber innerhalb einzelner Abschnitte nicht chaotisch vermischt werden.

## Beispiel Runbook

Ein Runbook ist primär handlungsorientiert und ähnelt How-to-Dokumentation, benötigt aber zusätzliche operative Elemente:

- Symptome;
- Impact;
- Voraussetzungen und Rechte;
- Diagnose;
- Mitigation;
- Verifikation;
- Eskalation;
- Rollback oder Rückweg, wenn relevant.

## Beispiel ADR

Ein ADR ist primär Explanation und Entscheidungsnachweis:

- Kontext;
- Entscheidung;
- betrachtete Alternativen;
- Konsequenzen;
- Status;
- spätere Ablösung durch neue ADR statt stiller Umschreibung.

## Dokumenttyp zuerst klassifizieren

Vor Schreib- oder Reviewregeln zunächst klären:

```text
Leserbedürfnis
→ Diátaxis-Modus

Dokumentationszweck / Lifecycle
→ Artefakttyp
```

Erst danach passende Struktur- und Qualitätsregeln laden.

## Leitgedanke

> Nicht jede gute Dokumentationsregel gilt für jeden Dokumenttyp.
