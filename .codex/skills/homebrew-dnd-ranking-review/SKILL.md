---
name: homebrew-dnd-ranking-review
description: Use for D&D 5.5e/2024/5R homebrew ranking and review work in this project. Enforces homebrews/Rankings/changelog.md criteria, source archiving via 原文, Archive-on-change workflow, out-of-boundary balance accounting, personal-intent review sections, and shared official-ranking calibration from the official-dnd-ranking-review skill.
---

# Homebrew D&D Ranking Review

Use this skill for any review or ranking under `homebrews\Rankings`.

Do not write homebrew evaluations into root `Rankings` unless the user explicitly asks to convert or compare against official / partner content. Root official ranking work uses the separate `official-dnd-ranking-review` skill.

## Skill Dependency

This skill intentionally delegates shared D&D 5.5e/2024 ranking standards to:

`C:\Users\royal\Documents\DND\5R\.codex\skills\official-dnd-ranking-review\SKILL.md`

A skill can point to another skill file by path and instruct the agent to read it. This is not automatic implicit loading: when using this homebrew skill, explicitly open the official skill file and apply only the shared standards listed below. Ignore official-only output rules, class README leaderboard rules, root `Rankings` workflow, official filename/marker rules, and official/UA/partner scope discovery unless the homebrew task explicitly needs them for comparison.

## Duplicated Content Delegated To Official Skill

The following content used to be duplicated in this homebrew skill. Do not restate it here; read and follow it from the official skill:

- Local-source verification and no model-memory rule for official content: official `## Non-Negotiable Rule`.
- Chinese translation requirement, including `起源专长`: official `## Non-Negotiable Rule`.
- Mojibake / GBK-CP936 handling when local Chinese text displays incorrectly: official `Required Workflow` local-source steps.
- 2024 spell-timing and “one spell with a spell slot per turn” analysis: official `Build the actual rules context before scoring`.
- Resource counting, action economy, concentration, unwanted interruption, severe costs, and feature-overlap analysis: official `Build the actual rules context before scoring`.
- “On par with” comparisons, damage-dice face counting, abuse-path auditing, `暗示术` / `群体暗示术`, high-level abuse frameworks, Divine Intervention / Wish / Glyph / Demiplane compression, and scroll / Magical Secrets / spell-list lock-in standards: official `Build the actual rules context before scoring`.
  - Especially preserve the official skill's `祈愿术` standard: the verified local 2024 text says the caster does not need to satisfy any prerequisite required by the target spell, including costly material components, to make the duplicated spell take effect. In this project, that includes the target spell's casting time unless a more specific local rule says otherwise. Apply this equally to any homebrew, subclass, build, item, or official route that actually casts `祈愿术`; differences in ranking come from access timing, frequency, restrictions, spell-list/preparation economy, proxy abuse, and downstream limits, not from changing what `祈愿术` itself does.
- Species, 起源专长, general feats, magic items, opportunity cost, replaceability, `猎人印记` vs `脆弱诅咒`, and resource-conversion comparisons: official `Build the actual rules context before scoring`.
- Rank order and rank definitions: official `Use the same scoring system`. This includes the current allowance for `B+` as the only lower-mid power subrank. `B-` may be used only for design-related scores under the official design-score rule; do not use `B-` for power/function/overall rankings, and do not invent `C+`, `C-`, `D+`, `D-`, or `E+` unless the official skill later defines them.
- Full-caster / near-full-caster compression, non-full-caster, half-caster, gish, skill-first, weapon mastery, magic item assumptions, and within-tier timing standards: official `Use the same scoring system`.
- Design-score separation, shared 2024 assumptions, and blunt Simplified Chinese output style: official `Apply design-score separation`, `Account for shared 2024 assumptions`, and `Output Style`.

Homebrew reviews still use these shared standards exactly. The homebrew-specific sections below only add source archiving, personal intent, output location, and improvement-advice rules.

## Non-Negotiable Homebrew Rule

Never evaluate a homebrew interaction with official content from model memory. If the homebrew mentions an official class, subclass, feature, feat, item, spell, monster stat block, condition, action, or rule term, first verify the current local text in `DND5e_chm`, using the shared verification rules from the official skill.

If a homebrew source contains both English and Chinese, use the Chinese text as authoritative for the archived `原文` unless the user says otherwise. Preserve homebrew-created names as written in the source. For official / partner / UA / third-party names embedded in homebrew text, use the verified Chinese translation from `DND5e_chm` in the review whenever it can be found.

Out-of-boundary or overpowered content is included in balance ranking. Do not silently “fix” it before scoring. Point it out in `详细评价` and `修改建议` as future refinement material.

## Required Workflow

1. Identify scope and output path.
   - Homebrew outputs go under `homebrews\Rankings`.
   - Use subdirectories by class/type, such as `牧师`, `圣武士`, `法师`, `游荡者`, etc.
   - Keep root `Rankings` as calibration/reference only, not as a homebrew output target.
   - `homebrews\Rankings\README.md` is deprecated. Do not create or update it.

2. Read standards in this order.
   - Read this homebrew skill.
   - Read the official skill file named in `## Skill Dependency`, applying only the delegated shared standards listed above.
   - Read `homebrews\Rankings\changelog.md` for homebrew-specific history.
   - Use root `Rankings\changelog.md` and existing root `Rankings` files as official / UA / partner / third-party calibration baselines.

3. Read the source homebrew file.
   - Use the current file in `homebrews`.
   - Archive the Chinese source text in `原文`; if both English and Chinese are present, use Chinese only unless the user asks otherwise.
   - Preserve author notes such as `附注`, `Note`, `设计意图`, `设计目标`, `个人意图`, or similar. These notes are part of `原文`.
   - If author notes state personal/table-specific design purpose, normal balance/function ranks still use the full ecosystem standard, but the review must also include `设计相关评分 - 个人期望`.
   - If the source says it is `基于...改编` / `based on...`, verify the origin resource before judging personal design purpose and adaptation quality. Prefer local project resources first (`DND5e_chm`, `5e Reference`, `Rankings`, `homebrews`, PDFs or text files named by the source). If the source cannot be verified locally and network is unavailable or not requested, state the uncertainty rather than inventing the baseline.
   - Explicit baseline rule: for `看门狗 Watch Dog`, consult `5e Reference\My New D20 Modern Campaign.pdf` before evaluating the referenced UA/D20 Modern baseline.

4. Compare current source against existing review.
   - If no ranking exists, create a new file and include `原文`.
   - If ranking exists, compare the current source Chinese text to its `## 原文` section.
   - If source changed, first archive the current ranking file to:
     `homebrews\Rankings\[class]\Archive\[subclass name] - [YYYYMMDD HHMMSS].md`
   - If only standards, wording, or calibration changed and source text did not change, update in place without archive.

5. Build official context and score.
   - Use the official skill’s shared rules-context and scoring standards.
   - Strictly compare homebrew balance/functionality against official first-party, UA, partner, and third-party published options already reviewed in root `Rankings`, not merely against its own base class or other homebrews.
   - Do not discount a homebrew because it is homebrew, and do not inflate it because it is only strong inside its own class.
   - Give `S+` only when it stands at the best-of-the-best ceiling across that full comparison pool.
   - Design scores should punish bad boundaries, unclear rules, broken action economy, resource loops, bounded accuracy breaks, and DM-dependent ambiguity, even when the feature is powerful.
   - Do not treat overlap with official subclasses as inherently invalid. Flag overlap only when the homebrew outperforms the official subclass in that official subclass’s main role or makes that niche mostly obsolete.

6. Write the review.
   - Output in Simplified Chinese.
   - Include `原文`.
   - Include team/rules position, feature-level `详细评价`, per-tier `分项评分`, vertical `综合评分`, `设计相关评分`, official baseline comparison / uncertainty notes, and `修改建议`.
   - If the source has personal design-purpose sections, include `设计相关评分 - 个人期望` after normal design scoring.
   - If the source is an explicit adaptation, include adaptation discussion in `详细评价`, `横向对照与不确定点`, or a dedicated `改编基准` section.
   - Do not repeat generic scoring boilerplate. Explain actual features, actions, resources, saves, concentration, interactions, official comparisons, and Tier curve.

`综合评分` must use this vertical table:

```markdown
## 综合评分
| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A | 具体说明为什么此阶段给这个综合强度。 |
| Tier 2（5-10） | B | 具体说明此阶段队伍定位、功能面、资源和横向比较。 |
| Tier 3（11-16） | C | 具体说明高等级变化。 |
| Tier 4（17-20） | C | 具体说明终局表现。 |
```

`具体理由` must explain whether the score comes mainly from the base class, from the homebrew increment, or from their interaction. A strong base class cannot erase a weak homebrew increment, and a strong homebrew increment can raise a weaker chassis only when it solves real tier problems.

7. Write improvement advice in the review file.
   - Do not rely on a central `homebrews\Rankings\README.md` for improvement advice.
   - Every review file should include `## 修改建议`.
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
   - For public-release advice, compare against official / UA / partner / third-party calibrated ecosystem standards.
   - For personal-intent advice, judge whether the text achieves the stated author purpose without pretending that personal intent changes normal balance ranks.

8. Update records.
   - Prepend concise changes to `homebrews\Rankings\changelog.md` when a new evaluation, archive, standard change, or calibration occurs.
   - Keep `homebrews\Rankings\changelog.md` in reverse chronological order: newest entries at the beginning.
   - Record when `homebrews\Rankings\README.md` is removed or intentionally not maintained under the current workflow.

## Practical Search Pattern

```powershell
rg -n "Homebrew Feature|中文名|English Name" .\homebrews
rg -n "Official Spell|Feat|Item|Feature|Monster|Rule" .\DND5e_chm
rg -n "原文|综合强度|设计质量|能力设计质量" .\homebrews\Rankings
```

Open the matched local source before writing. Search results are not enough when wording matters.

## Common Failure Modes To Avoid

- Forgetting to read the official skill’s delegated shared standards before scoring.
- Accidentally applying official-only output rules, root `Rankings` leaderboard rules, or official filename/source-marker rules to homebrew files.
- Using 2014 spell memory for 2024 spells, such as treating `睡眠术` as a hit-point pool instead of verifying the 5.5e saving-throw version.
- Treating a homebrew’s out-of-boundary feature as if it were already nerfed.
- Forgetting to archive a previous ranking after source text changes.
- Forgetting `原文`, or archiving English when the Chinese source is present.
- Calling a subclass `S+` merely because it exceeds its own class boundary.
- Giving high design scores just because a feature is powerful.
- Maintaining improvement advice only in `homebrews\Rankings\README.md` instead of each review file.
- Treating personal design intent as if it changed normal balance ranks, rather than adding `设计相关评分 - 个人期望`.
- Treating overlap with an official subclass as automatically invalid when the homebrew does not outperform that official subclass in its main role.
- Treating `基于...改编` as flavor only. Adaptation claims require checking the origin source and evaluating the quality of the 5.5e/2024 conversion.
