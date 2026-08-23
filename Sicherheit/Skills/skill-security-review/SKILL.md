---
name: skill-security-review
description: Prüft einen Agent-Skill auf Supply-Chain-, Berechtigungs-, Prompt-Injection-, Datenexfiltrations-, Script-, External-Action- und Update-Risiken. Verwenden vor Freigabe mächtiger oder externer Skills und bei Upstream-Änderungen; nicht als allgemeiner fachlicher Skillreview ohne Sicherheitsbezug.
---

# Skill Security Review

## Inputs

Mindestens:

- zu prüfender Skill;
- ggf. Scripts, References und Assets;
- bekannte Tool-/Capability-Rechte;
- bei externem Skill Herkunft und Upstreamstand.

## Ablauf

1. **Provenance prüfen**
   - Herkunft, Lizenz, mutable Upstreams, lokaler Forkstatus.

2. **Capabilities inventarisieren**
   - Lesen, Schreiben, Ausführen, Netzwerk, externe Wirkung.

3. **Least Privilege prüfen**
   - jede mächtige Capability gegen tatsächlichen Skillzweck halten.

4. **Untrusted Inputs prüfen**
   - Web, Dateien, E-Mail, Issues, Tooloutput;
   - Prompt-Injection-Grenzen vorhanden?

5. **Datenfluss prüfen**
   - welche sensiblen Daten können gelesen werden?
   - wohin können sie gelangen?
   - Logs/Outputs/Telemetry berücksichtigen.

6. **Scripts und externe Abhängigkeiten prüfen**
   - Dateiwirkung, Prozesse, Netzwerk, Downloads, dynamische Ausführung.

7. **Außenwirkung prüfen**
   - Sends, Publishes, Deploys, Deletes, Production Writes;
   - Human Gates vorhanden?

8. **Update-Risiko prüfen**
   - mutable Upstream registriert?
   - könnten Updates Rechte oder Verhalten erweitern?

## Ausgabe

Für jeden Fund:

- Severity: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`;
- betroffene Stelle;
- Risiko;
- Evidence;
- empfohlene Abhilfe.

Danach Gesamturteil:

- `security-pass`;
- `security-pass-with-followups`;
- `security-fail`.

## Harte Regeln

- Keine automatische Freigabe aufgrund bekannter Herkunft.
- Keine Rechte als sicher annehmen, nur weil sie im Skill selbst so beschrieben werden.
- Keine Secrets in Reviewausgabe wiederholen.
- Bei schweren offenen Funden keine `stable`-Empfehlung.
