# Geführter KI-Regeln-Einstieg – Offline-Prototyp

Der [HTML-Demonstrator](Gefuehrter-Workflow-Einstieg.html) zeigt, wie vorhandene
KI-Regeln-Workflows für **Menschen ohne Skill-Katalogwissen** in wenige
verständliche Schritte übersetzt werden können. Orientierung anhand von
[Seb AI – App-Workflow](https://seb-ai.pages.dev/app/), **kein**
übernommener Quellcode, Text, Formular oder Webhook.

**Öffnen:** Repository lokal herunterladen/klonen und
`Dokumentation/Demos/Gefuehrter-Workflow-Einstieg.html` im Browser öffnen.
Der Demonstrator benötigt weder Server noch Installation, Netzwerk, API-Key
oder Google-/Claude-Konto. Die Markdown-Quellenlinks lassen sich im
lokalen Repository auflösen; ob ein Browser Markdown direkt gut darstellt,
ist geräteabhängig (alternativ im Editor öffnen).

## Gezeigte Aufgaben

- Smartphone-App: [Mobile-App bis Store-Freigabe](../../Workflows/Mobile-App-bis-Store-Freigabe.md).
- Website: [Website-Neuentwicklung](../../Workflows/Website-Neuentwicklung.md).
- Recherche: [Deep Research](../../Workflows/Deep-Research.md).

Die Schritttexte sind **human-facing Beispiele**, kein zweites
verbindliches Skill-Routing. Autoritativ bleiben `AGENTS.md`,
`skill-catalog.yml` und die jeweils verlinkten Workflows.
Die Prompt-Vorlagen sind zu prüfende Startaufträge und werden nicht
automatisch ausgeführt. Der „Erledigt“-Haken markiert nur eine
**Benutzeraktion**, keinen getesteten/verifizierten Arbeitserfolg.

## Privacy / Security

- Kein Formular, keine Kontaktdatensammlung, keine Webhooks, keine Analytics.
- Keine Drittbibliotheken, externen Assets, Fetches, Service Worker,
  Browser-Speicherung oder automatischen Prozesse.
- Eingaben bestehen nur aus einer lokalen Workflow-Auswahl und
  temporären Checkbox-States im offenen Tab.
- Copy-Buttons verwenden nur nach Benutzerinteraktion die
  Clipboard-API. Wenn diese nicht verfügbar ist, kann der Prompt
  direkt markiert werden.
- Store-Publikation, externe Kommunikation, Schlüssel, Installationen
  und kostenpflichtige Aktionen bleiben ausdrücklich gated.

## Nicht getestet / nicht behauptet

Noch kein echter Einsteigertest, keine Screenreader-Studie, kein
vollständiger Accessibility-Audit, kein Cross-Browser-Test und
keine Live-Veröffentlichung. Statische Offline-Checks in
`tests/test_guided_workflow_demo.py` sind kein visueller Browser-PASS.

## Architekturentscheidung

**Keine neue allgemeine Skill-Discovery-Engine.** Der Demonstrator
ist bewusst nur ein dünnes UI vor bestehenden Workflows.
Falls ein künftiger Ausbau geplant wird, müssen Inhalte aus
kanonischen Quellen abgeleitet oder maschinell auf Drift geprüft
werden. Ein UI-Demonstrator ist **kein** Ersatz für AGENTS.md.
