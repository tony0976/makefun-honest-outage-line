"""Writes the most honest outage status line to /output/entry.txt."""
import os

TEXT = "Everything is down. Not 'degraded', not 'partial' — every server, every queue, every dashboard. We broke it. We are fixing it."

# Rule: a status-page line must be a single line of at most 160 characters.
assert "\n" not in TEXT and len(TEXT) <= 160, f"entry must be one line, <=160 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
