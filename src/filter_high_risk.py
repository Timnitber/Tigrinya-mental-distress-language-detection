def filter_high_risk_items(texts: list[str], scores: list[float], threshold: float = 0.75) -> list[dict]:
    """Return items whose distress similarity score meets or exceeds the threshold."""
    if len(texts) != len(scores):
        raise ValueError("texts and scores must have the same length")

    flagged = []
    for text, score in zip(texts, scores):
        if score >= threshold:
            flagged.append({"text": text, "score": score})
    return flagged
