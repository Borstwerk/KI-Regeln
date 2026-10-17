# Workflow – Mobile App von der Idee bis zur Store-Freigabe

## Zweck und Abgrenzung

Führt eine **mobile** App kontrolliert von Zieldefinition und MVP über Gerätetests bis zur vorbereiteten iOS-/Android-Store-Einreichung. Das ist eine **Zusammenstellung vorhandener KI-Regeln-Methoden** mit wenigen plattformspezifischen Gates, **kein neuer Skill** und keine automatische Veröffentlichungsfreigabe.

**Verwenden:** neue mobile Apps, Expo/React-Native-Projekte und mobile Store-Releases. **Nicht verwenden:** reine Websites, Desktop-Anwendungen, App-Store-Marketing ohne vorliegende App oder ungeprüftes Verschieben einer produktiven App in neue Stacks. Ein bestehender Native-/Flutter-Stack geht vor Expo.

## Routing und Sources of Truth

Ausgangspunkt: `AGENTS.md` → `Dokumentation/Skill-Handbuch.md` → `skill-catalog.yml` → `routing-overlays.yml`, danach dieses Dokument. Wähle für die konkrete Aufgabe nur nötige Skills.

- Produktauftrag: `requirements-elicitation`/`requirements-baseline` nach Katalog, bei größerer Systementscheidung `architecture-decision` bzw. vorhandener Architekturworkflow.
- Konkretes Feature: [Software-Feature](Software-Feature.md).
- Risikobasierte Prüfungen: `test-strategy` und [Teststrategie und QA](Teststrategie-und-QA.md).
- Veröffentlichung: `deployment-strategy` für kontrollierten Release; externe Actions und Rechte mit `tool-permission-review` bewerten.
- Externe Plugins, Skill-Bundles und ausführbare Screenshothilfen **vor Aktivierung** mit `skill-security-review` prüfen.

**Priorität:** Projektkontext, reale App-/Plattformversion, aktuelle Apple-/Google-/Expo-Dokumentation und nachgewiesenes Toolverhalten schlagen dieses allgemeine Beispiel. Expo, EAS und TestFlight sind optionale **Runtimes**, keine KI-Regeln-Pflicht.

## Ablauf

```text
Nutzerproblem + Zielgruppe + Risiken
→ MVP-Scope + Abnahmekriterien + Datenflüsse
→ Stack-/Tool-Entscheidung und Rechteplan
→ Implementierung in kleinen, nachprüfbaren Schritten
→ echte Gerätetests + Datenschutz-/Security-Gates
→ Build + Signierung + Store-Metadaten (Preview)
→ TestFlight / interner Track + unabhängiges Review
→ explizite Einreichfreigabe → Submit → Reviewresultat
→ kontrollierte Veröffentlichung und Betrieb
```

### 1. Ziel, MVP und Datenverantwortung

- Zielplattformen, Kernnutzen, Zielgruppe, unterstützte Geräte und Betriebssysteme klären.
- **Kleinstes testbares MVP** und Akzeptanzfälle definieren; Streaks, Push-Benachrichtigungen, Accounts, Analytics und Käufe **nicht** als pauschale Wachstumstricks aufnehmen.
- Dateninventar erstellen: personenbezogene und sensible Daten, SDKs, Empfänger, Speicherung, Löschung, Einwilligungen und Berechtigungen. Kein fingiertes Privacy-Statement erzeugen.
- Ergebnis: MVP-Scope, User-Flows, erste Risks, Datenflussliste, explizite `OUT_OF_SCOPE`-Features.

**Gate:** Kein Code-Start aus einem Ein-Satz-Prompt, wenn kritische Produkt- oder Datengrenzen unklar sind.

### 2. Stack, Agent- und Toolrechte

- Vorhandenen App-Stack erhalten; für ein **neues** geeignetes Cross-Platform-Projekt sind React Native + Expo mögliche Optionen.
- SDK-/Node-/Expo-Go-Kompatibilität **aktuell** prüfen. Native-Module können Development Builds statt Expo Go erfordern.
- Projektordner und lokale Regeln trennen; Agent nur mit benötigten Dateirechten ausstatten.
- Installationen, neue Plugin-/MCP-Fähigkeiten und fremde Skills explizit reviewen, anstatt sie blind aus einem Web-Guide zu übernehmen.

**Gate:** Kein globales Installieren, keine geheimen Schlüssel in Prompts, keine Store-Credentials für reine Implementierungsaufgaben.

### 3. Implementierung und frühe Verifikation

- Kernfunktion entwickeln, automatisierte Tests passend zum Risiko ergänzen.
- Auf echten Geräten und den relevanten OS-Versionen kontrollieren: Navigation, Touch, Fokus/Screenreader soweit benötigt, Offline-/Netzfehler, App-Lifecycle, Fehlerzustände und Berechtigungsdialoge.
- Bei neuen Funktionen verifizieren und Artefakte/Evidence speichern. Browser-Vorschau allein ersetzt iOS-/Android-Gerätetests nicht.

**Gate:** Kein `PASS` für Plattformverhalten ohne ausgeführte Geräte-/Build-Evidence; sonst `NOT_RUN`.

### 4. Store-Readiness und Signierung

- Apple- und Google-Developer-Konten, Rechte, Bundle-ID/Application-ID, Signierung, Zertifikate/Provisioning und Versionsschema prüfen.
- Store-Metadaten: Name, Texte, Kategorien/Altersfreigabe, Support-Kontakt, Privacy Policy **auf Basis realer Datenflüsse**, App-Privacy-/Data-Safety-Angaben, Rechte an Marken und Bildern.
- Screenshots müssen zur tatsächlich implementierten App passen. KI-generierte Marketingrahmen dürfen keine Funktionen, Geräteansichten oder Behauptungen erfinden.
- Test- und Produktionsumgebungen samt Ziel-App/Tenant identifizieren; zunächst Preview/Plan-only, nicht direkt Submit.

**Gate:** Fehlende Privacy-/Berechtigungsnachweise, unklare Artwork-Rechte oder ungetesteter Release-Build blockieren die Freigabe.

### 5. Beta und unabhängiger Review

- Signierten Build auf TestFlight oder dem internen Android-Track überprüfen, inklusive Installation, Start, Kernflow, Gerätetests, Crash-/Privacy-Befunden.
- Unabhängigen Release-Check durchführen. Dokumentieren, was `VERIFIED`, `FAILED`, `NOT_RUN` ist.
- Store-Review kann trotz grüner lokaler Tests ablehnen; Metadaten und mögliche Ablehnungsgründe vorab kontrollieren.

**Gate:** Build erfolgreich ≠ eingereicht ≠ freigegeben ≠ veröffentlicht.

### 6. Einreichung, Veröffentlichung und Betrieb

- Vor **jedem** Upload, Submit, Release oder kostenpflichtiger Aktion die aktuelle Account-/Umgebungsidentität und die **explizite Autorisierung** für genau diese Aktion prüfen.
- Keine automatische Store-Einreichung aufgrund einer früheren Zustimmung zum Entwickeln.
- Reviewstatus nachhalten; bei Ablehnung gezielt korrigieren und erneut freigeben lassen.
- Geplante Veröffentlichung, Release Notes, Support, Telemetrie/Datenschutz, Incident- und Updatepfad dokumentieren. Nicht reversible Außenwirkungen und tatsächliche Rollback-Grenzen offenlegen.

## Kurz-Verifikationsvertrag

| Dimension | Nachweis / Status |
| --- | --- |
| MVP und tatsächliche Features | getesteter Akzeptanzfall, `VERIFIED` oder `NOT_RUN` |
| Android und iOS | **getrennte** Build-/Geräte-Evidence; keine plattformübergreifende PASS-Abkürzung |
| Datenschutz und Berechtigungen | realer SDK-/Datenflussreview, Policy- und Plattformangaben |
| Store-Metadaten und Screenshots | belegter Produktbezug, Rechte, menschlicher Review |
| Identität des Ziel-Stores | aktuell verifizierte Account-/App-/Track-Identität |
| Außenaktion | spezifische menschliche Freigabe + beobachtetes Submit-Ergebnis |
| Betrieb | Release-/Support-/Rollbackplan, offene Restrisiken |

## Externe methodische Quellen (keine Übernahme)

- [Expo – Build with AI](https://docs.expo.dev/tutorial/build-with-ai/introduction/) und [Expo Agenten/Skills](https://docs.expo.dev/agents/): entwicklungsnahe Beispiele, **keine** pauschale Toolfreigabe.
- [Expo – Development Builds](https://docs.expo.dev/develop/development-builds/introduction/) und [EAS Build](https://docs.expo.dev/build/introduction/).
- [Apple – App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/de/): verbindliche aktuelle Richtlinien und Privacy-Anforderungen gesondert prüfen.
- [Seb AI – App-Workflow](https://seb-ai.pages.dev/app/): Inspiration für menschlichen Fünfschritte-Einstieg, **keine** primäre technische Autorität. Keine Seitenscripts oder Webhooks übernommen.

**Scope:** Entwurf des Workflows, keine Expo-Installation, kein TestFlight-Login, keine App gebaut oder eingereicht.