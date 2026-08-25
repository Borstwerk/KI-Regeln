# Quellen und Inspirationen – Programmieren

## Zweck

Diese Datei dokumentiert externe Quellen, die die allgemeinen Programmier-Skills dieses Repositories beeinflusst haben.

Konkrete externe Skills werden nicht als unveränderliche Wahrheit behandelt. Die lokalen Skills sind eigenständig generalisiert und an die übergeordneten Regeln für Agentenarbeit, Evidence und Human Gates angepasst.

## Matt Pocock – Engineering Skills

Repository:

`https://github.com/mattpocock/skills`

Besonders relevante Upstreams:

- `skills/engineering/tdd/SKILL.md`;
- `skills/engineering/diagnosing-bugs/SKILL.md`;
- `skills/engineering/code-review/SKILL.md`;
- `skills/engineering/domain-modeling/SKILL.md`.

Nützliche Konzepte:

- TDD als kleiner testbarer Red/Green-Arbeitsloop;
- Diagnose über reproduzierbare Feedback-Loops, Hypothesen und gezielte Gegenproben;
- Code-Review gegen tatsächlichen Diff, Spezifikation und Repository-Standards;
- Domänenbegriffe und Architekturentscheidungen bewusst von Implementierungsdetails trennen.

Lokale Auswirkungen:

- `Skills/tdd/SKILL.md`;
- `Skills/diagnose/SKILL.md`;
- `Skills/code-review/SKILL.md`;
- `Skills/domain-modeling/SKILL.md`;
- teilweise `Entwicklungsprozess.md` und `Agent-Anweisungen.md`.

Die vier konkreten Skill-Dateien werden deshalb im zentralen Upstream-Register per Blob-SHA überwacht.

## AI Hero – Skill-Katalog

Quelle:

`https://www.aihero.dev/skills`

Einordnung:

Der Katalog war ergänzendes Beobachtungs- und Vergleichsmaterial für öffentlich verfügbare Software-Agent-Skills.

Er ist kein direkter Source-of-Truth-Upstream für eine konkrete lokale Regel und wird deshalb nicht als exakte Dependency synchronisiert. Neue relevante Skills können über den allgemeinen Radar-Check als Kandidaten auftauchen.

## Lizenz und Attribution

Das Monitoring der konkreten GitHub-Upstreams steht in `../Dokumentation/upstream-sources.yml`. Der aktuelle Lizenz-/Provenance-Prüfstand steht in `../Dokumentation/upstream-provenance.yml`. Daraus wird keine abschließende Redistributability oder Open-Source-Readiness abgeleitet.

## Leitgedanke

> Externe Coding-Skills liefern überprüfbare Arbeitsideen. Welche davon zentral gelten, entscheidet das lokale Regelwerk.