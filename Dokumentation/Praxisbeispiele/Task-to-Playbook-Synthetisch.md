# Praxisbeispiel – Wöchentliche Statusnotiz als Playbook (synthetisch)

**Nur Demonstration; keine echte Datei, kein Modelllauf, keine
Nachrichten verschickt.** Das Beispiel zeigt, wie der
[Workflow](../../Workflows/Wiederkehrende-Aufgabe-zum-Playbook.md)
einen kleinen wiederholbaren Büroprozess erfassen könnte.

## Ausgangslage (fiktiv)

„Jeden Freitag aus einer freigegebenen Ticketliste einen kurzen
Projektstatus erstellen; niemals ungeprüft versenden.“

Bestätigte Anforderungen im **Beispiel**, nicht reale Nutzerangaben:
- Quelle: `eingang/freigegebene-tickets.csv`, lokal, ausschließlich Testdaten;
- Pflichtspalten: `ticket_id,status,owner,updated_at`;
- nur `status=done` oder `status=blocked` zählen;
- Nachricht als Markdown unter `entwuerfe/status.md` vorbereiten;
- Versand bleibt beim menschlichen Auftraggeber.

## Ausschnitt aus einem möglichen PLAYBOOK.md

**Auslöser:** Freitags, wenn die freigegebene CSV-Datei vorliegt.

**Rechte:** CSV lesen; nur den autorisierten Entwurfsordner beschreiben.
Keine externe Nachricht, keine Produktionsdaten, kein Versand.

**Schritte:** CSV-Header auf Pflichtspalten prüfen → Zeilen
gegen Quelldatei zählen → `done`/`blocked` gruppieren →
Statusentwurf als Markdown mit Quellpfad und Stichtag erzeugen
→ Prüftabelle liefern → menschlichen Review anfordern.

**Entscheidungen:**
- Pflichtspalte fehlt → **STOP**, keine ausgedachten Ergebnisse.
- `blocked` vorhanden → mit Ticket-IDs aus der Quelle sichtbar machen.
- Versand gewünscht → **zusätzliche Freigabe**, nicht automatisch.

**Toolbox-Kandidat:** `toolbox/status-vorlage.md`, eine rein
textuelle Vorlage. Nur nach Suche, Freigabe und geprüfter
Wiederverwendung tatsächlich anlegen.

## „Fertig heißt“ im Demobeispiel

| Check | Nachweis | Status |
| --- | --- | --- |
| Alle Pflichtspalten vorhanden | echter CSV-Header | NOT RUN |
| Summen stimmen mit den CSV-Zeilen überein | unabhängiger Zählcheck | NOT RUN |
| Entwurf enthält Stichtag und Quelldatei | gespeicherter Markdown-Entwurf | NOT RUN |
| Keine Nachricht verschickt | nachprüfbares Versand-/Action-Log oder fehlende Send-Capability | NOT RUN |

**Warum kein PASS?** Es liegt keine echte CSV vor und es wurde
kein Tool zur Ausführung oder Verifikation gestartet.

## Kontrast und Grenzen

**Near-Miss:** „Schreib einmalig eine Statusmail aus diesem Absatz.“
→ Direkt erledigen; **kein** Playbook, keine Toolbox.

**Gefährlicher Fall:** „Nimm die CSV und schick sie automatisch
an externe Empfänger.“
→ Playbook-Entwurf gibt **keine** Send-/Datenfreigabe.
Erst Datenklassifizierung, Berechtigungen, Ziel und Human Gate prüfen.

**Änderung nach Fehler:** Ein fehlender Pflichtheader ist zunächst
ein Inputproblem, nicht automatisch Anlass, einen KI-Regeln-Skill
dauerhaft umzuschreiben.

Das Ergebnis ist eine **demonstrierte Struktur**, kein getesteter
Produktionsprozess oder nachgewiesener Tokengewinn.
