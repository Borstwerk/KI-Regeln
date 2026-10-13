# Claude und Instagram – Connector-/Skill-Audit (12.10.2026)

## Ausgangsfrage

Es wurde von einem Claude-Instagram-Skill berichtet, der sich mit Instagram **verbindet**. „Skill“ ist dabei nicht gleichbedeutend mit API-/Accountzugriff.

Drei klar unterschiedliche Jobs:

1. **Content offline erstellen** (Hooks, Reels, Captions, Redaktionsplan);
2. **Instagram-Daten lesen** (eigene Professional-Account-Medien, Insights, Kommentare oder persönliche gespeicherte Beiträge, je nach Zugriffsmethode);
3. **Aktionen ausführen** (posten, planen, DMs lesen oder beantworten, Kommentare schreiben).

Diese Jobs nie unbemerkt mischen. Ein Content-Skill mit lesbaren `SKILL.md`-Dateien ist nicht automatisch ein Instagram-Connector. Ein MCP-Connector ist wiederum keine fachliche Social-Media-Methodik.

## Status, Priorität und Hinweis für spätere KI-Agenten

**DISCOVERY-ONLY / NOT ADMITTED.** Der Nutzer möchte diese Quellen für eine spätere Nutzung **vormerken**, aber derzeit weder einen kostenpflichtigen Dienst auswählen noch ein Instagram-Konto verbinden oder etwas veröffentlichen.

**Priorität 1 – Instagram-Publishing mit Claude:** Reels, Bilder, Karussells und Beiträge aus bereits freigegebenen Entwürfen veröffentlichen oder terminieren. Ein späterer Agent soll zuerst die offiziellen Meta-Publishing-Möglichkeiten und danach geeignete MCP-/Provider-Adapter prüfen. Veröffentlichung bleibt immer eine gesondert autorisierte externe **ACTION**; Planen oder Entwerfen erteilt keine Erlaubnis zum Post.

**Priorität 2 – optional HypeRadar-READ:** Instagram als mögliche zusätzliche Discovery- oder Performance-Quelle evaluieren. Zunächst nur zulässige Lese-Capabilities, Datenabdeckung und API-Rechte prüfen; aus einer Publishing-Verbindung folgt **kein** Leserecht für beliebige Reels, private gespeicherte Inhalte oder DMs. Keine HypeRadar-Automatisierung in diesem Audit.

### Agenten-Discovery-Regel für spätere Aufträge

Wenn ein Auftrag künftig **Instagram-Publishing, Instagram-MCP oder HypeRadar-Instagram-Recherche** betrifft:

1. Dieses Dokument und die verlinkten Primärquellen **neu lesen**; frühere Preis-, Feature-, Scope- und ToS-Angaben nicht als aktuelle Tatsache übernehmen.
2. Auftrag unterscheiden: offline Content erstellen, Instagram-Inhalte/Insights lesen, Draft speichern, terminieren oder **öffentlich veröffentlichen**.
3. Native und bereits freigegebene Integrationen vor Drittanbieter-MCP prüfen; **Kontotyp, Meta-App/API-Permissions, Providerkosten, Rate-/Postlimits, Datenflüsse, Media-Hosting und Support** aktuell überprüfen.
4. Anbieter-/Skill-Admission nach `Sicherheit/MCP-und-externe-Tools.md` und gegebenenfalls `skill-security-review`; READ/WRITE/ACTION und Least-Privilege gesondert behandeln.
5. **Keine Installation, Kontoanmeldung, Tokenanforderung, Abbuchung, Terminierung oder Veröffentlichung** allein wegen dieses Fundes. Zuerst Nutzerzustimmung zum konkreten Anschluss beziehungsweise zur Ausgabe und bei Veröffentlichungen ein eindeutiges Human Approval einholen.
6. Bei fehlender Eignung der APIs oder notwendigem Drittanbieterabonnement den **Kosten-/Privacy-/Wartungs-Trade-off** transparent machen. Dass ein Nutzer mögliche Kosten akzeptiert, ersetzt keinen aktuellen Planentscheid.

**Statuswerte:** Quellen bekannt; Connectors nicht freigegeben; Toolinstallationen und Authentisierung nicht durchgeführt; keine Behavioral- oder Live-Publishing-Evidence.

## Offizielle Quellen und potenzielle Provider (erneut prüfen vor Umsetzung)

**Meta / Plattform-Primärquellen**

- [Meta – Instagram API mit Instagram Login (offizielle Postman-Collection)](https://www.postman.com/meta/instagram/folder/1z5vxzu/instagram-api-with-instagram-login): Professional-Accounts (Business/Creator), Berechtigungen wie `instagram_business_content_publish`. Der dokumentierte Instagram-Login-Pfad ist nicht mit dem Facebook-Login-Pfad gleichzusetzen.
- [Meta – Instagram API mit Facebook Login (offizielle Postman-Collection)](https://www.postman.com/meta/instagram/folder/u4g5a2a/instagram-api-with-facebook-login): Professional-Account und verknüpfte Facebook-Seite sowie andere Permissions (u. a. `instagram_content_publish`).
- [Meta – offizielle Instagram API / Reels-Publishing-Beispiele](https://www.postman.com/meta/instagram/collection/6yqw8pt/instagram-api): Container-Erzeugung, Statusprüfung und eigentlicher Publish-Aufruf sind unterschiedliche Schritte. Aktuelle Format-, Rechte-, App-Review- und Media-Hosting-Voraussetzungen vor Umsetzung prüfen.

**Mögliche Integrationsanbieter – unverbindliche Kandidaten**

- [PostZen – Instagram MCP](https://www.postzen.dev/mcp/instagram): nach Anbieterangaben remote MCP für Claude und Instagram-Publishing, Scheduling sowie Analytics; OAuth-/API-Key-/Profil-Scope im tatsächlichen Angebot prüfen.
- [PostZen – Preise](https://www.postzen.dev/pricing) und [PostZen – Billing-Dokumentation](https://docs.postzen.dev/billing): beim Audit 12.10.2026 bewirbt der Anbieter einen Free-Tier (bis 20 Plattform-Posts/Monat, zwei Accounts) und kostenpflichtige Tarife ab 19 USD/Monat. **Momentaufnahme eines Anbieters, keine verlässliche Kostenzusage.** Posts auf mehreren Zielkonten, Zusatzaccounts und Drittplattform-Gebühren gesondert prüfen.
- [PostZen – Instagram Agent Skill](https://github.com/postzen-dev/instagram-agent-skill): Beispiel einer Verbindung aus Agent-Skills und externem Publishing-MCP; Paket-/Permission-Audit steht aus.
- [William-Gao/instagram-mcp](https://github.com/William-Gao/instagram-mcp): alternativer MCP-Adapter zur Instagram-API; Wartung, Auth, erlaubte Aktionen und Release-Sicherheit vor Einsatz neu verifizieren.

**Bewertung:** Offizielle Meta-Pfade sind die erste Capability-/Berechtigungsreferenz. PostZen und Open-Source-Adapter sind **unbewertete Anbieteroptionen**, keine Empfehlung zum Kauf, Installieren oder Verbinden. Anbieter-Marketing ist nicht gleich unabhängig bestätigte Funktion oder Sicherheit.

## Geprüfte Kandidaten

| Projekt | Geprüfter Head | Lizenzmetadatum | Eigentliche Capability | Vorläufige Entscheidung |
|---|---|---|---|---|
| [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) | `d03c56bb598b` | MIT | 13 Skills für Reel-/Caption-/Profil-/Planung; **keine echte Kontoverbindung oder automatische Veröffentlichung** | Methoden-Audit gegen vorhandene Social-Media-Skills; kein pauschaler Import |
| [vrajdesai78/instagram-skill](https://github.com/vrajdesai78/instagram-skill) | `85259f9b626c` | Apache-2.0 | authentifizierter Chrome-Tab + Claude-in-Chrome-MCP; private Instagram-Web-API für u. a. DMs, gespeicherte Reels, Posts | **High-Risk, keine Admission** ohne gesondertes Browser-/Session-/Privacy-Review |
| [William-Gao/instagram-mcp](https://github.com/William-Gao/instagram-mcp) | `d8e1adf7ae1c` | MIT | Instagram API mit Instagram Login; Lese- und Schreibfähigkeiten einschließlich Publishing | potentieller API-Adapter, zunächst READ-only Scoping/Meta-App-/Tokenprüfung, WRITE gesondert |
| [demaAlramhe/instagram-claude-mcp](https://github.com/demaAlramhe/instagram-claude-mcp) | `93e1e9c02201` | nicht verifiziert | deklarativ READ-only Graph-API-Connector für Profile, Insights, Medien und Kommentare | geringerer funktionaler Scope; Auth-/Transport-/Secrets-Audit trotzdem erforderlich |
| [postzen-dev/instagram-agent-skill](https://github.com/postzen-dev/instagram-agent-skill) | `b38be357f1a7` | MIT | Content-Skills mit Drittanbieter-MCP für Veröffentlichung, DMs, Kommentare und Insights | stärkerer Berechtigungs-/Drittanbieter-Datenfluss, keine automatische Installation/Admission |

Die SHA-Werte referenzieren zum Auditzeitpunkt beobachtete Default-Branch-Stände und sind keine Releasefreigabe. Lizenzmetadaten belegen nicht die Lizenzen oder Sicherheit aller Abhängigkeiten.

## Architekturschluss für KI-Regeln

Bestehende Bereiche nutzen:

- Contentplanung und Hooks → `Social-Media-und-Content-Praesenz/` bzw. passende vorhandene Kreativ-/Kommunikations-Skills;
- MCP-/Plugin-Admission → `Sicherheit/MCP-und-externe-Tools.md`, Permission Review, Source Review;
- Capability/Output/Fehler/Retry → `Skill-Engineering/Agent-Tool-Vertraege.md`;
- Account-Actions → READ/WRITE/ACTION und Human Gates;
- source-/evidence-basierte Claims über Views/Reach → vorhandene Quellen-/Claimprüfung.

**Kein neuer Instagram-Skill** allein deshalb, weil eine Verbindung technisch möglich ist. Ein späterer benannter Skill braucht einen eigenständigen Job und Tests gegen vorhandene Social-Media-Owner.

## Wichtige Risikotrennung

### Browser-/private API-Skill

Ein im Chrome-Tab angemeldetes Instagram-Konto enthält eine aktive Sitzung. Das Ausführen von JavaScript in diesem Kontext und die Nutzung privater Webendpunkte kann Cookies/CSRF-bezogenen Zugriff und nicht dokumentierte Datenflüsse einschließen; möglich sind Instabilität, Kontorisiken sowie breite Lesezugriffe bis zu persönlichen DMs. Auch wenn ein Anbieter „keine Passwörter gespeichert“ schreibt, ist das **kein Beweis**, dass eine authentifizierte Browseraktion risikoarm ist.

Vor möglichem Test: Source-/Dependency-Audit, konkrete Endpunkte, Browserzugriffsrechte, Drittanbietertransfers, Least Privilege, personenbezogene Daten und Nutzungsbedingungen. Keine Installation/Session-Kopplung in diesem Audit.

### Offizielle Instagram API / Professional Account

Für die hier betrachteten Meta-API-Projekte werden in der Regel Instagram Business-/Creator-Konten, eine Meta-App, passende Berechtigungen/Tokens und gegebenenfalls App Review benötigt. Der verfügbare API-Scope bestimmt, welche Daten tatsächlich erreichbar sind. **Eigene gespeicherte private Reels und beliebige DMs sind nicht automatisch über dieselbe API zugänglich.**

Tokens nur über autorisierte Flows bereitstellen, nicht ins Repository/Prompt kopieren; Server muss selbst authentisiert, HTTPS-gesichert und korrekt beschränkt sein. Bei einem Projekt, das Zugangsdaten direkt auf einer Drittanbieter-Seite anfordert, keine automatische Sicherheitsgleichwertigkeit mit Meta-OAuth behaupten.

### Aktionen

```text
READ Profil/Insights
≠ WRITE Caption/Entwurf in lokalen Dateien
≠ ACTION veröffentlichen / kommentieren / DMs senden
```

Post/Send/Delete erfordern konkrete Konto-/Content-/Zielauswahl, Preview, ausdrückliche Freigabe und Receipt/Evidence. Toolverfügbarkeit ist keine Publishing-Autorisierung.

## Auswahl nach Nutzerziel

- **Nur Reelideen, Texte und Planung?** Methoden ohne Instagram-Login und ohne Accountrechte vorziehen.
- **Einzelnes öffentliches Reel verstehen?** Vom Nutzer bereitgestellte Screenshots/Transkript oder zulässige öffentliche Quellen; keine Browser-Session für eine einfache Textauswertung erzwingen.
- **Gespeicherte/private Inhalte, eigene DMs?** Persönliche Sitzung betroffen; erst High-Risk-Review, nicht API-Zugang versprechen.
- **Eigenen Professional-Account auswerten?** möglicher offizieller READ-only API-Pfad; zuerst genaue Berechtigungen klären.
- **Automatisch veröffentlichen?** gesonderter WRITE-/ACTION-Prozess mit Human Approval und Idempotenz.

## Test- und Reviewplan – nicht durchgeführt

1. Zweck und Accounttyp erfragen, maximal benötigte Rechte definieren.
2. Anbieterentscheidung **unabhängig** von Marketingclaims anhand Code und Endpunkten.
3. Paket-/Dependency-/Transport-/Credential-Audit, konkrete Revision pinnen.
4. Isolierter Test ohne Hauptkonto und zunächst nur READ, mit erlaubten bekannten Beispieldaten.
5. Tool-Outputs und negative Rechtefälle prüfen (WRITE/DMS ausdrücklich blockiert).
6. Erst bei bewiesener Notwendigkeit separat Write-/Action-Gates planen.

Status: **DISCOVERY / NOT INSTALLED / NOT AUTHENTICATED / NOT BEHAVIORALLY TESTED.**

## Leitgedanke

> Der wertvollste Instagram-Skill hängt vom Auftrag ab. Der Zugriff auf ein Konto muss getrennt von der Qualität eines Content-Skills bewertet werden.
