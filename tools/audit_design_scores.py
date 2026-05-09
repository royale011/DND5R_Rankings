from __future__ import annotations

import collections
import pathlib
import re


ROOT = pathlib.Path("Rankings")


def iter_review_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for path in ROOT.rglob("*.md"):
        if "Archive" in path.parts:
            continue
        if path.name.lower() == "changelog.md":
            continue
        files.append(path)
    return sorted(files)


def extract_design_rows(text: str) -> list[tuple[str, str, str]]:
    match = re.search(r"## 设计相关评分\s*(.*?)(?=\n## |\Z)", text, re.S)
    if not match:
        return []

    rows: list[tuple[str, str, str]] = []
    for line in match.group(1).splitlines():
        if not line.startswith("|"):
            continue
        if line.startswith("|---"):
            continue
        cols = [col.strip() for col in line.strip().strip("|").split("|")]
        if len(cols) >= 3:
            if cols[0] in {"项目", "设计项"} or cols[1] in {"评分", "等级"}:
                continue
            rows.append((cols[0], cols[1], cols[2]))
    return rows


def main() -> None:
    file_rows: dict[pathlib.Path, list[tuple[str, str, str]]] = {}
    for path in iter_review_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        rows = extract_design_rows(text)
        if rows:
            file_rows[path] = rows

    same_design_feature: list[pathlib.Path] = []
    malformed: list[tuple[pathlib.Path, list[str]]] = []
    all_reasons: list[tuple[pathlib.Path, str, str, str]] = []
    for path, rows in file_rows.items():
        by_item = {item: (rank, reason) for item, rank, reason in rows}
        items = [item for item, _, _ in rows]
        expected = {"设计质量", "主题", "能力设计质量", "主题与能力关联度"}
        if set(items) != expected or len(items) != 4:
            malformed.append((path, items))
        if (
            "设计质量" in by_item
            and "能力设计质量" in by_item
            and by_item["设计质量"][1] == by_item["能力设计质量"][1]
        ):
            same_design_feature.append(path)
        for item, rank, reason in rows:
            all_reasons.append((path, item, rank, reason))

    print(f"Design-score files: {len(file_rows)}")
    print(f"Rows: {len(all_reasons)}")
    print(f"Malformed design tables: {len(malformed)}")
    for path, items in malformed:
        print(f"MALFORMED\t{path}\t{items}")
    print(f"Same 设计质量 / 能力设计质量 reason: {len(same_design_feature)}")
    for path in same_design_feature:
        print(f"SAME\t{path}")

    print("\nRepeated reasons:")
    counter = collections.Counter(reason for _, _, _, reason in all_reasons)
    for reason, count in counter.most_common():
        if count <= 1:
            break
        print(f"{count}\t{reason}")


if __name__ == "__main__":
    main()
