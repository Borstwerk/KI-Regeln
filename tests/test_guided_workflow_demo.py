"""Static structural/contract checks for human-facing guided demo.

No browser, no agent and no external network: these assertions cannot
demonstrate rendered UI quality, clipboard behavior or actual accessibility.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "Dokumentation/Demos/Gefuehrter-Workflow-Einstieg.html"
WORKFLOW = ROOT / "Workflows/Mobile-App-bis-Store-Freigabe.md"


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.links = []
        self.ids = set()
        self.inlines = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "script" and "src" not in a:
            self.inlines += 1
        if tag in ("script", "img", "iframe", "link") and a.get("src", a.get("href", "")).startswith(("https://", "http://", "//")):
            raise AssertionError(f"remote asset: {tag}")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


class GuidedDemoContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML.read_text(encoding="utf-8")
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.parser = Scan()
        cls.parser.feed(cls.html)
        cls.parser.close()

    def test_offline_no_lead_form_network_or_persistence(self):
        self.assertNotIn("form", self.parser.tags)
        self.assertNotIn("iframe", self.parser.tags)
        self.assertEqual(self.parser.inlines, 1)
        self.assertNotIn("<script src=", self.html)
        for pattern in (r"\bfetch\s*\(", r"XMLHttpRequest", r"\blocalStorage\s*\.", r"\bsessionStorage\s*\.",
                        r"\bsendBeacon\s*\(", r"\bWebSocket\s*\(", r"\beval\s*\(", r"\bnew Function\s*\("):
            self.assertNotRegex(self.html, pattern)
        self.assertIn('copy.addEventListener("click"', self.html)

    def test_guided_accessible_structure_exists(self):
        self.assertIn('lang="de"', self.html)
        self.assertIn("prefers-reduced-motion", self.html)
        self.assertIn("focus-visible", self.html)
        self.assertIn("Zum Guide springen", self.html)
        for id_ in ("guide", "goal", "steps", "sources", "progressLabel", "progress"):
            self.assertIn(id_, self.parser.ids)
        self.assertIn("aria-label", self.html)
        self.assertIn('box.type="checkbox"', self.html)

    def test_three_explicit_tasks_have_prompts_and_links(self):
        for key in ("mobile:", "website:", "research:"):
            self.assertIn(key, self.html)
        self.assertIn("Prompt kopieren", self.html)
        self.assertIn("NOT_RUN", self.html)

    def test_workflow_exists_in_index_and_demo(self):
        self.assertIn("Workflows/Mobile-App-bis-Store-Freigabe.md",
                      (ROOT / "workflow-index.yml").read_text(encoding="utf-8"))
        self.assertIn("Mobile-App-bis-Store-Freigabe.md", self.html)
        self.assertIn("Human", self.html)
        self.assertIn("Store-Freigabe", self.workflow)

    def test_referenced_workflow_and_skill_paths_exist(self):
        # Static, committed relative links: no runtime fetch or remote dependency.
        urls = re.findall(r'"(\.\./\.\./[^"]+\.md)"', self.html)
        self.assertGreaterEqual(len(urls), 9)
        for url in urls:
            self.assertTrue((HTML.parent / url).resolve().is_file(), url)

    def test_human_gate_cannot_be_replaced_by_checkbox(self):
        self.assertIn("kein technischer PASS", self.html)
        self.assertIn("keine Außenaktion ohne meine ausdrückliche Freigabe", self.html)
        self.assertIn("Build erfolgreich ≠ eingereicht ≠ freigegeben ≠ veröffentlicht", self.workflow)
        self.assertIn("Android und iOS", self.workflow)
        self.assertIn("NOT_RUN", self.workflow)

    def test_demo_is_not_registered_as_agent_skill(self):
        catalog = (ROOT / "skill-catalog.yml").read_text(encoding="utf-8")
        self.assertNotIn("gefuehrter-workflow-einstieg", catalog)
        self.assertNotIn("mobile-app-bis-store-freigabe", catalog)


if __name__ == "__main__":
    unittest.main()
