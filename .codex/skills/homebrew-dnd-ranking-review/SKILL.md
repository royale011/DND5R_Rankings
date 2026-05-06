---
name: homebrew-dnd-ranking-review
description: Use for D&D 5.5e/2024/5R homebrew ranking and review work in this project. Enforces homebrews/Rankings/changelog.md criteria, source archiving via 原文, Archive-on-change workflow, out-of-boundary balance accounting, and local DND5e_chm verification for any official class, subclass, feature, spell, feat, item, monster, or rule referenced by a homebrew.
---

# Homebrew D&D Ranking Review

Use this skill for any review or ranking under `homebrews\Rankings`.

Do not write homebrew evaluations into root `Rankings` unless the user explicitly asks to convert or compare against official / partner content. Root official ranking work uses the separate `official-dnd-ranking-review` skill.

## Non-Negotiable Rule

Never evaluate a homebrew interaction with official content from model memory. If the homebrew mentions an official class, subclass, feature, feat, item, spell, monster stat block, condition, action, or rule term, first verify the current local text in `DND5e_chm`.

Example: Atlassian 学派 14级 `Ask Rovo` result 4 references `睡眠术 Sleep`. In 5.5e/2024, `Sleep` is not the 2014 total-HP pool spell; it uses a saving throw. Therefore do not write “高等级通常不稳定，因为低生命值池” unless the verified local spell text says so. Judge it as a 5.5e saving-throw sleep effect, including DC, target count/area, condition, repeat saves, and action economy.

The target audience is Chinese. When naming any official / partner / UA / third-party published class, subclass, feature, spell, feat, item, monster, rule, action, condition, weapon mastery, or other rules object referenced by a homebrew, use the Chinese translation from `DND5e_chm` whenever it can be found. You may include the English name in parentheses on first mention for searchability, but the displayed name must not be English-only unless no Chinese translation can be located locally.

Known verified terminology note: `Origin Feat(s)` is `起源专长`, as found in `DND5e_chm\玩家手册2024\专长\起源专长.htm`. Do not translate it as `出身专长`.

## Required Workflow

1. Identify scope and output path.
   - Homebrew outputs go under `homebrews\Rankings`.
   - Use subdirectories by class/type, such as `牧师`, `圣武士`, `法师`, `游荡者`, etc.
   - Keep root `Rankings` as calibration/reference only, not as an output target.

2. Read homebrew standards.
   - Before substantial homebrew work, consult `homebrews\Rankings\changelog.md`.
   - Use root `Rankings\changelog.md` and existing root `Rankings` files as official/partner baselines.

3. Read the source homebrew file.
   - Use the current file in `homebrews`.
   - If both English and Chinese are present, use Chinese as the authoritative archived `原文` unless the user says otherwise.
   - Preserve homebrew-created names as written in the source. For official / partner names embedded in the homebrew text, replace or explain them with the verified Chinese translation from `DND5e_chm` when writing the review.
   - At the beginning of a homebrew file, watch for sections such as `附注`, `Note`, `设计意图`, `设计目标`, `个人意图`, or similar author notes. These may state a personal/table-specific design purpose that intentionally differs from public-release balance expectations. Archive these sections in `原文` like any other source text, but keep two standards separate:
     - Balance/functionality ranks still use the normal official/partner/homebrew-calibrated ecosystem standard.
     - If such personal-purpose sections exist, add an extra section named `设计相关评分 - 个人期望` that judges whether the design succeeds at the stated personal/table-specific purpose.
   - If an `附注` / `Note` / `设计意图` section says the homebrew is `基于...改编`, `based on...`, adapted from a previous edition, UA, prestige class, subclass, class, feat, spell, monster, setting mechanic, or another explicit source, treat that as an adaptation baseline. Identify and verify the origin resource before deciding the personal design purpose. Then judge both:
     - Whether the homebrew preserves the original source's intended fantasy, table role, and signature mechanics.
     - Whether the conversion into 5.5e/2024 rules is mechanically healthy, including action economy, resource model, bounded accuracy, scaling, terminology, and compatibility with current class/subclass structure.

4. Compare against existing ranking `原文`.
   - If no ranking exists, create a new file and include `原文`.
   - If ranking exists, compare the current source Chinese text to its `## 原文` section.
   - If source changed, first archive the current ranking file to:
     `homebrews\Rankings\[class]\Archive\[subclass name] - [YYYYMMDD HHMMSS].md`
   - If only standards or wording changed and source text did not change, update in place without archive.

5. Verify official references locally.
   - Search `DND5e_chm` with `rg` for every official spell/feat/item/class/subclass/feature/monster/rule cited by the homebrew.
   - Prefer 2024/5.5e/5R local text over 2014 same-name text.
   - If the homebrew clearly references a 2014 rule while the evaluation environment is 5.5e, state the mismatch and judge the expected 5.5e use unless the user says the homebrew intentionally uses 2014 text.
   - For spells, verify casting time/action, concentration, save type, repeat saves, target count/area, scaling, and condition/effect wording.
   - For monsters/companions, verify AC, HP, speed, senses, attacks, traits, and whether the homebrew overrides any stat.
   - Record the Chinese translation for every official / partner name you plan to mention. If the local source only exposes an English name or garbled text prevents reliable Chinese extraction, state that the Chinese translation could not be localized and keep the English name.

6. Evaluate full text strength.
   - Out-of-boundary or overpowered content is included in balance ranking. Do not silently “fix” it before scoring.
   - Point out out-of-boundary content in `详细评价` as future refinement material.
   - Design scores should punish bad boundaries, unclear rules, broken action economy, resource loops, bounded accuracy breaks, and DM-dependent ambiguity.

7. Respect special exclusions and explicit external baselines.
   - If the user explicitly excludes sidebars, flavor text, or a named section from balance scoring, ignore it for balance and only discuss it under design.
   - If the source says it is `基于...改编` / `based on...`, locate the origin source before final evaluation. Prefer local project resources first (`DND5e_chm`, `5e Reference`, `Rankings`, `homebrews`, PDFs or text files named by the source). If the source cannot be found locally and network access is unavailable or not requested, state that the origin could not be verified and mark the adaptation-quality judgment as uncertain rather than inventing the baseline.
   - For adaptations from 3.5e, 4e, 5e/2014, UA, third-party, partner, or another homebrew, do not copy old-edition power assumptions directly into 5.5e. Translate the role and fantasy, then evaluate whether the new text uses 2024-compatible actions, saving throws, proficiency scaling, rest resources, spell-slot assumptions, concentration, weapon mastery, and subclass feature cadence.
   - For `看门狗 Watch Dog`, the source states it is based on a 5e UA. Before evaluating it, also consult `5e Reference\My New D20 Modern Campaign.pdf` as the explicit external baseline for the referenced UA material, then compare that baseline against the current 5.5e/2024 environment and official criteria.

8. Use the same scoring system.
   - Tier 1: levels 1-4.
   - Tier 2: levels 5-10.
   - Tier 3: levels 11-16.
   - Tier 4: levels 17-20.
   - Categories: `近战伤害者`, `远程伤害者`, `法术伤害者`, `防御和生存`, `治疗和临时生命`, `团队增益`, `反制施法者`, `减益`, `战场分隔`, `召唤 / 伙伴`, `技能使用`, `制造`.
   - `S`: top of the relevant comparison set.
   - `S+`: only if it is among the best of the best across the whole official/partner/homebrew-calibrated ecosystem, not merely above its own class boundary.
   - `E`: can do it but is among the worst.
   - `E-`: uniquely worst real participant.
   - `F`: no meaningful rules access.
   - Overall score is based on team role and high-impact functions, not simple averaging.

9. Do not treat official overlap as inherently invalid.
   - A homebrew subclass overlapping an official subclass’s theme, role, or mechanic is not automatically a design failure.
   - Flag overlap as a mechanical/design problem only when the homebrew clearly outperforms the original official subclass in that official subclass’s main role, or when it makes the official subclass’s distinct table niche mostly obsolete.
   - If overlap is mostly flavor, presentation, or subjective taste, say that directly and do not downgrade balance/design as if it were a rules defect.

10. Apply 2024 assumptions.
   - 起源专长（Origin Feats） exist. `魔法入门（法师） Magic Initiate (Wizard)` can grant `护盾术 Shield` to many spell-slot users, so a homebrew giving `护盾术 Shield` is not an exclusive ceiling; it saves feat/preparation cost and may improve integration.
   - `武器精通 Weapon Mastery` is part of the martial baseline.
   - General magic items may exist by tier, but do not assume unlimited item economy.
   - FRHoF `Circle Magic` is not default unless the task or source makes it relevant.

11. Write the review.
   - Output in Simplified Chinese.
   - Use Chinese translated names for official / partner features, spells, feats, items, monsters, conditions, actions, and rules terms whenever `DND5e_chm` contains them. Do not leave names such as `Action Surge`, `Shield`, `Magic Initiate`, or `Weapon Mastery` English-only if their Chinese names are available locally.
   - Include `原文`.
   - Include team/rules position, feature-level `详细评价`, per-tier scoring table, overall scoring table, design scoring table, official baseline comparison, `修改建议`, and uncertainty/test notes.
   - If the source has personal design-purpose sections (`附注`, `Note`, `设计意图`, etc.), also include `设计相关评分 - 个人期望` after the normal design scoring table.
   - If the source is an explicit adaptation (`基于...改编` / `based on...`), include an adaptation discussion in `详细评价`, `横向对照与不确定点`, or a dedicated `改编基准` section. State the verified origin source, what was preserved, what was changed for 5.5e/2024, and whether those changes are good translation, necessary modernization, overcorrection, or rules drift.
   - Do not repeat generic scoring boilerplate. Explain actual features, actions, resources, saves, concentration, interactions, and Tier curve.
   - `综合评分` must use this vertical table, not the old horizontal Tier table:

```markdown
## 综合评分
| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A | 具体说明为什么此阶段给这个综合强度。 |
| Tier 2（5-10） | B | 具体说明此阶段队伍定位、功能面、资源和横向比较。 |
| Tier 3（11-16） | C | 具体说明高等级变化。 |
| Tier 4（17-20） | C | 具体说明终局表现。 |
```

   - `具体理由` must be specific to that homebrew and tier. Mention the actual feature, spell, action economy, resource loop, scaling, official baseline comparison, or boundary issue that causes the score. Do not repeat generic phrases.

12. Write improvement advice in the review file.
   - Do not rely on a central `homebrews\Rankings\README.md` for improvement advice.
   - Every review file should include a `## 修改建议` section.
   - If the homebrew has personal design-purpose sections, split advice into:

```markdown
## 修改建议 - 公开发布

## 修改建议 - 个人意图
```

   - In advice sections, explicitly separate:
     - `必须修改`: rules, balance, wording, resource, action-economy, or bounded-accuracy problems that should be changed.
     - `可以保留`: strong or unusual choices that are acceptable.
     - `强但可接受`: features above baseline that are tolerable because of cost, timing, niche, risk, or intended role.
     - `仅公开发布时是问题`: elements that are fine for a private table or personal fantasy but likely unacceptable for public release.
     - `主观口味批评`: criticism based on tone, theme preference, elegance, or overlap taste rather than mechanical defect.
   - For public-release advice, compare against official/partner/homebrew-calibrated ecosystem standards.
   - For personal-intent advice, judge whether the text achieves the stated author purpose without pretending that personal intent changes the normal balance ranks.

13. Remove and do not maintain homebrew root summary.
   - `homebrews\Rankings\README.md` is deprecated for homebrew batch summaries. Do not create or update it.
   - If it exists during a homebrew review pass, remove it unless the user explicitly asks to keep a historical snapshot.
   - Any batch-level observations should go into `homebrews\Rankings\changelog.md`; actionable refinement advice belongs in each individual review file’s `修改建议` section.

14. Update records.
   - Prepend concise changes to `homebrews\Rankings\changelog.md` when a new evaluation, archive, standard change, or calibration occurs.
   - Keep `homebrews\Rankings\changelog.md` in reverse chronological order: newest entries at the beginning of the file, older entries below.
   - Record when `README.md` is removed or intentionally not maintained under the current workflow.

## Practical Search Pattern

```powershell
rg -n "Homebrew Feature|中文名|English Name" .\homebrews
rg -n "Official Spell|Feat|Item|Feature|Monster|Rule" .\DND5e_chm
rg -n "原文|综合强度|设计质量|能力设计质量" .\homebrews\Rankings
```

Open the matched local source before writing. Search results are not enough when wording matters.

## Common Failure Modes To Avoid

- Using 2014 spell memory for 2024 spells, such as treating `Sleep` as a hit-point pool instead of verifying the 5.5e saving-throw version.
- Treating a homebrew’s out-of-boundary feature as if it were already nerfed.
- Forgetting to archive a previous ranking after source text changes.
- Forgetting `原文`, or archiving English when the Chinese source is present.
- Calling a subclass S+ merely because it exceeds its own class boundary.
- Giving high design scores just because a feature is powerful.
- Maintaining improvement advice only in `homebrews\Rankings\README.md` instead of each review file.
- Treating personal design intent as if it changed the normal balance ranks, rather than adding `设计相关评分 - 个人期望`.
- Treating overlap with an official subclass as automatically invalid when the homebrew does not outperform that official subclass in its main role.
- Treating `基于...改编` as flavor only. Adaptation claims require checking the origin source and evaluating the quality of the 5.5e/2024 conversion.
