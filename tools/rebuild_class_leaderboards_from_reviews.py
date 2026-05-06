from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RANKINGS = ROOT / "Rankings"

CLASS_DIRS = ["野蛮人", "战士", "武僧", "游荡者", "圣武士", "游侠", "牧师", "吟游诗人", "魔契师", "术士", "法师", "德鲁伊", "奇械师"]
TIER_LABELS = ["Tier 1（1-4）", "Tier 2（5-10）", "Tier 3（11-16）", "Tier 4（17-20）"]
RANK_ORDER = ["S+", "S", "A", "B", "C", "D", "E", "E-", "F"]


def split_row(line: str) -> list[str]:
    line = line.strip()
    if not (line.startswith("|") and line.endswith("|")):
        return []
    return [part.strip() for part in line.strip("|").split("|")]


def extract_overall(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    marker = "## 综合评分"
    if marker not in text:
        raise ValueError(f"{path} missing {marker}")
    section = text.split(marker, 1)[1]
    next_heading = re.search(r"\n## ", section)
    if next_heading:
        section = section[:next_heading.start()]
    rows: list[tuple[str, str]] = []
    for line in section.splitlines():
        parts = split_row(line)
        if len(parts) < 3:
            continue
        if parts[0] in ("阶段", "---") or parts[0].startswith("---"):
            continue
        if parts[0] in TIER_LABELS:
            rows.append((parts[1], parts[2]))
    if len(rows) != 4:
        raise ValueError(f"{path} has {len(rows)} 综合评分 rows, expected 4")
    return rows


def is_non_first_party(stem: str) -> bool:
    if "（" not in stem or "）" not in stem:
        return False
    # Source markers are mandatory for UA / partner / third-party files in this project.
    # First-party official / official legacy files are intentionally unmarked.
    return True


def render_leaderboard(title: str, entries: dict[str, list[tuple[str, str]]]) -> str:
    out = [f"## {title}", ""]
    for idx, tier in enumerate(TIER_LABELS):
        out.append(f"{tier}:")
        buckets: dict[str, list[tuple[str, str]]] = {}
        for name, rows in entries.items():
            rank, reason = rows[idx]
            buckets.setdefault(rank, []).append((name, reason))
        for rank in RANK_ORDER:
            if rank not in buckets:
                continue
            out.append(f"- {rank}:")
            for name, reason in buckets[rank]:
                out.append(f"  - {name}：{reason}")
        out.append("")
    return "\n".join(out).rstrip()


def rebuild_class(class_name: str) -> None:
    class_dir = RANKINGS / class_name
    summary = class_dir / "0x总评.md"
    if not summary.exists():
        raise FileNotFoundError(summary)

    official: dict[str, list[tuple[str, str]]] = {}
    non_first: dict[str, list[tuple[str, str]]] = {}

    for path in sorted(class_dir.glob("*.md"), key=lambda p: p.name):
        if path.name == "0x总评.md":
            continue
        stem = path.stem
        non_first_party = is_non_first_party(stem)
        try:
            rows = extract_overall(path)
        except ValueError:
            if non_first_party:
                # Some older partner/third-party files may only have the legacy
                # horizontal summary until that source group is revisited.
                # Official first-party files remain strict.
                continue
            raise
        if non_first_party:
            non_first[stem] = rows
        egw_exception = (
            (class_name == "战士" and stem == "回音骑士（EGW）")
            or (class_name == "法师" and stem in {"时间魔法（EGW）", "重力魔法（EGW）"})
        )
        if not non_first_party or egw_exception:
            official[stem] = rows

    replacement = render_leaderboard("分阶段子职排行榜", official)
    if non_first:
        replacement += "\n\n" + render_leaderboard("UA/合作方/第三方子职分阶段排行榜", non_first)
    replacement += "\n\n"

    text = summary.read_text(encoding="utf-8")
    start = text.find("## 分阶段子职排行榜")
    search_from = start if start >= 0 else 0
    design = text.find("## 设计相关评分", search_from)
    if design < 0 and start >= 0:
        summary.write_text(text[:start].rstrip() + "\n\n" + replacement, encoding="utf-8")
        return
    if design < 0:
        raise ValueError(f"{summary} missing 设计相关评分 after leaderboard")
    if start < 0:
        summary.write_text(text[:design] + replacement + text[design:], encoding="utf-8")
    else:
        summary.write_text(text[:start] + replacement + text[design:], encoding="utf-8")


def main() -> None:
    for class_name in CLASS_DIRS:
        rebuild_class(class_name)


if __name__ == "__main__":
    main()
