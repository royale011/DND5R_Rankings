---
name: official-dnd-ranking-review
description: Use for official, partner, UA, third-party published, or legacy-compatible D&D 5.5e/2024/5R ranking and review work in this project. Enforces local DND5e_chm source verification, Rankings/changelog.md criteria, version matching for community comments, and prevents using model memory for class/subclass feature text.
---

# Official D&D Ranking Review

Use this skill for any work under root `Rankings` involving official / partner / UA / third-party published / legacy-compatible D&D class, subclass, build, rule, spell, feat, item, or balance review.

Do not use this skill for `homebrews` unless the user explicitly asks to compare a homebrew against official standards; homebrew output uses `homebrews\Rankings\changelog.md`.

## Non-Negotiable Rule

Never write or revise a class/subclass feature review from model memory. First verify the current feature names, levels, and wording in `DND5e_chm`.

If community comments mention a feature that does not match the `DND5e_chm` version, treat that comment as historical or mismatched and do not use it as evidence for the current review.

Example: for 2024 `奉献之誓 Oath of Devotion`, do not mention 2014 `Purity of Spirit` if `DND5e_chm\玩家手册2024\角色职业\圣武士\奉献之誓.htm` has the 5.5e feature `卫护斩 Smite of Protection`.

The target audience is Chinese. When naming any official / partner / UA / third-party published class, subclass, feature, spell, feat, item, monster, rule, action, condition, weapon mastery, or other rules object, use the Chinese translation from `DND5e_chm` whenever it can be found. You may include the English name in parentheses on first mention for searchability, but the displayed name must not be English-only unless no Chinese translation can be located locally.

Known verified terminology note: `Origin Feat(s)` is `起源专长`, as found in `DND5e_chm\玩家手册2024\专长\起源专长.htm`. Do not translate it as `出身专长`.

Class and subclass display names, directory names, and review filenames must also match the verified Chinese name in `DND5e_chm`. If an existing ranking file uses a stale or unofficial translation, rename the file and update headings/links to the local Chinese name before continuing the review. Example: if the local source names `Oath of the Watchers` as `守望者之誓`, use `守望者之誓.md`, not `守望之誓.md`, even if an older path or previous review used the shorter wording.

Filename source markers are mandatory for non-first-party official material. If a review file is for UA, partner, or third-party content, append a full-width bracket marker after the verified Chinese class/subclass/build name:
- UA: `子职中文名（UA）.md`.
- Partner resource: `子职中文名（资源缩写）.md`, for example `回音骑士（EGW）.md` if a separate marked file is needed.
- Third-party resource: `子职中文名（资源缩写或资源中文简称）.md`, using the abbreviation/name found in `DND5e_chm` where possible.
Unmarked filenames are reserved for current official first-party published or official legacy resources. Do not let a UA replacement review occupy the unmarked official filename.

## Required Workflow

1. Identify scope.
   - Official / partner / UA / third-party published / legacy-compatible content writes to root `Rankings`.
   - Homebrew writes to `homebrews\Rankings` and follows homebrew archiving rules, not this root workflow.

2. Read project criteria.
   - Before substantial official ranking work, consult `Rankings\changelog.md`.
   - Preserve the established scoring scale, S+ restraint, Tier definitions, and “overall is not an average” rule.

3. Locate the local rules text.
   - Use `rg` over `DND5e_chm` for Chinese name, English name, and distinctive feature names.
   - For every class-wide pass, read `DND5e_chm\不全书.wcp` and locate that class's topic block in `[TOPICS]`. Do not assume the existing `Rankings` files are complete.
   - In `不全书.wcp`, class topic blocks can contain `————合作内容分割线————`. Entries after that divider and before the next class topic are partner / third-party content for that class unless a more specific local source classification says otherwise. List these entries before deciding scope, filenames, source markers, and leaderboard exclusion.
   - Entries before the divider are official first-party / official legacy / UA / partner items according to their own source tag and path; do not treat all old 5e books as partner merely because they are not 2024 PHB.
   - Prefer the newest local source when names collide inside the same source category:
     - 2024 PHB / 5.5e / 5R official paths over 2014 official paths.
     - `DND5e_chm\其他\新UA` before older UA when a UA appears to overwrite old UA content.
     - FRHoF / current partner source over older same-name partner material when it is clearly newer.
   - Do not let a 5.5e / 2024 UA update erase an older official 5e / 2014 published subclass. If an old official subclass has a newer 5.5e / 2024 UA update, evaluate both: keep the latest official published version in the unmarked filename, and put the latest UA version in a separate `（UA）` file.
   - When converting a 5e / 2014 subclass to the 5.5e / 2024 class chassis, treat every subclass feature or subclass spell that the old source grants below level 3 as being gained at level 3 instead. This reflects the 2024 subclass-entry level and prevents Tier 1 over-crediting from old level-1/2 subclass timing.
   - For 5e / 2014 Cleric subclasses converted to the 5.5e / 2024 Cleric chassis, ignore subclass features that grant `重甲` / `Heavy Armor` training, `军用武器` / `Martial Weapon` proficiency, `神圣打击` / `Divine Strike`, or `强力施法` / `Potent Spellcasting` when assigning balance/functionality ranks. Those benefits are covered or overwritten by the 2024 Cleric base class through `神圣秩序` and `受祝击`; they may be mentioned only as legacy-source notes or design/compatibility issues, not as subclass power gains.
   - Record enough local context in your own notes before writing: source path, class/subclass name, feature names, feature levels, spell list, and any special action/resource wording.
   - Record the Chinese translation for every official / partner name you plan to mention. If the local source only exposes an English name or garbled text prevents reliable Chinese extraction, state that the Chinese translation could not be localized and keep the English name.
   - Verify the class/subclass Chinese name before choosing the output directory, filename, and top-level heading. The filename must be `[verified subclass Chinese name].md` for first-party official content, or `[verified subclass Chinese name]（source marker）.md` for UA / partner / third-party content; class summaries must stay as `README.md` inside the verified class-name directory. If a previous file has the wrong Chinese name or lacks a required source marker, move/rename it rather than creating a duplicate.

4. Version-lock the review.
   - Only analyze features present in the verified local source.
   - If a previous review file contains old-version features, remove or correct them.
   - If a feature cannot be reliably found locally, explicitly say the source could not be localized and keep the analysis conservative. Do not invent feature names.

5. Use community comments only after local verification.
   - Browse when the user asks for community comments, current opinions, or calibration.
   - Treat RPGBOT, Tabletop Builds, Treantmonk, Pack Tactics, Dungeon Dudes, Reddit, Giantitp, and D&D Beyond forums as calibration sources, not rules sources.
   - Keep only comments that match the local version’s actual feature set.
   - If a community review is about 2014 content but the file is 2024, use it only as historical contrast.
   - In final responses, cite online sources used.

6. Write feature-level reviews.
   - `详细评价` should explain actual level features, spell list, action economy, resources, concentration, weapon mastery, feat/item interactions, and Tier curve.
   - Use Chinese translated names for official / partner features, spells, feats, items, conditions, actions, and rules terms whenever `DND5e_chm` contains them. Do not leave names such as `Action Surge`, `Shield`, `Magic Initiate`, or `Weapon Mastery` English-only if their Chinese names are available locally.
   - Do not simply repeat the scoring table in prose.
   - For class files, analyze class-level features by level/tier.
   - For subclass files, explain how subclass features adjust the base class and other subclasses.
   - `综合评分` must use this vertical table, not the old horizontal Tier table. This applies to class files, subclass files, and build files under `Rankings\构筑`.

```markdown
## 综合评分
| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A | 具体说明为什么此阶段给这个综合强度。 |
| Tier 2（5-10） | B | 具体说明此阶段队伍定位、功能面、资源和横向比较。 |
| Tier 3（11-16） | C | 具体说明高等级变化。 |
| Tier 4（17-20） | C | 具体说明终局表现。 |
```

   - `具体理由` must be specific to that class/subclass/build and tier. Do not use generic wording such as “表现稳定” without naming the feature, spell list, action economy, role compression, or limitation that causes the score.
   - For build files, `具体理由` must name the build's actual level split, delayed features, ability-score pressure, spell-slot progression, action economy, and the point where the multiclass combination becomes stronger or weaker than staying single-class.
   - `Rankings\构筑` is for multiclass or cross-system build packages, not pure class / pure subclass optimization writeups. If a community "build" is simply one class/subclass from level 1-20 with feat choices, do not create a build file for it; fold that analysis into the relevant class/subclass review instead. This avoids conflict with direct subclass review and keeps build rankings from duplicating subclass rankings. Exception: if the user explicitly asks for a named community package whose identity depends on cross-version rules, legacy options, magic-item assumptions, or a distinct play package that is not represented by the subclass review, it may be included as a clearly marked cross-system build file; the file must state why it is not just a duplicate subclass review and must separate default strength from table-permission strength.

7. Keep rankings calibrated.
   - Tier 1: levels 1-4.
   - Tier 2: levels 5-10.
   - Tier 3: levels 11-16.
   - Tier 4: levels 17-20.
   - Categories: `近战伤害者`, `远程伤害者`, `法术伤害者`, `防御和生存`, `治疗和临时生命`, `团队增益`, `反制施法者`, `减益`, `战场分隔`, `召唤 / 伙伴`, `技能使用`, `制造`.
   - `S`: top of the relevant comparison set.
   - `S+`: only when it clearly exceeds the whole ecosystem, not merely its own class.
   - `E`: can technically do it but is among the worst options.
   - `E-`: only when it is the uniquely worst real participant.
   - `F`: no meaningful rules access to that function.
   - Overall score is based on team role and high-impact functions, not arithmetic average. Control, anti-caster tools, team buffs, healing, summoning, battlefield division, and high-level problem solving weigh more than raw DPR.
   - Partner, UA, and third-party published classes/subclasses must be ranked by their actual balance and functionality, not intentionally lowered because of source status. If community feedback is scarce, combine careful local text analysis, action economy, resource math, spell/feat/item interactions, and comparison against existing official rankings to assign the proper rank.
   - If a partner, UA, or third-party option breaks the expected class boundary, count that in its balance ranking. Give `S+` only when it exceeds the ceiling of the broader class/subclass ecosystem, not merely when it exceeds its own base class. If it is merely strong, specialized, or above its class baseline, use the appropriate normal rank.

8. Apply design-score separation.
   - Four design items: `设计质量`, `主题`, `能力设计质量`, `主题与能力关联度`.
   - High power is not automatically good design.
   - Overpowered action economy, bounded accuracy breaks, resource loops, old-version incompatibility, DM-dependent ambiguity, or feature bloat can lower design quality even if strength is high.

9. Account for shared 2024 assumptions.
   - 起源专长（Origin Feats） exist; `魔法入门（法师） Magic Initiate (Wizard)` can give many characters `护盾术 Shield`, so do not over-credit a subclass just for easy Shield access.
   - `武器精通 Weapon Mastery` is part of the 2024 martial baseline.
   - General magic items can affect a tier, but do not assume unlimited magic item economy.
   - FRHoF `Circle Magic` can strongly alter full-caster/team environments; do not assume it is always active unless the file or task says so.

10. Update records.
   - When a round changes official ranking methodology, standards, or calibration, prepend a concise entry to `Rankings\changelog.md`.
   - Keep `Rankings\changelog.md` in reverse chronological order: newest entries at the beginning of the file, older entries below.
   - Do not pollute individual review files with repeated community-source boilerplate; keep source summaries in `changelog.md` unless a file needs a specific citation or uncertainty note.

## Required Official Summary Sections

For every class `README.md`, after all subclasses of that class have been evaluated or revised, add or update `## 分阶段子职排行榜`.

Also add or update `## UA/合作方/第三方子职分阶段排行榜` whenever that class has any UA, partner, or third-party subclass review files. This second leaderboard uses the same Tier/rank bucket structure, but it contains only UA / partner / third-party subclass entries, including non-first-party subclasses that were excluded from `## 分阶段子职排行榜`.

For root `Rankings\README.md`, add or update `## 分阶段子职排行榜` only after all classes/subclasses are complete and the user asks to create or update the root summary. Root `分阶段子职排行榜` is now a practical ecosystem leaderboard: include official first-party subclasses, the explicit EGtW partner exceptions, and all valid multiclass / cross-system build files under `Rankings\构筑` in the same Tier/rank buckets so builds compete directly with official subclasses. Under the same condition, add or update root `## UA/合作方/第三方子职分阶段排行榜` if any such non-first-party subclass review files exist.

The section groups subclasses and, for root `README.md` only, builds by Tier and by their `综合评分` rank. Use verified Chinese class/subclass names from `DND5e_chm`; for builds, use the current build filename/title from `Rankings\构筑`. Skip any rank bucket that has no entry in that Tier. Each bullet reason should come from that subclass/build file’s `综合评分` -> `具体理由` for the same Tier; condense if needed, but do not replace it with a generic reason.

Strict consistency rule: `分阶段子职排行榜` and `UA/合作方/第三方子职分阶段排行榜` must be generated from the actual current subclass/build review file, not from memory, old notes, previous summaries, or a separate hand-written rank list. For every listed subclass/build and Tier, first read that file’s `## 综合评分` table and use its `综合强度` as the bucket and its same-row `具体理由` as the bullet reason. If the leaderboard rank disagrees with the standalone file, the standalone file is authoritative unless you deliberately recalibrate that file itself in the same pass and update its `综合评分` table. Never “correct” only the summary while leaving a contradictory standalone review.

Do not include partner, UA, or third-party subclasses/classes in `分阶段子职排行榜` for an official published base class, even if their individual review files exist and even if their actual rank is high. The leaderboard is for official first-party published options unless an exception below applies. Exception: if the base class being summarized in `README.md` is itself partner, UA, or third-party, then include all of that base class's subclasses in its `分阶段子职排行榜`, because the whole class ecosystem is non-official-first-party and the section is still useful for comparing its options.

Root-summary build exception: valid files under `Rankings\构筑` are not treated as UA/partner/third-party subclasses for root `分阶段子职排行榜`. They are included in the root official ecosystem leaderboard because the purpose of that root section is to compare real table options against official subclasses. This exception applies only to root `Rankings\README.md`; class-level `README.md` leaderboards do not include builds.

Explicit partner exception: `荒洲探险家指南 Explorer's Guide to Wildemount (EGtW)` counts as a partner resource in this project, but its subclasses are allowed in `分阶段子职排行榜` despite the general partner exclusion. Include EGtW `回音骑士 Echo Knight`, `时间魔法 Chronurgy Magic`, and `重力魔法 Graviturgy Magic` in the relevant Fighter/Wizard class leaderboards and root leaderboard when those summaries are generated or revised.

This leaderboard exclusion does not affect individual review scoring. Partner, UA, and third-party files still receive full, honest balance/functionality ranks in their own `分项评分` and `综合评分`.

The excluded entries must not disappear from class/root summaries. Put them into `## UA/合作方/第三方子职分阶段排行榜`:
- Include UA, partner, and third-party subclasses/classes reviewed under that class.
- Include EGtW `回音骑士`, `时间魔法`, and `重力魔法` here as partner entries even though they are also explicitly allowed in the official first-party leaderboard by project exception.
- Do not include first-party official published or official legacy subclasses in this section.
- Use the same rank and reason source rule as `## 分阶段子职排行榜`: each bullet reason should come from that subclass file’s same-Tier `综合评分` -> `具体理由`, condensed only as needed.
- If a class has no UA / partner / third-party subclass files, omit the section rather than creating an empty heading.

Naming format differs by summary scope:
- In a single class `README.md`, list each item as `子职中文名：理由`, because the class context is already explicit.
- In root `Rankings\README.md`, list subclass items as `职业中文名 - 子职中文名：理由`, so readers can identify the class immediately.
- In root `Rankings\README.md`, list build items as `构筑 - 构筑文件名去掉.md：理由`, so readers can distinguish builds from subclasses while still seeing them in the same rank buckets.

Required structure:

```markdown
## 分阶段子职排行榜

Tier 1（1-4）:
- S+:
  - 子职中文名：该子职在 Tier 1 的综合评分具体理由。
- S:
  - 子职中文名：该子职在 Tier 1 的综合评分具体理由。
- A:
  - 子职中文名：该子职在 Tier 1 的综合评分具体理由。

Tier 2（5-10）:
- A:
  - 子职中文名：该子职在 Tier 2 的综合评分具体理由。
```

For root `Rankings\README.md`, use the same buckets but change each bullet to:

```markdown
  - 职业中文名 - 子职中文名：该子职在该 Tier 的综合评分具体理由。
  - 构筑 - 构筑名：该构筑在该 Tier 的综合评分具体理由。
```

For `## UA/合作方/第三方子职分阶段排行榜`, use the same structure and naming format rules, but include source markers in the item name so readers immediately know why the entry is separated:

```markdown
## UA/合作方/第三方子职分阶段排行榜

Tier 1（1-4）:
- S+:
  - 子职中文名（UA）：该子职在 Tier 1 的综合评分具体理由。
- A:
  - 子职中文名（资源缩写或资源中文简称）：该子职在 Tier 1 的综合评分具体理由。
```

For root `Rankings\README.md`, use:

```markdown
  - 职业中文名 - 子职中文名（来源标记）：该子职在该 Tier 的综合评分具体理由。
```

## Practical Search Pattern

Use local search before writing:

```powershell
rg -n "English Name|中文名|Distinctive Feature|Subclass Name" .\DND5e_chm
rg -n "Old Feature Name|New Feature Name" .\DND5e_chm .\Rankings
```

Then open the relevant source file and existing ranking file. Do not rely on the search result alone when feature levels or wording matter.

## Output Style

For files in `Rankings`, write Simplified Chinese. Use Chinese translated official / partner names from `DND5e_chm` by default; English names are optional parenthetical search aids, not replacements. Be blunt, objective, and specific. If uncertain, state exactly what is uncertain and why.
