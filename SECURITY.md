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

**Das Repository ist öffentlich (verifiziert am 29.10.2026).** Ob GitHub **Private Vulnerability Reporting** tatsächlich aktiviert ist, konnte anhand der derzeit verfügbaren GitHub-Berechtigungen **nicht verifiziert** werden. Das Fehlen einer Bestätigung ist weder ein Nachweis, dass die Funktion deaktiviert ist, noch ein Beleg, dass sie aktiv ist.

- Falls GitHub bei [Repository-Sicherheitsmeldungen](https://github.com/Borstwerk/KI-Regeln/security/advisories) **„Report a vulnerability“** anbietet, nutze diesen GitHub-internen privaten Meldeweg.
- Falls dieser private Meldeweg **nicht** verfügbar ist, übermittle dort und in öffentlichen Issues/PRs **keine Schwachstellendetails oder Secrets**. Ein öffentliches Issue darf allenfalls **ohne technische Details** nach einem vertraulichen Kontaktweg fragen. Es ist aktuell kein anderer verifizierter privater Sicherheitskontakt dokumentiert.
- Die Maintainer müssen den realen Meldeweg separat bestätigen und diese Anleitung erst **nach erfolgreicher Prüfung** als vollständig markieren. Bis dahin bleibt das dokumentierte Security-Reporting-Gate offen.

## Maintainer-Check für Private Vulnerability Reporting

1. Mit berechtigtem GitHub-Konto: **Settings → Security and quality → Advanced Security → Private vulnerability reporting** prüfen; falls noch aus, aktivieren. [GitHub-Anleitung](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
2. Anschließend aus Sicht eines externen Meldeberechtigten kontrollieren, ob **„Report a vulnerability“** tatsächlich erreichbar ist. Keine echten Secrets und keinen künstlichen öffentlichen Exploitbericht für die Prüfung verwenden.
3. Verifizierten Status, Datum und eine geeignete **nicht-sensitive** Evidence in `Dokumentation/open-source-readiness.yml` dokumentieren. Erst dann `security_reporting` und den verbleibenden Audit-Gate-Status aktualisieren.

Die GitHub-Sichtbarkeit `public` ist **nicht** gleichbedeutend mit einer abgenommenen Security-Reporting-Konfiguration.

## Umgang mit Secrets

Wird ein mögliches Secret gefunden:

1. Wert nicht in Issues, Commitmessages, Changelogs oder Reports wiederholen;
2. betroffenen Credential-/Token-Typ und Fundpfad sicher erfassen;
3. Credential bei realem Risiko rotieren bzw. widerrufen;
4. Current Tree und Git-History getrennt behandeln;
5. erst nach Remediation die Veröffentlichung neu bewerten.

Ein sauberer aktueller Tree beweist keine saubere History.
