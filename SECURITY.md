# Security Policy

## Scope

Als Security-Themen dieses Repositories gelten insbesondere:

- echte Secrets, Zugangsdaten oder vertrauliche Daten im Repository oder seiner erreichbaren History;
- unsichere GitHub-Actions-/Supply-Chain-Konfiguration;
- Regeln oder Skills, die gefährliche Tool-, Berechtigungs- oder Prompt-Injection-Grenzen systematisch aushebeln;
- Schwachstellen in repository-eigenen Audit-/Validator-Tools, wenn daraus ein relevantes Sicherheitsrisiko entsteht.

Reine fachliche Meinungsverschiedenheiten oder normale Qualitätsbugs sind keine Security-Meldungen.

## Melden

Veröffentliche keine echten Secrets und keine unnötigen sensiblen Exploitdetails in öffentlichen Issues, Pull Requests oder Diskussionen.

Für den aktuellen privaten Projektstand ist **noch kein belastbar dokumentierter privater Security-Meldekanal festgelegt**. Vor einer Umstellung auf ein öffentliches Repository muss deshalb entweder GitHubs Private Vulnerability Reporting aktiviert oder ein anderer privater Meldekanal ausdrücklich festgelegt und hier dokumentiert werden.

Bis dieses Gate geschlossen ist, ist die Public-Release-Readiness im Bereich Security Reporting nur teilweise erfüllt.

## Umgang mit Secrets

Wird ein mögliches Secret gefunden:

1. Wert nicht in Issues, Commitmessages, Changelogs oder Reports wiederholen;
2. betroffenen Credential-/Token-Typ und Fundpfad sicher erfassen;
3. Credential bei realem Risiko rotieren bzw. widerrufen;
4. Current Tree und Git-History getrennt behandeln;
5. erst nach Remediation die Veröffentlichung neu bewerten.

Ein sauberer aktueller Tree beweist keine saubere History.
