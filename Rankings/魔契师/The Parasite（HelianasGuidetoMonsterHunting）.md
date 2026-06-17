# The Parasite（HelianasGuidetoMonsterHunting）

## 目录

- [队伍定位摘要](#队伍定位摘要)
- [详细评价](#详细评价)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 队伍定位摘要
The Parasite是Heliana体系里的寄生共生近战/防御宗主。它不是Grim Hollow的反施法型`The Parasite Patron`，而是把魔契师变成带寄生武器、活体盾牌、短休黏液魔宠和临时液化身体的中近距离战斗者。核心强项是高AC、长触及魅力武器、`Spirit Guardians`/`Haste`等扩表可选、可短休再造的`Parasitic Ooze`以及10级后让黏液替队友承伤。它的缺点也很明确：旧扩表不是始终准备，寄生武器没有自动加魅力伤害，召唤物血量有限，14级终局主要强化个人肉搏而非提供团队级改写。

## 详细评价
本地来源确认该子职来自`HelianasGuidetoMonsterHunting`，位于`5etools-homebrew/collection/Loot Tavern; Heliana's Guide To Monster Hunting.json`，采用旧`Warlock|PHB`接口和1/6/10/14级特征节奏。本轮按项目兼容口径视作XPHB魔契师在3级取得旧1级子职包，后续6/10/14级照常取得。`DND5e_chm`与本地中文资源中未定位该子职可靠中文正式译名，因此文件名和正文保留英文名。

`Expanded Spell List`加入`Heroism`、`Sanctuary`、`Enhance Ability`、`Enlarge/Reduce`、`Haste`、`Spirit Guardians`、`Evard's Black Tentacles`、`Freedom of Movement`、`Endure`和`Dominate Person`。这张表很强，但按旧魔契师接口理解：这些法术只是加入你的可选列表，仍要占已知法术。`Sanctuary`和`Heroism`提高早期防护，`Enhance Ability`补探索，`Haste`和`Spirit Guardians`给中阶近身玩法强理由，`Black Tentacles`补战场分隔，`Freedom of Movement`和`Dominate Person`提供高阶功能。自带5环`Endure`是很怪也很强的“不倒下”按钮：目标在1分钟内忽略力竭、中毒，并不能失能、震慑、麻痹或昏迷；会被打到0时改掷死亡豁免，但结束后会按失败死亡豁免付出力竭和昏迷代价。它能救急，但不适合轻率使用。

3级`Parasitic Weapon`用附赠动作显现爪、齿、触须或其他附肢。你在自己回合采取`Attack`动作时得到一个特殊近战武器攻击，触及等于熟练加值的5倍，熟练，并用魅力取代力量作攻击检定；命中造成1d12钝击、穿刺或挥砍，显现时选择伤害类型，但不加属性调整值到伤害。寄生武器攻击数随魔契师等级提高：5级两次，11级三次，17级四次；若你另有额外攻击，则那些额外攻击会替代这些寄生武器攻击的一部分。6级起这些攻击视为魔法武器。

这个武器的定位很特别。它不是单纯压过`Eldritch Blast`的输出路线，因为没有自动加魅力伤害；但它用10到30尺触及、魅力命中、1d12骰和可携盾的身体武器，让魔契师能在中距离近战威胁区里打出稳定攻击。源文还给DM一个建议：可考虑让以`Eldritch Blast`为前提的祈唤影响寄生武器，例如`Agonizing Blast`和`Repelling Blast`。本轮不把这个可选建议纳入主评分；一旦表上允许，它会显著提高输出和推拉上限，也会让不同桌之间强度差距变大。

3级`Symbiotic Reinforcement`让你在力量豁免中可用魅力调整值取代力量调整值，并能用附赠动作让宗主在空手中显现为盾牌，你熟练使用此盾；失能或用附赠动作解散时盾牌消失。10级时该盾牌提供的AC加值提高到3。这是The Parasite早期强度的另一半：它不只是近战魔契师，还能在不依赖普通装备的情况下获得盾牌防线。对一个仍可保留远程魔能爆底盘、又可用长触及武器作战的角色来说，3级免费盾和10级+3盾都很可观。

6级`Birth Parasite`可花1分钟在5尺内空位挤出一块独立宗主碎片，表现为`Find Familiar`式魔宠，数据使用`Parasitic Ooze`。若你有链之契，它也算作魔宠以接受相关收益。短休或长休后可再次生产；已有黏液时再用会让旧黏液溶解。`Parasitic Ooze`是微型黏怪，AC为`8 + PB`，生命值为`5 + 3倍魔契师等级`，15尺步行/攀爬，黯蚀抗性，免疫目盲、魅惑、耳聋、力竭、恐慌和倒地，能穿过1寸空间、倒挂攀爬、静止伪装成油池或湿石；伪足用你的法术攻击命中，造成`1d6 + PB`钝击。它不是高伤害召唤，但作为侦察、触发、贴身阻挡和后续承伤载体很好用。

同为6级的`Liquefied Body`让你用附赠动作把身体变成黏稠液体10分钟，装备可落在原地或并入形态；期间能挤过6寸宽空间，且穿越困难地形不额外耗移动。短休或长休一次。这给潜入、逃脱、地牢移动和污染废墟探索很强的非战斗弹性，也和黏液魔宠主题对齐。它的直接战斗收益有限，但能改变很多场景的进入/撤离方式。

10级`Transmit Parasite`让你在`Parasitic Ooze`未失能时用附赠动作命令它立刻执行两种选项之一。`Detonate Ooze`使黏液移动至多自身速度后爆炸并掉到0生命，10尺内每个生物对你的魔契师法术DC作敏捷豁免，失败受4d6黯蚀并目盲到你下回合结束，成功半伤且不目盲。`Symbiote's Ward`使黏液移动至多自身速度并附着到5尺内自愿生物身上；附着期间黏液失能、速度为0，你能和被附着者心灵沟通，且该生物每次受伤时由黏液代替承受伤害；你可用附赠动作命令它脱离。

这是中高阶主要跃迁。爆炸的4d6不大，但短休黏液、10尺AoE和无额外资源目盲很实用；承伤模式则让黏液的生命值变成队友保护池。它不是无限护盾，因为黏液血量随等级线性增长而AC低，被打空就没了，且需要提前生产、移动和附着；但它把一个原本偏侦察的魔宠变成可靠的战术资源。

14级`Virulent Form`用动作获得1分钟形态，短休或长休一次：体型增大一级，若空间不足则不变；每回合开始获得等于魅力调整值的临时生命，至少1；寄生武器伤害骰变为2d8；寄生武器攻击19或20重击；当你受到来自寄生武器触及内生物的伤害时，可用反应以寄生武器攻击该生物。这个终局特性把The Parasite推向真正的个人前线形态，尤其在17级后四次2d8攻击、19-20重击和受伤反击叠加时，近战表现不差。

不过`Virulent Form`仍有边界。它用动作启动，临时生命每回合只有魅力调整值规模，反击要求敌人在你的寄生武器触及内且你保留反应；它不提供飞行、豁免光环、队伍动作经济或高环施法改写。它更像“我终于完全变成寄生怪物”，而不是顶级宗主那种能改写整场遭遇的终局按钮。

整体结论：The Parasite是很结实、很有画面的近战/防护宗主。T1有免费盾、魅力长触及武器、力量豁免替换和防护扩表，达到A+；T2有多段寄生武器、魔法武器、黏液魔宠、液化身体，以及`Haste`/`Spirit Guardians`可选，进入A+高位；T3靠10级+3盾、黏液承伤/爆炸目盲、三段寄生武器和高阶魔契师底盘进入S-；T4有四段2d8、19-20重击、受伤反击和完整奥秘，但仍偏个人战斗与保护，维持S-。它比Flesh Patron更像固定战斗形态、比The Parasite Patron健康许多，也低于Cosmic Patron那种远程稳定循环和Grim Hollow寄生宗主的反施法失衡压制。

## 分项评分
| 项目 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | A | A+ | A+ | S- |
| 远程伤害者 | A | A | A | A |
| 法术伤害者 | B | A | A+ | A+ |
| 防御和生存 | A | A+ | S- | S- |
| 治疗和临时生命 | B | B+ | A | A |
| 团队增益 | B | B+ | A | A |
| 反制施法者 | D | D | D | D |
| 减益 | B | A | A+ | A+ |
| 战场分隔 | C | A | A | A |
| 召唤 / 伙伴 | E | A | A+ | A+ |
| 技能使用 | B | A | A | A |
| 制造 | E | E | E | E |

## 综合评分
| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | 3-4级有免费显现盾、魅力长触及1d12寄生武器、力量豁免替换，以及`Sanctuary`/`Heroism`等扩表可选；但寄生武器不加属性伤害，旧扩表也不是始终准备。 |
| Tier 2（5-10） | A+ | 5-10级寄生武器多段和魔法化、`Haste`/`Spirit Guardians`可选、短休黏液魔宠、液化身体与10级+3盾成型；强项很实用，但输出和伙伴血量仍有天花板。 |
| Tier 3（11-16） | S- | 11-16级三段寄生武器、黏液爆炸目盲、黏液替队友承伤、`Black Tentacles`/`Freedom of Movement`可选和高阶魔契师底盘让防御与战术资源进入强档；缺少反制和团队终局引擎。 |
| Tier 4（17-20） | S- | 17-20级四段2d8寄生武器、19-20重击、受伤反击、每回合小额临时生命和完整`玄奥秘法`让个人前线很稳；但14级主要强化自身肉搏，无法上探S。 |

## 设计相关评分
| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B+ | 寄生武器、活体盾、黏液魔宠、液化身体、承伤转移和终局怪物形态层层推进，结构清楚；扣分点是旧接口兼容、寄生武器与`Eldritch Blast`祈唤的可选侧栏会制造明显桌差。 |
| 主题 | A | 宿主体内武器、共生护盾、生产黏液子体、液化肉身、黏液附体替伤和终局寄生怪物形态都高度贴合“寄生者”。 |
| 能力设计质量 | B | 大多数规则可执行，且每个阶段都有明确新玩法；但寄生武器不加属性伤害又给可选祈唤兼容建议，导致默认强度和许可后强度相差很大，10级承伤也需要仔细处理黏液何时承受与归零。 |
| 主题与能力关联度 | A | 该子职的战斗、防御、侦察、保护和终局都由寄生共生体直接提供，玩法与主题高度重合。 |

## 校准说明
本轮按`HelianasGuidetoMonsterHunting`旧`Warlock|PHB`文本兼容XPHB魔契师评估。`DND5e_chm`未定位该子职可靠中文正式译名，因此保留英文名`The Parasite`。源文的“允许以`Eldritch Blast`为前提的祈唤影响寄生武器”属于DM可选建议，本轮不纳入默认评分，只在设计评分中记录其桌差风险。

社区校准检索覆盖：`"The Parasite" warlock "Heliana's Guide to Monster Hunting"`、`"Parasitic Weapon" "The Parasite" warlock`、`"Birth Parasite" "Transmit Parasite" warlock`、`site:reddit.com "The Parasite" "Heliana" warlock`、`"Heliana's Guide" "The Parasite" warlock`、`"Parasitic Weapon" "Heliana"`、`"Virulent Form" "Parasitic Weapon"`与`site:dndbeyond.com/forums "The Parasite" "Heliana" warlock`；未定位稳定同版本强度讨论。本轮以本地Heliana文本、XPHB魔契师底盘和已重评魔契师横向样本为主。

主要本地来源：`5etools-homebrew/collection/Loot Tavern; Heliana's Guide To Monster Hunting.json`中的`The Parasite|Warlock|PHB|Parasite|HelianasGuidetoMonsterHunting`、`Parasitic Weapon`、`Symbiotic Reinforcement`、`Birth Parasite`、`Liquefied Body`、`Transmit Parasite`、`Virulent Form`、`Parasitic Ooze`与`Endure`。
