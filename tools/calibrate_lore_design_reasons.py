from __future__ import annotations

from pathlib import Path
from typing import NamedTuple


ROOT = Path("Rankings")

EXCLUDE = {
    "秘密尖塔",
    "瓦尔达",
    "邪狱使",
    "铳士",
    "拳斗士",
    "狮鹫鞍包",
}

STRIXHAVEN = {
    "衡鉴魔法师",
    "银毫魔法师",
    "粹丽魔法师",
    "量析魔法师",
    "靡华魔法师",
}

class LoreNote(NamedTuple):
    marker: str
    theme: str
    alignment: str


SOURCE_NOTES = [
    LoreNote(
        "EGW",
        "设定复核后，它应被读成 Exandria 邓纳曼西与 Kryn 传统的表达，而不是泛用空间/时间奇术。",
        "对齐度看它是否把可能性、重力或时间残影转成可操作的战斗/探索循环。",
    ),
    LoreNote(
        "塔尔多雷",
        "设定复核后，主题应落在 Tal'Dorei / Exandria 的阵营、神祇和英雄时代遗产上。",
        "对齐度看能力是否把 Tal'Dorei 的英雄叙事、宗教或阵营身份落实到实际玩法。",
    ),
    LoreNote(
        "鬼魅幽谷",
        "设定复核后，主题需要服务 Etharis 的黑暗奇幻、死神祇、诅咒和宗教裂痕。",
        "对齐度看机制是否让审判、腐败、诅咒或绝望感成为桌面决策，而不只是暗色命名。",
    ),
    LoreNote(
        "歪曲之月",
        "设定复核后，主题应贴住 Druskenvald / Wickermoor 的民俗恐怖、迷信、仪式和社群压力。",
        "对齐度看机制是否把民俗恐怖的仪式性、代价或社会张力转成稳定玩法。",
    ),
    LoreNote(
        "谦卑林",
        "设定复核后，主题应放在 Everden / Humblewood 的鸟民、谦民、伟大韵律、火灾创伤和社群秩序中理解。",
        "对齐度看能力是否把迁徙、社群、自然节律或火灾后的秩序压力落到桌面循环。",
    ),
    LoreNote(
        "黯潮之书",
        "设定复核后，主题应服务 Shadow Realm 的黯潮、影路、影精和暗影礼法。",
        "对齐度看机制是否把阴影国度的通行、契约、伪装或侵蚀感变成实际选择。",
    ),
    LoreNote(
        "胧忆岛",
        "设定复核后，主题应尊重 The Islands of Sina Una 的菲律宾神话、群岛、精魂和食月者传说。",
        "对齐度看机制是否把群岛旅行、精魂互动、祖灵或神话灾厄转成清楚玩法。",
    ),
    LoreNote(
        "阿芒凯",
        "设定复核后，主题应落在 Amonkhet 的五神试炼、神法老秩序和 cartouche 式德性上。",
        "对齐度看机制是否真的体现试炼、服从、野心、团结或热忱，而不是只借用神祇标签。",
    ),
    LoreNote(
        "克苏鲁",
        "设定复核后，主题应服务克苏鲁神话的宇宙恐怖、邪教、禁忌知识和人类脆弱性。",
        "对齐度看机制是否让未知、污染、疯狂或渺小感影响实际桌面选择。",
    ),
    LoreNote(
        "血猎手",
        "设定复核后，主题应读作 Critical Role / Exandria 中 Claret Orders 的血魔法猎魔传统，而不是泛用黑暗游侠。",
        "对齐度看机制是否把 Hunter's Bane、血魔法代价、猩红仪式、血咒和各圣约的怪物猎手身份落实到实际循环。",
    ),
]


def source_note(path: Path) -> LoreNote | None:
    name = str(path)
    if any(token in name for token in EXCLUDE):
        return None
    for note in SOURCE_NOTES:
        if note.marker in name:
            return note
    if "5E UA" in name and any(token in path.name for token in STRIXHAVEN):
        return LoreNote(
            "斯翠海文",
            "设定复核后，主题应读作 Arcavios 五大学院的校园魔法身份，而不是普通法师/术士/吟游诗人换皮。",
            "对齐度看机制是否把学院课程、社团身份和校园式协作/竞争落实到玩法。",
        )
    if path.name in {"精魂学院.md", "精魂学院（UA）.md", "死灵宗主.md", "死灵宗主（UA）.md"}:
        return LoreNote(
            "鸦阁",
            "设定复核后，主题应放入 Ravenloft 的恐怖类型、恐惧魔域、黑暗领主和逝者叙事中理解，而不是普通亡灵装饰。",
            "对齐度看机制是否把恐惧、通灵、亡者故事、黑暗契约或不死威压变成可见的桌面选择。",
        )
    if path.name == "月之术法.md":
        return LoreNote(
            "龙枪",
            "设定复核后，主题应落在 Krynn / Dragonlance 的三月、月相魔法和高阶巫术传统中理解。",
            "对齐度看机制是否把月相切换、三月神秘学和随月盈亏的法术节奏落实到实际资源循环。",
        )
    return None


def clean_previous_lore_sentence(reason: str) -> str:
    starts = (
        " 设定复核后应读作",
        " 机制是否贴合，按其能否把",
        " 设定复核后，它应被读成",
        " 对齐度看它是否",
        " 设定复核后，主题应落在",
        " 对齐度看能力是否",
        " 设定复核后，主题需要服务",
        " 对齐度看机制是否",
        " 设定复核后，主题应贴住",
        " 设定复核后，主题应放在",
        " 设定复核后，主题应服务",
        " 设定复核后，主题应尊重",
        " 设定复核后，主题应读作",
    )
    cut = len(reason)
    for start in starts:
        idx = reason.find(start)
        if idx != -1:
            cut = min(cut, idx)
    return reason[:cut].rstrip()


def update_design_table(text: str, note: LoreNote) -> str:
    lines = text.splitlines()
    in_table = False
    changed = False
    for i, line in enumerate(lines):
        if line.startswith("## 设计相关评分"):
            in_table = True
            continue
        if in_table and line.startswith("## ") and not line.startswith("## 设计相关评分"):
            break
        if not in_table or not line.startswith("|"):
            continue
        cells = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        row_name = cells[0]
        if row_name not in {"主题", "主题与能力关联度"}:
            continue
        reason = clean_previous_lore_sentence(cells[-1])
        if row_name == "主题":
            addition = note.theme
        else:
            addition = note.alignment
        cells[-1] = f"{reason} {addition}"
        lines[i] = "| " + " | ".join(cells) + " |"
        changed = True
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), changed


def write_lf(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main() -> None:
    changed_files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if path.name in {"README.md", "changelog.md"}:
            continue
        note = source_note(path)
        if note is None:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        updated, changed = update_design_table(text, note)
        if changed:
            write_lf(path, updated)
            changed_files.append(path)
    for path in changed_files:
        print(path)
    print(f"changed={len(changed_files)}")


if __name__ == "__main__":
    main()
