from pathlib import Path

from generate_rankings import ASPECTS, TIERS, CLASSES, OUT, BUILDS, aspect_table, build_overall as base_build_overall, table, record_doc, summary_doc


CLASS_DESIGN = {
    "野蛮人": {
        "设计质量": "B：核心循环非常清楚，Rage、Reckless Attack、Weapon Mastery 能稳定表达前排压迫；扣分点是高等级仍缺少可靠的反制、飞行、位移和非战斗解题工具。",
        "主题": "A：愤怒、强韧、原始力量和危险前排形象直接有效。",
        "能力设计质量": "B：数值和动作经济比 2014 顺，但不少高等级能力只是“更能打/更能扛”，没有给出足够新战术维度。",
        "主题与能力关联度": "A：绝大多数能力都在支持“靠身体和怒火解决问题”。",
    },
    "战士": {
        "设计质量": "A：2024 战士终于更像战斗专家，Weapon Mastery、Second Wind 扩展和子职战术能支撑多种武器路线。",
        "主题": "B：职业主题故意宽泛，方便容纳士兵、决斗者、骑士、射手；代价是基础职业个性不如圣武士或武僧鲜明。",
        "能力设计质量": "A：动作、资源和成长节奏干净，Action Surge 仍是强而易懂的核心爆点。",
        "主题与能力关联度": "A：机制基本都在服务“比别人更懂战斗”。",
    },
    "武僧": {
        "设计质量": "S：新版把旧版最大问题，资源紧、伤害低、防御脆、机动与控制互相抢动作，基本全部修正。",
        "主题": "A：高速武术、内力、纪律和超凡身体表达充分。",
        "能力设计质量": "S：攻击、防御、机动、控制的资源曲线非常顺，玩家每轮有真实选择。",
        "主题与能力关联度": "A：机制强烈支持“靠训练和内力支配战场”，只有少数子职仍像半施法翻译。",
    },
    "圣武士": {
        "设计质量": "A：Smite 爆发被拉回合理区间后，职业仍靠光环、誓言、治疗和武器维持清楚队伍位置。",
        "主题": "A：誓言骑士、神圣守护和惩戒恶敌的幻想非常稳。",
        "能力设计质量": "B：Aura of Protection 仍强到几乎定义职业，导致设计预算被单一能力占据；新版 Smite 限制则牺牲了一部分爽感。",
        "主题与能力关联度": "A：光环、圣疗、誓言法术和惩戒都紧扣主题。",
    },
    "游侠": {
        "设计质量": "C：实战不弱，但职业被 Hunter's Mark 牵着走，集中检定和法术选择经常互相打架。",
        "主题": "B：猎手、荒野专家、探索者主题明确，但“半施法武器手”和“标记猎物机器”之间有割裂。",
        "能力设计质量": "C：武器、技能和法术都可用，问题是许多能力把玩家推回同一套标记流程。",
        "主题与能力关联度": "C：探索和猎杀主题存在，但机制常把复杂荒野幻想压缩成额外 d6。",
    },
    "游荡者": {
        "设计质量": "B：Cunning Strike 让玩法明显更有趣，但战斗资源和高等级影响力仍不足。",
        "主题": "A：技能专家、偷袭者、潜入者的职业幻想非常清楚。",
        "能力设计质量": "B：无资源循环优雅，问题是偷袭骰同时承担伤害和控制成本，优化环境里容易显弱。",
        "主题与能力关联度": "A：Expertise、Sneak Attack、Cunning Action 都精准表达狡猾专家。",
    },
    "吟游诗人": {
        "设计质量": "A：技能、施法、激励和魔法秘密组成最完整的队伍工具箱之一。",
        "主题": "A：表演者、学识者、鼓舞者和社交核心都能成立。",
        "能力设计质量": "A：Bardic Inspiration 与法表支撑多角色定位，强但不如法师那样完全吞掉子职存在感。",
        "主题与能力关联度": "A：用语言、艺术和知识改变战局的主题与机制高度一致。",
    },
    "牧师": {
        "设计质量": "A：领域、神术、护甲、治疗和 Channel Divinity 的结构稳定，几乎没有真正弱期。",
        "主题": "A：神力代理人主题清楚，领域让不同神格/理念有足够差异。",
        "能力设计质量": "A：强度很高但队伍定位清晰；主要风险是 Spirit Guardians 系和治疗/防御叠加让低中等级过硬。",
        "主题与能力关联度": "A：神术、领域法术、引导神力和复活都直接支撑信仰主题。",
    },
    "德鲁伊": {
        "设计质量": "A：Wild Shape 更规整，法表仍强，治疗、召唤、地形和侦察让职业位置完整。",
        "主题": "A：自然施法者、变形者、生态守护者的主题非常强。",
        "能力设计质量": "A：新版降低旧月亮德鲁伊低级离谱度；但召唤和地形法术仍会给 DM 带来管理压力。",
        "主题与能力关联度": "A：变形、自然控制、召唤和治疗都服务同一主题。",
    },
    "术士": {
        "设计质量": "A：新版改善已知法术压力，超魔法和子职额外法术让奥术爆发职业更完整。",
        "主题": "A：血脉/异变/天赋施法者的幻想清楚。",
        "能力设计质量": "A：Metamagic 是强设计核心；强子职额外法术会显著拉开子职差距。",
        "主题与能力关联度": "A：用内在魔力扭曲法术的表达非常直接。",
    },
    "魔契师": {
        "设计质量": "A：契约、祈唤、短休法术和 Eldritch Blast 让职业高度模块化。",
        "主题": "A：与超自然宗主交易力量的主题鲜明。",
        "能力设计质量": "A：自定义空间强，但也最容易产生多职业前置滥用和规则边界讨论。",
        "主题与能力关联度": "A：宗主赠礼、契约和祈唤都在表达“借来的异界力量”。",
    },
    "法师": {
        "设计质量": "A：法术书、准备施法和学派结构是 D&D 奥术核心；扣分来自法表过强压低子职差异。",
        "主题": "A：研究、知识、仪式和奥术掌控表达非常强。",
        "能力设计质量": "A：单项能力并不总夸张，但整个法表组合在高等级形成系统性统治。",
        "主题与能力关联度": "A：几乎所有机制都在服务“知识就是力量”。",
    },
    "奇械师": {
        "设计质量": "A：注法、工具、半施法和制造规则构成独特队伍位置。",
        "主题": "A：魔法工程师、炼金师、附魔工匠和战场技师主题清楚。",
        "能力设计质量": "A：强度依赖战役是否重视制作和魔法物品；在普通地城战里不如满施法者直接。",
        "主题与能力关联度": "A：工具施法、注法和专精都紧扣“把魔法做成东西”。",
    },
    "灵能使": {
        "设计质量": "B：UA 二期已经比旧 Mystic 更克制，但仍有“像法师换皮”与“灵能骰外挂”的双重风险。",
        "主题": "A：精神力、心灵、念动、空间折叠和身体异变主题明确。",
        "能力设计质量": "B：Psionic Energy Die 提供身份感；需要更多公开实桌验证资源曲线是否过强或过窄。",
        "主题与能力关联度": "A：核心能力和子职都直接围绕心灵力量展开。",
    },
}

RANK_NUM = {"F": 0, "E-": 0.5, "E": 1, "D": 2, "C": 3, "B": 4, "A": 5, "S": 6, "S+": 7}


def avg_rank(vals):
    return sum(RANK_NUM.get(v, 0) for v in vals) / len(vals)


def aspect_summary(scores):
    strong = sorted(scores.items(), key=lambda kv: avg_rank(kv[1]), reverse=True)
    top = [k for k, v in strong if avg_rank(v) >= 5][:4]
    good = [k for k, v in strong if 4 <= avg_rank(v) < 5][:4]
    weak = [k for k, v in strong if avg_rank(v) <= 2][:5]
    dead = [k for k, v in strong if all(x == "F" for x in v)]
    swing = [k for k, v in strong if max(RANK_NUM.get(x, 0) for x in v) - min(RANK_NUM.get(x, 0) for x in v) >= 2.5]
    return top, good, weak, dead, swing


def format_list(items):
    return "、".join(items) if items else "无明显项目"


def tier_curve(overall):
    if overall[0] == overall[-1]:
        return f"综合强度基本稳定在 {overall[0]}，不是靠等级爆点翻身，而是靠同一套队伍职责持续工作。"
    if RANK_NUM.get(overall[-1], 0) > RANK_NUM.get(overall[0], 0):
        return f"综合强度从 {overall[0]} 走到 {overall[-1]}，说明它越到高等级越依赖法术、资源升级或队伍级工具取得优势。"
    return f"综合强度从 {overall[0]} 滑到 {overall[-1]}，不是角色绝对变弱，而是同 Tier 中控制、反制、召唤、位移和高环法术的权重上升。"


def class_review(name, data):
    top, good, weak, dead, swing = aspect_summary(data["scores"])
    strengths = (top + [x for x in good if x not in top])[:6]
    strength_line = (
        f"从功能分项看，它最值得围绕的维度是 {format_list(strengths)}；这些项目决定它在队伍中的真实位置，而不是文件名或主题口号。"
        if strengths else
        "从功能分项看，它没有真正值得围绕的强项；这通常意味着该子职只在风味、怀旧或特定战役条件下成立，不能作为优化队伍的核心答案。"
    )
    weak_line = (
        f"它的明显短板是 {format_list(weak)}。这些短板解释了为什么该职业即使有高分项目，也不一定能在所有 Tier 保持 S：队伍功能越复杂，单一输出或单一防御越难覆盖全部问题。"
        if weak else
        "它没有低到 D/E 的硬短板；真正限制来自功能上限，而不是某个分项完全崩盘。换言之，它能填很多格子，但未必能在高等级压过满施法者的战役级工具。"
    )
    lines = [
        f"{name} 的核心价值集中在 {format_list(strengths)}。这不是抽象印象，而是来自四个 Tier 分项评分：这些项目在同级比较里长期保持 B/A 以上，能稳定成为队伍计划的一部分。",
        weak_line,
    ]
    if dead:
        lines.append(f"其中 {format_list(dead)} 属于规则层面基本不能承担的功能，不能靠“玩家操作好”自然补齐，只能靠专长、魔法物品、队友法术或多职业解决。")
    lines += [
        f"{tier_curve(data['overall'])} 评分时我没有把所有分项机械平均；反制施法者、团队增益、战场分隔、召唤 / 伙伴、治疗和临时生命在高等级的权重更高，因为这些维度更直接决定队伍能否处理复杂遭遇。",
    ]
    lines.append(
        f"需要重点复核的波动项是 {format_list(swing)}。这些项目通常受子职、魔法物品、Origin feats、法术表、DM 对休息/召唤/制作的管理方式影响最大。"
        if swing else
        "它的分项没有明显跨 Tier 大跳变；校准重点应放在子职、魔法物品、Origin feats、休息频率和 DM 对制作/召唤/隐藏的管理方式。"
    )
    return "\n".join(lines)


def subclass_review(cls, name, note, overall, scores):
    top, good, weak, dead, swing = aspect_summary(scores)
    strengths = (top + [x for x in good if x not in top])[:6]
    strength_line = (
        f"从功能分项看，它最值得围绕的维度是 {format_list(strengths)}；这些项目决定它在队伍中的真实位置，而不是文件名或主题口号。"
        if strengths else
        "从功能分项看，它没有真正值得围绕的强项；这通常意味着该子职只在风味、怀旧或特定战役条件下成立，不能作为优化队伍的核心答案。"
    )
    weak_line = (
        f"它不擅长 {format_list(weak)}。这些项目是实际组队时要提前补位的地方，不能只看子职主题就默认它能承担。"
        if weak else
        "它没有低到 D/E 的硬短板；评价重点转向它是否在关键强项上足够突出，能否比同职业其他子职更值得占用子职位置。"
    )
    lines = [
        f"{name} 相对 {cls} 基础职业的实际调整是：{note}",
        strength_line,
        weak_line,
    ]
    if dead:
        lines.append(f"其中 {format_list(dead)} 没有稳定规则入口，除非通过多职业、专长、魔法物品或队友支援绕开。")
    lines += [
        f"{tier_curve(overall)} 如果综合分没有因为某个高分项目继续上升，原因通常是该子职只改善了单一输出/防御，没补上高等级更值钱的控制、反制、召唤、团队增益或战役级工具。",
    ]
    lines.append(
        f"最容易因战役环境而改变的项目是 {format_list(swing)}；这些应在实桌中按敌人类型、地形、休息频率和可用法术/物品再校准。"
        if swing else
        "它的分项随 Tier 波动不大；实桌复核重点应放在敌人类型、地形、休息频率和可用法术/物品，而不是期待某一级突然翻盘。"
    )
    return "\n".join(lines)


def build_scores(name):
    scores = {
        "近战伤害者": ["A", "A", "A", "B"], "远程伤害者": ["B", "A", "A", "A"], "法术伤害者": ["C", "B", "A", "A"],
        "防御和生存": ["A", "A", "A", "A"], "治疗和临时生命": ["C", "B", "B", "B"], "团队增益": ["B", "A", "A", "A"],
        "反制施法者": ["D", "B", "A", "A"], "减益": ["C", "B", "A", "A"], "战场分隔": ["C", "B", "A", "A"],
        "召唤 / 伙伴": ["F", "C", "B", "B"], "技能使用": ["C", "C", "C", "C"], "制造": ["E", "E", "E", "E"],
    }
    if "诡术师游荡者" in name:
        scores["技能使用"] = ["S", "S", "S", "S"]
        scores["法术伤害者"] = ["E", "C", "B", "B"]
        scores["反制施法者"] = ["F", "C", "B", "A"]
        scores["减益"] = ["D", "B", "A", "A"]
        scores["战场分隔"] = ["D", "B", "A", "A"]
        scores["防御和生存"] = ["B", "B", "B", "B"]
        scores["近战伤害者"] = ["C", "C", "C", "C"]
        scores["远程伤害者"] = ["B", "B", "B", "B"]
        return scores
    if "奇械师" in name:
        scores["制造"] = ["S", "S", "S", "S"]
    if "游荡者" in name:
        scores["技能使用"] = ["S", "S", "S", "S"]
        scores["法术伤害者"] = ["E", "C", "B", "B"]
    if "法师" in name:
        scores["反制施法者"] = ["D", "S", "S", "S+"]
        scores["战场分隔"] = ["A", "S", "S", "S+"]
        scores["减益"] = ["A", "S", "S", "S+"]
    if "武僧 / 游侠" in name:
        scores["近战伤害者"] = ["A", "A", "B", "B"]
        scores["远程伤害者"] = ["B", "B", "B", "C"]
        scores["技能使用"] = ["A", "A", "A", "A"]
    return scores


def build_overall(name):
    if "诡术师游荡者" in name:
        return ["B", "B", "A", "A"]
    return base_build_overall(name)


def build_review(name, desc, overall, scores):
    top, good, weak, dead, swing = aspect_summary(scores)
    strengths = (top + [x for x in good if x not in top])[:6]
    weak_line = (
        f"明显代价是 {format_list(weak)}。这些是构筑核心通常不会解决的维度，需要队友、物品或战役资源补位。"
        if weak else
        "它没有低到 D/E 的硬短板；真正代价通常不是功能缺失，而是关键等级延迟和属性/专长压力。"
    )
    lines = [
        f"这个构筑的目的不是“多职业一定更强”，而是用具体前置补齐主职业短板：{desc}",
        f"实际强项是 {format_list(strengths)}。如果这些强项没有在你的战役中频繁出现，这个构筑就不值得为了它延迟主职业等级。",
        weak_line,
    ]
    if dead:
        lines.append(f"其中 {format_list(dead)} 几乎没有规则入口，不能因为多职业标签就自动视为可用。")
    lines += [
        f"{tier_curve(overall)} 低等级构筑尤其要小心：延迟 Extra Attack、3 环法术、Aura of Protection、ASI 或关键子职能力，往往比纸面终局收益更伤。",
    ]
    lines.append(
        f"环境敏感项：{format_list(swing)}。这些受起始等级、休息频率、魔法物品、专长可用性和 DM 对新版兼职措辞的解释影响最大。"
        if swing else
        "它的分项没有明显跨 Tier 大跳变；真正敏感的是起始等级、关键能力延迟、属性压力、专长可用性和 DM 对新版兼职措辞的解释。"
    )
    return "\n".join(lines)


def base_scores(cls):
    return {k: list(v) for k, v in CLASSES[cls]["scores"].items()}


def with_focus(cls, focus):
    scores = base_scores(cls)
    scores.update(focus)
    return scores


EXTRA_CLASSES = {
    "灵能使": {
        "en": "Psion（UA）",
        "overall": ["B", "A", "A", "A"],
        "design": ["B", "A", "B", "A"],
        "team": "UA 灵能满施法/特殊施法者，队伍位置介于术士、法师和心灵主题专家之间。二期文本比 2017 Mystic 克制得多，但仍需要实桌验证它的灵能骰、专属法术和子职叠加是否会在 Tier 2 后过强。",
        "scores": {
            "近战伤害者": ["F", "E", "D", "D"], "远程伤害者": ["D", "C", "C", "C"], "法术伤害者": ["B", "A", "A", "A"],
            "防御和生存": ["C", "B", "B", "B"], "治疗和临时生命": ["E", "D", "D", "D"], "团队增益": ["C", "B", "A", "A"],
            "反制施法者": ["D", "B", "A", "A"], "减益": ["A", "A", "A", "A"], "战场分隔": ["B", "A", "A", "A"],
            "召唤 / 伙伴": ["F", "E", "D", "D"], "技能使用": ["B", "B", "B", "B"], "制造": ["E", "E", "E", "E"],
        },
        "subs": {},
    }
}


EXTRA_SUBS = [
    # Forgotten Realms: Heroes of Faerun
    ("吟游诗人", "皓月学院", "College of the Moon", "FRHoF", "月相/幻光/情绪支援主题，核心价值在控制、增益和社交氛围；不如逸闻学院泛用，但更有设定味。", ["A", "A", "S", "S"], ["A", "A", "A", "A"], {"团队增益": ["A", "A", "S", "S"], "减益": ["A", "A", "S", "S"]}),
    ("圣武士", "巨灵贵族之誓", "Oath of the Noble Genies", "FRHoF", "元素抗性、机动和异界贵族主题很强；强度看元素法术和坐骑/飞行资源是否能充分展开。", ["A", "A", "A", "A"], ["A", "A", "A", "A"], {"法术伤害者": ["D", "C", "C", "C"], "防御和生存": ["A", "A", "A", "A"]}),
    ("战士", "旗将", "Banneret / Purple Dragon Knight", "FRHoF", "旧紫龙骑士长期被认为过弱，新版若给出真实团队指挥动作经济才有价值；评价保守给中上。", ["B", "B", "B", "B"], ["B", "A", "B", "A"], {"团队增益": ["C", "B", "B", "B"], "治疗和临时生命": ["D", "C", "C", "C"]}),
    ("术士", "咒火术法", "Spellfire Sorcery", "FRHoF", "围绕吸收/释放魔法能量，主题极强；若和 Counterspell、Circle Magic、吸能类机制叠加，反施法和爆发上限会很高。", ["A", "S", "S", "S"], ["A", "A", "A", "A"], {"法术伤害者": ["A", "S", "S", "S"], "反制施法者": ["C", "A", "S", "S"]}),
    ("法师", "剑咏者", "Bladesinger", "FRHoF / SCAG update", "旧版已经是高上限法师，新版放进 2024 法师底盘后仍强；不是最优控制法师，但防御、机动和近战表演性极好。", ["A", "S", "S", "S+"], ["A", "A", "A", "A"], {"近战伤害者": ["C", "B", "B", "B"], "防御和生存": ["B", "A", "A", "A"]}),
    ("游侠", "凛冬行者", "Winter Walker", "FRHoF", "寒冷、减速、地形压迫主题；强度取决于敌人抗性和地形，控制面优于纯 DPR。", ["B", "B", "B", "C"], ["B", "A", "B", "A"], {"减益": ["B", "B", "A", "A"], "战场分隔": ["B", "B", "A", "A"]}),
    ("游荡者", "三神门徒", "Scion of the Three", "FRHoF", "把游荡者拉向宗教/神秘刺客，工具面好于纯刺客；仍受游荡者基础战斗上限限制。", ["B", "C", "C", "C"], ["A", "A", "A", "A"], {"减益": ["C", "B", "B", "B"], "技能使用": ["S", "S", "S", "S"]}),
    ("牧师", "知识领域", "Knowledge Domain", "FRHoF / PHB legacy", "知识、技能和信息法术让牧师更像神术调查员；战斗不如光明/生命尖锐，但解题面很好。", ["S", "S", "S", "S"], ["A", "A", "A", "A"], {"技能使用": ["A", "A", "A", "A"], "团队增益": ["A", "A", "S", "S"]}),

    # UA 2025+ overwrites and new tests
    ("战士", "魔射手（UA二期）", "Arcane Archer UA II", "UA Arcane Subclasses II", "旧魔射手最大问题是资源太少、箭术效果不够改变战局；UA 二期若改善次数和 DC，才配得上战士远程控制子职。", ["B", "B", "B", "B"], ["B", "A", "B", "A"], {"远程伤害者": ["A", "A", "A", "A"], "减益": ["C", "B", "B", "B"]}),
    ("武僧", "纹身武者（UA二期）", "Tattooed Warrior UA II", "UA Arcane Subclasses II", "用魔法纹身给武僧增加元素/防御/工具，主题新鲜；风险是变成一组离散小法术而不是武僧玩法。", ["A", "A", "A", "B"], ["B", "A", "B", "A"], {"法术伤害者": ["E", "D", "D", "D"], "团队增益": ["D", "C", "C", "C"]}),
    ("法师", "咒法师（UA二期）", "Conjurer UA II", "UA Arcane Subclasses II", "如果保留更顺的召唤与传送能力，就是高等级最危险的学派之一；召唤规则管理仍是设计负担。", ["A", "S", "S", "S+"], ["A", "A", "A", "A"], {"召唤 / 伙伴": ["D", "S", "S", "S"], "战场分隔": ["A", "S", "S", "S+"]}),
    ("法师", "惑控师（UA二期）", "Enchanter UA II", "UA Arcane Subclasses II", "心智控制在能生效时极强，但免疫、传奇抗力和社交边界让它比防护/预言更不稳定。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"减益": ["A", "S", "S", "S"], "团队增益": ["B", "A", "A", "A"]}),
    ("法师", "死灵师（UA二期）", "Necromancer UA II", "UA Arcane Subclasses II", "亡灵召唤和吸命主题强，桌面负担也高；优化上限看新版召唤是否被压住。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"召唤 / 伙伴": ["F", "A", "S", "S"], "治疗和临时生命": ["E", "D", "C", "C"]}),
    ("法师", "变化师（UA二期）", "Transmuter UA II", "UA Arcane Subclasses II", "主题经典但历史上机制常偏杂；若新版把防御、变形和材料转化整合好，才从中游上升。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"防御和生存": ["C", "B", "A", "A"], "制造": ["C", "B", "B", "B"]}),
    ("牧师", "奥秘领域（UA）", "Arcana Domain UA", "UA Arcane Subclasses", "奥术神职补 Counterspell/Bigby's Hand 等更实用法术后价值上升，是反施法和工具牧师。", ["S", "S", "S", "S"], ["A", "A", "A", "A"], {"反制施法者": ["D", "A", "S", "S"], "法术伤害者": ["A", "A", "A", "A"]}),
    ("术士", "先祖术法（UA）", "Ancestral Sorcery UA", "UA Arcane Subclasses", "主题像血脉记忆/祖灵奥术，功能偏防御和额外工具；公开样本少，保守给强但非顶级。", ["A", "A", "S", "S"], ["B", "A", "B", "A"], {"团队增益": ["C", "B", "A", "A"]}),
    ("魔契师", "咒剑宗主（UA）", "Hexblade Patron UA", "UA Horror/Arcane", "历史上 Hexblade 因魅力武器前置和防御过强塑造了整个优化生态；新版若削弱前置价值仍会很强。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "A", "A", "A"], "防御和生存": ["B", "A", "A", "A"]}),
    ("奇械师", "苏生师（UA）", "Reanimator UA", "UA Horror Subclasses", "亡灵科学家/尸体工匠主题强，召唤与治疗/强化生物结合；平衡风险在伙伴耐久和动作经济。", ["B", "A", "A", "B"], ["B", "A", "B", "A"], {"召唤 / 伙伴": ["C", "A", "A", "A"], "治疗和临时生命": ["C", "B", "B", "B"]}),
    ("游侠", "幽邃戍卫（UA）", "Hollow Warden UA", "UA Horror Subclasses", "恐怖林地守卫，能把游侠从标记猎物转向变身/压迫前排；强度看变身资源和控制 DC。", ["A", "A", "B", "B"], ["A", "A", "A", "A"], {"近战伤害者": ["A", "A", "B", "B"], "防御和生存": ["B", "A", "A", "A"]}),
    ("游荡者", "鬼魅（UA）", "Phantom UA", "UA Horror Subclasses", "旧 Phantom 中高等级灵魂资源很强但前期慢；UA 若提前核心循环会明显改善。", ["B", "C", "C", "C"], ["B", "A", "B", "A"], {"法术伤害者": ["F", "E", "E", "E"], "减益": ["D", "C", "B", "B"]}),
    ("吟游诗人", "精魂学院（UA）", "College of Spirits UA", "UA Horror Subclasses", "随机故事/招魂主题强，问题一直是随机性和动作经济；氛围好，优化稳定性一般。", ["A", "A", "A", "S"], ["B", "A", "B", "A"], {"团队增益": ["A", "A", "A", "S"], "减益": ["A", "A", "A", "A"]}),
    ("牧师", "坟墓领域（UA）", "Grave Domain UA", "UA Horror Subclasses", "救濒死、反亡灵、制造易伤窗口都很实用；不如暮光/和平离谱，但设计比旧版更顺。", ["S", "S", "S", "S"], ["A", "A", "A", "A"], {"治疗和临时生命": ["S", "S", "S", "S"], "减益": ["A", "A", "A", "A"]}),
    ("术士", "幽影术法（UA）", "Shadow Sorcery UA", "UA Horror Subclasses", "暗影生存、黑暗视域和控制主题明确；比时械/畸变少额外法术压制力。", ["A", "A", "S", "S"], ["A", "A", "A", "A"], {"防御和生存": ["C", "B", "A", "A"], "减益": ["A", "A", "S", "S"]}),
    ("魔契师", "死灵宗主（UA）", "Undead Patron UA", "UA Horror Subclasses", "恐惧、临时生命、坏死输出都直接有效，是比不朽者更成功的亡灵宗主。", ["A", "A", "A", "A"], ["A", "A", "A", "A"], {"减益": ["A", "A", "A", "A"], "防御和生存": ["B", "A", "A", "A"]}),
    ("野蛮人", "精魂守卫道途（UA）", "Ancestral Guardian UA update", "UA XGE update", "保护队友的野蛮人，能强迫敌人处理你而不是后排；输出不顶尖但队伍价值高。", ["A", "A", "B", "B"], ["A", "A", "A", "A"], {"团队增益": ["C", "B", "B", "B"], "减益": ["C", "B", "B", "B"]}),
    ("野蛮人", "风暴先驱道途（UA）", "Storm Herald UA update", "UA XGE update", "旧版最大问题是光环数值太小；UA 若提升环境选择和可切换性，才接近可用。", ["B", "B", "C", "C"], ["C", "A", "C", "A"], {"法术伤害者": ["F", "F", "F", "F"], "团队增益": ["D", "C", "C", "C"]}),
    ("武僧", "醉拳僧（UA）", "Drunken Master UA update", "UA XGE update", "机动、脱离和误导主题好；强度取决于是否真正增加控制，而不只是移动得更花。", ["A", "A", "B", "B"], ["B", "A", "B", "A"], {"防御和生存": ["B", "A", "A", "A"], "技能使用": ["C", "B", "B", "B"]}),
    ("圣武士", "破誓者（UA）", "Oathbreaker UA update", "UA XGE update", "反英雄/亡灵指挥主题非常强；桌面许可问题比强度问题更大。若允许，输出和光环都危险。", ["A", "A", "A", "A"], ["A", "A", "A", "A"], {"召唤 / 伙伴": ["F", "B", "A", "A"], "减益": ["D", "B", "B", "B"]}),
    ("战士", "晓骑士（UA）", "Cavalier / Dawn Knight UA update", "UA XGE update", "骑乘/守护路线若不能稳定骑乘就缩水；若新版补站位保护，才是合格防线战士。", ["B", "B", "B", "B"], ["B", "A", "B", "A"], {"防御和生存": ["A", "A", "A", "A"], "团队增益": ["D", "C", "C", "C"]}),
    ("术士", "亵渎术法（UA）", "Defiled Sorcery UA", "UA Havoc Subclasses", "灾厄/污染奥术主题，通常会给伤害和减益；公开样本少，按强术士底盘给高但保守。", ["A", "A", "S", "S"], ["B", "A", "B", "A"], {"法术伤害者": ["A", "S", "S", "S"], "减益": ["A", "A", "S", "S"]}),
    ("魔契师", "巫王宗主（UA）", "Witch King Patron UA", "UA Havoc Subclasses", "支配、恐惧、诅咒和亡灵权威主题强；若给召唤或群控，Tier 2 后很好用。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"减益": ["B", "A", "A", "A"], "召唤 / 伙伴": ["D", "B", "B", "B"]}),
    ("德鲁伊", "疗愈结社（UA）", "Circle of Healing UA", "UA Havoc Subclasses", "治疗德鲁伊的队伍容错极高，但若只增加治疗数字，优化胜率不会超过控制/召唤德鲁伊。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"治疗和临时生命": ["S", "S", "S", "S"], "团队增益": ["A", "A", "A", "A"]}),
    ("战士", "角斗士（UA）", "Gladiator UA", "UA Havoc Subclasses", "竞技场控制、嘲讽和表演性近战；若没有真实控制，只会是勇士的花哨版本。", ["A", "A", "B", "B"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "A", "A", "A"], "减益": ["C", "C", "C", "C"]}),
    ("圣武士", "护法之誓（UA）", "Oath of Guardianship UA", "UA Mystic Subclasses", "护卫型誓言，能进一步放大圣武士最强的保护定位；伤害不如复仇，但队伍价值稳定。", ["A", "S", "A", "A"], ["A", "A", "A", "A"], {"团队增益": ["A", "S", "S", "A"], "防御和生存": ["A", "S", "S", "A"]}),
    ("武僧", "秘术武者（UA）", "Arcane Warrior Monk UA", "UA Mystic Subclasses", "给武僧法术感工具，但风险是资源挤占武僧原本优秀动作经济。", ["A", "A", "B", "B"], ["B", "A", "B", "A"], {"法术伤害者": ["E", "D", "C", "C"], "反制施法者": ["D", "C", "B", "B"]}),
    ("游荡者", "窃法者（UA）", "Spell Thief Rogue UA", "UA Mystic Subclasses", "如果能稳定偷取/干扰法术，是少数让游荡者拥有反施法身份的子职；仍受偷袭上限拖累。", ["B", "B", "B", "B"], ["A", "A", "A", "A"], {"反制施法者": ["D", "B", "A", "A"], "技能使用": ["S", "S", "S", "S"]}),
    ("魔契师", "契灵宗主（UA）", "Pact Spirit Patron UA", "UA Mystic Subclasses", "宗主变成契约灵体/守护灵，主题有趣；强度看是否提供稳定召唤、治疗或防御。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"召唤 / 伙伴": ["D", "B", "B", "B"], "治疗和临时生命": ["D", "C", "C", "C"]}),

    # Official 2014-era options not cleanly overwritten
    ("野蛮人", "野兽道途", "Path of the Beast", "TCE", "自然武器和变形战斗让野蛮人有更多形态选择；在 2024 Weapon Mastery 环境下要小心自然武器是否吃不到装备红利。", ["A", "B", "C", "C"], ["A", "A", "A", "A"], {"近战伤害者": ["A", "A", "B", "B"]}),
    ("野蛮人", "狂野魔法道途", "Path of Wild Magic", "TCE", "随机效果主题好，实际优化评价偏保守；可玩性大于稳定强度。", ["B", "B", "C", "C"], ["B", "A", "B", "A"], {"团队增益": ["D", "C", "C", "C"]}),
    ("野蛮人", "战狂", "Battlerager", "SCAG", "铠刺主题窄、装备锁定严重、数值老旧；在 2024 环境几乎只剩怀旧价值。", ["C", "D", "E", "E"], ["D", "B", "D", "C"], {"近战伤害者": ["B", "C", "D", "D"], "防御和生存": ["B", "B", "C", "C"]}),
    ("野蛮人", "图腾武者道途（旧版）", "Totem Warrior legacy", "PHB/SCAG legacy", "旧熊图腾防御仍出名，但新版野蛮人已有新子职覆盖多数用途；保留给旧规则桌。", ["A", "A", "B", "B"], ["A", "A", "A", "A"], {"防御和生存": ["S", "S", "A", "A"]}),
    ("吟游诗人", "迷惑学院", "College of Glamour", "XGE", "群体移动和魅惑支援很有团队价值，社交主题强；遇到免疫魅惑的敌人会掉价。", ["A", "A", "A", "S"], ["A", "A", "A", "A"], {"团队增益": ["A", "S", "S", "S"]}),
    ("吟游诗人", "剑舞学院", "College of Swords", "XGE", "给吟游诗人近战玩法，但真正强度仍来自满施法；若想武器吟游诗人，2024 勇气/舞蹈常更顺。", ["A", "A", "A", "S"], ["B", "A", "B", "A"], {"近战伤害者": ["C", "B", "B", "B"], "防御和生存": ["C", "B", "B", "B"]}),
    ("吟游诗人", "低语学院", "College of Whispers", "XGE", "恐吓、伪装、精神伤害很有剧情味，战斗贡献比其他学院窄。", ["B", "B", "A", "A"], ["B", "A", "B", "A"], {"减益": ["A", "A", "A", "A"], "技能使用": ["S", "S", "S", "S"]}),
    ("吟游诗人", "创造学院", "College of Creation", "TCE", "创造物品和动画伙伴给吟游诗人补上制造/召唤维度，强度和创意上限都高。", ["A", "S", "S", "S"], ["S", "A", "S", "A"], {"制造": ["A", "A", "A", "A"], "召唤 / 伙伴": ["D", "A", "A", "A"]}),
    ("牧师", "锻造领域", "Forge Domain", "XGE", "重甲、制造和火焰主题强，低中等级非常硬；高等级仍靠牧师法表。", ["S", "S", "S", "S"], ["A", "A", "A", "A"], {"制造": ["A", "A", "A", "A"], "防御和生存": ["S", "S", "S", "S"]}),
    ("牧师", "秩序领域", "Order Domain", "TCE/Ravnica", "让队友用反应攻击的动作经济极强，是典型优化牧师前置候选。", ["S", "S", "S", "S"], ["A", "A", "A", "A"], {"团队增益": ["S", "S", "S", "S"]}),
    ("牧师", "和平领域", "Peace Domain", "TCE", "社区公认的过强领域之一，Emboldening Bond 破坏 bounded accuracy 体验。", ["S+", "S+", "S+", "S+"], ["C", "B", "D", "B"], {"团队增益": ["S+", "S+", "S+", "S+"], "防御和生存": ["S", "S", "S", "S"]}),
    ("牧师", "暮光领域", "Twilight Domain", "TCE", "低中等级临时生命光环过强，极大压低遭遇威胁；强度高但设计不健康。", ["S+", "S+", "S", "S"], ["C", "A", "D", "A"], {"治疗和临时生命": ["S+", "S+", "S", "S"], "防御和生存": ["S", "S", "S", "S"]}),
    ("德鲁伊", "梦境结社", "Circle of Dreams", "XGE", "治疗和机动温和实用，但相比星辰/牧人/大地缺少决定战局的尖点。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"治疗和临时生命": ["A", "A", "A", "A"]}),
    ("德鲁伊", "牧人结社", "Circle of the Shepherd", "XGE", "旧版召唤德鲁伊顶级代表，强但拖慢桌面；若使用 2024 召唤规则需重估。", ["A", "S", "S", "S"], ["C", "A", "C", "A"], {"召唤 / 伙伴": ["D", "S+", "S+", "S"], "团队增益": ["A", "A", "A", "A"]}),
    ("德鲁伊", "孢子结社", "Circle of Spores", "Ravnica/TCE", "想做近战菌类德鲁伊，但动作经济和临时生命掉落让近战计划不稳。", ["B", "A", "A", "A"], ["B", "A", "C", "A"], {"近战伤害者": ["C", "B", "B", "C"], "防御和生存": ["B", "B", "B", "B"]}),
    ("德鲁伊", "野火结社", "Circle of Wildfire", "TCE", "治疗、位移和范围火焰很好，伙伴动作经济让它比表面更强。", ["A", "S", "S", "S"], ["A", "A", "A", "A"], {"召唤 / 伙伴": ["C", "A", "A", "A"], "治疗和临时生命": ["B", "A", "A", "A"]}),
    ("战士", "骑兵", "Cavalier", "XGE", "防线和骑乘主题明确，但很多战役不稳定支持骑乘；站桩保护还可以。", ["B", "B", "B", "B"], ["B", "A", "B", "A"], {"防御和生存": ["A", "A", "A", "A"]}),
    ("战士", "武士", "Samurai", "XGE", "简单可靠的优势/临时生命爆发，配远程或重武器都行；工具面窄。", ["A", "A", "B", "B"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "A", "A", "A"], "远程伤害者": ["A", "A", "A", "A"]}),
    ("战士", "符文骑士", "Rune Knight", "TCE", "优秀的被动/主动符文、体型、控制和技能加成，旧版战士最强子职竞争者。", ["A", "A", "A", "A"], ["S", "A", "S", "A"], {"减益": ["C", "B", "A", "A"], "技能使用": ["B", "B", "B", "B"]}),
    ("战士", "回音骑士", "Echo Knight", "EGW", "回音提供攻击、位移、威胁范围和规避，强到经常触发规则边界讨论。", ["A", "S", "A", "A"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "S", "A", "A"], "战场分隔": ["B", "A", "A", "A"]}),
    ("武僧", "剑圣宗", "Kensei", "XGE", "武器武僧主题自然，但 2024 武僧底盘和精通系统让旧剑圣优势缩水。", ["B", "B", "B", "C"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "A", "B", "B"], "远程伤害者": ["C", "B", "B", "B"]}),
    ("武僧", "日魂宗", "Sun Soul", "XGE/SCAG", "远程气功幻想很清楚，数值长期偏低，资源换伤害不划算。", ["C", "C", "C", "D"], ["C", "A", "C", "A"], {"远程伤害者": ["C", "C", "C", "C"], "法术伤害者": ["E", "E", "E", "E"]}),
    ("武僧", "永亡宗", "Long Death", "SCAG", "恐惧和临时生命很适合黑暗武僧，强度中等，设计比数值更有味。", ["B", "B", "B", "B"], ["B", "A", "B", "A"], {"防御和生存": ["B", "A", "A", "A"], "减益": ["C", "B", "B", "B"]}),
    ("武僧", "星界我宗", "Astral Self", "TCE", "想把武僧变成感知 SAD 和长臂控制，但资源消耗与收益长期被认为一般。", ["B", "B", "B", "C"], ["B", "A", "B", "A"], {"近战伤害者": ["B", "B", "B", "C"]}),
    ("武僧", "神龙宗", "Ascendant Dragon", "Fizban", "元素吐息和龙翼主题强，实际数值偏温和；适合风味，不是优化最强。", ["B", "B", "B", "C"], ["B", "A", "B", "A"], {"法术伤害者": ["E", "D", "D", "D"], "战场分隔": ["C", "C", "C", "C"]}),
    ("圣武士", "征服之誓", "Oath of Conquest", "XGE", "恐惧锁场与光环结合很强，是最控制向的圣武士之一。", ["A", "S", "A", "A"], ["A", "A", "A", "A"], {"减益": ["B", "A", "A", "A"], "战场分隔": ["C", "A", "A", "A"]}),
    ("圣武士", "救赎之誓", "Oath of Redemption", "XGE", "防御与和平主题强，机制能保护队友但和杀敌效率有张力。", ["B", "A", "A", "A"], ["A", "A", "A", "A"], {"团队增益": ["B", "S", "S", "A"], "防御和生存": ["A", "S", "S", "A"]}),
    ("圣武士", "王冠之誓", "Oath of the Crown", "SCAG", "守护与牵制主题清楚，法术/能力不如征服或守望尖锐。", ["B", "A", "A", "A"], ["B", "A", "B", "A"], {"团队增益": ["B", "A", "A", "A"]}),
    ("圣武士", "守望者之誓", "Oath of the Watchers", "TCE", "反异界、先攻光环和反施法倾向非常适合优化桌。", ["A", "S", "A", "A"], ["A", "A", "A", "A"], {"反制施法者": ["D", "B", "A", "A"], "团队增益": ["B", "S", "S", "A"]}),
    ("游侠", "边界行者", "Horizon Walker", "XGE", "位面主题和传送感强，伤害启动慢；高等级机动不错但不改游侠根本问题。", ["B", "B", "B", "C"], ["B", "A", "B", "A"], {"战场分隔": ["C", "B", "B", "B"]}),
    ("游侠", "怪物杀手", "Monster Slayer", "XGE", "反单体、反施法主题明确；但标记类动作经济和数值偏保守。", ["B", "B", "C", "C"], ["B", "A", "B", "A"], {"反制施法者": ["D", "C", "B", "B"]}),
    ("游侠", "龙兽守卫", "Drakewarden", "Fizban", "伙伴随等级成长、主题好，真实桌面比旧 Beast Master 稳。", ["A", "A", "B", "B"], ["A", "A", "A", "A"], {"召唤 / 伙伴": ["C", "A", "A", "A"]}),
    ("游侠", "群集守护者", "Swarmkeeper", "TCE", "推拉、移动和额外效果让游侠更像控制者，是设计较好的旧版游侠子职。", ["A", "A", "B", "B"], ["A", "A", "A", "A"], {"减益": ["B", "B", "A", "A"], "战场分隔": ["B", "B", "A", "A"]}),
    ("游荡者", "风流剑客", "Swashbuckler", "SCAG/XGE", "让游荡者单挑和移动更顺，是最受欢迎旧版游荡者之一；高等级仍缺资源。", ["B", "C", "C", "C"], ["A", "A", "A", "A"], {"近战伤害者": ["B", "C", "C", "C"], "技能使用": ["S", "S", "S", "S"]}),
    ("游荡者", "策士", "Mastermind", "SCAG/XGE", "队友 Help 玩法有主题，但战斗数值太弱；社交伪装不错。", ["C", "D", "D", "D"], ["C", "A", "C", "A"], {"团队增益": ["C", "C", "C", "C"], "技能使用": ["S", "S", "S", "S"]}),
    ("游荡者", "调查员", "Inquisitive", "XGE", "侦探主题强，Insightful Fighting 实战不如直接取得优势；偏剧情桌。", ["C", "C", "D", "D"], ["B", "A", "B", "A"], {"技能使用": ["S", "S", "S", "S"]}),
    ("游荡者", "斥候", "Scout", "XGE", "机动和自然技能很好，战斗只是更会保持距离的游荡者。", ["B", "C", "C", "C"], ["B", "A", "B", "A"], {"技能使用": ["S", "S", "S", "S"], "远程伤害者": ["B", "C", "C", "C"]}),
    ("术士", "神圣之魂", "Divine Soul", "XGE", "术士拿牧师法表是巨大扩展，治疗、增益和控制都上升；已知法术限制仍是成本。", ["A", "S", "S", "S"], ["A", "A", "A", "A"], {"治疗和临时生命": ["B", "A", "A", "A"], "团队增益": ["A", "A", "S", "S"]}),
    ("术士", "风暴术法", "Storm Sorcery", "SCAG/XGE", "主题酷但机制长期偏弱，近身风暴施法和脆皮术士天然冲突。", ["B", "A", "A", "A"], ["C", "A", "C", "A"], {"法术伤害者": ["A", "A", "A", "A"], "防御和生存": ["C", "C", "C", "C"]}),
    ("术士", "月之术法", "Lunar Sorcery", "Dragonlance", "额外法术和模式切换给术士大量灵活性，强度接近顶级旧版术士。", ["A", "S", "S", "S"], ["A", "A", "A", "A"], {"法术伤害者": ["A", "S", "S", "S"], "团队增益": ["C", "A", "A", "A"]}),
    ("魔契师", "巨灵宗主", "Genie Patron", "TCE", "飞行、额外伤害、容器、愿望主题和法术列表都优秀，是旧版魔契师顶级宗主。", ["A", "A", "A", "A"], ["S", "A", "S", "A"], {"法术伤害者": ["B", "A", "A", "A"], "防御和生存": ["B", "B", "A", "A"]}),
    ("魔契师", "深海意志", "Fathomless Patron", "TCE", "触手控制和海洋主题好，强度稳定但不如巨灵或咒剑改变生态。", ["A", "A", "A", "A"], ["A", "A", "A", "A"], {"减益": ["B", "A", "A", "A"], "战场分隔": ["B", "A", "A", "A"]}),
    ("魔契师", "不朽者", "Undying Patron", "SCAG", "社区长期公认弱宗主，能力窄且数值低；通常被死灵宗主取代。", ["C", "C", "C", "C"], ["D", "B", "D", "C"], {"防御和生存": ["C", "C", "C", "C"], "治疗和临时生命": ["D", "D", "D", "D"]}),
    ("法师", "战争魔法", "War Magic", "XGE", "反应防御和先攻强，优化价值高；主题比防护/塑能稍抽象但机制很好。", ["A", "S", "S", "S+"], ["A", "B", "A", "B"], {"防御和生存": ["B", "A", "A", "A"], "反制施法者": ["D", "S", "S", "S+"]}),
    ("法师", "抄写师", "Order of Scribes", "TCE", "法术书主题极强，换伤害类型和快速抄录有趣；强度来自法师底盘，子职本身偏工具。", ["A", "S", "S", "S"], ["A", "A", "B", "A"], {"制造": ["C", "C", "C", "C"], "法术伤害者": ["A", "S", "S", "S"]}),
    ("法师", "时间魔法", "Chronurgy Magic", "EGW", "社区公认极强甚至过强，先攻、重骰、行动封存都直接改写战斗。", ["A", "S+", "S+", "S+"], ["C", "A", "D", "A"], {"减益": ["A", "S+", "S+", "S+"], "团队增益": ["B", "S", "S", "S"]}),
    ("法师", "重力魔法", "Graviturgy Magic", "EGW", "控制、位移和地形操作主题好，强度不如时间但仍靠法师底盘很强。", ["A", "S", "S", "S+"], ["A", "A", "A", "A"], {"战场分隔": ["A", "S", "S", "S+"], "减益": ["A", "S", "S", "S"]}),

    # Plane Shift / third-party
    ("牧师", "力量领域", "Strength Domain", "Plane Shift: Amonkhet", "力量神职偏武器和体能，风味明确但机制像旧战争领域旁支。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"近战伤害者": ["B", "B", "B", "C"]}),
    ("牧师", "团结领域", "Solidarity Domain", "Plane Shift: Amonkhet", "团队保护和协作主题好，若叠加 2024 牧师底盘会很稳。", ["S", "S", "S", "S"], ["A", "A", "A", "A"], {"团队增益": ["A", "S", "S", "S"]}),
    ("牧师", "热忱领域", "Zeal Domain", "Plane Shift: Amonkhet", "爆发神术和武器伤害强，接近风暴/战争混合；有爆发滥用风险。", ["S", "S", "S", "S"], ["B", "A", "B", "A"], {"法术伤害者": ["A", "A", "A", "A"], "近战伤害者": ["B", "B", "B", "C"]}),
    ("牧师", "野心领域", "Ambition Domain", "Plane Shift: Amonkhet", "潜行、欺瞒和控制类神职，主题强但偏设定专用。", ["A", "A", "S", "S"], ["B", "A", "B", "A"], {"技能使用": ["A", "A", "A", "A"], "减益": ["A", "A", "A", "A"]}),
    ("术士", "烈焰术士", "Pyromancer", "Plane Shift: Kaladesh", "纯火焰术士，主题直接但抗性/免疫环境会让它掉价；如果没有绕抗性能力，强度不如术士顶级子职。", ["B", "A", "A", "A"], ["B", "A", "B", "A"], {"法术伤害者": ["A", "A", "A", "A"]}),
    ("野蛮人", "实验道途", "Path of the Experiment", "Grim Hollow / Crooked Moon", "身体改造恐怖野蛮人，通常强在变异和爆发；第三方数值需保守看待。", ["A", "B", "B", "C"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "A", "B", "B"], "防御和生存": ["A", "A", "B", "B"]}),
    ("吟游诗人", "灵哨学院", "College of the Spirit Whistle", "Crooked Moon", "民俗恐怖支援吟游，氛围强；若依赖恐惧/魅惑，免疫环境会限制它。", ["A", "A", "A", "S"], ["B", "A", "B", "A"], {"团队增益": ["A", "A", "A", "S"], "减益": ["A", "A", "A", "A"]}),
    ("圣武士", "惩戒之誓", "Oath of Penance", "Crooked Moon", "惩戒、负罪和反击主题，队伍位置类似复仇但更黑暗；保守给强。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"近战伤害者": ["A", "A", "A", "B"], "减益": ["D", "C", "C", "C"]}),
    ("德鲁伊", "柳艺结社", "Circle of Wicker", "Crooked Moon", "植物/编织/民俗仪式主题，通常偏召唤和控制；第三方资料缺社区样本，按德鲁伊底盘给高。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"召唤 / 伙伴": ["D", "A", "S", "S"], "战场分隔": ["A", "S", "S", "S"]}),
    ("德鲁伊", "旧途结社", "Circle of the Old Ways", "Crooked Moon", "古老自然和仪式主题，若偏治疗/控制则强；缺公开优化样本，保守。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"团队增益": ["B", "A", "A", "A"], "战场分隔": ["A", "S", "S", "S"]}),
    ("战士", "陵墓守卫", "Tomb Warden", "Crooked Moon", "守墓战士，防线和反亡灵主题强；没有法术时高 Tier 上限仍有限。", ["A", "A", "B", "B"], ["B", "A", "B", "A"], {"防御和生存": ["A", "A", "A", "A"], "减益": ["C", "C", "C", "C"]}),
    ("术士", "猩红术法", "Crimson Sorcery", "Crooked Moon", "血魔法术士，治疗/自伤/爆发可能很强也可能危险；按第三方保守评价。", ["A", "A", "S", "S"], ["B", "A", "B", "A"], {"法术伤害者": ["A", "S", "S", "S"], "治疗和临时生命": ["D", "C", "C", "C"]}),
    ("武僧", "疫障武者", "Plague Barrier Warrior", "Crooked Moon", "疾病/毒素/防护武僧，主题强但常受免疫毒/疾病影响。", ["B", "B", "B", "C"], ["B", "A", "B", "A"], {"减益": ["C", "B", "B", "B"], "防御和生存": ["B", "A", "A", "A"]}),
    ("法师", "神秘学者", "Occultist Wizard", "Crooked Moon", "民俗神秘学法师，仍是法师底盘；子职多半增加仪式、知识和诅咒。", ["A", "S", "S", "S+"], ["B", "A", "B", "A"], {"技能使用": ["B", "B", "B", "B"], "减益": ["A", "S", "S", "S"]}),
    ("法师", "贤者", "Sage Wizard", "Crooked Moon", "知识型法师，强度来自法表，子职若只加技能则不如防护/预言。", ["A", "S", "S", "S"], ["B", "A", "B", "A"], {"技能使用": ["A", "A", "A", "A"]}),
    ("游侠", "噩兆先驱", "Omen Harbinger", "Crooked Moon", "预兆/诅咒游侠，若能稳定给队友优势或敌人惩罚，比纯 DPR 游侠更有价值。", ["A", "A", "B", "B"], ["B", "A", "B", "A"], {"减益": ["B", "A", "A", "A"], "团队增益": ["C", "B", "B", "B"]}),
    ("游荡者", "罪人", "Sinner Rogue", "Crooked Moon", "罪业主题游荡者，偏社交/恐惧/惩罚；战斗仍受游荡者底盘限制。", ["B", "C", "C", "C"], ["B", "A", "B", "A"], {"技能使用": ["S", "S", "S", "S"], "减益": ["D", "C", "B", "B"]}),
    ("牧师", "丰收领域", "Harvest Domain", "Crooked Moon", "丰收神职可走治疗、腐败或资源循环；强度取决于是否给稳定临时生命/回复。", ["S", "S", "S", "S"], ["B", "A", "B", "A"], {"治疗和临时生命": ["S", "S", "S", "S"]}),
    ("魔契师", "愚神宗主", "Fool God Patron", "Crooked Moon", "荒诞神祇宗主，随机性或反转效果会影响稳定性；风味大于优化确定性。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"减益": ["B", "A", "A", "A"]}),
    ("魔契师", "角之王宗主", "Horned King Patron", "Crooked Moon", "民俗狩猎/野性宗主，适合近战或召唤魔契师；强度看是否补防御。", ["A", "A", "A", "A"], ["B", "A", "B", "A"], {"近战伤害者": ["B", "B", "B", "B"], "召唤 / 伙伴": ["D", "B", "B", "B"]}),
]


PSION_SUBS = [
    ("传心师", "Telepath", "心灵链接、读心、魅惑和精神控制路线，非伤害维度强；对免疫心灵/魅惑的敌人掉价。", ["B", "A", "A", "A"], ["A", "A", "A", "A"], {"团队增益": ["B", "A", "A", "A"], "减益": ["A", "A", "A", "A"]}),
    ("念动使", "Psykinetic", "念动力伤害、推拉、护盾和物体操控路线，战斗表现最直观。", ["B", "A", "A", "A"], ["B", "A", "B", "A"], {"法术伤害者": ["B", "A", "A", "A"], "战场分隔": ["B", "A", "A", "A"]}),
    ("蜕变者", "Metamorph", "身体变形路线，能补近战和防御；问题是如果要和武僧/野蛮人比近战，施法者动作经济会紧。", ["B", "A", "A", "A"], ["B", "A", "B", "A"], {"近战伤害者": ["C", "B", "B", "B"], "防御和生存": ["B", "B", "A", "A"]}),
    ("裂空者", "Psi Warper", "空间折叠和传送路线，机动、逃脱和战场重排强；直接伤害不是核心。", ["B", "A", "A", "A"], ["A", "A", "A", "A"], {"战场分隔": ["B", "A", "A", "A"], "防御和生存": ["C", "B", "B", "B"]}),
]


def design_table(name, design_scores, extra_note=None):
    notes = CLASS_DESIGN.get(name)
    if notes is None:
        notes = {
            "设计质量": f"{design_scores[0]}：{extra_note or '此项主要依据子职是否提供清晰的新玩法、是否改善基础职业短板。'}",
            "主题": f"{design_scores[1]}：主题是否鲜明、是否能从名称和能力直接读出角色幻想。",
            "能力设计质量": f"{design_scores[2]}：看动作经济、资源曲线、数值压力、规则边界和是否造成桌面负担。",
            "主题与能力关联度": f"{design_scores[3]}：看能力是否真的支撑主题，而不是只贴名字。",
        }
    rows = ["| 设计项 | 评分 | 具体理由 |", "|---|---|---|"]
    for idx, key in enumerate(["设计质量", "主题", "能力设计质量", "主题与能力关联度"]):
        rows.append(f"| {key} | {design_scores[idx]} | {notes[key]} |")
    return "\n".join(rows)


def source_design_context(source):
    if "UA" in source:
        return "UA 版本只按测试稿评价：允许概念分高，但规则稳定性和未来改写风险会压低设计质量。"
    if "Plane Shift" in source:
        return "Plane Shift 材料篇幅短、设计预算粗，主题可借设定成立，但机制完整度通常不能按正式扩展同权处理。"
    if "Crooked Moon" in source or "第三方" in source:
        return "第三方/合作材料先看能否接入 2024 底盘；如果要额外解释、额外管理或依赖 DM 放宽，能力设计会降分。"
    if "FRHoF" in source:
        return "FRHoF 属较新来源，评价重点是它是否顺着 2024 子职节奏给出独立玩法，而不是只补旧版怀旧功能。"
    if "2024" in source or "已生成基准" in source:
        return "2024 基准子职按新版职业节奏评价：3 级即应给出明确玩法入口，后续特性应扩展而不是重复同一数值。"
    return "旧正式扩展按 2024 兼容环境重新评价：旧口碑只作参考，关键看动作经济、特性等级和新版核心机制是否还咬合。"


def score_verdict(score, good, neutral, bad):
    if score in ("S+", "S"):
        return good[0]
    if score == "A":
        return good[1]
    if score == "B":
        return neutral[0]
    if score == "C":
        return neutral[1]
    return bad


def design_issue(note, source):
    if "过强" in note or "破坏" in note or "压低遭遇" in note or "极强甚至过强" in note:
        return "核心问题是数值/动作经济越过健康边界：它不是不给玩家选择，而是太容易把同职业其他选择和 DM 遭遇预算挤掉。"
    if "召唤" in note or "2024 召唤" in note or "兼容" in note:
        return "核心问题是旧版召唤、伙伴或特性接口和 2024 规则不完全咬合，实桌需要 DM 先确认怎样换算。"
    if "随机" in note:
        return "核心问题是随机结果削弱了玩家规划，强度和体验会随着骰面、遭遇节奏和队友配合大幅摆动。"
    if "动作经济" in note:
        return "核心问题是动作、附赠动作、反应或准备回合被占用后，收益没有稳定超过同职业其他选择。"
    if "数值低" in note or "偏弱" in note or "太弱" in note or "弱宗主" in note:
        return "核心问题是数值预算偏低或触发条件太窄，导致主题能看懂但实桌回报不足。"
    if "装备锁定" in note or "主题窄" in note:
        return "核心问题是构筑入口被特定装备、场景或旧书假设锁死，玩家自由度和新版兼容性都受损。"
    if "被动" in note or "堆叠" in note:
        return "核心问题是能力多为被动加值，易用但缺少足够决策深度和回合内表达。"
    if "DM" in note or "依赖" in note:
        return "核心问题是效果边界依赖 DM 解释，不同桌之间强度和体验差距会很大。"
    if "UA" in source:
        return "核心问题是测试稿尚未证明资源曲线和规则边界稳定，不能按正式出版内容给同等信心。"
    if "Plane Shift" in source or "Crooked Moon" in source:
        return "核心问题是来源篇幅和测试样本较少，许多能力需要按 2024 底盘自行校准。"
    return "核心问题不是某个单项缺失，而是它是否用足够少的规则负担提供清楚、可重复、可判断的玩法循环。"


def subclass_design_reasons(name, note, design_scores, source, scores):
    top, good, weak, dead, swing = aspect_summary(scores)
    primary = format_list((top or good)[:3])
    meaningful_dead = [x for x in dead if x != "制造"]
    meaningful_weak = [x for x in weak if x != "制造"]
    liabilities = format_list((meaningful_dead or meaningful_weak or dead or weak)[:3])
    if liabilities == "制造":
        liabilities = "非核心制造/长期制作维度"
    volatile = format_list(swing[:3])
    context = source_design_context(source)
    issue = design_issue(note, source)
    overloaded = "过强" in note or "破坏" in note or "压低遭遇" in note or "极强甚至过强" in note
    very_low = len([x for x in dead if x != "制造"]) >= 3 or len([x for x in weak if x != "制造"]) >= 5

    design_quality = score_verdict(
        design_scores[0],
        (
            f"{note} 设计上不仅给数值，还把子职的队伍位置落到 {primary}；即使横向很强，能力入口仍清楚，玩家知道自己每轮该做什么。{context}",
            f"{note} 子职玩法能和基础职业分工拉开距离，主要贡献集中在 {primary}，没有明显靠含糊措辞或 DM 许可才成立的核心循环。{context}",
        ),
        (
            f"{note} 有清楚卖点，但设计更多是在基础职业上加一个方向，真正改变玩法的部分集中在 {primary}；若这些场景少，存在感会下降。{context}",
            f"{note} 概念能成立，但规则完成度一般；它的有效维度是 {primary}。{issue} {context}",
        ),
        f"{note} 设计扣分来自核心循环不稳、旧规则兼容差或数值预算失衡。{issue} 不能只因主题有趣就给高设计分。{context}",
    )
    if overloaded and design_scores[0] in ("C", "D", "E", "E-", "F"):
        design_quality += " 这里尤其不是因为弱而低分，而是因为强到挤压同职业选择或破坏 bounded accuracy/动作经济，属于坏平衡。"

    theme = score_verdict(
        design_scores[1],
        (
            f"{name} 的主题非常直接：{note} 名称、叙事钩子和战斗职责能互相说明，玩家几乎不需要额外解释就能抓到角色幻想。",
            f"{name} 的主题清楚且容易落桌：{note} 即使强度评价变化，概念本身仍能支撑角色扮演、选法术/装备和队伍身份。",
        ),
        (
            f"{name} 的主题可读但不稀有：{note} 它能成立，不过和同职业相邻子职相比，辨识度更多来自少数关键词而不是完整玩法。",
            f"{name} 的主题表达有断层：{note} 一部分能力服务概念，另一部分只是通用战斗/防御补丁，所以主题分被压到中档。",
        ),
        f"{name} 的主题不够自洽或过度依赖外部设定说明：{note} 如果不先读背景，单看能力很难判断它想让玩家扮演什么。",
    )

    ability_quality = score_verdict(
        design_scores[2],
        (
            f"能力设计强在动作经济和资源回报匹配：高分项是 {primary}，这些能力能在不同 Tier 继续扩展，而不是只在获得等级闪光一次。",
            f"能力组的节奏健康：{primary} 是它的真实功能面，资源、DC/命中和回合占用没有明显互相踩踏。",
        ),
        (
            f"能力设计可用但不锋利：{primary} 能让它工作，问题是 {volatile} 对战役环境敏感，或需要玩家反复权衡资源是否值得。",
            f"能力设计有明显噪音：它能靠 {primary} 做事，但{issue}",
        ),
        f"能力设计低分不是强度低的同义词；这里主要因为{issue} 可能出现纸面好看、实桌难顺，或强到让遭遇设计失真的情况。",
    )
    if overloaded and design_scores[2] in ("C", "D", "E"):
        ability_quality += " 强度过高本身也会扣能力设计分，因为它降低队友选择和 DM 遭遇设计空间。"
    if very_low and design_scores[2] in ("A", "S", "S+"):
        ability_quality += " 高能力设计分只说明机制干净，不表示它能承担所有队伍功能。"

    alignment = score_verdict(
        design_scores[3],
        (
            f"主题与能力高度咬合：文件中的强项 {primary} 正好在表达“{note}”，不是把通用加值贴上主题名。",
            f"能力基本都在服务同一幻想：{primary} 与子职描述一致，弱项 {liabilities} 也没有破坏核心身份，只是功能边界。",
        ),
        (
            f"主题与能力大体一致，但仍有拼装感：{primary} 能回应主题；限制主要是{issue}",
            f"关联度中等：{note} 的叙事方向明确，但实际功能更多落在 {primary}；{issue}",
        ),
        f"主题与能力脱节较明显：{note} 听起来有方向，但实际评分显示 {liabilities} 太多或主要功能不支持该幻想。",
    )

    return [design_quality, theme, ability_quality, alignment]


def subclass_design_table(name, note, design_scores, source, scores):
    rows = ["| 设计项 | 评分 | 具体理由 |", "|---|---|---|"]
    reasons = subclass_design_reasons(name, note, design_scores, source, scores)
    for label, score, reason in zip(["设计质量", "主题", "能力设计质量", "主题与能力关联度"], design_scores, reasons):
        rows.append(f"| {label} | {score} | {reason} |")
    return "\n".join(rows)


def class_doc(name, data):
    return "\n".join([
        f"# {name}（{data['en']}）总评",
        "",
        "## 队伍定位摘要",
        data["team"],
        "",
        "## 详细评价",
        class_review(name, data),
        "",
        "## 分项评分",
        aspect_table(data["scores"]),
        "",
        "## 综合评分",
        table([("综合强度", data["overall"])]),
        "",
        "## 设计相关评分",
        design_table(name, data["design"]),
        "",
        "## 校准说明",
        "若战役大量使用魔法物品购买/制作、据点设施、Circle Magic、宽松休息或高频社交探索，本评分可按文件内定位上调或下调。若某个选项来自 UA 或第三方，评分更依赖规则文本推演和相似机制比较。",
    ]) + "\n"


def uncertainty_note(source):
    if "UA" in source:
        return "这是测试材料，公开讨论会集中在纸面强度、滥用点和与正式版底盘的兼容性，实桌样本不足。评分优先按规则文本、动作经济、资源曲线、法术/专长/物品互动和同职业强弱基准推导；若后续 UA 或正式出版改写，应重新校准。"
    if "Plane Shift" in source or "Crooked Moon" in source or "第三方" in source:
        return "这是半官方或第三方材料，公开优化讨论和实桌样本都明显少于 PHB/XGE/TCE 级别选项。评分主要来自文本机制、同类子职横向比较、常见魔法物品/专长互动和可预期战役环境；若实际桌允许的配套内容不同，结论可能移动一个等级。"
    if "FRHoF" in source:
        return "这是较新的官方/合作设定来源，规则文本可评估，但长期社区共识还不如 2024 PHB 与旧核心扩展稳定。评分把 2024 职业底盘、Circle Magic、常见专长和同职业已知强弱作为基准；高等级结论需要更多实桌回报复核。"
    if "2024" in source or "已生成基准" in source:
        return "这是 2024 或当前采用版本的基准评估，公开讨论相对充分，但 Tier 3-4 的真实实桌样本仍少于数学推演和构筑讨论。评分不按热度给分，而按同 Tier 队伍功能、资源效率、动作经济、法术表/武器精通/专长/物品互动统一校准。"
    return "这是旧版正式扩展或未被新版明确取代的兼容材料，社区讨论样本通常较成熟，但放入 2024 底盘后会受武器精通、专长、法术改写和多职业规则影响。评分以旧版口碑为参考，但最终按 2024 环境中的功能贡献重新估算。"


def subclass_doc(cls, name, en, source, note, overall, design, scores):
    return "\n".join([
        f"# {name}",
        "",
        f"所属职业：{cls}（{CLASSES[cls]['en']}）",
        f"英文名 / 社区检索名：{en}",
        f"来源 / 版本：{source}",
        "",
        "## 队伍定位调整",
        note,
        "",
        "## 详细评价",
        subclass_review(cls, name, note, overall, scores),
        "",
        "## 分项评分",
        aspect_table(scores),
        "",
        "## 综合评分",
        table([("综合强度", overall)]),
        "",
        "## 设计相关评分",
        subclass_design_table(name, note, design, source, scores),
        "",
        "## 不确定点",
        uncertainty_note(source),
    ]) + "\n"


def existing_sub_doc(cls, name, subdata):
    note, overall, design = subdata
    scores = base_scores(cls)
    return subclass_doc(cls, name, name, "已生成基准 / 2024 或当前采用版本", note, overall, design, scores)


def add_extra_data():
    CLASSES.update(EXTRA_CLASSES)
    for name, en, note, overall, design, focus in PSION_SUBS:
        CLASSES["灵能使"]["subs"][name] = (note, overall, design)
    for cls, name, en, source, note, overall, design, focus in EXTRA_SUBS:
        if cls not in CLASSES:
            continue
        CLASSES[cls]["subs"][name] = (note, overall, design)


def write():
    add_extra_data()
    OUT.mkdir(exist_ok=True)
    for cls, data in CLASSES.items():
        cdir = OUT / cls
        cdir.mkdir(exist_ok=True)
        (cdir / "README.md").write_text(class_doc(cls, data), encoding="utf-8")

    for cls, data in CLASSES.items():
        cdir = OUT / cls
        for name, subdata in data["subs"].items():
            # If it is one of our extended records, use its source/focus.
            record = next((r for r in EXTRA_SUBS if r[0] == cls and r[1] == name), None)
            if record:
                _, _, en, source, note, overall, design, focus = record
                scores = with_focus(cls, focus)
                (cdir / f"{name}.md").write_text(subclass_doc(cls, name, en, source, note, overall, design, scores), encoding="utf-8")
                continue
            psion = next((r for r in PSION_SUBS if cls == "灵能使" and r[0] == name), None)
            if psion:
                _, en, note, overall, design, focus = psion
                scores = with_focus(cls, focus)
                (cdir / f"{name}.md").write_text(subclass_doc(cls, name, en, "UA Psion 二期", note, overall, design, scores), encoding="utf-8")
                continue
            (cdir / f"{name}.md").write_text(existing_sub_doc(cls, name, subdata), encoding="utf-8")

    build_dir = OUT / "构筑"
    build_dir.mkdir(exist_ok=True)
    for name, en, desc, link in BUILDS:
        scores = build_scores(name)
        overall = build_overall(name)
        safe = name.replace("/", "／").replace(":", "：")
        text = "\n".join([
            f"# {name}",
            "",
            f"英文/社区称呼：{en}",
            f"社区来源链接：{link}",
            "",
            "## 构筑细节",
            desc,
            "",
            "## 队伍定位",
            "这是以具体关键能力为目标的多职业构筑，不是默认优于单职业。它的价值取决于能否在不严重延迟核心等级的前提下，换到防御、光环、法术表、短休资源、攻击次数、技能或制造能力。",
            "",
            "## 详细评价",
            build_review(name, desc, overall, scores),
            "",
            "## 分项评分",
            aspect_table(scores),
            "",
            "## 综合评分",
            table([("综合强度", overall)]),
            "",
            "## 校准结论",
            "若战役从 1 级成长，任何兼职都要严肃计算关键等级延迟；若从 Tier 2 或 Tier 3 起步，前置职业的收益会明显上升。构筑评分不是社区热度排名，而是按队伍功能维度估算。",
        ]) + "\n"
        (build_dir / f"{safe}.md").write_text(text, encoding="utf-8")

    extra_record = [
        "",
        "## 第二轮扩展记录（2026-05-03）",
        "- 改写所有现有职业/子职文件的设计四项说明，使每项评分都有具体理由。",
        "- 按分项评分重写 `详细评价`：每个文件现在明确列出强项、短板、F 项、等级曲线和环境敏感项。",
        "- 新增覆盖：FRHoF 子职、UA Horror/Arcane/Psion/Havoc/Mystic/XGE 更新、XGE/TCE/SCAG/EGW/Fizban/Dragonlance/Ravenloft 等未被 2024 PHB 明确取代的旧版选项。",
        "- 新增第三方/半官方覆盖：Plane Shift Amonkhet/Kaladesh 中职业相关内容，以及《歪曲之月》第三章子职。",
        "- 对 UA 二期存在的项目，优先采用二期；对 2024 PHB 已正式更新的 PHB 同名子职，不再生成旧版覆盖文件。",
        "- 对社区资料不足的条目，评分依据写入文件中的“不确定点”，并按规则文本、动作经济、资源曲线、法术/专长/物品互动和同职业基准估算。",
        "",
        "## 第三轮横向校准记录（2026-05-03）",
        "- 统一“不确定点”标准：2024/旧正式/FRHoF/UA/Plane Shift/第三方分别使用不同证据权重，不再把讨论充分的正式子职写成“公开社区讨论不足”。",
        "- 校准多职业构筑评分：`诡术师游荡者 / 法师`不再套用直升法师的 S+/S 控制曲线；它保留 S 级技能，但因法术环阶延迟，反制、战场分隔和综合强度下调到更符合实际等级曲线的位置。",
        "- 保留真正异常的 S+：和平领域、暮光领域、时间魔法和高等级护甲法师仍被视为跨同 Tier 竞争中的上限案例；S+ 只用于资源效率或动作经济明显越过同类的项目。",
        "",
        "## 第四轮设计说明校准记录（2026-05-03）",
        "- 重查社区讨论后，设计评分不再只复述子职概述；每个设计项都按来源稳定性、主题清晰度、动作经济、资源曲线、旧版兼容和文件内分项强弱生成独立理由。",
        "- 社区校准点：D&D Beyond 2024 兼容讨论反复提到旧子职需要按新版 3 级子职节奏、Cunning Strike、Channel Divinity、Wild Shape、自动已知法术等接口重看；牧人结社等召唤旧机制在 2024 兼容中存在功能性断裂风险。",
        "- 社区校准点：D&D Beyond partnered-content 讨论显示合作/第三方子职接入 2024 时不仅是数据链接问题，也会遇到“是否按 2024 子职标准重调”的争议；因此第三方/Plane Shift/FRHoF 的设计理由会额外标注来源稳定性。",
        "- 社区校准点：2024 PHB 讨论普遍肯定武器精通和新版子职结构让武系更有战术入口；但高等级满施法法表仍会压低很多子职的相对设计存在感。",
        "- 本轮参考链接：https://www.dndbeyond.com/forums/d-d-beyond-general/general-discussion/201337-5e-to-2024-subclasses ，https://www.dndbeyond.com/forums/d-d-beyond-general/bugs-support/208626-partnered-content-subclasses-dont-show-up-for-2024 ，https://www.polygon.com/dnd-dungeons-dragons/452893/new-weapon-mastery-rules-players-handbook ，https://www.polygon.com/dnd-dungeons-dragons/451969/new-players-handbook-review-2024",
        "",
        "## 第五轮设计分数校准记录（2026-05-03）",
        "- 本轮不只改理由，也校准四项设计分：过强到破坏 bounded accuracy/动作经济的子职，下调“能力设计质量”；旧召唤/伙伴接口在 2024 下需要 DM 换算的子职，下调“设计质量/能力设计质量”；强主题但机制未兑现的子职，下调“主题与能力关联度”。",
        "- 具体校准：和平领域、暮光领域、时间魔法的“能力设计质量”从 C 下调到 D；牧人结社从 B/A/B/A 调为 C/A/C/A；炼金师的“主题与能力关联度”从 A 下调到 B。",
        "- 理由生成也同步校准：不再把非核心制造、反制施法或召唤缺口机械地当成所有子职的设计失败；低分理由优先引用该子职真正的问题，如过强、随机、动作经济、旧版兼容、数值不足、装备锁定或 DM 依赖。",
    ]
    (OUT / "changelog.md").write_text(record_doc() + "\n".join(extra_record) + "\n", encoding="utf-8")
    (OUT / "README.md").write_text(summary_doc() + "\n## 第二轮扩展说明\n本目录现包含 2024 基准、UA、旧版未覆盖、合作设定书和第三方子职。总评主表仍只列基础职业与构筑；具体子职请进入各职业目录查看。\n", encoding="utf-8")


if __name__ == "__main__":
    write()
