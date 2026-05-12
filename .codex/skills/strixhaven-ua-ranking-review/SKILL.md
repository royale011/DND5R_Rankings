---
name: strixhaven-ua-ranking-review
description: Use when reviewing or ranking the 5e-era UA Strixhaven multi-class subclasses in this DND5R_Rankings project. Applies the official-dnd-ranking-review workflow, plus Strixhaven-specific base-class/subclass-feature level mapping.
---

# Strixhaven UA Ranking Review

Use this skill for the 5e-era UA `Mages of Strixhaven` subclasses:

- `衡鉴魔法师 Mage of Lorehold`
- `粹丽魔法师 Mage of Prismari`
- `量析魔法师 Mage of Quandrix`
- `银毫魔法师 Mage of Silverquill`
- `靡华魔法师 Mage of Witherbloom`

This is a narrow companion skill. All source-verification, community-calibration, ranking-scale, README, changelog, and tooling rules are the same as `.codex/skills/official-dnd-ranking-review/SKILL.md`; read and follow that skill first. Do not use this skill for the published Strixhaven background/feat system unless the user specifically asks to compare it to the UA subclass system.

## Review Input Boundary

Follow the official skill's independent-review rule. A Strixhaven mapping review is based on the latest verified local UA source, the base-class mapping rules in this skill, the official ranking skill, and version-matched community discussion. Prompt context, older review files, and source-diff notes are only inspection aids unless a new criterion has first been recorded in the relevant skill / changelog.

## Local Source Rules

- Treat these as `5E UA` resources.
- Verify names, compatible classes, feature text, subclass spell tables, and prerequisites from local `DND2014_legacy` / `DND5e_chm` Strixhaven UA text before writing.
- Default to enabling the published Strixhaven context under `DND5e_chm\斯翠海文：混沌研习` when evaluating the UA subclasses. This means Strixhaven spells, feats, backgrounds, magic items, campus assumptions, and other published setting support can be discussed as available context, while the subclass features themselves remain the 5e-era UA subclass features.
- Use Chinese names from local source where available. Include English names on first mention only when useful for searchability. Follow the official skill's abbreviation rule: common CN-community abbreviations such as `UA`, `DPR`, `RAW`, `RAI`, `DM`, `PC`, `BA`, `OA`, `ASI`, and source abbreviations do not need forced Chinese translation.
- Apply the project legacy-subclass compatibility rule: old subclass features or subclass spells that would be granted below level 3 are evaluated as coming online at level 3 in the 5.5e / 2024 environment.

## Core Mapping Rule

Strixhaven UA subclasses do not map cleanly to one class schedule. They list feature prerequisites such as `1+`, `6+`, `10+`, and `14+`, and compatible classes receive subclass features only when that base class grants a subclass feature.

When evaluating a Strixhaven UA subclass:

1. Identify the base class being reviewed.
2. Use that base class's subclass-feature levels, converted to 5.5e / 2024 compatibility.
3. At each subclass-feature level, grant only the Strixhaven features whose prerequisite is met and whose feature slot is actually reached by that base class.
4. If a base class skips a Strixhaven prerequisite level, the feature is delayed until the next subclass-feature level that can legally take it.
5. If more than one unchosen Strixhaven feature is legal at the same subclass-feature level, record the choice and evaluate the strongest normal choice and the opportunity cost of not taking the other one.
6. Do not assume every compatible class receives every `1+ / 6+ / 10+ / 14+` feature at those exact levels.

## Compatible Classes

- `衡鉴魔法师 Mage of Lorehold`: `吟游诗人`, `魔契师`, `法师`
- `粹丽魔法师 Mage of Prismari`: `德鲁伊`, `术士`, `法师`
- `量析魔法师 Mage of Quandrix`: `术士`, `法师`
- `银毫魔法师 Mage of Silverquill`: `吟游诗人`, `魔契师`, `法师`
- `靡华魔法师 Mage of Witherbloom`: `德鲁伊`, `魔契师`

## Base-Class Feature Slot Mapping

Use this default 5.5e-compatible mapping unless local source or a later project rule overrides it:

| Base class | Strixhaven feature slots for this project |
|---|---|
| `吟游诗人` | level 3 gets `1+` package; level 6 gets `6+`; level 14 can choose one legal remaining feature, usually `10+` or `14+`, not both. |
| `德鲁伊` | level 3 gets `1+` package; level 6 gets `6+`; level 10 gets `10+`; level 14 gets `14+`. |
| `魔契师` | level 3 gets `1+` package; level 6 gets `6+`; level 10 gets `10+`; level 14 gets `14+`. |
| `法师` | level 3 gets `1+` package; level 6 gets `6+`; level 10 gets `10+`; level 14 gets `14+`. |
| `术士` | level 3 gets `1+` package; level 6 gets `6+`; level 14 can choose `10+` or `14+`; level 18 can take the remaining legal feature if the subclass text and review convention allow another subclass feature slot. |

## Review Output Expectations

- A single Strixhaven subclass may need separate review files per base class if the feature mapping changes enough to change strength or role. Do not collapse them into one file if a class loses/delays a major feature.
- In `详细评价`, explicitly state the base class being evaluated and the feature-slot mapping used.
- In `综合评分`, do not score the subclass as if all compatible classes receive the same package.
- In class README leaderboards, use filenames/source markers that make both the Strixhaven subclass and base-class context clear.
