import unittest
from src.score_distress import score_distress_texts


class TestScoreDistressTexts(unittest.TestCase):
    def test_scores_geez_and_latin_distress_phrases_high(self):
        texts = [
            "ሎሚ ኣዝየ ተጨኒቐ ኣለኹ፣ ተስፋ ቆሪጸ",
            "Hiji azie dkum eye, tesfa qoritse",
        ]
        scores = score_distress_texts(texts)
        self.assertEqual(len(scores), 2)
        self.assertGreaterEqual(scores[0], 0.85)
        self.assertGreaterEqual(scores[1], 0.85)

    def test_scores_neutral_and_empty_text_low(self):
        texts = ["ሰላም ከመይ ኣለኻ", ""]
        scores = score_distress_texts(texts)
        self.assertLess(scores[0], 0.30)
        self.assertEqual(scores[1], 0.0)


if __name__ == "__main__":
    unittest.main()