# Ranking Maintenance Tools

## 目录

- [Tracked Scripts](#tracked-scripts)
- [Scratch Scripts](#scratch-scripts)

## Tracked Scripts

- `rebuild_class_leaderboards_from_reviews.py`: rebuilds class README subclass leaderboards from file-level `综合评分` tables.
- `update_root_summary.py`: rebuilds root `Rankings/README.md` summary tables from current review files.
- `update_readme_toc.py`: maintains `## 目录` sections for active README and review Markdown files.
- `audit_design_scores.py`: audits design-score tables and repeated design-score reason patterns.

## Scratch Scripts

Do not commit one-off `rewrite_*`, `calibrate_*`, `generate_*`, or source-migration helper scripts. Those scripts are useful while doing a specific batch rewrite, but they should remain local scratch files unless they become stable reusable infrastructure.
