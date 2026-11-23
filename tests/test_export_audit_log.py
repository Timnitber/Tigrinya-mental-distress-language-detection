import tempfile
import unittest
from pathlib import Path
from src.export_audit_log import export_audit_log


class TestExportAuditLog(unittest.TestCase):
    def test_exports_html_with_item_details(self):
        sample_items = [
            {
                "text": "I feel hopeless, please contact [REDACTED_HANDLE]",
                "score": 0.91,
                "region": "US",
                "resources": {
                    "hotline": "988 Suicide & Crisis Lifeline",
                    "diaspora_support": "Tigrinya Community Mental Health Network",
                },
            }
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_file = Path(tmp_dir) / "audit_log.html"
            saved_path = export_audit_log(sample_items, str(out_file))

            self.assertTrue(Path(saved_path).exists())
            content = Path(saved_path).read_text(encoding="utf-8")
            self.assertIn("Tigrinya Distress Screening Audit Log", content)
            self.assertIn("[REDACTED_HANDLE]", content)
            self.assertIn("988 Suicide &amp; Crisis Lifeline", content)

    def test_exports_empty_state_message_when_no_items(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_file = Path(tmp_dir) / "empty_log.html"
            export_audit_log([], str(out_file))

            content = out_file.read_text(encoding="utf-8")
            self.assertIn("No flagged items recorded.", content)


if __name__ == "__main__":
    unittest.main()