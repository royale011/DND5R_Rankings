---
name: official-dnd-ranking-review
description: Use for official, partner, UA, third-party published, or legacy-compatible D&D 5.5e/2024/5R ranking and review work in this project. Enforces local DND5e_chm source verification, Rankings/changelog.md criteria, version matching for community comments, full rule/resource/action/spell/feat interaction analysis, and prevents using model memory for class/subclass feature text.
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
   - If `Get-Content`, `Select-String`, or `rg` displays mojibake for Chinese source text, do not guess the translation. Re-read the file with the correct local encoding, commonly GBK/CP936 for this repository, or inspect another local index/list page. Example PowerShell pattern: `[System.Text.Encoding]::GetEncoding(936).GetString([System.IO.File]::ReadAllBytes($path))`. Only write the Chinese name after this check.
   - Verify the class/subclass Chinese name before choosing the output directory, filename, and top-level heading. The filename must be `[verified subclass Chinese name].md` for first-party official content, or `[verified subclass Chinese name]（source marker）.md` for UA / partner / third-party content; class summaries must stay as `README.md` inside the verified class-name directory. If a previous file has the wrong Chinese name or lacks a required source marker, move/rename it rather than creating a duplicate.

4. Version-lock the review.
   - Only analyze features present in the verified local source.
   - If a previous review file contains old-version features, remove or correct them.
   - If a feature cannot be reliably found locally, explicitly say the source could not be localized and keep the analysis conservative. Do not invent feature names.

5. Build the actual rules context before scoring.
   - Identify which core or supplement rules the feature text relies on. Do not treat a feature sentence in isolation when PHB / DMG / MM / XGE / TCE / FRHoF or another local rule changes the real effect. Example: under 2024 `每回合仅能施展一道消耗法术位的法术 One Spell with a Spell Slot per Turn`, old bonus-action spell limits may be redundant or less meaningful than in 2014.
   - Community calibration for 2024 spell timing: discussions on the 2024 one-slot-spell rule commonly distinguish "spending a spell slot" from casting without a slot through a feature, item, scroll, or other special rule. When ranking action-economy compression, do not automatically apply the old 2014 bonus-action spell restriction. Verify whether the second spell actually expends a spell slot, whether a long casting time is already consuming the Magic action and concentration each turn, when the slot is expended, and whether the character still has the action / bonus action / reaction needed. This can make no-slot spell access, magic items, scrolls, and feature-cast spells more valuable, but only when the action economy and components still work. Concrete examples include `魔契师` `玄奥秘法`, `魔法学徒`, `妖精触碰` / `阴影触碰` / similar `*-Touched` feats, and `游侠` free long-rest casts of `猎人印记`: each may avoid spending a spell slot for that casting, but still requires checking its own uses, recharge, casting time, components, concentration, spell-list/preparation legality, and feat or class-feature opportunity cost.
   - Read the base class again when reviewing a subclass. Record the exact resource amount, recharge timing, and feature conflicts for class resources such as `动作如潮`, `回气`, Channel Divinity, Rage, Focus/Ki, Bardic Inspiration, Wild Shape, spell slots, pact slots, prepared spells, and similar class currencies.
   - Separate resource ceiling from practical throughput. A feature that looks extreme may be limited by short-rest/long-rest recharge, action cost, concentration, spell slots, prepared spell count, limited uses, saving throws, positioning, or competition with the class’s normal best turn.
   - Treat concentration as a real resource, not a parenthetical cost. For any feature or spell that requires concentration, ask what it is replacing at that level and whether it is worth concentrating on compared with the class's best spells/features. Example: `重力魔法` `调节密度` and `事件视界` have real tactical value, but they compete with Wizard concentration staples; do not score them as if they can run alongside the same caster's best control, summon, wall, or defense concentration spell. Conversely, no-concentration features that duplicate a concentration spell may be stronger than they first look.
   - Community calibration for concentration-bound class identity: the 2024 Ranger discussion repeatedly centers on `猎人印记` consuming concentration and bonus actions while several other Ranger combat spells have lost concentration. When a class feature is tied to a concentration spell, compare the whole package against the class's actual no-concentration alternatives and its best concentration alternatives. A feature can be strong as an attrition/default mode while still being bad design if it makes higher-level spell slots, subclass commands, or capstones feel locked behind a low-level concentration effect.
   - Evaluate unwanted interruption consequences. If a feature can end early because concentration breaks, the caster is incapacitated, the caster dies, range/line/position is lost, a required per-turn action is missed, a companion disappears, or a maintained effect is dispelled/suppressed, ask what immediately happens to affected creatures, objects, terrain, summons, flight, restraints, shared attunement, temporary forms, or delayed costs. Verify the relevant local rules rather than assuming the effect simply “turns off safely.” Example: if a concentration feature grants allies a fly speed and then concentration breaks while allies are airborne, 2024 `飞行` says a creature falls when it loses its fly speed unless it can hover or another effect keeps it aloft, and `坠落` can cause 1d6 bludgeoning damage per 10 feet, up to 20d6, plus prone on landing unless all falling damage is avoided. This risk affects practical strength, action planning, and design wording even if it does not always change the rank.
   - Compare “on par with” designs to the closest official feature or spell before scoring ceiling and design quality. Similar scale, action economy, duration, concentration, spell level, target type, and resource frequency matter. Examples: a 360-foot storm should be compared to `复仇风暴`, including that `复仇风暴` is a 9th-level concentration spell; a fire-damage maximization feature should be compared to `塑能师` `超限导能`, including that `超限导能` has spell-level limits while an unrestricted maximizer could interact with `流星爆`. If an option removes an official limiter, raise balance risk and possibly ranking; if it adds tighter frequency/target/turn limits, do not overstate the ceiling.
   - For any feature that maximizes, rerolls, upgrades, copies, doubles, adds, or otherwise manipulates a number of damage dice, count both the number of dice and the die faces. A cap like “12 damage dice” is not the same as “12d6”: 12d6 averages 42 and maximizes to 72, while 12d8 averages 54 and maximizes to 96, 12d10 averages 66 and maximizes to 120, and 12d12 averages 78 and maximizes to 144. If the design is meant to match a specific official benchmark, decide whether the wording actually caps the benchmark or only caps dice count. Example: if a fire maximization option is meant to sit near `塑能师` `超限导能` and 5th-level `灼热射线` (six rays at 2d6 each, 12d6 total), “up to 12 fire damage dice” still allows larger die faces from spells, monster actions, magic items, partner/third-party content, or homebrew. In official reviews, evaluate the first-party default environment separately from open-content / partner / third-party / monster-ally assumptions, and mark whether the wording would need an equivalent-d6 cap, a maximum total die-face cap such as 72, a fixed expected-value bonus, or a spell-level/source restriction to preserve the benchmark.
   - Evaluate severe costs by asking what can actually pay or undo them in that tier. Death, disintegration, lost bodies, exhaustion, expensive material components, 9th-level spell slots, once-per-long-rest spell access, and treasure economy all matter. Example: if an option kills and ashes the target after a 24-hour super-buff, verify whether only `完全复生术` or `祈愿术` can restore the target, the required spell level and material component cost, who can cast it, and whether a Tier 4 party can reasonably afford that cost repeatedly. A cost that is payable once for a final boss fight is not the same as a free drawback, and it should still affect design quality and repeated-use ranking.
   - Audit abuse paths, not only intended use. For any feature that targets `友方`, `盟友`, `自愿生物`, `非敌对生物`, a controlled creature, an incapacitated creature, a summoned/created creature, or a creature whose attitude can be changed, ask whether the party can turn an enemy into a legal target and then weaponize the effect or downside. Write the possible procedure, required spells/features, saves, concentration, duration, action timing, resource cost, death/revival cost, DM adjudication, and failure points before deciding whether it changes balance or mostly damages design quality. Grade abuse severity by payoff: if the only abuse is protective and does not create significant extra damage, control, forced movement, action denial, instant kill, resource theft, or other offensive payoff against the affected target or its side, worry less and usually treat it as wording cleanup rather than a major balance issue. Example: protecting a controlled enemy is usually much less concerning than using that controlled enemy for maximized damage, lockdown, resource extraction, or no-save death. If a feature grants a 24-hour super-buff and kills/ashes the target when the caster dies, check whether `支配怪物`, `支配类人`, `暗示术`, social coercion, charm effects, or another table-permitted control can make an enemy count as a friendly creature, then trigger the lethal drawback intentionally. Such a path may be unreliable because of target-legality rulings, failed saves, legendary resistance, concentration, timing, caster-death cost, `完全复生术` economy, and DM scrutiny; but if the wording enables it cleanly, it should affect balance and design scores.
   - Treat `暗示术` and `群体暗示术` as real but DM-sensitive abuse tools, not generic domination. Local 2024 `暗示术` is a 2nd-level concentration spell lasting up to 8 hours; the suggestion must be achievable, must not involve obvious harm to the target or its allies, requires the target to hear and understand, fails against charm-immune creatures, and ends if the caster or allies damage the target. Community examples of pressure points include forcing an NPC to answer questions truthfully for hours, making a shopkeeper sell goods for 1 copper, asking enemies to leave combat and find harmless work, or telling guards/soldiers to put down weapons and perform another nonharmful task. For scoring, this means:
     - Do not count `暗示术` as reliable mind-control access to every friendly-target exploit; the target must be charmed, the wording must be table-reasonable, and direct self/ally harm is blocked.
     - It can still support abuse when the requested behavior is framed as nonharmful, achievable, and socially plausible, such as "stop fighting and leave", "bring me the key", "cooperate with this ritual", "stand here while we prepare", "lend your help to this ally", or "come with us for questioning". If that behavior makes the target a legal `友方` / `盟友` / `非敌对` target for another feature, record the exact wording and the DM ruling dependency.
     - Economic/social coercion is not free utility. Community discussion commonly treats magical swindling, forced testimony, and coerced bargains as crimes or campaign-level consequences. Rankings may credit the spell's control/social ceiling, but design notes should flag table consent, legal consequences, hostile witnesses, anti-charm law enforcement, `解除魔法`, and later retaliation.
   - Include high-level abuse frameworks in that audit, but do not automatically treat every theoretical chain as default play. Typical real abuse appears when a feature's intended limiter is resource ownership, duration, body risk, action economy, or punishment, and another effect moves that limiter elsewhere. Check at least these frameworks when relevant:
     - Summon / created creature plus `异界誓缚` (`Planar Binding`): 2024 `异界誓缚` is available to Bard, Cleric, Druid, Warlock, and Wizard; it targets Celestial, Elemental, Fey, or Fiend creatures, costs a 1000+ GP consumable gem, takes 1 hour, requires the target to remain within 60 feet during casting, and extends the duration of a summoned/created target to match the binding. If a class/subclass summons one of those creature types, ask whether the party can bind it into a 24-hour, 10-day, 30-day, 180-day, or 366-day servant and whether that turns a combat-duration companion into long-term action economy, scouting, spell delivery, damage, or utility. If the subclass only creates a short-lived nonmatching creature type, or if the table cannot hold the target in range through the casting, do not over-credit the abuse.
     - `魔魂壶` (`Magic Jar`) plus transformation/body access: 2024 `魔魂壶` is a Wizard spell. The caster keeps their game statistics but uses the host body's hit points, Hit Dice, Strength, Dexterity, Constitution, speed, and senses. Abuse exists when class/subclass features were balanced around the caster's fragile body, low physical scores, death risk, or limited senses, but the caster can operate from a stronger Humanoid body. Audit target type, protection from `防护善恶` / `防护法阵`, Charisma save, jar range, jar destruction, host death, and whether transformation or other body-changing effects create a valid or better host. Treat it as high-risk table tech, not baseline unless the build/class can reliably supply it.
     - `拟像术` (`Simulacrum`): 2024 `拟像术` is a Wizard spell, creates a Beast or Humanoid construct copy with half hit point maximum, no leveling, no short rests or long rests, cannot cast `拟像术`, is costly to repair, and a new casting destroys the old simulacrum. Abuse exists when the simulacrum can spend spell slots, class/subclass resources, reactions, once-per-rest features, item charges, or accept backlash/punishment instead of the original character. This can change the evaluation of features whose limiter is “you pay the resource / you take the consequence,” including exhaustion, backlash damage, dangerous spell use, or limited high-impact reactions. Also check whether the feature text says “you,” “a creature,” “a copy,” “a spell you cast,” or otherwise blocks proxy use.
     - `祈愿术` (`Wish`): 2024 `祈愿术` is on the Sorcerer and Wizard lists, can duplicate any 8th-level or lower spell without prerequisites or costly components, and non-duplication uses impose real stress, including spellcasting backlash, Strength 3 for 2d4 days, and 33% chance to lose `祈愿术`. Abuse exists when that stress is carried by a simulacrum, bound creature, monster, magic item, or other proxy, or when `祈愿术` bypasses the material/time/target restrictions that normally keep another spell from enabling a class/subclass feature. Separate spell-duplication use from open-ended reality reshaping; the former is rules-constrained, the latter is DM-adjudicated and should not define default rankings unless the review explicitly assumes permissive high-level play.
     - Action-economy compression through replicated spells: 2024 `神圣干预` lets a Cleric use a Magic action to choose a 5th-level or lower Cleric spell with casting time other than Reaction and cast it as part of that action without a spell slot or material components. `进阶神圣干预` lets that same feature choose `祈愿术`; `祈愿术` itself is an action and can duplicate any 8th-level or lower spell without prerequisites, including costly components. Whenever a class/subclass/build relies on a spell's long casting time, material cost, location setup, or downtime footprint as the limiter, check whether `神圣干预`, `进阶神圣干预`, or `祈愿术` compresses it into an action or bypasses the setup. Examples include, but are not limited to, `守卫刻纹` (1 hour), `治疗祷言` (10 minutes), `圣居` (24 hours), `克隆术` (1 hour plus 120-day maturation remains relevant), and `海啸术` (1 minute). Do not assume every duplicated spell loses all downstream limits: read the replicated spell and preserve any duration, target, maturation, placement, concentration, area, trigger, or post-casting requirement that still applies.
       Community calibration: public discussion around 2024 `神圣干预` often centers on whether this wording truly compresses long casting times, especially for `圣居`, `治疗祷言`, and `守卫刻纹`. The project default is the verified local wording: the selected spell is cast as part of the Magic action. Still, if a rank depends on instant `圣居`, action `治疗祷言`, free resurrection/restoration, action `守卫刻纹`, or action `异界誓缚` setup, write the dependency explicitly and mark it as table-ruling-sensitive. Also check counterplay: `解除魔法`, `法术反制` if components/casting are observable and table rules allow it, creature-type limits, range, line of effect, and encounter relocation can reduce the practical ceiling.
     - `守卫刻纹` (`Glyph of Warding`) spell glyph abuse: 2024 `守卫刻纹` can store a prepared spell, trigger it later, and if the stored spell requires concentration, the effect lasts for its maximum duration without anyone concentrating. The glyph is destroyed if the warded object/surface is moved more than 10 feet from the casting location, so the real abuse is not “carry a glyph anywhere” by default; it is prebuilding a fixed buff/trap room, stacking multiple paid glyphs, converting concentration buffs or area spells into no-concentration triggers, and then using teleportation, `半位面`, base defenses, or planned encounter locations to bring targets to the glyphs. Audit spell level, upcast slot, 200+ GP diamond dust per glyph, 1-hour casting time unless compressed, trigger wording, target legality, whether the stored spell can target the triggering creature or area, and whether the reviewed feature makes glyph setup easier or more rewarding.
       Community calibration: `守卫刻纹` + extradimensional storage is commonly discussed as a "buff room", "god box", or demiplane staging exploit. Do not turn that into a blanket S rank for every class that can eventually cast the spells. Treat it as high-level infrastructure that needs downtime, money, spell preparation, slot expenditure, legal triggers, a stable location, and encounter access. It increases the ceiling of prepared full casters and specific builds; it should change a subclass score only when that subclass materially improves the setup, access, trigger reliability, spell storage payoff, or ability to force enemies/allies through the room.
     - `半位面` (`Demiplane`) storage and staging abuse: 2024 `半位面` creates or reconnects to a persistent 30-foot room through a 1-hour door; objects left inside remain there, creatures can remain unless they choose ejection when the door disappears, and the caster can reconnect to a known demiplane. Abuse exists when a party uses it as a portable fixed location for `守卫刻纹` stacks, stored bodies, `克隆术` containers, bound creatures, dangerous objects, prebuilt terrain, or delayed-cost features. This does not automatically make every stored setup combat-reliable: check access action, who knows the demiplane, whether enemies can follow, whether glyphs/objects were ever moved more than allowed, whether creatures can survive/wait there, and whether the encounter gives time to open and trigger the room.
     - `涅斯图魔法灵光` (`Nystul's Magic Aura`) type/aura manipulation: 2024 local text says the `伪装` effect can make spells and other magical effects treat a willing creature as another creature type, and the `虚假灵光` effect can alter an object's apparent magic aura. Community discussion often brings this up as counterplay or support for `圣居`, creature-type triggers, detection, glyph conditions, and some binding/control assumptions. Before crediting it as an exploit, verify target willingness, 24-hour duration, 30-day permanence setup, dispel vulnerability, whether the relevant effect checks actual type or magically perceived type, and whether the table treats this as affecting targeting restrictions or only detection/trigger processing. This is a real rules interaction, but it is table-sensitive enough that it should usually be a caveat or design-risk modifier unless the reviewed option directly enables it.
     - Combined chains: `拟像术` + `祈愿术`, `魔魂壶` + transformation, summon + `异界誓缚` + subclass aura/buff, or any combination with magic items, monster allies, or partner/third-party content can magnify a feature far beyond its printed class boundary. For each chain, state who can access each piece, whether one character can self-enable it or needs a party member, what level and material cost it requires, how many saves/concentration checks/DM rulings it needs, what failure does, and whether it is stable enough to affect balance ranking or should mainly affect design risk notes.
   - When applying abuse analysis, separate four environments: (1) default single-class/default party assumptions, (2) ordinary party cooperation with official spells, (3) magic item / monster ally / story reward assumptions, and (4) open partner / third-party / homebrew assumptions. Stable, repeatable abuse in environments 1-2 can change balance rankings. Environment 3-4 abuse usually belongs in caveats or design-quality risk unless the reviewed content itself grants the enabling piece.
   - For every caster or spell-granting subclass/build, check spell-slot progression, prepared/known spell count, preparation change rules, subclass bonus spells, spell-list scope, combat spell value, noncombat spell value, and whether the feature’s delivery mode actually improves the spells worth casting. Do not assume “more spell access” is strong without naming the spells and the use case.
   - If a caster can change prepared/known spells only when leveling up, treat each spell choice as a long-term build commitment, not a daily toolbox. Identify which spells are actually worth locking at each tier, then explain what is crowded out. Examples of high-pressure locked choices include defense (`护盾术`, `吸收元素` if locally available), encounter control (`催眠图纹`, `恐惧术`, `缓慢术`, `放逐术`), anti-caster tools (`法术反制`, `解除魔法`, `沉默术`), mobility/escape (`迷踪步`, `任意门`), healing/recovery (`治愈真言`, `次等复原术`, `回生术`), summon/companion spells (`野兽召唤术`, `妖精召唤术`, `亡灵召唤术`, `龙类召唤术`), and battlefield division (`蛛网术`, `力墙术`, `力场墙`, `墙`-type spells where locally present). A class with level-up-only swaps can still be strong, but its rank must reflect lower day-to-day adaptability and the real opportunity cost of carrying situational spells.
   - Bard-specific example: 2024 `吟游诗人` can replace only one prepared spell when gaining a Bard level. `魔法奥秘` expands future preparations and replacement choices to the Bard/Cleric/Druid/Wizard lists, but it does not create daily full-list preparation. At level 10, optimized Bards often need to replace several low-level transitional Bard spells over multiple later levels because cross-list staples such as `法术反制`, `解除魔法`, `回生术`, `野兽召唤术` / `妖精召唤术`, `力墙术` / `力场墙`, `护盾术`, `迷踪步`, or another table-specific answer are competing for limited prepared slots and replacement opportunities. When ranking Bard or Bard subclasses, credit `魔法奥秘` as a major power spike, but do not score every possible cross-list role as simultaneously online immediately at level 10.
   - Community calibration for 2024 `魔法奥秘`: when evaluating a Bard that starts play above level 10, reconstruct spell choices level by level instead of assuming the character appears with every possible cross-list slot already optimized. Community discussions commonly count one new Magical Secrets-eligible prepared spell when the prepared-spell number increases and one replacement on Bard level-up; this matters for how quickly a Bard can purge low-level transitional spells. Also verify cantrips locally: `魔法奥秘` keys off prepared spells of level 1+ in the Bard table, so do not assume it grants cross-list cantrips unless a subclass/feature says so.
   - Spell scroll interaction matters for caster rankings. Under the 2024 `法术卷轴` rule and local `贤者谏言2025`, the spell on a scroll must be on a spell list used by the character. For Bards, `魔法奥秘` does not let them read every Wizard/Cleric/Druid scroll. A cross-list spell counts as a Bard spell for scroll use only if the Bard has actually prepared that spell through `魔法奥秘`. Example: a Bard can use a `灵体卫士` scroll only if `灵体卫士` is currently prepared through `魔法奥秘`; otherwise the Bard cannot understand that scroll. When ranking Bard scroll access, treat scrolls as improving depth for already-locked Magical Secrets choices, not as solving every missing role.
   - EGW `秘迹学法术 Dunamancy Spells` are not a normal Wizard / Bard / Cleric / Druid spell-list expansion. Local EGW text says these spells can be used directly by the Wizard subclasses in that chapter (`时间魔法` and `重力魔法`) and should not simply be added to other casting classes' full spell lists; a DM may award other casters a small number of such spells as campaign rewards. Therefore do not credit ordinary `魔法奥秘` with access to `秘迹学法术` such as `灵敏之赐`, `时流刹转`, `暗黑星辰`, `饕餮虚空`, or similar unless another verified local rule explicitly adds them to a usable spell list or the table assumption says the DM awarded them. Conversely, when ranking `时间魔法（EGW）` and `重力魔法（EGW）`, count their relevant `秘迹学法术` as part of the subclass ecosystem and compare those spells against official Wizard subclass ceilings.
   - When scoring a level-up-only caster, do not give full credit in every spell-related aspect merely because the spell list contains options. Credit only the functions that a reasonable optimized character can afford to lock simultaneously at that tier. If choosing `法术反制` means delaying `催眠图纹`, a summon, healing, or mobility, discuss that tradeoff in the relevant aspect and overall reason.
   - Check species, origin feats, general feats, setting feats, and common magic items that realistically interact with the class/subclass at each tier. Examples to remember: `阿斯莫` `天启` / `天堂飞翼` is 1/long rest; `魔法学徒（法师）` can grant `护盾术`; Human can have two origin feats; `妖精触碰` can choose Divination or Enchantment spells such as `猎人印记` or `脆弱诅咒`; The Crooked Moon `教团新进者` can grant `脆弱诅咒`; `魔咒武器` can duplicate some concentration-damage packages.
   - Community calibration for `魔法学徒`: `魔法学徒（法师）` is widely valued because `护盾术`, `寻获魔宠`, `剑刃防护`, and similar options can patch defenses or utility early, and the 2024 feat lets the 1st-level spell be cast once without a slot and also with any spell slots the character has. Do not treat this as free universal defense. Score the actual opportunity cost against `警觉`, `音乐家`, `幸运`, `强韧`, weapon/damage feats, ASI pressure, reaction economy, component/free-hand requirements, and encounter mix. `护盾术` is much less valuable against saving-throw-heavy encounters or when a later feature such as `防御决斗术` covers the same reaction-defense niche; `寻获魔宠` may outperform it in scouting/help-heavy campaigns.
   - Community calibration for `魔法学徒（德鲁伊）` / `橡棍术`: Charisma/Intelligence/Wisdom-based weapon plans can be real, especially for Paladins, Valor Bards, Eldritch Knights, Bladesingers, or homebrew gishes, but check bonus-action startup, weapon mastery limits, heavy-armor Strength requirements, shield/component/free-hand rules, and general feat stat bonuses. A build becoming SAD is not automatically higher damage or better defense if it delays Great Weapon Master, Polearm Master, War Caster, Defensive Duelist, an ASI, or class-specific action economy.
   - Explain whether a feat/item/species interaction is actually worth the opportunity cost. Compare against common competing choices such as Great Weapon Master, Polearm Master, Magic Initiate, resilient defenses, ASI pressure, and concentration economy.
   - Evaluate action economy explicitly: action, bonus action, reaction, concentration, free/no-action timing, precombat setup, companion command, and whether the feature competes with the class’s normal damage/control/defense loop. A “ribbon” that is free and does not compete with key actions/resources may matter more than its text size suggests; a powerful feature that consumes the same action as the class’s best turn may matter less.
   - Check whether the feature's benefit is already available from the class chassis, common spells, `武器精通`, feats, species traits, magic items, or widely used party tactics before calling it a major strength. Apply this to every scoring aspect, not only advantage or DPR: damage riders, accuracy, defense, saves, resistance, healing, temporary hit points, mobility, forced movement, prone/restraining, debuff, anti-caster tools, battlefield division, summons/companions, skills, crafting, information gathering, ritual utility, and exploration.
   - For each overlap, ask what is actually left: lower action cost, no-save reliability, no-concentration, no spell slot, no resource, earlier level, longer duration, bigger range, team-wide effect, off-turn/reaction compatibility, better scaling, better target type, fewer counters, or lower opportunity cost. Credit those differences directly; if the feature merely duplicates a common baseline, lower uniqueness/design credit and avoid over-scoring the relevant function.
   - Advantage is a common example, not a special-only case: `烦扰` / `Vex`, `失衡` / `Topple`, prone, invisibility, help actions, and spells such as `闪耀斩` can make a cheap advantage feature less unique at later tiers. Still credit the feature if it is cheaper, no-save, no-concentration, no-slot, works before the first hit, applies to more attacks, works at range, or stacks with reaction/off-turn attacks; but do not score it as if no other advantage engine exists.
   - Community calibration for weapon mastery advantage: `烦扰` is easy advantage but usually needs a hit first and is strongest when it can chain on the same target; `失衡` can create prone advantage for melee allies but may penalize ranged allies and usually involves a save. When comparing a subclass advantage engine against weapon mastery, write whether the feature works before the first attack, works for ranged attacks, bypasses saves, helps the whole team, supports off-turn attacks, or avoids weapon restrictions.
   - Evaluate replaceability. If a class identity is built around an effect that can be copied by common feats, spells, or magic items, lower the uniqueness/design value unless later class features meaningfully deepen or protect that niche. Example: treat Hunter's Mark-style damage as more replaceable when `妖精触碰`, `教团新进者`, `魔咒武器`, or `脆弱诅咒` can cover a similar combat role.
   - Community calibration for `猎人印记` vs `脆弱诅咒`: discussion generally treats their damage role as similar but not identical. In 2024, `脆弱诅咒` ability-check disadvantage is narrower in combat because many old contest/counterplay cases moved to saving throws, and it deals a more commonly resisted damage type; `猎人印记` has tracking utility, force damage, and simpler components, but it remains concentration and often bonus-action constrained. When judging replaceability, compare damage type, components, target transfer, tracking/skill utility, immunity/resistance, and the fact that both compete with stronger concentration options.
   - For resource-conversion mechanics, count the resource at each tier and account for every competing feature that spends it. Compare to official analogues with the same rigor. Example: compare a luck/Portent-style home or partner mechanic against `预言师` `预兆` / `高等预兆` and `时间魔法` `收束未来`, including whether costs such as `力竭` can be mitigated by high-level wizard tools like `拟像术` or other immunity/avoidance methods when those assumptions are table-legal.

6. Use community comments only after local verification.
   - Browse when the user asks for community comments, current opinions, or calibration.
   - Treat RPGBOT, Tabletop Builds, Treantmonk, Pack Tactics, Dungeon Dudes, Reddit, Giantitp, and D&D Beyond forums as calibration sources, not rules sources.
   - Keep only comments that match the local version’s actual feature set.
   - If a community review is about 2014 content but the file is 2024, use it only as historical contrast.
   - In final responses, cite online sources used.

7. Write feature-level reviews.
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

8. Keep rankings calibrated.
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

9. Apply design-score separation.
   - Four design items: `设计质量`, `主题`, `能力设计质量`, `主题与能力关联度`.
   - High power is not automatically good design.
   - Overpowered action economy, bounded accuracy breaks, resource loops, old-version incompatibility, DM-dependent ambiguity, or feature bloat can lower design quality even if strength is high.

10. Account for shared 2024 assumptions.
   - 起源专长（Origin Feats） exist; `魔法学徒（法师） Magic Initiate (Wizard)` can give many characters `护盾术 Shield`, so do not over-credit a subclass just for easy Shield access.
   - `武器精通 Weapon Mastery` is part of the 2024 martial baseline.
   - General magic items can affect a tier, but do not assume unlimited magic item economy.
   - FRHoF `Circle Magic` can strongly alter full-caster/team environments; do not assume it is always active unless the file or task says so.

11. Update records.
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
