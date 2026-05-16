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
- Chinese translation requirement, including `起源专长`, plus the exception that common CN-community abbreviations such as `DPR`, `RAW`, `RAI`, `DM`, `PC`, `UA`, `BA`, `OA`, `ASI`, and source abbreviations do not need forced Chinese translation: official `## Non-Negotiable Rule`.
- Mojibake / GBK-CP936 handling when local Chinese text displays incorrectly: official `Required Workflow` local-source steps.
- 2024 spell-timing and “one spell with a spell slot per turn” analysis: official `Build the actual rules context before scoring`.
- Spell-level comparison wording for light/darkness, suppression, dispelling, and similar effects, including the 2024 `昼明术 Daylight` official pattern and how upcast/effective spell level should be handled: official `Build the actual rules context before scoring`.
- Resource counting, action economy, concentration, stored-spell timing and caster identity such as `储法戒指` / `奥法暂滞`-style storage, same-subclass feature stacking, base-class chassis stacking, exact `武器攻击` / `近战武器攻击` / `远程武器攻击` wording, melee / short-range / multi-hit damage-increment resources, 2024 `繁彩球 Chromatic Orb` bounce chance / maximum bounce calibration, Paladin `神恩` / smite-spell concentration exception handling, unwanted interruption, severe costs, and feature-overlap analysis: official `Build the actual rules context before scoring`.
- Dual-wield / `迅击` / `双持客` hit-count amplification, including the current conditional Paladin standard, feat-opportunity-cost audit, Fighter `长柄武器大师` / `巨武器大师` comparison, smite-spell comparison, and setup-tempo analysis: official `Build the actual rules context before scoring`.
- “On par with” comparisons, damage-dice face counting, abuse-path auditing, `暗示术` / `群体暗示术`, high-level abuse frameworks, Divine Intervention / Wish / Glyph / Demiplane compression, and scroll / Magical Secrets / spell-list lock-in standards: official `Build the actual rules context before scoring`.
- Species, 起源专长, general feats, magic items, opportunity cost, replaceability, `猎人印记` vs `脆弱诅咒`, and resource-conversion comparisons: official `Build the actual rules context before scoring`.
- Class-specific 2024 spell-preparation mechanics, including prepared-spell count, when preparation choices are made, long-rest replacement limits, level-up replacement limits, always-prepared spells, spellbook preparation, and the distinction between expanding a preparation menu and actually preparing every spell on that menu: official `Build the actual rules context before scoring`.
- Official compatibility assumptions used as calibration baselines, including third-party 5e-era class patches and narrow class-specific feat assumptions, must be read from the official skill rather than redefined here. Current examples include `血猎手` / `邪狱使` compatibility patches and the `铳士`-only `枪手` assumption; do not generalize those assumptions to unrelated homebrews unless the homebrew review explicitly compares to that published option.
- Tooling hygiene for shared maintenance scripts: official `## Tooling Hygiene`. Homebrew work may use the same tracked maintenance scripts when relevant, especially `tools\update_readme_toc.py` and `tools\audit_design_scores.py`, but one-off homebrew rewrite / calibration / generation helpers must stay local and ignored unless promoted into reusable infrastructure.
- Rank order and rank definitions: official `Use the same scoring system`. This includes the current allowance for `B+` as the only lower-mid power subrank. Design-only subranks such as `B-`, `C+`, `C-`, `D+`, `D-`, and `E+` may be used only under the official design-score rule when the reason truly needs that precision; do not use those design-only subranks for power/function/overall rankings.
- Full-caster / near-full-caster compression, non-full-caster, half-caster, gish, skill-first, weapon mastery, magic item assumptions, and within-tier timing standards: official `Use the same scoring system`.
- Design-score separation, design-expression drift checks, latest-online-lore verification for setting-bound concepts, shared 2024 assumptions, and blunt Simplified Chinese output style: official `Apply design-score separation`, `Account for shared 2024 assumptions`, and `Output Style`. This includes the official skill's explicit lore-bound ranges such as Exandria / Critical Role / Blood Hunter, Ravenloft, Dragonlance, Strixhaven, and other recorded setting-bound sources when a homebrew adapts or compares against them.

Homebrew reviews still use these shared standards exactly. The homebrew-specific sections below only add source archiving, personal intent, output location, and improvement-advice rules.

## Non-Negotiable Homebrew Rule

Never evaluate a homebrew interaction with official content from model memory. If the homebrew mentions an official class, subclass, feature, feat, item, spell, monster stat block, condition, action, or rule term, first verify the current local text in `DND5e_chm`, using the shared verification rules from the official skill.

If a homebrew source contains both English and Chinese, use the Chinese text as authoritative for the archived `原文` unless the user says otherwise. Preserve homebrew-created names as written in the source. For official / partner / UA / third-party names embedded in homebrew text, use the verified Chinese translation from `DND5e_chm` in the review whenever it can be found. Common abbreviations already understood by Chinese D&D communities do not need to be translated into awkward Chinese wording; keep them when they are the clearer community term, and explain once only when context makes them ambiguous.

Out-of-boundary or overpowered content is included in balance ranking. Do not silently “fix” it before scoring. Point it out in `详细评价` and `修改建议` as future refinement material.

If a homebrew uses a design pattern that already exists in official 2024 rules but the official rule itself leaves a relevant wording boundary unresolved, do not demand that the homebrew solve that official ambiguity as a mandatory wording fix. Examples include `祈愿术` duplicating spells and `进阶神圣干预` choosing `祈愿术`. In this situation, the review should state that the official RAW is itself poorly bounded or table-ruling-sensitive. The absence of extra regulator wording in the homebrew is not, by itself, a `必须修改` item and should not by itself lower `设计质量` or `能力设计质量`; apply design penalties only for ambiguity, abuse paths, or resource loops introduced beyond the comparable official pattern.

When a homebrew wording has a clear inheritance relationship with an official rule, feature, spell, action, or class mechanic, evaluate it by normal rules inheritance. Parts that are not explicitly changed continue to work as the original official rule works. Do not require the homebrew to repeat every inherited part, and do not treat the absence of repeated inherited wording as a design flaw, wording flaw, or reason to lower `设计质量` / `能力设计质量`. Conversely, if the homebrew explicitly says it ignores, replaces, waives, changes, or adds a cost/condition/timing/component/resource, that explicit text overrides the inherited rule to that extent and must be scored as written.

Example: local 2024 Cleric `神圣干预` says the chosen Cleric spell is cast as part of the Magic action, without a spell slot or material components. Because it explicitly waives spell slots and material components, those parts override normal spellcasting. Other spell rules that are not waived still apply unless the feature says otherwise. By contrast, if a homebrew feature says the character may cast a Wizard spell as part of an Attack action but does not say spell slots, components, concentration, range, targets, or other spell rules are waived, the default reading is that those normal spellcasting rules still apply.

Do not ask the author to add long boilerplate such as "this otherwise follows all normal spellcasting rules" unless the text creates a real ambiguity. Long, repetitive clarification of inherited official rules can itself reduce readability and elegance; if a feature repeatedly restates ordinary rules that were not being changed, mark it as duplicated wording / rules bloat and consider lowering wording-related `能力设计质量` or `设计质量` when the repetition materially harms public readability.

When a review has suggestions for fixing that comparable official RAW problem, put them in a standalone `## 官方RAW修复建议` section rather than inside `详细评价`, `横向对照与不确定点`, or `修改建议`. This section is for official-rule repair options and their table impact, not for required homebrew changes.

For power, functionality, and balance ranks related to that official ambiguity, do not default to a conservative-RAI / permissive-RAW split when official references exist. First perform horizontal calibration: identify which official classes, subclasses, spells, features, builds, or spell-list owners already have the same or similar boundary-crossing resource; record their level, resource frequency, action cost, spell-list / preparation economy, current rank in root `Rankings`, and the exact role that resource plays in that rank. Then score the homebrew feature by comparing its timing, chassis, resource chain, synergy, cooldown, scope, and table burden against those official baselines. If the official baseline is `S` and the homebrew has narrower access, later timing, or harsher cost, do not call it `S+` merely because it crosses its own class boundary; if the homebrew adds stronger synergy than the official owner, state the exact rank increase and why. Use `EX` only for power/function/balance scores that exceed the whole official/UA/partner/third-party ecosystem ceiling; use `S+` for decisive increment above ordinary `S` that is not ecosystem-breaking.

Example: for `迷思卓诺之誓` level-20 `理想宣言`, compare the `祈愿术` access against Wizard as a Tier 4 `S` full-caster package with spellbook / ritual / high-level arcane breadth, Cleric as a Tier 4 `S` class whose `进阶神圣干预` can choose `祈愿术`, and reviewed Wizard multiclass builds that still sit at Tier 4 `S` rather than `S+` when they gain ninth-level spells late. The Paladin feature should receive real credit as a full-caster-boundary, `S`-level endpoint for the roles `祈愿术` actually covers, but it should not inherit Wizard's spellbook economy or Cleric's full divine toolkit; decide the exact feature and overall Tier 4 rank from the feature's actual level-20-only, Heroic-Inspiration-gated, song-ending, cooldown-limited access.

Discuss RAI / RAW effects on power, functionality, or balance ranking only when no usable official reference or reviewed analogue exists. In that case, explain which reading is being scored, why that reading is the most defensible for the project, and how the alternate reading would change the rank.

Every homebrew review must be completed as an individual evaluation of the latest source text. For ordinary public-release review sections, the only valid inputs are:
- the latest formal homebrew source text outside author-note / meta sections;
- this skill and the delegated shared standards from the official skill;
- verified official / UA / partner / third-party calibration files and version-matched community discussion.

Do not let the user prompt, current conversation, previous assistant wording, older review text, source-diff direction, blind-review comments, GPT review files, or change-comparison narrative determine public-facing rankings, public-oriented design scores, `详细评价`, `分项评分`, or `综合评分`. Those materials may tell you what to inspect, but the conclusion must be rebuilt from the latest formal text and the standards. If the user provides a new rule, criterion, or factual assumption that should affect ranking, first record it in the relevant skill or changelog, then evaluate from that rule. If the prompt provides a preferred result, treat it only as a hypothesis to verify.

Version-to-version changes should be discussed in a standalone section such as `本次改动判断` or `版本变化说明`. That section may explain what changed and whether the changed text matters, but the changed-from-previous-version narrative must not appear as a justification inside public `详细评价`, public `设计相关评分`, balance/function ranks, or `综合评分`. Public review content should read as a review of the current version, not as a response to the previous version or to the prompt.

## Required Workflow

1. Identify scope and output path.
   - Homebrew outputs go under `homebrews\Rankings`.
   - Use subdirectories by class/type, such as `牧师`, `圣武士`, `法师`, `游荡者`, etc.
   - Keep root `Rankings` as calibration/reference only, not as a homebrew output target.
   - `homebrews\Rankings\README.md` is deprecated. Do not create or update it.
   - Do not create 神圣奇术 / Theurgy mappings for homebrew Cleric domains unless the user explicitly asks for that mapping. If explicitly requested, put the mapped review files under `homebrews\Rankings\法师\神圣奇术`, but do not create `homebrews\Rankings\法师\神圣奇术\README.md`; homebrew Theurgy mappings remain ordinary standalone subclass review files, not a class-like Theurgy hub.
   - Every active homebrew review Markdown file, including standalone subclass files, must include an up-to-date `## 目录` near the top and maintain it when headings change. Skip `homebrews\Rankings\changelog.md` and files under `Archive`.
   - If a future user explicitly asks to create any homebrew `README.md`, include the same up-to-date `## 目录` near the top and maintain it when headings change. Do not create homebrew README files by default.

2. Read standards in this order.
   - Read this homebrew skill.
   - Read the official skill file named in `## Skill Dependency`, applying only the delegated shared standards listed above.
   - Read `homebrews\Rankings\changelog.md` for homebrew-specific history.
   - Use root `Rankings\changelog.md` and existing root `Rankings` files as official / UA / partner / third-party calibration baselines.

3. Read the source homebrew file.
   - Use the current file in `homebrews`.
   - Archive the Chinese source text in `原文`; if both English and Chinese are present, use Chinese only unless the user asks otherwise.
   - Preserve author notes such as `附注`, `Note`, `设计意图`, `设计目标`, `个人意图`, or similar. These notes are part of `原文`.
   - For the ordinary public-release review, treat author notes as out-of-scope evidence. Do not use note contents to justify `详细评价`, balance/function ranks, `综合评分`, or ordinary public-facing design ranks. Those sections evaluate only the playable rules text, public-facing theme text, and mechanics outside the note section.
   - Default assumption: anything under an author-note / notes section is not part of the homebrew's formal published text and would be removed before publication, unless the source or user explicitly says a specific note is meant to remain in the published text. This includes `附注`, `Note`, `设计意图`, `设计目标`, `个人意图`, task lists, blind-review prompts, implementation comments, and similar meta text.
   - External materials that are introduced only by the notes section inherit the same exclusion for public-release scoring. This includes English drafts, prompts, GPT / human blind reviews, review notes, implementation comments, and external feedback files named by notes. You may discuss them in `附注任务材料处理`, `设计相关评分 - 个人期望`, or advice sections when the user asks, but they must not determine public-purpose `详细评价`, balance/function ranks, `综合评分`, or ordinary design ranks.
   - If a note-derived external review points out a possible issue, verify the issue independently from the formal homebrew text, official local rules, and ecosystem calibration before using it. In public-purpose sections, present the conclusion as your own objective analysis of the formal text, not as “the blind review said so.”
   - If author notes state personal/table-specific design purpose, normal balance/function ranks still use the full ecosystem standard, but the review must also include `设计相关评分 - 个人期望`.
   - Do not cite or rely on author-note contents when justifying ordinary non-personal design ranks such as `设计质量`, `主题`, `能力设计质量`, or `主题与能力关联度`. Those ranks judge the text and mechanics as public-facing material. Mention note contents only in `设计相关评分 - 个人期望`, personal-intent advice, or a neutral source-change note such as `本次改动判断`, and only under the aspect they actually inform, such as stated private goal, intended table power, author fantasy, adaptation purpose, or pending author questions.
   - If the source says it is `基于...改编` / `based on...`, verify the origin resource before judging personal design purpose and adaptation quality. Prefer local project resources first (`DND5e_chm`, `5e Reference`, `Rankings`, `homebrews`, PDFs or text files named by the source). If the source cannot be verified locally and network is unavailable or not requested, state the uncertainty rather than inventing the baseline.
   - For `看门狗 Watch Dog` or any homebrew that references 5e-era UA / legacy-compatible modern firearm rules, follow the official skill's `DND2014_legacy\其他\UA\城市规则.html` baseline and firearm-category mapping. Use the CN translated legacy source, not an external or obsolete PDF path, as the review source.

4. Compare current source against existing review.
   - If no ranking exists, create a new file and include `原文`.
   - If ranking exists, compare the current source Chinese text to its `## 原文` section.
   - If source changed, first archive the current ranking file to:
     `homebrews\Rankings\[class]\Archive\[subclass name] - [YYYYMMDD HHMMSS].md`
   - If source changed for an explicitly requested homebrew Theurgy mapping under `homebrews\Rankings\法师\神圣奇术`, archive the old mapped review under `homebrews\Rankings\法师\神圣奇术\Archive`, not directly under the Wizard directory.
   - If only standards, wording, or calibration changed and source text did not change, update in place without archive.

5. Build official context and score.
   - Use the official skill’s shared rules-context and scoring standards.
   - Strictly compare homebrew balance/functionality against official first-party, UA, partner, and third-party published options already reviewed in root `Rankings`, not merely against its own base class or other homebrews.
   - Do not discount a homebrew because it is homebrew, and do not inflate it because it is only strong inside its own class.
   - Give `EX` only when it stands at the best-of-the-best, ecosystem-breaking ceiling across that full comparison pool. Give `S+` when it clearly beats ordinary `S` through real feature increment but does not reach `EX`.
   - Design scores should punish bad boundaries, unclear rules, broken action economy, resource loops, bounded accuracy breaks, and DM-dependent ambiguity, even when the feature is powerful.
   - Do not treat overlap with official subclasses as inherently invalid. Flag overlap only when the homebrew outperforms the official subclass in that official subclass’s main role or makes that niche mostly obsolete.
   - For homebrew Paladin Sacred Oaths, do not mechanically require the 7th-level feature to be an Aura. Not every official Paladin subclass uses a level-7 aura pattern. The correct question is whether the 7th-level feature opens a meaningful new subclass dimension: team protection, battlefield role, target access, action-economy change, anti-caster value, noncombat identity, or a clearer oath/theme expression. If the subclass also lacks Oath Spells, has an unreliable Channel Divinity, or already spent earlier budget on a narrow combat module, then a 7th-level feature that only increases the same dice/resources/numbers should be criticized as narrow functional growth rather than as "missing an aura."

6. Write the review.
   - Output in Simplified Chinese.
   - Include `原文`.
   - Include team/rules position, feature-level `详细评价`, per-tier `分项评分`, vertical `综合评分`, `设计相关评分`, official baseline comparison / uncertainty notes, and `修改建议`.
   - If the review identifies an official RAW ambiguity and has suggestions on how to fix that official wording, include `## 官方RAW修复建议` as its own section and include it in the TOC.
   - If the source has personal design-purpose sections, include `设计相关评分 - 个人期望` after normal design scoring.
   - Keep note-derived content out of `详细评价`, `分项评分`, `综合评分`, and the ordinary `设计相关评分` table. The normal design table may discuss public text, mechanics, clarity, theme expression, and ecosystem health; the personal table may discuss whether the notes' stated goals are achieved.
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
- Calling a subclass `S+` merely because it exceeds its own class boundary, or calling it `EX` when it is only a strong `S+` increment rather than ecosystem-breaking.
- Giving high design scores just because a feature is powerful.
- Maintaining improvement advice only in `homebrews\Rankings\README.md` instead of each review file.
- Treating personal design intent as if it changed normal balance ranks, rather than adding `设计相关评分 - 个人期望`.
- Citing author notes in `详细评价`, ordinary balance/function ranks, `综合评分`, or ordinary non-personal design ranks. Note contents belong in `设计相关评分 - 个人期望`, personal-intent advice, or neutral source-change notes, not in public-facing review justification.
- Treating anything under `附注` / `Note` / design-intent sections as formal public homebrew text by default. Archive it in `原文`, but assume it is removed from a published version unless explicitly marked otherwise.
- Letting note-derived external materials such as GPT blind reviews, prompts, English drafts, or private feedback determine public-purpose rankings or design scores. Verify any useful point independently against the formal homebrew text and official rules before using it in public-purpose analysis.
- Treating overlap with an official subclass as automatically invalid when the homebrew does not outperform that official subclass in its main role.
- Treating `基于...改编` as flavor only. Adaptation claims require checking the origin source and evaluating the quality of the 5.5e/2024 conversion.
- Using a conservative-RAI / permissive-RAW split for rank decisions when official or reviewed analogues exist. Horizontal calibration comes first; RAI / RAW rank deltas are only for cases without usable references.
