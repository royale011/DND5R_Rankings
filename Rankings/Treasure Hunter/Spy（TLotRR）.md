# Spy（TLotRR）评测

## 目录

- [概要](#概要)
- [详细评价](#详细评价)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 概要

Spy 是 `Treasure Hunter|TLotRR` 的侦查、反渗透和弱点锁定Speciality。本轮依据本地 `5etools-homebrew\collection\Free League; The Lord of the Rings Roleplaying.json` 核对 `Spy|Treasure Hunter|TLotRR`：3级获得 `Cunning Eye` 与 `Weak Spot`，7级获得 `Sharp-Eyed`。`DND5e_chm`、`5etools-cn` 与既有 `Rankings` 未定位可靠中文正式译名，因此文件暂保留英文名。

Spy 的强点是把Treasure Hunter的侦查技能和偷袭兑现连在一起。`Cunning Eye` 用Int补Insight/Perception，并允许用Cunning Action进行Search；`Weak Spot` 用附赠动作对30尺可见目标进行Investigation或Perception对抗目标Stealth，成功后1分钟内即使没有优势也能对该目标使用Sneak Attack；`Sharp-Eyed` 再在低速移动时给Investigation和Perception优势。它不增加偷袭骰本身，但显著提高“单独盯住一个目标并稳定打出偷袭”的能力。

## 详细评价

3级 `Cunning Eye` 允许把Intelligence调整值加入Wisdom (Insight) 和Wisdom (Perception) 检定，并能用 `Cunning Action` 的附赠动作执行Search。前半部分把Treasure Hunter的智力豁免/调查主题真正接到常用感知技能上，后半部分让战斗中找隐藏敌人、识破环境线索、定位目标或处理侦查任务更省动作。它不是直接伤害，但对斥候/间谍位很关键。

同为3级的 `Weak Spot` 是Spy的战斗核心。你能用附赠动作对30尺内可见生物进行Intelligence (Investigation) 或Wisdom (Perception) 检定，目标用Dexterity (Stealth) 对抗；你赢后，即使没有攻击优势，也可以对该目标使用Sneak Attack，前提是你没有劣势。效果持续1分钟，或直到你成功对另一个目标使用该能力。它解决了远程或单独行动时“没有队友贴身/没有优势就丢偷袭”的问题，尤其适合侦查先手、屋顶射击、单体追杀和Boss盯防。限制是需要附赠动作、需要看见目标、要赢对抗检定，且不能绕过劣势。

7级 `Sharp-Eyed` 在同一回合移动不超过半速时，让Investigation和Perception检定具有优势。它与Cunning Eye、Expertise、Reliable Talent和Weak Spot同向叠加：你越像一个慢速观察、找破绽、拆伪装的间谍，收益越高。限制同样来自半速移动和可见目标条件；在高速追击或遮蔽很少的战斗里，它更像侦察保障而非纯战斗加成。

综合来看，Spy 是Treasure Hunter家族中最强的实战Speciality。它把技能可靠性转成偷袭准入，既加强侦查身份，也让远程/单独潜入更稳定。由于它没有额外攻击、没有增加偷袭骰、没有控制/反制/施法，T2仍停在A+，不进入Champion强Way的S线。

## 分项评分

> TLotRR的Calling/职业表原生止于10级；本文件只评价Tier 1与Tier 2，Tier 3/Tier 4不评估。

| 项目 | Tier 1（1-4） | Tier 2（5-10） |
|---|---|---|
| 近战伤害者 | A- | A |
| 远程伤害者 | A | A+ |
| 法术伤害者 | F | F |
| 防御和生存 | B+ | A- |
| 治疗和临时生命 | F | D |
| 团队增益 | C | C+ |
| 反制施法者 | F | F |
| 减益 | D | C |
| 战场分隔 | F | F |
| 召唤 / 伙伴 | F | F |
| 技能使用 | A+ | S- |
| 制造 | C | B |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | Treasure Hunter低级底盘叠加Int加入Insight/Perception、附赠动作Search和`Weak Spot`单体偷袭准入，使远程/潜入场景的偷袭兑现更稳定；限制是要附赠动作并赢对抗检定。 |
| Tier 2（5-10） | A+ | 3-5d6偷袭、Uncanny Dodge、Reliable Talent、Cunning Eye和`Weak Spot`叠加，使Spy在侦查、找弱点和单体稳定偷袭上最可靠；但仍无施法、反制或额外攻击，保持A+。 |

## 设计相关评分

| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 子职把侦查检定、Search动作和偷袭准入连成一条清楚路线，玩法明确；扣分点是Weak Spot用目标Stealth对抗在非潜行敌人身上略反直觉，且仍受10级封顶限制。 |
| 主题 | A | 洞察、观察、搜索、找弱点和反间谍监视都准确表达Spy，而不是泛泛的伤害增强。 |
| 能力设计质量 | B | 动作、距离、可见目标、持续时间和劣势限制都写得可执行；主要波动来自对抗检定选择和DM如何处理怪物Stealth基准。 |
| 主题与能力关联度 | A | 最强玩法就是观察目标、发现破绽并稳定偷袭，主题与机制高度一致。 |

## 校准说明

Spy 作为Treasure Hunter Speciality横向校准。它不提高偷袭骰，但提高偷袭可用率，尤其对远程、单独潜入和无队友贴身的场景很重要；因此T1高于Burglar，T2与Burglar同为A+但排序更靠前。T3/T4因TLotRR原生止于10级不评估。
