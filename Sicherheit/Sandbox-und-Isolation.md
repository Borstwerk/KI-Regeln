# Sandbox und Isolation

## Grundsatz

> Wo Fehler oder kompromittierte Instruktionen Schaden verursachen können, soll der mögliche Schadensradius technisch begrenzt werden.

## Isolationsebenen

Je nach Aufgabe können sinnvoll sein:

- separater Arbeitsbaum / Branch;
- temporäres Verzeichnis;
- Container / Sandbox;
- Testumgebung statt Produktion;
- eingeschränktes Dateisystem;
- eingeschränkter Netzwerkzugriff;
- getrennte Credentials;
- isolierte Parallel-Agent-Workspaces.

## Wann stärkere Isolation nötig ist

Insbesondere bei:

- unbekannten Dritt-Scripts;
- Codeausführung aus untrusted Quellen;
- Paketinstallation;
- Dateikonvertierung mit komplexen Parsern;
- Browser-/Webautomation mit Downloads;
- destruktiven Datenoperationen;
- parallelen Agenten mit Schreibzugriff.

## Isolation ist kein Ersatz für Review

Sandboxing reduziert Schaden, macht eine Aktion aber nicht automatisch fachlich oder sicher korrekt.

Auch isolierte Änderungen benötigen normale Verifikation und Freigabe.

## Parallele Agenten

Wenn mehrere Agenten unabhängig schreiben:

- getrennte veränderliche Workspaces;
- klare Ownership von Dateien oder Tasks;
- kontrollierte Zusammenführung;
- Konflikte und gegenseitige Überschreibungen sichtbar machen.

## Produktion

Produktionszugriff soll nicht Standard-Fallback sein, wenn lokale oder Testumgebungen fehlen.

Fehlende sichere Testmöglichkeit kann ein legitimer Blocker sein.

## Cleanup

Temporäre:

- Credentials;
- Debugartefakte;
- Testdaten;
- heruntergeladene untrusted Dateien;
- Instrumentierung

nach Abschluss entsprechend Projektregeln entfernen oder sicher archivieren.

## Leitgedanke

> Isolation macht Fehler kleiner. Sie macht sie nicht richtig.
