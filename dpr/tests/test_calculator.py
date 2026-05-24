from __future__ import annotations

import unittest

from dpr.core import AttackEvent, ConditionalDamageEvent, DamageDice, DamageRoutine, SaveEvent, VexChainEvent, calculate_routine, rank_routine
from dpr.core.calculator import hit_and_crit_chance, save_fail_chance
from dpr.core.matrix import build_calibration_rows


class CalculatorTests(unittest.TestCase):
    def test_hit_and_crit_normal(self) -> None:
        event = AttackEvent("test", 1, attack_bonus=5, target_ac=15)
        hit, crit = hit_and_crit_chance(event)
        self.assertAlmostEqual(hit, 0.55)
        self.assertAlmostEqual(crit, 0.05)

    def test_expanded_crit_range(self) -> None:
        event_19 = AttackEvent("champion", 1, attack_bonus=5, target_ac=15, crit_min=19)
        event_18 = AttackEvent("superior champion", 1, attack_bonus=5, target_ac=15, crit_min=18)
        self.assertAlmostEqual(hit_and_crit_chance(event_19)[1], 0.10)
        self.assertAlmostEqual(hit_and_crit_chance(event_18)[1], 0.15)

    def test_expanded_crit_range_with_advantage(self) -> None:
        event = AttackEvent("adv champion", 1, attack_bonus=5, target_ac=15, crit_min=18, advantage="advantage")
        _, crit = hit_and_crit_chance(event)
        self.assertAlmostEqual(crit, 1 - (17 / 20) ** 2)

    def test_crit_on_hit_with_advantage(self) -> None:
        event = AttackEvent("paralyzed", 1, attack_bonus=5, target_ac=15, advantage="advantage", crit_on_hit=True)
        hit, crit = hit_and_crit_chance(event)
        self.assertAlmostEqual(hit, 0.7975)
        self.assertAlmostEqual(crit, hit)

    def test_crit_doubles_dice_not_flat(self) -> None:
        routine = DamageRoutine(
            name="crit test",
            level=1,
            category="close_burst",
            events=(AttackEvent("hit", 1, 5, (DamageDice(1, 8),), flat_damage=4, target_ac=15),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        self.assertAlmostEqual(result.all_hit_damage, 8.5)
        self.assertAlmostEqual(result.expected_damage, 0.55 * 8.5 + 0.05 * 4.5)

    def test_graze_miss_damage_does_not_count_as_hit_damage(self) -> None:
        routine = DamageRoutine(
            name="graze test",
            level=1,
            category="close_burst",
            events=(AttackEvent("greatsword", 1, 0, (DamageDice(2, 6),), flat_damage=5, target_ac=30, miss_damage=5),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        event = result.events[0]
        self.assertAlmostEqual(event.hit_chance, 0.05)
        self.assertAlmostEqual(event.miss_chance, 0.95)
        self.assertAlmostEqual(result.expected_damage, 0.05 * 12 + 0.05 * 7 + 0.95 * 5)

    def test_conditional_damage_requires_at_least_one_hit(self) -> None:
        trigger = "attack"
        routine = DamageRoutine(
            name="searing smite test",
            level=1,
            category="close_burst",
            events=(AttackEvent(trigger, 2, 5, (DamageDice(1, 8),), target_ac=15),),
            conditional_events=(
                ConditionalDamageEvent(
                    "searing smite",
                    trigger_event_names=(trigger,),
                    damage=(DamageDice(2, 6, crit_doubles=False),),
                ),
            ),
            burst_window="cold_start",
            recovery="long_rest",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        self.assertAlmostEqual(result.conditional_events[0].trigger_chance, 1 - 0.45**2)
        self.assertAlmostEqual(result.conditional_events[0].expected_damage, (1 - 0.45**2) * 7)

    def test_paladin_searing_smite5_branch_uses_two_5d6_packets(self) -> None:
        from dpr.benchmarks import all_routines

        routine = all_routines()["paladin-20-greatsword-gwm-spirit-shroud-searing-smite5-graze"]
        result = calculate_routine(routine)
        self.assertEqual(result.conditional_events[0].all_triggered_damage, 35)
        self.assertIn("5th-level slot: Spirit Shroud", routine.resources)
        self.assertIn("5th-level slot: Searing Smite", routine.resources)

    def test_save_half_damage(self) -> None:
        self.assertAlmostEqual(save_fail_chance(15, 4), 0.5)
        routine = DamageRoutine(
            name="save test",
            level=5,
            category="ranged_aoe",
            save_events=(
                SaveEvent(
                    "fire",
                    1,
                    15,
                    4,
                    (DamageDice(8, 6, crit_doubles=False),),
                    on_success="half",
                    target_count=3,
                ),
            ),
            burst_window="cold_start",
            recovery="long_rest",
            range_band="150",
            setup="cast",
        )
        result = calculate_routine(routine)
        self.assertAlmostEqual(result.all_hit_damage, 84)
        self.assertAlmostEqual(result.expected_damage, 63)

    def test_two_attack_vex_chain(self) -> None:
        routine = DamageRoutine(
            name="vex test",
            level=1,
            category="close_burst",
            vex_events=(VexChainEvent("rapier", 2, 5, (DamageDice(1, 8),), target_ac=15),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        self.assertAlmostEqual(result.expected_damage, 6.130125)

    def test_four_attack_vex_chain_bounds(self) -> None:
        routine = DamageRoutine(
            name="vex test",
            level=1,
            category="close_burst",
            vex_events=(VexChainEvent("rapier", 4, 5, (DamageDice(1, 8),), target_ac=15),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        normal_only = 4 * (0.55 * 4.5 + 0.05 * 4.5)
        advantage_only = 4 * (0.7975 * 4.5 + 0.0975 * 4.5)
        self.assertGreater(result.expected_damage, normal_only)
        self.assertLess(result.expected_damage, advantage_only)

    def test_rank_routine(self) -> None:
        routine = DamageRoutine(
            name="rank test",
            level=1,
            category="close_burst",
            events=(AttackEvent("hit", 1, 99, (DamageDice(2, 6),), target_ac=1),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = rank_routine(routine)
        self.assertEqual(result.reference_cr, "1")
        self.assertGreater(result.percent_hp, 20)

    def test_cme_bound_routines_are_close_burst(self) -> None:
        from dpr.benchmarks import all_routines

        routines = all_routines()
        self.assertEqual(routines["wizard-20-cme9-plus-scorching-ray8"].category, "close_burst")
        self.assertEqual(
            routines["valor-bard16-warlock2-fighter2-cme-turret-longbow-battle-magic"].category,
            "close_burst",
        )

    def test_valor_bard_bracers_dual_scimitar_extreme_case(self) -> None:
        from dpr.benchmarks import all_routines

        routine = all_routines()["valor-bard16-warlock2-fighter2-cme-turret-bracers-dual-scimitar"]
        result = calculate_routine(routine)
        self.assertEqual(routine.category, "close_burst")
        self.assertEqual(routine.variant, "item_ceiling")
        self.assertAlmostEqual(result.all_hit_damage, 643.0)
        self.assertAlmostEqual(result.expected_damage, 319.0)

    def test_valor_bard_bracers_dual_scimitar_paralyzed_case(self) -> None:
        from dpr.benchmarks import all_routines

        routine = all_routines()["valor-bard16-warlock2-fighter2-cme-turret-bracers-dual-scimitar-paralyzed"]
        result = calculate_routine(routine)
        self.assertEqual(routine.category, "close_burst")
        self.assertEqual(routine.variant, "condition_ceiling")
        self.assertAlmostEqual(result.all_hit_damage, 1236.0)
        self.assertAlmostEqual(result.expected_damage, 862.11)

    def test_calibration_matrix_separates_item_ceiling_from_default(self) -> None:
        from dpr.benchmarks import all_routines

        rows = build_calibration_rows(all_routines())
        bracers = next(row for row in rows if row.routine == "Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar")
        default_dual = next(row for row in rows if row.routine == "Valor Bard16 Warlock2 Fighter2 CME Turret Dual Scimitar")

        self.assertEqual(bracers.variant, "item_ceiling")
        self.assertEqual(bracers.default_calibrated_rank, "-")
        self.assertIn(bracers.ceiling_rank, ("EX", "S"))
        self.assertEqual(default_dual.variant, "default")
        self.assertEqual(default_dual.ceiling_rank, "-")

    def test_calibration_matrix_excludes_vex_rows(self) -> None:
        from dpr.benchmarks import all_routines

        rows = build_calibration_rows(all_routines())
        names = {row.routine for row in rows}
        self.assertNotIn("Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic Prior Vex", names)
        self.assertNotIn("Eldritch Knight 20 Rapier Shield Dueling Vex Surge", names)


if __name__ == "__main__":
    unittest.main()
