# Quellen und Inspirationen – Testing und QA

Stand: 2026-08-23

Dieser Bereich wurde aus mehreren unabhängigen Quellen synthetisiert. Externe Skills dienen als Radar und Praxismuster; fachliche Regeln werden soweit möglich gegen Primärdokumentation, etablierte Testing-Literatur oder Standards gegengeprüft.

Es wurden keine fremden Skilltexte übernommen. Die lokalen Regeln sind eigenständig formuliert und bewusst frameworkneutral abstrahiert.

## Mutable Agent-Skill-Upstreams

### Anthropic – `testing-strategy`

Repository: `anthropics/knowledge-work-plugins`  
Pfad: `engineering/skills/testing-strategy/SKILL.md`  
Beobachteter Blob-SHA: `4ff59410c8fe67872a98ca97135815b778ca1219`

Relevant für:

- Teststrategie als eigene Disziplin;
- Unit / Integration / Contract / E2E als unterschiedliche Ebenen;
- Fokus auf kritische Pfade, Error Handling und Datenintegrität.

Nicht übernommen wurde eine starre Testpyramide als universelle Mengenregel.

### Anthropic – `webapp-testing`

Repository: `anthropics/skills`  
Pfad: `skills/webapp-testing/SKILL.md`  
Beobachteter Blob-SHA: `4726215301db64a0cc4d41fc3219c61f37a30f4a`

Relevant als konkretes Beispiel dafür, dass Browser-/E2E-Ausführung andere Capabilities und Evidence benötigt als reine Teststrategie.

### Currents – `playwright-best-practices`

Repository: `currents-dev/playwright-best-practices-skill`  
Pfad: `playwright-best-practices/SKILL.md`  
Beobachteter Blob-SHA: `0da736253c343081ab8c0cb9802729a707c23196`  
Beobachtete Version: `1.2`

Relevant für:

- getrennte Testing-Aktivitäten;
- Flakiness und Isolation;
- Testdaten;
- Error-/Failure-States;
- Mock-vs-real-Entscheidungen;
- CI- und Diagnose-Evidence.

Die Playwright-spezifische Regel „eigene APIs nie mocken, Third Parties immer mocken“ wurde bewusst **nicht** universell übernommen. Lokal gilt stattdessen die risikobasierte Seam-/Dependency-Regel.

### obra/superpowers – `verification-before-completion`

Repository: `obra/superpowers`  
Pfad: `skills/verification-before-completion/SKILL.md`  
Beobachteter Blob-SHA: `7d45333cc4a49c57a80df6c1fe2fa777a207afbc`

Relevant für:

- frische Evidence vor Completion Claims;
- vollständigen relevanten Nachweis statt extrapolierter Teilprüfung;
- unabhängige Verifikation von Agenten-Erfolgsmeldungen.

Kein eigener lokaler Skill: das Prinzip wird in `Agentenarbeit/Skills/verification-loop` und in den Testing-Regeln integriert.

## Lebende Primär- und Fachdokumentation

### ISTQB – CTFL 4.0

https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/

Relevant für:

- Testing-Grundbegriffe;
- Test Levels / Test Types;
- Test Analysis und Design;
- Risk Management;
- Test Monitoring, Control und Completion;
- Quality Reporting.

Lokale Abstraktion: Testing liefert Qualitäts- und Risikoevidence; eine Releaseentscheidung bleibt beim gültigen lokalen Gate.

### Playwright – Best Practices / Auto-Waiting

https://playwright.dev/docs/best-practices  
https://playwright.dev/docs/actionability

Relevant für:

- nutzersichtbares Verhalten;
- Testisolation;
- resiliente Locators;
- beobachtbare Synchronisation statt willkürlicher Sleeps.

### Pact – Contract Testing

https://docs.pact.io/

Relevant für:

- Consumer-/Provider-Verträge;
- Contract Testing als eigene Grenze;
- Abgrenzung von vollständigen Functional Tests.

### Testcontainers

https://testcontainers.com/getting-started/

Relevant für:

- reale, kurzlebige Testdependencies;
- isolierte Integrationstests;
- bekannte Startzustände statt gemeinsam genutzter Infrastruktur;
- Grenzen von In-Memory-/Fake-Ersatzsystemen.

### Hypothesis

https://hypothesis.readthedocs.io/

Relevant für Property-based Testing als Testdesign-Technik.

### Stryker Mutator

https://stryker-mutator.io/

Relevant für Mutation Testing und die Trennung von Coverage und tatsächlicher Fehlersensitivität.

### Testing Library

https://testing-library.com/docs/

Relevant für das Prinzip, Tests möglichst an realer Nutzung und beobachtbarem Verhalten auszurichten.

## Stabile / etablierte Referenzen

### Martin Fowler – Practical Test Pyramid

https://martinfowler.com/articles/practical-test-pyramid.html

Relevant für unterschiedliche Testgranularitäten, Test Doubles und das Verhältnis von Feedbackgeschwindigkeit und Integrationsbreite.

### Martin Fowler – Mocks Aren't Stubs / Test Double

https://martinfowler.com/articles/mocksArentStubs.html  
https://martinfowler.com/bliki/TestDouble.html

Relevant für:

- Test-Double-Begriffe;
- State vs. Behavior Verification;
- klassische vs. mock-orientierte Testing-Stile;
- keine universelle Mocking-Doktrin.

### Google Testing Blog

https://testing.googleblog.com/

Relevant insbesondere für:

- Flakiness;
- Hermetik;
- E2E-Kosten und -Grenzen;
- deterministische Tests;
- Testdiagnose.

Die einzelnen Artikel sind überwiegend datierte Referenzen und werden nicht wie mutable Skill-Dependencies synchronisiert.

### Principles of Chaos Engineering

https://principlesofchaos.org/

Relevant **zur Abgrenzung**, nicht zur Aufnahme in den Testing-Scope:

Chaos Engineering arbeitet mit Steady-State-Hypothesen, kontrollierten systemischen Störungen und Blast Radius. Diese Disziplin wird später `Reliability/` zugeordnet.

## Lokale Synthese

Aus den Quellen wurde insbesondere folgende Struktur abgeleitet:

```text
Risiko
→ Teststrategie
→ Testebene
→ Testdesign
→ Seams / Daten / Isolation
→ Ausführung
→ Evidence
→ Restunsicherheit
→ lokales Freigabe-Gate
```

Dabei gilt weiterhin:

> Quelle ist Inspiration oder Evidence – keine automatische lokale Regel.