# The Coven（GrimHollowPG24）

## 目录

- [队伍定位摘要](#队伍定位摘要)
- [详细评价](#详细评价)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 队伍定位摘要
The Coven是一个鬼婆/女巫结社主题的控制、诅咒、调查和一次性魔法物品后勤宗主。它的低中级强度来自新版始终准备法术、魅调次无槽`Hex`、`Counterspell`、`Polymorph`和10级无槽`Bestow Curse`；高阶亮点则是`Hag's Visage`的人形生物恐慌-麻痹-归零连锁，以及14级临时药水和`Minor Heartstone`。它不是角之王宗主那种稳定无专注诅咒引擎，也不是Stone Sovereign那种长期伙伴宗主，而是一个上限很高、但目标类型、动作经济和文本边界都比较挑桌面的实用型鬼婆宗主。

## 详细评价
本地来源确认该子职来自`GrimHollowPG24`，采用`Warlock|XPHB`、`edition: one`和3/6/10/14级特征节奏。`DND5e_chm`目前只定位到《鬼魅幽谷》旧版资料，未找到2024版`The Coven`的可靠中文正式译名，因此本轮文件名和正文保留英文名，机制以`5etools-homebrew/collection/Ghostfire Gaming; Grim Hollow - Player's Guide - 2024.json`为准。

`Coven Spells`是新版写法：达到对应魔契师等级后始终准备。3级给`Hold Person`、`Identify`、`Locate Object`和`Ray of Sickness`，5级给`Bestow Curse`与`Counterspell`，7级给`Phantasmal Killer`与`Polymorph`，9级给`Divination`与`Locate Creature`，17级给`Contact Other Plane`与`Scrying`。这张表很像鬼婆工具箱：找物、鉴定、占卜、诅咒、病害、定身、变形和窥探都有。强度上，低级`Hold Person`和`Locate Object`有明确场景价值；5级`Counterspell`是魔契师最关键的反制入口；7级`Polymorph`是强通用按钮；17级的远程情报法术让终局侦察不空。

3级`Hag's Eye`给一个可作魔契师法器的鬼婆之眼饰物。只要你持有它，就能每天不消耗法术位施放魅力调整值次`Hex`，至少一次；10级后还可每天用它无槽施放一次`Bestow Curse`。无槽`Hex`低级非常实在：它省下少量契约位，让`Eldritch Blast`和侦查/追踪类能力检定压制更容易运作。不过它仍吃专注，也会和`Hold Person`、`Bestow Curse`、`Polymorph`、`Phantasmal Killer`等法术争同一专注位，所以不是无限叠加的伤害引擎。

6级`Hag's Guile`给额外`Minor Illusion`，并让你在生物用`Study`动作检查你的幻术时用反应让该检定劣势；同一幻术法术第一次被`Study`成功识破时，还能造成心灵伤害，数值为`1d6 + 每个施放该法术所用法术位等级1d6`，次数为魅力调整值，短休或长休恢复。这一层的主题非常好，但强度不稳定。原因很简单：它要求敌人真的花`Study`动作检查幻术，而很多战斗敌人会绕开、攻击、离场或直接用其他感官/法术处理。若队伍善用`Silent Image`、`Major Image`、地形遮蔽和诱敌，它会提高幻术可信度并惩罚识破；若桌上很少让怪物主动调查幻术，它就主要是一个额外戏法和低频反应。

10级`Hag's Visage`是The Coven最有戏剧性的战斗按钮。你用`Magic`动作启动1分钟鬼婆面容，长休一次。持续期间，`Horrifying Gaze`可用附赠动作选择30尺内你能看见且能看见你的人形生物，目标作感知豁免，若能看见你则对该豁免有劣势，失败恐慌1分钟且回合结束重复豁免。然后`Paralyzing Gaze`可用`Magic`动作针对已经恐慌的人形生物，再次感知豁免失败则麻痹；成功则受等于魔契师等级的黯蚀伤害、失去恐慌，且在你下次长休前不能再被你的`Hag's Visage`指定。最后`Death Gaze`可用`Magic`动作针对已麻痹的人形生物，目标以优势作感知豁免，失败生命值降为0；成功则受两倍魔契师等级的黯蚀伤害、失去麻痹，且同样免疫你本轮特性的后续指定。

这个连锁的上限很吓人：附赠动作恐慌先给劣势豁免，随后动作麻痹，再用动作尝试直接归零。它对单个重要人形NPC非常有压迫力，尤其在队友能保护你、限制目标离开视线和30尺范围时。但它也有很多刹车：只能打人形生物，需要彼此可见，起手要动作，后续还要动作，目标每步都有感知豁免，死亡凝视还给优势，高阶首领常有传奇抗力/魔法抗性/条件免疫。更重要的是，`Paralyzing Gaze`文本没有清楚写麻痹持续到何时、是否随`Hag's Visage`结束而结束，虽然可按“持续期间获得的能力”理解为受1分钟窗口约束，但正式桌面仍会需要DM裁定。这让它强而不够干净。

14级`Hag's Craft`给两种临时魔法物品制造。第一，你可消耗一个法术位把普通容器临时变成`Hag's Cauldron`，持续10分钟；期间可用`Magic`动作倒出三瓶普通、两瓶非普通或一瓶稀有药水，药水在你下次短休或长休结束时失效；此能力长休恢复。这个能力的上限取决于可选药水清单和DM如何处理“任意同稀有度药水”的可得性：普通治疗药水、非普通飞行/成长/抗性类药水、稀有强效治疗或强战斗药水都可能改变一次冒险日的资源分配。它需要消耗法术位和动作，且每天一次，但“按稀有度任选药水”本身是很宽的后勤入口。

第二，你完成长休时可消耗一个法术位，把至少10金币的宝石变成`Minor Heartstone`，持续24小时并在结束时粉碎；持有者免疫中毒状态，并可无槽施放一次`Blink`。这比坩埚更稳定：把`Blink`交给前排、关键施法者或需要自保的侦察位都很有价值，中毒免疫也能打鬼婆、毒物、疾病/沼泽风格战役。它不改变高环现实，但很像鬼婆给爪牙发小护符，主题和功能都成立。

整体结论：The Coven是强于普通宗主平均线的工具/控制宗主。T1靠始终准备法术、无槽`Hex`和魔契师底盘达到A+；T2取得`Counterspell`、`Polymorph`、10级无槽`Bestow Curse`和`Hag's Visage`后仍是A+，但不进S-，因为6级实战触发低频、10级连锁又受人形限定和多步动作/豁免限制。T3-T4凭高阶魔契师底盘、占卜/窥探法术、一次性人形首领处决线、临时药水和`Minor Heartstone`进入S-；但它没有稳定团队资源引擎、无专注压制轴或跨表高环解题，因此不应和角之王宗主、契灵宗主等顶层生态型宗主同档。

## 分项评分
| 项目 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | C | C | C | C |
| 远程伤害者 | A | A | A | A |
| 法术伤害者 | B+ | A | A | A |
| 防御和生存 | B | B+ | A | A |
| 治疗和临时生命 | C | C | B+ | B+ |
| 团队增益 | B | B+ | A | A |
| 反制施法者 | D | A | A | A |
| 减益 | A | A+ | A+ | A+ |
| 战场分隔 | B | A | A | A |
| 召唤 / 伙伴 | E | E | E | E |
| 技能使用 | B+ | B+ | A | A |
| 制造 | E | E | A | A |

## 综合评分
| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | 3-4级始终准备`Hold Person`、`Identify`、`Locate Object`和`Ray of Sickness`，并用`Hag's Eye`每天无槽施放魅调次`Hex`；功能面明显高于普通宗主，但仍受专注和低级契约位数量限制。 |
| Tier 2（5-10） | A+ | 5-10级取得`Counterspell`、`Bestow Curse`、`Polymorph`和10级无槽`Bestow Curse`，`Hag's Visage`能压人形目标；但6级依赖敌人`Study`幻术，10级连锁又吃动作、视线、人形限定和多次感知豁免。 |
| Tier 3（11-16） | S- | 11-16级高阶魔契师底盘叠加`Hag's Visage`的人形首领处决线，14级`Hag's Craft`能临时制造稀有药水并交出`Minor Heartstone`的中毒免疫和无槽`Blink`；强但每天次数少且药水边界宽。 |
| Tier 4（17-20） | S- | 17-20级9环`玄奥秘法`、`Contact Other Plane`、`Scrying`和完整鬼婆物品后勤让它仍是强宗主；但子职没有新的终局资源、稳定团队防线或跨表高环改写，维持S-。 |

## 设计相关评分
| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 鬼婆法术、鬼婆之眼、幻术欺诈、恐怖凝视和坩埚/心石构成清晰成长线；扣分点是10级麻痹持续时间不够明确，14级任意药水制造边界很宽。 |
| 主题 | A | 交易、鬼婆之眼、诅咒、幻术欺诈、恐怖面容、坩埚和心石都强烈指向鬼婆结社与Etharis式黑暗童话。 |
| 能力设计质量 | B- | 始终准备表和无槽`Hex`很顺，但6级要求敌人主动`Study`幻术导致实战波动；10级多步控制/归零链和14级药水选择都需要DM认真管理边界。 |
| 主题与能力关联度 | A | 侦查/诅咒/病害/定身/变形/窥探、鬼婆之眼、识破幻术惩罚和临时坩埚都把“鬼婆代理人”变成具体玩法。 |

## 校准说明
本轮按`GrimHollowPG24`的XPHB魔契师文本评估。`DND5e_chm`只提供旧版《鬼魅幽谷》资料参考，未定位该2024子职可靠中文正式译名，因此保留英文名`The Coven`。

社区校准检索覆盖：`"The Coven" warlock "Grim Hollow"`、`"Hag's Visage" "The Coven" warlock`、`"Hag's Eye" "The Coven" "Warlock"`、`site:reddit.com "The Coven" "Grim Hollow" warlock`、`"Coven Spells" "Grim Hollow"`、`"Hag's Craft" "Grim Hollow" warlock`、`"Hag's Guile" "Grim Hollow"`、`site:dndbeyond.com/forums "The Coven" "Grim Hollow" warlock`、`"Grim Hollow Player's Guide 2024" "The Coven" "Warlock"`、`"Grim Hollow" "Hag's Eye" "Warlock"`、`"Grim Hollow" "Hag's Visage"`与`"The Coven" "Hag's Eye" "Hag's Visage"`；未定位稳定同版本强度讨论。本轮以本地GrimHollowPG24文本、XPHB魔契师底盘和已重评魔契师横向样本为主。

主要本地来源：`5etools-homebrew/collection/Ghostfire Gaming; Grim Hollow - Player's Guide - 2024.json`中的`The Coven|Warlock|XPHB|Coven|GrimHollowPG24`及其`Coven Spells`、`Hag's Eye`、`Hag's Guile`、`Hag's Visage`与`Hag's Craft`特征。
