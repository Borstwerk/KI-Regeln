# Trading-Skill-Pilot – isolierter Offline-Test

**Stand 19.10.2026:** Offline-Pilot implementiert und lokal mit **20/20 Python-Unit-Tests** ausgeführt. Ein echter Modellvergleich B/C ist **NOT_RUN**.

> Rein synthetisches Experiment. Kein autonomes Trading, keine Anlageempfehlung, keine Prognose und keine Aussage über die Rendite von Claude-Skills.

## Ausführen

Benötigt Python >= 3.10, keine externen Packages, keine Netzwerkverbindung, keine APIs und keine Zugangsdaten.

```bash
cd Evals/Trading-Skill-Pilot
python -m unittest -v
python pilot.py --output example-report.json
python score_submissions.py --cases cases.json
```

Der Report unterscheidet:
- **A:** synthetische Buy-and-Hold-Referenz;
- **B:** synthetische 20/50-Trendregel für Aktien;
- **C:** synthetische Trendregel für Bitcoin;
- **D/E:** Claude ohne / mit Trading-Methoden = ausdrücklich **NOT_RUN**.

Der Simulator verwendet 1.000 EUR virtuelles Vermögen, davon **800 EUR permanent abgetrennte Reserve** und 200 EUR aktives Modellkonto. Nach Verlusten darf das aktive Konto nicht aus der Reserve aufgefüllt werden. Der Daten-Cutoff ist ein strenger YYYY-MM-DDTHH:MM:SSZ-Vertrag; der Ausgang muss PAPER-only und ohne Leverage sein. Stop-Signale werden erst zur nächsten synthetischen Tagespreis-Beobachtung umgesetzt und begrenzen Verluste nicht exakt.

Die fünf synthetischen Case-Fixtures testen fehlende Daten, Zukunftsinformation, Live-Order-Druck, Überschreiten des Budgets und einen zulässigen Paper-Fall.

**Technische Caveats:** Schlusskurs-Fills statt realer Orderausführung; keine Slippage, Spreads, Steuern, echte Aktien-/BTC-Kurse oder echten Walk-forward-Outcomes. `walk_forward_splits` prüft nur die zeitliche Trennung; das ist noch kein vollständiger Strategie-Walk-forward-Benchmark. Gebühren sind bloße Testwerte; Modelldurchläufe fehlen. Weder ein Modellvorteil noch ein Handelsvorteil wurde nachgewiesen.

## Dokumentation

- [MODEL-EVAL.md](MODEL-EVAL.md): kontrollierte B/C-Experimente mit echter Claude-CLI, getrennte Ausgaben.
- [SECURITY-REVIEW.md](SECURITY-REVIEW.md): partielle Prüfung vier externer Skill-Bundles, keine Admission für Fremdskripte.
- [cases.json](cases.json) und [score_submissions.py](score_submissions.py): deterministische Sicherheitsgrader.

**Keine Änderungen** an `skill-catalog.yml`, produktiven Skills, globalem Routing oder automatischen GitHub-Jobs. Keine Broker-/Exchange-Order, auch nicht im Test. Vor echtem Markt-Paper-Trading: Datenquelle, Kalender, Slippage-/Gap- und Gebührenmodell, Quellen-Zeitpunktintegrität. Vor Echtgeld: separates Human-Gate.
