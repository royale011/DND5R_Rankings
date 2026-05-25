from __future__ import annotations

from dataclasses import dataclass

from .calculator import RoutineResult, calculate_routine
from .model import DamageRoutine, DprCategory
from .reference import rank_for_percent, reference_for


@dataclass(frozen=True)
class RankedRoutineResult:
    routine: DamageRoutine
    result: RoutineResult
    category: DprCategory
    level: int
    reference_cr: str
    reference_hp: float
    reference_ac: float
    reference_targets: int
    percent_hp: float
    rank_pressure: str


def rank_routine(routine: DamageRoutine, level: int | None = None, category: DprCategory | None = None) -> RankedRoutineResult:
    actual_level = level if level is not None else routine.level
    actual_category = category if category is not None else routine.category
    if actual_level is None:
        raise ValueError(f"Routine {routine.name!r} has no level.")
    if actual_category is None:
        raise ValueError(f"Routine {routine.name!r} has no DPR category.")

    result = calculate_routine(routine)
    _, cr_stats, target_count = reference_for(actual_level, actual_category)
    denominator = cr_stats.median_hp * target_count
    percent_hp = result.expected_damage / denominator * 100 if denominator else 0
    return RankedRoutineResult(
        routine=routine,
        result=result,
        category=actual_category,
        level=actual_level,
        reference_cr=cr_stats.cr,
        reference_hp=cr_stats.median_hp,
        reference_ac=cr_stats.median_ac,
        reference_targets=target_count,
        percent_hp=percent_hp,
        rank_pressure=rank_for_percent(actual_category, percent_hp),
    )


def markdown_report(rows: tuple[RankedRoutineResult, ...]) -> str:
    lines = [
        "# DPR Calculated Benchmarks",
        "",
        "> Generated report. Treat `rank_pressure` as math pressure, not final review rank.",
        "",
        "| Level | Category | Routine | Ref CR | Ref HP x Targets | AC | All-hit | Expected | % HP | Rank pressure | Setup | Recovery |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        result = row.result
        lines.append(
            "| "
            f"{row.level} | {row.category} | {result.name} | {row.reference_cr} | "
            f"{row.reference_hp:g} x {row.reference_targets} | {row.reference_ac:g} | "
            f"{result.all_hit_damage:.2f} | {result.expected_damage:.2f} | "
            f"{row.percent_hp:.1f}% | {row.rank_pressure} | {result.burst_window}: {result.setup} | {result.recovery} |"
        )
    lines.extend(["", "## Event Details", ""])
    for row in rows:
        lines.append(f"### Lv{row.level} {row.result.name}")
        lines.append("")
        for event in row.result.events:
            lines.append(
                f"- {event.name}: count={event.count}, hit={event.hit_chance:.3f}, miss={event.miss_chance:.3f}, "
                f"crit={event.crit_chance:.3f}, crit_min={event.crit_min}, crit_on_hit={event.crit_on_hit}, "
                f"miss_damage={event.miss_damage:.2f}, "
                f"all-hit={event.all_hit_damage:.2f}, "
                f"expected={event.expected_damage:.2f}"
            )
        for event in row.result.vex_events:
            lines.append(
                f"- {event.name}: Vex chain count={event.count}, "
                f"normal hit/crit={event.normal_hit_chance:.3f}/{event.normal_crit_chance:.3f}, "
                f"adv hit/crit={event.advantage_hit_chance:.3f}/{event.advantage_crit_chance:.3f}, "
                f"crit_min={event.crit_min}, crit_on_hit={event.crit_on_hit}, "
                f"all-hit={event.all_hit_damage:.2f}, expected={event.expected_damage:.2f}"
            )
        for event in row.result.save_events:
            lines.append(
                f"- {event.name}: count={event.count}, targets={event.target_count}, "
                f"fail={event.fail_chance:.3f}, all-failed={event.all_failed_damage:.2f}, "
                f"expected={event.expected_damage:.2f}"
            )
        for event in row.result.direct_events:
            lines.append(
                f"- {event.name}: count={event.count}, targets={event.target_count}, "
                f"damage={event.damage:.2f}"
            )
        for event in row.result.conditional_events:
            lines.append(
                f"- {event.name}: trigger={event.trigger_chance:.3f}, targets={event.target_count}, "
                f"all-triggered={event.all_triggered_damage:.2f}, expected={event.expected_damage:.2f}"
            )
        for event in row.result.hit_pool_events:
            lines.append(
                f"- {event.name}: dice={event.dice_count}, spent={event.expected_spent_dice:.2f} expected/"
                f"{event.all_spent_dice} all-hit, all-hit={event.all_hit_damage:.2f}, "
                f"expected={event.expected_damage:.2f}"
            )
        for event in row.result.miss_reroll_events:
            lines.append(
                f"- {event.name}: uses={event.uses}, trigger={event.trigger_chance:.3f}, "
                f"all-hit={event.all_hit_damage:.2f}, expected={event.expected_damage:.2f}"
            )
        if row.result.resources:
            lines.append(f"- Resources: {', '.join(row.result.resources)}")
        for note in row.result.notes:
            lines.append(f"- Note: {note}")
        lines.append("")
    return "\n".join(lines)
