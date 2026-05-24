from __future__ import annotations

from dpr.core import AttackEvent, DamageDice, DamageRoutine, calculate_routine


def wizard_cme_scorching_ray() -> DamageRoutine:
    # 9th-level Conjure Minor Elementals adds 7d8. 8th-level Scorching Ray has 9 rays.
    return DamageRoutine(
        name="20级法师：9环咒唤微元素群 + 8环灼热射线",
        events=(
            AttackEvent(
                name="8环灼热射线：9 rays, each 2d6 + 7d8",
                count=9,
                attack_bonus=11,
                target_ac=19,
                damage=(DamageDice(2, 6, label="灼热射线"), DamageDice(7, 8, label="9环CME")),
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="15",
        setup="CME must already be active; burst spends an 8th-level slot on Scorching Ray.",
        resources=("9th-level slot: CME", "8th-level slot: Scorching Ray", "concentration"),
        notes=("All-hit ceiling should match 346.5 before hit/crit math.",),
    )


def valor_bard_warlock_fighter_turret() -> DamageRoutine:
    # Conservative pilot: prebuffed 8th-level CME (6d8), one 7th-level Scorching Ray,
    # Action Surge into Eldritch Blast. It does not assume a second slotted spell in the same turn.
    return DamageRoutine(
        name="勇气学院16 / 魔契师2 / 战士2：CME炮台保守核算",
        events=(
            AttackEvent(
                name="7环灼热射线：8 rays, each 2d6 + 6d8",
                count=8,
                attack_bonus=11,
                target_ac=19,
                damage=(DamageDice(2, 6, label="灼热射线"), DamageDice(6, 8, label="8环CME")),
            ),
            AttackEvent(
                name="魔能爆：4 beams, each 1d10 + CHA + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=19,
                damage=(DamageDice(1, 10, label="魔能爆"), DamageDice(6, 8, label="8环CME")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="15",
        setup="CME must already be active; Action Surge supplies the second action for Eldritch Blast.",
        resources=("8th-level slot: CME", "7th-level slot: Scorching Ray", "Action Surge", "concentration"),
        notes=(
            "This is a conservative legal baseline, not every possible external-buff ceiling.",
            "It spends one slotted spell in the burst turn; Eldritch Blast is a cantrip.",
        ),
    )


def eldritch_knight_polearm() -> DamageRoutine:
    # A transparent martial baseline: four Attack-action hits, Action Surge for four more,
    # plus one Polearm Master bonus attack. Spirit Shroud at EK's 4th-level slot remains 1d8.
    return DamageRoutine(
        name="20级奥法骑士：长柄武器 + 巨武器大师 + 4环魂灵环绕 + 动作如潮",
        events=(
            AttackEvent(
                name="长柄武器主攻击：8 hits, each 1d10 + STR + GWM + 1d8",
                count=8,
                attack_bonus=11,
                target_ac=19,
                damage=(DamageDice(1, 10, label="武器"), DamageDice(1, 8, label="魂灵环绕")),
                flat_damage=11,
            ),
            AttackEvent(
                name="长柄武器大师附赠攻击：1 hit, 1d4 + STR + GWM + 1d8",
                count=1,
                attack_bonus=11,
                target_ac=19,
                damage=(DamageDice(1, 4, label="武器"), DamageDice(1, 8, label="魂灵环绕")),
                flat_damage=11,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="10",
        setup="Spirit Shroud must already be active; Action Surge is used for a second Attack action.",
        resources=("4th-level slot: Spirit Shroud", "Action Surge", "concentration", "Polearm Master", "Great Weapon Master"),
        notes=("EK only has one 4th-level slot at level 19-20, and Spirit Shroud is still 1d8 at 4th level.",),
    )


def main() -> None:
    routines = (
        wizard_cme_scorching_ray(),
        valor_bard_warlock_fighter_turret(),
        eldritch_knight_polearm(),
    )
    for routine in routines:
        result = calculate_routine(routine)
        print(f"\n## {result.name}")
        print(f"- all_hit_damage: {result.all_hit_damage:.2f}")
        print(f"- expected_damage_vs_AC19: {result.expected_damage:.2f}")
        print(f"- range_band: {result.range_band}")
        print(f"- burst_window: {result.burst_window}")
        print(f"- recovery: {result.recovery}")
        print(f"- setup: {result.setup}")
        print(f"- resources: {', '.join(result.resources)}")
        for event in result.events:
            print(
                f"  - {event.name}: count={event.count}, "
                f"hit={event.hit_chance:.3f}, crit={event.crit_chance:.3f}, "
                f"all_hit={event.all_hit_damage:.2f}, expected={event.expected_damage:.2f}"
            )


if __name__ == "__main__":
    main()

