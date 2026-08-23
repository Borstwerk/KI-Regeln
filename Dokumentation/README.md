# Dokumentation

Dieser Bereich erklärt, wie das Repository praktisch verwendet, gepflegt und verstanden wird.

Er richtet sich vor allem an Menschen, die:

- das Repository neu kennenlernen;
- verstehen möchten, was einzelne Skills bedeuten;
- Regeln in eigene Projekte übernehmen wollen;
- den Bestand regelmäßig auf Aktualität prüfen möchten;
- nachvollziehen möchten, welche externen Skills und Quellen aktiv beobachtet werden.

## Inhalte

- `Nutzung-des-Repositories.md` – erklärt, wie das Repository in echten Projekten eingesetzt wird;
- `Skill-Handbuch.md` – erklärt die allgemeinen Skills in verständlicher Sprache;
- `Skill-Handbuch-Dokumentationserstellung.md` – erklärt die Skills des Bereichs `Dokumentationserstellung/`;
- `Pflege-und-Aktualisierung.md` – beschreibt Pflegeprozess, Review-Rhythmus und den Umgang mit neuen Quellen und Entwicklungen;
- `Quellenregister.md` – erklärt Quellenklassen, Monitoring-Arten und den Umgang mit veränderlichen Upstreams;
- `upstream-sources.yml` – maschinenlesbare Liste aktiv beobachteter Upstreams mit Monitoring-Modus, Cadence, geprüftem SHA/Stand und lokalem Einfluss;
- `Upstream-Audit-2026-08-23.md` – dokumentiert den ersten vollständigen Audit aller Fachbereiche und begründet, welche Quellen aktiv beobachtet oder bewusst nur als Referenz/Radar behandelt werden.

## Grundsatz

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das Repository liefert wiederverwendbare Methoden. Projektziele, Fachlogik, Kanon, Architektur, Referenzen und lokale Anforderungen bleiben im jeweiligen Projekt.

## Quellen und Upstreams

Fachbereiche besitzen eigene `Quellen-und-Inspirationen.md`-Dateien. Sie beantworten:

> Welche externen Konzepte haben diesen Bereich beeinflusst?

Das zentrale Quellenregister beantwortet zusätzlich:

> Welche veränderlichen Quellen beobachten wir aktiv auf Updates?

Aktuell gibt es zwei Monitoring-Arten:

- `exact-sha` für konkrete GitHub-Dateien;
- `semantic-review` für lebende Web- und Produktdokumentation.

Zusätzlich unterscheiden wir zwischen monatlich und quartalsweise zu prüfenden Quellen.

Dabei gilt:

> Upstream-Änderung = Review-Signal, nicht automatischer Sync.

## Für Einsteiger

Wer das Repository zum ersten Mal verwendet, sollte in dieser Reihenfolge lesen:

1. `../README.md`
2. `Nutzung-des-Repositories.md`
3. `Skill-Handbuch.md`
4. bei Dokumentationsarbeit zusätzlich `Skill-Handbuch-Dokumentationserstellung.md`
5. erst danach die für das eigene Vorhaben relevanten Regel- und Skill-Dateien.

Nicht das komplette Repository muss für jede Aufgabe geladen oder übernommen werden. Gute Nutzung bedeutet gezielte Auswahl.