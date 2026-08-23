# Agent-Anweisungen für Softwarearbeit

## Zweck

Diese Datei beschreibt die allgemeine Arbeitsdisziplin eines KI-Agenten in einem Softwareprojekt.

Sie ist absichtlich projektneutral. Fachliche und technische Wahrheit kommt aus dem jeweiligen Repository.

## Vor relevanter Entwicklungsarbeit

1. Den konkreten Auftrag und die zugehörige Anforderung identifizieren.
2. Relevante Projekt-, Architektur-, Entscheidungs- und Testdokumentation lesen.
3. Bestehenden Code und vorhandene Tests prüfen, bevor eine Lösung geplant wird.
4. Den Entwicklungsprozess aus `Entwicklungsprozess.md` beachten.
5. Passende Skills nur innerhalb ihres vorgesehenen Kontexts einsetzen.

## Vorrang

Bei Widersprüchen gilt:

```text
konkreter Nutzerauftrag
→ verbindliche Anforderung / Spezifikation
→ gültige Projektentscheidungen
→ freigegebener Plan
→ lokale Repository-Regeln
→ allgemeine Skills und Regeln
```

Ein allgemeiner Skill eröffnet keine zweite Spezifikation.

## Planen vor größeren Änderungen

Bei größeren Verhaltens-, Daten- oder Architekturänderungen nicht direkt mit Code beginnen.

Der Plan soll mindestens klären:

- betroffene Komponenten;
- geplante Lösung;
- Risiken;
- Tests und Nachweise;
- Scope-Grenzen;
- notwendige manuelle Prüfungen.

Wenn eine notwendige Entscheidung offen ist, diese sichtbar machen statt sie stillschweigend in Code zu treffen.

## Umsetzung

Während der Implementierung:

- kleine überprüfbare Schnitte bevorzugen;
- bestehende Architektur respektieren;
- keine unnötigen Abhängigkeiten einführen;
- keine fremden Bereiche nebenbei refactoren;
- Tests und Validierung nicht abschwächen;
- keine persistierten oder öffentlichen Verträge beiläufig verändern;
- Änderungen auf den freigegebenen Scope begrenzen.

## Fehlerdiagnose

Bei Bugs, Regressionen, sporadischem Verhalten oder Performanceproblemen zuerst einen belastbaren Repro oder Messnachweis schaffen.

Keinen Fix nur aus Code-Lektüre erraten, wenn das Problem reproduzierbar geprüft werden kann.

## Review

Nach der Umsetzung nicht nur Testzahlen oder Abschlussbericht bewerten.

Prüfen:

- tatsächlichen Diff;
- Anforderung und Akzeptanzkriterien;
- Scope Creep;
- Daten- und Sicherheitsrisiken;
- neue Abhängigkeiten und Schnittstellen;
- Qualität der Tests;
- notwendige manuelle Prüfungen.

## Abschlussbericht

Ein guter Abschluss nennt mindestens:

- umgesetzte Anforderung beziehungsweise Auftrag;
- geänderte Bereiche;
- relevante technische Entscheidung;
- ausgeführte Tests und Prüfungen;
- Nachweis pro Akzeptanzkriterium, soweit vorhanden;
- verbleibende manuelle Prüfungen;
- offene Risiken oder Unsicherheiten.

Keine Freigabe behaupten, solange notwendige Prüfungen noch offen sind.

## Skills

Die Skills unter `Skills/` sind Arbeitsweisen, keine Projektwahrheit:

- `domain-modeling` – Begriffe, Fachobjekte und Grenzen schärfen;
- `tdd` – Umsetzung in kleinen Red/Green-Schnitten;
- `diagnose` – reproduzierbare Root-Cause-Diagnose;
- `code-review` – Diff gegen Anforderung und Standards prüfen.