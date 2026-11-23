DEFAULT_DISTRESS_MARKERS = {
    # Ge'ez script Tigrinya distress expressions and weights
    "ተስፋ ቆሪጸ": 0.90,
    "ተስፋ ቆሪጹ": 0.90,
    "ሕይወተይ ኣብ ሓደጋ": 0.95,
    "ነብሰይ ክቐትል": 0.98,
    "ኣዝየ ተጨኒቐ": 0.80,
    "በይነይ ተሪፈ": 0.75,
    # Latin-transliterated Tigrinya distress expressions and weights
    "tesfa qoritse": 0.90,
    "tesfa koritse": 0.90,
    "hiwetey ab hadega": 0.95,
    "nebsey kqetl": 0.98,
    "nebsey kiketil": 0.98,
    "azye techeniqe": 0.80,
    "beyney terife": 0.75,
}


def score_single_text(text: str, markers: dict[str, float] | None = None) -> float:
    """Return a distress score between 0.0 and 1.0 for a Tigrinya text string."""
    lexicon = markers if markers is not None else DEFAULT_DISTRESS_MARKERS
    normalized = text.strip().lower()
    if not normalized:
        return 0.0

    matched_scores = [
        weight for phrase, weight in lexicon.items() if phrase.lower() in normalized
    ]
    return max(matched_scores) if matched_scores else 0.10


def score_distress_texts(
    texts: list[str], markers: dict[str, float] | None = None
) -> list[float]:
    """Score a list of Tigrinya texts (Ge'ez script or Latin transliteration)."""
    return [score_single_text(text, markers=markers) for text in texts]