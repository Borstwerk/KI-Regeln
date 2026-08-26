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

Für den aktuellen privaten Projektstand ist **noch kein belastbar dokumentierter privater Security-Meldekanal festgelegt**. GitHub Private Vulnerability Reporting ist für öffentliche Repositories vorgesehen und wird deshalb nicht als im privaten Vorbereitungszustand bereits aktivierbares Pflicht-Setting behandelt.

Verbindlicher Phase-4-Release-Schritt: Nach dem Visibility-Wechsel Private Vulnerability Reporting aktivieren, praktisch prüfen, dass ein privater Reportweg funktioniert, und anschließend diese `SECURITY.md`-Anleitung bestätigen beziehungsweise ergänzen. Falls vor dem Visibility-Wechsel ein anderer autorisierter privater Meldekanal festgelegt und dokumentiert wird, kann das Gate entsprechend früher geschlossen werden.

Bis ein privater Meldeweg tatsächlich eingerichtet und verifiziert ist, bleibt die Public-Release-Readiness im Bereich Security Reporting blockiert.

## Umgang mit Secrets

Wird ein mögliches Secret gefunden:

1. Wert nicht in Issues, Commitmessages, Changelogs oder Reports wiederholen;
2. betroffenen Credential-/Token-Typ und Fundpfad sicher erfassen;
3. Credential bei realem Risiko rotieren bzw. widerrufen;
4. Current Tree und Git-History getrennt behandeln;
5. erst nach Remediation die Veröffentlichung neu bewerten.

Ein sauberer aktueller Tree beweist keine saubere History.
