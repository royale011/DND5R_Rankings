from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RANKINGS = ROOT / "Rankings"

TIER_LABELS = ["Tier 1（1-4）", "Tier 2（5-10）", "Tier 3（11-16）", "Tier 4（17-20）"]
TIER_SHORT = ["T1", "T2", "T3", "T4"]
RANK_ORDER = ["S+", "S", "S-", "A+", "A", "A-", "B+", "B", "C", "D", "E", "E-", "F"]
SUMMARY_FILE = "README.md"


def write_utf8_lf(path: Path, text: str) -> None:
    path.write_bytes((text.rstrip() + "\n").encode("utf-8"))
NON_FIRST_PARTY_BASE_CLASSES = {"灵能使"}


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
    out = [
        f"## {title}",
    ]
    for idx, tier in enumerate(TIER_LABELS):
        out.extend([
            "",
            f"### {tier}",
            "",
            "| 阶段 | 评级 | 子职 | 具体理由 |",
            "|---|---|---|---|",
        ])
        tier_entries: list[tuple[str, str, str]] = []
        for name, rows in entries.items():
            rank, reason = rows[idx]
            tier_entries.append((rank, name, reason))
        tier_entries.sort(key=lambda item: (RANK_ORDER.index(item[0]), item[1]))
        for rank, name, reason in tier_entries:
            out.append(f"| {TIER_SHORT[idx]} | {rank} | {name} | {reason} |")
    return "\n".join(out).rstrip()


def class_dirs() -> list[str]:
    names: list[str] = []
    for path in sorted(RANKINGS.iterdir(), key=lambda p: p.name):
        if not path.is_dir() or path.name == "构筑":
            continue
        if (path / SUMMARY_FILE).exists():
            names.append(path.name)
    return names


def rebuild_class(class_name: str) -> None:
    class_dir = RANKINGS / class_name
    summary = class_dir / SUMMARY_FILE
    if not summary.exists():
        raise FileNotFoundError(summary)

    official: dict[str, list[tuple[str, str]]] = {}
    non_first: dict[str, list[tuple[str, str]]] = {}

    for path in sorted(class_dir.glob("*.md"), key=lambda p: p.name):
        if path.name == SUMMARY_FILE:
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
        if not non_first_party or egw_exception or class_name in NON_FIRST_PARTY_BASE_CLASSES:
            official[stem] = rows

    replacement = render_leaderboard("分阶段子职排行榜", official)
    if non_first and class_name not in NON_FIRST_PARTY_BASE_CLASSES:
        replacement += "\n\n" + render_leaderboard("UA/合作方/第三方子职分阶段排行榜", non_first)
    replacement += "\n\n"

    text = summary.read_text(encoding="utf-8")
    start = text.find("## 分阶段子职排行榜")
    search_from = start if start >= 0 else 0
    design = text.find("## 设计相关评分", search_from)
    if design < 0 and start >= 0:
        write_utf8_lf(summary, text[:start].rstrip() + "\n\n" + replacement)
        return
    if design < 0:
        raise ValueError(f"{summary} missing 设计相关评分 after leaderboard")
    if start < 0:
        write_utf8_lf(summary, text[:design] + replacement + text[design:])
    else:
        write_utf8_lf(summary, text[:start] + replacement + text[design:])


def main() -> None:
    for class_name in class_dirs():
        rebuild_class(class_name)


if __name__ == "__main__":
    main()
