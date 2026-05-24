# DPR Ranking Reference Draft

> Local draft. This file is intentionally ignored by Git through `/loot/`.

## Purpose

This file is a working reference for mapping DPR calculations into the six damage-ranking aspects:

- `近距爆发DPR（15尺内）`
- `近距持续DPR（15尺内）`
- `近距范围DPR（15尺内）`
- `远程爆发DPR`
- `远程持续DPR`
- `远程范围DPR`

It is not a replacement for review judgment. A rank still needs target access, action economy, setup, resource recovery, concentration, survivability, enemy type, resistance/immunity, save/attack reliability, and party context.

## Sources And Calibration Notes

- Monster HP/AC source: `5etools-src/data/bestiary/bestiary-xmm.json`, source tag `XMM`.
- Encounter budget source: 2024 Combat Encounters XP Budget per Character table, using a 4-PC party and `Moderate` / `High` budgets as the default ranking reference.
- Community DPR calibration: RPGBOT's Fundamental Math uses 65% as the expected attack-success baseline and derives DPR bands from monster HP over a 3-round, 4-PC encounter model. The community also commonly uses Warlock baseline / optimized martial baseline as a horizontal build check, but those are PC-vs-PC reference points rather than monster-percentage references.
- Adventuring day calibration: 6-8 medium/hard encounters is best treated as an endurance upper estimate, not as the only real table pace. The file therefore separates `长休爆发`, `短休爆发`, `每战/低消耗`, and `可连续维持`.
- Magic item calibration: 2024 DMG basic rules state that magic items are not required for characters to keep up, but also give a typical party-wide magic-item award table totaling 100 items by level 20. This reference therefore uses three item profiles instead of a single hard assumption.

## Reference CR Method

For each PC level, use these reference monsters:

- `爆发CR`: highest single monster CR whose XP fits a 4-PC `High` encounter budget.
- `持续CR`: highest single monster CR whose XP fits a 4-PC `Moderate` encounter budget.
- `近距AoE CR`: highest CR where 2 monsters fit a 4-PC `Moderate` encounter budget.
- `远程AoE CR`: highest CR where 3 monsters fit a 4-PC `Moderate` encounter budget.

Melee and ranged single-target reference CRs are numerically identical. The ranking difference comes from delivery risk:

- 近距 DPR is discounted if the routine must stand in 5/10/15 ft danger, needs concentration, or has weak escape/concentration protection.
- 远程 DPR is discounted if range is only 30/60 ft, relies on line of sight, poor target access, poor ammunition/item support, or disadvantage from close enemies.
- AoE DPR is discounted if it requires table-perfect enemy packing, friendly-fire avoidance, enemy size/terrain cooperation, or a low-probability bounce/chain condition.

## PC Level Reference Table

| 等级 | 近距爆发CR | 近距持续CR | 近距AoE CR | 远程爆发CR | 远程持续CR | 远程AoE CR | 参考HP/AC摘要 |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1/2 x2 | 1 | 1 | 1/2 x3 | 爆发CR1 HP中位/均值 26/28.9 AC中位 13；持续CR1 HP中位/均值 26/28.9 AC中位 13 |
| 2 | 3 | 2 | 1 x2 | 3 | 2 | 1 x3 | 爆发CR3 HP中位/均值 65/62.7 AC中位 14；持续CR2 HP中位/均值 45/46.2 AC中位 13 |
| 3 | 4 | 3 | 2 x2 | 4 | 3 | 1 x3 | 爆发CR4 HP中位/均值 71/70.9 AC中位 15；持续CR3 HP中位/均值 65/62.7 AC中位 14 |
| 4 | 5 | 4 | 3 x2 | 5 | 4 | 2 x3 | 爆发CR5 HP中位/均值 93.5/98.9 AC中位 15；持续CR4 HP中位/均值 71/70.9 AC中位 15 |
| 5 | 8 | 7 | 4 x2 | 8 | 7 | 3 x3 | 爆发CR8 HP中位/均值 136/135 AC中位 16；持续CR7 HP中位/均值 126.5/128.4 AC中位 16 |
| 6 | 9 | 8 | 5 x2 | 9 | 8 | 4 x3 | 爆发CR9 HP中位/均值 156.5/157.8 AC中位 17.5；持续CR8 HP中位/均值 136/135 AC中位 16 |
| 7 | 10 | 9 | 6 x2 | 10 | 9 | 4 x3 | 爆发CR10 HP中位/均值 161.5/170.7 AC中位 18；持续CR9 HP中位/均值 156.5/157.8 AC中位 17.5 |
| 8 | 12 | 10 | 7 x2 | 12 | 10 | 5 x3 | 爆发CR12 HP中位/均值 182/188 AC中位 18；持续CR10 HP中位/均值 161.5/170.7 AC中位 18 |
| 9 | 13 | 11 | 8 x2 | 13 | 11 | 6 x3 | 爆发CR13 HP中位/均值 195/200.2 AC中位 18；持续CR11 HP中位/均值 197/194.1 AC中位 17 |
| 10 | 14 | 12 | 8 x2 | 14 | 12 | 7 x3 | 爆发CR14 HP中位/均值 195/200.5 AC中位 18.5；持续CR12 HP中位/均值 182/188 AC中位 18 |
| 11 | 16 | 14 | 9 x2 | 16 | 14 | 7 x3 | 爆发CR16 HP中位/均值 255/240.1 AC中位 19；持续CR14 HP中位/均值 195/200.5 AC中位 18.5 |
| 12 | 17 | 15 | 11 x2 | 17 | 15 | 8 x3 | 爆发CR17 HP中位/均值 256/255.4 AC中位 20；持续CR15 HP中位/均值 209.5/216 AC中位 18 |
| 13 | 18 | 16 | 12 x2 | 18 | 16 | 9 x3 | 爆发CR18 HP中位/均值 180/180 AC中位 20；持续CR16 HP中位/均值 255/240.1 AC中位 19 |
| 14 | 19 | 17 | 12 x2 | 19 | 17 | 10 x3 | 爆发CR19 HP中位/均值 287/287 AC中位 19；持续CR17 HP中位/均值 256/255.4 AC中位 20 |
| 15 | 20 | 18 | 13 x2 | 20 | 18 | 11 x3 | 爆发CR20 HP中位/均值 332.5/331.2 AC中位 20；持续CR18 HP中位/均值 180/180 AC中位 20 |
| 16 | 21 | 19 | 14 x2 | 21 | 19 | 11 x3 | 爆发CR21 HP中位/均值 333/335.8 AC中位 21；持续CR19 HP中位/均值 287/287 AC中位 19 |
| 17 | 22 | 20 | 15 x2 | 22 | 20 | 12 x3 | 爆发CR22 HP中位/均值 444/405.3 AC中位 22；持续CR20 HP中位/均值 332.5/331.2 AC中位 20 |
| 18 | 23 | 21 | 16 x2 | 23 | 21 | 14 x3 | 爆发CR23 HP中位/均值 468/444.8 AC中位 22；持续CR21 HP中位/均值 333/335.8 AC中位 21 |
| 19 | 24 | 22 | 18 x2 | 24 | 22 | 15 x3 | 爆发CR24 HP中位/均值 526.5/526.5 AC中位 22；持续CR22 HP中位/均值 444/405.3 AC中位 22 |
| 20 | 25 | 23 | 20 x2 | 25 | 23 | 16 x3 | 爆发CR25 HP中位/均值 553/553 AC中位 23；持续CR23 HP中位/均值 468/444.8 AC中位 22 |

High-CR warning: XMM currently has very few samples at some high CRs. CR18, CR19, CR25, and CR30 are especially thin in this extraction. Use those rows as reference anchors, not as proof that one specific monster's HP should define the whole tier.

## XMM CR Stats

| CR | XP | XMM样本 | HP中位 | HP均值 | AC中位 |
|---:|---:|---:|---:|---:|---:|
| 1/8 | 25 | 24 | 8 | 8.5 | 12 |
| 1/4 | 50 | 44 | 13 | 13.7 | 12.5 |
| 1/2 | 100 | 34 | 19 | 20.4 | 12 |
| 1 | 200 | 41 | 26 | 28.9 | 13 |
| 2 | 450 | 59 | 45 | 46.2 | 13 |
| 3 | 700 | 41 | 65 | 62.7 | 14 |
| 4 | 1100 | 27 | 71 | 70.9 | 15 |
| 5 | 1800 | 36 | 93.5 | 98.9 | 15 |
| 6 | 2300 | 23 | 112 | 109 | 16 |
| 7 | 2900 | 16 | 126.5 | 128.4 | 16 |
| 8 | 3900 | 23 | 136 | 135 | 16 |
| 9 | 5000 | 12 | 156.5 | 157.8 | 17.5 |
| 10 | 5900 | 16 | 161.5 | 170.7 | 18 |
| 11 | 7200 | 12 | 197 | 194.1 | 17 |
| 12 | 8400 | 7 | 182 | 188 | 18 |
| 13 | 10000 | 9 | 195 | 200.2 | 18 |
| 14 | 11500 | 4 | 195 | 200.5 | 18.5 |
| 15 | 13000 | 6 | 209.5 | 216 | 18 |
| 16 | 15000 | 7 | 255 | 240.1 | 19 |
| 17 | 18000 | 7 | 256 | 255.4 | 20 |
| 18 | 20000 | 1 | 180 | 180 | 20 |
| 19 | 22000 | 1 | 287 | 287 | 19 |
| 20 | 25000 | 4 | 332.5 | 331.2 | 20 |
| 21 | 33000 | 5 | 333 | 335.8 | 21 |
| 22 | 41000 | 3 | 444 | 405.3 | 22 |
| 23 | 50000 | 5 | 468 | 444.8 | 22 |
| 24 | 62000 | 2 | 526.5 | 526.5 | 22 |
| 25 | 75000 | 1 | 553 | 553 | 23 |
| 30 | 155000 | 1 | 697 | 697 | 25 |

## Damage Rank Mapping Draft

These percentages are intended for expected damage, not all-hit ceiling. If only an all-hit ceiling is known, write that clearly and do not rank it as stable DPR.

### Sustained Single-Target DPR

Use percentage of the `持续CR` reference monster's HP removed per round.

| Rank | Expected DPR as reference HP percentage |
|---|---:|
| EX | 45%+ |
| S+ | 33-44% |
| S | 25-32% |
| S- | 20-24% |
| A+ | 16.7-19% |
| A | 12.5-16.6% |
| A- | 10-12.4% |
| B+ | 8.3-9.9% |
| B | 6.5-8.2% |
| C | 4.5-6.4% |
| D | 3-4.4% |
| E | 1-2.9% |
| E- | Nonzero but below 1% |
| F | No meaningful DPR line |

### Burst Single-Target DPR

Use percentage of the `爆发CR` reference monster's HP removed in the burst turn.

| Rank | Expected burst damage as reference HP percentage |
|---|---:|
| EX | 100%+ |
| S+ | 75-99% |
| S | 55-74% |
| S- | 40-54% |
| A+ | 30-39% |
| A | 22-29% |
| A- | 16.7-21% |
| B+ | 12.5-16.6% |
| B | 8.3-12.4% |
| C | 5-8.2% |
| D | 3-4.9% |
| E | 1-2.9% |
| E- | Nonzero but below 1% |
| F | No meaningful burst |

### AoE DPR

AoE DPR should be scored by total expected enemy HP removed, then reduced for target-count reliability.

| Rank | Expected AoE damage as total reference HP percentage |
|---|---:|
| EX | 100%+ of the whole reference group |
| S+ | 75-99% |
| S | 55-74% |
| S- | 40-54% |
| A+ | 30-39% |
| A | 22-29% |
| A- | 16.7-21% |
| B+ | 12.5-16.6% |
| B | 8.3-12.4% |
| C | 5-8.2% |
| D | 3-4.9% |
| E | 1-2.9% |
| E- | Nonzero but below 1% |
| F | No meaningful AoE damage |

AoE target-count defaults:

- `近距范围DPR`: default 2 meaningful targets.
- `远程范围DPR`: default 3 meaningful targets.
- If the effect is no-friendly-fire, huge-radius, selective, repeatable, or has forced-movement abuse, mention a higher ceiling separately.
- If the effect is small, self-centered, melee-only, enemy-placement-dependent, friendly-fire-heavy, or bounce-dependent, reduce the practical rank even when the all-hit math is high.

## ASI, Feat, And Attack Bonus Profiles

ASI / damage attribute growth must be part of the model. Damage rankings should not assume both perfect feat stacking and perfect ability-score progression unless the build actually has the ASI economy to support it.

| Profile | Main stat assumption | Use case |
|---|---|---|
| 基础成长 | +3 at level 1, +4 at level 4, +5 at level 8 | Rules-math baseline; matches ordinary attack/DC growth. |
| 2024专长成长 | Half-feats or class ASIs keep main stat near baseline while adding a key feat | Common optimized 2024 build path. |
| 延迟属性 | Feats delay +4 or +5 main stat | Feat-heavy martial/gish routes; lower hit chance and flat damage must be counted. |
| 魔法物品修正 | Add +1/+2/+3 to attack/damage or spell attack/DC only when item supports it | Use with item profiles below. |

Attack-roll reference:

- Baseline attack math assumes roughly 65% hit chance against level/CR-appropriate AC.
- If a build delays the attack stat, uses a penalty, lacks proficiency, or attacks a higher-AC reference monster, calculate directly.
- If a build has advantage, rerolls, forced failed saves, or attack-result replacement, calculate that explicitly instead of applying a flat rank bump.

## Magic Item Profiles

These profiles are for DPR calibration only. They are not promises that every table grants the exact item.

| Profile | Weapon / focus expectation | Ranking use |
|---|---|---|
| 保守 | No assumed +X weapon/focus; only class-granted magic weapons/items count | Low-magic tables, early Tier 1, or when item access is uncertain. |
| 默认 | Tier 2 can plausibly have a +1 weapon/focus; Tier 3 can plausibly have +1/+2; Tier 4 can plausibly have +2 and sometimes +3 | Default project math when a class needs ordinary item support to function, especially weapon users. |
| 慷慨 | Tier 2 +1, Tier 3 +2, Tier 4 +3 if rarity and campaign assumptions support it | High-magic or optimization-assumed tables; do not use as default without saying so. |

Separate item types:

- `+X weapon`: adds to attack and damage for that weapon, affects expected DPR strongly.
- `+X spell attack / DC focus`: affects spell attacks and saving throw success, but does not add damage unless the item says so.
- `魔咒武器`, damage-rider items, ammunition, poisons, scrolls, and charged items must be modeled as their own resources, not folded into generic +X.

## Upper-Limit Sanity Anchors

These are current project sanity checks, not rank rules:

- Level 20 Wizard, 9th-level `咒唤微元素群` + 8th-level `灼热射线`: all-hit ceiling around 346.5 before hit chance.
- Valor Bard 16 / Warlock 2 / Fighter 2 with 8th-level `咒唤微元素群`, 7th-level `灼热射线`, `魔能爆`, and `动作如潮`: all-hit ceiling can reach roughly 600 in ideal conditions, but it is close-range, resource-heavy, setup-dependent, and not a normal sustained line.
- Level 20 Eldritch Knight polearm burst is around the 200 all-hit band depending assumptions, much lower than top full-caster CME nova but more weapon-line repeatable.

When a build exceeds these anchors, verify:

- whether the calculation used expected damage or all-hit ceiling;
- whether the setup was legal under the one-slot-spell-per-turn rule;
- whether concentration was already active;
- whether resources were long-rest, short-rest, or at-will;
- whether target distance was 5/10/15 ft, 30 ft, 60 ft, or longer;
- whether the target can realistically be reached and kept in range.

## How To Use In Reviews

1. Choose the relevant category: near/ranged, burst/sustained/AoE.
2. Calculate expected DPR against the reference AC, not only all-hit damage.
3. Convert expected damage to percentage of reference HP.
4. Apply the rank table as a starting point.
5. Adjust down or up only with stated reasons: setup, concentration, target access, resource repeatability, defensive risk, enemy packing, friendly fire, save/attack reliability, item dependence, and whether the routine also brings control or party leverage.
6. Do not use DPR rank to force overall rank. Overall rank still weighs control, anti-caster value, team defense, healing, summoning, battlefield division, skill utility, and high-level problem solving more heavily than raw damage.
