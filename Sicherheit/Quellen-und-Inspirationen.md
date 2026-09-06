# Quellen und Inspirationen – Sicherheit

## OWASP Agentic Skills Top 10

Quelle:

https://owasp.org/www-project-agentic-skills-top-10/

Relevante Risikofelder der aktuellen 2026er Arbeit umfassen unter anderem:

- malicious skills;
- Supply-Chain-Kompromittierung;
- over-privileged skills;
- unsichere Metadaten;
- untrusted external instructions;
- schwache Isolation;
- Update Drift;
- unzureichendes Scanning;
- fehlende Governance;
- Cross-Platform-Reuse.

Für dieses Repository besonders relevant sind Provenance, Least Privilege, Content Pinning, Update-Monitoring und Skill-Inventarisierung.

Die OWASP-Arbeit wird als Sicherheitsrahmen genutzt, nicht als automatische Vorgabe jeder technischen Einzelmaßnahme.

## OWASP Top 10 for Agentic Applications 2026

Quelle:

https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

Einordnung:

Breiterer Sicherheitsrahmen für agentische Anwendungen. Bestätigt, dass Agentensicherheit nicht nur Modelloutput, sondern Toolnutzung, autonome Aktionen, Identitäten, Berechtigungen und Workflow-Governance umfasst.

## OpenAI – sichere agentische Ausführung

Quelle:

https://openai.com/index/running-codex-safely/

Relevante Konzepte:

- Sandbox- und Approval-Grenzen;
- begrenzte Netzwerk- und Dateirechte;
- riskante Aktionen nicht allein durch Agentenintention autorisieren.

## OpenAI – Deep Research System Card

Quelle:

https://openai.com/index/deep-research-system-card/

Relevanter Aspekt:

Webinhalte können bösartige oder irreführende Instruktionen enthalten. Daraus wird die allgemeine Trust-Boundary-Regel abgeleitet, externe Inhalte als Daten statt als neue Autorität zu behandeln.

## OpenTelemetry GenAI Observability

Quelle:

https://opentelemetry.io/blog/2026/genai-observability/

Einordnung:

Die aktuellen GenAI Semantic Conventions zeigen, dass Modellaufrufe, Toolcalls, Tokenmetriken und optional auch Inhaltsdaten strukturiert beobachtbar gemacht werden können. Für dieses Repository ist besonders die Trennung zwischen nützlicher Telemetrie und optionaler, potenziell sensibler Inhaltsaufzeichnung relevant.

## guillaumemeyer/watermarks-remover

Quelle:

https://github.com/guillaumemeyer/watermarks-remover

Geprüfter Repository-Stand:

`d9e9590d94e19b39eb2794266292324bfec8249a`

Lizenz am geprüften Stand: MIT.

Methodisch relevant sind insbesondere:

- Inspect-first statt blindem Entfernen;
- Trennung von Unicode-Artefakten, C2PA/Content Credentials, EXIF/XMP, Dokumentmetadaten und anderen Markerklassen;
- Capability Detection: nur behaupten, was das vorhandene Tool tatsächlich prüfen kann;
- Before/After-Evidence und Re-Inspection;
- Confidence-, False-Positive- und Residual-Risk-Denken;
- klare Trennung zwischen verifizierbaren technischen Entfernungen und best-effort Aussagen.

Bewusst **nicht** als lokale Produktlogik übernommen werden:

- Detector-Evasion oder „human score“-Optimierung;
- statistische Rewrite-Rezepte zur Schwächung von Text-Watermarks;
- Watermark-Stealing oder Secret-Key-Rekonstruktion;
- destructive Pixel-/Audio-/Video-Purification als allgemeine Standardfähigkeit;
- Entfernen verpflichtender Provenienz-, Attribution- oder Disclosure-Signale;
- die Annahme, fehlende oder entfernte Marker bewiesen menschliche Urheberschaft;
- die konkrete Claude-Plugin-, HTTP-Service-, Docker-, Modell- oder Backend-Architektur des Upstreams.

Der Upstream dient als methodischer Referenzraum. KI-Regeln übernimmt weder dessen Runtime noch dessen Skilltext oder automatische Synchronisation.

## Eigene Synthese

Der Sicherheitsbereich verbindet diese Quellen mit den bereits vorhandenen Regeln zu Human Gates, Context Engineering, Upstream-Monitoring und Agenten-Observability.

Leitmodell:

```text
untrusted Input
+ Capability
+ Berechtigung
+ Isolation
+ Gate
+ Evidence
+ nachvollziehbarer Upstream
```

Für Inhaltsprovenienz kommt hinzu:

```text
inspect
→ Evidence klassifizieren
→ Erhaltungspflichten
→ optional begrenztes Change Set
→ re-inspect
→ Residual Risk
```

## Leitgedanke

> Agentensicherheit entsteht nicht aus einem einzigen Filter, sondern aus mehreren unabhängigen Grenzen.
