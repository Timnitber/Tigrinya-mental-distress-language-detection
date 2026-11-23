from src.deidentify_text import deidentify_items
from src.explain_distress import explain_distress_items
from src.export_audit_log import export_audit_log
from src.filter_high_risk import filter_high_risk_items
from src.lookup_resources import attach_localized_resources
from src.score_distress import score_distress_texts


def run_distress_pipeline(
    texts: list[str],
    output_html_path: str,
    region: str = "GLOBAL",
    threshold: float = 0.75,
) -> list[dict]:
    """Run scoring, high-risk filtering, explanation, resource lookup, de-identification, and audit export."""
    scores = score_distress_texts(texts)
    flagged_items = filter_high_risk_items(texts, scores, threshold=threshold)
    explained_items = explain_distress_items(flagged_items)
    enriched_items = attach_localized_resources(explained_items, region=region)
    safe_items = deidentify_items(enriched_items)
    export_audit_log(safe_items, output_html_path)
    return safe_items