# DPR Calibration Matrix

> Generated calibration data. `阈值评级` is raw HP-percentage pressure; `默认校准评级` excludes specific rare/very rare/legendary item assumptions; `上限评级` is for item/condition ceiling branches only.

## Calibration Rules

- EX is assigned by horizontal dominance, not by a fixed HP percentage. A row must be at least S by threshold and at least 1.5x the next comparable same-level/category row.
- `幻影师护臂` is only an item-ceiling assumption. It can create EX ceiling evidence, but does not change default ranks.
- Vex-derived benchmark rows are excluded from this matrix, although the calculator still supports Vex chains.
- Great Weapon Master is modeled as per qualifying Attack-action hit. It is not applied to Polearm Master or Illusionist's Bracers bonus-action hits.
- Great Weapon Fighting is modeled with the broad benchmark reading: eligible attack damage dice of 1-2 count as 3. This is table-sensitive when applied to rider dice.

| Level | Category | Option | Variant | Routine | Ref CR | HP x Targets | AC | All-hit | Expected | % HP | 阈值评级 | Dominance | 默认校准评级 | 上限评级 | Assumptions |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|
| 9 | ranged_aoe | Light Cleric 9 Fireball | default | Light Cleric 9 Fireball | 6 | 112 x 3 | 16 | 84.00 | 71.40 | 21.2% | A- | - | A- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 13 | close_aoe | Druid 13 Conjure Woodland Beings Movement | default | Druid 13 Conjure Woodland Beings Movement | 12 | 182 x 2 | 18 | 45.00 | 34.88 | 9.6% | B | - | B | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Eldritch Knight 20 Greatsword GWM | condition_ceiling | Eldritch Knight 20 Vorpal Greatsword CME8 Bracers Booming Blade Paralyzed | 25 | 553 x 1 | 23 | 1148.25 | 971.73 | 175.7% | EX | - | - | EX | 状态上限：依赖目标已有关键状态或外部配合，仅用于上限说明。 |
| 20 | close_burst | Champion 20 Polearm GWF GWM/PAM | condition_ceiling | Champion 20 Vorpal Polearm CME8 Paralyzed | 25 | 553 x 1 | 23 | 1046.60 | 961.14 | 173.8% | EX | - | - | EX | 状态上限：依赖目标已有关键状态或外部配合，仅用于上限说明。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | condition_ceiling | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Vorpal Dual Scimitar Paralyzed | 25 | 553 x 1 | 23 | 1302.00 | 936.36 | 169.3% | EX | - | - | EX | 状态上限：依赖目标已有关键状态或外部配合，仅用于上限说明。 |
| 20 | close_burst | Fighter 20 Polearm GWF GWM/PAM | condition_ceiling | Fighter 20 Vorpal Polearm CME8 Paralyzed | 25 | 553 x 1 | 23 | 1046.60 | 886.34 | 160.3% | EX | - | - | EX | 状态上限：依赖目标已有关键状态或外部配合，仅用于上限说明。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | default | Valor Bard16 Warlock2 Fighter2 CME Turret Dual Scimitar | 25 | 553 x 1 | 23 | 528.50 | 262.50 | 47.5% | S- | 1.52x | S- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Wizard 20 CME9 + Scorching Ray8 | default | Wizard 20 CME9 + Scorching Ray8 | 25 | 553 x 1 | 23 | 346.50 | 173.25 | 31.3% | A+ | - | A+ | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Eldritch Knight 20 Polearm GWF GWM/PAM CME4 True Strike | default | Eldritch Knight 20 Polearm GWF GWM/PAM CME4 True Strike | 25 | 553 x 1 | 23 | 269.80 | 155.00 | 28.0% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Battle Master 20 Polearm GWF GWM/PAM | default | Battle Master 20 Polearm GWF GWM/PAM | 25 | 553 x 1 | 23 | 197.05 | 125.06 | 22.6% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Champion 20 Polearm GWF GWM/PAM | default | Champion 20 Polearm GWF GWM/PAM | 25 | 553 x 1 | 23 | 158.05 | 113.12 | 20.5% | A- | - | A- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Paladin 20 Greatsword GWM | default | Paladin 20 Greatsword GWF GWM Spirit Shroud Searing Smite5 Graze | 25 | 553 x 1 | 23 | 111.25 | 72.59 | 13.1% | B+ | - | B+ | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Champion 20 Polearm GWF GWM/PAM | item_ceiling | Champion 20 Vorpal Polearm CME8 | 25 | 553 x 1 | 23 | 448.30 | 414.11 | 74.9% | S | 1.18x | - | S | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_burst | Eldritch Knight 20 Greatsword GWM | item_ceiling | Eldritch Knight 20 Vorpal Greatsword CME8 Bracers Booming Blade | 25 | 553 x 1 | 23 | 499.12 | 349.93 | 63.3% | S | - | - | S | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | item_ceiling | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Vorpal Dual Scimitar | 25 | 553 x 1 | 23 | 649.00 | 336.25 | 60.8% | S | - | - | S | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | item_ceiling | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar | 25 | 553 x 1 | 23 | 643.00 | 319.00 | 57.7% | S | - | - | S | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_burst | Fighter 20 Polearm GWF GWM/PAM | item_ceiling | Fighter 20 Vorpal Polearm CME8 | 25 | 553 x 1 | 23 | 448.30 | 316.89 | 57.3% | S | - | - | S | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | item_ceiling | Valor Bard16 Warlock2 Fighter2 CME Turret Vorpal Dual Scimitar | 25 | 553 x 1 | 23 | 537.50 | 288.38 | 52.1% | S- | - | - | S- | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_sustained | Noble Genies Paladin 20 Dual Wield CME5 Divine Favor | default | Noble Genies Paladin 20 Dual Wield CME5 Divine Favor | 23 | 468 x 1 | 22 | 116.00 | 74.40 | 15.9% | A | 1.02x | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_sustained | Berserker Barbarian 20 GWF GWM Graze | default | Berserker Barbarian 20 GWF GWM Graze | 23 | 468 x 1 | 22 | 82.00 | 72.68 | 15.5% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_sustained | Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor | default | Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor | 23 | 468 x 1 | 22 | 76.00 | 69.30 | 14.8% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_sustained | Hunter Ranger 20 Dual Wield Hunter's Mark | default | Hunter Ranger 20 Dual Wield Hunter's Mark | 23 | 468 x 1 | 22 | 48.00 | 30.20 | 6.5% | C | - | C | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | ranged_sustained | Warlock 20 Eldritch Blast Hex | default | Warlock 20 Eldritch Blast Hex | 23 | 468 x 1 | 22 | 56.00 | 29.80 | 6.4% | C | - | C | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | ranged_sustained | Warlock 20 Eldritch Blast Hex | item_ceiling | Warlock 20 Eldritch Blast Hex Bracers | 23 | 468 x 1 | 22 | 112.00 | 59.60 | 12.7% | A | 2.00x | - | A | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |

## Calculation Details

### Lv9 Light Cleric 9 Fireball

- Option: Light Cleric 9 Fireball
- Variant: default
- Calculation: 1x 3rd-level Fireball, 8d6, Dex half, 3 targets vs 3 targets
- Notes: Uses the ranged AoE default of three meaningful targets. Resources: 3rd-level slot

### Lv13 Druid 13 Conjure Woodland Beings Movement

- Option: Druid 13 Conjure Woodland Beings Movement
- Variant: default
- Calculation: 1x Conjure Woodland Beings, 5d8, Wis half, 2 targets vs 2 targets
- Notes: This is movement/table-position sensitive and should not be treated as automatic multi-hit damage. Resources: 4th-level slot, concentration, movement access

### Lv20 Eldritch Knight 20 Vorpal Greatsword CME8 Bracers Booming Blade Paralyzed

- Option: Eldritch Knight 20 Greatsword GWM
- Variant: condition_ceiling
- Calculation: 6x Paralyzed target: Vorpal Greatsword Attack-action hits, 6 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8; 2x Paralyzed target: Attack-action Booming Blade replacements, 2 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8 + 3d8 thunder; 1x Paralyzed target: Illusionist's Bracers bonus-action Booming Blade, 2d6 GWF + STR + Vorpal + CME8 + 3d8 thunder
- Notes: Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Illusionist's Bracers. The ordinary EK row remains PHB 2024 True Strike; Booming Blade is used only for this non-PHB item-ceiling case. GWM damage applies to Attack-action hits only, not the Bracers bonus-action Booming Blade. Only Booming Blade's on-hit thunder damage is counted; target movement damage is excluded. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. CME and Booming Blade dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit. Flat damage is not doubled; all damage dice on the attack are doubled. Graze miss damage still applies on misses but does not trigger CME, Booming Blade, Vorpal, or GWM. Resources: Enspelled Weapon: CME8, Vorpal Greatsword, Illusionist's Bracers, Action Surge, Great Weapon Fighting, Great Weapon Master, Weapon Mastery: Graze, War Magic, Booming Blade, concentration, 3 attunements, Paralyzed target

### Lv20 Champion 20 Vorpal Polearm CME8 Paralyzed

- Option: Champion 20 Polearm GWF GWM/PAM
- Variant: condition_ceiling
- Calculation: 7x Paralyzed target: Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8; 1x Paralyzed target: Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8; 1x Paralyzed target: Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8; Champion Heroic Inspiration rerolls one missed attack against Paralyzed target, trigger chance 0.792
- Notes: Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Vorpal Glaive. GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. CME dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Champion level 10+ is modeled as spending one Heroic Inspiration reroll on the first missed attack in the burst turn. Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit. Flat damage is not doubled; all damage dice on the attack are doubled. Graze miss damage still applies on misses but does not trigger CME, Vorpal, or GWM. Resources: Enspelled Weapon: CME8, Vorpal Greatsword, Vorpal Glaive, Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze, concentration, 3 attunements, Paralyzed target

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Vorpal Dual Scimitar Paralyzed

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: condition_ceiling
- Calculation: 8x Paralyzed target: 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Paralyzed target: Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Paralyzed target: Action Surge Attack action: Vorpal main-hand scimitar, 1d6 + 8 + 6d8; 1x Paralyzed target: Action Surge Attack action: Vorpal Nick off-hand scimitar, 1d6 + 8 + 6d8; 4x Paralyzed target: Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8
- Notes: Extreme item-dependent branch with exactly three attunements: Illusionist's Bracers and two Vorpal Scimitars. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit. Flat damage is not doubled; all damage dice on the attack are doubled. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Vorpal Scimitar x2, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration, 3 attunements, Paralyzed target

### Lv20 Fighter 20 Vorpal Polearm CME8 Paralyzed

- Option: Fighter 20 Polearm GWF GWM/PAM
- Variant: condition_ceiling
- Calculation: 7x Paralyzed target: Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8; 1x Paralyzed target: Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8; 1x Paralyzed target: Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8
- Notes: Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Vorpal Glaive. This is a no-subclass Fighter comparison row with no Champion crit expansion or Heroic Inspiration reroll. GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. CME dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit. Flat damage is not doubled; all damage dice on the attack are doubled. Graze miss damage still applies on misses but does not trigger CME, Vorpal, or GWM. Resources: Enspelled Weapon: CME8, Vorpal Greatsword, Vorpal Glaive, Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze, concentration, 3 attunements, Paralyzed target

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Dual Scimitar

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: default
- Calculation: 8x 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8; 1x Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8; 1x Bonus-action off-hand scimitar, 1d6 + 5 + 6d8
- Notes: Default optimized branch without Illusionist's Bracers. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Three scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. No Advantage, paralysis, or prior Vex is assumed. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration

### Lv20 Wizard 20 CME9 + Scorching Ray8

- Option: Wizard 20 CME9 + Scorching Ray8
- Variant: default
- Calculation: 9x 8th-level Scorching Ray, 9 rays, 2d6 + 7d8
- Notes: All-hit ceiling anchor is 346.5 before hit chance. Resources: 9th-level slot: CME, 8th-level slot: Scorching Ray, concentration

### Lv20 Eldritch Knight 20 Polearm GWF GWM/PAM CME4 True Strike

- Option: Eldritch Knight 20 Polearm GWF GWM/PAM CME4 True Strike
- Variant: default
- Calculation: 5x Greatsword Attack-action hits, 5 attacks, 2d6 GWF + STR + GWM + CME4; 2x Greatsword True Strike replacements, 2 attacks, 2d6 GWF + STR + GWM + CME4 + 3d6 radiant; 1x Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM + CME4; 1x Polearm Master bonus attack, 1d4 GWF + STR + CME4
- Notes: This ordinary EK row uses PHB 2024 True Strike rather than Booming Blade. GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. CME and True Strike dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Graze miss damage is Strength modifier only and does not trigger CME, True Strike, or GWM. Resources: 4th-level slot: CME, Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze, War Magic, True Strike, concentration

### Lv20 Battle Master 20 Polearm GWF GWM/PAM

- Option: Battle Master 20 Polearm GWF GWM/PAM
- Variant: default
- Calculation: 7x Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + GWM; 1x Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM; 1x Polearm Master bonus attack, 1d4 GWF + STR; Superiority dice spent on successful hits, up to 6d12, 3.99/6 dice expected
- Notes: GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3. Graze miss damage is Strength modifier only and does not trigger GWM. Superiority dice are modeled as a limited pool spent only on successful hits. Resources: Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze, superiority dice

### Lv20 Champion 20 Polearm GWF GWM/PAM

- Option: Champion 20 Polearm GWF GWM/PAM
- Variant: default
- Calculation: 7x Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + GWM; 1x Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM; 1x Polearm Master bonus attack, 1d4 GWF + STR; Champion Heroic Inspiration rerolls one missed attack, trigger chance 0.999
- Notes: GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3. Graze miss damage is Strength modifier only and does not trigger GWM. Champion level 15+ crits on 18-20 with weapon attacks and Unarmed Strikes. Champion level 10+ is modeled as spending one Heroic Inspiration reroll on the first missed attack in the burst turn. Resources: Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze

### Lv20 Paladin 20 Greatsword GWF GWM Spirit Shroud Searing Smite5 Graze

- Option: Paladin 20 Greatsword GWM
- Variant: default
- Calculation: 2x Greatsword Attack-action hits, 2 attacks, 2d6 GWF + STR + GWM + Radiant Strikes + Spirit Shroud5 + Divine Favor; 5th-level Searing Smite initial and guaranteed burn damage, 10d6 if any greatsword attack hits if trigger chance 0.750
- Notes: Searing Smite is modeled as two guaranteed 5d6 damage packets after a hit: the initial rider and the follow-up burn; only the initial hit-linked packet uses the broad GWF dice-floor benchmark. If every greatsword attack misses, Searing Smite is not cast and adds no damage. Graze miss damage does not trigger Searing Smite, Spirit Shroud, Radiant Strikes, or Great Weapon Master. GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3. Resources: 5th-level slot: Spirit Shroud, Divine Favor, 5th-level slot: Searing Smite, Great Weapon Fighting, Great Weapon Master, Weapon Mastery: Graze, concentration

### Lv20 Champion 20 Vorpal Polearm CME8

- Option: Champion 20 Polearm GWF GWM/PAM
- Variant: item_ceiling
- Calculation: 7x Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8; 1x Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8; 1x Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8; Champion Heroic Inspiration rerolls one missed attack, trigger chance 0.990
- Notes: Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Vorpal Glaive. GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. CME dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Champion level 10+ is modeled as spending one Heroic Inspiration reroll on the first missed attack in the burst turn. Resources: Enspelled Weapon: CME8, Vorpal Greatsword, Vorpal Glaive, Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze, concentration, 3 attunements

### Lv20 Eldritch Knight 20 Vorpal Greatsword CME8 Bracers Booming Blade

- Option: Eldritch Knight 20 Greatsword GWM
- Variant: item_ceiling
- Calculation: 6x Vorpal Greatsword Attack-action hits, 6 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8; 2x Attack-action Booming Blade replacements, 2 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8 + 3d8 thunder; 1x Illusionist's Bracers bonus-action Booming Blade, 2d6 GWF + STR + Vorpal + CME8 + 3d8 thunder
- Notes: Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Illusionist's Bracers. The ordinary EK row remains PHB 2024 True Strike; Booming Blade is used only for this non-PHB item-ceiling case. GWM damage applies to Attack-action hits only, not the Bracers bonus-action Booming Blade. Only Booming Blade's on-hit thunder damage is counted; target movement damage is excluded. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. CME and Booming Blade dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Resources: Enspelled Weapon: CME8, Vorpal Greatsword, Illusionist's Bracers, Action Surge, Great Weapon Fighting, Great Weapon Master, Weapon Mastery: Graze, War Magic, Booming Blade, concentration, 3 attunements

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Vorpal Dual Scimitar

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: item_ceiling
- Calculation: 8x 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Action Surge Attack action: Vorpal main-hand scimitar, 1d6 + 8 + 6d8; 1x Action Surge Attack action: Vorpal Nick off-hand scimitar, 1d6 + 8 + 6d8; 4x Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8
- Notes: Extreme item-dependent branch with exactly three attunements: Illusionist's Bracers and two Vorpal Scimitars. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. No Advantage, paralysis, or prior Vex is assumed. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Vorpal Scimitar x2, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration, 3 attunements

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: item_ceiling
- Calculation: 8x 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8; 1x Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8; 4x Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8
- Notes: Extreme item-dependent branch. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. No Advantage, paralysis, or prior Vex is assumed. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration

### Lv20 Fighter 20 Vorpal Polearm CME8

- Option: Fighter 20 Polearm GWF GWM/PAM
- Variant: item_ceiling
- Calculation: 7x Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8; 1x Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8; 1x Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8
- Notes: Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Vorpal Glaive. This is a no-subclass Fighter comparison row with no Champion crit expansion or Heroic Inspiration reroll. GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. CME dice are included in the broad GWF dice-floor benchmark; this is table-sensitive. Resources: Enspelled Weapon: CME8, Vorpal Greatsword, Vorpal Glaive, Action Surge, Great Weapon Fighting, Great Weapon Master, Polearm Master, Weapon Mastery: Graze, concentration, 3 attunements

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Vorpal Dual Scimitar

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: item_ceiling
- Calculation: 8x 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Action Surge Attack action: Vorpal main-hand scimitar, 1d6 + 8 + 6d8; 1x Action Surge Attack action: Vorpal Nick off-hand scimitar, 1d6 + 8 + 6d8; 1x Bonus-action Vorpal off-hand scimitar, 1d6 + 8 + 6d8
- Notes: Item-dependent branch with two Vorpal Scimitars and no Illusionist's Bracers. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Three scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded. No Advantage, paralysis, or prior Vex is assumed. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Vorpal Scimitar x2, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration, 2 attunements

### Lv20 Noble Genies Paladin 20 Dual Wield CME5 Divine Favor

- Option: Noble Genies Paladin 20 Dual Wield CME5 Divine Favor
- Variant: default
- Calculation: 4x Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 3d8 + 1d4
- Notes: Close-range concentration branch; lower hit count than full-caster ray/EB CME routines. Resources: 5th-level slot: CME, Divine Favor, concentration, Nick, Dual Wielder

### Lv20 Berserker Barbarian 20 GWF GWM Graze

- Option: Berserker Barbarian 20 GWF GWM Graze
- Variant: default
- Calculation: 2x Reckless greatsword Attack-action hits, 2 attacks, 2d6 GWF + STR + Rage + GWM + Frenzy
- Notes: Frenzy dice are folded into the event as once-per-turn damage. GWM damage applies to Attack-action hits. Graze miss damage is modeled as Strength modifier only; Rage, GWM, and Frenzy are not added to Graze. GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3. Resources: Rage, Reckless Attack, Great Weapon Fighting, Great Weapon Master, Weapon Mastery: Graze

### Lv20 Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor

- Option: Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor
- Variant: default
- Calculation: 4x Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 1d6 + 1d4
- Notes: This is a sustained weapon-rider branch, not a smite nova branch. Resources: Hunter's Mark, Divine Favor, Vow of Enmity, Nick, Dual Wielder

### Lv20 Hunter Ranger 20 Dual Wield Hunter's Mark

- Option: Hunter Ranger 20 Dual Wield Hunter's Mark
- Variant: default
- Calculation: 4x Dual-wield hits, 4 hits, 1d6 + 5 + 1d6
- Notes: Subclass damage riders are not included; use as a Ranger floor branch. Resources: Hunter's Mark, Nick, Dual Wielder

### Lv20 Warlock 20 Eldritch Blast Hex

- Option: Warlock 20 Eldritch Blast Hex
- Variant: default
- Calculation: 4x Eldritch Blast, 4 beams, 1d10 + 5 + 1d6
- Notes: Resources: Hex, concentration, Agonizing Blast

### Lv20 Warlock 20 Eldritch Blast Hex Bracers

- Option: Warlock 20 Eldritch Blast Hex
- Variant: item_ceiling
- Calculation: 8x Eldritch Blast action plus Illusionist's Bracers bonus action, 8 beams, 1d10 + 5 + 1d6
- Notes: Item-ceiling sustained branch; not part of default Warlock DPR ranking. Resources: Hex, concentration, Agonizing Blast, Illusionist's Bracers
