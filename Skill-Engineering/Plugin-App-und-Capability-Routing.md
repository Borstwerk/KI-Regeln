# Plugin-, App- und Capability-Routing

## Inhalt

- Grundidee
- Begriffe
- Routing-Reihenfolge
- Read / Write / Action
- Verfügbarkeit ist keine Autorisierung
- Plugin Directory als Discovery-Layer
- Plugin-Vorschläge statt manueller Umwege
- Fallbacks
- Security und Governance
- Portabilität
- Leitgedanke

## Grundidee

Externe Apps und Plugins erweitern die Fähigkeiten einer Laufzeit. Sie ersetzen aber weder fachliche Skilllogik noch Autorisierung.

Ein Agent soll nicht reflexartig einen manuellen Export-/Copy-Paste-Umweg verlangen, wenn eine geeignete native Capability oder eine verfügbare Plugin-/App-Verbindung denselben Schritt kontrolliert übernehmen kann.

Bevorzugtes Routing:

~~~text
Nutzerproblem
→ fachlichen Skill / Workflow bestimmen
→ benötigte Capability bestimmen
→ native Capability vorhanden?
   ├─ ja → nutzen
   └─ nein
        ↓
      bereits verbundenes / installiertes Plugin oder App vorhanden?
        ├─ ja → Rechte + Scope prüfen → nutzen
        └─ nein
             ↓
           Plugin Directory prüfen, wenn externe Integration materiell helfen würde
             ├─ geeignete Option → Verbindung/Installation transparent anbieten
             └─ keine geeignete Option → Fallback
~~~

Damit bleibt der **fachliche Job** zentral. Plugin- oder App-Namen sind Runtime-/Capability-Details.

## Begriffe

### Plugin

Ein Plugin ist eine paketierte Workflow-Erweiterung. Es kann Skills, Apps und weitere Plugin-Komponenten bündeln.

### App

Eine App verbindet ChatGPT beziehungsweise die aktuelle Laufzeit mit externen Daten oder Aktionen, zum Beispiel einem Mail-, Datei-, Design-, CRM- oder Projektmanagementdienst.

Ein Plugin kann eine oder mehrere Apps enthalten. Installation und App-Verbindung sind getrennte Zustände.

### Native Capability

Eine Fähigkeit, die die aktuelle Laufzeit bereits ohne externe Plugin-/App-Verbindung bereitstellt.

Beispiele können je nach Host sein:

- Webrecherche;
- Dateiarbeit;
- Bildgenerierung;
- Codeausführung;
- geplante Tasks;
- Browser-/Computerzugriff.

Die konkrete Liste ist runtimeabhängig.

## Routing-Reihenfolge

### 1. Fachliche Aufgabe zuerst

Nicht:

~~~text
Canva vorhanden
→ Canva-Skill aktivieren
→ Aufgabe suchen
~~~

Sondern:

~~~text
Nutzer braucht ein gebrandetes Social-Visual
→ fachlicher Bild-/Designworkflow
→ benötigte externe Capability?
→ falls Canva passend und verfügbar: Canva als Runtime nutzen
~~~

### 2. Native Capability prüfen

Wenn die Laufzeit die Aufgabe bereits direkt und ausreichend ausführen kann, keine unnötige externe Integration erzwingen.

### 3. Verbundene/Installierte Option prüfen

Wenn eine passende App oder ein Plugin bereits verbunden ist, darf sie/es genutzt werden, sofern:

- der Nutzerauftrag dazu passt;
- die nötigen Rechte vorhanden sind;
- der konkrete Read-/Write-/Action-Scope vom Auftrag gedeckt ist;
- vorhandene Human Gates erhalten bleiben.

### 4. Plugin Directory prüfen

Wenn die Aufgabe von einem externen Dienst, Account oder Datenbestand materiell profitieren würde und keine passende Verbindung vorhanden ist, den Plugin-/App-Katalog als Discovery-Layer prüfen.

Beispiele:

- Design → Canva, Figma, Adobe, Miro oder ähnliche;
- Mail/Kalender → Gmail, Outlook, Google Calendar oder ähnliche;
- Projektarbeit → Asana, Atlassian, Linear, Trello oder ähnliche;
- Entwicklung → GitHub, Context7, Railway, Render oder ähnliche;
- CRM/Marketing → HubSpot, Attio, Semrush, Metricool oder ähnliche;
- Reisen → Booking.com, Tripadvisor, Skyscanner oder ähnliche.

Die Beispiele sind **nicht vollständig und nicht garantiert verfügbar**. Sichtbarkeit hängt unter anderem von Plan, Workspace, Rolle, Region, Plattform und Pluginstatus ab.

## Read / Write / Action

Plugins und Apps unterscheiden sich nicht nur nach Fachgebiet, sondern nach Wirkung.

### READ

Nur Informationen lesen oder analysieren.

Beispiele:

- Dateien suchen;
- E-Mails lesen;
- Analytics abrufen;
- Projektstatus zusammenfassen.

### WRITE

Persistente externe Daten verändern.

Beispiele:

- Dokument aktualisieren;
- Task anlegen;
- CRM-Datensatz ändern;
- Design bearbeiten.

### ACTION

Extern sichtbare oder geschäftlich wirksame Aktion auslösen.

Beispiele:

- Nachricht senden;
- Meeting buchen;
- Veröffentlichung starten;
- Deployment triggern;
- Payment Link erzeugen.

Die Klassen sind keine universelle technische Taxonomie. Sie dienen als lokales Risikomodell.

## Verfügbarkeit ist keine Autorisierung

Wichtige Invariante:

~~~text
Plugin verfügbar
≠
Plugin verbunden

Plugin verbunden
≠
jede Aktion autorisiert

Capability vorhanden
≠
Write / Action erlaubt
~~~

Installation oder Plugin-Auswahl darf Anbieter-, Account- oder Workspace-Berechtigungen nicht umgehen.

Riskante, irreversible oder extern sichtbare Aktionen behalten ihre vorhandenen Human Gates.

## Plugin Directory als Discovery-Layer

Das Plugin Directory ist dynamisch und accountabhängig. Deshalb führt KI-Regeln **keine vollständige statische Pluginliste als Source of Truth**.

Stattdessen:

- einige Beispiele dokumentieren;
- Plugin Directory als aktuelle Discoveryquelle behandeln;
- neue relevante Capability-Klassen im Radar beobachten;
- konkrete Plugins erst dann als eigene Upstreams registrieren, wenn lokale Regeln tatsächlich von ihnen abhängen.

~~~text
Plugin im Directory
→ Discovery

Plugin beeinflusst konkrete lokale Regel
→ deliberate review
→ ggf. upstream-sources.yml
~~~

## Plugin-Vorschläge statt manueller Umwege

Wenn ein Nutzer eine externe Aufgabe oder Datenquelle nennt und eine passende Integration materiell helfen kann, ist folgender Ablauf bevorzugt:

~~~text
passende Integration suchen
→ vorhandene Verbindung nutzen
oder
→ Installation/Verbindung anbieten
→ unabhängige Teile der Aufgabe trotzdem weiterbearbeiten
~~~

Nicht zuerst nach Copy-Paste, CSV-Export, Screenshots oder manueller Übertragung fragen, wenn eine geeignete Verbindung verfügbar und sinnvoll ist.

Ausnahmen:

- Nutzer möchte bewusst ohne Plugin/App arbeiten;
- Datenschutz-/Security-/Compliance-Gründe sprechen dagegen;
- Plugin ist für den konkreten Account nicht verfügbar;
- die Verbindung bringt keinen relevanten Vorteil;
- benötigte Aktion liegt außerhalb des freigegebenen Scopes.

## Fallbacks

Kein Plugin/App verfügbar:

- Import/Export nur als transparenter Fallback;
- lokale Datei statt Cloudquelle;
- Patch statt direktem Write;
- Entwurf statt Veröffentlichung;
- manuelle Übergabe statt vorgetäuschter Integration.

Der Fallback muss die fachliche Disziplin erhalten und den Capability-Verlust sichtbar machen.

## Security und Governance

Vor sensibler Plugin-/App-Nutzung prüfen:

- welche Daten gelesen werden;
- welche externen Writes möglich sind;
- ob Secrets oder personenbezogene Daten beteiligt sind;
- ob die Verbindung vertrauenswürdig und für den Zweck angemessen ist;
- ob Plugin/App laut Workspace/Account überhaupt zulässig ist.

Ein Verifizierungsbadge oder ein bekannter Anbieter ersetzt keine organisationsspezifische Datenschutz-, Sicherheits- oder Vendorprüfung.

## Portabilität

Fachliche Skills sollen keine konkrete App als universelle Wahrheit voraussetzen.

Bevorzugt:

~~~text
Capability: collaborative-design-write
~~~

Runtime-Adapter:

~~~text
Canva / Figma / Miro / andere passende App
~~~

Nur wenn eine konkrete Plattform selbst Gegenstand der Aufgabe ist, gehört ihr Name in den fachlichen Kern.

## Leitgedanke

> Erst die Aufgabe verstehen, dann die benötigte Capability wählen, danach die beste verfügbare Runtime – und Autorisierung niemals aus Verfügbarkeit ableiten.
