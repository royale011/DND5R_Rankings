# DPR Toolkit

## 目录

- [Purpose](#purpose)
- [Range And Burst Standards](#range-and-burst-standards)
- [Current Engine](#current-engine)
- [Reference Data](#reference-data)
- [Calibration Matrix](#calibration-matrix)
- [CLI Usage](#cli-usage)
- [Pilot Samples](#pilot-samples)

## Purpose

This directory contains reusable DPR calculation helpers for the ranking project. It is not a replacement for review judgment: the output is a math checkpoint that must still be interpreted with source verification, action economy, concentration, target access, resource recovery, and table assumptions.

## Range And Burst Standards

- `近距` means the meaningful damage routine requires 15 feet or less.
- Finer range bands should still be recorded: `touch`, `5`, `10`, `15`, `30`, `60+`, `120+`.
- Burst routines should be labeled as `cold_start`, `prebuffed`, or `setup_amortized`.
- Resource recovery should be labeled as `long_rest`, `short_rest`, `encounter_low_cost`, or `sustained`.
- All-hit ceiling and expected damage are both useful. Use expected damage for ranking decisions first, then discuss all-hit ceiling, setup, resource cost, and repeatability.

## Current Engine

The calculator supports explicit benchmark routines. It does not infer class features automatically; the routine definition must already encode the legal attack, spell, resource, setup, and target assumptions.

Current primitives:

- attack bonus vs AC
- normal / advantage / disadvantage
- crit chance, expanded crit ranges, and doubled dice
- condition branches where any hit becomes a critical hit, such as attacking a Paralyzed target from within 5 feet
- repeated weapon or spell attack events
- sequential `Vex` attack chains where each hit can grant Advantage to the next attack
- saving throw damage, including half-on-save and no-damage-on-save
- direct damage that is conditional on another successful routine step
- limited hit-pool riders, such as Battle Master dice spent only after successful hits
- dice-floor modeling for Great Weapon Fighting
- crit-only flat damage, such as Vorpal Sword's +30 damage when decapitation cannot apply
- AoE target counts
- per-hit riders such as `咒唤微元素群`, `魂灵环绕`, `神恩`, `猎人印记`, and `脆弱诅咒`
- multi-action samples such as `动作如潮`
- reference-CR percentage and tentative rank-pressure mapping

It intentionally does not automate every D&D rule. Add new primitives only when a review batch needs them.

## Reference Data

The calculator uses structured reference tables in `dpr/core/reference.py`, derived from the local `loot/dpr-ranking-reference.md` draft:

- PC level to reference CR for burst, sustained, close AoE, and ranged AoE.
- CR median HP, average HP, median AC, and median save bonuses.
- DPR percentage thresholds for tentative rank pressure.

The markdown draft remains the human-facing calibration note. The calculator reads the structured table so report generation is stable and not dependent on markdown parsing.

## Calibration Matrix

The calibration matrix keeps three assumption layers separate:

- `default`: ordinary optimized play without specific rare/very rare/legendary magic item dependency.
- `item_ceiling`: table-sensitive item branches such as `幻影师护臂`; these can show ceiling pressure but do not change the default rank.
- `condition_ceiling`: external state branches such as a Paralyzed target; these demonstrate kill ceiling and abuse potential, not ordinary DPR.

EX is not a fixed `% HP` threshold. In the matrix, EX requires horizontal dominance over same-level and same-category peers. The current dominance gate is at least S by threshold and at least `1.5x` the next comparable row. Vex remains supported by the calculator, but Vex-derived rows are excluded from this calibration pass unless a later review explicitly asks for stable Vex assumptions.

## CLI Usage

Generate the current benchmark report:

```powershell
python -m dpr.cli report --out loot/dpr-calculated-benchmarks.md
```

Print all current benchmark rows:

```powershell
python -m dpr.cli benchmark
```

Filter by level:

```powershell
python -m dpr.cli benchmark --levels 13-20 --category close_burst
```

Calculate one routine by id:

```powershell
python -m dpr.cli routine wizard-20-cme9-plus-scorching-ray8 --level 20
```

Use `--format json` on `routine` or `benchmark` for machine-readable output.

Generate the default/item/condition calibration matrix:

```powershell
python -m dpr.cli matrix
```

This writes tracked calibration files under `loot/`:

- `loot/dpr-calibration-matrix.md`
- `loot/dpr-calibration-matrix.json`

## Pilot Samples

Run:

```powershell
python -m dpr.examples.baselines
```

The current samples cover:

- 20级法师：9环 `咒唤微元素群` + 8环 `灼热射线`
- 勇气学院吟游诗人16 / 魔契师2 / 战士2：8环 `咒唤微元素群` with 7环 `灼热射线`, `魔能爆`, and `动作如潮`
- 20级奥法骑士：长柄武器 / `巨武器大师` / `魂灵环绕` / `动作如潮`

The newer CLI benchmarks are broader and should be preferred for ranking calibration.

Current benchmark notes:

- `勇气学院16 / 魔契师2 / 战士2` includes no-`幻影师护臂` Battle Magic variants for longbow and shortbow.
- It also includes an explicitly item-dependent `幻影师护臂` extreme branch with Spell Sniper, Dual Wielder, two scimitars, and Nick.
- The same extreme branch has a separate Paralyzed-target variant; it is condition-dependent and should not be treated as the ordinary DPR line.
- CME-bound weapon/ray/beam routines are categorized as `close_burst` or `close_sustained` when the added damage requires the target to be within 15 feet.
- Champion Fighter weapon attacks use expanded critical range in the relevant benchmark rows.
- The current Fighter polearm rows use Great Weapon Fighting, Great Weapon Master, Polearm Master, and Graze. Great Weapon Master is modeled as applying to each qualifying Attack-action hit, not to Polearm Master bonus-action hits.
- Great Weapon Fighting uses the broad benchmark reading: eligible attack damage dice showing 1 or 2 count as 3. Rows that apply this to riders such as CME, Spirit Shroud, Divine Favor, Radiant Strikes, Booming Blade, or Searing Smite mark that assumption as table-sensitive.
- Graze miss damage is modeled as ability modifier only and never triggers hit riders such as CME, smite damage, Great Weapon Master, Vorpal Sword, Radiant Strikes, Frenzy, or Battle Master dice.
- Ordinary Eldritch Knight uses PHB 2024 True Strike for War Magic replacement. The item-ceiling Eldritch Knight row uses Booming Blade only for the non-PHB extreme branch, and excludes Booming Blade's movement damage.
- Vorpal Sword item-ceiling rows model +30 damage as crit-only flat damage when the target cannot be beheaded.
- Vex chains are stateful: if one attack misses, the next attack does not gain Vex Advantage from that missed attack.
