from __future__ import annotations

import unittest

from dpr.core import (
    AttackEvent,
    ConditionalDamageEvent,
    DamageDice,
    DamageRoutine,
    HitPoolDamageEvent,
    MissRerollEvent,
    SaveEvent,
    VexChainEvent,
    calculate_routine,
    rank_routine,
)
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

    def test_gwf_dice_floor(self) -> None:
        self.assertAlmostEqual(DamageDice(1, 6, minimum_roll=3).average, 4.0)
        self.assertAlmostEqual(DamageDice(2, 6, minimum_roll=3).average, 8.0)
        self.assertAlmostEqual(DamageDice(1, 4, minimum_roll=3).average, 3.25)

    def test_crit_flat_damage_only_on_critical(self) -> None:
        routine = DamageRoutine(
            name="vorpal test",
            level=1,
            category="close_burst",
            events=(AttackEvent("vorpal", 1, 5, (DamageDice(1, 8),), target_ac=15, crit_flat_damage=30),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        self.assertAlmostEqual(result.all_hit_damage, 4.5)
        self.assertAlmostEqual(result.expected_damage, 0.55 * 4.5 + 0.05 * (4.5 + 30))

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

    def test_hit_pool_damage_spends_only_on_successful_hits(self) -> None:
        trigger = "attack"
        routine = DamageRoutine(
            name="hit pool test",
            level=1,
            category="close_burst",
            events=(AttackEvent(trigger, 2, 5, (DamageDice(1, 8),), target_ac=15),),
            hit_pool_events=(HitPoolDamageEvent("maneuvers", (trigger,), dice_count=1, die_sides=12),),
            burst_window="cold_start",
            recovery="short_rest",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        self.assertAlmostEqual(result.hit_pool_events[0].all_hit_damage, 6.5)
        self.assertAlmostEqual(result.hit_pool_events[0].expected_spent_dice, 1 - 0.45**2)
        self.assertAlmostEqual(result.hit_pool_events[0].expected_damage, (1 - 0.45**2) * 6.5)

    def test_miss_reroll_event_adds_only_incremental_expected_damage(self) -> None:
        trigger = "attack"
        routine = DamageRoutine(
            name="miss reroll test",
            level=1,
            category="close_burst",
            events=(AttackEvent(trigger, 1, 5, (DamageDice(1, 8),), target_ac=15),),
            miss_reroll_events=(MissRerollEvent("reroll", (trigger,)),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        first_roll = 0.55 * 4.5 + 0.05 * 4.5
        self.assertAlmostEqual(result.miss_reroll_events[0].trigger_chance, 0.45)
        self.assertAlmostEqual(result.expected_damage, first_roll + 0.45 * first_roll)
        self.assertAlmostEqual(result.all_hit_damage, 4.5)

    def test_miss_reroll_event_does_not_double_count_graze_damage(self) -> None:
        trigger = "attack"
        routine = DamageRoutine(
            name="graze reroll test",
            level=1,
            category="close_burst",
            events=(AttackEvent(trigger, 1, 5, (DamageDice(1, 8),), target_ac=15, miss_damage=5),),
            miss_reroll_events=(MissRerollEvent("reroll", (trigger,)),),
            burst_window="cold_start",
            recovery="at_will",
            range_band="5",
            setup="none",
        )
        result = calculate_routine(routine)
        first_roll = 0.55 * 4.5 + 0.05 * 4.5 + 0.45 * 5
        reroll_increment = 0.55 * 4.5 + 0.05 * 4.5 + 0.45 * 5 - 5
        self.assertAlmostEqual(result.expected_damage, first_roll + 0.45 * reroll_increment)

    def test_paladin_searing_smite5_branch_uses_two_5d6_packets(self) -> None:
        from dpr.benchmarks import all_routines

        routine = all_routines()["paladin-20-greatsword-gwf-gwm-spirit-shroud-searing-smite5-graze"]
        result = calculate_routine(routine)
        self.assertEqual(result.conditional_events[0].all_triggered_damage, 37.5)
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

    def test_valor_bard_vorpal_dual_scimitar_cases(self) -> None:
        from dpr.benchmarks import all_routines

        routines = all_routines()
        three_weapon = routines["valor-bard16-warlock2-fighter2-cme-turret-vorpal-dual-scimitar"]
        bracers = routines["valor-bard16-warlock2-fighter2-cme-turret-bracers-vorpal-dual-scimitar"]

        self.assertEqual(len([event for event in three_weapon.events if "scimitar" in event.name.lower()]), 3)
        self.assertEqual(len([event for event in bracers.events if "scimitar" in event.name.lower()]), 2)

        three_weapon_result = calculate_routine(three_weapon)
        bracers_result = calculate_routine(bracers)
        self.assertAlmostEqual(three_weapon_result.all_hit_damage, 537.5)
        self.assertAlmostEqual(three_weapon_result.expected_damage, 288.375)
        self.assertAlmostEqual(bracers_result.all_hit_damage, 649.0)
        self.assertAlmostEqual(bracers_result.expected_damage, 336.25)

    def test_valor_bard_bracers_dual_scimitar_paralyzed_case(self) -> None:
        from dpr.benchmarks import all_routines

        routine = all_routines()["valor-bard16-warlock2-fighter2-cme-turret-bracers-vorpal-dual-scimitar-paralyzed"]
        result = calculate_routine(routine)
        self.assertEqual(routine.category, "close_burst")
        self.assertEqual(routine.variant, "condition_ceiling")
        self.assertAlmostEqual(result.all_hit_damage, 1302.0)
        self.assertAlmostEqual(result.expected_damage, 936.36)

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

    def test_updated_fighter_routines_replace_old_cases(self) -> None:
        from dpr.benchmarks import all_routines

        routines = all_routines()
        self.assertIn("champion-20-polearm-gwf-gwm-pam", routines)
        self.assertIn("battle-master-20-polearm-gwf-gwm-pam", routines)
        self.assertIn("eldritch-knight-20-polearm-gwf-gwm-pam-cme4-true-strike", routines)
        self.assertIn("champion-20-vorpal-polearm-cme8", routines)
        self.assertIn("champion-20-vorpal-polearm-cme8-paralyzed", routines)
        self.assertIn("eldritch-knight-20-vorpal-greatsword-cme8-bracers-booming-blade", routines)
        self.assertIn("eldritch-knight-20-vorpal-greatsword-cme8-bracers-booming-blade-paralyzed", routines)
        self.assertNotIn("eldritch-knight-20-polearm-spirit-shroud", routines)
        self.assertNotIn("eldritch-knight-20-rapier-shield-dueling-vex-surge", routines)

    def test_fighter_vorpal_item_ceiling_paralyzed_cases(self) -> None:
        from dpr.benchmarks import all_routines

        routines = all_routines()
        champion = routines["champion-20-vorpal-polearm-cme8-paralyzed"]
        ek = routines["eldritch-knight-20-vorpal-greatsword-cme8-bracers-booming-blade-paralyzed"]

        champion_result = calculate_routine(champion)
        ek_result = calculate_routine(ek)
        self.assertEqual(champion.variant, "condition_ceiling")
        self.assertEqual(ek.variant, "condition_ceiling")
        self.assertAlmostEqual(champion_result.all_hit_damage, 1046.6)
        self.assertAlmostEqual(champion_result.expected_damage, 961.141830851364)
        self.assertAlmostEqual(ek_result.all_hit_damage, 1148.25)
        self.assertAlmostEqual(ek_result.expected_damage, 971.73)

    def test_flat_fighter_vorpal_item_ceiling_cases(self) -> None:
        from dpr.benchmarks import all_routines

        routines = all_routines()
        fighter = routines["fighter-20-vorpal-polearm-cme8"]
        fighter_paralyzed = routines["fighter-20-vorpal-polearm-cme8-paralyzed"]
        champion = routines["champion-20-vorpal-polearm-cme8"]

        fighter_result = calculate_routine(fighter)
        fighter_paralyzed_result = calculate_routine(fighter_paralyzed)
        champion_result = calculate_routine(champion)
        self.assertEqual(fighter.variant, "item_ceiling")
        self.assertEqual(fighter_paralyzed.variant, "condition_ceiling")
        self.assertEqual(len(fighter.miss_reroll_events), 0)
        self.assertEqual(len(champion.miss_reroll_events), 1)
        self.assertAlmostEqual(fighter_result.expected_damage, 316.895)
        self.assertAlmostEqual(fighter_paralyzed_result.expected_damage, 886.344)
        self.assertGreater(champion_result.expected_damage, fighter_result.expected_damage)

    def test_champion_heroic_inspiration_reroll_is_modeled(self) -> None:
        from dpr.benchmarks import all_routines

        routine = all_routines()["champion-20-polearm-gwf-gwm-pam"]
        result = calculate_routine(routine)
        self.assertEqual(len(routine.miss_reroll_events), 1)
        self.assertAlmostEqual(result.all_hit_damage, 158.05)
        self.assertAlmostEqual(result.expected_damage, 113.11647923792549)

    def test_gwm_applies_to_attack_action_not_bonus_action(self) -> None:
        from dpr.benchmarks import all_routines

        champion = all_routines()["champion-20-polearm-gwf-gwm-pam"]
        self.assertEqual(champion.events[0].flat_damage, 11)
        self.assertEqual(champion.events[1].flat_damage, 11)
        self.assertEqual(champion.events[2].flat_damage, 5)

        ek_extreme = all_routines()["eldritch-knight-20-vorpal-greatsword-cme8-bracers-booming-blade"]
        self.assertEqual(ek_extreme.events[0].flat_damage, 14)
        self.assertEqual(ek_extreme.events[1].flat_damage, 14)
        self.assertEqual(ek_extreme.events[2].flat_damage, 8)

    def test_ek_cantrip_sources_are_separated(self) -> None:
        from dpr.benchmarks import all_routines

        ordinary = all_routines()["eldritch-knight-20-polearm-gwf-gwm-pam-cme4-true-strike"]
        extreme = all_routines()["eldritch-knight-20-vorpal-greatsword-cme8-bracers-booming-blade"]

        self.assertTrue(any("True Strike" in event.name for event in ordinary.events))
        self.assertFalse(any("Booming Blade" in event.name for event in ordinary.events))
        self.assertTrue(any("Booming Blade" in event.name for event in extreme.events))
        self.assertFalse(any("True Strike" in event.name for event in extreme.events))
        self.assertTrue(any("movement damage is excluded" in note for note in extreme.notes))


if __name__ == "__main__":
    unittest.main()
