# Lizenzentscheidung für eine spätere Open-Source-Veröffentlichung

Stand: 2026-08-25

Diese Entscheidungsvorlage betrifft ausschließlich das **eigene KI-Regeln-Material**. Drittmaterial bleibt unabhängig davon unter den jeweils anwendbaren Bedingungen. Die technische Provenance-Prüfung ersetzt keine Rechtsberatung.

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
- löst weder Rights-Holder- noch Third-Party-Provenance-Fragen.

## Apache License 2.0

### Vorteile

- ebenfalls permissiv;
- enthält einen ausdrücklichen Patent Grant mit Patent-Termination-Regel;
- beschreibt Lizenz-/Notice- und Änderungsanforderungen ausführlicher;
- kann sinnvoll sein, wenn Patentklarheit für Contributors oder Implementierungen eine zentrale Governance-Anforderung ist.

### Nachteile

- deutlich länger und prozessreicher als MIT;
- die NOTICE-Mechanik erhöht den Pflegeaufwand, wenn sie tatsächlich relevant wird;
- für das derzeit überwiegend dokumentations- und methodenorientierte Repository entsteht aus dem zusätzlichen Mechanismus kein offensichtlich notwendiger Nutzen;
- auch Apache-2.0 kann ungeklärtes Drittmaterial oder unklare Rechteinhaberschaft nicht nachträglich bereinigen.

## Empfehlung

Für die derzeitige Struktur von KI-Regeln ist **MIT der bevorzugte Kandidat**: permissiv, leicht verständlich und für die erwartete Wiederverwendung von Regeln, Skills, Dokumentation und kleinen Tools ausreichend schlank.

Apache-2.0 wäre die stärkere Alternative, falls vor Veröffentlichung ein ausdrücklicher Patent Grant als bewusste Projektanforderung festgelegt wird.

## Decision Gate vor Einführung einer Root-Lizenz

Die Empfehlung ist noch **keine wirksame Lizenzierung** des Repositories.

Eine Root-`LICENSE` wird erst eingeführt, wenn:

1. die Rights-/Copyright-Holder für das eigene Material belastbar bestätigt sind;
2. redistribution-relevantes Drittmaterial vollständig identifiziert und mit seiner eigenen Lizenz-/Notice-Pflicht isoliert ist;
3. offene `needs-human/legal-review`-Fälle einer Root-Lizenzierung nicht entgegenstehen;
4. ein Public-Release-Audit die Einführung ausdrücklich freigibt.

Repository-Eigentum, GitHub-Organisation oder Commit-Autorenschaft werden dabei nicht automatisch mit vollständiger urheberrechtlicher Rechteinhaberschaft gleichgesetzt.

**Phase-3-Entscheidung:** MIT empfohlen; Root-`LICENSE` bis zur bestätigten Rights-Holder-Entscheidung blockiert.
