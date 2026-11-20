import unittest
from src.lookup_resources import attach_localized_resources


class TestAttachLocalizedResources(unittest.TestCase):
    def test_matches_known_region(self):
        items = [{"text": "sample flagged post", "score": 0.88}]
        result = attach_localized_resources(items, "us")
        self.assertEqual(result[0]["region"], "US")
        self.assertIn("988", result[0]["resources"]["hotline"])

    def test_falls_back_to_global_for_unknown_region(self):
        items = [{"text": "sample flagged post", "score": 0.91}]
        result = attach_localized_resources(items, "Mars")
        self.assertEqual(result[0]["region"], "MARS")
        self.assertIn("findahelpline.com", result[0]["resources"]["hotline"])


if __name__ == "__main__":
    unittest.main()
    