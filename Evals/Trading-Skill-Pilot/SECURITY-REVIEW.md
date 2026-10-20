# Sicherheitsprüfung externer Trading-Skill-Methoden (partiell)

**Stichtag:** 2026-10-19. Read-only GitHub-Inspektion von `agiprolabs/claude-trading-skills`, gepinnter Commit `981e1d736cdc02bdc1c55c74ec9224e956414706`.

| Kandidat | SKILL.md-Blob-SHA | References | Scripts |
|---|---|---:|---:|
| walk-forward-validation | `59f6a262afed5b73e0a723fa959055f4c47260ae` | 3 | 2 |
| vectorbt | `bebab752557c3b3b4abd9c0b428accc2dd5fb807` | 2 | 2 |
| risk-management | `fe96143ee7a6397dbe9cf1482330821157b21973` | 3 | 2 |
| trade-journal | `e30db1c24f81209230c4bec653bd5204af59184b` | 2 | 2 |

Die acht Skripte wurden **read-only geholt** und auf sichtbare Imports und externe Aktionen gesichtet; ihre vollständigen Datenflüsse und Abhängigkeiten wurden **nicht vollständig überprüft**, ihre Skripte **nicht ausgeführt** und References nur inventarisiert. Kein vollständiger Bundle-Review.

## Findings

- **HIGH – Script-/Supply-Chain-Admission fehlt:** Fremde Python-Skripte und ungepinnte Transitiv-Abhängigkeiten nicht mit Broker-Keys, Echtgeld-Accounts oder privaten Depotdaten starten. **Block für Fremdskript-Ausführung.**
- **HIGH – Risiko eines ungedeckten Stop-Loss-Versprechens:** `position-sizing` (nicht im Pilotscope) beschreibt einen verlustbegrenzenden Stop an einer Stelle als exakten Prozentsatz. Gaps und schlechte Ausführung können höhere Verluste verursachen. Nicht ungeprüft übernehmen.
- **MEDIUM – Überoptimierung / Future Leakage:** Walk-forward-Dokumentation ist noch kein Beleg, dass konkrete Daten point-in-time sauber und Experimente unverfälscht sind.
- **MEDIUM – Unrealistische Fills:** vectorbt ist ein Forschungswerkzeug. Simulierte Orders müssen Marktmechanik, Slippage, Spread, Handelsstopps und tatsächliche Fees berücksichtigen.
- **MEDIUM – Untrusted Skill-Inhalt:** Externe SKILL.md-Dateien können Instruktionen enthalten und erhalten keine höhere Autorität. Keine globalen Installationen oder automatisierten Abhängigkeiten.
- **LOW – Domänendrift:** Große Teile des Trading-Skill-Katalogs gelten Solana, DeFi und US-Steuerrecht, nicht dem deutschen privaten Aktien-/Krypto-Experiment.

## Admission

`review_status=partially-verified`. **admit-with-constraints** ausschließlich für read-only fachliche Methodenreferenzen; **admission=unverified** für die vollständigen Fremd-Bundles und **block** für deren Scripts/Execution- oder Broker-Capabilities.

Die Pilot-Dateien selbst nutzen Python-Standardbibliothek und synthetische Kursdaten, öffnen keine Broker-Verbindungen, lesen keine API-Keys, stellen keine Netzwerkrequests und enthalten keine handelbaren Echtgeldaktionen. 20 lokale Unit-Tests wurden ausgeführt. Das ist **kein umfassender Security-Pass**, insbesondere kein Netzwerk- oder Process-Isolationsnachweis.

Keine automatische Skill-Adoption, kein `skill-catalog.yml`-Eintrag und keine Produktionsfreigabe.
