from src.score_distress import DEFAULT_DISTRESS_MARKERS


def _detect_script(text: str) -> str:
    """Identify whether text contains Ge'ez characters, Latin script, or mixed."""
    has_geez = any("\u1200" <= ch <= "\u137f" for ch in text)
    has_latin = any("a" <= ch.lower() <= "z" for ch in text)
    if has_geez and has_latin:
        return "mixed Ge'ez and Latin"
    if has_geez:
        return "Ge'ez"
    return "Latin transliteration"


def _find_matched_markers(text: str, markers: dict[str, float]) -> list[str]:
    normalized = text.strip().lower()
    return [phrase for phrase in markers if phrase.lower() in normalized]


def explain_distress_items(
    items: list[dict], markers: dict[str, float] | None = None
) -> list[dict]:
    """Attach a concise volunteer-facing rationale explaining each flagged item."""
    lexicon = markers if markers is not None else DEFAULT_DISTRESS_MARKERS
    explained = []

    for item in items:
        updated = dict(item)
        text = str(updated.get("text", ""))
        score = float(updated.get("score", 0.0))
        script_type = _detect_script(text)
        matched = _find_matched_markers(text, lexicon)

        severity = "critical" if score >= 0.90 else "elevated"
        if matched:
            signals = ", ".join(f"'{m}'" for m in matched)
            rationale = (
                f"Flagged at {severity} risk (score {score:.2f}) in {script_type} script. "
                f"Detected Tigrinya distress signal(s): {signals}. "
                f"Recommend warm volunteer outreach and localized crisis resource sharing."
            )
        else:
            rationale = (
                f"Flagged at {severity} risk (score {score:.2f}) in {script_type} script "
                f"based on overall distress score threshold. Recommend human volunteer review."
            )

        updated["explanation"] = rationale
        explained.append(updated)

    return explained
