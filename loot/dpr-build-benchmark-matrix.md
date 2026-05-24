# DPR Build Benchmark Matrix Draft

> Local draft. This file is intentionally ignored by Git through `/loot/`.

## Purpose

This file is the third DPR calibration layer. It does not replace:

- `dpr-ranking-reference.md`: default CR / percentage curve.
- `dpr-ranking-reference-overchallenge.md`: high-tier boss stress-test curve.

This file answers a different question: *what do known high-output builds actually look like at each level, and how should those numbers pressure the damage-rank curve?*

The tables below are a working calibration artifact, not final public ranking text. They should be used to identify suspicious ranks and to decide what a future automated DPR calculator must support.

## Core Method

### Range And Category

- `近距` means the core routine requires 15 ft or less.
- `接触/5尺` is a stronger risk tag than `10尺`, which is stronger than `15尺`.
- A routine that can be performed at 30 ft or farther is not `近距` unless its main damage rider requires the 15-ft band.
- Ranged weapon or spell lines still record true range: 30, 60, 120, 150/600, or longer.

### Damage Outputs

Each benchmark should record:

- all-hit or failed-save ceiling;
- expected damage;
- percent of reference HP;
- setup state;
- resource recovery;
- tentative DPR rank.

Expected attack damage is calculated from attack bonus vs reference AC. Expected save damage uses caster DC vs the median monster saving throw for the reference CR.

### Save Bonus Reference

This snapshot is extracted from `5etools-src/data/bestiary/bestiary-xmm.json`. If a monster lacks a save proficiency entry, its ability modifier is used.

| CR | n | Str | Dex | Con | Int | Wis | Cha |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 41 | +2 | +2 | +1 | -2 | +1 | -1 |
| 2 | 59 | +3 | +2 | +2 | -1 | +1 | -1 |
| 3 | 41 | +3 | +2 | +2 | +0 | +1 | +0 |
| 4 | 27 | +3 | +2 | +3 | +0 | +1 | +2 |
| 5 | 36 | +4 | +1 | +3 | -2 | +1 | -1.5 |
| 7 | 16 | +4 | +2.5 | +4 | -0.5 | +3.5 | +0 |
| 8 | 23 | +4 | +2 | +5 | +1 | +4 | +2 |
| 10 | 16 | +5 | +5 | +5 | +3 | +7 | +4.5 |
| 11 | 12 | +6 | +4.5 | +5 | +1.5 | +4.5 | +4 |
| 14 | 4 | +5.5 | +6.5 | +6 | +4 | +7 | +4 |
| 16 | 7 | +8 | +5 | +9 | +4 | +8 | +6 |
| 20 | 4 | +8 | +6.5 | +7.5 | +3.5 | +9 | +6 |
| 23 | 5 | +10 | +7 | +10 | +4 | +10 | +7 |
| 25 | 1 | +10 | +8 | +10 | -4 | +8 | -1 |
| 30 | 1 | +10 | +9 | +10 | +5 | +9 | +9 |

Save-DC expected damage formula:

- fail chance = number of d20 rolls where `roll + save_bonus < DC`, bounded by natural 1/20 only if the rule says so. Ordinary saving throws do not auto-fail on natural 1 or auto-succeed on natural 20 unless a feature says otherwise.
- half-on-save expected = `fail chance * full damage + success chance * half damage`.
- no-save area damage = full expected damage, then manually discount for movement, target access, and table positioning.

### Paralysis Branch

Paralysis is not a default branch.

If a target is Paralyzed:

- attack rolls against it have Advantage;
- attacks that hit from within 5 ft are critical hits;
- the attack roll still must hit;
- only dice are doubled;
- flat damage, Great Weapon Master, Agonizing Blast, ability modifiers, and most fixed riders are not doubled.

Therefore a build dealing 60-70% of a reference target's HP can jump to 100%+ only if the routine uses many dice, attacks from within 5 ft, and actually has a reliable paralysis source. This should normally be tagged `paralysis-dependent`, not used as the default DPR rank.

### Warm-Up And Circle Magic

`咒唤微元素群`, `魂灵环绕`, `猎人印记`, `脆弱诅咒`, `神恩`, `加速术`, and similar riders must be separated by setup state:

- `冷启动`: this turn includes activation cost.
- `预启动`: the rider was already legally active before the turn.
- `设置折算`: the cost is amortized across 2-3 rounds.
- `Circle Magic`: separate branch only. Do not treat Circle Magic as default; it can change spell-slot ceiling and availability enough to create a different table environment.

## Rank Pressure Notes

The existing CR-percentage curve is not sufficient by itself. It is useful, but it must be pressure-tested against:

- the best legal build at the level;
- the highest all-hit ceiling;
- the highest expected DPR;
- how many turns/resources are needed;
- whether the routine is repeatable;
- whether the routine needs a condition such as paralysis;
- whether an item such as `幻影师护臂` is assumed.

Tentative interpretation:

- `EX` damage should normally mean "best-in-ecosystem or near best-in-ecosystem at that level and category", not merely 100% of a reference monster in an artificial branch.
- `S+` means the build is a clear apex for that category but still has a major limiter: setup, item dependence, melee risk, target condition, one-fight-per-day assumption, or narrow spell-slot timing.
- `S` means it is top-tier and fight-shaping but has real peers or stronger branches above it.

## Level 1-20 Maximum Pressure Matrix

This table gives the current likely pressure point for each level. It is intentionally conservative: if a branch needs `幻影师护臂`, paralysis, Circle Magic, or permissive prebuffing, it is not used as the default max row and is instead listed in notes.

| Lv | 近距爆发 pressure | 近距持续 pressure | 近距AoE pressure | 远程爆发 pressure | 远程持续 pressure | 远程AoE pressure |
|---:|---|---|---|---|---|---|
| 1 | Barbarian / Fighter weapon burst, B+ | Barbarian / Fighter weapon, B | small cleave or spell splash, C | Archery Fighter / Warlock EB, B | Archery Fighter / EB, B | Burning Hands-style cone, B |
| 2 | Fighter `动作如潮`, A | Barbarian Rage / Fighter, B+ | early cone / Thunderwave, B | Fighter Action Surge bow, A- | EB / Archery, B+ | Thunderwave / Burning Hands, B |
| 3 | Berserker / Battle Master / Vengeance mark branches, A | Berserker / dual wield Ranger, A- | Spike Growth if forced movement exists, A | Gloom Stalker / Battle Master bow, A | Warlock EB+Hex, A- | Shatter / Scorching Ray branches, B+ |
| 4 | feat-complete martial burst, A | feat martial sustained, A- | Spike Growth abuse branch, A | Gloom Stalker / Sharpshooter-style branch, A | EB+Hex / Archery, A- | Web+damage not pure DPR, B+ |
| 5 | Extra Attack martials / Paladin Divine Favor, A+ | GWM/PAM or dual wield, A | Spirit Guardians appears for Cleric, A+ | Gloom Stalker / Fighter Extra Attack, A+ | EB 2 beams / Hunter, A | Fireball-style AoE, S- |
| 6 | Battle Master / Paladin / Valor Bard extra attack, A+ | Paladin / Fighter / Ranger, A | Spirit Guardians / Spike Growth, S- | Fighter / Ranger / EB, A+ | EB / Fighter, A | Fireball / Light Cleric, S- |
| 7 | subclass riders mature, A+ | martial packages, A | Conjure/Spirit Guardians lines, S- | Ranger/Fighter/Warlock, A+ | EB+Hex, A | Fireball/upcast AoE, S- |
| 8 | ASI+feat lines complete, S- | Fighter/Ranger/Paladin, A+ | Spirit Guardians + forced movement, S | Fighter/Ranger/Warlock, S- | EB+Agonizing+Hex, A+ | upcast AoE, S- |
| 9 | Paladin `魂灵环绕`, Ranger CWB, Cleric SG, S | Paladin/Ranger/Cleric zones, A+ | CWB / SG movement damage, S | ranged martial + riders, S- | EB / Fighter/Ranger, A+ | Cone/Fireball/upcast, S- |
| 10 | Valor Bard base online; Fighter spikes, S- | martial/gish sustained, A+ | SG/CWB, S | Fighter / Warlock / Sorcerer, S- | EB+Hex, A+ | AoE caster, S |
| 11 | Fighter 3 attacks; Paladin Radiant Strikes, S | Fighter/Paladin sustained, S- | SG/CWB upcast, S | Fighter 3 attacks / EB 3 beams, S | EB / Fighter, S- | high caster AoE, S |
| 12 | feat-rich Fighter and Warlock, S | Fighter / Paladin, S- | SG/CWB, S | EB / Fighter, S | EB+Hex, S- | high caster AoE, S |
| 13 | Noble Genies Paladin CME starts, S+ branch | CME gish / Fighter, S | CWB / SG / CME close AoE, S+ | full caster ranged spell burst, S | EB / Fighter / Ranger, S- | high caster AoE, S |
| 14 | Valor Bard multiclass gets Magical Secrets if Bard10 path, S+ branch | CME/Spirit Shroud branches, S | CME/CWB, S+ | Bard/Warlock/Fighter CME turret starts, S+ | EB / Fighter, S | high caster AoE, S |
| 15 | 7th-level slot pressure; Bard CME turret rises, S+ | high gish sustained, S | high SG/CWB, S+ | CME + Scorching Ray / EB, S+ | Warlock / Fighter / caster, S | high caster AoE, S+ |
| 16 | ASI complete high-tier builds, S+ | top martial/gish, S | high close zones, S+ | CME turret / Sorcerer / Wizard, S+ | EB/Fighter/caster, S | high caster AoE, S+ |
| 17 | 9th-level full caster nova, S+ / EX candidate | high sustained with 9th resources, S | top caster AoE, S+ | Wizard/Sorcerer 9th-level lines, S+ | Warlock EB / Fighter / caster, S | 9th-level AoE, S+ |
| 18 | Wizard/Sorcerer high nova, S+ | high gish/caster, S | top zones, S+ | Wizard/Sorcerer/Bard, S+ | EB/Fighter/caster, S | 9th-level AoE, S+ |
| 19 | feat cap + 9th slots, S+ | top martials/gishes, S | top zones, S+ | CME turret and caster nova, S+ | EB/Fighter/caster, S | 9th-level AoE, S+ |
| 20 | Valor Bard16/W2/F2 CME turret apex, EX candidate | top repeatable gish, S+ | top zones / 9th AoE, S+ | CME turret / Wizard / Sorcerer, EX candidate | EB/Fighter/caster, S | 9th-level AoE, S+ |

## Branch Formulas By Build Family

### Valor Bard 16 / Warlock 2 / Fighter 2 CME Turret

Recommended build-order assumption for calibration:

1. Bard 1-6 first to secure Valor Bard Extra Attack and Bardic chassis.
2. Warlock 1-2 for `魔能爆` + `痛苦魔爆` / invocation package.
3. Fighter 1-2 for armor/weapon package and `动作如潮`.
4. Return Bard 7-16.

This delays `魔法奥秘` relative to pure Bard: Bard 10 arrives at total level 14. It is the main reason this build is not a Tier 2 CME build.

| Total Lv | Bard Lv | Key line | Slot ceiling | Default all-hit formula | Expected/rank pressure |
|---:|---:|---|---|---|---|
| 6 | 6 | Valor Extra Attack weapon line | 3rd | 2 weapon hits + Bard support | not turret yet; A-/A weapon line |
| 8 | 6 | Warlock 2 online | pact only | 2 weapon hits or 2 EB beams | A ranged sustain, no CME |
| 10 | 6 | Fighter 2 online | Bard 3rd | weapon action + Action Surge weapon/cantrip | A+ burst, not CME |
| 14 | 10 | Magical Secrets CME starts | 5th | `灼热射线` 6 rays x `(2d6+3d8)` + EB 3 beams x `(1d10+CHA+3d8)` with Action Surge | S+ short-range burst, 15-ft setup |
| 15 | 11 | 6th slot CME | 6th | Scorching Ray 7 rays x `(2d6+4d8)` + EB 3 beams x `(1d10+CHA+4d8)` | S+ |
| 17 | 13 | 7th slot CME | 7th | Scorching Ray 8 rays x `(2d6+5d8)` + EB 4 beams x `(1d10+CHA+5d8)` | S+ |
| 19 | 15 | 8th slot CME | 8th | Scorching Ray 9 rays x `(2d6+6d8)` + EB 4 beams x `(1d10+CHA+6d8)` | S+ / EX candidate if reliable |
| 20 | 16 | final build | 8th | same slot ceiling; better ASI / feat state | EX candidate among build benchmarks |

`幻影师护臂` branch:

- If the turn includes `魔能爆`, the item can add another bonus-action `魔能爆` if the item is allowed and timing is satisfied.
- Level 17+ branch adds 4 more beams x `(1d10+CHA+CME)`.
- This is item-dependent and should not set default class/subclass ranks.

Paralysis branch:

- Only attacks within 5 ft auto-crit on hit.
- EB is a ranged spell attack; if used within 5 ft, it needs disadvantage mitigation and still is not a melee attack. Paralysis gives advantage, cancelling adjacent-ranged disadvantage if applicable, but the auto-crit condition still requires the attack be from within 5 ft. This is legal if the attack hits, but it is a highly constrained 5-ft branch.
- Weapon dual-wield branch benefits more cleanly from paralysis but has fewer total hit events than CME + rays/EB.

Shortbow / longbow branch:

- Longbow is the clearer range line if proficiency is secured.
- Shortbow is less damage but easier for some builds.
- Neither bow line beats the CME turret once CME + EB + Action Surge is online; it mainly matters before total level 14 or when CME is unavailable/banned.

### Fighter Polearm Family

Assumptions:

- Strength starts +3, reaches +4 at level 4 and +5 by level 8 unless feat-heavy branch delays it.
- GWM and PAM are scored as feat economy allows.
- Fighter has `动作如潮`; Battle Master adds superiority dice / accuracy/control; Champion adds crit rate; no-subclass Fighter is baseline.

| Lv band | No subclass Fighter | Champion | Battle Master | Eldritch Knight |
|---|---|---|---|---|
| 1-4 | baseline weapon DPR; Action Surge at 2 | slightly better crit after subclass | best burst due maneuver dice and accuracy/control | not online until subclass; utility/defense more than DPR |
| 5-10 | Extra Attack + GWM/PAM line | crit value still modest | strongest ordinary Fighter damage/control | `护盾术` / utility; DPR near baseline unless using rider spell |
| 11-16 | 3 attacks make PAM/GWM excellent | crit scaling improves but still not Battle Master control | top nonmagical pressure | `魂灵环绕` starts late and short-range; can add per-hit value |
| 17-20 | 4 attacks; Action Surge burst is top martial reference | high hit count makes crit more relevant | maneuvers plus 8-hit surge remains elite | 4th-level `魂灵环绕` is only 1d8; still good, but not CME-style |

Level 20 EK polearm anchor:

- all-hit formula: 8 main hits x `(1d10 + 5 STR + 6 GWM + 1d8 Spirit Shroud)` + 1 PAM hit x `(1d4 + 5 + 6 + 1d8)`.
- all-hit average around 198.5 before crits.
- expected vs AC19 with +11 attack is around the high martial burst band, but below full-caster CME nova.

### Paladin Family

General assumptions:

- `神恩` is non-concentration and works on weapon attacks, including ranged weapon attacks.
- Most smite spells are non-concentration in 2024 except known exceptions; still check local spell text before scoring.
- Divine Smite costs Bonus Action and is melee-only / hit-triggered.
- Dual-wielding Paladin is feat- and BA-sensitive; do not assume every oath can afford `妖精触碰`.

| Lv band | Typical GWM Paladin | Vengeance dual-wield | Noble Genies Paladin |
|---|---|---|---|
| 1-4 | weapon + `神恩`; good but not nova king | `猎人印记` oath access supports more hit-based play | sword/shield or ordinary weapon line |
| 5-8 | Extra Attack, `神恩`, smite burst | dual-wield + Hunter's Mark is viable; compare BA congestion | still ordinary Paladin line |
| 9-12 | `魂灵环绕` appears for Paladin; 5th-level not yet | compare Hunter's Mark vs Spirit Shroud vs Haste: Spirit Shroud wins close DPR when already active, Haste gives defense/mobility/action utility but weaker pure per-hit DPR | can pivot toward dual-wield with Spirit Shroud |
| 13-16 | 4th-level slots and stronger auras | dual-wield remains strong but resource limited | `咒唤微元素群` from oath list creates true S+/near-EX short-range branch |
| 17-20 | 5th slots, capstone competition | 5th-level Spirit Shroud is 2d8 per hit; still setup-heavy | 5th-level CME is 3d8 per hit and can stack with `神恩`; apex Paladin DPR branch |

Noble Genies Paladin CME anchor:

- Level 13-16: dual-wield routine can carry 4th-level CME `(2d8 per hit)` if available.
- Level 17-20: 5th-level CME `(3d8 per hit)` plus `神恩` `(1d4 per hit)` can make each hit carry high extra dice.
- This is close-range, concentration, setup-heavy, and does not automatically outrank full-caster CME turret because Paladin has fewer spell slots and lower multi-hit spell options.

### Barbarian Family

Barbarian lacks Fighting Style, so dual-wield loses ability modifier on the Nick/off-hand damage unless another source grants it.

| Branch | Strength | Limiter |
|---|---|---|
| GWM Berserker | usually best burst/sustained Barbarian line because Rage + Reckless + heavy weapon feat synergy | target access, melee only, defensive risk |
| Polearm Berserker | stable BA attack and opportunity pressure | BA competition and lower die on butt-end attack |
| Dual-wield Berserker | more hit events but no Fighting Style by default | weaker flat damage per off-hand hit; feat pressure |
| Typical Barbarian best-of | usually GWM or polearm, not dual-wield | high-tier damage remains martial, not spell-nova |

### Ranger Family

Hunter dual-wield and Gloom Stalker ranged lines are the most relevant baselines.

- `猎人印记` is a core rider but concentration/BA pressure and replaceability matter.
- Dual-wield Hunter is strong in Tier 1-2 because many hit events carry the mark.
- At Tier 3+, Ranger can use `咒唤林地卫士`; movement-triggered close AoE can outrank ordinary weapon DPR if the Ranger can move through enemies while maintaining concentration.
- Ranged Gloom Stalker remains a high burst reference, especially with first-turn package, but it is encounter-start sensitive.

### Rogue Family

Rogue DPR is usually one large hit, not many hit events.

| Branch | DPR meaning |
|---|---|
| Typical Rogue | reliable single-hit Sneak Attack; sustained but rarely top DPR |
| Arcane Trickster | can add spell utility/control; CME + Scorching Ray is generally not ideal due slot limits and stronger control concentration |
| Soulknife | reliable ranged/psychic attack package and skill value, but not top burst DPR |

Paralysis helps Rogue because Sneak Attack dice double on a crit, but Rogue usually has fewer attacks, so it is not the same ceiling as ray/CME multi-hit builds.

### Cleric And Druid Close AoE

Close AoE often matters more than single-target melee DPR for Cleric/Druid.

| Build | Key line | Expected calculation |
|---|---|---|
| War Domain Cleric | weapon bonus + Spirit Guardians / Spirit Shroud choice | usually not a pure weapon apex; domain action economy matters |
| Light Domain Cleric | `灼热射线` + `魂灵环绕` if close enough | strong close spell burst; 10-ft risk and concentration |
| Tempest Domain Cleric | lightning/thunder maximization branches | burst depends on exact spell access and Channel Divinity |
| Generic Cleric | `灵体卫士` close AoE | Wis save expected damage; half-on-save; movement/positioning sensitive |
| Moon Druid | Wild Shape attacks + concentration spells | beast form hit count, Con save, and form CR determine value |
| Generic Druid | `咒唤林地卫士` / terrain control | close movement damage can be very high if enemies are forced/repeatedly crossed |
| Wildfire Druid | ranged fire spell / spirit delivery | AoE better than weapon DPR but not always close-range apex |

`灵体卫士` expected line:

- Damage is Wis save, half on success.
- Use reference CR Wis save median.
- Default target count: 2 for close AoE; 3+ only with strong positioning evidence.

`咒唤林地卫士` expected line:

- Damage can repeat through movement and enemy positioning.
- Count one trigger per target per round as default unless the build has a reliable forced-movement loop.
- Ranger gets this late and with half-caster slots; Druid gets stronger spell-slot support.

### Wizard / Sorcerer / Warlock Ranged And Short-Range Spell Burst

| Build | Key line | Limiter |
|---|---|---|
| Wizard generic | high-level AoE / control; CME + Scorching Ray for short-range nova | 15-ft risk, high slots, concentration |
| Evoker | safer/sculpted blast and overchannel-style mid-level spike | subclass ceiling lower than Chronurgy-type control |
| Draconic Sorcery | elemental DPR and metamagic | spell selection pressure, resistance type |
| Generic Sorcerer | metamagic + high-level spell list, includes Wish at T4 | narrower than Wizard but strong nova/control |
| Fiend Warlock | `灼热射线` patron spell + `魂灵环绕` close burst | pact-slot ceiling, 10-ft risk |
| Hexblade / weapon Warlock | weapon + `魂灵环绕` + invocations | 5th-level pact slot cap; strong but not full-caster CME |
| Generic Warlock | EB + Hex / Spirit Shroud | short-rest repeatability is meaningful T1-T2; high-level fixed Arcanum limits flexibility |

Wizard 20 CME anchor:

- 9th CME = `+7d8` per hit.
- 8th Scorching Ray = 9 rays.
- all-hit = `9 x (2d6 + 7d8)` = 346.5.
- expected depends heavily on attack bonus vs reference AC and Advantage availability.

Valor Bard / Warlock / Fighter 20 turret anchor:

- Without `幻影师护臂`: `9 rays x (2d6 + 6d8)` + `4 EB beams x (1d10 + 5 + 6d8)`.
- With `幻影师护臂`: add `4 EB beams x (1d10 + 5 + 6d8)` as item-dependent BA branch if timing is legal.
- This is one of the key `EX` pressure candidates for short-range burst, but only under a narrow 15-ft, concentration, high-slot, multiclass, item-sensitive environment.

## Six DPR Category Tables

### 近距爆发DPR

| Lv | Candidate | Formula snapshot | Setup | Tentative rank | Notes |
|---:|---|---|---|---|---|
| 1 | Barbarian/Fighter | 1 weapon hit + class rider if any | cold | B+ | no Extra Attack |
| 2 | Fighter | Action Surge: 2 weapon hits | short rest | A- | early spike |
| 3 | Berserker / Battle Master | weapon + subclass dice/rider | short/long | A | best martial pressure |
| 4 | feat martial | weapon + feat/rider | cold | A | ASI/feat matters |
| 5 | Extra Attack Paladin/Fighter | 2 hits + GWM/PAM/Divine Favor branch | cold/pre | A+ | Paladin BA smite competes |
| 6 | Valor/Battle Master/Paladin | 2-hit chassis + subclass | cold/pre | A+ | no CME yet |
| 7 | mature martial | 2-hit + rider | cold/pre | A+ | target access dominates |
| 8 | feat-complete martial | 2-hit + feat + rider | cold/pre | S- | top noncaster curve |
| 9 | Paladin Spirit Shroud | multi-hit + 1d8/2d8 rider if upcast later | pre | S | 10-ft risk |
| 10 | Fighter/Bard multiclass | Action Surge package | short | S- | Valor turret not online |
| 11 | Fighter 3 attacks / Paladin Radiant Strikes | 3 hits or 2 hits + radiant | pre | S | strong martial breakpoint |
| 12 | Fighter/Warlock gish | 3 hits + riders | pre | S | resource limited |
| 13 | Noble Genies Paladin | dual-wield + CME + Divine Favor | pre | S+ | 15-ft concentration |
| 14 | Valor Bard W2/F2/B10 | CME + Scorching Ray + EB | pre | S+ | first real turret level |
| 15 | Valor turret | 6th slot CME branch | pre | S+ | all-hit ceiling rises |
| 16 | Valor turret / full caster | 7th slot pressure soon | pre | S+ | item branch can exceed |
| 17 | Wizard/Sorcerer 9th spells | 9th-level nova branches | pre/cold | S+ | EX only for ecosystem apex |
| 18 | Wizard/Sorcerer/Bard | high-slot nova | pre | S+ | check spell access |
| 19 | Valor turret / Wizard | high slot + feat cap | pre | S+ | item branch pressure |
| 20 | Valor Bard16/W2/F2 | CME + Scorching Ray + EB + Action Surge; item branch adds BA EB | pre | EX candidate | no one-beats-that branch if item allowed |

### 近距持续DPR

| Lv | Candidate | Formula snapshot | Setup | Tentative rank | Notes |
|---:|---|---|---|---|---|
| 1-4 | Barbarian/Fighter/Ranger | weapon + Rage/mark | cold/pre | B to A- | low-level variance high |
| 5-8 | GWM/PAM Fighter, Paladin, Hunter Ranger | Extra Attack + rider | cold/pre | A to A+ | sustainable if rider cheap |
| 9-12 | Paladin Spirit Shroud, Fighter 3-hit at 11 | multi-hit + concentration rider | pre | A+ to S- | concentration and 10-ft risk |
| 13-16 | Noble Genies Paladin CME, Fighter 3-hit, Druid CWB | CME/CWB sustained if maintained | pre | S to S+ | not all fights allow setup |
| 17-20 | CME gish / top Fighter / Warlock weapon | repeated high rider or 4 attacks | pre | S to S+ | spell-slot scarcity matters |

### 近距范围DPR

| Lv | Candidate | Formula snapshot | Save/target | Tentative rank | Notes |
|---:|---|---|---|---|---|
| 1-4 | Burning Hands / Thunderwave / Spike Growth setup | cone/push/zone | Dex/Con or movement | B to A | positioning sensitive |
| 5-8 | Spirit Guardians Cleric | 3d8+ Wis save half, 2 targets default | Wis save median | A+ to S | repeatable if concentration holds |
| 9-12 | Spirit Guardians upcast / Conjure Woodland Beings | zone/movement damage | Wis/Dex or no-save movement text | S | forced movement can raise ceiling |
| 13-16 | Druid/Ranger CWB, high SG, CME cleave branches | repeated close-zone damage | save/positioning | S+ | default 2 targets; more needs proof |
| 17-20 | high-slot SG/CWB/9th AoE close lines | high-slot repeated damage | save/positioning | S+ | EX only if reliable multi-target lock |

### 远程爆发DPR

| Lv | Candidate | Formula snapshot | Setup | Tentative rank | Notes |
|---:|---|---|---|---|---|
| 1-4 | Archery Fighter / Warlock EB / Gloom Stalker | ranged hit(s) + rider | cold/pre | B+ to A | Vex/advantage matters |
| 5-8 | Gloom Stalker / Fighter / Warlock EB 2 | Extra Attack or 2 beams | cold/pre | A to S- | range safer than melee |
| 9-12 | Fighter/Ranger/Warlock/Sorcerer | multi-hit or spell burst | cold/pre | S- to S | high slots appear |
| 13-16 | Bard/Wizard/Sorcerer ranged spell burst | rays/AoE; CME if within 15 is not truly ranged | cold/pre | S to S+ | distinguish 15-ft CME from true range |
| 17-20 | Wizard/Sorcerer/Bard/Warlock | 9th-level spell / EB / item branches | cold/pre | S+ / EX candidate | Wish access is not raw DPR by itself |

### 远程持续DPR

| Lv | Candidate | Formula snapshot | Setup | Tentative rank | Notes |
|---:|---|---|---|---|---|
| 1-4 | EB+Hex / Archery weapon | 1 hit/beam + rider | pre | B+ to A- | short-rest Warlock matters |
| 5-8 | EB 2 beams / Fighter/Ranger Extra Attack | 2 beams/hits + rider | pre | A to A+ | Hunter's Mark/Hex concentration |
| 9-12 | EB 3 beams at 11 / Fighter 3 attacks | 3 hits/beams | pre | A+ to S- | Warlock short-rest repeatability |
| 13-16 | EB / Fighter / Ranger / caster cantrips | 3-4 beams later | pre | S- to S | caster often uses control instead |
| 17-20 | EB 4 beams / Fighter 4 attacks / caster repeat lines | 4 hits or cantrip+rider | pre | S | highest ranged sustained has peers |

### 远程范围DPR

| Lv | Candidate | Formula snapshot | Save/target | Tentative rank | Notes |
|---:|---|---|---|---|---|
| 1-4 | Burning Hands/Thunderwave/Shatter | low-level AoE | Dex/Con save | B to A- | slot pressure high |
| 5-8 | Fireball / Light Cleric / Wildfire Druid | 8d6 Dex half, 3 targets default | Dex median | S- to S | classic AoE spike |
| 9-12 | upcast Fireball / Cone / Synaptic Static | save half or rider | Dex/Int/Wis median | S | control rider may matter more than DPR |
| 13-16 | high-level AoE caster | larger dice / better area | save-specific | S to S+ | target count and save type matter |
| 17-20 | 9th-level AoE / Meteor Swarm | very high AoE | Dex save, half | S+ | EX only if target count and encounter shape support it |

## Immediate Calibration Takeaways

1. A pure CR-percent curve is useful but insufficient. The table must be anchored by actual build ceilings.
2. Valor Bard / Warlock / Fighter CME turret is a real top-end pressure point, but the default branch starts late and depends on 15-ft positioning, concentration, multiclass timing, and high slots. `幻影师护臂` should be an item-ceiling branch, not default.
3. Paralysis can turn strong DPR into kill-level DPR, but it is condition-dependent and 5-ft-dependent. It should not define ordinary rank unless the build reliably creates paralysis.
4. Warm-up is rank-critical. CME's best branch is usually pre-started; cold-start CME often loses a key turn unless the encounter allows preparation. Circle Magic is a separate environment.
5. Saving-throw AoE must use monster save bonuses. High-level Wis/Con saves can sharply reduce expected damage compared with failed-save ceiling, while Dex saves vary by CR and creature type.
6. Melee/close DOT AoE such as Spirit Guardians / Conjure Woodland Beings can outperform weapon DPR when target count and movement loops are reliable, but default target count should stay conservative.
7. Full-caster high-level damage should be compared against other uses of the same slot. A DPR line can be mathematically high and still be strategically worse than control, denial, or Wish-level utility.

## Next Automation Requirements

The permanent DPR engine should eventually support:

- saving throw events with half-on-save / no-save / repeat-save variants;
- auto-crit-on-hit branches for paralysis within 5 ft;
- prebuff and setup amortization across multiple rounds;
- resource recovery labels and max uses per day;
- spell-slot progression by class/multiclass level;
- weapon mastery and feat bundles;
- item branches such as `幻影师护臂`;
- AoE target-count assumptions and forced-movement triggers;
- per-level benchmark output for each configured build.

