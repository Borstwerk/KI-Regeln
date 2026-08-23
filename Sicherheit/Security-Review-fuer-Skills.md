# Security Review für Skills

## Zweck

Ein Skillreview bewertet nicht nur fachliche Qualität, sondern bei relevanten Capabilities auch die Sicherheitswirkung des Skills.

## Reviewfragen

### Provenance

- Woher stammt der Skill?
- wurde externer Inhalt kopiert, adaptiert oder nur als Inspiration genutzt?
- sind Lizenz und Upstream dokumentiert?
- ist der geprüfte Stand nachvollziehbar?

### Rechte

- welche Tools und Capabilities benötigt der Skill?
- sind sie wirklich erforderlich?
- fordert der Skill Schreib-, Netzwerk- oder Ausführungsrechte unnötig pauschal?

### Untrusted Input

- verarbeitet der Skill Webseiten, Dateien, E-Mails, Issues oder Tooloutput?
- kann solcher Inhalt neue Befehlsautorität vortäuschen?
- sind Prompt-Injection-Grenzen vorhanden?

### Daten

- könnte der Skill Secrets oder vertrauliche Daten lesen?
- könnten diese in Logs, Outputs oder externe Systeme gelangen?
- sind Redaction und Datenminimierung vorgesehen?

### Scripts / externe Abhängigkeiten

- was führen Scripts aus?
- welche Dateien verändern sie?
- greifen sie auf Netzwerk oder externe Pakete zu?
- sind Downloads oder dynamische Ausführung nötig?

### Außenwirkung

- kann der Skill Nachrichten senden, publizieren, deployen oder löschen?
- sind Human Gates und Preview-/Execute-Trennung korrekt?

### Updates

- existiert ein mutable Upstream?
- ist er im Quellenregister erfasst?
- können Upstream-Änderungen Rechte oder Verhalten erweitern?

## Findings

Priorisierung:

- **CRITICAL** – direkte Exfiltration, unkontrollierte Ausführung, schwere Supply-Chain- oder Berechtigungsgefahr;
- **HIGH** – unnötige mächtige Rechte, fehlende Trust Boundary, unsicherer externer Write;
- **MEDIUM** – relevante Governance-/Logging-/Fallback-Schwäche;
- **LOW** – begrenzte Hardening- oder Dokumentationsverbesserung.

## Security Gate für Maturity

Ein Skill mit relevanten externen, Schreib- oder Ausführungsfähigkeiten soll nicht auf `stable` gesetzt werden, solange offene schwere Security-Funde bestehen.

## Leitgedanke

> Fachlich nützlich und sicher ausführbar sind zwei getrennte Freigabeachsen.
