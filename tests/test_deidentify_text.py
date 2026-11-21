import unittest
from src.deidentify_text import deidentify_items, redact_identifiers


class TestDeidentifyText(unittest.TestCase):
    def test_redacts_handle_email_and_phone(self):
        sample = "Reach @tig_helper or test@example.com or +1 (212) 555-0199."
        cleaned = redact_identifiers(sample)
        self.assertNotIn("@tig_helper", cleaned)
        self.assertNotIn("test@example.com", cleaned)
        self.assertNotIn("555-0199", cleaned)
        self.assertIn("[REDACTED_HANDLE]", cleaned)
        self.assertIn("[REDACTED_EMAIL]", cleaned)
        self.assertIn("[REDACTED_PHONE]", cleaned)

    def test_deidentify_items_preserves_other_fields(self):
        items = [{"text": "Call +1 917-555-0144", "score": 0.92, "region": "US"}]
        result = deidentify_items(items)
        self.assertEqual(result[0]["score"], 0.92)
        self.assertEqual(result[0]["region"], "US")
        self.assertIn("[REDACTED_PHONE]", result[0]["text"])


if __name__ == "__main__":
    unittest.main()
    