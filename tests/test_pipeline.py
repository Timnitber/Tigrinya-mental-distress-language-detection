import tempfile
import unittest
from pathlib import Path
from src.pipeline import run_distress_pipeline


class TestDistressPipeline(unittest.TestCase):
    def test_end_to_end_pipeline_filters_redacts_and_exports(self):
        sample_texts = [
            "ሰላም ከመይ ኣለኻ",
            "ተስፋ ቆሪጸ ኣለኹ፣ reach @someone_tig or +1 212-555-0188",
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            html_out = Path(tmp_dir) / "pipeline_audit.html"
            results = run_distress_pipeline(
                texts=sample_texts,
                output_html_path=str(html_out),
                region="US",
                threshold=0.75,
            )

            self.assertEqual(len(results), 1)
            item = results[0]
            self.assertNotIn("@someone_tig", item["text"])
            self.assertNotIn("212-555-0188", item["text"])
            self.assertIn("explanation", item)
            self.assertEqual(item["region"], "US")
            self.assertTrue(html_out.exists())
            html_content = html_out.read_text(encoding="utf-8")
            self.assertIn("Tigrinya Distress Screening Audit Log", html_content)


if __name__ == "__main__":
    unittest.main()