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

The official skill's DPR calculation and `开放改进问题` requirements apply here. For each base-class mapping, calculate DPR only for routes that are legal for that mapped class progression. If the Strixhaven subclass changes a DPR aspect from the base class, include the subclass DPR-delta table; if it enables an aspect the base class lacks, calculate and rank that aspect normally. If no DPR aspect changes, state that it follows the mapped base class. `开放改进问题` should focus on the UA multi-class mapping, delayed/missing feature slots, published Strixhaven context, and any RAW/RAI ambiguity created by using one subclass across multiple base classes.

## Review Input Boundary

Follow the official skill's independent-review rule. A Strixhaven mapping review is based on the latest verified local UA source, the base-class mapping rules in this skill, the official ranking skill, and version-matched community discussion. Prompt context, older review files, and source-diff notes are only inspection aids unless a new criterion has first been recorded in the relevant skill / changelog.

## Local Source Rules

- Treat these as `5E UA` resources.
- Verify names, compatible classes, feature text, subclass spell tables, and prerequisites from the UA source before writing. Prefer the CN online raw-root first when available: resolve `UA2021MagesOfStrixhaven` through `https://ua.kiwee.top/_generated/index-sources.json` or `https://ua.kiwee.top/_generated/index-props.json`, then fetch the mapped translated JSON path from `https://ua.kiwee.top/`. Use `5etools-unearthed-arcana` as the local EN fallback and sanity check: resolve `ua2021magesofstrixhaven` / Strixhaven prerelease through `5etools-unearthed-arcana\_generated\index-sources.json`, then open the referenced JSON under the relevant category or `collection`. If the CN online JSON is reachable but an individual Chinese entry is missing, use `DND5e_chm` first and `DND2014_legacy` second for translation confirmation before writing a provisional Chinese rendering. Use `DND2014_legacy` / `DND5e_chm` Strixhaven text and existing `Rankings` files for Chinese name, local phrasing, and translation confirmation.
- Default to enabling the published Strixhaven context under `DND5e_chm\斯翠海文：混沌研习` when evaluating the UA subclasses. This means Strixhaven spells, feats, backgrounds, magic items, campus assumptions, and other published setting support can be discussed as available context, while the subclass features themselves remain the 5e-era UA subclass features.
- Follow the official skill's version-precedence and publish-date audit rules. The published Strixhaven background / feat / spell / setting system does not replace the 5e-era UA multi-class subclass mechanics unless the user explicitly asks for a conversion or comparison. If a future official or UA source republishes a same-name subclass in a newer rules era, use separate files when the official skill requires separate 2014-official / 2024-UA handling.
- If Strixhaven rows are added to a root checklist, also follow the official skill's checklist rules: include resource release date, avoid duplicate same-lineage entries, and record the UA source/date rather than treating the published Strixhaven setting book as the subclass source.
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
