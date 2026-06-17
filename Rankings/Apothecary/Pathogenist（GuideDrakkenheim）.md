# Pathogenist（GuideDrakkenheim）评级

所属职业：Apothecary

英文名 / 社区检索名：Pathogenist / Apothecary Pathogenist

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

Pathogenist 是 Apothecary 的疾病、毒素和持续减益路线。它的低级强度来自 Apothecary 本体的治疗/控制/复原底盘、始终准备的疾病法术、`Infect` 与 `Mutant Strain`；中级开始获得疾病免疫穿透、死亡传播、无专注 `Infect`；14级以后，一旦敌人感染你的疾病，就会对你的 Apothecary 法术豁免处于劣势，直接把“先感染，再控制”的战术推到高阶强控制线。

它的限制也同样清楚：许多核心法术瞄准体质豁免，疾病与中毒主题在怪物生态里经常遇到免疫、抗性、高体质、传奇抗力或复原法术；`Breakthrough Infection` 虽然能无视疾病免疫，但会让免疫目标对你的疾病豁免有优势。也就是说，Pathogenist 的上限很高，但它不像 Alienist 那样直接把关键智/感/魅豁免成功压回去，而是需要先让疾病命中并维持。

## 核心特性分解

1级 `Plague Proficiency` 给 `Chill Touch` 戏法与草药包熟练。`Pathogenist Spells` 始终准备 `Infect`、`Inflict Wounds`、`Blindness/Deafness`、`Biohazard`、`Pestilence`、`Venomous Aura`、`Blight`、`Blood Worm`、`Contagion`、`Insect Plague`，这让 Pathogenist 从低级开始就有死灵伤害、目盲/耳聋、疾病、毒云和虫群压场。`Infect` 本身是1环、60尺、专注1分钟的体质豁免疾病：目标每回合开始体质豁免，失败受死灵伤害，三次成功后法术结束，`Lesser Restoration` 可提前结束。

3级 `Mutant Strain` 是子职的核心菜单。你从2个已知菌株开始，9级为3个，15级为4个；每次施放会造成疾病的法术时，可把一个菌株效果附加到目标身上，持续至该法术结束。低级可选项包括禁止反应、失败疾病豁免后速度降到5尺、每回合体质豁免失败后不能说话、每回合开始掉落手持物。9级后有近战武器伤害减半、失败疾病豁免后目盲、不能恢复生命、失去伤害抗性；15级后有失败疾病豁免后失能，以及获得钝击/穿刺/挥砍易伤。这个菜单的上限很高，尤其失能、禁疗、去抗性和B/P/S易伤都能显著改变团队击杀窗口。

3级 `Pernicious Pathogens` 保护你的疾病不被轻易清掉。任何生物施放法术或使用特质/能力来治愈或移除你的疾病时，必须先用施法属性，或未指定施法属性时用魅力调整值，进行一次属性检定，DC等于你的法术豁免DC；失败则法术、特质或能力无效，材料和法术位也被浪费。它不是直接提升命中，但会显著抬高敌方解病成本。

6级 `Breakthrough Infection` 让你用 Apothecary 法术位或 `Greater Formula` 施放会造成疾病的法术时，无视生物的疾病免疫；这类生物改为对你的疾病豁免有优势。这个特性非常关键，因为否则疾病路线在高阶会被免疫生态压扁。优势仍是强限制，但至少让路线不被单行免疫关闭。

同为6级的 `Outbreak` 让一个感染你疾病的生物死亡时，你可用反应把疾病传播给该生物30尺内你能看见的另一个生物。它在清杂和连续遭遇里有价值，但需要感染目标先死、消耗反应、需要可见新目标，不能当作无条件群控。

10级 `Insidious Incubation` 每短休或长休一次，在开始施放 `Infect` 时可让它不需要专注，但本次持续时间变为1分钟。这个节点让 Pathogenist 可以同时维持一个疾病基底和普通 Apothecary 专注法术，是T2后半到T3的关键跃迁。它只指定 `Infect`，且次数有限，所以不是所有疾病法术都获得无专注。

14级 `Immunocompromised` 是真正的高阶爆点。感染了你疾病的生物，对你的 Apothecary 法术豁免具有劣势。由于 Apothecary 本身有 `Hypnotic Pattern`、`Fear`、`Slow`、`Hold Monster`、`Polymorph`、`Greater Formula` 等强法术，一旦先手疾病站住，后续控制、处决、剥夺行动和高阶解题法术的可靠性都会明显提高。限制是你必须先让疾病命中并维持，且传奇抗力、免疫、解除疾病、体质高豁免和距离/视线仍会参与博弈。

18级 `Rapid Evolution` 让你施放会造成疾病的法术时，对该法术的一个目标改为附加两个菌株效果。终局常见组合如失能+禁疗、失能+易伤、目盲+去抗性、禁反应+不能说话，都会把一个成功感染的目标变成团队集火或控制连锁的核心。它强，但仍是建立在“疾病先成立”的条件之上。

## 资料与社区校准

本轮依据本地 `5etools-homebrew\collection\Ghostfire Gaming; Sebastian Crowe's Guide to Drakkenheim.json` 中 `Pathogenist|Apothecary|GuideDrakkenheim|Pathogenist|GuideDrakkenheim` 及其 `Plague Proficiency`、`Pathogenist Spells`、`Pernicious Pathogens`、`Mutant Strain`、`Breakthrough Infection`、`Outbreak`、`Insidious Incubation`、`Immunocompromised`、`Rapid Evolution` 重查。`DND5e_chm`与`5etools-cn`未定位可靠中文正式译名，因此文件保留英文名。

社区校准检索覆盖 `Pathogenist Apothecary Drakkenheim balance review`、`"Pathogenist" "Apothecary" "Drakkenheim"`、`"Pernicious Pathogens" "Apothecary"`、`"Mutant Strain" "Pathogenist" "Drakkenheim"`、Reddit、D&D Beyond论坛与通用网页方向；未定位稳定同版本强度讨论。本轮按本地文本、Apothecary基础职业重评结论和当前第三方新职业横向样本独立判断。

## 横向比较

横向校准后，Pathogenist 的低级不应超过 Alienist/Exorcist：它有很强的减益菜单，但疾病通常要先过体质豁免并持续，而低级资源槽少。T2进入S，是因为9级菌株、免疫穿透、疾病传播和10级无专注 `Infect` 已经让它能同时铺病和施放普通控制。T3-T4进入S+，主要来自14级 `Immunocompromised`：感染目标对你的 Apothecary 法术豁免劣势，和高阶公式/短休5环槽叠加后非常接近“先设定状态，再压关键法术”的控制引擎。它不进EX，因为疾病入口、体质豁免、免疫目标优势、解除疾病检定、反应传播限制、传奇抗力和条件免疫都是真实边界。

## 分项评分

| 评分项 | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |
|---|---|---|---|---|
| 法术伤害者 | A | A+ | A+ | S- |
| 控制 | A | S- | S | S+ |
| 减益 | A+ | S | S+ | S+ |
| 防御和生存 | A- | A | A | A+ |
| 探索和社交 | A- | A | A | A |
| 团队支援 | A | A+ | S- | S |
| 资源效率 | A | S- | S | S |

## 综合评分

| 阶段 | 综合强度 | 具体理由 |
|---|---|---|
| Tier 1（1-4） | A+ | Apothecary强底盘加始终准备疾病/死灵扩表、`Infect`、`Pernicious Pathogens`和初始`Mutant Strain`，低级减益质量很高；但疾病多吃体质豁免、专注和有限短休槽，尚未形成稳定连锁。 |
| Tier 2（5-10） | S | 免疫穿透、疾病死亡传播、9级高价值菌株和10级短休一次无专注`Infect`让Pathogenist能同时铺疾病与维持普通控制，进入强控制子职线；但仍依赖疾病先命中。 |
| Tier 3（11-16） | S+ | 14级`Immunocompromised`让感染目标对你的Apothecary法术豁免劣势，再叠加6-8环`Greater Formula`、短休5环槽和15级失能/易伤菌株，形成高阶控制引擎；体质入口和传奇抗力阻止它进入EX。 |
| Tier 4（17-20） | S+ | 9环公式、额外高阶公式与18级`Rapid Evolution`双菌株叠加，使感染目标可同时承受失能、禁疗、易伤、去抗性或禁反应等压力；仍受疾病成立、免疫目标优势、解病检定和条件免疫约束。 |

## 设计评分

| 评分项 | 评分 | 具体理由 |
|---|---|---|
| 设计质量 | B | 疾病研究、突变症状和传播链条主题鲜明，但大量强度压在自定义疾病法术与菌株菜单上，桌面需要频繁判断哪些法术“造成疾病”。 |
| 主题与能力关联度 | A | 几乎所有核心能力都围绕感染、病原变异、免疫突破、传播和免疫削弱展开，实际玩法很好地表达Pathogenist身份。 |
| 能力设计质量 | B | 菌株选项有明确战术差异，`Immunocompromised`也给出清晰高阶回报；问题是体质入口、疾病免疫优势、解病检定和高阶劣势链条使强弱随遭遇类型摆动很大。 |
| 平衡性 | A- | T3以后非常强，但需要先感染并维持疾病，且会被传奇抗力、高体质、复原资源、条件免疫和疾病免疫优势限制；整体属于高上限、有边界的S+线。 |
