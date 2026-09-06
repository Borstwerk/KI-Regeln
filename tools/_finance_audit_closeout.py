from pathlib import Path

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
marker = "Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.\n"
heading = "### Vertiefter Anthropic-Finance-Upstream-Audit"
section = """

### Vertiefter Anthropic-Finance-Upstream-Audit

- `anthropics/financial-services` am 2026-09-06 bis zum geprüften Commit `69cbc81467a5dced793eee03dec4658aa24ef856` vertieft als Apache-2.0-lizenzierter methodischer Referenzraum auditiert; Anthropic dient als Methodenquelle, nicht als Copy/Paste-, Runtime- oder automatische Sync-Abhängigkeit;
- bestehende Skills `vermoegensprojektion`, `portfolioanalyse` und `anlagevergleich` gegen unbelegte Universaldefaults, veraltete Finanz-/Produktdaten, vermischte Analyseebenen und implizite Aktionsautorisierung gehärtet;
- drei klar getrennte Finance-Skills `portfolio-rebalancing`, `unternehmensanalyse` und `bewertungsanalyse` ergänzt; alle drei starten `experimental` mit `partial` Evalabdeckung, ohne bestehende Maturity hochzustufen;
- `investmentthese` bewusst nicht als separaten Skill angelegt: falsifizierbare These, Gegenargumente, disconfirming Evidence und Invalidation Conditions bleiben zunächst Modus der `unternehmensanalyse`, bis persistentes Thesis-Tracking als eigenständiger wiederkehrender Job belegt ist;
- Workflow `Workflows/Unternehmens-und-Investmentanalyse.md` ergänzt und in `workflow-index.yml` registriert: Unternehmen verstehen → These/Gegen-Evidence → optional Bewertung → optional Anlagevergleich → optional Portfolio-Kontext → Human Gate;
- drei neue Finance-Evalpacks mit jeweils sechs Startfällen ergänzt, insgesamt 18 definierte Cases zu fehlender Zielallokation, veralteten Depot-/Unternehmens-/Marktdaten, automatischen Trades, aktueller Earnings-Evidence, unfalsifizierbaren Thesen, Peer-Cherry-Picking, erfundenen WACC-/Terminal-Growth-Defaults und DCF-zu-Order-Kurzschlüssen; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- bewusst nicht übernommen: 401(k), IRA, Roth, 529, RMD, Wash-Sale- und andere US-spezifische Konto-/Steuerlogik als allgemeine Wahrheit, feste Rebalancing-Bänder, feste WACC-/Terminal-Growth-/Multiple-Defaults, automatische Trade-Listen oder Buy/Hold/Sell-Automatismen sowie Anthropic-spezifische MCP-/Office-/Python-/Connector-/Subagent-Struktur;
- aktueller Gesamtstand: 148 Skills, 123× `partial`, 25× `none`, 0× `core`/`broad`; 123 Skill-Evalpacks mit insgesamt 640 definierten Cases;
- keine Broker-/Bank-/Trade-Aktion autorisiert, keine Maturity hochgestuft, keine Behavioral-Eval-Ergebnisse erfunden und kein Tag, Release oder automatischer Upstream-Sync erzeugt.
"""

if heading not in text:
    if marker not in text:
        raise SystemExit("Unreleased insertion marker not found")
    path.write_text(text.replace(marker, marker + section, 1), encoding="utf-8")
