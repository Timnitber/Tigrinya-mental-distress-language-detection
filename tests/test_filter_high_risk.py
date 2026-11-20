import unittest
from src.filter_high_risk import filter_high_risk_items


class TestFilterHighRiskItems(unittest.TestCase):
    def test_filters_items_above_threshold(self):
        texts = ["post one", "post two", "post three"]
        scores = [0.2, 0.85, 0.9]
        result = filter_high_risk_items(texts, scores, threshold=0.75)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["text"], "post two")

    def test_mismatched_lengths_raises_error(self):
        with self.assertRaises(ValueError):
            filter_high_risk_items(["only one"], [0.5, 0.9])


if __name__ == "__main__":
    unittest.main()
    