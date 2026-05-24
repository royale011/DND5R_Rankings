# DPR Calculated Benchmarks

> Generated report. Treat `rank_pressure` as math pressure, not final review rank.

| Level | Category | Routine | Ref CR | Ref HP x Targets | AC | All-hit | Expected | % HP | Rank pressure | Setup | Recovery |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 9 | ranged_aoe | Light Cleric 9 Fireball | 6 | 112 x 3 | 16 | 84.00 | 71.40 | 21.2% | A- | cold_start: Fireball is cast in the burst turn. | long_rest |
| 13 | close_aoe | Druid 13 Conjure Woodland Beings Movement | 12 | 182 x 2 | 18 | 45.00 | 34.88 | 9.6% | B | prebuffed: The emanation is already active and the Druid can move through two targets. | long_rest |
| 20 | close_burst | Battle Master 20 Polearm Surge | 25 | 553 x 1 | 23 | 184.50 | 121.35 | 21.9% | A- | prebuffed: Action Surge and superiority dice are committed to the burst turn. | short_rest |
| 20 | close_burst | Champion 20 Polearm Surge | 25 | 553 x 1 | 23 | 145.50 | 87.00 | 15.7% | B+ | prebuffed: Action Surge turn with Superior Critical expanded crit range. | short_rest |
| 20 | close_burst | Eldritch Knight 20 Polearm Spirit Shroud | 25 | 553 x 1 | 23 | 186.00 | 88.05 | 15.9% | B+ | prebuffed: Spirit Shroud is already active; Action Surge is used. | short_rest |
| 20 | close_burst | Eldritch Knight 20 Rapier Shield Dueling Vex Spirit Shroud Surge | 25 | 553 x 1 | 23 | 128.00 | 95.39 | 17.3% | A- | prebuffed: Spirit Shroud is already active; Action Surge is used; Vex advantage depends on the previous hit. | short_rest |
| 20 | close_burst | Eldritch Knight 20 Rapier Shield Dueling Vex Surge | 25 | 553 x 1 | 23 | 92.00 | 67.32 | 12.2% | B | prebuffed: Action Surge is used; Vex advantage only appears after the previous rapier hit. | short_rest |
| 20 | close_burst | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar | 25 | 553 x 1 | 23 | 643.00 | 319.00 | 57.7% | S | prebuffed: CME is already active; Scorching Ray is cast with the normal action; Action Surge supplies an Attack action using Valor cantrip replacement; Illusionist's Bracers repeat Eldritch Blast as the bonus action. | short_rest |
| 20 | close_burst | Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar Paralyzed | 25 | 553 x 1 | 23 | 1236.00 | 862.11 | 155.9% | EX | prebuffed: CME is already active; Scorching Ray is cast with the normal action; Action Surge supplies an Attack action using Valor cantrip replacement; Illusionist's Bracers repeat Eldritch Blast as the bonus action. Target is Paralyzed and all attacks are made within 5 feet. | short_rest |
| 20 | close_burst | Valor Bard16 Warlock2 Fighter2 CME Turret Longbow Battle Magic | 25 | 553 x 1 | 23 | 458.50 | 231.65 | 41.9% | S- | prebuffed: CME is already active; Action Surge supplies Eldritch Blast; Battle Magic supplies one bonus-action weapon attack. | short_rest |
| 20 | close_burst | Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic | 25 | 553 x 1 | 23 | 457.50 | 231.05 | 41.8% | S- | prebuffed: CME is already active; Action Surge supplies Eldritch Blast; Battle Magic supplies one bonus-action weapon attack. | short_rest |
| 20 | close_burst | Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic Prior Vex | 25 | 553 x 1 | 23 | 457.50 | 241.28 | 43.6% | S- | prebuffed: CME is already active; Action Surge supplies Eldritch Blast; Battle Magic supplies one bonus-action weapon attack. | short_rest |
| 20 | close_burst | Wizard 20 CME9 + Scorching Ray8 | 25 | 553 x 1 | 23 | 346.50 | 173.25 | 31.3% | A+ | prebuffed: CME is already active; the burst spends an 8th-level slot. | long_rest |
| 20 | close_sustained | Berserker Barbarian 20 GWM | 23 | 468 x 1 | 22 | 72.00 | 61.84 | 13.2% | A | sustained: Rage is active; Reckless Attack is used. | encounter_low_cost |
| 20 | close_sustained | Hunter Ranger 20 Dual Wield Hunter's Mark | 23 | 468 x 1 | 22 | 48.00 | 30.20 | 6.5% | C | prebuffed: Hunter's Mark is active. | encounter_low_cost |
| 20 | close_sustained | Noble Genies Paladin 20 Dual Wield CME5 Divine Favor | 23 | 468 x 1 | 22 | 116.00 | 74.40 | 15.9% | A | prebuffed: CME and Divine Favor are already active. | long_rest |
| 20 | close_sustained | Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor | 23 | 468 x 1 | 22 | 76.00 | 69.30 | 14.8% | A | prebuffed: Hunter's Mark and Divine Favor are already active; Vow advantage is active. | encounter_low_cost |
| 20 | ranged_sustained | Warlock 20 Eldritch Blast Hex | 23 | 468 x 1 | 22 | 56.00 | 29.80 | 6.4% | C | prebuffed: Hex is active. | encounter_low_cost |

## Event Details

### Lv9 Light Cleric 9 Fireball

- 3rd-level Fireball, 8d6, Dex half, 3 targets: count=1, targets=3, fail=0.700, all-failed=84.00, expected=71.40
- Resources: 3rd-level slot
- Note: Uses the ranged AoE default of three meaningful targets.

### Lv13 Druid 13 Conjure Woodland Beings Movement

- Conjure Woodland Beings, 5d8, Wis half, 2 targets: count=1, targets=2, fail=0.550, all-failed=45.00, expected=34.88
- Resources: 4th-level slot, concentration, movement access
- Note: This is movement/table-position sensitive and should not be treated as automatic multi-hit damage.

### Lv20 Battle Master 20 Polearm Surge

- Main polearm attacks with Action Surge, 8 hits, 1d10 + 11: count=8, hit=0.550, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=132.00, expected=74.80
- Polearm Master bonus attack, 1d4 + 11: count=1, hit=0.550, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=13.50, expected=7.55
- Superiority dice spent on hits, 6d12: count=1, targets=1, damage=39.00
- Resources: Action Surge, Polearm Master, Great Weapon Master, superiority dice
- Note: Maneuver dice are modeled as spent on successful hits, not as separate attack rolls.

### Lv20 Champion 20 Polearm Surge

- Main polearm attacks with Action Surge, 8 hits, 1d10 + 11: count=8, hit=0.550, crit=0.150, crit_min=18, crit_on_hit=False, all-hit=132.00, expected=79.20
- Polearm Master bonus attack, 1d4 + 11: count=1, hit=0.550, crit=0.150, crit_min=18, crit_on_hit=False, all-hit=13.50, expected=7.80
- Resources: Action Surge, Polearm Master, Great Weapon Master
- Note: Champion level 15+ crits on 18-20 with weapon attacks and Unarmed Strikes.

### Lv20 Eldritch Knight 20 Polearm Spirit Shroud

- Main polearm attacks with Action Surge, 8 hits, 1d10 + 11 + 1d8: count=8, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=168.00, expected=79.60
- Polearm Master bonus attack, 1d4 + 11 + 1d8: count=1, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=18.00, expected=8.45
- Resources: 4th-level slot: Spirit Shroud, Action Surge, Polearm Master, Great Weapon Master
- Note: EK's 4th-level Spirit Shroud remains 1d8; this is a martial burst anchor.

### Lv20 Eldritch Knight 20 Rapier Shield Dueling Vex Spirit Shroud Surge

- Rapier Vex chain with Action Surge, 8 attacks, 1d8 + 7 + 1d8: Vex chain count=8, normal hit/crit=0.550/0.050, adv hit/crit=0.797/0.098, crit_min=20, crit_on_hit=False, all-hit=128.00, expected=95.39
- Resources: 4th-level slot: Spirit Shroud, Action Surge, Dueling Fighting Style, shield, Vex
- Note: EK's 4th-level Spirit Shroud remains 1d8; Vex is modeled as a sequential chain.

### Lv20 Eldritch Knight 20 Rapier Shield Dueling Vex Surge

- Rapier Vex chain with Action Surge, 8 attacks, 1d8 + 7: Vex chain count=8, normal hit/crit=0.550/0.050, adv hit/crit=0.797/0.098, crit_min=20, crit_on_hit=False, all-hit=92.00, expected=67.32
- Resources: Action Surge, Dueling Fighting Style, shield, Vex
- Note: This is a defensive rapier-and-shield reference, not a maximum DPR route.

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar

- 7th-level Scorching Ray, 8 rays, 2d6 + 6d8: count=8, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=272.00, expected=136.00
- Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=150.00, expected=74.00
- Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8: count=1, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=35.50, expected=17.50
- Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8: count=1, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=35.50, expected=17.50
- Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=150.00, expected=74.00
- Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration
- Note: Extreme item-dependent branch. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage.
- Note: Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style.
- Note: No Advantage, paralysis, or prior Vex is assumed.

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar Paralyzed

- Paralyzed target: 7th-level Scorching Ray, 8 rays, 2d6 + 6d8: count=8, hit=0.698, crit=0.698, crit_min=20, crit_on_hit=True, all-hit=544.00, expected=379.44
- Paralyzed target: Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.698, crit=0.698, crit_min=20, crit_on_hit=True, all-hit=280.00, expected=195.30
- Paralyzed target: Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8: count=1, hit=0.698, crit=0.698, crit_min=20, crit_on_hit=True, all-hit=66.00, expected=46.03
- Paralyzed target: Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8: count=1, hit=0.698, crit=0.698, crit_min=20, crit_on_hit=True, all-hit=66.00, expected=46.03
- Paralyzed target: Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.698, crit=0.698, crit_min=20, crit_on_hit=True, all-hit=280.00, expected=195.30
- Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Illusionist's Bracers, Spell Sniper, Dual Wielder, Weapon Mastery: Nick, concentration, Paralyzed target
- Note: Extreme item-dependent branch. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage.
- Note: Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style.
- Note: Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit.
- Note: Flat damage is not doubled; all damage dice on the attack are doubled.

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Longbow Battle Magic

- 7th-level Scorching Ray, 8 rays, 2d6 + 6d8: count=8, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=272.00, expected=136.00
- Eldritch Blast through Action Surge, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=150.00, expected=74.00
- Battle Magic longbow, 1d8 + 5 + 6d8: count=1, hit=0.550, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=36.50, expected=21.65
- Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Battle Magic, concentration
- Note: No Illusionist's Bracers. Longbow has no Vex branch.

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic

- 7th-level Scorching Ray, 8 rays, 2d6 + 6d8: count=8, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=272.00, expected=136.00
- Eldritch Blast through Action Surge, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=150.00, expected=74.00
- Battle Magic shortbow, 1d6 + 5 + 6d8: count=1, hit=0.550, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=35.50, expected=21.05
- Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Battle Magic, concentration
- Note: No Illusionist's Bracers. Shortbow has Vex, but this single bonus-action attack has no prior Vex advantage.

### Lv20 Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic Prior Vex

- 7th-level Scorching Ray, 8 rays, 2d6 + 6d8: count=8, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=272.00, expected=136.00
- Eldritch Blast through Action Surge, 4 beams, 1d10 + 5 + 6d8: count=4, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=150.00, expected=74.00
- Battle Magic shortbow with prior Vex Advantage, 1d6 + 5 + 6d8: count=1, hit=0.797, crit=0.098, crit_min=20, crit_on_hit=False, all-hit=35.50, expected=31.29
- Resources: 8th-level slot: CME, 7th-level slot: Scorching Ray, Action Surge, Battle Magic, concentration
- Note: No Illusionist's Bracers. This branch assumes a prior shortbow Vex hit made this bonus-action attack advantaged.

### Lv20 Wizard 20 CME9 + Scorching Ray8

- 8th-level Scorching Ray, 9 rays, 2d6 + 7d8: count=9, hit=0.450, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=346.50, expected=173.25
- Resources: 9th-level slot: CME, 8th-level slot: Scorching Ray, concentration
- Note: All-hit ceiling anchor is 346.5 before hit chance.

### Lv20 Berserker Barbarian 20 GWM

- Reckless greatsword attacks, 2 hits, 2d6 + STR + Rage + GWM + Frenzy: count=2, hit=0.840, crit=0.098, crit_min=20, crit_on_hit=False, all-hit=72.00, expected=61.84
- Resources: Rage, Reckless Attack, Great Weapon Master
- Note: Frenzy dice are folded into the event as once-per-turn damage.

### Lv20 Hunter Ranger 20 Dual Wield Hunter's Mark

- Dual-wield hits, 4 hits, 1d6 + 5 + 1d6: count=4, hit=0.600, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=48.00, expected=30.20
- Resources: Hunter's Mark, Nick, Dual Wielder
- Note: Subclass damage riders are not included; use as a Ranger floor branch.

### Lv20 Noble Genies Paladin 20 Dual Wield CME5 Divine Favor

- Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 3d8 + 1d4: count=4, hit=0.600, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=116.00, expected=74.40
- Resources: 5th-level slot: CME, Divine Favor, concentration, Nick, Dual Wielder
- Note: Close-range concentration branch; lower hit count than full-caster ray/EB CME routines.

### Lv20 Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor

- Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 1d6 + 1d4: count=4, hit=0.840, crit=0.098, crit_min=20, crit_on_hit=False, all-hit=76.00, expected=69.30
- Resources: Hunter's Mark, Divine Favor, Vow of Enmity, Nick, Dual Wielder
- Note: This is a sustained weapon-rider branch, not a smite nova branch.

### Lv20 Warlock 20 Eldritch Blast Hex

- Eldritch Blast, 4 beams, 1d10 + 5 + 1d6: count=4, hit=0.500, crit=0.050, crit_min=20, crit_on_hit=False, all-hit=56.00, expected=29.80
- Resources: Hex, concentration, Agonizing Blast
