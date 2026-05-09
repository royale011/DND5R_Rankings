from pathlib import Path
import re

ROOT = Path("Rankings")
TIERS = ["Tier 1（1-4）", "Tier 2（5-10）", "Tier 3（11-16）", "Tier 4（17-20）"]
TIER_SHORT = {"Tier 1（1-4）": "T1", "Tier 2（5-10）": "T2", "Tier 3（11-16）": "T3", "Tier 4（17-20）": "T4"}
RANKS = ["S+", "S", "S-", "A+", "A", "A-", "B+", "B", "C", "D", "E", "E-", "F"]
SUMMARY_FILE = "README.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_overall(path: Path):
    text = read(path)
    m = re.search(r"## 综合评分\s*(.*?)(?=\n## |\Z)", text, re.S)
    if not m:
        return None
    section = m.group(1)
    rows = {}
    for line in section.splitlines():
        if not line.startswith("| Tier "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0] in TIERS:
            rows[cells[0]] = (cells[1], cells[2])
    if len(rows) != 4:
        return None
    return rows


def short_reason(reason: str, limit: int = 96) -> str:
    reason = re.sub(r"\s+", " ", reason).strip()
    if len(reason) <= limit:
        return reason
    cut = reason[:limit]
    for sep in ["。", "；", "，"]:
        idx = cut.rfind(sep)
        if idx >= 34:
            return cut[: idx + 1]
    return cut + "..."


def is_marked_nonfirst_party(name: str) -> bool:
    return bool(re.search(r"（[^）]+）$", name))


def is_egw_exception(name: str) -> bool:
    return name.endswith("（EGW）")


def display_subclass_name(class_dir: Path, path: Path) -> str:
    if class_dir.name == "法师" and path.parent.name == "神圣奇术":
        return f"神圣奇术（5E UA） - {path.stem}"
    return path.stem


def is_theurgy_mapping(class_dir: Path, path: Path) -> bool:
    return class_dir.name == "法师" and path.parent.name == "神圣奇术"


def class_dirs():
    dirs = []
    for p in sorted(ROOT.iterdir(), key=lambda x: x.name):
        if not p.is_dir() or p.name == "构筑":
            continue
        if (p / SUMMARY_FILE).exists():
            dirs.append(p)
    return dirs


def class_scores():
    rows = []
    for d in class_dirs():
        scores = extract_overall(d / SUMMARY_FILE)
        if scores:
            rows.append((d.name, scores))
    return rows


def subclass_entries():
    official = []
    nonfirst = []
    for d in class_dirs():
        paths = list(d.glob("*.md"))
        if d.name == "法师" and (d / "神圣奇术").exists():
            paths.extend((d / "神圣奇术").glob("*.md"))
        for p in sorted(paths, key=lambda x: str(x.relative_to(d))):
            if p.name == SUMMARY_FILE:
                continue
            if p.parent.name == "神圣奇术" and p.name == SUMMARY_FILE:
                continue
            scores = extract_overall(p)
            if not scores:
                continue
            sub = display_subclass_name(d, p)
            theurgy_mapping = is_theurgy_mapping(d, p)
            marked_nonfirst = is_marked_nonfirst_party(sub)
            entry = {
                "class_name": d.name,
                "item_name": sub,
                "scores": scores,
                "kind": "subclass",
                "marked": marked_nonfirst or theurgy_mapping,
            }
            if theurgy_mapping:
                nonfirst.append(entry)
            elif marked_nonfirst:
                nonfirst.append(entry)
                if is_egw_exception(sub):
                    official.append(entry)
            else:
                official.append(entry)
    return official, nonfirst


def build_entries():
    entries = []
    build_dir = ROOT / "构筑"
    if not build_dir.exists():
        return entries
    for p in sorted(build_dir.glob("*.md"), key=lambda x: x.name):
        scores = extract_overall(p)
        if scores:
            entries.append({
                "class_name": "构筑",
                "item_name": p.stem,
                "scores": scores,
                "kind": "build",
            })
    return entries


def rank_table(title, first_col, rows):
    out = [f"## {title}", f"| {first_col} | Tier 1（1-4） | Tier 2（5-10） | Tier 3（11-16） | Tier 4（17-20） |", "|---|---|---|---|---|"]
    for name, scores in rows:
        out.append("| " + " | ".join([name] + [scores[t][0] for t in TIERS]) + " |")
    return "\n".join(out)


def leaderboard(title, entries):
    out = [
        f"## {title}",
    ]
    for tier in TIERS:
        out.extend([
            "",
            f"### {tier}",
            "",
            "| 阶段 | 评级 | 职业 | 子职 | 具体理由 |",
            "|---|---|---|---|---|",
        ])
        rows = []
        for e in entries:
            rank, reason = e["scores"][tier]
            rows.append((tier, rank, e["class_name"], e["item_name"], short_reason(reason)))
        rows.sort(key=lambda row: (RANKS.index(row[1]), row[2], row[3]))
        for tier, rank, class_name, item_name, reason in rows:
            out.append(f"| {TIER_SHORT[tier]} | {rank} | {class_name} | {item_name} | {reason} |")
    return "\n".join(out).rstrip()


def main():
    classes = class_scores()
    builds = [(e["item_name"], e["scores"]) for e in build_entries()]
    official_subclasses, nonfirst_subclasses = subclass_entries()
    build_es = build_entries()
    official_plus_builds = official_subclasses + build_es

    doc = []
    doc.append("# 5.5e / 2024 职业、子职与构筑总评")
    doc.append("")
    doc.append("## 5e 到 5.5e 的平衡变化")
    doc.append("2024规则把武器职业的底线抬高了：`武器精通`、武僧重做、战士资源扩展、野蛮人和游侠的可玩性都比2014更好。圣武士的爆发被压制，但`守护灵光`仍然让它在Tier 2开始保持队伍核心地位。游荡者获得更有趣的`狡诈打击`，但高等级仍缺少足够强的战斗资源。满施法者没有被真正压低，高等级仍然靠法表、控制、召唤、反制、传送、信息、复活和现实改写支配战局。")
    doc.append("")
    doc.append("## 各 Tier 职业平衡")
    doc.append("Tier 1里牧师、野蛮人、武僧、战士、圣武士和部分德鲁伊/术士都很强，低级法师与吟游诗人更依赖法术位管理。Tier 2是圣武士、牧师、德鲁伊、法师、术士、吟游诗人和部分强构筑全面发力的区间。Tier 3-4明显进入满施法者游戏；武器职业需要魔法物品、队友增益、特定战术或强子职才能维持与高阶施法者同桌比较的存在感。")
    doc.append("")
    doc.append(rank_table("职业综合强度表", "职业", classes))
    doc.append("")
    doc.append(rank_table("构筑综合强度表", "构筑", builds))
    doc.append("")
    doc.append(leaderboard("分阶段子职排行榜", official_plus_builds))
    doc.append("")
    doc.append("本节把官方第一方子职、项目例外的EGW子职，以及`Rankings\\构筑`中的有效构筑放在同一竞争池。构筑在`职业`列标为`构筑`，方便和单职业子职区分；每条理由来自对应单文件`综合评分`。")
    doc.append("")
    doc.append(leaderboard("UA/合作方/第三方子职分阶段排行榜", nonfirst_subclasses))
    doc.append("")
    doc.append("## 设计变化")
    doc.append("2024的设计质量总体上升：更多职业在低等级就能表达主题，资源使用更清楚，动作经济更现代。但设计质量不等于强度。游侠是典型例子：实战并非不可用，但`猎人印记`绑定让职业设计观感偏弱。游荡者则相反：新版机制更有趣，优化强度仍偏低。法师的问题不是缺少设计，而是法表过强，导致子职很难在不破坏平衡的前提下显得同样重要。")
    doc.append("")
    doc.append("## 职业设计横向比较")
    doc.append("武僧、战斗大师战士、世界树野蛮人、星辰德鲁伊、防护/预言法师、时械/畸变术士属于设计与强度都优秀的样本。炼金师奇械师、勇士战士、荣耀圣武士、猎人游侠属于主题能懂但机制不够锋利的样本。灵能使作为UA职业，二期方向比一期清楚，`裂空使`保留一期文本后也能形成完整生态，但它仍更像灵能主题满施法者，而不是完全独立的灵能系统。")
    doc.append("")
    doc.append("## 总体结论")
    doc.append("如果以队伍胜率和解题能力为唯一标准，Tier 3-4的S层仍主要由法师、牧师、德鲁伊、术士、吟游诗人、灵能使和少数高强构筑占据；如果以Tier 1-2的桌面体验和战斗贡献看，2024武僧、战士、圣武士、游侠和野蛮人都比2014更值得玩。5.5e的最大成功是让多数职业更好玩；最大失败是没有真正解决高等级施法者统治。")
    doc.append("")
    doc.append("## 更新说明")
    doc.append("本次总评从当前各职业、子职与构筑文件的`综合评分`表回读生成排行榜。根`分阶段子职排行榜`已按新标准加入构筑，使其直接与官方子职竞争；UA、合作方、第三方子职仍保留在独立排行榜中，EGW子职按项目例外同时出现在两个排行榜。")
    doc.append("")
    (ROOT / SUMMARY_FILE).write_bytes(("\n".join(doc).rstrip() + "\n").encode("utf-8"))

    # Standards updates are recorded manually in Rankings/changelog.md.
    # This script only regenerates Rankings/README.md from file-level 综合评分 tables.


if __name__ == "__main__":
    main()
