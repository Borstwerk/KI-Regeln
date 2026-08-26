# Lizenzentscheidung für eine spätere Open-Source-Veröffentlichung

Stand: 2026-08-26

Diese Projektentscheidung betrifft ausschließlich das **originäre KI-Regeln-Material**. Drittmaterial bleibt unabhängig davon unter den jeweils anwendbaren Bedingungen. Die technische Provenance-Prüfung ersetzt keine Rechtsberatung.

## Zielbild

Die gewünschte Projektrichtung ist permissive Open Source mit möglichst niedriger Einstiegshürde für Nutzung, Anpassung und Weitergabe. Die Lizenz soll zu einem Repository passen, das überwiegend aus Regeln, Skills, Workflows, Dokumentation, Evals und kleinen Audit-/Validator-Werkzeugen besteht.

## MIT

### Vorteile

- sehr kurze und verbreitete permissive Lizenz;
- geringe Integrations- und Verständnislast für Nutzer und Beiträge;
- erlaubt Nutzung, Änderung und Weitergabe unter Beibehaltung des Copyright-/Permission-Hinweises;
- passt gut zu einem Repository, dessen Hauptwert in wiederverwendbaren Text-, Regel- und kleinen Tool-Artefakten liegt;
- benötigt keinen zusätzlichen NOTICE-Prozess für das eigene Projektmaterial.

### Nachteile

- enthält keinen so ausdrücklichen Patent Grant und keine Patent-Termination-Mechanik wie Apache-2.0;
- bietet weniger formalisierte Leitplanken für Notices und Änderungen;
- löst keine Third-Party-Provenance-Fragen für Fremdmaterial.

## Apache License 2.0

Apache-2.0 wurde als permissive Alternative betrachtet. Sie enthält einen ausdrücklichen Patent Grant und detailliertere Notice-/Änderungsregeln, erzeugt für das derzeit überwiegend dokumentations- und methodenorientierte KI-Regeln-Projekt aber zusätzlichen Prozess ohne festgestellten projektspezifischen Bedarf.

## Verbindliche Projektentscheidung

**MIT entschieden.**

Der autorisierte Projekt-/Rights-Holder-Decision-Gate ist am 2026-08-26 geschlossen worden: Das originäre KI-Regeln-Projektmaterial soll unter der **MIT License** veröffentlicht werden.

Dementsprechend liegt im Repository eine Root-`LICENSE` mit dem standardmäßigen MIT-Lizenztext und dem neutralen projektbezogenen Copyright-Hinweis

`Copyright (c) 2026 KI-Regeln contributors`

vor.

Die Root-MIT-Lizenz wird **nicht** als Relicensing von Drittmaterial verstanden:

- tatsächlich redistribution-relevante Fremdanteile bleiben unter ihrer jeweiligen dokumentierten Lizenz und ihren Notice-/Attributionspflichten;
- `THIRD-PARTY-NOTICES.md` bleibt für solche Fremdanteile maßgeblich;
- die vier Matt-Pocock-Adaptionsfälle behalten ihre dokumentierte same-state-MIT-Evidence und den dafür geführten MIT-Notice;
- `neon-postgres-best-practices` ist nach source-spezifischem Review `assessed / reference/inspiration / concepts/methods-only / not-relied-on`; seine same-state Apache-2.0-Evidence ist historische Provenance-Evidence, keine benötigte Redistributionsfreigabe für den lokalen Reference-only-Fall.

Repository-Eigentum, GitHub-Organisation oder einzelne Commit-Autorenschaft werden durch diese Dokumentation nicht pauschal zu einer Aussage über die persönliche Rechteinhaberschaft einzelner Personen umgedeutet. Die verwendete Copyright-Zeile ist bewusst projektbezogen und neutral.

## Verbleibende Release-Grenze

Die Projektlizenzentscheidung selbst ist kein offener Public-Release-Blocker mehr. Ein Public Release bleibt dennoch getrennt gated, insbesondere bis der dokumentierte private Security-Reporting-Pfad für den öffentlichen Repositoryzustand tatsächlich eingerichtet und praktisch verifiziert wurde.
