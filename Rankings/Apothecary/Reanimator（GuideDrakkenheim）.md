# Reanimator（GuideDrakkenheim）评级

所属职业：Apothecary

英文名 / 社区检索名：Reanimator / Apothecary Reanimator

来源：Sebastian Crowe's Guide to Drakkenheim（GuideDrakkenheim）

## 目录

- [定位概览](#定位概览)
- [核心特性分解](#核心特性分解)
- [资料与社区校准](#资料与社区校准)
- [横向比较](#横向比较)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计评分](#设计评分)

## 定位概览

Reanimator 是 Apothecary 的尸造伙伴、死灵复生和怪物护卫路线。它不像 Pathogenist/Alienist 那样把敌方豁免可靠性推到顶线，而是把 Apothecary 的强施法底盘与一个可命令的 `Corpsewrought Creature` 结合起来：低级获得额外战斗实体，中级获得护卫反击、死者交谈与知识可靠性，10级后伙伴变大型并获得命中后擒抱，14级双击，18级变巨型、10尺触及、速度和伤害继续提高。

它的主要强度是“强施法者底盘 + 额外身体 + 站位/擒抱/吸收伤害”。主要限制是附赠动作命令、伙伴自身命中/生命/移动、复活需要消耗 Apothecary 法术位且1分钟后才回场，以及高阶缺少直接改写敌方关键豁免或否决Boss动作的机制。因此它很强，但高阶不应和 Alienist、Exorcist、Pathogenist 的 S+控制/防线同档。

## 核心特性分解

1级 `Spark of Life` 给 `Shocking Grasp` 与 `Spare the Dying`，都算作 Apothecary 法术且不占戏法已知。`Reanimator Spells` 始终准备 `False Life`、`Inflict Wounds`、`Gentle Repose`、`Invigorate`、`Lightning Bolt`、`Revivify`、`Death Ward`、`Corpse Explosion`、`Raise Dead`、`Nerve Gas`，并在子职法术列表中出现 `Animate Dead` 与 `Speak with Dead`。这套扩表很符合复生/死灵/电击主题，也补了复活、保命、爆发和尸体利用。

3级 `Corpsewrought Creature` 是路线核心。伙伴是中型构装，AC为 `14 + PB`，生命为 `5 + 5倍Apothecary等级`，有30尺速度、18力量、16体质、体质/感知豁免加PB、运动加PB、60尺黑暗视觉、毒素和闪电免疫、免疫中毒，并能吸收闪电伤害转为治疗。它与Reanimator同先攻，在你之后行动；默认只能移动、反应和闪避，除非你用附赠动作命令它执行动作。它死亡后若在1小时内，你可用动作、治疗包和一个 Apothecary 法术位在1分钟后满血复活；长休也可重造。

低级时这个伙伴已经很实用：它能占位、挡路、提供一次额外近战命中、吸收攻击，并给 Apothecary 这个中甲施法者更多前线空间。但它的攻击需要你的附赠动作，这会和治疗词、部分职业/法术操作以及物品互动形成竞争；伙伴死亡后的战斗内复活也很慢。

6级 `Bodyguard` 让伙伴5尺内的生物攻击你时，伙伴可用反应近战攻击该攻击者，并让伙伴的猛击视为魔法攻击；同时你可以用一个 Apothecary 法术位施放一次 `Animate Dead`，用后长休前不能再通过该特性施放。Bodyguard 很适合把伙伴放在你身边做近身反击，但触发只保护你，不是全队保护光环。

6级 `Reanimated Head` 是探索与信息节点：你可以把一颗复生头颅作为法器，头颅会通用语和一门自选语言；你进行可加入熟练加值的智力属性检定时，d20掷出9或以下视为10，并获得奥秘和调查熟练；还可每短休或长休一次无槽施放 `Speak with Dead`。这个能力很强地表达“疯狂研究者”身份，也让Reanimator在调查、验尸、魔法识别和城市/恐怖冒险里比普通伙伴子职更有存在感。

10级 `Behold, My Creation` 让伙伴变为大型，速度提高到40尺；伙伴近战命中后可立刻尝试擒抱，逃脱DC为 `8 + 伙伴力量调整值（+4） + 你的PB`。这让伙伴从“附赠动作攻击单位”变成能占更大面积、卡位和拉住关键敌人的战术单位。限制是仍要命中，且很多高阶敌人有巨大体型、传送、强运动/特技或免疫/规避抓摔的手段。

14级 `Berserk Fury` 让你命令伙伴执行攻击动作时，伙伴可以攻击两次。这显著提高伙伴的命中稳定、擒抱触发机会和DPR，但仍要吃你的附赠动作。与 Apothecary 本体的高阶公式相比，它是可靠增量，不是系统级突破。

18级 `I Can't Stop The Monster I Created` 让伙伴变为巨型，触及10尺，速度50尺，猛击额外造成1d8钝击伤害，并且可推/举重量翻倍。这是很有视觉冲击的终局怪物，但强度仍主要是站位、触及、擒抱和附赠动作双击；它不会像失败豁免改写、动作否决、无条件队伍数学或 `Wish` 那样直接改变终局规则所有权。

## 资料与社区校准

本轮依据本地 `5etools-homebrew\collection\Ghostfire Gaming; Sebastian Crowe's Guide to Drakkenheim.json` 中 `Reanimator|Apothecary|GuideDrakkenheim|Reanimator|GuideDrakkenheim`、`Corpsewrought Creature` 及其 `Spark of Life`、`Reanimator Spells`、`Corpsewrought Creature`、`Bodyguard`、`Reanimated Head`、`Behold, My Creation`、`Berserk Fury`、`I Can't Stop The Monster I Created` 重查。`DND5e_chm`与`5etools-cn`未定位可靠中文正式译名，因此文件保留英文名。

社区校准检索覆盖 `Reanimator Apothecary Drakkenheim balance review`、`"Reanimator" "Apothecary" "Drakkenheim"`、`"Corpsewrought Creature" "Apothecary"`、`"Reanimator" "Sebastian Crowe's Guide to Drakkenheim"`、Reddit、D&D Beyond论坛与通用网页方向；未定位稳定同版本强度讨论。本轮按本地文本、Apothecary基础职业重评结论、奇械师掘坟人/战地匠师等伙伴子职横向样本独立判断。

## 横向比较

横向上，Reanimator 明显强于普通“给一个宠物”的弱子职，因为它挂在 Apothecary 这种短休高环准备施法底盘上，且伙伴AC/HP/免疫/闪电吸收/复活都不错。它也比很多单纯死灵扩表路线更稳定，因为3级就能提供实体占位，6级又补信息/调查和护卫反击。

但它没有 Pathogenist 14级后的法术豁免劣势引擎，也没有 Alienist 的关键智/感/魅豁免成功重骰取低，更没有 Exorcist 的 `Negation` 动作否决。伙伴双击和巨型触及在高阶好用，却仍停留在战术层；面对高阶飞行、传送、传奇抗力、范围伤害、条件免疫和强位移敌人时，不能替代顶级控制/反制。综合定为 `A+ / S- / S / S`。

## 分项评分

| 评分项 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | A | A+ | S- | S |
| 法术伤害者 | A | A+ | S- | S |
| 控制 | A | A+ | S- | S |
| 防御和生存 | A+ | S- | S | S |
| 探索和社交 | A | S | S | S |
| 团队支援 | A | A+ | S- | S- |
| 资源效率 | A | A+ | S- | S |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | Apothecary强底盘加复生/死灵扩表、两个额外戏法和3级`Corpsewrought Creature`，低级即有额外身体、占位、吸伤和附赠动作攻击；但伙伴命令吃附赠动作，且复活战斗内较慢。 |
| Tier 2（5-10） | S- | 6级护卫反击、魔法猛击、一次`Animate Dead`、智力检定保底10、短休`Speak with Dead`和10级大型擒抱伙伴，让Reanimator同时有战斗实体与调查宽度；但控制仍要命中/擒抱成立。 |
| Tier 3（11-16） | S | 6-8环`Greater Formula`、短休5环槽与14级伙伴双击叠加，伙伴可更稳定触发擒抱并承担前线；强度进入S，但缺少Alienist/Pathogenist级豁免可靠性和Exorcist级动作否决。 |
| Tier 4（17-20） | S | 9环公式、额外高阶公式与18级巨型10尺触及伙伴让站位、擒抱和伤害继续增长；终局仍主要是战术身体和Apothecary底盘，不是S+级规则改写或全队防线。 |

## 设计评分

| 评分项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B+ | 伙伴、复生头颅、死灵扩表和巨型怪物成长线清楚，玩法比纯召唤更有身份；但伙伴规则、复活、命令、体型和擒抱会增加桌面管理量。 |
| 主题与能力关联度 | A | 复活、尸造伙伴、死者交谈、死灵扩表和“我创造的怪物停不下来”都稳定表达Reanimator主题。 |
| 能力设计质量 | B+ | 核心动作经济和伙伴数值边界明确，闪电吸收、智力检定保底和大型擒抱都有辨识度；缺点是高阶成长偏数值/体型，缺少更优雅的终局规则突破。 |
| 平衡性 | A | 伙伴叠加强施法底盘很强，但附赠动作、命中、体型、伙伴生命和高阶怪物机动性都是实际限制；整体位于S线，不压过S+控制/防护子职。 |
