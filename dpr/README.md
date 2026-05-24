# DPR Toolkit

## 目录

- [Purpose](#purpose)
- [Range And Burst Standards](#range-and-burst-standards)
- [Current Engine](#current-engine)
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

The first version supports attack-based routines:

- attack bonus vs AC
- normal / advantage / disadvantage
- crit chance and doubled dice
- repeated weapon or spell attack events
- per-hit riders such as `咒唤微元素群`, `魂灵环绕`, `神恩`, `猎人印记`, and `脆弱诅咒`
- multi-action samples such as `动作如潮`

It intentionally does not automate every D&D rule. Add new primitives only when a review batch needs them.

## Pilot Samples

Run:

```powershell
python -m dpr.examples.baselines
```

The current samples cover:

- 20级法师：9环 `咒唤微元素群` + 8环 `灼热射线`
- 勇气学院吟游诗人16 / 魔契师2 / 战士2：8环 `咒唤微元素群` with 7环 `灼热射线`, `魔能爆`, and `动作如潮`
- 20级奥法骑士：长柄武器 / `巨武器大师` / `魂灵环绕` / `动作如潮`

