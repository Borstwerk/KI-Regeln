# Skill-Redundanz und Kontextkosten

## Problem

Skills wachsen häufig, weil nach jedem Fehler eine weitere Schutzregel angefügt wird. Das kann zu:

- identischen Regeln in mehreren Skills;
- widersprüchlichen lokalen Präzisierungen;
- mehrfach geschilderten Abläufen ohne eigene Ownership;
- größerer Kontextlast bei echter Composition;
- längerer Review- und Wartungszeit

führen. **Mehr Text ist nicht automatisch mehr Sicherheit.**

## Quellenwahrheit und Ownership

Bevor eine Wiederholung entfernt wird, feststellen:

1. Wo ist die kanonische Regel verankert?
2. Braucht der konkrete Skill diese Regel als Sicherheits-/Handoff-Kurzform lokal?
3. Ist die Passage eine fachlich sinnvolle Ausnahme oder echte Dopplung?
4. Würde eine Streichung Trigger, Near-Misses, Rechte, Gates oder Acceptance verändern?
5. Ist die Regel für frische Agenten ohne globales Volltextladen weiterhin auffindbar?

Eine globale Regel nicht blind zentralisieren, wenn dadurch die lokale Ausführung oder Sicherheitsgrenze unverständlich wird.

## Report-only-Audit

```bash
python tools/skill_redundancy_audit.py --repo .
python tools/skill_redundancy_audit.py --repo . --json
```

Der Audit ist **read-only** und findet nur **lexikalisch identische längere Absatzblöcke** in verschiedenen `SKILL.md`-Dateien nach Normalisierung von Leerraum/Großschreibung. Er gibt Hash, Wortzahl, betroffene Pfade und Zeilen aus. Er verändert nichts.

### Was das Ergebnis NICHT bedeutet

- Keine semantische Widerspruchserkennung.
- Keine Erkennung sämtlicher Paraphrasen oder redundanten Skillzwecke.
- Kein gemessener Token-/Kosten-Ersparniswert.
- Kein automatisches Entfernen von Security-/Human-Gates.
- Eine wiederholte Formulierung ist **Kandidat**, kein Befund einer fachlichen Fehlkonstruktion.

Doppelte, bewusst notwendige Stop-Gates dürfen bleiben.

## Semantischer Review (menschlich oder unabhängiger Agent)

Aus den Kandidaten und Skill-Metadaten gezielt prüfen:

- Überschneiden sich `description` und Near-Miss-Signale so stark, dass Router beide ohne eigenständigen Job laden?
- Wiederholt ein Skill die allgemeine Arbeitsweise ohne fachspezifischen Mehrwert?
- Widersprechen sich zwei Regeln bei gleichem Auftrag/Checkpoint?
- Können ausführliche Referenzen in eine kanonische Dokumentation ausgelagert werden, während lokale Trigger/Gates kurz bleiben?
- Ist die Einsparung real im **tatsächlich geladenen** Skill-Satz? Ein unbenutzter Skill kostet im Runner nicht automatisch Kontexttokens.

### Änderungsregel

```text
Kandidaten finden
→ Ownership / Safety / Handoff prüfen
→ kleinste textuelle Änderung
→ Validator + Trigger-/Near-Miss-Evals
→ Behavioral-Kontrolle, falls Routing oder Ausführung betroffen
```

Keine automatische Maturity-Hochstufung. Vorher/Nachher-Wortzahl nur als Proxy beschreiben; tatsächliche Kosten anhand beobachteter Kontextladung messen.

## Herkunft

[Cockroach Labs, MOLT Sinai (09.10.2026)](https://www.cockroachlabs.com/blog/experiment-running-hospital-code/) beschreibt einen Audit redundanter Rollen-Prompts. Die berichtete Einsparung ist ein projektspezifisches Erfahrungsbeispiel, **kein** universeller Zielwert für KI-Regeln.

## Leitgedanke

> So wenig redundanter Kontext wie möglich, so viel lokale Klarheit und Schutz wie nötig.
