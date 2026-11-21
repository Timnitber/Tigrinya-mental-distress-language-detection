import re


def redact_identifiers(text: str) -> str:
    """Mask handles, email addresses, and phone numbers in a text string."""
    redacted = re.sub(r"@[\w.-]+", "[REDACTED_HANDLE]", text)
    redacted = re.sub(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", "[REDACTED_EMAIL]", redacted)
    redacted = re.sub(r"(?<!\w)(?:\+?\d[\d\s().-]{7,}\d)(?!\w)", "[REDACTED_PHONE]", redacted)
    return redacted


def deidentify_items(items: list[dict], text_key: str = "text") -> list[dict]:
    """Return a new list of items with personal identifiers redacted in text_key."""
    cleaned_items = []
    for item in items:
        updated = dict(item)
        if text_key in updated and isinstance(updated[text_key], str):
            updated[text_key] = redact_identifiers(updated[text_key])
        cleaned_items.append(updated)
    return cleaned_items