# Shadow Domain（GuideDrakkenheim）

所属职业：牧师
英文名 / 社区检索名：Shadow Domain
来源 / 版本：第三方：Sebastian Crowe's Guide to Drakkenheim（GuideDrakkenheim / SCGtD）

## 目录

- [队伍定位调整](#队伍定位调整)
- [详细评价](#详细评价)
- [本轮重评](#本轮重评)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)

## 队伍定位调整

GuideDrakkenheim版Shadow Domain是黑暗防线、阴影视觉和暗场位移牧师。它和`暗影领域（黯潮之书）`不是同一个子职：黯潮版重心是`Shadow Grasp`的短窗口控制与终局多目标扩展；本版重心是1级300尺魔法黑暗视觉、2级`Cloak of the Night`给单目标在昏暗/黑暗中全伤害抗性、6级`Shifting Shadows`重排暗场站位、17级`Reborn in Darkness`黑暗再生与死亡延迟。

在队伍里，它最像“把光照条件变成防御资源的牧师”。它能用`Darkness`、熄灭光源和天然夜战环境保护关键队友，也能用`Pass without Trace`、`Hypnotic Pattern`、`Evard's Black Tentacles`和`Greater Invisibility`补足牧师通常缺少的潜入与奥术控制工具。限制也很明确：暗场会牵动队友视线、特殊感官和光照规则，核心保护是单目标、动作和引导神力资源，不是和平/暮光/Mind那种持续全队防错。

## 详细评价

本轮依据`5etools-homebrew\collection\Dungeon Dudes; Sebastian Crowe's Guide to Drakkenheim.json`复核`Shadow Domain|Cleric|PHB|Shadow|SCGtD`，确认这是旧`Cleric|PHB`接口的1/2/6/8/17级子职文本，并按XPHB牧师底盘兼容评价。本地`DND5e_chm`可定位到《德拉肯海姆》资料，但未定位该领域可靠中文正式译名；为避免和`暗影领域（黯潮之书）`混淆，文件与标题保留英文官方名。社区校准检索覆盖`Shadow Domain`、`Sebastian Crowe's Guide to Drakkenheim`、`Guide to Drakkenheim`、`Cloak of the Night`、`Shadow Sight`、`Shifting Shadows`、`Reborn in Darkness`、Reddit与DDB方向；未定位稳定同版本强度讨论，因此本轮按本地SCGtD文本、XPHB牧师底盘、当前牧师横向样本和已完成Theurgy映射独立判断。

领域法术为`False Life`、`Sleep`、`Darkness`、`Pass without Trace`、`Hypnotic Pattern`、`Nondetection`、`Evard's Black Tentacles`、`Greater Invisibility`、`Cone of Cold`、`Dream`，并通过`Bonus Cantrips`额外学习`Chill Touch`和`Minor Illusion`，且计为牧师戏法但不计入已知数量。这张表对牧师很优秀：`Pass without Trace`是强团队潜入入口，`Hypnotic Pattern`和`Evard's Black Tentacles`把牧师带到更接近奥术控制者的位置，`Greater Invisibility`和`Dream`也补足战术与长线工具。`Cone of Cold`只是可用的爆破，`Sleep`在高等级衰减明显，但低级仍能配合暗场和牧师控制节奏。

1级`Shadow Sight`给300尺魔法与非魔法黑暗中的正常视觉。这不是单纯“有黑暗视觉”：它直接解决`Darkness`和熄灯战术最常见的自我反噬，使牧师自己能在暗场中维持施法、治疗、站位判断和目标选择。真正的代价是队友未必有同等视觉，敌人的盲视、真视、震动感知、非视觉定位和开阔明亮战场也会降低暗场收益。

2级`Channel Divinity: Cloak of the Night`是核心强点。你用动作制造持续1分钟的魔法阴影，选择60尺内一个可见生物，包括自己；该生物处于昏暗或黑暗中时，对所有伤害具有抗性。发动时，60尺内非魔法光源熄灭，由环级不高于熟练加值的法术创造的魔法光源也会被解除。单目标全伤害抗性非常强，尤其能保护被集火前排、濒危队友或正在维持关键专注的自己；而熄灯效果又能主动创建条件。限制是动作成本、引导神力、单目标、1分钟、光照条件和队伍视线协调。它不是无条件全队半伤。

6级`Shifting Shadows`让你用动作选择60尺内一个处于昏暗或黑暗、且你能看见的生物，将其传送到60尺内你能看见、同样处于昏暗或黑暗、能承载目标且无需挤入的空位；非自愿目标通过感知豁免则无效，次数等于熟练加值，长休恢复。这是很好的救援和地形控制工具：可以把队友从包围中拉走，把敌人丢进`Spirit Guardians`、`Evard's Black Tentacles`或危险地形，也可以在夜战/地下城里重排站位。它的硬限制是动作、两端都要昏暗/黑暗、非自愿目标有豁免，且Foundry元数据写成附赠动作但正文明确为动作；本评审按正文动作处理。

8级`Potent Spellcasting`让牧师戏法伤害加入感知调整值。它能增强`Chill Touch`、`Sacred Flame`或其他牧师戏法，和300尺暗场视觉配合时远程小伤害很稳定，但它不是本领域的主要强度来源。XPHB兼容下，若桌面用新版牧师通用`Blessed Strikes`替换旧8级领域特性，应以桌面兼容口径为准；本文件仍记录并评价SCGtD源文本中的`Potent Spellcasting`。

17级`Reborn in Darkness`让你在黑暗中每回合开始回复10点生命；受到辉耀伤害后，该再生直到下回合开始前不生效；你只有在自己的回合没有再生时才会死亡，并且在黑暗中不会老化。这是强力终局自保：牧师已经有治疗、复原、`Death Ward`类资源和暗场视野，本领域又能通过`Darkness`与熄灯维持再生条件。它仍不是无限生命：辉耀伤害、被拖出黑暗、失去行动/视线、被放逐或困住、特殊死亡效果、敌人改造光照和队友无法支援都会构成真实反制。

## 本轮重评

Shadow Domain（GuideDrakkenheim）新增为`S- / S / S / S`。T1凭300尺魔法黑暗视觉、两个额外戏法、`False Life`/`Sleep`/`Darkness`/`Pass without Trace`和单目标全伤害抗性进入S-；T2取得`Hypnotic Pattern`、`Evard's Black Tentacles`、`Greater Invisibility`和`Shifting Shadows`后，已经是兼具牧师底盘、潜入、控场、保护和救援的S级领域；T3延续高环牧师资源和强暗场控制；T4因`Reborn in Darkness`获得强自保与死亡延迟，但没有持续全队数学或失败豁免改写，因此维持S而不进入S+。

## 分项评分

| 项目 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | C | C | C | C |
| 远程伤害者 | B | B+ | B+ | B+ |
| 法术伤害者 | A | S- | S- | S |
| 防御和生存 | S- | S | S | S+ |
| 治疗和临时生命 | A | A+ | S- | S |
| 团队增益 | A+ | S- | S- | S- |
| 反制施法者 | C | A | A | A+ |
| 减益 | A | S | S | S |
| 战场分隔 | A | S | S | S |
| 召唤 / 伙伴 | F | B | A | A |
| 技能使用 | S- | S- | S- | S- |
| 制造 | C | C | C | C |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | S- | 300尺魔法黑暗视觉、`Darkness`/`Pass without Trace`和`Cloak of the Night`的单目标全伤害抗性让低级阶段极硬且有团队潜入入口；动作、引导神力、光照条件和队友视线成本阻止它进入S。 |
| Tier 2（5-10） | S | 5-10级取得`Hypnotic Pattern`、`Evard's Black Tentacles`、`Greater Invisibility`、更多牧师资源和`Shifting Shadows`，把暗场保护、奥术控制、潜入和救援整合到牧师底盘上。 |
| Tier 3（11-16） | S | 高环牧师法术、持续暗场视觉、全伤害抗性窗口和PB/长休阴影传送继续保持强保护与控场；限制是核心收益仍依赖昏暗/黑暗和队伍配合，不是无条件全队防错。 |
| Tier 4（17-20） | S | `Reborn in Darkness`提供黑暗中的每轮再生和死亡延迟，配合牧师复原/防护资源很难被普通伤害带走；但辉耀伤害、光照反制、特殊感官和非团队型终局收益使它停在S而不进S+。 |

## 设计相关评分

| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 光暗平衡、黑暗视野、阴影防护和暗场位移形成清楚玩法；扣分来自光照/感官追踪负担、旧PHB接口兼容成本，以及`Shifting Shadows`正文动作与Foundry元数据不一致。 |
| 主题 | A | 领域法术、黑暗视觉、熄灯披风、阴影传送和黑暗再生都围绕“在光明背面执行神圣审判”的主题展开。 |
| 能力设计质量 | B | `Cloak of the Night`强但有明确条件，`Shadow Sight`解决核心玩法自洽，`Shifting Shadows`给出可执行救援/控场，`Reborn in Darkness`有辉耀与黑暗边界；整体可运行，但依赖DM认真执行光照与特殊感官。 |
| 主题与能力关联度 | A- | 实战确实会围绕黑暗、熄灯、救援、控制和再生展开；扣分是最优暗场玩法可能妨碍队友视线，主题表现依赖队伍是否愿意配合黑暗战术。 |
