# KI-Regeln im XERJ Corpus Hub – Status und offener Prüfpfad

**Stand: 29.10.2026 – externer Kandidat, NICHT als live suchbarer Corpus nachgewiesen.**
Dieses Dokument ist ein datierter Fremddienst-Status, **keine** neue Skill-, Lizenz-, Security- oder Routing-Wahrheit. Kanonische Quellen bleiben `AGENTS.md`, `skill-catalog.yml`, `LICENSE`, `ASSET-LICENSES.md`, `THIRD-PARTY-NOTICES.md`, `REUSE.toml` und `SECURITY.md`.

## Nachgewiesene externe Registry-Evidence

- XERJ-Registry: [Kandidat `borstwerk--ki-regeln`](https://github.com/xerj-org/xerj/blob/corpus-hub/tools/xerj-code/hub/candidates/authors/borstwerk--ki-regeln.json), **`status: draft`** und `cloned_at: null` am beobachteten Registry-Stand `540ccea61f8f90577d6c879e0d8dce6f3d6bdff8`.
- Als Quelle ist `https://github.com/Borstwerk/KI-Regeln` mit **altem Pin** `e4edd6c9257b16148294410b3875209167e443c8` hinterlegt. Die dokumentierte Zustimmung des Autors zur Aufnahme ist vorhanden; sie ist **kein** Nachweis eines bereits gebauten/indexierten/suchbaren Corpus.
- Im Eintrag lautet der Lizenzbefund für **diesen alten Pin** `NOASSERTION`, mit Hinweis auf **MIT auf Repository-Ebene** und gesonderte Zustimmung. `NOASSERTION` ist **kein Lizenztyp** und beweist weder eine MIT-Abdeckung jeder Datei noch eine Freigabe für alle Drittinhalte.
- Der [XERJ-Live-Katalog](https://hub.xerj.org/llms.txt) (laut Datei zuletzt aktualisiert **28.10.2026**, 524 Corpora) enthält keinen Treffer für `borstwerk` oder `ki-regeln`. **Nicht** mit späterer aktueller Live-Verfügbarkeit verwechseln. Contributor-Listung, Kandidatenregistrierung, gebauter/signierter Corpus und Live-Suchbarkeit sind verschiedene Zustände.

## Lizenz- und Umfangsgrenzen

- Für **KI-Regeln-eigenes Material** gilt die Root-[MIT-Lizenz](../LICENSE). Tatsächliche Adaptionen, Zitate und Weitergabe-Hinweise stehen in [THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md) und der kanonischen Provenance-Liste.
- **Sechs** generierte Medienassets sind ausdrücklich **von MIT ausgenommen** und separat unter **CC BY-SA 4.0** eingeordnet, soweit Rechte wirksam lizenziert werden können: [ASSET-LICENSES.md](../ASSET-LICENSES.md) / [REUSE.toml](../REUSE.toml).
- Der XERJ-Corpus sollte für agentische Wissenssuche vorzugsweise **kanonische Text-/Skill-Dateien** enthalten (z. B. `AGENTS.md`, `skill-catalog.yml`, `workflow-index.yml`, `Dokumentation/Skill-Handbuch.md`, `*/Skills/*/SKILL.md`). Historische Evals, Test-Fixtures, binäre Medien und generierte Reports dürfen nicht ohne Prüfung als gleichwertige normative Quelle erscheinen.
- Keine automatische Änderung am KI-Regeln-Repository, kein XERJ-Installer und keine pauschale `MIT`-Freigabe für fremde oder ausgenommene Dateien nur wegen eines Registry-Eintrags.

## Offene Fragen an XERJ

1. Ist der Kandidat nur zur Prüfung eingereicht (`draft`) oder ist bereits ein Build/Live-Termin beziehungsweise ein konkreter Blocker bekannt?
2. Kann der Pin auf einen **neueren explizit benannten Commit** aktualisiert werden, der die aktuellen `LICENSE`-, `ASSET-LICENSES.md`-, `REUSE.toml`- und `THIRD-PARTY-NOTICES.md`-Dateien enthält? Nicht ohne erneute Quellen-/Lizenzprüfung.
3. Kann die Indexierung relevante Text-/Skills-Verzeichnisse priorisieren oder ausgenommene Medienassets ausklammern? Wie bleibt die **gemischte Lizenzlage** in Metadaten und Zitaten erkennbar?
4. Woran ist eine spätere Live-Verfügbarkeit überprüfbar (Corpus-Seite, Registry-Merge, Signatur/Pack, konkrete Suchabfrage)?

**Kontaktstatus:** noch keine ausgehende Nachricht über dieses Projekt gesendet. Der ursprünglich erhaltenen E-Mail kann der Maintainer direkt antworten; keine Kontaktadresse erfinden.

## Retrieval-Abnahme erst NACH tatsächlicher Freischaltung

Eine kleine, vorab festgehaltene Frageprobe prüfen, ohne Modellantworten als Suchtreffer auszugeben:

| Prüffrage | Erwartete kanonische Quelle |
| --- | --- |
| „Wie findet ein Agent ohne Skillnamen eine passende Arbeitsweise?“ | `AGENTS.md`; `Dokumentation/Skill-Handbuch.md`; `skill-catalog.yml` |
| „Woran erkennt man, dass ein Test tatsächlich ausgeführt wurde?“ | `Testing-und-QA/`-Verifikationsregeln; `Evals/README.md` für Statusgrenzen |
| „Welche Freigabe braucht eine externe Aktion?“ | `AGENTS.md`; `Agentenarbeit/Human-Gates-und-Freigaben.md`; relevante Security-Regeln |

Pro Frage die **tatsächlichen Top-5-Datei-/Zeilen-Treffer**, Pin, Lizenzhinweis und Lücken erfassen. Historische Evals dürfen nicht als aktuelle Pflichtanweisung fehlgedeutet werden. Wenn kanonische Inhalte fehlen oder von Fixtures überlagert werden, XERJ-Index-Scope/Metadaten **mit Evidence** anpassen lassen. Kein eigener Such-Router für diesen Fremddienst erforderlich.

## Nicht durch diesen Review nachgewiesen

Keine persönliche Contributor-Seite verifiziert, kein erfolgreicher Corpus-Pull, keine lokal ausgeführten XERJ-Suchen, kein verifiziertes XERJ-Lizenzreview für den aktuellen KI-Regeln-Commit, keine bestätigte GitHub Private Vulnerability Reporting-Konfiguration und keine neue Security-/Secret-History-Prüfung.
