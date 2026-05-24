from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .benchmarks import all_routines
from .core.matrix import build_calibration_rows, markdown_matrix, write_matrix_reports
from .core.model import DprCategory
from .core.report import markdown_report, rank_routine


CATEGORIES: tuple[DprCategory, ...] = (
    "close_burst",
    "close_sustained",
    "close_aoe",
    "ranged_burst",
    "ranged_sustained",
    "ranged_aoe",
)


def _parse_levels(value: str) -> set[int]:
    levels: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            levels.update(range(int(start), int(end) + 1))
        else:
            levels.add(int(part))
    return levels


def _rows(levels: set[int] | None = None, routine_id: str | None = None, category: str | None = None, level_override: int | None = None):
    routines = all_routines()
    if routine_id:
        if routine_id not in routines:
            known = ", ".join(sorted(routines))
            raise SystemExit(f"Unknown routine id: {routine_id}\nKnown routines: {known}")
        routines = {routine_id: routines[routine_id]}
    rows = []
    for routine in routines.values():
        actual_level = level_override if level_override is not None else routine.level
        actual_category = routine.category
        if levels is not None and actual_level not in levels:
            continue
        if category not in (None, "all") and actual_category != category:
            continue
        rows.append(rank_routine(routine, level=actual_level))
    return tuple(sorted(rows, key=lambda row: (row.level, row.category, row.result.name)))


def _print_json(rows) -> None:
    print(json.dumps([asdict(row) for row in rows], ensure_ascii=False, indent=2))


def _print_markdown(rows, out: str | None = None) -> None:
    text = markdown_report(rows)
    if out:
        path = Path(out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path}")
    else:
        print(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="DPR benchmark calculator for ranking calibration.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    routine_parser = subparsers.add_parser("routine", help="Calculate one routine by id.")
    routine_parser.add_argument("routine_id")
    routine_parser.add_argument("--level", type=int, default=None, help="Override the routine's default level reference.")
    routine_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")

    benchmark_parser = subparsers.add_parser("benchmark", help="Calculate benchmark routines.")
    benchmark_parser.add_argument("--levels", default=None, help="Level filter, e.g. 5,9,13-20.")
    benchmark_parser.add_argument("--category", choices=("all", *CATEGORIES), default="all")
    benchmark_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")

    report_parser = subparsers.add_parser("report", help="Write a markdown benchmark report.")
    report_parser.add_argument("--levels", default=None, help="Level filter, e.g. 5,9,13-20.")
    report_parser.add_argument("--category", choices=("all", *CATEGORIES), default="all")
    report_parser.add_argument("--out", default="loot/dpr-calculated-benchmarks.md")

    matrix_parser = subparsers.add_parser("matrix", help="Write the default/item/condition DPR calibration matrix.")
    matrix_parser.add_argument("--out", default="loot/dpr-calibration-matrix.md")
    matrix_parser.add_argument("--json-out", default="loot/dpr-calibration-matrix.json")
    matrix_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")

    args = parser.parse_args()
    levels = _parse_levels(args.levels) if getattr(args, "levels", None) else None

    if args.command == "routine":
        rows = _rows(routine_id=args.routine_id, level_override=args.level)
        _print_json(rows) if args.format == "json" else _print_markdown(rows)
    elif args.command == "benchmark":
        rows = _rows(levels=levels, category=args.category)
        _print_json(rows) if args.format == "json" else _print_markdown(rows)
    elif args.command == "report":
        _print_markdown(_rows(levels=levels, category=args.category), args.out)
    elif args.command == "matrix":
        if args.format == "json":
            rows = build_calibration_rows(all_routines())
            print(json.dumps([asdict(row) for row in rows], ensure_ascii=False, indent=2))
        else:
            write_matrix_reports(all_routines(), markdown_path=args.out, json_path=args.json_out)
            print(f"Wrote {args.out}")
            print(f"Wrote {args.json_out}")


if __name__ == "__main__":
    main()
