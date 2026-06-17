# Sanguine Thief（GrimHollowPG24）

## 目录

- [概述](#概述)
- [核心机制](#核心机制)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计评分](#设计评分)
- [更新记录](#更新记录)

## 概述

本评审采用 Grim Hollow: Player's Guide 2024 `Sanguine Thief`，并放在 XPHB 2024 游荡者底盘上比较。本地规则文本核对自`5etools-homebrew\collection\Ghostfire Gaming; Grim Hollow - Player's Guide - 2024.json`；`DND5e_chm`仅定位到旧版《鬼魅幽谷》资料，未定位到该子职的可靠中文译名，因此文件名和正文显示名暂保留英文。

Sanguine Thief 是血魔法版诡术游荡者：它获得智力施法的三分之一法师施法，且没有学派限制；同时把1-4环的 Sangromancy 法术视为本子职的法师法术，并用一池 d8 Sangromancy Dice 替代这些血术法术和本子职能力所需的 Hit Dice。它的强度不来自单个爆炸特性，而来自“完整低环法师工具 + 血术资源缓冲 + 游荡者技能/偷袭底盘”的叠加。

这使它明显强于普通只给若干战斗招式的第三方游荡者。低级已有`护盾术`、`易容术`、`云雾术`、`Find Familiar`类低环工具以及`Blood Rush`/`Somnolence`等血术；中阶进入2环法术后，`Wilting Smite`把命中后的附赠动作爆发、移除抗性和偷袭回合合在一起；13级以后，3环法术与`Reanimate`带来普通游荡者很少见的复活入口；17级`Bloody Exit`则给一次短休级别的自动闪避、传送和反击。

它没有进入S档的原因也很清楚：法术进度仍是三分之一施法，槽位很少，智力有属性压力；Sangromancy Dice 虽然缓解血术成本，但不是额外法术位；很多血术仍要消耗动作、专注、材料、近身位置或合适目标。它是一个宽而强的A+级魔法游荡者，而不是能替代满施法者、团队核心防线或终局战役改写器的子职。

## 核心机制

3级`Spellcasting`提供智力施法、三道法师/血术戏法、三分之一施法槽与法师准备法术。准备法术来自法师列表，且 Sangromancy 法术和戏法为本子职视为法师法术；7级可准备2环，13级可准备3环，19级可准备4环。和2024诡术师一样，这个开放法师表本身已经很强：低环防御、潜入、伪装、遮蔽、召唤熟悉魔宠、控制和机动都能补上游荡者短板。

3级`Stolen Power`给一池 d8 Sangromancy Dice，数量等于游荡者偷袭伤害骰数，长休回满；施放 Sangromancy 法术时可用这些骰子替代 Hit Dice。3级`Steal Blood`又允许你在造成偷袭伤害时恢复1枚 Sangromancy Die，若你处于`浴血`则可改为掷该骰回血；次数等于智力调整值，最低1次，长休恢复。这让血术成本不再直接吃角色短休治疗资源，并能在战斗中少量回收。

9级`Bloody Blades`在长休后最多消耗2枚 Hit Dice 或 Sangromancy Dice 造出同等数量的匕首。匕首可作为本子职法术的奥术法器，并允许你手持它们时施放有姿势成分的法术；若用该武器重击，可造成等于当初投入骰数的 d8 黯蚀额外伤害。这个特性主要解决持武施法与主题武器问题，重击收益有味道但不稳定。

13级`Bloodstitch`用魔法动作消耗3枚 Hit Dice 或 Sangromancy Dice，造成30尺自中心可选目标的3d8黯蚀伤害，敏捷豁免减半，并在用它把生物降到0 HP时回收 Hit Die 或 Sangromancy Die；短休或长休一次。这个数值在13级偏低，更多是补充性清杂/收割按钮，不是评分核心。

17级`Bloody Exit`在被攻击命中时，用反应并消耗5枚 Hit Dice 或 Sangromancy Dice，让该攻击自动失手，传送到30尺内可见空位，并可立刻进行一次近战武器攻击；命中则追加5d8黯蚀伤害。短休或长休一次。它是很强的保命与反击特性，尤其适合终局游荡者避开一次关键命中，但仍是个人反应防御，不是队伍级反制。

血术法术中，1环`Blood Rush`能用附赠动作与一枚血术/生命骰回血，`Somnolence`按当前HP阈值制造睡眠并可能附带力竭惩罚；2环`Wilting Smite`在近战命中后附赠动作施放，消耗两枚骰造成额外黯蚀并短暂移除抗性；3环`Reanimate`能在10分钟内复活目标到1 HP并给临时生命，代价是昂贵材料与三枚骰；3环`Sanguine Poppet`提供远距感知/引爆工具；4环`Circle of Scarlet`是大范围黯蚀爆发和临时生命来源。它们让Sanguine Thief比普通诡术师更偏向血术续航、处决和风险资源管理。

## 分项评分

| 项目 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 近战伤害者 | B+ | A- | A- | A |
| 远程伤害者 | B+ | B+ | B+ | B+ |
| 法术伤害者 | B | B+ | A- | A- |
| 控制者 | A- | A | A | A |
| 防御和生存 | A | A | A+ | A+ |
| 治疗和临时生命 | B+ | B+ | A- | A- |
| 支援 | B+ | A- | A | A |
| 探索 | A | A | A | A |
| 社交 | B+ | B+ | B+ | B+ |
| 召唤/仆从 | B+ | B+ | A- | A- |
| 资源经济 | A- | A | A | A |
| 泛用性 | A | A+ | A+ | A+ |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A | 3级开放法师一环准备法术、三道戏法和Sangromancy Dice，已经能补防御、潜入、遮蔽与少量血术续航；但槽位少、智力吃紧，血术池也只有低级偷袭骰规模，所以保持A而非A+。 |
| Tier 2（5-10） | A+ | 7级进入2环法师法术，9级`Bloody Blades`解决武器/法器手位，`Wilting Smite`等血术让近战命中后的爆发和抗性处理更强；它比普通诡术师更有战斗资源厚度。 |
| Tier 3（11-16） | A+ | 13级取得3环法术、`Reanimate`复活入口、`Sanguine Poppet`和更多Sangromancy Dice，游荡者底盘也有可靠技能与高阶诡诈打击；`Bloodstitch`本身偏弱，但整体工具宽度很高。 |
| Tier 4（17-20） | A+ | 17级`Bloody Exit`提供短休级自动失手、传送和反击，19级才有4环槽与`Circle of Scarlet`等血术；终局仍是强魔法游荡者，但三分之一施法与个人向特性限制它进入S档。 |

## 设计评分

| 项目 | 评级 | 具体理由 |
|---|---|---|
| 设计质量 | B+ | 子职身份清楚，血术资源、开放低环法师表和游荡者偷袭循环能实际运转；扣分点是规则负担偏高，Sangromancy Dice、Hit Dice、施法槽、偷袭触发和材料成本叠在一起，对桌面管理要求不低。 |
| 主题 | A | “以受害者与自己的血为燃料的盗贼/刺客”表达鲜明，血刃、血术、复活、红雾撤离和浴血回血都很有辨识度。 |
| 能力设计质量 | B+ | `Stolen Power`给血术成本一个独立缓冲，`Steal Blood`把资源回收到偷袭循环，`Bloody Exit`也很干净；但开放法师表再叠第三方血术池，边界比普通官方子职更宽，需要DM仔细确认法术选择和资源替代。 |
| 主题与能力关联度 | A | 主要机制几乎都围绕血、偷袭、伤口、红雾和生命代价展开；即使最强部分包含普通法师低环工具，也能服务潜入型血术刺客，而不是完全偏离主题。 |

## 更新记录

本轮新增评审。社区校准检索覆盖`"Sanguine Thief" "Grim Hollow" rogue`、`"Sanguine Thief" "GrimHollowPG24"`、`site:reddit.com "Sanguine Thief" "Grim Hollow"`、`site:dndbeyond.com "Sanguine Thief" rogue`、`"Stolen Power" "Sanguine Thief"`、`"Steal Blood" "Sanguine Thief"`、`"Bloody Exit" "Sanguine Thief"`、`"Bloodstitch" "Sanguine Thief"`、`"Grim Hollow Player's Guide 2024" "Rogue" "Sanguine"`与`"Sanguine Thief" "Sangromancy"`；未定位到稳定同版本强度讨论，本轮以本地GrimHollowPG24文本、XPHB游荡者底盘、2024诡术师和已完成游荡者第三方样本为主。
