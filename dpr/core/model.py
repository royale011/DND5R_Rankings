from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


AdvantageState = Literal["normal", "advantage", "disadvantage"]
BurstWindow = Literal["cold_start", "prebuffed", "setup_amortized", "sustained"]
Recovery = Literal["long_rest", "short_rest", "encounter_low_cost", "sustained", "at_will"]
SaveOutcome = Literal["half", "none"]
DprCategory = Literal[
    "close_burst",
    "close_sustained",
    "close_aoe",
    "ranged_burst",
    "ranged_sustained",
    "ranged_aoe",
]
AssumptionVariant = Literal["default", "item_ceiling", "condition_ceiling"]


@dataclass(frozen=True)
class DamageDice:
    """A group of dice in a damage expression."""

    count: int
    sides: int
    crit_doubles: bool = True
    label: str = ""

    @property
    def average(self) -> float:
        return self.count * (self.sides + 1) / 2


@dataclass(frozen=True)
class AttackEvent:
    """Repeated attack roll event with the same damage and hit math."""

    name: str
    count: int
    attack_bonus: int
    damage: tuple[DamageDice, ...] = ()
    flat_damage: float = 0.0
    advantage: AdvantageState = "normal"
    target_ac: int = 19
    crit_min: int = 20
    crit_on_hit: bool = False
    miss_damage: float = 0.0


@dataclass(frozen=True)
class VexChainEvent:
    """Sequential Vex attacks where each hit grants Advantage to the next attack."""

    name: str
    count: int
    attack_bonus: int
    damage: tuple[DamageDice, ...] = ()
    flat_damage: float = 0.0
    target_ac: int = 19
    crit_min: int = 20
    crit_on_hit: bool = False
    initial_advantage: bool = False


@dataclass(frozen=True)
class SaveEvent:
    """Repeated save-based damage event with the same DC and damage math."""

    name: str
    count: int
    save_dc: int
    save_bonus: float
    damage: tuple[DamageDice, ...] = ()
    flat_damage: float = 0.0
    on_success: SaveOutcome = "half"
    target_count: int = 1


@dataclass(frozen=True)
class DirectDamageEvent:
    """Damage that is already conditional on another routine step succeeding."""

    name: str
    count: int
    damage: tuple[DamageDice, ...] = ()
    flat_damage: float = 0.0
    target_count: int = 1


@dataclass(frozen=True)
class ConditionalDamageEvent:
    """Damage that is applied if at least one named attack event hits."""

    name: str
    trigger_event_names: tuple[str, ...]
    damage: tuple[DamageDice, ...] = ()
    flat_damage: float = 0.0
    target_count: int = 1


@dataclass(frozen=True)
class DamageRoutine:
    """A complete damage routine for one turn or one repeated round."""

    name: str
    burst_window: BurstWindow
    recovery: Recovery
    range_band: str
    setup: str
    events: tuple[AttackEvent, ...] = ()
    vex_events: tuple[VexChainEvent, ...] = ()
    save_events: tuple[SaveEvent, ...] = ()
    direct_events: tuple[DirectDamageEvent, ...] = ()
    conditional_events: tuple[ConditionalDamageEvent, ...] = ()
    category: DprCategory | None = None
    level: int | None = None
    resources: tuple[str, ...] = ()
    notes: tuple[str, ...] = field(default_factory=tuple)
    option_name: str = ""
    variant: AssumptionVariant = "default"
    exclude_from_calibration: bool = False
