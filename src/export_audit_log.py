import html
from pathlib import Path


def export_audit_log(items: list[dict], output_path: str) -> str:
    """Render de-identified flagged items into a standalone HTML audit log."""
    rows = []
    for item in items:
        safe_text = html.escape(str(item.get("text", "")))
        safe_score = html.escape(str(item.get("score", "N/A")))
        safe_region = html.escape(str(item.get("region", "GLOBAL")))
        resources = item.get("resources", {})
        safe_hotline = html.escape(str(resources.get("hotline", "N/A")))
        safe_support = html.escape(str(resources.get("diaspora_support", "N/A")))

        rows.append(
            f"<tr>"
            f"<td>{safe_text}</td>"
            f"<td>{safe_score}</td>"
            f"<td>{safe_region}</td>"
            f"<td>{safe_hotline}</td>"
            f"<td>{safe_support}</td>"
            f"</tr>"
        )

    table_body = "\n".join(rows) if rows else '<tr><td colspan="5">No flagged items recorded.</td></tr>'

    document = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tigrinya Distress Screening Audit Log</title>
  <style>
    body {{ font-family: sans-serif; margin: 2rem; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 0.6rem; text-align: left; }}
    th {{ background-color: #f4f4f4; }}
  </style>
</head>
<body>
  <h1>Tigrinya Distress Screening Audit Log</h1>
  <table>
    <thead>
      <tr>
        <th>De-identified Text</th>
        <th>Distress Score</th>
        <th>Region</th>
        <th>Crisis Hotline</th>
        <th>Diaspora Support</th>
      </tr>
    </thead>
    <tbody>
      {table_body}
    </tbody>
  </table>
</body>
</html>
"""
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(document, encoding="utf-8")
    return str(destination)