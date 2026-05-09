---
name: theurgy-ua-ranking-review
description: Use when reviewing or ranking the 5e-era UA Wizard subclass 神圣奇术 Theurgy and its required mapping to every non-homebrew Cleric domain in this DND5R_Rankings project. Applies the official-dnd-ranking-review workflow, plus Theurgy-specific compatibility wording, output directory structure, and Cleric-domain synchronization rules.
---

# Theurgy UA Ranking Review

Use this skill for `神圣奇术 Theurgy`, the 5e-era UA Wizard subclass that maps onto Cleric domains.

This is a narrow companion skill. All source-verification, community-calibration, ranking-scale, README, changelog, and tooling rules are the same as `.codex/skills/official-dnd-ranking-review/SKILL.md`; read and follow that skill first.

## Effective Source

- Treat `神圣奇术 Theurgy` as a `5E UA` resource.
- The original 5e UA text is only used for source identity and historical comparison.
- The effective mechanics for project review are the credited 5.5e-compatible text stored in `Rankings\法师\神圣奇术\README.md`, under the heading `神圣奇术规则（by 落雨随枫）`.
- Do not use model memory for Theurgy feature text. Re-read `Rankings\法师\神圣奇术\README.md` before every Theurgy review pass.

## Core Compatibility Rules

Use these project rules when mapping a Cleric domain onto Theurgy:

- All domain spells and Cleric spells added to the spellbook by Theurgy count as Wizard spells for the Theurgy character.
- Other Wizards cannot copy Cleric spells gained by Theurgy from that spellbook.
- `奥术入信 Arcane Initiate`: whenever the character gains a Wizard level, one Wizard spell that would be added to the spellbook may be replaced by a spell from the chosen Cleric domain, limited by spell slots. After all domain spells are added, the replacement may use any Cleric-list spell, still limited by spell slots.
- `引导奥秘 Channel Arcana` uses the domain's level-3 Channel Divinity option through the Theurgy Channel Arcana resource.
- If a Theurgy feature uses wording that refers to Cleric level, replace it with Wizard level.
- Channel Arcana / Channel Divinity use count follows the multiclass Channel Divinity rule.
- Save DC for Channel Arcana effects equals Wizard spell save DC.
- Wisdom-based uses/effects from mapped Cleric-domain features become Intelligence-based.
- If a mapped domain feature points to Cleric spells, it points to the Theurgy character's Wizard spells.
- `奥术侍僧 Arcane Acolyte` at Wizard 6 grants the chosen domain's level-3 non-Channel-Divinity benefits, but never grants weapon or armor proficiency.
- `奥术祭司 Arcane Priest` at Wizard 10 grants the chosen domain's level-6 benefit.
- `奥术大祭司 Arcane High Priest` at Wizard 14 grants the chosen domain's level-17 benefit.

## Domain Scope

- Map Theurgy to every existing non-homebrew Cleric domain that has a root `Rankings\牧师` review.
- Include official, 5E UA, newer UA, partner, and third-party published Cleric domains.
- Exclude all homebrew Cleric domains. Homebrew Cleric content is not mapped to Theurgy unless the user explicitly requests it later.
- When a new non-homebrew Cleric-domain review is added under root `Rankings\牧师`, create or update the corresponding Theurgy review in the same pass.

## Output Structure

- Base directory: `Rankings\法师\神圣奇术`.
- The base file is `Rankings\法师\神圣奇术\README.md`.
- Standalone review files live under that directory, one file per Cleric-domain mapping.
- Use the Cleric domain's verified Chinese name and source marker in the Theurgy file name, preserving UA / partner / third-party markers where applicable.

Theurgy is not a root-level class and must not be added as a base class to root `Rankings\README.md`.

## Leaderboard Rules

`Rankings\法师\神圣奇术\README.md` should behave like a class README for the Theurgy mapping set:

- Include `分阶段子职排行榜` for Theurgy mappings based on official first-party Cleric domains.
- Include `UA/合作方/第三方子职分阶段排行榜` for Theurgy mappings based on UA, partner, or third-party Cleric domains.

`Rankings\法师\README.md` must include all Theurgy-domain combinations in the Wizard UA / partner / third-party leaderboard, because Theurgy itself is 5E UA. Use this display format:

`神圣奇术（5E UA） - [牧师领域中文名]`

The root `Rankings\README.md` must use the same display format and also place all Theurgy-domain combinations in `UA/合作方/第三方子职分阶段排行榜`.

## Review Focus

Each Theurgy-domain review must explicitly separate:

- Wizard chassis contribution: spellbook, rituals, prepared Wizard list, `奥术回想`, `记忆法术`, high-level Wizard spells, `法术精通`, and `招牌法术`.
- Theurgy base package: domain/Cleric spellbook conversion, Channel Arcana, `神圣奥能`, and Cleric-list access pressure.
- Domain increment: the actual mapped domain spells and features at Wizard 3 / 6 / 10 / 14.
- Cleric spell access timing: before every chosen domain spell has been added to the spellbook, `奥术入信` is mostly locked to that domain's domain-spell list. A normal Cleric domain has ten domain spells. Since Theurgy starts at Wizard level 3 and gains one `奥术入信` replacement per Wizard level, the character is normally forced to spend levels 3-12 adding domain spells before open Cleric-list replacement begins at level 13. From level 13 onward, this is still only one Cleric-list replacement per Wizard level; it is not the same as a true Cleric preparing from the whole Cleric list every day. Like Bard `魔法奥秘 Magical Secrets`, the first free picks may need to backfill low-level staples that the character did not previously have, rather than immediately taking the highest-level Cleric spells. This lowers the chance of clean high-level Cleric-spell synergy and increases the importance of choosing which low-level Cleric spells are actually worth a level-up replacement. Domains with weak, narrow, redundant, or low-level-heavy domain spells delay access to the open Cleric list and should not be scored as if the Theurgy Wizard freely chooses from the whole Cleric list from level 3. Domains with strong always-useful domain spells or fewer painful redundancies reach the "open Cleric list" phase with less opportunity cost.
- Chassis synergy check: do not assume a Cleric-domain feature remains equally good on a Wizard. If the mapped domain encourages melee, weapon attacks, standing in a duration aura, armor/shield tanking, or repeated front-line concentration, ask whether the Wizard chassis can actually support that plan. In 5.5e / 2024, `克敌先击 True Strike` no longer grants advantage; it is an action-cast cantrip that makes one attack with a proficient weapon worth at least 1 CP, uses the spellcasting ability for that attack and damage roll, can convert the damage type to radiant, and gains extra radiant damage at cantrip breakpoints. A Wizard can also use `魔法学徒（德鲁伊） Magic Initiate (Druid)` as an `起源专长` route to obtain `橡棍术 Shillelagh`, improving staff/club-based melee ability. These are real melee patches, but they do not grant armor/shield proficiency, Extra Attack, martial durability, free advantage, or a front-line action loop; they also carry origin-feat, bonus-action/setup, weapon, and action-opportunity costs. Domains such as War- or Death-style packages must be scored by actual Wizard usability, not by how well they work on Cleric.
- Abuse vigilance: some mapped domains can create unusual timing or multiclass openings because Theurgy moves a Cleric domain's level-17 feature to Wizard level 14. The main warning case is `奥秘领域 Arcana Domain`: if its level-17 feature grants high-level Wizard spells, a Theurgy Wizard may receive those spell choices at Wizard 14. A pure Wizard 14 cannot yet cast 8th- or 9th-level spells, but a multiclass character may later obtain 8th/9th-level spell slots through the multiclass spellcasting rules while keeping those granted spells known/in the spellbook, then combine them with other class benefits such as Sorcerer metamagic, Bardic Inspiration or martial Bard features, Artificer utility, Paladin/Ranger martial chassis, or Paladin aura if ability scores allow. Treat these as abuse vectors to analyze explicitly; do not automatically declare them S+, but do not ignore the rule interaction.
- Limits: level-up-only spellbook replacement pressure, prepared spell pressure, action economy, concentration conflict, Channel Arcana use limits, table sensitivity of Cleric spell access as Wizard spells, and whether the domain feature still works cleanly when moved to an Intelligence-based Wizard.

Do not score every Theurgy mapping as `S` merely because the Wizard chassis is strong. If the domain contributes little beyond spell access, say that the result mainly rides the Wizard chassis and use the appropriate `S-` / `A+` / lower rank.

## Mapping Examples

Use these as sanity checks when building a full review:

- `神圣奇术（5E UA） - 知识领域`: level 3 gains Theurgy base package, `神圣奥能`, and the domain's level-3 Channel Divinity option through `引导奥秘`; level 6 gains the domain's level-3 non-Channel-Divinity benefits through `奥术侍僧`, excluding weapon/armor proficiency; level 10 gains the domain's level-6 feature; level 14 gains the domain's level-17 feature. Any Wisdom-based wording becomes Intelligence-based.
- `神圣奇术（5E UA） - 生命领域`: level 6 does not grant heavy armor or weapon proficiency even if a legacy source would; the mapped healing feature matters only if the Theurgy Wizard actually prepares and casts healing spells. Domain spells become Wizard spells in the spellbook, but prepared-spell pressure remains real.
- `神圣奇术（5E UA） - 光明领域`: level 3 can use the domain's Channel Divinity option through Channel Arcana; level 6 receives the domain's level-3 non-Channel-Divinity defensive/light feature; level 10 receives the domain's level-6 protection/reaction-style feature if present in the verified source; level 14 receives the domain's level-17 offensive light/fire feature. Check whether action/reaction and concentration costs compete with normal Wizard defenses and control.
- `神圣奇术（5E UA） - 和平领域`: if using the mapped official/legacy domain source, do not assume the Theurgy Wizard gets a Cleric's whole domain package at level 3. Channel Divinity comes through Channel Arcana at level 3, non-Channel level-3 benefits arrive at Wizard 6, level-6 benefits at Wizard 10, and level-17 benefits at Wizard 14. This timing can still be very strong, but the delay and resource channel matter.
