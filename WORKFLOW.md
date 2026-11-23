# Tigrinya Distress Screening Workflow

## Overview
This pipeline screens Tigrinya social media text (Ge'ez script and Latin transliteration) to flag elevated emotional distress, attach culturally relevant support resources, redact personal identifiers, and export an HTML audit log for community volunteers.

## Module Architecture
- **Atomic Protocols:**
  - `score_distress.py`: Scores Ge'ez and Latin-transliterated Tigrinya text (`0.0`–`1.0`).
  - `filter_high_risk.py`: Filters posts meeting or exceeding the risk threshold.
  - `deidentify_text.py`: Masks emails, `@handles`, and phone numbers before review.
- **Disposable Components:**
  - `explain_distress.py`: Generates concise volunteer-facing risk explanations.
  - `lookup_resources.py`: Attaches localized crisis hotlines and diaspora support networks.
  - `export_audit_log.py`: Renders a standalone HTML audit report.
  