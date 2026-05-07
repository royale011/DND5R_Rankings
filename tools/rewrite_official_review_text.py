from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RANKINGS = ROOT / "Rankings"

TIERS = ["Tier 1", "Tier 2", "Tier 3", "Tier 4"]
RANK_VALUE = {"F": 0, "E": 1, "D": 2, "C": 3, "B": 4, "A": 5, "S": 6, "S+": 7}
VALUE_RANK = {v: k for k, v in RANK_VALUE.items()}

ASPECT_ORDER = [
    "近战伤害者",
    "远程伤害者",
    "法术伤害者",
    "防御和生存",
    "治疗和临时生命",
    "团队增益",
    "反制施法者",
    "减益",
    "战场分隔",
    "召唤 / 伙伴",
    "技能使用",
    "制造",
]

CLASS_NOTES = {
    "野蛮人": "它的价值来自稳定近战、承伤和强迫敌人处理前排；短板是法术、远程和战役级工具。",
    "战士": "它依靠额外攻击、动作爆发、武器精通和专长扩展输出面；队伍级解题仍依赖子职或装备。",
    "武僧": "它以机动、控制和防御反应换取较低装备依赖；高等级仍需要面对法术生态的压力。",
    "游荡者": "它是技能、潜入和无资源单点输出专家；复杂战斗中的团队影响力主要看子职是否补工具。",
    "圣武士": "它把前线输出、豁免灵光、治疗和爆发压在同一底盘上；强度通常来自队伍防线而不只是 DPR。",
    "游侠": "它处在武器输出、探索、半施法和伙伴/召唤之间；真实强度很依赖法术选择与战役地形。",
    "牧师": "它的底盘已经同时拥有治疗、增益、控制、防御和高等级神术；子职只要补对方向就会很强。",
    "德鲁伊": "它的强度来自控制、召唤、变形和环境法术；子职差距主要体现在动作经济和形态/召唤管理。",
    "法师": "它是最强法术表的载体；子职评价重点是是否进一步提高先手、控制命中、资源弹性或现实改写。",
    "吟游诗人": "它用技能、辅助、控制和魔法秘密填补队伍缺口；输出通常不是核心卖点。",
    "术士": "它用短休法术位、魔能祈唤和契约形态换取稳定循环；高等级全能性不如法师但构筑弹性很高。",
    "魔契师": "它用短休资源、祈唤与契约构筑形成模块化角色；强弱取决于资源恢复和祈唤组合。",
    "奇械师": "它围绕魔法物品、工具、半施法和防御支持运作；强度高度依赖物品经济与制作规则。",
    "灵能使": "它以灵能骰/点数、心灵控制和特殊资源表达主题；评价重点是资源是否能稳定换成战术优势。",
}

SOURCE_NOTES = {
    "TCE": "旧扩展内容放入 2024 环境时，要特别看动作经济、特性等级和新版核心规则是否产生额外叠加。",
    "XGE": "XGE 子职有较成熟社区口碑，但在 2024 底盘下仍需要重新检查动作、专长和法术改写后的表现。",
    "EGW": "EGW 内容常有较强的战役特色和高上限，不能只按普通 PHB 子职预算评估。",
    "UA": "UA 内容按测试材料处理：可以评价实际强度，但设计分必须更严格看文本边界和未定稿风险。",
    "FRHoF": "FRHoF 内容需要同时考虑 Circle Magic、地区主题和新资源入口对高等级生态的影响。",
}


def split_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## .+$", text, flags=re.M))
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group(0)[3:].strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[title] = text[start:end].strip("\n")
    return sections


def replace_section(text: str, title: str, body: str) -> str:
    pattern = re.compile(rf"(^## {re.escape(title)}\n)(.*?)(?=^## |\Z)", flags=re.S | re.M)
    if pattern.search(text):
        return pattern.sub(lambda m: m.group(1) + body.strip() + "\n\n", text, count=1)
    return text.rstrip() + f"\n\n## {title}\n{body.strip()}\n"


def parse_scores(section: str) -> dict[str, list[str]]:
    scores: dict[str, list[str]] = {}
    for line in section.splitlines():
        if not line.startswith("| ") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 5 and cells[0] in ASPECT_ORDER:
            scores[cells[0]] = cells[1:5]
    return scores


def parse_overall(section: str) -> list[str]:
    for line in section.splitlines():
        if line.startswith("| 综合强度 "):
            cells = [c.strip() for c in line.strip("|").split("|")]
            return cells[1:5]
    return []


def parse_design(section: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in section.splitlines():
        if not line.startswith("| ") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[0] in {"设计质量", "主题", "能力设计质量", "主题与能力关联度"}:
            out[cells[0]] = cells[1]
    return out


def avg_rank(values: list[str]) -> float:
    nums = [RANK_VALUE.get(v, 0) for v in values]
    return sum(nums) / len(nums) if nums else 0


def trend(values: list[str]) -> str:
    if not values:
        return "缺少综合评分，需要回到源文本复核。"
    start = RANK_VALUE[values[0]]
    end = RANK_VALUE[values[-1]]
    if end >= start + 2:
        return f"综合评分从 {values[0]} 上升到 {values[-1]}，说明它越到高等级越依赖法术、资源升级或队伍级工具取得优势。"
    if start >= end + 2:
        return f"综合评分从 {values[0]} 下降到 {values[-1]}，不是角色绝对失效，而是同 Tier 中高环法术、反制、召唤、位移和战役级工具的权重快速上升。"
    if len(set(values)) == 1:
        return f"综合评分长期维持在 {values[0]}，说明它的主要贡献不是某一级爆点，而是同一队伍职责持续有效。"
    return f"综合评分在 {' / '.join(values)} 之间波动，说明它的价值受等级节点、资源规模和战役环境共同影响。"


def top_bottom(scores: dict[str, list[str]]) -> tuple[list[str], list[str], list[str]]:
    avgs = {k: avg_rank(v) for k, v in scores.items()}
    tops = [k for k, v in sorted(avgs.items(), key=lambda kv: (-kv[1], ASPECT_ORDER.index(kv[0]))) if v >= 4][:6]
    if not tops:
        tops = [k for k, v in sorted(avgs.items(), key=lambda kv: (-kv[1], ASPECT_ORDER.index(kv[0]))) if v >= 3][:4]
    mids = [k for k, v in sorted(avgs.items(), key=lambda kv: (-kv[1], ASPECT_ORDER.index(kv[0]))) if 3 <= v < 5][:6]
    lows = [k for k, v in sorted(avgs.items(), key=lambda kv: (kv[1], ASPECT_ORDER.index(kv[0]))) if v <= 2][:6]
    return tops, mids, lows


def list_zh(items: list[str]) -> str:
    if not items:
        return "无明显项目"
    return "、".join(items)


def first_line(section: str) -> str:
    for line in section.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def source_note(source: str) -> str:
    for key, note in SOURCE_NOTES.items():
        if key in source or key in source.upper():
            return note
    if "2024" in source or "PHB" in source or "玩家手册" in source:
        return "2024 基准内容按新版职业节奏评价：3 级入口、动作经济和高等级扩展都应能与新版核心规则咬合。"
    if "第三方" in source or "partner" in source.lower():
        return "合作或第三方内容按实际文本评价，不默认获得官方 PHB 子职的平衡背书。"
    return "评分按当前采用版本和 2024 兼容环境统一校准。"


def overall_sentence(overall: list[str]) -> str:
    if not overall:
        return "综合评分缺失，以下评价只作为结构化阅读辅助。"
    mx = max(RANK_VALUE[v] for v in overall)
    mn = min(RANK_VALUE[v] for v in overall)
    if mx >= 7:
        return "出现 S+ 时，我按全生态天花板处理：它必须不只是强于同职业，还要能压过多数官方/合作选项的同 Tier 上限。"
    if mx >= 6 and mn <= 3:
        return "它有非常强的高点，但低分项也真实存在；组队时不能把一个强项误读成全功能覆盖。"
    if mx >= 6:
        return "它在自身核心职责上已经达到顶级，但是否成为队伍核心仍取决于这些高分项是否正好补到队伍缺口。"
    if mx <= 3:
        return "它不是不能玩，而是在优化或高等级环境里缺少足够能改变遭遇走向的工具。"
    return "它的强度更多来自稳定补位，而不是单个能力直接接管遭遇。"


def aspect_profile(aspect: str, values: list[str]) -> str:
    avg = avg_rank(values)
    ranks = " / ".join(values)
    if aspect in {"近战伤害者", "远程伤害者"}:
        if avg >= 5:
            return f"{aspect}为 {ranks}，说明它在武器回合里不是陪衬；命中、额外伤害、优势来源或攻击次数足以和同 Tier 输出手比较。"
        if avg >= 3:
            return f"{aspect}为 {ranks}，属于能参与但不该被当成主要胜利条件的水平；它更依赖队友控场、专长、魔法武器或短休资源补足。"
        return f"{aspect}为 {ranks}，基本不是该选项的队伍职责；把它推到这个位置通常会牺牲它本来更强的功能。"
    if aspect == "法术伤害者":
        if avg >= 5:
            return f"法术伤害为 {ranks}，代表它有稳定的范围、爆发或高环压制手段；这类评分通常来自法术表和资源规模，而不是单个伤害特性。"
        if avg >= 3:
            return f"法术伤害为 {ranks}，可以补刀或处理群怪，但很难在专职施法者生态里取得绝对优势。"
        return f"法术伤害为 {ranks}，说明它没有可靠施法输出入口；相关排名不能用魔法物品或队友法术替它抬分。"
    if aspect in {"防御和生存", "治疗和临时生命", "团队增益"}:
        if avg >= 5:
            return f"{aspect}为 {ranks}，是它最能改变队伍容错率的部分；这类能力会直接影响前排站位、豁免压力和连续遭遇续航。"
        if avg >= 3:
            return f"{aspect}为 {ranks}，能提供真实帮助，但通常只是把队伍从危险边缘拉回正常水平，而不是重塑整场遭遇。"
        return f"{aspect}为 {ranks}，不能指望它承担队伍安全网；需要牧师、圣武士、吟游诗人、法术或物品来补。"
    if aspect in {"反制施法者", "减益", "战场分隔"}:
        if avg >= 5:
            return f"{aspect}为 {ranks}，这是高等级最有价值的贡献之一；它能减少敌方有效行动，而不是只追加伤害数字。"
        if avg >= 3:
            return f"{aspect}为 {ranks}，有可用工具但不稳定；常见限制是豁免类型、专注、射程、先攻或每天资源。"
        return f"{aspect}为 {ranks}，表示它缺少处理施法者、精英怪或复杂地形的硬工具。"
    if aspect == "召唤 / 伙伴":
        if avg >= 5:
            return f"召唤 / 伙伴为 {ranks}，会显著增加行动经济、侦察面或承伤缓冲；若 DM 严格管理召唤节奏，实桌表现会更接近表中保守值。"
        if avg >= 3:
            return f"召唤 / 伙伴为 {ranks}，可作为补充资源，但通常不够稳定到围绕它建队。"
        return f"召唤 / 伙伴为 {ranks}，不是该选项的真实卖点。"
    if aspect == "技能使用":
        if avg >= 5:
            return f"技能使用为 {ranks}，说明它在战斗外能持续产出信息、潜入、交涉或工具优势。"
        if avg >= 3:
            return f"技能使用为 {ranks}，足以覆盖常规检定，但还不到游荡者或吟游诗人那种队伍核心工具位。"
        return f"技能使用为 {ranks}，战斗外贡献主要依赖玩家创意和背景，而不是职业文本。"
    if aspect == "制造":
        if avg >= 5:
            return f"制造为 {ranks}，在允许制作、魔法物品经济和准备时间的战役中会明显改变队伍资源曲线。"
        if avg >= 3:
            return f"制造为 {ranks}，有规则入口但不是可靠强项；是否有价值很看 DM 是否给时间、材料和市场。"
        return f"制造为 {ranks}，不能把它当作长期经济或装备优势来源。"
    return f"{aspect}为 {ranks}，按同 Tier 功能权重校准。"


def selected_aspect_profiles(scores: dict[str, list[str]], tops: list[str], lows: list[str]) -> str:
    chosen: list[str] = []
    for aspect in tops[:3] + lows[:2]:
        if aspect in scores and aspect not in chosen:
            chosen.append(aspect)
    if not chosen:
        chosen = [k for k in ASPECT_ORDER if k in scores][:3]
    return "\n\n".join(aspect_profile(aspect, scores[aspect]) for aspect in chosen)


def build_position(title: str, class_name: str, old: str, scores: dict[str, list[str]], overall: list[str], is_class: bool) -> str:
    tops, _, lows = top_bottom(scores)
    base = CLASS_NOTES.get(class_name, "它的评价需要放回所属职业底盘、子职资源和同 Tier 队伍功能中看。")
    label = "摘要" if is_class else "调整"
    lead = old or base
    low_text_class = (
        f"低分项集中在 {list_zh(lows[:4])}，这些不是操作细节能完全弥补的缺口，而是职业工具箱本身的边界。"
        if lows
        else "它没有特别尖锐的规则空白；真正的限制通常来自资源规模、动作经济和高等级遭遇的复杂度。"
    )
    low_text_sub = (
        f"如果战役重点落在 {list_zh(lows[:3])}，它仍需要队友、法术、专长或魔法物品补位。"
        if lows
        else "它没有明显完全空白的低分项，评价重点应放在资源效率、动作经济和高等级贡献是否足够。"
    )
    if is_class:
        return (
            f"{lead}\n\n"
            f"按当前评分，{title} 的稳定价值集中在 {list_zh(tops[:4])}。{base} "
            f"{low_text_class}"
        )
    return (
        f"{lead}\n\n"
        f"相对 {class_name} 底盘，{title} 主要改变的是 {list_zh(tops[:4])}。"
        f"如果这些维度正好是队伍缺口，它会明显抬高存在感；{low_text_sub}"
    )


def build_detail(title: str, class_name: str, old_position: str, scores: dict[str, list[str]], overall: list[str], source: str, is_class: bool) -> str:
    tops, mids, lows = top_bottom(scores)
    role = "基础职业" if is_class else "子职"
    first = (
        f"作为{role}，{title} 的有效队伍位置由 {list_zh(tops[:5])} 决定。"
        f"这些项目不是简单的主题标签，而是它在同 Tier 比较中真正能反复兑现的功能。"
    )
    aspects = selected_aspect_profiles(scores, tops, lows)
    if lows:
        second = (
            f"它的短板也很明确：{list_zh(lows[:5])}。"
            f"这些低分项若长期停在 E/F，通常代表文本本身没有规则入口；若只是 C/D，则说明能碰到该功能，但效率、资源或动作经济不足以当主责。"
        )
    else:
        second = (
            "它没有明显完全空白的功能项，但这不等于没有弱点。"
            "这类选项要看多个 B/A 项能否在连续遭遇中同时兑现，而不是只看单场最佳表现。"
        )
    third = (
        f"{trend(overall)} {overall_sentence(overall)} "
        f"因此综合评分不是十二项的机械平均，而是按控制、反制、团队增益、治疗、召唤、战场分隔和高等级解题权重重新校准。"
    )
    fourth = (
        f"{source_note(source)} "
        f"实际实桌还要看敌人类型、休息频率、魔法物品经济、Origin feats、Circle Magic、队伍是否已有同类功能，以及 DM 对召唤、制作、隐藏和信息获取的裁定。"
    )
    if old_position:
        return f"{old_position}\n\n{first}\n\n{aspects}\n\n{second}\n\n{third}\n\n{fourth}"
    return f"{first}\n\n{aspects}\n\n{second}\n\n{third}\n\n{fourth}"


def design_reason(item: str, rating: str, title: str, class_name: str, scores: dict[str, list[str]], overall: list[str], old_position: str, source: str) -> str:
    tops, _, lows = top_bottom(scores)
    max_overall = max((RANK_VALUE.get(x, 0) for x in overall), default=0)
    low_design_high_power = item in {"设计质量", "能力设计质量"} and rating in {"C", "D", "E"} and max_overall >= 6
    top_focus = tops[0] if tops else "核心功能"
    top_ranks = " / ".join(scores.get(top_focus, [])) if top_focus in scores else ""
    low_focus = lows[0] if lows else ""
    identity = f"{title} 的核心概念"
    if item == "设计质量":
        if low_design_high_power:
            return f"{rating}：{title} 的强度不低，问题是规则预算过满。它在 {list_zh(tops[:3])} 上压得很重，容易挤压 {class_name} 的其他选择或增加 DM 遭遇负担。"
        if rating in {"A", "S", "S+"}:
            return f"{rating}：设计骨架清楚，{list_zh(tops[:3])} 能从早期一路延伸到后期；它没有把强度藏在模糊裁定里，而是让玩家知道自己该怎样为队伍创造价值。"
        if rating == "B":
            if lows:
                return f"{rating}：整体可以直接落桌，卖点也清楚；扣分在于它主要强化既有路线，对 {list_zh(lows[:2])} 没有给出足够新的队伍解法。"
            return f"{rating}：整体可以直接落桌，但更像稳定补强而不是结构性创新；它能把 {list_zh(tops[:2])} 做扎实，却很少改变队伍构成方式。"
        return f"{rating}：概念能看懂，但规则完成度跟不上；主要问题落在动作经济、装备/场景依赖或数值预算，导致实际表现比主题承诺更窄。"
    if item == "主题":
        if rating in {"A", "S", "S+"}:
            return f"{rating}：主题辨识度高；{identity} 能自然解释 {list_zh(tops[:3])}，也能支撑角色扮演、装备选择和队伍身份。"
        if rating == "B":
            tail = f"；但 {list_zh(lows[:2])} 的功能缺口说明主题没有覆盖全部队伍职责" if lows else "；但它更像熟悉主题的稳健版本，而不是特别尖锐的新表达"
            return f"{rating}：主题可读，{identity} 能建立基本形象{tail}。"
        return f"{rating}：主题表达偏散，{identity} 没有稳定压住整套能力；读者能理解它想做什么，但很难立刻看出它和相邻选项的本质差别。"
    if item == "能力设计质量":
        if low_design_high_power:
            return f"{rating}：低分不是因为弱，而是因为 {list_zh(tops[:3])} 的收益过高或过集中，可能破坏 bounded accuracy、动作经济、资源消耗或高等级遭遇预算。"
        if rating in {"A", "S", "S+"}:
            return f"{rating}：能力循环干净，{top_focus}{f'（{top_ranks}）' if top_ranks else ''} 的评分来自可重复使用的规则入口；资源、动作和命中/DC 没有明显互相抢占。"
        if rating == "B":
            if lows:
                return f"{rating}：能力组基本健康，但有些等级只是把既有打法加厚；对 {list_zh(lows[:2])} 的补救不足，所以功能边界仍很清楚。"
            return f"{rating}：能力组基本健康，{top_focus}{f'（{top_ranks}）' if top_ranks else ''} 能稳定兑现；不足是部分等级更像数值加固，而不是提供新的战术问题解法。"
        return f"{rating}：能力文本或资源边界需要复核；它可能过窄、过度依赖场景，或把关键强度交给 DM 裁定，导致同桌可预期性不足。"
    if item == "主题与能力关联度":
        if rating in {"A", "S", "S+"}:
            return f"{rating}：主题和功能互相支撑，{list_zh(tops[:3])} 都能直接解释为 {title} 应该做到的事；玩家不需要额外脑补能力为何存在。"
        if rating == "B":
            extra = f"；同时 {low_focus} 的缺口也说明主题没有覆盖所有队伍职责" if low_focus else ""
            return f"{rating}：大部分能力能回应主题，但仍有少数功能更像通用补强，而不是从 {title} 的核心意象自然长出来{extra}。"
        return f"{rating}：主题和能力之间有明显断层；即使数值可用，玩家也可能觉得这些功能只是拼装在一起，而不是同一个概念的自然展开。"
    return f"{rating}：按当前文本和同职业基准校准。"


def build_design_table(title: str, class_name: str, design: dict[str, str], scores: dict[str, list[str]], overall: list[str], old_position: str, source: str) -> str:
    lines = [
        "| 设计项 | 评分 | 具体理由 |",
        "|---|---|---|",
    ]
    for item in ["设计质量", "主题", "能力设计质量", "主题与能力关联度"]:
        rating = design.get(item, "B")
        lines.append(f"| {item} | {rating} | {design_reason(item, rating, title, class_name, scores, overall, old_position, source)} |")
    return "\n".join(lines)


def build_uncertainty(source: str, scores: dict[str, list[str]], overall: list[str], is_class: bool) -> str:
    tops, _, lows = top_bottom(scores)
    caveat = source_note(source)
    low_clause_class = (
        f"若长期考验 {list_zh(lows[:3])}，则需要队友补位。"
        if lows
        else "若战役要求跨领域全能解题，则需要检查资源消耗和动作经济是否跟得上。"
    )
    low_clause_sub = (
        f"若战役重点落在 {list_zh(lows[:3])}，它的短板会被放大。"
        if lows
        else "若战役重点是连续复杂遭遇，它的资源效率和高等级上限会比单场表现更重要。"
    )
    if is_class:
        return (
            f"{caveat}\n\n"
            f"本文件是职业总评，子职、构筑、多职业、魔法物品、休息频率和战役题材都会改变实际表现。"
            f"尤其当战役大量奖励 {list_zh(tops[:3])} 时评分会上浮；{low_clause_class}"
        )
    return (
        f"{caveat}\n\n"
        f"本评分不按社区热度给分，而按同 Tier 队伍功能、资源效率、动作经济和规则可重复性校准。"
        f"若实桌环境持续奖励 {list_zh(tops[:3])}，该子职会显得更强；{low_clause_sub}"
    )


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "## 分项评分" not in text or "## 综合评分" not in text or "## 设计相关评分" not in text:
        return False
    if path.parent.name == "构筑":
        return False

    sections = split_sections(text)
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    title = title_match.group(1).strip() if title_match else path.stem
    class_name = path.parent.name
    is_class = path.name == "README.md"
    if is_class:
        title = title.replace("总评", "").strip()
        title = re.sub(r"（[^）]*）", "", title).strip("（） ")

    source = ""
    m = re.search(r"^来源 / 版本：(.+)$", text, flags=re.M)
    if m:
        source = m.group(1).strip()

    scores = parse_scores(sections.get("分项评分", ""))
    overall = parse_overall(sections.get("综合评分", ""))
    design = parse_design(sections.get("设计相关评分", ""))

    pos_title = "队伍定位摘要" if is_class else "队伍定位调整"
    old_position = first_line(sections.get(pos_title, ""))
    text = replace_section(text, pos_title, build_position(title, class_name, old_position, scores, overall, is_class))
    text = replace_section(text, "详细评价", build_detail(title, class_name, old_position, scores, overall, source, is_class))
    text = replace_section(text, "设计相关评分", build_design_table(title, class_name, design, scores, overall, old_position, source))

    uncertainty_title = "校准说明" if is_class else "不确定点"
    if uncertainty_title in split_sections(text):
        text = replace_section(text, uncertainty_title, build_uncertainty(source, scores, overall, is_class))

    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    changed = 0
    skipped = 0
    for path in sorted(RANKINGS.rglob("*.md")):
        if path.name == "changelog.md" or (path.name == "README.md" and path.parent == RANKINGS):
            skipped += 1
            continue
        if process_file(path):
            changed += 1
        else:
            skipped += 1
    print(f"rewritten={changed} skipped={skipped}")


if __name__ == "__main__":
    main()
