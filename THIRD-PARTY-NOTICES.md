# Third-Party Notices and Provenance Status

KI-Regeln enthält lokal entwickelte Regeln und Skills, die teilweise durch externe öffentliche Quellen und Agent-Skills beeinflusst wurden. Die maschinenlesbare Zuordnung der tatsächlich einflussreichen GitHub-Artefakte steht in `Dokumentation/upstream-sources.yml`; Lizenz- und Nutzungsklassifikation steht in `Dokumentation/upstream-provenance.yml`.

**Wichtig:** Ein Eintrag als Upstream bedeutet nicht automatisch, dass Quelltext oder Skilltext kopiert wurde. `reference/inspiration`, `adapted` und `copied/vendored` werden ausdrücklich unterschieden. Ein unbekannter Lizenzstatus wird nicht als Erlaubnis zur Weiterverteilung interpretiert.

## Matt Pocock – skills

Mehrere Engineering-Praktiken in diesem Repository wurden teilweise durch `mattpocock/skills` inspiriert, insbesondere Debugging, Code Review und Domain Modeling. Die aktuelle lokale Nutzungsklasse ist `reference/inspiration`.

Source: https://github.com/mattpocock/skills

License: MIT

License source: https://github.com/mattpocock/skills/blob/main/LICENSE

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Noch nicht abschließend lizenzgeklärte GitHub-Upstreams

Alle weiteren in `Dokumentation/upstream-sources.yml` als `kind: github-file` geführten Quellen bleiben bis zur belastbaren Prüfung des Lizenzstands am beobachteten Commit/Blob konservativ `redistribution_status: unresolved`, sofern `Dokumentation/upstream-provenance.yml` keinen engeren Eintrag enthält. Diese Quellen dürfen nicht allein aufgrund ihrer öffentlichen Erreichbarkeit als redistributable behandelt werden.
