# Skill-Struktur und Progressive Disclosure

## Inhalt

- Grundprinzip
- Empfohlene Struktur
- Drei Ebenen
- Kontextbudget
- Navigierbare Referenzen
- Freiheitsgrad und Determinismus
- Scripts
- Assets
- Portabilität
- Leitgedanke

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

Als praktische Portabilitätsheuristik soll der Body von `SKILL.md` möglichst deutlich unter 500 Zeilen bleiben. Die Zahl ist kein Qualitätsbeweis und kein universelles Laufzeitlimit; sie ist ein Signal, umfangreiche Spezialdetails über Progressive Disclosure auszulagern.

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

## Navigierbare Referenzen

Referenzen müssen nicht nur vorhanden, sondern für die Laufzeit auffindbar sein.

- Referenz- oder Fachdokumente mit mehr als ungefähr 100 Zeilen erhalten nahe am Anfang ein Inhaltsverzeichnis, das die relevanten Hauptabschnitte sichtbar macht.
- Eine begründete Ausnahme ist möglich, wenn die Datei beispielsweise rein generiert, strikt tabellarisch oder anderweitig bereits eindeutig navigierbar ist; die Ausnahme soll dann dokumentiert sein.
- Wichtige Detailinformationen dürfen nicht nur über Ketten aus Referenz → Referenz → weitere Referenz erreichbar sein. Für portable Skill-Pakete sollen benötigte Referenzen möglichst direkt aus `SKILL.md` erreichbar sein.
- Shared Domain Docs dieses Repositories dürfen außerhalb des Skill-Verzeichnisses liegen, sollen aber vom verwendenden `SKILL.md` direkt benannt werden, wenn sie für die Ausführung relevant sind.

Die ~100-Zeilen-Grenze ist eine Authoring-Heuristik für Laufzeiten, die lange Dateien teilweise vorab ansehen. Sie bedeutet **nicht**, dass Inhalt nach Zeile 100 grundsätzlich unsichtbar oder unwirksam ist.

## Freiheitsgrad und Determinismus

Der notwendige Instruktionsgrad wird **pro wesentlichem Arbeitsschritt** gewählt, nicht pauschal pro Skill.

### Hoher Freiheitsgrad

Geeignet, wenn mehrere Lösungswege fachlich gültig sind und Kontext die beste Vorgehensweise bestimmt.

Bevorzugt: Ziel, Kontext/Motivation, Qualitätskriterien, relevante Referenzen/Beispiele, Grenzen und Evidence.

Bei hohem Freiheitsgrad nicht unnötig den internen Lösungsweg als langen Schritt-für-Schritt-Plan vorschreiben. Sequenzielle Schritte oder Checklisten sind dagegen sinnvoll, wenn Reihenfolge oder Vollständigkeit fachlich tatsächlich zählt.

### Mittlerer Freiheitsgrad

Geeignet, wenn ein bevorzugtes Muster existiert, aber Parameter oder konkrete Ausgestaltung variieren dürfen.

Bevorzugt: Template, Pseudocode oder klarer Vertrag mit konfigurierbaren Teilen.

### Niedriger Freiheitsgrad

Geeignet, wenn ein Schritt fragil, fehleranfällig, folgenreich oder bewusst reproduzierbar sein muss.

Bevorzugt: deterministischer Check, Script oder Command Wrapper, wenige explizite Parameter und zusätzliche Human-/Safety-Gates bei realer Außenwirkung.

Ein Skill kann mehrere Freiheitsgrade kombinieren. Mehr Text ist **kein** Ersatz für Determinismus: Wenn ein kritischer Schritt exakt gleich ablaufen muss, ist ein geprüftes Script oft robuster als immer längere Sprachinstruktionen.

## Scripts

Scripts sind sinnvoll, wenn ein Teil der Arbeit:

- deterministisch prüfbar ist;
- wiederholt gleich ausgeführt wird;
- durch Code zuverlässiger als durch freie Sprachinterpretation ist.

Ein Script darf jedoch keine versteckten Rechte oder externen Aktionen einführen. Benötigte Runtime-, Paket- und Toolabhängigkeiten werden nach `Toolanforderungen-und-Fallbacks.md` explizit beschrieben und vor Ausführung geprüft.

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
- Runtime-Adapter oder klar gekapselte Metadaten;
- Fallbacks;

statt in die fachliche Kernlogik.

### Shared Core statt Client-Kopien

Wenn mehrere Clients dieselbe Arbeitsdisziplin nutzen, bleibt `SKILL.md` die gemeinsame fachliche Source of Truth.

Client- oder modellspezifische Konfiguration wird davon getrennt gehalten, insbesondere:

- Modellrouting;
- konkrete Tool-Allow-/Deny-Listen;
- Turn-/Execution-Limits;
- Isolation/Subagent-Konfiguration;
- host-spezifische Hooks;
- temporäre Runtime-Workarounds.

Mehrere fast identische Skillkopien sind zu vermeiden, wenn nur die Laufzeitkonfiguration variiert.

Details: `Portabler-Skill-Kern-und-Runtime-Adapter.md`.

## Leitgedanke

> Kleiner Discovery-Footprint, klarer operativer Kern, Details nur bei Bedarf.
