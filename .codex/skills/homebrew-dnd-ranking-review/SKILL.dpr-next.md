<!--
DPR NEXT BACKUP

This file preserves the experimental six-category DPR standards and calculation-tool workflow that were active before the current public review workflow returned to the legacy damage aspects.

Maintenance rule: when the active SKILL.md changes for reasons unrelated to damage-aspect taxonomy or DPR calculation workflow, sync the same non-DPR change into this backup file. Future changes to six-category DPR aspects, DPR calculation tables, near-range burst anchors, and related tooling guidance should be made here first, not in the active SKILL.md, until the new DPR system is explicitly re-enabled.
-->

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
- 5etools submodule and online CN raw-root strategy: official `Required Workflow` rules-text location steps. Homebrew reviews may use `5etools-src` and `5etools-cn` as the main structured search resources for official / UA / partner / third-party mechanics, including `data/` JSON and `search/index-*.json` indexes. Use `5etools-unearthed-arcana` as the local EN source for 5etools `loadextprerelease` UA / playtest JSON referenced by current or legacy UA discussions; treat its contents as UA / prerelease, not official published rules, unless a later official source republishes the option. Use `5etools-homebrew` as the local EN source for 5etools external homebrew / partner / third-party JSON referenced by `loadexthomebrew` or `index-partnered.json`; treat its contents as partner / third-party published calibration, not first-party official rules, unless a more specific project rule says otherwise. When CN text is needed for UA / partner / third-party calibration, also follow the official skill's verified online raw-root workflow: `https://ua.kiwee.top/_generated/index-sources.json` / `index-props.json` and `https://homebrew.kiwee.top/_generated/index-sources.json` / `index-props.json` can map source IDs and entity properties to full translated JSON files. Use those online CN JSON files when accessible, while falling back to local EN JSON plus `DND5e_chm`, `DND2014_legacy`, `5etools-cn\search`, and existing verified `Rankings` names when not accessible, when a translation appears stale, or when only part of the CN translation exists. Missing individual CN names / entries in an otherwise accessible online JSON should be resolved through `DND5e_chm` first and `DND2014_legacy` second before using a provisional translation. Do not treat `https://homebrew.kiwee.top/index.json` 404 as proof the CN partner content is missing; use the `_generated` indexes instead. Follow the official skill's same-name version-precedence, publish-date audit, checklist release-date, and same-lineage dedupe rules when using root `Rankings` as calibration: official 2014 + UA 2024 versions may require separate reviews, but partner / third-party 2024 / 5.5e versions supersede their 2014 / 5e counterparts unless a legacy comparison is explicitly requested. If no verified Chinese translation exists, mark any Chinese rendering as temporary / descriptive instead of treating it as official.
- SRD 5.1 / 5e / 2014 to SRD 5.2.1 / 5.5e / 2024 conversion audit: official `Required Workflow` local conversion reference and conversion checklist. Apply it when a homebrew adapts legacy official, UA, partner, third-party, SRD 5.1, or older-edition-like wording. Do not cite or commit `converting-to-srd-5.2.1.pdf`; use the official skill's recorded conversion rules, then verify current mechanics and Chinese names locally.
- Chinese translation requirement, including `起源专长`, plus the exception that common CN-community abbreviations such as `DPR`, `RAW`, `RAI`, `DM`, `PC`, `UA`, `BA`, `OA`, `ASI`, and source abbreviations do not need forced Chinese translation: official `## Non-Negotiable Rule`.
- Mojibake / GBK-CP936 handling when local Chinese text displays incorrectly: official `Required Workflow` local-source steps.
- 2024 spell-timing and “one spell with a spell slot per turn” analysis: official `Build the actual rules context before scoring`.
- Spell-level comparison wording for light/darkness, suppression, dispelling, and similar effects, including the 2024 `昼明术 Daylight` official pattern and how upcast/effective spell level should be handled: official `Build the actual rules context before scoring`.
- Open-ended boundary audit and encounter/story counter calibration: unbounded-looking target counts, action-economy compression, spell copying, stored spells, broad ally benefits, spell-slot-per-turn exceptions, narrow hard counters, damage/condition immunities, always-on detection, high passive skill floors, divination, and other story-axis breakers are investigation triggers rather than automatic defects. Verify current executable routes, costs, timing, counterplay, official ecosystem baselines, campaign-frequency, DM encounter/story design burden, raw frequency versus reliance, self-only versus party-wide scope, and whether the danger depends on extreme NPC/summon density, permissive DM setup, future unreleased resources, a narrow encounter category, or a specific campaign premise before changing rank or demanding a fix. Use the official skill's principle-level baselines and 5etools JSON lookup workflow instead of copying old single-example conclusions: official `Build the actual rules context before scoring`.
- Resource counting, action economy, concentration, stored-spell timing and caster identity, same-subclass feature stacking, base-class chassis stacking, exact attack-wording distinctions, post-roll / post-failure correction math, melee / short-range / multi-hit damage-increment resources, spell bounce / chain mechanics, Paladin smite / rider concentration checks, unwanted interruption, severe costs, and feature-overlap analysis: official `Build the actual rules context before scoring`.
- Six-category DPR scoring, including `近距爆发DPR（15尺内）`, `近距持续DPR（15尺内）`, `近距范围DPR（15尺内）`, `远程爆发DPR`, `远程持续DPR`, `远程范围DPR`, the 15-foot near-range threshold, finer distance tags, cold-start / prebuffed / setup-amortized burst windows, long-rest / short-rest / per-encounter / sustained repeatability labels, all-hit ceiling vs expected-DPR separation, conditional extra attack opportunities as a correction layer inside existing DPR / `团队增益` aspects, build-available route calculation, strongest legal route listing, base-class all-aspect DPR tables, subclass DPR-delta tables, and brief `F` explanations for impossible DPR aspects: official `Use the same scoring system` and `Write feature-level reviews`.
- Dual-wield / `迅击` / `双持客` hit-count amplification, including the current conditional Paladin standard, feat-opportunity-cost audit, Fighter `长柄武器大师` / `巨武器大师` comparison, smite-spell comparison, and setup-tempo analysis: official `Build the actual rules context before scoring`.
- “On par with” comparisons, damage-dice face counting, abuse-path auditing, `暗示术` / `群体暗示术`, high-level abuse frameworks, Divine Intervention / Wish / Glyph / Demiplane compression, and scroll / Magical Secrets / spell-list lock-in standards: official `Build the actual rules context before scoring`.
- Species, 起源专长, general feats, magic items, opportunity cost, replaceability, `猎人印记` vs `脆弱诅咒`, and resource-conversion comparisons: official `Build the actual rules context before scoring`.
- Class-specific 2024 spell-preparation mechanics, including prepared-spell count, when preparation choices are made, long-rest replacement limits, level-up replacement limits, always-prepared spells, spellbook preparation, and the distinction between expanding a preparation menu and actually preparing every spell on that menu: official `Build the actual rules context before scoring`.
- Official compatibility assumptions used as calibration baselines, including third-party 5e-era class patches and narrow class-specific feat assumptions, must be read from the official skill rather than redefined here. Do not generalize those assumptions to unrelated homebrews unless the homebrew review explicitly compares to that published option.
- Tooling hygiene for shared maintenance scripts: official `## Tooling Hygiene`. Homebrew work may use the same tracked maintenance scripts when relevant, especially `tools\update_readme_toc.py` and `tools\audit_design_scores.py`, but one-off homebrew rewrite / calibration / generation helpers must stay local and ignored unless promoted into reusable infrastructure.
- Rank order and rank definitions: official `Use the same scoring system`. This includes the current allowance for `B+` as the only lower-mid power subrank. Design-only subranks such as `B-`, `C+`, `C-`, `D+`, `D-`, and `E+` may be used only under the official design-score rule when the reason truly needs that precision; do not use those design-only subranks for power/function/overall rankings.
- Full-caster / near-full-caster compression, non-full-caster, half-caster, gish, skill-first, weapon mastery, magic item assumptions, and within-tier timing standards: official `Use the same scoring system`.
- Design-score separation, design-expression drift checks, latest-online-lore verification for setting-bound concepts, shared 2024 assumptions, and blunt Simplified Chinese output style: official `Apply design-score separation`, `Account for shared 2024 assumptions`, and `Output Style`. Use the official skill's current lore-bound-source workflow when a homebrew adapts or compares against setting-bound published content.

Homebrew reviews still use these shared standards exactly. The homebrew-specific sections below only add source archiving, personal intent, output location, and improvement-advice rules.

## Non-Negotiable Homebrew Rule

Never evaluate a homebrew interaction with official content from model memory. If the homebrew mentions an official class, subclass, feature, feat, item, spell, monster stat block, condition, action, or rule term, first verify the current mechanics through `5etools-src` / `5etools-cn` JSON when available, then confirm the Chinese name and local wording through `DND5e_chm` or, for missing legacy 5e-era material, `DND2014_legacy`, using the shared verification rules from the official skill.

If a homebrew source contains both English and Chinese, use the Chinese text as authoritative for the archived `原文` unless the user says otherwise. Preserve homebrew-created names as written in the source. For official / partner / UA / third-party names embedded in homebrew text, use the verified Chinese translation from `DND5e_chm` in the review whenever it can be found. Common abbreviations already understood by Chinese D&D communities do not need to be translated into awkward Chinese wording; keep them when they are the clearer community term, and explain once only when context makes them ambiguous.

Out-of-boundary or overpowered content is included in balance ranking. Do not silently “fix” it before scoring. Point it out in `详细评价` and `修改建议` as future refinement material.

If a homebrew uses a design pattern that already exists in official 2024 rules but the official rule itself leaves a relevant wording boundary unresolved, do not demand that the homebrew solve that official ambiguity as a mandatory wording fix. Examples include `祈愿术` duplicating spells and `进阶神圣干预` choosing `祈愿术`. In this situation, the review should state that the official RAW is itself open-ended or table-ruling-sensitive. The absence of extra regulator wording in the homebrew is not, by itself, a `必须修改` item and should not by itself lower `设计质量` or `能力设计质量`; apply design penalties only for ambiguity, abuse paths, or resource loops introduced beyond the comparable official pattern.

Treat long-history open-ended spells and rules patterns as normal D&D design. `祈愿术 Wish` is not abnormal merely because it is broad, DM-adjudicated, or historically open-ended; similar multi-edition spells/features should be judged from their actual current wording and normal ecosystem role, not from LLM-style fear of unboundedness. Spell duplication through `祈愿术` is normally resolved by the spell's own text plus tabletop DM adjudication. For homebrew that simply grants or references `祈愿术`, do not require a subclass-specific sidebar that tries to settle every `Wish` duplication question; such a sidebar can be worse design if it looks like it overwrites official `Wish` globally or creates a private `Wish` variant just for the subclass. A homebrew may be criticized when it changes the historical/official bargain: waiving the spell's normal stress, shifting the cost to a proxy, bypassing the loss chance, shortening cooldowns, creating repeatable cost-free loops, compressing action economy beyond the spell's own verified rule, or adding a class/subclass synergy that makes the old spell do something meaningfully new. Do not require extra regulator text solely to make an already-proven open-ended official spell look safer.

When a homebrew wording has a clear inheritance relationship with an official rule, feature, spell, action, or class mechanic, evaluate it by normal rules inheritance. Parts that are not explicitly changed continue to work as the original official rule works. Do not require the homebrew to repeat every inherited part, and do not treat the absence of repeated inherited wording as a design flaw, wording flaw, or reason to lower `设计质量` / `能力设计质量`. Conversely, if the homebrew explicitly says it ignores, replaces, waives, changes, or adds a cost/condition/timing/component/resource, that explicit text overrides the inherited rule to that extent and must be scored as written.

Example: local 2024 Cleric `神圣干预` says the chosen Cleric spell is cast as part of the Magic action, without a spell slot or material components. Because it explicitly waives spell slots and material components, those parts override normal spellcasting. Other spell rules that are not waived still apply unless the feature says otherwise. By contrast, if a homebrew feature says the character may cast a Wizard spell as part of an Attack action but does not say spell slots, components, concentration, range, targets, or other spell rules are waived, the default reading is that those normal spellcasting rules still apply.

Do not ask the author to add long boilerplate such as "this otherwise follows all normal spellcasting rules" unless the text creates a real ambiguity. Long, repetitive clarification of inherited official rules can itself reduce readability and elegance; if a feature repeatedly restates ordinary rules that were not being changed, mark it as duplicated wording / rules bloat and consider lowering wording-related `能力设计质量` or `设计质量` when the repetition materially harms public readability.

Likewise, do not ask a homebrew feature to restate normal d20 / attack-roll inheritance such as "natural 1 still misses" when the feature merely adds a bonus, replacement value, or rider to an attack roll and does not say it overrides the attack-roll rule. Verify the current 2024 local rule first, then score the feature as inheriting that rule. Only require explicit text if the feature actually replaces the d20 result, changes what counts as a hit / miss / critical hit, or creates a real uncertainty about whether the normal attack-roll rule still applies.

For homebrew design scoring, use the same concise-text principle as the official skill: inherited official rules should remain concise, while self-made exceptions must define the new boundary they create. A formal sidebar, published rule note, or clearly included rules appendix can protect `能力设计质量` when it explains a complex exception without bloating the main feature. Ordinary `附注`, task notes, prompts, blind-review responses, private discussion, or author meta-commentary do not repair public-facing rules text unless the source or user explicitly says that material is meant to be published with the subclass.

When a review has suggestions for fixing that comparable official RAW problem, put them in a standalone `## 官方RAW修复建议` section rather than inside `详细评价`, `横向对照与不确定点`, or `修改建议`. This section is for official-rule repair options and their table impact, not for required homebrew changes.

For power, functionality, and balance ranks related to that official ambiguity, do not default to a conservative-RAI / permissive-RAW split when official references exist. First perform horizontal calibration: identify which official classes, subclasses, spells, features, builds, or spell-list owners already have the same or similar boundary-crossing resource; record their level, resource frequency, action cost, spell-list / preparation economy, current rank in root `Rankings`, and the exact role that resource plays in that rank. Then score the homebrew feature by comparing its timing, chassis, resource chain, synergy, cooldown, scope, and table burden against those official baselines. If the official baseline is `S` and the homebrew has narrower access, later timing, or harsher cost, do not call it `S+` merely because it crosses its own class boundary; if the homebrew adds stronger synergy than the official owner, state the exact rank increase and why. Use `EX` only for power/function/balance scores that exceed the whole official/UA/partner/third-party ecosystem ceiling; use `S+` for decisive increment above ordinary `S` that is not ecosystem-breaking.

Example: for `迷思卓诺之誓` level-20 `理想宣言`, compare the `祈愿术` access against Wizard as a Tier 4 `S` full-caster package with spellbook / ritual / high-level arcane breadth, Cleric as a Tier 4 `S` class whose `进阶神圣干预` can choose `祈愿术`, and reviewed Wizard multiclass builds that still sit at Tier 4 `S` rather than `S+` when they gain ninth-level spells late. The Paladin feature should receive real credit as a full-caster-boundary, `S`-level endpoint for the roles `祈愿术` actually covers, but it should not inherit Wizard's spellbook economy or Cleric's full divine toolkit; decide the exact feature and overall Tier 4 rank from the feature's actual level-20-only, Heroic-Inspiration-gated, song-ending, cooldown-limited access.

Discuss RAI / RAW effects on power, functionality, or balance ranking only when no usable official reference or reviewed analogue exists. In that case, explain which reading is being scored, why that reading is the most defensible for the project, and how the alternate reading would change the rank.

Every homebrew review must be completed as an individual evaluation of the latest source text. For ordinary public-release review sections, the only valid inputs are:
- the latest formal homebrew source text outside author-note / meta sections;
- this skill and the delegated shared standards from the official skill;
- verified official / UA / partner / third-party calibration files and version-matched community discussion.

Do not let the user prompt, current conversation, our conversation, previous assistant wording, older review text, archived review files, archived source versions, source-diff direction, blind-review comments, GPT review files, author notes, personal notes, task notes, or change-comparison narrative determine public-facing power ranks, function ranks, balance ranks, overall ranks, public-oriented design scores, `详细评价`, `分项评分`, or `综合评分`. Those materials may tell you what to inspect, but the conclusion must be rebuilt from the latest formal text and the standards. If the user provides a new rule, criterion, or factual assumption that should affect ranking, first record it in the relevant skill or changelog, then evaluate from that rule. If the prompt provides a preferred result, treat it only as a hypothesis to verify.

For both power and design rankings, "out of context" means any note-only material or content-unrelated outside material is excluded from scoring. Do not use author history, intended changes, abandoned versions, archived versions, archived reviews, blind-review pressure, unrelated community comments, personal therapy/context, private conversation, or non-published side documents to raise or lower ranks. Do not give credit because the current version fixed an archived version's problem, and do not penalize because an older version had that problem; score only the current formal text. Only use outside material when it directly verifies or calibrates the current formal content: official / UA / partner / third-party source text, same-version rules references, verified errata/FAQ/Sage Advice, version-matched community rules discussion about the same mechanics, and existing project calibration files.

Resource-enablements are not note-derived personal context. If the formal source, user task, project standard, or review file explicitly enables an expanded resource, optional rule, UA package, partner/third-party book, homebrew module, house rule, firearm era, feat pool, spell package, magic-item environment, or other external rules resource for the review, treat that resource as a shared campaign environment for everyone who can legally access it. Do not score the reviewed homebrew as if it alone owns the enabled resource. Give credit only when the homebrew has exclusive access, earlier timing, lower opportunity cost, better action economy, stronger scaling, better compatibility, or a feature that uniquely exploits that shared resource. If the enabled resource materially buffs official / UA / partner / third-party competitors too, horizontally recalibrate against those competitors before assigning ranks.

When assigning ordinary public-facing design ranks, deliberately simulate an out-of-context reader. Score `设计质量`, `主题`, `能力设计质量`, and `主题与能力关联度` from the formal public text and shared rubric, not from the creation story, author recovery, previous-version trauma, assistant/user conversation, or how much better the current version is than an older draft. Put those materials only in standalone sections such as `版本变迁讨论`, `附注任务处理`, `设计相关评分 - 个人期望`, or `历史版本价值`. A homebrew can deserve high creator-facing / historical praise while still receiving a lower public `设计质量` because the rules surface is dense, edge-case heavy, or costly for strangers to run.

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
   - If the source says it is `基于...改编` / `based on...`, verify the origin resource before judging personal design purpose and adaptation quality. Prefer structured local project resources first (`5etools-src`, `5etools-cn`, then `DND5e_chm`, `DND2014_legacy`, `Rankings`, `homebrews`, PDFs or text files named by the source). If the source cannot be verified locally and network is unavailable or not requested, state the uncertainty rather than inventing the baseline.
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
   - Include team/rules position, feature-level `详细评价`, per-tier `分项评分`, vertical `综合评分`, `设计相关评分`, official baseline comparison / uncertainty notes, DPR calculation sections when the homebrew affects DPR, and `修改建议`.
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
   - Do not pad `修改建议` with invented defects. It is valid for `必须修改` to be `无`, and it is useful to say that a feature needs no change when it is clear, thematic, sufficiently regulated, or strong but acceptable. Good review preserves good design instead of only removing risk.
   - For public-release advice, compare against official / UA / partner / third-party calibrated ecosystem standards.
   - For personal-intent advice, judge whether the text achieves the stated author purpose without pretending that personal intent changes normal balance ranks.
   - Homebrew reviews may also include `## 开放改进问题` when the issue is better framed as a design question than a direct fix. Use the same independent-improvement logic as the official skill, but keep formal public-purpose judgment separate from notes, prompts, blind reviews, and private author discussion. If the open question comes from note-derived material, place it in the personal/notes-related section rather than using it to justify public ranking.

8. Update records.
   - Prepend concise changes to `homebrews\Rankings\changelog.md` when a new evaluation, archive, standard change, or calibration occurs.
   - Keep `homebrews\Rankings\changelog.md` in reverse chronological order: newest entries at the beginning.
   - Record when `homebrews\Rankings\README.md` is removed or intentionally not maintained under the current workflow.

## Practical Search Pattern

```powershell
rg -n "Homebrew Feature|中文名|English Name" .\homebrews
rg -n "Official Spell|Feat|Item|Feature|Monster|Rule" .\5etools-src\data .\5etools-cn\data .\DND5e_chm .\DND2014_legacy
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
