# DPR Calibration Matrix

> Generated calibration data. `阈值评级` is raw HP-percentage pressure; `默认校准评级` excludes specific rare/very rare/legendary item assumptions; `上限评级` is for item/condition ceiling branches only.

## Calibration Rules

- EX is assigned by horizontal dominance, not by a fixed HP percentage. A row must be at least S by threshold and at least 1.5x the next comparable same-level/category row.
- `幻影师护臂` is only an item-ceiling assumption. It can create EX ceiling evidence, but does not change default ranks.
- Vex-derived benchmark rows are excluded from this matrix, although the calculator still supports Vex chains.

| Level | Category | Option | Variant | Routine | Ref CR | HP x Targets | AC | All-hit | Expected | % HP | 阈值评级 | Dominance | 默认校准评级 | 上限评级 | Assumptions |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|
| 9 | ranged_aoe | Light Cleric 9 Fireball | default | Light Cleric 9 Fireball | 6 | 112 x 3 | 16 | 84.00 | 71.40 | 21.2% | A- | - | A- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 13 | close_aoe | Druid 13 Conjure Woodland Beings Movement | default | Druid 13 Conjure Woodland Beings Movement | 12 | 182 x 2 | 18 | 45.00 | 34.88 | 9.6% | B | - | B | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | condition_ceiling | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar Paralyzed | 25 | 553 x 1 | 23 | 1236.00 | 862.11 | 155.9% | EX | - | - | EX | 状态上限：依赖目标已有关键状态或外部配合，仅用于上限说明。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | default | Valor Bard16 Warlock2 Fighter2 CME Turret Dual Scimitar | 25 | 553 x 1 | 23 | 528.50 | 262.50 | 47.5% | S- | 1.52x | S- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Wizard 20 CME9 + Scorching Ray8 | default | Wizard 20 CME9 + Scorching Ray8 | 25 | 553 x 1 | 23 | 346.50 | 173.25 | 31.3% | A+ | - | A+ | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Eldritch Knight 20 Greatsword GWM | default | Eldritch Knight 20 Greatsword GWM CME4 Graze | 25 | 553 x 1 | 23 | 216.00 | 125.60 | 22.7% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Battle Master 20 Polearm Surge | default | Battle Master 20 Polearm Surge | 25 | 553 x 1 | 23 | 184.50 | 121.35 | 21.9% | A- | - | A- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Eldritch Knight 20 Polearm | default | Eldritch Knight 20 Polearm CME4 | 25 | 553 x 1 | 23 | 226.50 | 108.30 | 19.6% | A- | - | A- | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Eldritch Knight 20 Polearm Spirit Shroud | default | Eldritch Knight 20 Polearm Spirit Shroud | 25 | 553 x 1 | 23 | 186.00 | 88.05 | 15.9% | B+ | - | B+ | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Champion 20 Polearm Surge | default | Champion 20 Polearm Surge | 25 | 553 x 1 | 23 | 145.50 | 87.00 | 15.7% | B+ | - | B+ | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Paladin 20 Greatsword GWM | default | Paladin 20 Greatsword GWM Spirit Shroud Searing Smite5 Graze | 25 | 553 x 1 | 23 | 103.00 | 76.50 | 13.8% | B+ | - | B+ | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_burst | Valor Bard16 / Warlock2 / Fighter2 CME Turret | item_ceiling | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar | 25 | 553 x 1 | 23 | 643.00 | 319.00 | 57.7% | S | 1.22x | - | S | 物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。 |
| 20 | close_sustained | Noble Genies Paladin 20 Dual Wield CME5 Divine Favor | default | Noble Genies Paladin 20 Dual Wield CME5 Divine Favor | 23 | 468 x 1 | 22 | 116.00 | 74.40 | 15.9% | A | 1.07x | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_sustained | Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor | default | Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor | 23 | 468 x 1 | 22 | 76.00 | 69.30 | 14.8% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
| 20 | close_sustained | Berserker Barbarian 20 GWM | default | Berserker Barbarian 20 GWM | 23 | 468 x 1 | 22 | 72.00 | 64.08 | 13.7% | A | - | A | - | 默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。 |
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

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar Paralyzed

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: condition_ceiling
- Calculation: 8x Paralyzed target: 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Paralyzed target: Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Paralyzed target: Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8; 1x Paralyzed target: Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8; 4x Paralyzed target: Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8
- Notes: Extreme item-dependent branch. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit. Flat damage is not doubled; all damage dice on the attack are doubled. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration, Paralyzed target

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

### Lv20 Eldritch Knight 20 Greatsword GWM CME4 Graze

- Option: Eldritch Knight 20 Greatsword GWM
- Variant: default
- Calculation: 8x Greatsword attacks with Action Surge, 8 hits, 2d6 + 11 + 2d8
- Notes: Graze miss damage is only the Strength modifier and does not count as a hit. CME is not added to Graze damage because a missed attack is not a hit. Resources: 4th-level slot: CME, Action Surge, Great Weapon Master, Weapon Mastery: Graze, concentration

### Lv20 Battle Master 20 Polearm Surge

- Option: Battle Master 20 Polearm Surge
- Variant: default
- Calculation: 8x Main polearm attacks with Action Surge, 8 hits, 1d10 + 11; 1x Polearm Master bonus attack, 1d4 + 11; 1x Superiority dice spent on hits, 6d12
- Notes: Maneuver dice are modeled as spent on successful hits, not as separate attack rolls. Resources: Action Surge, Polearm Master, Great Weapon Master, superiority dice

### Lv20 Eldritch Knight 20 Polearm CME4

- Option: Eldritch Knight 20 Polearm
- Variant: default
- Calculation: 8x Main polearm attacks with Action Surge, 8 hits, 1d10 + 11 + 2d8; 1x Polearm Master bonus attack, 1d4 + 11 + 2d8
- Notes: CME adds 2d8 per hit at 4th level but requires targets within 15 feet. Resources: 4th-level slot: CME, Action Surge, Polearm Master, Great Weapon Master, concentration

### Lv20 Eldritch Knight 20 Polearm Spirit Shroud

- Option: Eldritch Knight 20 Polearm Spirit Shroud
- Variant: default
- Calculation: 8x Main polearm attacks with Action Surge, 8 hits, 1d10 + 11 + 1d8; 1x Polearm Master bonus attack, 1d4 + 11 + 1d8
- Notes: EK's 4th-level Spirit Shroud remains 1d8; this is a martial burst anchor. Resources: 4th-level slot: Spirit Shroud, Action Surge, Polearm Master, Great Weapon Master

### Lv20 Champion 20 Polearm Surge

- Option: Champion 20 Polearm Surge
- Variant: default
- Calculation: 8x Main polearm attacks with Action Surge, 8 hits, 1d10 + 11; 1x Polearm Master bonus attack, 1d4 + 11
- Notes: Champion level 15+ crits on 18-20 with weapon attacks and Unarmed Strikes. Resources: Action Surge, Polearm Master, Great Weapon Master

### Lv20 Paladin 20 Greatsword GWM Spirit Shroud Searing Smite5 Graze

- Option: Paladin 20 Greatsword GWM
- Variant: default
- Calculation: 2x Greatsword attacks, 2 hits, 2d6 + 5 + 1d8 + 2d8 + 1d4; 5th-level Searing Smite initial and guaranteed burn damage, 10d6 if any greatsword attack hits if trigger chance 0.840
- Notes: Searing Smite is modeled as two guaranteed 5d6 damage packets after a hit: the initial rider and the follow-up burn. If every greatsword attack misses, Searing Smite is not cast and adds no damage. Graze miss damage does not trigger Searing Smite, Spirit Shroud, Radiant Strikes, or Great Weapon Master. Resources: 5th-level slot: Spirit Shroud, Divine Favor, 5th-level slot: Searing Smite, Great Weapon Master, Weapon Mastery: Graze, concentration

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar

- Option: Valor Bard16 / Warlock2 / Fighter2 CME Turret
- Variant: item_ceiling
- Calculation: 8x 7th-level Scorching Ray, 8 rays, 2d6 + 6d8; 4x Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8; 1x Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8; 1x Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8; 4x Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8
- Notes: Extreme item-dependent branch. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage. Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style. No Advantage, paralysis, or prior Vex is assumed. Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration

### Lv20 Noble Genies Paladin 20 Dual Wield CME5 Divine Favor

- Option: Noble Genies Paladin 20 Dual Wield CME5 Divine Favor
- Variant: default
- Calculation: 4x Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 3d8 + 1d4
- Notes: Close-range concentration branch; lower hit count than full-caster ray/EB CME routines. Resources: 5th-level slot: CME, Divine Favor, concentration, Nick, Dual Wielder

### Lv20 Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor

- Option: Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor
- Variant: default
- Calculation: 4x Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 1d6 + 1d4
- Notes: This is a sustained weapon-rider branch, not a smite nova branch. Resources: Hunter's Mark, Divine Favor, Vow of Enmity, Nick, Dual Wielder

### Lv20 Berserker Barbarian 20 GWM

- Option: Berserker Barbarian 20 GWM
- Variant: default
- Calculation: 2x Reckless greatsword attacks, 2 hits, 2d6 + STR + Rage + GWM + Frenzy
- Notes: Frenzy dice are folded into the event as once-per-turn damage. Graze miss damage is modeled as Strength modifier only; Rage, GWM, and Frenzy are not added to Graze. Resources: Rage, Reckless Attack, Great Weapon Master

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
