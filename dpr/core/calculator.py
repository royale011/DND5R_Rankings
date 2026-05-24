from __future__ import annotations

from dataclasses import dataclass

from .model import AttackEvent, DamageRoutine


@dataclass(frozen=True)
class EventResult:
    name: str
    count: int
    hit_chance: float
    crit_chance: float
    all_hit_damage: float
    expected_damage: float


@dataclass(frozen=True)
class RoutineResult:
    name: str
    all_hit_damage: float
    expected_damage: float
    range_band: str
    burst_window: str
    recovery: str
    setup: str
    resources: tuple[str, ...]
    events: tuple[EventResult, ...]
    notes: tuple[str, ...]


def _single_roll_probs(attack_bonus: int, target_ac: int) -> tuple[float, float]:
    hits = 0
    crits = 0
    for roll in range(1, 21):
        if roll == 20:
            hits += 1
            crits += 1
        elif roll != 1 and roll + attack_bonus >= target_ac:
            hits += 1
    return hits / 20, crits / 20


def _advantage_probs(attack_bonus: int, target_ac: int) -> tuple[float, float]:
    hits = 0
    crits = 0
    total = 20 * 20
    for a in range(1, 21):
        for b in range(1, 21):
            roll = max(a, b)
            if roll == 20:
                hits += 1
                crits += 1
            elif roll != 1 and roll + attack_bonus >= target_ac:
                hits += 1
    return hits / total, crits / total


def _disadvantage_probs(attack_bonus: int, target_ac: int) -> tuple[float, float]:
    hits = 0
    crits = 0
    total = 20 * 20
    for a in range(1, 21):
        for b in range(1, 21):
            roll = min(a, b)
            if roll == 20:
                hits += 1
                crits += 1
            elif roll != 1 and roll + attack_bonus >= target_ac:
                hits += 1
    return hits / total, crits / total


def hit_and_crit_chance(event: AttackEvent) -> tuple[float, float]:
    if event.advantage == "advantage":
        return _advantage_probs(event.attack_bonus, event.target_ac)
    if event.advantage == "disadvantage":
        return _disadvantage_probs(event.attack_bonus, event.target_ac)
    return _single_roll_probs(event.attack_bonus, event.target_ac)


def calculate_event(event: AttackEvent) -> EventResult:
    hit_chance, crit_chance = hit_and_crit_chance(event)
    dice_average = sum(d.average for d in event.damage)
    crit_extra = sum(d.average for d in event.damage if d.crit_doubles)
    normal_hit_damage = dice_average + event.flat_damage
    expected_per_attack = hit_chance * normal_hit_damage + crit_chance * crit_extra
    all_hit_per_attack = normal_hit_damage
    return EventResult(
        name=event.name,
        count=event.count,
        hit_chance=hit_chance,
        crit_chance=crit_chance,
        all_hit_damage=event.count * all_hit_per_attack,
        expected_damage=event.count * expected_per_attack,
    )


def calculate_routine(routine: DamageRoutine) -> RoutineResult:
    events = tuple(calculate_event(event) for event in routine.events)
    return RoutineResult(
        name=routine.name,
        all_hit_damage=sum(event.all_hit_damage for event in events),
        expected_damage=sum(event.expected_damage for event in events),
        range_band=routine.range_band,
        burst_window=routine.burst_window,
        recovery=routine.recovery,
        setup=routine.setup,
        resources=routine.resources,
        events=events,
        notes=routine.notes,
    )

