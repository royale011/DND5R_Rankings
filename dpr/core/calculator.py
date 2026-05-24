from __future__ import annotations

from dataclasses import dataclass

from .model import AttackEvent, ConditionalDamageEvent, DamageRoutine, DirectDamageEvent, SaveEvent, VexChainEvent


@dataclass(frozen=True)
class EventResult:
    name: str
    count: int
    hit_chance: float
    miss_chance: float
    crit_chance: float
    crit_min: int
    crit_on_hit: bool
    miss_damage: float
    all_hit_damage: float
    expected_damage: float


@dataclass(frozen=True)
class VexChainResult:
    name: str
    count: int
    normal_hit_chance: float
    advantage_hit_chance: float
    normal_crit_chance: float
    advantage_crit_chance: float
    crit_min: int
    crit_on_hit: bool
    all_hit_damage: float
    expected_damage: float


@dataclass(frozen=True)
class SaveEventResult:
    name: str
    count: int
    target_count: int
    fail_chance: float
    all_failed_damage: float
    expected_damage: float


@dataclass(frozen=True)
class DirectEventResult:
    name: str
    count: int
    target_count: int
    damage: float


@dataclass(frozen=True)
class ConditionalEventResult:
    name: str
    trigger_chance: float
    target_count: int
    all_triggered_damage: float
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
    vex_events: tuple[VexChainResult, ...]
    save_events: tuple[SaveEventResult, ...]
    direct_events: tuple[DirectEventResult, ...]
    conditional_events: tuple[ConditionalEventResult, ...]
    notes: tuple[str, ...]


def _is_hit_and_crit(
    roll: int,
    attack_bonus: int,
    target_ac: int,
    crit_min: int,
    crit_on_hit: bool = False,
) -> tuple[bool, bool]:
    if roll == 20:
        return True, True
    if roll == 1:
        return False, False
    hit = roll + attack_bonus >= target_ac
    return hit, hit and (crit_on_hit or roll >= crit_min)


def _single_roll_probs(
    attack_bonus: int,
    target_ac: int,
    crit_min: int = 20,
    crit_on_hit: bool = False,
) -> tuple[float, float]:
    hits = 0
    crits = 0
    for roll in range(1, 21):
        hit, crit = _is_hit_and_crit(roll, attack_bonus, target_ac, crit_min, crit_on_hit)
        if hit:
            hits += 1
        if crit:
            crits += 1
    return hits / 20, crits / 20


def _advantage_probs(
    attack_bonus: int,
    target_ac: int,
    crit_min: int = 20,
    crit_on_hit: bool = False,
) -> tuple[float, float]:
    hits = 0
    crits = 0
    total = 20 * 20
    for a in range(1, 21):
        for b in range(1, 21):
            roll = max(a, b)
            hit, crit = _is_hit_and_crit(roll, attack_bonus, target_ac, crit_min, crit_on_hit)
            if hit:
                hits += 1
            if crit:
                crits += 1
    return hits / total, crits / total


def _disadvantage_probs(
    attack_bonus: int,
    target_ac: int,
    crit_min: int = 20,
    crit_on_hit: bool = False,
) -> tuple[float, float]:
    hits = 0
    crits = 0
    total = 20 * 20
    for a in range(1, 21):
        for b in range(1, 21):
            roll = min(a, b)
            hit, crit = _is_hit_and_crit(roll, attack_bonus, target_ac, crit_min, crit_on_hit)
            if hit:
                hits += 1
            if crit:
                crits += 1
    return hits / total, crits / total


def hit_and_crit_chance(event: AttackEvent) -> tuple[float, float]:
    if event.advantage == "advantage":
        return _advantage_probs(event.attack_bonus, event.target_ac, event.crit_min, event.crit_on_hit)
    if event.advantage == "disadvantage":
        return _disadvantage_probs(event.attack_bonus, event.target_ac, event.crit_min, event.crit_on_hit)
    return _single_roll_probs(event.attack_bonus, event.target_ac, event.crit_min, event.crit_on_hit)


def calculate_event(event: AttackEvent) -> EventResult:
    hit_chance, crit_chance = hit_and_crit_chance(event)
    miss_chance = 1 - hit_chance
    dice_average = sum(d.average for d in event.damage)
    crit_extra = sum(d.average for d in event.damage if d.crit_doubles)
    normal_hit_damage = dice_average + event.flat_damage
    expected_per_attack = hit_chance * normal_hit_damage + crit_chance * crit_extra + miss_chance * event.miss_damage
    all_hit_per_attack = normal_hit_damage + crit_extra if event.crit_on_hit else normal_hit_damage
    return EventResult(
        name=event.name,
        count=event.count,
        hit_chance=hit_chance,
        miss_chance=miss_chance,
        crit_chance=crit_chance,
        crit_min=event.crit_min,
        crit_on_hit=event.crit_on_hit,
        miss_damage=event.miss_damage,
        all_hit_damage=event.count * all_hit_per_attack,
        expected_damage=event.count * expected_per_attack,
    )


def _expected_per_attack(
    hit_chance: float,
    crit_chance: float,
    dice_average: float,
    crit_extra: float,
    flat_damage: float,
) -> float:
    return hit_chance * (dice_average + flat_damage) + crit_chance * crit_extra


def calculate_vex_chain_event(event: VexChainEvent) -> VexChainResult:
    normal_hit, normal_crit = _single_roll_probs(event.attack_bonus, event.target_ac, event.crit_min, event.crit_on_hit)
    advantage_hit, advantage_crit = _advantage_probs(event.attack_bonus, event.target_ac, event.crit_min, event.crit_on_hit)
    dice_average = sum(d.average for d in event.damage)
    crit_extra = sum(d.average for d in event.damage if d.crit_doubles)
    all_hit_per_attack = dice_average + event.flat_damage
    normal_expected = _expected_per_attack(normal_hit, normal_crit, dice_average, crit_extra, event.flat_damage)
    advantage_expected = _expected_per_attack(advantage_hit, advantage_crit, dice_average, crit_extra, event.flat_damage)

    advantage_state = 1.0 if event.initial_advantage else 0.0
    expected_damage = 0.0
    for _ in range(event.count):
        expected_damage += advantage_state * advantage_expected + (1 - advantage_state) * normal_expected
        advantage_state = advantage_state * advantage_hit + (1 - advantage_state) * normal_hit

    return VexChainResult(
        name=event.name,
        count=event.count,
        normal_hit_chance=normal_hit,
        advantage_hit_chance=advantage_hit,
        normal_crit_chance=normal_crit,
        advantage_crit_chance=advantage_crit,
        crit_min=event.crit_min,
        crit_on_hit=event.crit_on_hit,
        all_hit_damage=event.count * all_hit_per_attack,
        expected_damage=expected_damage,
    )


def save_fail_chance(save_dc: int, save_bonus: float) -> float:
    failures = 0
    for roll in range(1, 21):
        if roll + save_bonus < save_dc:
            failures += 1
    return failures / 20


def calculate_save_event(event: SaveEvent) -> SaveEventResult:
    fail_chance = save_fail_chance(event.save_dc, event.save_bonus)
    full_damage = sum(d.average for d in event.damage) + event.flat_damage
    success_damage = full_damage / 2 if event.on_success == "half" else 0
    expected_per_target = fail_chance * full_damage + (1 - fail_chance) * success_damage
    multiplier = event.count * event.target_count
    return SaveEventResult(
        name=event.name,
        count=event.count,
        target_count=event.target_count,
        fail_chance=fail_chance,
        all_failed_damage=multiplier * full_damage,
        expected_damage=multiplier * expected_per_target,
    )


def calculate_direct_event(event: DirectDamageEvent) -> DirectEventResult:
    damage = (sum(d.average for d in event.damage) + event.flat_damage) * event.count * event.target_count
    return DirectEventResult(
        name=event.name,
        count=event.count,
        target_count=event.target_count,
        damage=damage,
    )


def calculate_conditional_event(
    event: ConditionalDamageEvent,
    attack_results_by_name: dict[str, EventResult],
) -> ConditionalEventResult:
    miss_all = 1.0
    for name in event.trigger_event_names:
        result = attack_results_by_name[name]
        miss_all *= result.miss_chance ** result.count
    trigger_chance = 1 - miss_all
    damage = (sum(d.average for d in event.damage) + event.flat_damage) * event.target_count
    return ConditionalEventResult(
        name=event.name,
        trigger_chance=trigger_chance,
        target_count=event.target_count,
        all_triggered_damage=damage,
        expected_damage=trigger_chance * damage,
    )


def calculate_routine(routine: DamageRoutine) -> RoutineResult:
    events = tuple(calculate_event(event) for event in routine.events)
    attack_results_by_name = {event.name: event for event in events}
    vex_events = tuple(calculate_vex_chain_event(event) for event in routine.vex_events)
    save_events = tuple(calculate_save_event(event) for event in routine.save_events)
    direct_events = tuple(calculate_direct_event(event) for event in routine.direct_events)
    conditional_events = tuple(calculate_conditional_event(event, attack_results_by_name) for event in routine.conditional_events)
    return RoutineResult(
        name=routine.name,
        all_hit_damage=sum(event.all_hit_damage for event in events)
        + sum(event.all_hit_damage for event in vex_events)
        + sum(event.all_failed_damage for event in save_events)
        + sum(event.damage for event in direct_events)
        + sum(event.all_triggered_damage for event in conditional_events),
        expected_damage=sum(event.expected_damage for event in events)
        + sum(event.expected_damage for event in vex_events)
        + sum(event.expected_damage for event in save_events)
        + sum(event.damage for event in direct_events)
        + sum(event.expected_damage for event in conditional_events),
        range_band=routine.range_band,
        burst_window=routine.burst_window,
        recovery=routine.recovery,
        setup=routine.setup,
        resources=routine.resources,
        events=events,
        vex_events=vex_events,
        save_events=save_events,
        direct_events=direct_events,
        conditional_events=conditional_events,
        notes=routine.notes,
    )
