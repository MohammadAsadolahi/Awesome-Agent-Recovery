"""Regression tests for publication-only resource curation."""
import csv
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parents[1]
COLUMNS = ["id", "kind", "area", "title", "year", "date", "url", "why", "code", "note"]


class PublicationCurationTests(unittest.TestCase):
    def make_catalog(self, *, kind="paper", url="https://arxiv.org/abs/2610.41025"):
        self.addCleanup(lambda: None)
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "scripts").mkdir()
        (root / "data").mkdir()
        shutil.copy2(PROJECT / "scripts" / "validate.py", root / "scripts" / "validate.py")
        row = {
            "id": "sample-recovery-paper",
            "kind": kind,
            "area": "Recovery benchmark",
            "title": "A recovery-specific original publication",
            "year": "2026",
            "date": "2026-10",
            "url": url,
            "why": "Tests whether a failed agent can correct an action after a controlled fault.",
            "code": "",
            "note": "Synthetic record used only in unit tests.",
        }
        with (root / "data" / "resources.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerow(row)
        return root

    def run_validator(self, root, *flags):
        return subprocess.run(
            [sys.executable, str(root / "scripts" / "validate.py"), *flags],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_paper_primary_source_is_valid(self):
        root = self.make_catalog()
        self.assertEqual(self.run_validator(root, "--sync-json").returncode, 0)
        result = self.run_validator(root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads((root / "data" / "resources.json").read_text())[0]["kind"], "paper")

    def test_nonpaper_resource_is_rejected(self):
        root = self.make_catalog(kind="runtime")
        result = self.run_validator(root, "--sync-json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("kind=paper", result.stderr)

    def test_code_host_is_rejected_as_paper_primary_source(self):
        root = self.make_catalog(url="https://github.com/example/agent-framework")
        result = self.run_validator(root, "--sync-json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("canonical scholarly source", result.stderr)


if __name__ == "__main__":
    unittest.main()
