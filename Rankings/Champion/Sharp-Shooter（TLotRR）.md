# Sharp-Shooter（TLotRR）评测

## 目录

- [概览](#概览)
- [核心机制](#核心机制)
- [本轮重评](#本轮重评)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 概览

Sharp-Shooter 是《The Lord of the Rings Roleplaying》中 Champion 的 Way 子职。本轮依据本地 `5etools-homebrew\collection\Free League; The Lord of the Rings Roleplaying.json` 中 `Sharp-Shooter|Champion|TLotRR`、`Bonus Proficiency`、`Mighty Shot` 与 `True Shot` 重查；`DND5e_chm`、`5etools-cn` 与既有 `Rankings` 未定位到可靠中文正式译名，因此文件保留英文名。

它把Champion推向远程武器伤害路线。3级给感知熟练或专精；`Mighty Shot` 在远程武器攻击前可掷该武器伤害骰，并把点数从命中检定中扣除，若命中则额外掷两个武器伤害骰，每回合一次。7级 `True Shot` 让你在攻击动作中每回合放弃一次攻击，使本回合结束前下一次远程武器命中变成重击。

## 核心机制

`Bonus Proficiency` 很实在。感知熟练/专精不会提高DPR，但对侦察、伏击、守夜和远程角色定位有用；在TLotRR的旅行与危险侦测语境里，这不是空白功能。

`Mighty Shot` 是高风险高收益。它不像2024强力攻击专长那样固定命中惩罚，而是先掷武器伤害骰再扣命中：长弓平均会扣4.5，重弓/大弓更痛，短弓略低。命中后额外两个武器伤害骰，每回合一次。它适合有优势、低AC目标、Bless/灵感/高命中堆叠或必须爆发的场面；若盲目每轮使用，会因命中损失吞掉收益。

7级 `True Shot` 改变了计算。你可以在攻击动作里放弃一次攻击，换取本回合下一次远程武器命中变成重击。5-9级通常从两次攻击变成一次高质量命中；10级有三次攻击，放弃一次后仍剩两次尝试，稳定性明显提高。若DM按通常重击规则翻倍伤害骰，`Mighty Shot`的额外武器骰也会在重击时被放大；但它仍然需要命中，且没有把命中失败改成命中。

## 本轮重评

本轮社区校准检索覆盖 `The Lord of the Rings Roleplaying Sharp-Shooter Mighty Shot`、`TLotRR True Shot`、`Lord of the Rings Roleplaying Champion Sharp-Shooter`、Reddit、D&D Beyond 论坛与通用网页方向；未定位到稳定同版本强度讨论或实战优化专帖。公开材料主要是资料介绍，因此本轮按本地TLotRR文本、Champion基础职业、远程DPR横向样本和10级封顶结构独立判断。

Sharp-Shooter 的强度不在防线或控场，而在“远程命中资源足够时，单回合伤害骰很厚”。它比基础Champion更能利用Archery风格与10级三次攻击，但不如Slayer的无资源抗性和先手/免伏击宽。综合定为 `A+ / S-`；T3/T4因TLotRR原生止于10级不评估。

## 分项评分

> TLotRR的Calling/职业表原生止于10级；本文件只评价Tier 1与Tier 2，Tier 3/Tier 4不评估。

| 项目 | Tier 1（1-4） | Tier 2（5-10） |
|---|---|---|
| 近战伤害者 | C | C |
| 远程伤害者 | A+ | S |
| 法术伤害者 | F | F |
| 防御和生存 | A | A |
| 治疗和临时生命 | C | C+ |
| 团队增益 | C | C |
| 反制施法者 | F | F |
| 减益 | E | E |
| 战场分隔 | D | D |
| 召唤 / 伙伴 | F | F |
| 技能使用 | A- | A |
| 制造 | C | B |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | Champion强低级底盘叠加感知熟练/专精与`Mighty Shot`，远程路线在有优势或低AC目标时爆发很好；限制是命中扣减随机且偏重，盲用会亏。 |
| Tier 2（5-10） | S- | 5级两打、7级`True Shot`强制下一次远程命中重击、10级三打与`Mighty Shot`伤害骰叠加，形成很高的远程武器DPR窗口；但仍需命中，没有控制/反制/施法，保持S-。 |

## 设计相关评分

| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 远程高手主题清晰，感知、强射和真射形成明确玩法；扣分点是`Mighty Shot`随机命中扣减会让收益计算不直观。 |
| 主题 | A | 精准射手、巨弓重击和侦察感知都贴合主题。 |
| 能力设计质量 | B- | `True Shot`与`Mighty Shot`互动有趣，但放弃攻击、命中扣减、重击骰翻倍和10级三打的组合需要玩家仔细计算。 |
| 主题与能力关联度 | A | 机制几乎全部服务远程狙击和关键一箭。 |

## 校准说明

Sharp-Shooter 在Champion组内是远程DPR路线。它的T2高于基础Champion的远程面，但综合仍为S-而非S，因为强点集中在伤害骰和重击窗口，缺少Slayer的无资源抗性、先手防伏击和近战承伤能力，也没有施法/控制。
