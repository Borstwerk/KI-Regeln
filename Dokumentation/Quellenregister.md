# Quellenregister und Upstream-Monitoring

## Zweck

Die fachbezogenen `Quellen-und-Inspirationen.md`-Dateien dokumentieren, **woher Konzepte stammen**.

Dieses Register ergänzt eine zweite Frage:

> Welche externen Quellen können sich verändern und sollten deshalb aktiv auf Updates überwacht werden?

Die maschinenlesbare Liste steht in `upstream-sources.yml`.

## Zwei Arten von Quellen

### Stabile Referenzquellen

Beispiele:

- veröffentlichte Paper;
- historische Artikel;
- abgeschlossene Spezifikationen;
- grundlegende Frameworks wie Diátaxis.

Sie werden in den jeweiligen Fachbereichen dokumentiert und bei Bedarf erneut fachlich geprüft.

### Mutable Upstreams

Beispiele:

- `SKILL.md` auf einem `main`-Branch;
- laufend gepflegte Agent-Skill-Sammlungen;
- aktuelle Tool-Dokumentation;
- Style Guides oder Best-Practice-Sammlungen, die weiterentwickelt werden.

Diese Quellen können sich ändern, ohne dass unser Repository automatisch davon erfährt.

## Was wird gespeichert?

Für aktiv beobachtete Upstreams möglichst:

- eindeutige ID;
- Fachbereich;
- Repository und Dateipfad oder URL;
- beobachteter Branch / Ref;
- zuletzt beobachteter Blob-SHA oder veröffentlichte Version;
- Datum der letzten Prüfung;
- lokale Dateien, die von diesem Upstream beeinflusst wurden.

Beispiel:

```yaml
- id: beispiel-skill
  area: Recherche
  kind: github-file
  repository: owner/repo
  path: skills/example/SKILL.md
  ref: main
  observed_sha: abc123...
  last_checked: 2026-08-23
  local_impact:
    - Recherche/Skills/example/SKILL.md
```

## Monatlicher Upstream-Check

Für jeden Eintrag:

```text
gespeicherter SHA / Version
        ↓
aktuellen Upstream lesen
        ↓
unverändert?
   ├─ ja → last_checked aktualisieren
   └─ nein
        ↓
      Diff / neue Version prüfen
        ↓
      betrifft übernommene Konzepte?
        ├─ nein → Registry aktualisieren, keine lokale Regeländerung
        └─ ja  → Änderungskandidat dokumentieren
                    ↓
                  normaler Review- und Changelogprozess
```

## Keine automatische Synchronisierung

Ein Upstream-Update führt **niemals automatisch** zu einer Änderung unserer Skills.

Gründe:

- Upstream kann tool- oder projektspezifischer geworden sein;
- eine neue Regel kann unseren Grundsätzen widersprechen;
- der lokale Skill kann bewusst anders abstrahiert sein;
- ein Update kann Regressionen oder unnötige Komplexität einführen.

Deshalb gilt:

> Upstream-Änderung = Review-Signal, nicht Sync-Befehl.

## Änderungen bewerten

Bei einem geänderten Upstream prüfen:

1. Was hat sich tatsächlich geändert?
2. Betrifft es ein Konzept, das wir übernommen haben?
3. Ist der neue Ansatz allgemeiner, belastbarer oder sicherer?
4. Widerspricht er unseren bestehenden Regeln?
5. Ist eine lokale Änderung nötig oder nur die Quellenbasis zu aktualisieren?
6. Müssen Skill-Handbuch, Changelog oder Evals angepasst werden?

## Neue Upstreams aufnehmen

Ein Eintrag in `upstream-sources.yml` lohnt sich insbesondere, wenn:

- eine konkrete externe `SKILL.md` unsere lokale Regel deutlich beeinflusst hat;
- die Quelle regelmäßig gepflegt wird;
- Änderungen wahrscheinlich relevant sein können;
- ein gezielter Diff günstiger ist als regelmäßige komplette Neurecherche.

Nicht jede Webseite oder jedes Paper muss in die Upstream-Liste.

## Entfernte oder aufgegebene Quellen

Wenn eine Quelle verschwindet oder nicht mehr gepflegt wird:

- nicht automatisch unsere abgeleiteten Regeln löschen;
- lokale Regeln weiterhin nach eigenem Nutzen und Evidenz bewerten;
- Quelle im Register als `inactive` oder `archived` markieren;
- bei kritischer Abhängigkeit nach einer aktuelleren Primärquelle suchen.

## Verhältnis zu den Fachquellen

```text
Fachbereich/Quellen-und-Inspirationen.md
→ Was hat uns fachlich beeinflusst?

Dokumentation/upstream-sources.yml
→ Welche veränderlichen Quellen beobachten wir aktiv?

CHANGELOG.md
→ Welche lokalen Regeln haben wir tatsächlich geändert?
```

## Leitgedanke

> Quellen sollen nicht nur zitierbar, sondern bei veränderlichen Upstreams auch wartbar sein.
