# The First Vampire Patron（GrimHollowPG24）

## 目录

- [队伍定位摘要](#队伍定位摘要)
- [详细评价](#详细评价)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 队伍定位摘要
The First Vampire Patron是一个偏个人战斗、生存、吸血和黑夜变形的吸血鬼宗主。它给魔契师始终准备的诅咒/命令/雾云/召唤/支配/念控法术，也给`Drain Life`作为附赠动作近身吸血打击；中后期通过自我`Polymorph`、击杀回收契约位和1分钟吸血鬼形态提高续航。它强在“我能贴上去、咬一口、把血吸回来”，弱在很多强项都要求近身、命中、消耗契约位或完成击杀，团队解题和高阶生态改写不如顶级魔契师宗主。

## 详细评价
本地来源确认该子职来自`GrimHollowPG24`，采用`Warlock|XPHB`、`edition: one`和3/6/10/14级特征节奏。`DND5e_chm`当前只提供《鬼魅幽谷》旧版资料，未找到2024版`The First Vampire Patron`的可靠中文正式译名，因此本轮文件名和正文保留英文名，机制以`5etools-homebrew/collection/Ghostfire Gaming; Grim Hollow - Player's Guide - 2024.json`为准。

3级`First Vampire Spells`是新版始终准备表。3级给`Bane`、`Command`、`False Life`和`Fog Cloud`，5级给`Conjure Animals`和`Gaseous Form`，7级给`Dominate Person`和`Seeming`，9级给`Little Death`与`Telekinesis`。这张表的强度不低：`Command`、`Bane`和`Fog Cloud`低级就有战术用途；`Gaseous Form`、`Seeming`和`Telekinesis`提供潜入/伪装/控物；`Dominate Person`对人形敌人仍是高价值控场。表中`Conjure Animals`限定为蝙蝠、老鼠或狼主题，和新版XPHB法术的灵体式执行存在一点表达不贴合，但作为始终准备的3环专注伤害/区域压力法术仍有价值。

同级`Nocturnal Predator`给60尺黑暗视觉，已有黑暗视觉则增加60尺。它是实用但普通的夜行补丁：对没有黑暗视觉的角色非常舒服，对已有黑暗视觉的种族则主要提高侦察距离。相比许多宗主的低级核心，它不是决定性强度来源。

核心低级特性是`Drain Life`。你在采取攻击动作或`Magic`动作之后，可以用附赠动作进行一次徒手打击；命中时该徒手打击改为造成`1d6 + 魅力调整值`黯蚀伤害。命中后，你还可以消耗一个契约魔法法术位，额外造成`1d8 + 法术位环阶d8`黯蚀伤害，并恢复等同于该伤害的生命值。这个按钮的上限很真实：魔契师可以先用`Eldritch Blast`、控制法术或武器攻击，再靠附赠动作补一次吸血打击；若命中后花契约位，低级也能换到很大的回血。

但`Drain Life`也有几个硬限制。第一，它要求你进入徒手打击距离，普通魔契师并不天然想站在5尺内。第二，文本只把伤害改为`1d6 + 魅力调整值`，没有说徒手打击的攻击检定也改用魅力，因此默认仍要处理徒手命中能力值问题；刃契路线或有相应专长/属性投资时会舒服得多。第三，契约位吸血爆发和控制/召唤/反制都抢同一短休资源。第四，“恢复等同于该伤害”的“该伤害”可按额外黯蚀伤害理解，若有桌面解释为整次`Drain Life`伤害，则强度会更高；评审按较保守的额外伤害恢复理解。

6级`Creature of the Night`让你始终准备`Polymorph`。通过此特性，你可以不消耗法术位且不需材料，只对自己施放，变成蝙蝠、老鼠或狼；次数等于魅力调整值，长休恢复。变形时你的游戏数据被野兽数据替换，但保留生物类型、生命值、生命骰、智力/感知/魅力、职业特性、语言、专长、技能和豁免熟练，并可在自己与野兽修正值中取高。它的探索价值很高：蝙蝠飞行与盲视、老鼠潜入、狼嗅觉/地面机动，都能让魔契师有吸血鬼式侦查形态。战斗价值则较谨慎：形态本身CR低，若要保留职业特性会出现组件、施法、武器/物品、`Drain Life`能否自然运作等桌面执行问题。作为移动/潜入/逃脱很强，作为正面战斗形态不应高估。

10级`Eldritch Appetite`要求你用`Drain Life`把一个敌人降到0生命值后，用反应吞噬其残余生命，恢复一个已消耗的契约魔法法术位；长休一次。它显然是想补偿`Drain Life`消耗契约位的成本，若你用吸血爆发击杀目标，可以把一次高额回血/伤害近似变成“杀到就退槽”。问题是触发窄：必须是敌人、必须由`Drain Life`降到0、必须你还有反应，而且长休一次。它是优秀的击杀奖励，但不是稳定资源循环。

14级`Eternal Night`让你不再衰老，并获得黯蚀伤害抗性。你还可用附赠动作进入1分钟吸血鬼夜幕形态，长休一次：每回合开始时，若你至少有1生命值，且不在直射阳光或流水中，就恢复`1d6`生命；若你受到光耀伤害，下回合开始不恢复。该形态期间，你每次使用`Drain Life`都能不消耗法术位额外造成`1d8`黯蚀伤害。这个终局按钮很有主题，但强度偏个人：黯蚀抗性有用，1分钟自愈能增加韧性，免费1d8也能减轻吸血成本；但它没有扩大目标、提高命中/DC、给队友防线、压敌方豁免或改写行动经济。作为吸血鬼味道很好，作为14级宗主爆点只是合格。

`Little Death`是9级始终准备表中的特色5环法术。施法后你降到0生命并死亡，下回合开始变成幽魂，占据尸体空间；你的数据被幽魂替换，但保留生命值、生命骰、心智属性和语言，并把熟练加值加到幽魂攻击和能力DC。GM秘密掷`1d8`决定持续小时数，材料若留在尸体上，结束时以半血复活；材料不在尸体上则死亡。尸体若被摧毁到不能存活，持续时间变为永久，直到身体被能使死者复生的效果处理。这是高风险潜入/逃脱/幽魂玩法法术，不是普通战斗增益：它会让角色真的死一次，依赖尸体安全和材料安全，且只能使用幽魂数据的能力。The First Vampire能准备它很有风味，但不应把它当作无风险高阶解题。

整体结论：The First Vampire Patron比普通弱宗主强很多，但其强度集中在个人近身续航和吸血爆发。T1有始终准备表、黑暗视觉和`Drain Life`，可到A+；T2有`Conjure Animals`、`Gaseous Form`、自我野兽变形、`Dominate Person`、`Telekinesis`和一次击杀回槽，仍是A+，但不进S-，因为最强子职循环要求近身命中、消耗法术位和击杀触发。T3-T4靠高阶魔契师底盘、`Little Death`、`Telekinesis`和14级个人吸血鬼形态进入S-；但它缺少稳定团队资源、反应防线、持续压豁免和高阶跨表改写，不能和角之王、契灵或顶级控制宗主同档。

## 分项评分
| 项目 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | B+ | A | A | A |
| 远程伤害者 | A | A | A | A |
| 法术伤害者 | B+ | A+ | A+ | A+ |
| 防御和生存 | A | A | A+ | A+ |
| 治疗和临时生命 | B+ | A | A | A |
| 团队增益 | C | B | B | B |
| 反制施法者 | D | B | B+ | B+ |
| 减益 | B+ | A | A | A |
| 战场分隔 | B | A | A | A |
| 召唤 / 伙伴 | D | B+ | B+ | B+ |
| 技能使用 | B | B+ | B+ | B+ |
| 制造 | E | E | E | E |

## 综合评分
| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | 3-4级始终准备`Bane`、`Command`、`False Life`和`Fog Cloud`，`Drain Life`又能在攻击或`Magic`动作后用附赠动作补黯蚀打击并消耗契约位回血；但近身、命中和法术位成本限制它不上S线。 |
| Tier 2（5-10） | A+ | 5-10级取得`Conjure Animals`、`Gaseous Form`、自我野兽`Polymorph`、`Dominate Person`、`Telekinesis`和一次`Drain Life`击杀回槽；功能很宽，但核心吸血循环要求近身命中和击杀触发。 |
| Tier 3（11-16） | S- | 11-16级高阶魔契师底盘叠加`Little Death`、`Telekinesis`和14级`Eternal Night`，个人续航与吸血鬼主题完整；但14级主要是黯蚀抗性、自愈和免费1d8，缺少团队或控场级爆点。 |
| Tier 4（17-20） | S- | 17-20级9环`玄奥秘法`托底，完整吸血、变形、支配、念控和幽魂法术包仍强；子职终局不提供新的高阶资源或全队防线，因此维持S-。 |

## 设计相关评分
| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 吸血打击、夜行变形、击杀回槽和永夜自愈是一条清楚的吸血鬼成长线；扣分点是`Drain Life`攻击属性、回血指代、2024`Conjure Animals`限定和变形后职业特性执行都需要桌面解释。 |
| 主题 | A | 黑暗视觉、吸血、蝙蝠/老鼠/狼形态、支配人类、雾化、幽魂假死和永夜自愈都非常吸血鬼。 |
| 能力设计质量 | B- | 近身附赠动作吸血给了好玩的风险/收益，但把契约位爆发、回血和击杀回槽绑在徒手命中上会让构筑很挑；自我`Polymorph`保留职业特性的执行边界也偏松。 |
| 主题与能力关联度 | A | 每个主要特性都直接服务“初代吸血鬼代理人”的捕食、变形、支配和不死主题，强度问题主要来自执行边界而不是主题漂移。 |

## 校准说明
本轮按`GrimHollowPG24`的XPHB魔契师文本评估。`DND5e_chm`只提供旧版《鬼魅幽谷》资料参考，未定位该2024子职可靠中文正式译名，因此保留英文名`The First Vampire Patron`。

社区校准检索覆盖：`"The First Vampire Patron" warlock "Grim Hollow"`、`"Drain Life" "First Vampire" warlock`、`"Eldritch Appetite" "First Vampire" warlock`、`site:reddit.com "First Vampire" "Grim Hollow" warlock`、`"The First Vampire Patron" "GrimHollowPG24"`、`"Creature of the Night" "First Vampire" warlock`、`"Eternal Night" "First Vampire" warlock`、`site:dndbeyond.com/forums "First Vampire" "Grim Hollow" warlock`、`"Grim Hollow Player's Guide 2024" "First Vampire"`、`"Grim Hollow" "First Vampire Patron"`、`"Grim Hollow" "Drain Life" "Warlock"`与`"First Vampire Spells" "Warlock"`；未定位稳定同版本强度讨论。本轮以本地GrimHollowPG24文本、XPHB魔契师底盘和已重评魔契师横向样本为主。

主要本地来源：`5etools-homebrew/collection/Ghostfire Gaming; Grim Hollow - Player's Guide - 2024.json`中的`The First Vampire Patron|Warlock|XPHB|First Vampire|GrimHollowPG24`及其`Drain Life`、`Nocturnal Predator`、`First Vampire Spells`、`Creature of the Night`、`Eldritch Appetite`、`Eternal Night`，以及同文件中的`Little Death`法术。
