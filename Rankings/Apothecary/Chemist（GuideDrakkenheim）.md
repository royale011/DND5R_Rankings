# Chemist（GuideDrakkenheim）

所属职业：Apothecary
英文名 / 社区检索名：Chemist / Apothecary Chemist
来源 / 版本：第三方/合作方：Sebastian Crowe's Guide to Drakkenheim（GuideDrakkenheim）

## 目录

- [队伍定位调整](#队伍定位调整)
- [详细评价](#详细评价)
- [本轮重评](#本轮重评)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)

## 队伍定位调整

Chemist 是 Apothecary 的爆破、毒气和元素调配路线。它把 Apothecary 的短休高环槽和准备制法表推向酸、冷、火、闪电、毒素伤害：1级给炼金工具方向和始终准备的爆破/区域法术，3级让你在元素/毒酸法术里保护若干可见生物，6级把单目标伤害戏法扩成双目标并给一名生物1小时元素/毒酸抗性，10级用 `Bottled Spells` 把 Chemist 扩表法术装瓶交给别人释放，14级可在五种伤害类型之间转换，18级让用 Apothecary 槽施放的对应伤害法术视为7环。

它的强度不在“把伤害数字推到无条件最高”，而在把 AoE 施法的三个痛点同时处理：队友误伤、伤害抗性/免疫、行动经济/专注归属。`Bottled Spells` 是最强也最需要桌面确认的节点，因为开启瓶子的生物用动作施放瓶中法术，使用你的法术攻击加值和豁免DC，但在其他方面视为施法者。按文本，这会让队友代为启动部分 Chemist 法术、承担位置和可能的专注归属；这很强，但也把执行压力放在“瓶中法术持续多久、谁能安全携带、开瓶动作和施法者责任如何追踪”等细节上。

## 详细评价

1级 `Chemical Compound` 给炼金/化学方向的工具身份，`Chemist Spells`提供始终准备扩表。已核对本地 `GuideDrakkenheim` 源，扩表包括 `Flaming Sphere`、`Fireball`、`Stinking Cloud`、`Ice Storm`、`Wall of Fire`、`Cloudkill`、`Cone of Cold`，并在子职元数据中标出 `Fire Bolt`。这让 Chemist 从低中阶开始就有稳定爆破、毒气/遮断和大范围伤害路线，不占 Apothecary 的日常准备数。

3级 `Precise Application` 是友伤管理。你施放造成酸、冷、火、闪电或毒素伤害的法术并伤及你可见的其他生物时，可选数量等于智力调整值的目标自动通过该法术豁免，若成功本应半伤则改为无伤。这不是 `Careful Spell` 的完全复制，因为它只适用于五种伤害类型且要求可见；但对 `Fireball`、`Stinking Cloud`之外的毒酸区域、`Ice Storm`、`Cone of Cold` 和大量 Drakkenheim 自定义伤害法术都很实用，直接提高混战可投放性。

6级 `Chain Reaction` 让通常只以一个生物为目标、且造成酸/冷/火/闪电/毒素伤害的 Apothecary 戏法改为指定两个射程内生物。它给 Chemist 一个还不错的无槽清杂/补刀基线，尤其配合 `Fire Bolt` 或 Apothecary 自定义戏法；但它仍只是戏法扩目标，不是主要强度来源。同级 `Chemical Conditioning` 用动作触碰一名生物，给酸、冷、火、闪电或毒素之一的抗性1小时，再次使用会结束前一次。这是很干净的预防工具，能针对龙息、元素地形、毒云或Boss伤害类型做准备；限制是单目标、动作、一次只维持一种类型。

10级 `Bottled Spells` 是 Chemist 的核心跃迁。你施放来自 `Chemist Spells` 的法术时，可以让法术无即时效果而储存在触碰的小瓶中；瓶子被开启时，持有者用动作施放其中法术，使用你的攻击加值和DC，但其他方面把开启者视为施法者。你一次只能有一个未用瓶，使用后短休前不能再装瓶。这个能力能提前把短休槽转成队友动作、把施法位置交给前排/飞行/隐蔽角色、让队友承担持续法术的专注，并把你的强DC交给别人投放。它的上限非常高；限制是只限 Chemist 扩表、一次一个、要先花槽装瓶、开瓶要动作、携带和专注风险都真实存在。

14级 `Elemental Adjustment` 让你用 Apothecary 法术位施放造成酸、冷、火、闪电或毒素伤害的法术时，把该伤害改成列表内另一种。这能绕开抗性/免疫，也能针对敌人弱点或战术需求换型。因为毒素抗性/免疫生态很差，能把毒换成酸/闪电/火/冷很重要；但它只处理伤害类型，不处理豁免类型、条件免疫、传奇抗力或法术是否适合当前遭遇。

18级 `Chemical Cataclysm` 让你用 Apothecary 槽施放造成酸、冷、火、闪电或毒素伤害的法术时，视为用7环槽施放。对 pact 式5环短休槽来说，这是终局伤害效率提升，特别是对可升环的爆破/毒酸法术有用；但许多高环战斗的胜负仍由控制、反制、召唤、行动经济和豁免可靠性决定，单纯把伤害视为7环不足以把 Chemist 推到 Alienist 那种 S+控制可靠性。

## 本轮重评

本轮依据本地 `5etools-homebrew\collection\Ghostfire Gaming; Sebastian Crowe's Guide to Drakkenheim.json` 中 `Chemist|Apothecary|GuideDrakkenheim|Chemist|GuideDrakkenheim` 及其 `Chemical Compound`、`Chemist Spells`、`Precise Application`、`Chain Reaction`、`Chemical Conditioning`、`Bottled Spells`、`Elemental Adjustment`、`Chemical Cataclysm` 重查。`DND5e_chm`与`5etools-cn`未定位可靠中文正式译名，因此文件保留英文名。

社区校准检索覆盖 `Chemist Apothecary Drakkenheim balance review`、`"Chemist" "Apothecary" "Drakkenheim"`、`"Bottled Spells" "Chemist" Apothecary`、`"Chemical Cataclysm" "Apothecary"`、Reddit、D&D Beyond论坛与通用网页方向；未定位稳定同版本强度讨论。本轮按本地文本、Apothecary基础职业重评结论和当前第三方新职业横向样本独立判断。

横向校准后，Chemist 高于普通爆破子职，因为它不只是加伤害，而是解决友伤、类型、抗性和行动经济；但它低于 Alienist 的T3-T4 S+，因为它没有稳定把敌方关键豁免成功改写为失败，也没有同级别的精神防线与控制可靠性。综合定为 `A+ / S / S / S`。

## 分项评分

| 项目 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | D | C | C | C |
| 远程伤害者 | B+ | A- | A- | A- |
| 法术伤害者 | A+ | S | S | S+ |
| 防御和生存 | B+ | A | A | A |
| 治疗和临时生命 | A | A+ | S- | S |
| 团队增益 | B+ | A | A+ | A+ |
| 反制施法者 | D | B | A- | A |
| 减益 | A | S- | S- | S- |
| 战场分隔 | B+ | A+ | S | S |
| 召唤 / 伙伴 | E | B | B+ | A |
| 技能使用 | B+ | A- | A- | A- |
| 制造 | A | A+ | A+ | A+ |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | Apothecary强底盘加始终准备爆破/毒气扩表、`Fire Bolt`入口和3级`Precise Application`友伤管理，让低级AoE投放明显舒服；但资源槽仍少，主要强度还没脱离基础职业。 |
| Tier 2（5-10） | S | `Fireball`、`Stinking Cloud`、`Ice Storm`、`Wall of Fire`等扩表配合友伤管理、双目标伤害戏法、1小时抗性和10级`Bottled Spells`，让Chemist同时提升伤害、位置、专注归属和队友行动分配。 |
| Tier 3（11-16） | S | 6-8环`Greater Formula`、14级伤害类型转换和`Bottled Spells`继续保持高阶价值，尤其能把强DC扩表法术交给队友动作/位置释放；限制是缺少Alienist式豁免成功重骰，遇到传奇抗力或免疫仍要靠普通高阶法术解题。 |
| Tier 4（17-20） | S | 9环公式、额外高阶公式和18级`Chemical Cataclysm`把合格伤害法术视为7环槽，终局爆破效率很高；但顶级遭遇更看重控制可靠性、反制和规则所有权，缺少`Wish`与无条件失败制造，所以保持S而非S+。 |

## 设计相关评分

| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | Chemist 的玩法线很清楚，从友伤管理、抗性、装瓶、换型到终局升环都围绕炼金爆破展开；扣分点是`Bottled Spells`的施法者归属、持续携带、专注和预存窗口很强也很吃桌面解释。 |
| 主题 | A | 爆炸、毒气、元素调配、装瓶法术和化学灾变都非常贴合战地化学家/炼金爆破手主题。 |
| 能力设计质量 | B | 多数特性短而可执行，`Precise Application`和`Elemental Adjustment`边界也清楚；`Bottled Spells`虽然有次数限制，但把强DC、队友动作、位置和潜在专注转移绑在一起，复杂度与优化上限偏高。 |
| 主题与能力关联度 | A | 主要强点都来自化学投放、配方保存、伤害类型调整和灾变式升环，机制和主题高度一致。 |
