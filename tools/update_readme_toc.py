from __future__ import annotations

import re
import subprocess
from pathlib import Path


TOC_TITLE = "## 目录"


def slugify(text: str, used: dict[str, int]) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text).strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    if not text:
        text = "section"
    count = used.get(text, 0)
    used[text] = count + 1
    if count:
        return f"{text}-{count}"
    return text


def build_toc(markdown: str) -> str:
    headings: list[tuple[int, str]] = []
    in_fence = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
        if not match:
            continue
        title = match.group(2).strip()
        if title == "目录":
            continue
        headings.append((len(match.group(1)), title))

    used: dict[str, int] = {}
    lines = [TOC_TITLE, ""]
    for level, title in headings:
        indent = "  " * (level - 2)
        lines.append(f"{indent}- [{title}](#{slugify(title, used)})")
    return "\n".join(lines).rstrip()


def strip_existing_toc(markdown: str) -> str:
    pattern = re.compile(r"\n## 目录\n.*?(?=\n## (?!目录)|\Z)", re.S)
    return pattern.sub("", markdown).strip() + "\n"


def add_or_update_toc(markdown: str) -> str:
    markdown = strip_existing_toc(markdown)
    toc = build_toc(markdown)
    if toc == TOC_TITLE:
        return markdown

    match = re.search(r"\n## (?!目录)", markdown)
    if not match:
        return markdown.rstrip() + "\n\n" + toc + "\n"
    insert_at = match.start()
    updated = markdown[:insert_at].rstrip() + "\n\n" + toc + "\n\n" + markdown[insert_at + 1 :].lstrip()
    return updated.rstrip() + "\n"


def tracked_readmes() -> list[Path]:
    output = subprocess.check_output(
        ["git", "-c", "core.quotePath=false", "ls-files", "*README.md"],
        text=True,
        encoding="utf-8",
    )
    return [Path(line) for line in output.splitlines() if line.strip()]


def tracked_ranking_markdown() -> list[Path]:
    output = subprocess.check_output(
        ["git", "-c", "core.quotePath=false", "ls-files", "Rankings/*.md", "Rankings/**/*.md"],
        text=True,
        encoding="utf-8",
    )
    paths: list[Path] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        path = Path(line)
        if path.name == "changelog.md" or "Archive" in path.parts:
            continue
        paths.append(path)
    return paths


def active_homebrew_markdown() -> list[Path]:
    root = Path("homebrews") / "Rankings"
    if not root.exists():
        return []
    paths: list[Path] = []
    for path in root.rglob("*.md"):
        if path.name == "changelog.md" or "Archive" in path.parts:
            continue
        paths.append(path)
    return paths


def main() -> None:
    seen: set[Path] = set()
    paths = tracked_readmes() + tracked_ranking_markdown() + active_homebrew_markdown()
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated = add_or_update_toc(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
