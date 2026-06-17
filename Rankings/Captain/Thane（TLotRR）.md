# Thane（TLotRR）评测

## 目录

- [概览](#概览)
- [核心机制](#核心机制)
- [本轮重评](#本轮重评)
- [分项评分](#分项评分)
- [综合评分](#综合评分)
- [设计相关评分](#设计相关评分)
- [校准说明](#校准说明)

## 概览

Thane 是《The Lord of the Rings Roleplaying》中 Captain 的 Title 子职。本轮依据本地 `5etools-homebrew\collection\Free League; The Lord of the Rings Roleplaying.json` 中 `Thane|Captain|TLotRR`、`Bright Blade` 与 `Tireless Leader` 重查；`DND5e_chm`、`5etools-cn` 与既有 `Rankings` 未定位到可靠中文正式译名，因此文件保留英文名。

它把Captain推向“受王命的近战旗手”。3级 `Bright Blade` 是一次短休/长休恢复的附赠动作武器增益，持续1分钟：你以手中该近战武器攻击时，把魅力调整值加到攻击检定，且每次命中都会让下一次由你以外攻击者在你下回合开始前对该目标的攻击有优势。7级 `Tireless Leader` 让你和10尺内友方承受力竭效果时视为低一级。

## 核心机制

`Bright Blade` 是Captain两个Title里更直接的强度按钮。把魅力调整值加到攻击检定是非常大的命中修正，尤其Captain已经想要魅力来支持 `Leadership`、`Aura of Valour` 和部分Title DC。到5级以后，它会同时提高两次攻击命中率；到6级后又能提高 `Aura of Valour` 伤害实际兑现。命中后给下一名非你攻击者优势，也让Thane在近战队伍中自然承担“先手点亮目标”的角色。

限制同样需要明确。`Bright Blade` 只作用于你持有的近战武器，掉落、离手或昏迷会结束；它短休一次，不能作为全天常驻精度；它不直接给队友伤害，只给下一次攻击优势，且要求队友在你下一回合前攻击同一目标。若队伍以远程、法术豁免或控制为主，Thane的输出放大明显缩水。

7级 `Tireless Leader` 在TLotRR语境下很有价值。Journey、Shadow、艰苦旅行和低魔资源压力都会让力竭成为真实威胁，10尺团队降一级效果可以保护队伍不被疲劳拖垮。放进普通5.5e高魔战役时，它的价值更取决于DM是否频繁使用力竭、采用哪版力竭规则、以及队伍是否已经能用法术/休整解决环境损耗。作为战斗特性，它不如Chieftain的锁速直接；作为中洲冒险功能，它很贴题。

## 本轮重评

本轮社区校准检索覆盖 `The Lord of the Rings Roleplaying Thane Bright Blade`、`TLotRR Thane Bright Blade`、`Tireless Leader Captain TLotRR`、Reddit、D&D Beyond 论坛与通用网页方向；未定位到稳定同版本强度讨论或实战优化专帖。公开材料主要停留在TLotRR资料介绍层面，因此本轮按本地TLotRR文本、Captain基础职业、低魔10级结构和当前第三方武职子职横向样本独立判断。

横向上，Thane 是Captain两条Title里更强的T2数值路线。`Bright Blade` 的命中加值不是小修小补，而是能把Captain本人的攻击、6级加伤光环和队友下一击优势串起来；7级力竭光环又补中洲旅行耐力。它仍不是完整S线武职，因为资源短休一次、近战限定、没有硬控/反制/施法，也没有11级后原生成长。综合定为 `A+ / S-`；T3/T4因TLotRR原生止于10级不评估。

## 分项评分

> TLotRR的Calling/职业表原生止于10级；本文件只评价Tier 1与Tier 2，Tier 3/Tier 4不评估。

| 项目 | Tier 1（1-4） | Tier 2（5-10） |
|---|---|---|
| 近战伤害者 | A | A+ |
| 远程伤害者 | C | C |
| 法术伤害者 | F | F |
| 防御和生存 | A | A |
| 治疗和临时生命 | B+ | B+ |
| 团队增益 | A- | A+ |
| 反制施法者 | F | F |
| 减益 | E | E |
| 战场分隔 | F | D |
| 召唤 / 伙伴 | F | F |
| 技能使用 | B | B+ |
| 制造 | C | B |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | Captain低级底盘叠加3级`Bright Blade`，短休一次附赠动作让近战武器攻击加魅力命中，并在命中后给下一名非你攻击者优势；低级命中和团队点杀都明显强于基础Captain。 |
| Tier 2（5-10） | S- | 额外攻击、6级近战加伤光环和`Bright Blade`命中修正叠加，使Thane在关键战斗中能稳定兑现个人与队友近战DPR；7级`Tireless Leader`又给TLotRR旅行/力竭环境真实耐力。短休一次、近战限定、无硬控和无施法让它停在S-。 |

## 设计相关评分

| 设计项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 子职很清楚地把Captain做成近战旗手，且`Bright Blade`与基础魅力/光环资源自然相连；扣分点是命中加魅力的数值很大，低魔可控但跨到普通5e时需要注意短休爆发窗口。 |
| 主题 | A | 王命战士、明亮武器、带队抗疲劳都贴合Thane的忠诚近卫主题。 |
| 能力设计质量 | B | 两个特性都容易执行，`Bright Blade`的离手/昏迷结束条件也清楚；但队友优势窗口、近战武器绑定和不同版本力竭规则会带来一定桌面校准。 |
| 主题与能力关联度 | A- | 能力确实让Thane先击中目标、引导队友攻击并支撑旅途耐力；力竭光环更偏冒险流程而非战斗循环，但仍符合中洲题材。 |

## 校准说明

Thane 在Captain组内高于Chieftain的主要原因是`Bright Blade`直接提高命中并联动6级伤害光环和队友优势，T2爆发/稳定性更强；但它缺少Chieftain的锁线能力，也没有施法或高阶成长。因此T2上调到S-，T1为A+，T3/T4因TLotRR原生止于10级不评估。
