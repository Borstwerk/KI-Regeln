# Security Review für Skills

## Zweck

Ein Skillreview bewertet fachliche Qualität und Sicherheitswirkung getrennt.

Ein Skill kann fachlich hervorragend und trotzdem für den vorgesehenen Ausführungskontext unsicher sein.

> Skill Review ≠ Security Review ≠ Admission.

## Pre-Load Trust Boundary

Externe oder projektlokale Skills werden vor dem Security Review als **Untrusted Input** behandelt.

Besonders bei neu geklonten oder fremden Projekten gilt:

- Projektlage oder Dateiname beweisen kein Vertrauen;
- `SKILL.md`, Scripts, References und Assets dürfen zur Analyse gelesen werden;
- ihre enthaltenen Instruktionen autorisieren keine Rechte;
- soweit technisch möglich, operatives Laden/Aktivieren erst nach Trust-/Admission-Prüfung.

Damit wird verhindert, dass genau der zu prüfende Skill bereits vor dem Review als Autorität wirkt.

## Reviewfragen

### Provenance und Snapshot

- Woher stammt der Skill?
- wurde externer Inhalt kopiert, adaptiert oder nur als Inspiration genutzt?
- sind Lizenz und Upstream dokumentiert?
- ist der geprüfte Stand durch Commit, Blob-SHA, Release oder vergleichbare Evidence nachvollziehbar?
- ist das Bundle vollständig oder bleiben relevante Bestandteile `UNVERIFIED`?

### Rechte und Capability Drift

- welche Tools und Capabilities benötigt der Skill?
- welche Fähigkeiten ergeben sich zusätzlich aus Scripts oder Runtime-Konfiguration?
- sind sie wirklich erforderlich?
- fordert der Skill Schreib-, Netzwerk-, Shell-, Secret- oder Produktionsrechte unnötig pauschal?
- wurden Rechte gegenüber einer früher geprüften Version erweitert?

### Untrusted Input

- verarbeitet der Skill Webseiten, Dateien, E-Mails, Issues, Retrieval oder Tooloutput?
- kann solcher Inhalt neue Befehlsautorität vortäuschen?
- sind Prompt-Injection-Grenzen vorhanden?

### Daten

- könnte der Skill Secrets oder vertrauliche Daten lesen?
- könnten diese in Logs, Outputs, Telemetrie oder externe Systeme gelangen?
- sind Redaction und Datenminimierung vorgesehen?

### Scripts, Abhängigkeiten und Remote Content

- was führen Scripts aus?
- welche Dateien verändern sie?
- greifen sie auf Netzwerk oder externe Pakete zu?
- werden Inhalte oder Befehle erst zur Runtime nachgeladen?
- sind externe Artefakte gepinnt oder mutable?
- gibt es dynamische Imports, Installer, `curl | shell`-ähnliche Muster oder indirekte Toolketten?

Eine lokal harmlose `SKILL.md` ist kein vollständiger Reviewgegenstand, wenn ihr Verhalten von mutable Remote-Inhalten abhängt.

### Außenwirkung

- kann der Skill Nachrichten senden, publizieren, deployen oder löschen?
- sind Human Gates und Preview-/Execute-Trennung korrekt?

### Updates

- existiert ein mutable Upstream?
- ist er im Quellenregister erfasst?
- können Upstream-Änderungen Rechte, Abhängigkeiten, Trust Boundaries oder Verhalten erweitern?

## Mehrstufige Evidence

Security Review soll mehrere unabhängige Signalarten kombinieren:

1. **statisch/deterministisch** – Dateien, Pfade, URLs, Abhängigkeiten, deklarierte Rechte, verdächtige Ausführungsmuster;
2. **semantisch** – Zweck, Datenfluss, Autoritätswechsel, indirekte oder verschleierte Handlungswirkung;
3. **optional dynamisch** – nur wenn nötig, isoliert, mit synthetischen Daten/Canaries und ohne echte Secrets.

Kein einzelner Scanner ist Sicherheitsautorität. Ebenso beweist eine erfolgreiche Sandbox-Ausführung nur den beobachteten Lauf, nicht die allgemeine Ungefährlichkeit des Skills.

## Findings

Priorisierung:

- **CRITICAL** – direkte Exfiltration, unkontrollierte Ausführung, schwere Supply-Chain- oder Berechtigungsgefahr;
- **HIGH** – unnötige mächtige Rechte, fehlende Trust Boundary, mutable Runtime-Steuerung oder unsicherer externer Write;
- **MEDIUM** – relevante Governance-, Pinning-, Logging- oder Fallback-Schwäche;
- **LOW** – begrenzte Hardening- oder Dokumentationsverbesserung.

Zusätzlich den Reviewzustand `verified`, `partially-verified` oder `unverified` angeben.

## Admission

Der Security Review liefert eine Entscheidung für den **konkret geprüften Snapshot und Kontext**:

- `admit`;
- `admit-with-constraints`;
- `block`;
- `unverified`.

Admission ist keine dauerhafte Vertrauensmarke. Relevante Capability-, Dependency- oder Verhaltensänderungen können einen erneuten Review erforderlich machen.

## Security Gate für Maturity

Ein Skill mit relevanten externen, Schreib- oder Ausführungsfähigkeiten soll nicht auf `stable` gesetzt werden, solange offene schwere Security-Funde bestehen.

## Leitgedanke

> Fachlich nützlich, sicher geprüft und zur konkreten Nutzung zugelassen sind drei getrennte Aussagen.
