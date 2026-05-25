from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from .model import AssumptionVariant, DamageRoutine, DprCategory
from .reference import RANK_ORDER
from .report import RankedRoutineResult, rank_routine


DOMINANCE_RATIO_FOR_EX = 1.5
MIN_THRESHOLD_RANK_FOR_EX = "S"


@dataclass(frozen=True)
class CalibrationRow:
    level: int
    category: DprCategory
    option: str
    routine: str
    variant: AssumptionVariant
    assumptions: str
    calculation: str
    reference_cr: str
    reference_hp: float
    reference_ac: float
    reference_targets: int
    all_hit_damage: float
    expected_damage: float
    percent_hp: float
    threshold_rank: str
    dominance_ratio: float | None
    default_calibrated_rank: str
    ceiling_rank: str
    notes: str


def rank_index(rank: str) -> int:
    return RANK_ORDER.index(rank)


def is_rank_at_least(rank: str, minimum: str) -> bool:
    return rank_index(rank) <= rank_index(minimum)


def _option_name(routine: DamageRoutine) -> str:
    return routine.option_name or routine.name


def _assumptions(routine: DamageRoutine) -> str:
    if routine.variant == "default":
        return "默认优化：不计入特定稀有/珍稀/传奇魔法物品，不预设瘫痪等外部状态。"
    if routine.variant == "item_ceiling":
        return "物品上限：依赖特定魔法物品，仅用于上限比较，不改写默认评级。"
    return "状态上限：依赖目标已有关键状态或外部配合，仅用于上限说明。"


def _calculation(row: RankedRoutineResult) -> str:
    parts: list[str] = []
    for event in row.result.events:
        parts.append(f"{event.count}x {event.name}")
    for event in row.result.vex_events:
        parts.append(f"{event.count}x {event.name} (Vex chain)")
    for event in row.result.save_events:
        parts.append(f"{event.count}x {event.name} vs {event.target_count} targets")
    for event in row.result.direct_events:
        parts.append(f"{event.count}x {event.name}")
    for event in row.result.conditional_events:
        parts.append(f"{event.name} if trigger chance {event.trigger_chance:.3f}")
    for event in row.result.hit_pool_events:
        parts.append(f"{event.name}, {event.expected_spent_dice:.2f}/{event.dice_count} dice expected")
    for event in row.result.miss_reroll_events:
        parts.append(f"{event.name}, trigger chance {event.trigger_chance:.3f}")
    return "; ".join(parts)


def _format_notes(row: RankedRoutineResult) -> str:
    notes = list(row.result.notes)
    if row.routine.resources:
        notes.append(f"Resources: {', '.join(row.routine.resources)}")
    return " ".join(notes)


def _ranked_rows(routines: dict[str, DamageRoutine]) -> list[RankedRoutineResult]:
    rows: list[RankedRoutineResult] = []
    for routine in routines.values():
        if routine.exclude_from_calibration:
            continue
        rows.append(rank_routine(routine))
    return sorted(rows, key=lambda row: (row.level, row.category, row.routine.variant, -row.result.expected_damage, row.result.name))


def _dominance_pools(rows: list[RankedRoutineResult]) -> dict[tuple[int, DprCategory, AssumptionVariant], list[RankedRoutineResult]]:
    pools: dict[tuple[int, DprCategory, AssumptionVariant], list[RankedRoutineResult]] = {}
    for row in rows:
        if row.routine.variant == "condition_ceiling":
            continue
        key = (row.level, row.category, row.routine.variant)
        pools.setdefault(key, []).append(row)

        if row.routine.variant == "default":
            pools.setdefault((row.level, row.category, "item_ceiling"), []).append(row)

    for pool in pools.values():
        pool.sort(key=lambda row: row.result.expected_damage, reverse=True)
    return pools


def _dominance_ratio(row: RankedRoutineResult, pool: list[RankedRoutineResult] | None) -> float | None:
    if not pool or pool[0] is not row:
        return None
    if len(pool) < 2 or pool[1].result.expected_damage <= 0:
        return None
    return row.result.expected_damage / pool[1].result.expected_damage


def _calibrated_rank(row: RankedRoutineResult, dominance_ratio: float | None) -> str:
    if (
        dominance_ratio is not None
        and dominance_ratio >= DOMINANCE_RATIO_FOR_EX
        and is_rank_at_least(row.rank_pressure, MIN_THRESHOLD_RANK_FOR_EX)
    ):
        return "EX"
    return row.rank_pressure


def build_calibration_rows(routines: dict[str, DamageRoutine]) -> tuple[CalibrationRow, ...]:
    ranked = _ranked_rows(routines)
    pools = _dominance_pools(ranked)
    output: list[CalibrationRow] = []

    for row in ranked:
        routine = row.routine
        pool = None
        if routine.variant != "condition_ceiling":
            pool = pools.get((row.level, row.category, routine.variant))
        dominance = _dominance_ratio(row, pool)
        calibrated = _calibrated_rank(row, dominance)

        default_rank = calibrated if routine.variant == "default" else "-"
        ceiling_rank = calibrated if routine.variant != "default" else "-"
        if routine.variant == "condition_ceiling" and is_rank_at_least(row.rank_pressure, "EX"):
            ceiling_rank = "EX"

        output.append(
            CalibrationRow(
                level=row.level,
                category=row.category,
                option=_option_name(routine),
                routine=row.result.name,
                variant=routine.variant,
                assumptions=_assumptions(routine),
                calculation=_calculation(row),
                reference_cr=row.reference_cr,
                reference_hp=row.reference_hp,
                reference_ac=row.reference_ac,
                reference_targets=row.reference_targets,
                all_hit_damage=row.result.all_hit_damage,
                expected_damage=row.result.expected_damage,
                percent_hp=row.percent_hp,
                threshold_rank=row.rank_pressure,
                dominance_ratio=dominance,
                default_calibrated_rank=default_rank,
                ceiling_rank=ceiling_rank,
                notes=_format_notes(row),
            )
        )

    return tuple(output)


def markdown_matrix(rows: tuple[CalibrationRow, ...]) -> str:
    lines = [
        "# DPR Calibration Matrix",
        "",
        "> Generated calibration data. `阈值评级` is raw HP-percentage pressure; `默认校准评级` excludes specific rare/very rare/legendary item assumptions; `上限评级` is for item/condition ceiling branches only.",
        "",
        "## Calibration Rules",
        "",
        f"- EX is assigned by horizontal dominance, not by a fixed HP percentage. A row must be at least {MIN_THRESHOLD_RANK_FOR_EX} by threshold and at least {DOMINANCE_RATIO_FOR_EX:.1f}x the next comparable same-level/category row.",
        "- `幻影师护臂` is only an item-ceiling assumption. It can create EX ceiling evidence, but does not change default ranks.",
        "- Vex-derived benchmark rows are excluded from this matrix, although the calculator still supports Vex chains.",
        "- Great Weapon Master is modeled as per qualifying Attack-action hit. It is not applied to Polearm Master or Illusionist's Bracers bonus-action hits.",
        "- Great Weapon Fighting is modeled with the broad benchmark reading: eligible attack damage dice of 1-2 count as 3. This is table-sensitive when applied to rider dice.",
        "",
        "| Level | Category | Option | Variant | Routine | Ref CR | HP x Targets | AC | All-hit | Expected | % HP | 阈值评级 | Dominance | 默认校准评级 | 上限评级 | Assumptions |",
        "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|",
    ]
    for row in rows:
        dominance = "-" if row.dominance_ratio is None else f"{row.dominance_ratio:.2f}x"
        lines.append(
            "| "
            f"{row.level} | {row.category} | {row.option} | {row.variant} | {row.routine} | "
            f"{row.reference_cr} | {row.reference_hp:g} x {row.reference_targets} | {row.reference_ac:g} | "
            f"{row.all_hit_damage:.2f} | {row.expected_damage:.2f} | {row.percent_hp:.1f}% | "
            f"{row.threshold_rank} | {dominance} | {row.default_calibrated_rank} | {row.ceiling_rank} | {row.assumptions} |"
        )

    lines.extend(["", "## Calculation Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### Lv{row.level} {row.routine}",
                "",
                f"- Option: {row.option}",
                f"- Variant: {row.variant}",
                f"- Calculation: {row.calculation}",
                f"- Notes: {row.notes}" if row.notes else "- Notes: none",
                "",
            ]
        )
    return "\n".join(lines)


def write_matrix_reports(
    routines: dict[str, DamageRoutine],
    markdown_path: str = "loot/dpr-calibration-matrix.md",
    json_path: str = "loot/dpr-calibration-matrix.json",
) -> tuple[CalibrationRow, ...]:
    rows = build_calibration_rows(routines)
    md_path = Path(markdown_path)
    json_out = Path(json_path)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_out.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown_matrix(rows), encoding="utf-8")
    json_out.write_text(json.dumps([asdict(row) for row in rows], ensure_ascii=False, indent=2), encoding="utf-8")
    return rows
