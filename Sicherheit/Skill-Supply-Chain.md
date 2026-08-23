# Skill Supply Chain

## Grundsatz

Ein externer Skill ist ausführbarer bzw. handlungsleitender Drittinhalt und deshalb Teil der Supply Chain.

> Herkunft, Stand, Rechte und Änderungen eines Skills müssen prüfbar sein.

## Vor Aufnahme eines externen Skills

Prüfen:

- Quelle und Maintainer;
- Repository-/Dateipfad;
- Lizenz;
- relevante Tool- und Netzwerkrechte;
- eingebettete Scripts oder Assets;
- externe Links und Nachladepfade;
- Prompt-Injection-/Exfiltrationsrisiken;
- ob der Skill lokal kopiert, adaptiert oder nur als Inspiration genutzt wird.

## Pinning und Provenance

Mutable Quellen möglichst mit nachvollziehbarem Stand erfassen:

- Blob-SHA;
- Release-/Versionsnummer;
- Datum der Prüfung;
- lokale Auswirkungen.

Dafür dient `Dokumentation/upstream-sources.yml`.

## Updates

```text
Upstream geändert
→ Diff / semantische Änderung prüfen
→ Security-Auswirkung prüfen
→ fachliche Auswirkung prüfen
→ übernehmen / beobachten / verwerfen
```

Kein automatischer Sync nur wegen einer neuen Upstream-Version.

## Scripts und Assets

Ein Skill mit Script ist nicht nur Text.

Vor Ausführung prüfen:

- welche Dateien gelesen/geschrieben werden;
- welche Prozesse gestartet werden;
- ob Netzwerkzugriff erfolgt;
- ob Secrets gelesen werden könnten;
- ob Pfade außerhalb des erwarteten Scopes betroffen sind.

## Update Drift

Auch ein ursprünglich guter Skill kann durch spätere Änderungen:

- mehr Rechte verlangen;
- neue externe Abhängigkeiten hinzufügen;
- Verhalten verändern;
- unsichere Defaults einführen.

Deshalb ist Upstream-Monitoring Teil der Sicherheitskontrolle.

## Lokale Forks

Wenn ein lokaler Skill bewusst vom Upstream abweicht:

- Abweichung dokumentieren;
- Upstream trotzdem als Quelle beobachten, wenn relevant;
- Änderungen nicht blind mergen.

## Entfernung

Ein kompromittierter oder nicht mehr vertrauenswürdiger Upstream bedeutet nicht automatisch, dass jede lokal abstrahierte Regel falsch ist. Aber Provenance, Securityannahmen und weitere Nutzung müssen neu bewertet werden.

## Leitgedanke

> Ein Skill wird nicht dadurch vertrauenswürdig, dass er Markdown ist.
