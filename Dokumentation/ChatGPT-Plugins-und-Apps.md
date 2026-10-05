# ChatGPT Plugins und Apps

Stand: 2026-10-05

## Worum geht es?

ChatGPT kann über Plugins und Apps mit externen Werkzeugen, Daten und Aktionen verbunden werden.

OpenAI unterscheidet aktuell:

- **Plugins** bündeln wiederverwendbare Workflow-Funktionen und können Skills, Apps oder weitere Komponenten enthalten;
- **Apps** sind die konkrete Verbindung zu externen Diensten und Daten;
- die Installation eines Plugins kann eine App-Verbindung anstoßen, ersetzt aber keine erforderliche Konto- oder Workspace-Autorisierung.

Seit 2026 ist das Plugin Directory die zentrale Discovery-Oberfläche für solche Erweiterungen in ChatGPT und Codex.

## Warum das für KI-Regeln wichtig ist

Ein guter Workflow soll nicht unnötig manuell werden, nur weil eine externe Capability noch nicht verbunden ist.

Beispiel:

~~~text
Nutzer: "Mach aus diesem Briefing eine Canva-Präsentation."

schlecht:
→ "Kopiere den Text nach Canva."

besser:
→ prüfen, ob Canva bereits verbunden ist
→ falls ja: direkt verwenden
→ falls nein und hilfreich: Verbindung anbieten
→ sonst Fallback
~~~

Die Verbindung ändert aber nicht die fachlichen Regeln für Inhalt, Design, Rechte, Review oder Veröffentlichung.

## Aktuell beobachtete Plugin-Klassen

Die folgenden Beispiele wurden am 2026-10-05 im verfügbaren Plugin-Verzeichnis beobachtet. Sie sind **nicht vollständig** und können je nach Plan, Workspace, Rolle, Region und Plattform abweichen.

| Bereich | Beispiele |
| --- | --- |
| Design & Kreativ | Canva, Adobe, Adobe Express, Figma, Miro, Gamma, tldraw, MagicPath, HeyGen, Runway |
| Dokumente & Wissen | Google Drive, Notion, Dropbox, Box, GitBook, Readwise |
| Mail & Kalender | Gmail, Outlook Email, Google Calendar, Outlook Calendar, Calendly |
| Kommunikation & Meetings | Slack, Teams, Zoom, RingCentral, Fathom, Otter.ai, Fireflies |
| Projektmanagement | Asana, Atlassian, Linear, Trello, monday.com, ClickUp, Coda, Smartsheet |
| Entwicklung & Hosting | GitHub, Context7, Railway, Render, DigitalOcean, Replit, Lovable, Webflow, Vercel |
| Daten & Analytics | Databricks Genie, BigQuery, Mixpanel, PostHog, Amplitude, Supermetrics, Airtable |
| Marketing | Semrush, Metricool, Klaviyo, HYPD, ChatGPT Ads Manager |
| CRM & Sales | HubSpot, Attio, Salesforce, Close, Apollo.io, Zoho CRM, ZoomInfo |
| Business & Payments | Stripe, Shopify, Mercury, NetSuite |
| Recht & Compliance | Docusign, Vanta, Legal Data Hunter |
| Reisen | Booking.com, Tripadvisor, Skyscanner |
| Lernen & Research | Udemy, Scite, Hugging Face |

Nicht jeder Eintrag ist auf jedem Account installierbar. Einzelne Plugins können durch Adminregeln oder Plan-/Regionsgrenzen fehlen.

## Canva als Beispiel

Canva kann aktuell unter anderem für folgende Workflows genutzt werden:

- Präsentationen und Dokumente aus Briefings;
- Social Posts, Poster und Flyer;
- Bildgenerierung und Bildbearbeitung;
- Hintergrundentfernung;
- Resize für verschiedene Social-Formate;
- Designanpassungen;
- Brand-Kit-Prüfung;
- Feedback auf bestehende Designs.

Einige Funktionen können ein verbundenes Canva-Konto, bestimmte Canva-Pläne oder Canva-AI-Credits benötigen.

## Was KI-Regeln daraus ableitet

Bevor ein Nutzer Inhalte manuell zwischen Diensten kopieren, Dateien exportieren oder einen externen Arbeitsschritt selbst durchführen soll:

1. benötigte fachliche Capability bestimmen;
2. native Capability prüfen;
3. bereits verbundene/installierte Plugins und Apps prüfen;
4. falls sinnvoll, Plugin Directory nach einer passenden Integration durchsuchen;
5. erst danach manuellen Fallback wählen.

## Rechteklassen

Für die Praxis hilft diese grobe Einteilung:

| Klasse | Beispiel |
| --- | --- |
| READ | Datei lesen, E-Mail suchen, Analytics abrufen |
| WRITE | Dokument bearbeiten, Task anlegen, CRM-Feld ändern |
| ACTION | Nachricht senden, Meeting buchen, Deployment oder Veröffentlichung auslösen |

Wichtig:

> Verfügbarkeit ist keine Autorisierung.

Ein verbundenes Plugin darf nicht automatisch jede externe Änderung oder Aktion ausführen.

## Plugins sind keine Skills

Ein KI-Regeln-Skill beschreibt **wie** eine Aufgabe fachlich sauber erledigt wird.

Ein Plugin oder eine App beschreibt eher **womit** die Laufzeit Daten oder externe Systeme erreichen kann.

~~~text
Skill
→ fachliche Arbeitsweise

Plugin / App
→ Capability / Integration

Runtime
→ konkrete Ausführung
~~~

## Plugin Directory statt statischer Vollständigkeitsliste

Das Verzeichnis verändert sich laufend.

Deshalb führt KI-Regeln keine behauptet vollständige Pluginliste.

Stattdessen wird das offizielle Plugin Directory im wöchentlichen Radar beobachtet.

Interessant sind besonders:

- neue Capability-Klassen;
- neue Plugins, die bisher manuelle Fallbacks ersetzen;
- neue Write-/Action-Capabilities;
- neue Integrationen mit relevanten Security-/Privacy-Folgen.

## Offizielle Quellen

- OpenAI Help Center: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- OpenAI Help Center: https://help.openai.com/en/articles/11487775-apps-in-chatgpt
- Plugin Directory / Übersicht: https://openai.com/business/plugins/

Die offiziellen Produktseiten sind lebende Dokumentation. Lokale Aussagen bleiben deshalb an den jeweils geprüften Stand gebunden.

## Leitgedanke

> Plugins machen den Agenten handlungsfähiger. Sie machen externe Aktionen nicht automatisch erlaubt.
