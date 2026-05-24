from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


AdvantageState = Literal["normal", "advantage", "disadvantage"]
BurstWindow = Literal["cold_start", "prebuffed", "setup_amortized", "sustained"]
Recovery = Literal["long_rest", "short_rest", "encounter_low_cost", "sustained", "at_will"]


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


@dataclass(frozen=True)
class DamageRoutine:
    """A complete damage routine for one turn or one repeated round."""

    name: str
    events: tuple[AttackEvent, ...]
    burst_window: BurstWindow
    recovery: Recovery
    range_band: str
    setup: str
    resources: tuple[str, ...] = ()
    notes: tuple[str, ...] = field(default_factory=tuple)

