# Umgebungsabhängige Verifikation und Reports

## Zweck und Scope

Bei Softwareänderungen folgt die Verifikation dem **konkreten Projekt**, nicht der Sprache des KI-Regeln-Repositories. Dies ist eine Discovery-/Handoff-Regel für `test-strategy`, `verification-loop` und die Workflows `Software-Feature` sowie `Teststrategie-und-QA`; kein zusätzlicher Skill, Test-Runner oder Runtime-Zwang.

## Verification Discovery – vor der Ausführung

1. **Auftrag und Risikoschnitt bestimmen:** Welche Änderung, kritischen Invarianten, Testebenen und Qualitätsgates sind betroffen?
2. **Projektvorgaben zuerst lesen:** `AGENTS.md`, README, Build-/Testskripte, CI-Konfiguration, vorhandene Tests und projektlokale Source of Truth. Vorgegebene Testbefehle nicht durch eigene Präferenzen ersetzen.
3. **Umgebung tatsächlich beobachten:** Betriebssystem, Architektur, Sprache(n), Framework, Toolchain-Versionen, vorhandene Test-Runner und benötigte Abhängigkeiten. WPF-UI braucht zum Beispiel eine geeignete Windows-Runtime; portable .NET-Unit-Tests nicht unbedingt.
4. **Prüfplan nach Fähigkeit und Risiko wählen:** kleinste ausreichende native Prüfung; ergänzende Integration/E2E nur, wenn ein spezifisches Risiko es verlangt. Für PowerShell z. B. vorhandene Pester-/Analyzer-Projektkonfiguration, für .NET die passende Build-/Testkonfiguration – keine universellen Pflichtbefehle.
5. **Ausführungsrechte prüfen:** Ein gefundener Befehl ist keine Autorisierung. Vor unbekannten Skripten, externen Diensten, Datenbankwrites, Installation, Netzwerknutzung oder destruktiven Aktionen Wirkung und Projektfreigabe prüfen. Ohne Freigabe `BLOCKED` statt blind ausführen.
6. **Mit frischer Evidence ausführen:** Exitcode, beobachteten Status, Skips, Prüfumgebung und den exakt getesteten Quellzustand erhalten. Nach verhaltensrelevanten Änderungen erneut testen. Bei fehlendem SDK/OS/Runner `NOT_RUN` oder `BLOCKED`, nie einen Ersatz als gleichwertig ausgeben.

**Mehrsprachen-Projekte:** pro betroffener Komponente die passende native Prüfung wählen. Ein PowerShell-Orchestrator für eine C#-Anwendung ersetzt keine relevanten .NET-Tests; Python ist **keine** verpflichtende Prüfsprache.

## Portabler Datenvertrag

`../Schemas/verification-run.schema.json` (Draft 2020-12, `schema_version: 1`) ist ein **optionaler Austauschvertrag** für lokale, CI- oder Agentenläufe. Er beschreibt Beobachtungen, **führt selbst keine Tests aus**. Bestehende projektspezifische Reports bleiben gültig; Adapter dürfen nach diesem Vertrag exportieren, ohne ihre Fachlogik neu zu implementieren.

Minimalfelder:

- `project`, `task`: betroffener Auftrag und Projekt.
- `source_state`: `git-clean` mit Revision, `git-dirty` mit Revision und Digest inkl. dokumentiertem Scope, `snapshot` mit Digest und Scope oder `unavailable` mit Grund. Ein Commit alleine bindet **keine** nichtcommitteten Änderungen.
- `environment`: `location` (`local`, `ci`, `cloud-agent`, `other`), Betriebssystem und Runtime.
- `checks[]`: Prüftyp, Auswahlursprung, konkretes Tool, `required_for_claim`, Status, Exitcode, Skips, Evidence-Referenzen und gegebenenfalls Grund.

Statussemantik je Prüfung:

| Status | Bedeutung |
| --- | --- |
| `PASS` | Tatsächlich ausgeführt, Exitcode 0, keine Skips und mindestens eine beobachtbare Evidence-Referenz; kein Beweis, dass die gesamte Aufgabe gelöst ist |
| `FAIL` | Tatsächlich beobachteter Fehlschlag; Ursache/Exitcode beschreiben, nicht automatisch Produktdefekt behaupten |
| `BLOCKED` | Fehlende Rechte/Voraussetzungen oder Sicherheitsgate; kein ausgeführter Testclaim |
| `NOT_RUN` | Nicht ausgeführt, Grund erforderlich |
| `UNVERIFIED` | Ergebnis beobachtet oder berichtet, aber für den Claim nicht belastbar |

Ein `source_state.kind: unavailable` darf **keinen** `PASS`-Check tragen. Für `git-dirty` und `snapshot` fordert das Schema einen SHA-256-Digest mit deklariertem Scope. Digest-/Revision-Bindung, tatsächliche Ausführung und die Glaubwürdigkeit der Evidence müssen durch den ausführenden Adapter bzw. unabhängige Prüfungen nachgewiesen werden – JSON-Schema allein kann das **nicht**.

`checks[].required_for_claim` benennt die für einen konkreten Claim relevanten Checks. **Absichtlich kein globales `overall_pass` im Vertrag:** Ein grüner Teilcheck, ein fehlender Pflichtcheck oder ein abgesenkter Qualitätsmaßstab dürfen nicht zu einer Gesamtfreigabe hochgerechnet werden. Release/Human-Gates bleiben projektspezifisch.

### Beispiel – lokaler PowerShell-Prüflauf

```json
{
  "schema_version": 1,
  "project": {"name": "Beispiel-Skript"},
  "task": "Parser und Tests prüfen",
  "source_state": {"kind": "git-clean", "revision": "abc123"},
  "environment": {"location": "local", "os": "Windows", "runtime": "PowerShell 7"},
  "checks": [
    {
      "id": "unit-pester", "type": "unit", "required_for_claim": true,
      "selection": "project-prescribed", "tool": "Pester",
      "command_display": "Invoke-Pester -Path ./tests",
      "status": "PASS", "exit_code": 0, "skipped": 0,
      "evidence_refs": ["artifacts/pester-summary.xml"],
      "observed_at": "2026-10-15T09:00:00Z"
    },
    {
      "id": "external-sql", "type": "integration", "required_for_claim": true,
      "selection": "discovered", "tool": "SQL integration",
      "status": "BLOCKED", "exit_code": null, "skipped": 0,
      "evidence_refs": [], "reason": "Keine freigegebene Testdatenbank"
    }
  ]
}
```

*Das Beispiel ist synthetisch, nicht ausgeführt und kein PASS für eine Gesamtanwendung.*

## Reporting und Renderer-Grenze

Maschinenlesbare Evidence zuerst. Ein späterer HTML-Renderer auf Basis von `visual-answer` darf nur darstellen, filtern und auf Artefakte verweisen – keine Tests neu bewerten, keine fehlenden Werte erfinden. Rohlogs, Secrets, Zugriffstokens, Patienten-/Personendaten oder unkontrollierte Toolausgaben nicht automatisch in öffentliche Reports schreiben. Links und angezeigte Befehle redigieren; HTML sicher escapen.

`Schema valide` bedeutet nur: **Report formal plausibel**, nicht: Tests erfolgreich ausgeführt, Agent regelkonform, unabhängiger Review bestanden oder Release autorisiert.

## Grenzen und Weiterentwicklung

PR A umfasst nur Discovery-Regeln, Schema und synthetische Vertragskontrollen. Noch **keine** automatische Projekterkennung, kein nativer Runner-Adapter, keine HTML-Erzeugung und kein realer projektübergreifender Test. Das bestehende B2-/Behavioral-Harness bleibt unverändert.
