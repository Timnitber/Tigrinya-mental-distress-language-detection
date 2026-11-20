DEFAULT_RESOURCES = {
    "US": {
        "hotline": "988 Suicide & Crisis Lifeline (Call or Text 988)",
        "diaspora_support": "Tigrinya Community Mental Health Network - North America"
    },
    "UK": {
        "hotline": "Samaritans (Call 116 123)",
        "diaspora_support": "Eritrean & Tigrayan Diaspora Wellbeing Support UK"
    },
    "GLOBAL": {
        "hotline": "Find A Helpline (findahelpline.com)",
        "diaspora_support": "International Tigrinya Peer Support Directory"
    }
}


def attach_localized_resources(
    items: list[dict], region: str, resource_db: dict | None = None
) -> list[dict]:
    """Attach verified crisis hotlines and diaspora support based on region."""
    db = resource_db if resource_db is not None else DEFAULT_RESOURCES
    normalized_region = region.strip().upper()
    matched = db.get(normalized_region, db["GLOBAL"])

    enriched = []
    for item in items:
        updated_item = dict(item)
        updated_item["region"] = normalized_region
        updated_item["resources"] = matched
        enriched.append(updated_item)
    return enriched
