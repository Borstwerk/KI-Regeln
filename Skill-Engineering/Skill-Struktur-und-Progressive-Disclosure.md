# Skill-Struktur und Progressive Disclosure

## Grundprinzip

> Der Agent soll zuerst wissen, **dass** ein Skill passt – und erst danach laden, **was** er zur Ausführung wirklich braucht.

## Empfohlene Struktur

```text
skill-name/
├── SKILL.md
├── references/     # optional
├── scripts/        # optional
└── assets/         # optional
```

`SKILL.md` enthält die kompakte operative Disziplin. Große Referenzlisten, lange Beispiele, Spezifikationen oder Hilfsskripte gehören nicht automatisch hinein.

## Drei Ebenen

### 1. Discovery

Für die Auswahl reichen möglichst:

- Name;
- Description;
- ggf. wenige Metadaten.

Die Description muss deshalb klar sagen:

- was der Skill tut;
- wann er eingesetzt werden soll.

### 2. Activation

Nach Aktivierung wird `SKILL.md` gelesen.

Darin gehören insbesondere:

- Ziel und Scope;
- Prozess;
- harte Regeln;
- Stop-/Eskalationsbedingungen;
- Output / Evidence;
- relevante Fallbacks.

### 3. Execution

Zusätzliche Inhalte werden nur bei Bedarf geladen:

- `references/` für tiefere Fach- oder Formatregeln;
- `scripts/` für deterministische Hilfen;
- `assets/` für Vorlagen oder Ressourcen.

## Kontextbudget

Ein Skill ist kein Wissensarchiv.

Wenn eine Detailregel nur in seltenen Spezialfällen nötig ist, soll sie nicht bei jedem Lauf Kontext verbrauchen.

Bevorzugt:

```text
SKILL.md
→ Entscheidung: brauche ich Detail X?
→ genau diese Referenz laden
```

statt:

```text
SKILL.md mit 8.000 Zeilen
→ alles immer laden
```

## Scripts

Scripts sind sinnvoll, wenn ein Teil der Arbeit:

- deterministisch prüfbar ist;
- wiederholt gleich ausgeführt wird;
- durch Code zuverlässiger als durch freie Sprachinterpretation ist.

Ein Script darf jedoch keine versteckten Rechte oder externen Aktionen einführen.

## Assets

Assets können beispielsweise sein:

- Templates;
- Schemas;
- Beispieldaten;
- statische Prüflisten.

Sie sind Arbeitsmaterial, keine projektspezifische Wahrheit.

## Portabilität

Wo möglich soll die Skilllogik nicht an einen einzigen Agentenclient gebunden werden.

Plattformspezifische Details gehören in:

- Compatibility-/Capability-Hinweise;
- Adapter;
- Fallbacks;

statt in die fachliche Kernlogik.

## Leitgedanke

> Kleiner Discovery-Footprint, klarer operativer Kern, Details nur bei Bedarf.
