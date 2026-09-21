# Skill Supply Chain

## Grundsatz

Ein externer Skill ist ausführbarer bzw. handlungsleitender Drittinhalt und deshalb Teil der Supply Chain.

> Herkunft, Stand, Rechte, nachgeladene Abhängigkeiten und Änderungen eines Skills müssen prüfbar sein.

## Vor dem Laden: Trust Boundary

Ein Skill sollte nicht bereits dadurch Autorität erhalten, dass er in einem Projektverzeichnis liegt.

Bei neu geklonten, fremden oder anderweitig untrusted Projekten:

```text
Skill entdecken
→ read-only inventarisieren
→ Herkunft + Snapshot + Bundle prüfen
→ Security-/Trust-Review
→ Admission
→ erst danach operativ aktivieren, soweit die Laufzeit diese Trennung unterstützt
```

Wenn die Laufzeit keinen Pre-Load-Gate besitzt, muss diese Einschränkung explizit als Plattformrisiko behandelt werden.

## Vor Aufnahme eines externen Skills

Prüfen:

- Quelle und Maintainer;
- Repository-/Dateipfad und konkreter Snapshot;
- Lizenz;
- relevante Tool-, Shell-, Netzwerk- und Secret-Rechte;
- eingebettete Scripts, References oder Assets;
- externe Links, Paketquellen und Nachladepfade;
- Prompt-Injection-/Exfiltrationsrisiken;
- ob Verhalten von mutable Remote-Inhalten abhängt;
- ob der Skill lokal kopiert, adaptiert oder nur als Inspiration genutzt wird.

## Pinning und Provenance

Mutable Quellen möglichst mit nachvollziehbarem Stand erfassen:

- Blob-SHA;
- Repository-Commit oder Release-/Versionsnummer;
- Datum der Prüfung;
- lokale Auswirkungen.

Dafür dient `Dokumentation/upstream-sources.yml`.

Ein gepinnter lokaler Text pinnt **nicht automatisch** alle externen Inhalte, die er zur Runtime nachlädt.

## Remote und transitive Abhängigkeiten

Besonders kritisch prüfen:

- ungepinnte Pakete oder Installer;
- dynamische Imports;
- Remote-Scripts;
- `curl | shell`-ähnliche Installations- oder Ausführungsketten;
- Remote-Instruktionsdateien;
- Tool-/MCP-Server oder andere Komponenten, deren Verhalten außerhalb des geprüften Bundles liegt.

Mutable Remote-Inhalte erweitern den Trust Scope des Skills und müssen als solche dokumentiert werden.

## Mehrstufige Prüfung

Kein einzelner Scan deckt die gesamte Supply Chain ab.

Sinnvolle Kombination:

```text
statische / deterministische Prüfung
+ semantische Verhaltensprüfung
+ bei Bedarf isolierte dynamische Probe
+ menschliches Admission-Gate
```

Dabei gilt:

- Scanner = Evidence, nicht Freigabe;
- Sandbox = Schadensbegrenzung, nicht Sicherheitsbeweis;
- dynamische Tests mit synthetischen Daten/Canaries statt echten Secrets;
- unbekannte Bestandteile bleiben `UNVERIFIED`.

## Updates

```text
Upstream geändert
→ Snapshot / Diff bestimmen
→ Capability- und Dependency-Delta prüfen
→ Security-Auswirkung prüfen
→ fachliche Auswirkung prüfen
→ übernehmen / beobachten / verwerfen
```

Kein automatischer Sync nur wegen einer neuen Upstream-Version.

Eine frühere Freigabe gilt nicht pauschal für spätere Versionen, wenn sich Rechte, Runtime-Abhängigkeiten oder Verhalten geändert haben.

## Scripts und Assets

Ein Skill mit Script ist nicht nur Text.

Vor Ausführung prüfen:

- welche Dateien gelesen/geschrieben werden;
- welche Prozesse gestartet werden;
- ob Netzwerkzugriff erfolgt;
- ob Secrets gelesen werden könnten;
- ob Pfade außerhalb des erwarteten Scopes betroffen sind;
- ob Verhalten erst durch externe Inhalte bestimmt wird.

## Update Drift

Auch ein ursprünglich guter Skill kann durch spätere Änderungen:

- mehr Rechte verlangen;
- neue externe Abhängigkeiten hinzufügen;
- Verhalten verändern;
- unsichere Defaults einführen;
- statisch harmlos bleiben, aber Runtime-Inhalte austauschen.

Deshalb ist Upstream-Monitoring Teil der Sicherheitskontrolle.

## Lokale Forks

Wenn ein lokaler Skill bewusst vom Upstream abweicht:

- Abweichung dokumentieren;
- Upstream trotzdem als Quelle beobachten, wenn relevant;
- Änderungen nicht blind mergen.

## Entfernung

Ein kompromittierter oder nicht mehr vertrauenswürdiger Upstream bedeutet nicht automatisch, dass jede lokal abstrahierte Regel falsch ist. Aber Provenance, Securityannahmen und weitere Nutzung müssen neu bewertet werden.

## Leitgedanke

> Ein Skill wird nicht dadurch vertrauenswürdig, dass er Markdown ist – und ein grüner Scanner macht ihn nicht automatisch sicher.
