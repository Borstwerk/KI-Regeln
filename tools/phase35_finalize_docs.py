from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


# CHANGELOG: add Phase 3.5 only under Unreleased.
changelog = Path("CHANGELOG.md")
text = changelog.read_text(encoding="utf-8")
anchor = "Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.\n\n"
section = """### Hardening Phase 3.5 – Webdesign und Motion

- Webdesign um drei klar getrennte Motion-Skills ergänzt: `motion-design` definiert Zweck und Motion-Contract, `motion-implementation` setzt freigegebene Motion technisch um und `motion-review` bewertet vorhandene Motion unabhängig; Reverse Engineering aus Screenrecordings bleibt Evidence-Modus von `motion-review` statt eigener vierter Skill;
- gemeinsame Grundlage `Webentwicklung/Webdesign/Motion-und-Mikrointeraktionen.md` ergänzt: keine Animation als valides Ergebnis, kontextabhängige Timing-/Easing-Entscheidung, Spatial Continuity, Gesten, Interruptibility, Reduced Motion, evidenzbasierte Toolwahl und Performance ohne GPU-/Property-/Library-Dogmen;
- vier bestehende Web-Skills nur an realen Routingkanten geschärft (`frontend-design`, `design-system`, `web-design-review`, `visual-verification`); `accessibility-review` und `frontend-performance` blieben nach Prüfung unverändert;
- drei Motion-Evalpacks mit insgesamt 26 definierten Cases ergänzt, einschließlich positiver Trigger, Landingpage-/WCAG-/Performance-Near-Misses, `keine Animation`, Reduced Motion, Toolwahl, fehlende Render-Evidence sowie Screenrecording → `motion-review` → `motion-implementation` → `visual-verification`; diese Cases sind definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden;
- drei methodische Skill-Upstreams source-spezifisch als `reference/inspiration` geprüft (`emilkowalski/skills`, `mblode/agent-skills`, `Leonxlnx/taste-skill`); finaler Text übernimmt keine konkreten Tabellen, Skalen, Defaultwerte oder Source-Struktur und bleibt `similarity_audit: no-signal`; genealogisch abhängige Hinweise werden nicht als unabhängiger Konsens doppelt gezählt;
- acht konkrete technische Primärquellen für Reduced Motion, WAAPI, `@starting-style`, View Transitions, Scroll-driven Animations sowie Motion-/GSAP-Fähigkeiten registriert; technische Primärquellen werden nicht als methodischer Designkonsens behandelt;
- Skill-Katalog von 128 auf 131 Skills erweitert; die drei neuen Skills starten `experimental` mit `partial` Evalabdeckung, ohne bestehende Maturity hochzustufen; aktueller Coverage-Stand 103× `partial`, 28× `none`;
- GT-09 bewusst nicht allein zur Erhöhung der Golden-Task-Anzahl erzeugt: der zusätzliche kombinierte Motion-Reproduktionsfall prüft bereits die neue Cross-Skill-Routingkante, ohne aktuell einen zusätzlichen systemischen Golden-Task-Gewinn zu belegen;
- Upstream-Governance bleibt `review-only` mit `auto_sync: false`; kein Merge, Tag, Release, Visibility-Wechsel oder automatische Upstream-Synchronisation durch Phase 3.5.

"""
if "### Hardening Phase 3.5 – Webdesign und Motion" in text:
    raise SystemExit("Phase 3.5 changelog section already present")
text = replace_once(text, anchor, anchor + section, "CHANGELOG anchor")
changelog.write_text(text, encoding="utf-8")


# Human skill catalog: preserve Phase-2 history, add current Phase-3.5 state.
catalog = Path("Dokumentation/Skill-Katalog.md")
text = catalog.read_text(encoding="utf-8")
text = replace_once(text, "Der Katalog enthält aktuell 128 zentrale Skills:", "Der Katalog enthält aktuell 131 zentrale Skills:", "catalog skill count")
text = replace_once(text, "- Webentwicklung: 8;", "- Webentwicklung: 11;", "catalog web count")
text = replace_once(
    text,
    "Der reproduzierbare Coverage-Audit für Phase 2 ergibt aktuell:\n\n- 128 Skills insgesamt;\n- 100 Skills mit `partial` Eval Coverage;\n- 28 Skills mit `none`;\n- 0 Skills mit `core` oder `broad`;\n- 100 Evalpacks mit insgesamt 489 definierten Skill-Cases.",
    "Der Phase-2-Auditstand vor Phase 3.5 betrug:\n\n- 128 Skills insgesamt;\n- 100 Skills mit `partial` Eval Coverage;\n- 28 Skills mit `none`;\n- 0 Skills mit `core` oder `broad`;\n- 100 Evalpacks mit insgesamt 489 definierten Skill-Cases.",
    "Phase-2 snapshot wording",
)
anchor2 = "Für Social Media und Content-Präsenz sind sechs Startfälle je Skill definiert, insgesamt 54. Die erwartete Verteilung ist 36× `pass`, 9× `partial` und 9× `blocked`. Diese 54 Fälle sind derzeit **definiert, aber noch nicht ausgeführt oder bestanden**.\n"
motion = """
Für Webentwicklung ergänzen `motion-design`, `motion-implementation` und `motion-review` den Bestand als `experimental` mit `partial` Evalabdeckung. Für diese drei Skills sind 26 Motion-Cases definiert. Darunter befindet sich ein kombinierter Screenrecording-Reproduktionsfall, der die Komposition `motion-review → motion-implementation → visual-verification` absichert; er begründet derzeit keinen separaten `motion-reverse-engineering`-Skill. Die 26 Fälle sind **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**.

Aktueller Gesamtstand nach Phase 3.5: 131 Skills, davon 103× `partial` und 28× `none`, 0× `core`/`broad`; 103 Skill-Evalpacks mit insgesamt 515 definierten Cases. Die drei neuen Skills wurden nicht über `experimental` hinaus hochgestuft.
"""
text = replace_once(text, anchor2, anchor2 + motion, "motion catalog insertion")
catalog.write_text(text, encoding="utf-8")
