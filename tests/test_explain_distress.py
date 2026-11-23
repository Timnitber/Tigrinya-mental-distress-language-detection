import unittest
from src.explain_distress import explain_distress_items


class TestExplainDistressItems(unittest.TestCase):
    def test_explains_geez_item_with_matched_signal(self):
        items = [{"text": "ሎሚ ተስፋ ቆሪጸ ኣለኹ", "score": 0.90}]
        result = explain_distress_items(items)
        explanation = result[0]["explanation"]
        self.assertIn("critical risk", explanation)
        self.assertIn("Ge'ez", explanation)
        self.assertIn("ተስፋ ቆሪጸ", explanation)

    def test_explains_latin_item_without_lexicon_match(self):
        items = [{"text": "Custom high risk signal", "score": 0.82}]
        result = explain_distress_items(items)
        explanation = result[0]["explanation"]
        self.assertIn("elevated risk", explanation)
        self.assertIn("Latin transliteration", explanation)
        self.assertIn("human volunteer review", explanation)


if __name__ == "__main__":
    unittest.main()