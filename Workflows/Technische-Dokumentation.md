# Workflow – Technische Dokumentation

## Ziel

Dokumentation erzeugen oder überarbeiten, die lesbar **und** an der tatsächlichen Source of Truth verankert ist.

## Skill-Kette

```text
optional: research-plan / deep-research
→ docs-plan
→ passender Dokumenttyp-Skill
→ technical-writing
→ docs-review
```

Dokumenttyp-Skills beispielsweise:

- `readme`;
- `tutorial`;
- `how-to`;
- `reference-docs`;
- `explanation-docs`;
- `adr`;
- `runbook`.

## Phasen

### 1. Quellenlage klären

Wenn externe Fakten oder unbekannte Standards nötig sind, vorher Recherche durchführen.

Projektinterne Wahrheit nicht durch Webquellen ersetzen.

### 2. Docs Plan

`docs-plan`

Bestimmt:

- Leser;
- Aufgabe;
- Dokumenttyp;
- Diátaxis-Modus;
- Source of Truth;
- Lifecycle / Owner;
- Verifikationsbedarf.

### 3. Artefakt erstellen

Passenden Dokumenttyp-Skill verwenden.

### 4. Schreibqualität

`technical-writing`

Klarheit, Terminologie, Scanbarkeit und Beispiele verbessern, ohne fachliche Aussagen zu erfinden.

### 5. Review

`docs-review`

Priorität:

```text
fachliche Korrektheit
→ Verifikation
→ Vollständigkeit
→ Navigation
→ Stil
```

## Gate

Dokumentation ist nicht fertig, wenn nur die Prosa gut klingt.

Soweit relevant müssen:

- Befehle / Beispiele geprüft;
- Links geprüft;
- Parameter gegen Source of Truth geprüft;
- offene unverified Stellen markiert

sein.

## Wartung

Bei produktrelevanter Änderung prüfen, ob die Dokumentation im selben Change-Kontext aktualisiert werden muss.
