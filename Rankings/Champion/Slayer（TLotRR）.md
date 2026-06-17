# Slayer（TLotRR）评测

## 目录

- [概览](#概览)
- [核心机制](#核心机制)
- [本轮重评](#本轮重评)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 概览

Slayer 是《The Lord of the Rings Roleplaying》中 Champion 的 Way 子职。本轮依据本地 `5etools-homebrew\collection\Free League; The Lord of the Rings Roleplaying.json` 中 `Slayer|Champion|TLotRR`、`Battle-Fury`、`Sterner Than Steel` 与 `War-Hardened` 重查；`DND5e_chm`、`5etools-cn` 与既有 `Rankings` 未定位到可靠中文正式译名，因此文件保留英文名。

它把Champion推向近战狂战士。3级 `Battle-Fury` 在你回合第一次攻击时可选择鲁莽攻击：用力量进行近战武器攻击有优势，伤害加半熟练，直到你下回合开始前获得钝击/穿刺/挥砍抗性，但敌人攻击你也有优势。3级 `Sterner Than Steel` 增加最大生命；7级 `War-Hardened` 给先攻、力量检定、力量豁免优势，并使你在未目盲、耳聋或失能时不能被突袭。

## 核心机制

`Battle-Fury` 是非常强的低魔近战开关。它把野蛮人的鲁莽攻击与物理抗性浓缩进Champion子职：你获得近战力量攻击优势、少量伤害加值和B/P/S抗性，代价是敌人攻击你有优势。由于抗性覆盖最常见武器伤害，很多低魔遭遇中这个代价被抗性显著抵消。它没有写次数限制，默认是每回合可选，强度明显高于普通一次短休爆发。

`Sterner Than Steel` 进一步支持这个风险模型。3级立即+3最大生命，之后每个Champion等级再+1；到10级相当于额外10点生命。它不花动作，不和装备冲突，正好给`Battle-Fury`的被攻击优势兜底。

7级 `War-Hardened` 很宽：先攻优势提升开局权，力量检定/豁免优势支撑擒抱、推拉、抗击倒和环境压力，不能被突袭则让Champion更像永远准备好的战士。限制是它要求不处于目盲、耳聋或失能，且不处理感知豁免、法术控制、飞行/传送、远程风筝或非B/P/S伤害。

## 本轮重评

本轮社区校准检索覆盖 `The Lord of the Rings Roleplaying Slayer Battle-Fury`、`TLotRR War-Hardened`、`Lord of the Rings Roleplaying Champion Slayer`、Reddit、D&D Beyond 论坛与通用网页方向；未定位到稳定同版本强度讨论或实战优化专帖。公开材料主要是资料介绍，因此本轮按本地TLotRR文本、Champion基础职业、近战武职横向样本和10级封顶结构独立判断。

横向上，Slayer 是Champion组内最强的前10级Way。无资源近战优势、常见物理抗性、额外生命、先攻优势和不能被突袭把它推到S线；但它仍是纯武器路线，缺少施法、反制、强控制和11级以上职业表。综合定为 `S- / S`；T3/T4因TLotRR原生止于10级不评估。

## 分项评分

> TLotRR的Calling/职业表原生止于10级；本文件只评价Tier 1与Tier 2，Tier 3/Tier 4不评估。

| 项目 | Tier 1（1-4） | Tier 2（5-10） |
|---|---|---|
| 近战伤害者 | S- | S |
| 远程伤害者 | C | C |
| 法术伤害者 | F | F |
| 防御和生存 | A+ | S- |
| 治疗和临时生命 | C | C+ |
| 团队增益 | C | C |
| 反制施法者 | F | F |
| 减益 | C | C |
| 战场分隔 | D | D |
| 召唤 / 伙伴 | F | F |
| 技能使用 | B | B+ |
| 制造 | C | B |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | S- | Champion低级底盘叠加`Battle-Fury`的近战力量攻击优势、半熟练伤害、B/P/S抗性和`Sterner Than Steel`额外生命，低魔T1前排效率明显高于普通A+武职。 |
| Tier 2（5-10） | S | 两打/三打、短休`Surge of Vigour`、无资源鲁莽优势、物理抗性、额外生命、9级魅惑/恐慌免疫与7级先攻优势/不能被突袭叠加，使Slayer成为TLotRR前10级最强个人战斗底盘之一；缺少施法/反制使其不进S+。 |

## 设计相关评分

| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B- | 狂战士主题清楚、手感强，但无资源B/P/S抗性叠加攻击优势在低魔环境很强，跨到普通5e时需要谨慎校准。 |
| 主题 | A | 鲁莽、坚硬、先手、不能被突袭都直接表达复仇/屠戮战士。 |
| 能力设计质量 | B- | 循环易懂，但`Battle-Fury`同时给优势、加伤和抗性，代价又被抗性部分抵消，数值集中度偏高。 |
| 主题与能力关联度 | A | 能力全部推动“冲上去硬吃伤害并砍倒敌人”的玩法。 |

## 校准说明

Slayer 是Champion组内最高T1-T2路线。它不是因为复杂规则强，而是因为无资源近战优势+B/P/S抗性+额外生命+先攻防伏击在低魔战斗中太稳定。T3/T4因10级封顶不评估；T1-T2仍高于Sharp-Shooter与基础Champion。
