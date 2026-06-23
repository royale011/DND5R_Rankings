---
name: update-dnd-resources
description: Update this DND 5R project's resource submodules and review checklists. Use when asked to update all submodules, update 5etools resources, refresh official-review-checklist.md, scan new official / UA / partner / third-party classes or subclasses, or refresh external homebrew review checklist data.
---

# Update DND Resources

## Overview

Use this skill for the recurring resource refresh workflow in `C:\Users\royal\OneDrive\Documents\DND\5R`. It updates all current resource submodules except `DND2014_legacy`, rebuilds the official and external homebrew review checklists, and reports exactly what changed.

## Workflow

1. Capture the starting state.
   - Run `git status --short`.
   - Run `git submodule status`.
   - Note existing dirty files and do not revert unrelated changes.

2. Update only these submodules:
   - `DND5e_chm`
   - `5etools-src`
   - `5etools-cn`
   - `5etools-homebrew`
   - `5etools-unearthed-arcana`

3. Never update `DND2014_legacy` in this workflow.
   - If it appears modified before the task, report it as pre-existing.
   - If it changes accidentally, stop and ask before fixing.

4. Inspect changed content.
   - Use `git diff --submodule=log` after updating.
   - For changed 5etools resources, inspect relevant `data/`, `class/`, `subclass/`, `_generated/`, and search index changes.
   - For `DND5e_chm`, inspect changed filenames and directories enough to identify new official translations or source additions.

5. Rebuild checklists.
   - Run `python tools\rebuild_official_review_checklist.py`.
   - `official-review-checklist.md` receives official / UA / partner / third-party base classes and subclasses.
   - `homebrews\Rankings External\external-homebrew-review-checklist.md` receives raw creator-homebrew class/subclass rows from 5etools EN homebrew and verified CN raw homebrew sources.
   - Do not move raw creator-homebrew rows into root official rankings unless the user explicitly promotes a specific source.

6. Validate output.
   - Confirm both checklist headers' row counts match generated script output.
   - Confirm existing checkbox states are preserved.
   - Confirm `DND2014_legacy` did not update.
   - Run skill validation when this skill itself was edited.

7. Report concisely.
   - List submodules that changed with old and new short commits.
   - Summarize newly added official / UA / partner / third-party checklist rows.
   - Summarize newly added external homebrew checklist rows.
   - Mention any inaccessible CN raw index, network limitation, or deliberately skipped broad collection/adventure/book embedded scan.
   - End with `git status --short`.

## Commands

Use non-interactive commands. Recommended update command:

```powershell
git submodule update --remote DND5e_chm 5etools-src 5etools-cn 5etools-homebrew 5etools-unearthed-arcana
```

Recommended rebuild command:

```powershell
python tools\rebuild_official_review_checklist.py
```

If network access is blocked, rerun the same network command with approval instead of changing the workflow.
