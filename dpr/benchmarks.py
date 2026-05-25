from __future__ import annotations

from .core.model import (
    AttackEvent,
    ConditionalDamageEvent,
    DamageDice,
    DamageRoutine,
    HitPoolDamageEvent,
    MissRerollEvent,
    SaveEvent,
    VexChainEvent,
)


def _dice(count: int, sides: int, label: str = "", crit_doubles: bool = True) -> DamageDice:
    return DamageDice(count, sides, crit_doubles=crit_doubles, label=label)


def _gwf(count: int, sides: int, label: str = "", crit_doubles: bool = True) -> DamageDice:
    return DamageDice(count, sides, crit_doubles=crit_doubles, label=label, minimum_roll=3)


def all_routines() -> dict[str, DamageRoutine]:
    routines = [
        wizard_cme_scorching_ray_20(),
        valor_bard_warlock_fighter_turret_longbow_20(),
        valor_bard_warlock_fighter_turret_shortbow_20(),
        valor_bard_warlock_fighter_turret_shortbow_prior_vex_20(),
        valor_bard_warlock_fighter_turret_dual_scimitar_20(),
        valor_bard_warlock_fighter_turret_vorpal_dual_scimitar_20(),
        valor_bard_warlock_fighter_turret_bracers_dual_scimitar_20(),
        valor_bard_warlock_fighter_turret_bracers_vorpal_dual_scimitar_20(),
        valor_bard_warlock_fighter_turret_bracers_vorpal_dual_scimitar_paralyzed_20(),
        champion_polearm_gwf_20(),
        battle_master_polearm_gwf_20(),
        eldritch_knight_polearm_gwf_cme_true_strike_20(),
        fighter_vorpal_polearm_cme8_20(),
        fighter_vorpal_polearm_cme8_paralyzed_20(),
        champion_vorpal_polearm_cme8_20(),
        champion_vorpal_polearm_cme8_paralyzed_20(),
        eldritch_knight_vorpal_cme8_bracers_booming_blade_20(),
        eldritch_knight_vorpal_cme8_bracers_booming_blade_paralyzed_20(),
        vengeance_paladin_dual_wield_20(),
        noble_genies_paladin_cme_20(),
        paladin_gwm_searing_smite_20(),
        berserker_gwm_20(),
        hunter_ranger_dual_wield_20(),
        warlock_eldritch_blast_hex_20(),
        warlock_eldritch_blast_hex_bracers_20(),
        light_cleric_fireball_9(),
        druid_conjure_woodland_beings_13(),
    ]
    return {routine_id(routine): routine for routine in routines}


def routine_id(routine: DamageRoutine) -> str:
    return (
        routine.name.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("：", "-")
        .replace("，", "")
        .replace("+", "plus")
    )


def wizard_cme_scorching_ray_20() -> DamageRoutine:
    return DamageRoutine(
        name="Wizard 20 CME9 + Scorching Ray8",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="8th-level Scorching Ray, 9 rays, 2d6 + 7d8",
                count=9,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(2, 6, "Scorching Ray"), _dice(7, 8, "CME9")),
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="15",
        setup="CME is already active; the burst spends an 8th-level slot.",
        resources=("9th-level slot: CME", "8th-level slot: Scorching Ray", "concentration"),
        notes=("All-hit ceiling anchor is 346.5 before hit chance.",),
    )


def _valor_bard_turret_events(extra_attack: AttackEvent) -> tuple[AttackEvent, ...]:
    return (
        AttackEvent(
            name="7th-level Scorching Ray, 8 rays, 2d6 + 6d8",
            count=8,
            attack_bonus=11,
            target_ac=23,
            damage=(_dice(2, 6, "Scorching Ray"), _dice(6, 8, "CME8")),
        ),
        AttackEvent(
            name="Eldritch Blast through Action Surge, 4 beams, 1d10 + 5 + 6d8",
            count=4,
            attack_bonus=11,
            target_ac=23,
            damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
            flat_damage=5,
        ),
        extra_attack,
    )


def _valor_bard_turret(
    name: str,
    battle_magic_attack: AttackEvent,
    notes: tuple[str, ...],
) -> DamageRoutine:
    return DamageRoutine(
        name=name,
        level=20,
        category="close_burst",
        events=_valor_bard_turret_events(battle_magic_attack),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="15",
        setup="CME is already active; Action Surge supplies Eldritch Blast; Battle Magic supplies one bonus-action weapon attack.",
        resources=("8th-level slot: CME", "7th-level slot: Scorching Ray", "Action Surge", "Battle Magic", "concentration"),
        notes=notes,
        option_name="Valor Bard16 / Warlock2 / Fighter2 CME Turret",
        exclude_from_calibration="Vex" in name or any("Vex" in note for note in notes),
    )


def valor_bard_warlock_fighter_turret_longbow_20() -> DamageRoutine:
    return _valor_bard_turret(
        "Valor Bard16 Warlock2 Fighter2 CME Turret Longbow Battle Magic",
        AttackEvent(
            name="Battle Magic longbow, 1d8 + 5 + 6d8",
            count=1,
            attack_bonus=13,
            target_ac=23,
            damage=(_dice(1, 8, "longbow"), _dice(6, 8, "CME8")),
            flat_damage=5,
        ),
        ("No Illusionist's Bracers. Longbow has no Vex branch.",),
    )


def valor_bard_warlock_fighter_turret_shortbow_20() -> DamageRoutine:
    return _valor_bard_turret(
        "Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic",
        AttackEvent(
            name="Battle Magic shortbow, 1d6 + 5 + 6d8",
            count=1,
            attack_bonus=13,
            target_ac=23,
            damage=(_dice(1, 6, "shortbow"), _dice(6, 8, "CME8")),
            flat_damage=5,
        ),
        ("No Illusionist's Bracers. Shortbow has Vex, but this single bonus-action attack has no prior Vex advantage.",),
    )


def valor_bard_warlock_fighter_turret_shortbow_prior_vex_20() -> DamageRoutine:
    return _valor_bard_turret(
        "Valor Bard16 Warlock2 Fighter2 CME Turret Shortbow Battle Magic Prior Vex",
        AttackEvent(
            name="Battle Magic shortbow with prior Vex Advantage, 1d6 + 5 + 6d8",
            count=1,
            attack_bonus=13,
            target_ac=23,
            damage=(_dice(1, 6, "shortbow"), _dice(6, 8, "CME8")),
            flat_damage=5,
            advantage="advantage",
        ),
        ("No Illusionist's Bracers. This branch assumes a prior shortbow Vex hit made this bonus-action attack advantaged.",),
    )


def valor_bard_warlock_fighter_turret_dual_scimitar_20() -> DamageRoutine:
    return DamageRoutine(
        name="Valor Bard16 Warlock2 Fighter2 CME Turret Dual Scimitar",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="7th-level Scorching Ray, 8 rays, 2d6 + 6d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(2, 6, "Scorching Ray"), _dice(6, 8, "CME8")),
            ),
            AttackEvent(
                name="Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 6, "scimitar"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 6, "scimitar"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Bonus-action off-hand scimitar, 1d6 + 5 + 6d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 6, "scimitar"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="5",
        setup="CME is already active; Scorching Ray is cast with the normal action; Action Surge supplies an Attack action using Valor cantrip replacement; the bonus action is a weapon attack rather than Illusionist's Bracers.",
        resources=(
            "8th-level slot: CME",
            "7th-level slot: Scorching Ray",
            "Action Surge",
            "Spell Sniper",
            "Dual Wielder",
            "Weapon Mastery: Nick",
            "concentration",
        ),
        notes=(
            "Default optimized branch without Illusionist's Bracers.",
            "Spell Sniper is assumed to remove adjacent ranged-spell disadvantage.",
            "Three scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style.",
            "No Advantage, paralysis, or prior Vex is assumed.",
        ),
        option_name="Valor Bard16 / Warlock2 / Fighter2 CME Turret",
    )


def valor_bard_warlock_fighter_turret_vorpal_dual_scimitar_20() -> DamageRoutine:
    return DamageRoutine(
        name="Valor Bard16 Warlock2 Fighter2 CME Turret Vorpal Dual Scimitar",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="7th-level Scorching Ray, 8 rays, 2d6 + 6d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(2, 6, "Scorching Ray"), _dice(6, 8, "CME8")),
            ),
            AttackEvent(
                name="Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Action Surge Attack action: Vorpal main-hand scimitar, 1d6 + 8 + 6d8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_dice(1, 6, "vorpal scimitar"), _dice(6, 8, "CME8")),
                flat_damage=8,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Action Surge Attack action: Vorpal Nick off-hand scimitar, 1d6 + 8 + 6d8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_dice(1, 6, "vorpal scimitar"), _dice(6, 8, "CME8")),
                flat_damage=8,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Bonus-action Vorpal off-hand scimitar, 1d6 + 8 + 6d8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_dice(1, 6, "vorpal scimitar"), _dice(6, 8, "CME8")),
                flat_damage=8,
                crit_flat_damage=30,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="5",
        setup="CME is already active; Scorching Ray is cast with the normal action; Action Surge supplies an Attack action using Valor cantrip replacement; the bonus action is the Dual Wielder weapon attack. The target cannot be beheaded.",
        resources=(
            "8th-level slot: CME",
            "7th-level slot: Scorching Ray",
            "Action Surge",
            "Vorpal Scimitar x2",
            "Spell Sniper",
            "Dual Wielder",
            "Weapon Mastery: Nick",
            "concentration",
            "2 attunements",
        ),
        notes=(
            "Item-dependent branch with two Vorpal Scimitars and no Illusionist's Bracers.",
            "Spell Sniper is assumed to remove adjacent ranged-spell disadvantage.",
            "Three scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style.",
            "Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded.",
            "No Advantage, paralysis, or prior Vex is assumed.",
        ),
        option_name="Valor Bard16 / Warlock2 / Fighter2 CME Turret",
        variant="item_ceiling",
    )


def valor_bard_warlock_fighter_turret_bracers_dual_scimitar_20() -> DamageRoutine:
    return DamageRoutine(
        name="Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="7th-level Scorching Ray, 8 rays, 2d6 + 6d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(2, 6, "Scorching Ray"), _dice(6, 8, "CME8")),
            ),
            AttackEvent(
                name="Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Action Surge Attack action: main-hand scimitar, 1d6 + 5 + 6d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 6, "scimitar"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Action Surge Attack action: Nick off-hand scimitar, 1d6 + 5 + 6d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 6, "scimitar"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="5",
        setup="CME is already active; Scorching Ray is cast with the normal action; Action Surge supplies an Attack action using Valor cantrip replacement; Illusionist's Bracers repeat Eldritch Blast as the bonus action.",
        resources=(
            "8th-level slot: CME",
            "7th-level slot: Scorching Ray",
            "Action Surge",
            "Illusionist's Bracers",
            "Spell Sniper",
            "Dual Wielder",
            "Weapon Mastery: Nick",
            "concentration",
        ),
        notes=(
            "Extreme item-dependent branch. Spell Sniper is assumed to remove adjacent ranged-spell disadvantage.",
            "Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style.",
            "No Advantage, paralysis, or prior Vex is assumed.",
        ),
        option_name="Valor Bard16 / Warlock2 / Fighter2 CME Turret",
        variant="item_ceiling",
    )


def valor_bard_warlock_fighter_turret_bracers_vorpal_dual_scimitar_20() -> DamageRoutine:
    return DamageRoutine(
        name="Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Vorpal Dual Scimitar",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="7th-level Scorching Ray, 8 rays, 2d6 + 6d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(2, 6, "Scorching Ray"), _dice(6, 8, "CME8")),
            ),
            AttackEvent(
                name="Action Surge Attack action: Eldritch Blast replacing one Valor attack, 4 beams, 1d10 + 5 + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
            AttackEvent(
                name="Action Surge Attack action: Vorpal main-hand scimitar, 1d6 + 8 + 6d8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_dice(1, 6, "vorpal scimitar"), _dice(6, 8, "CME8")),
                flat_damage=8,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Action Surge Attack action: Vorpal Nick off-hand scimitar, 1d6 + 8 + 6d8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_dice(1, 6, "vorpal scimitar"), _dice(6, 8, "CME8")),
                flat_damage=8,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Illusionist's Bracers bonus action: Eldritch Blast, 4 beams, 1d10 + 5 + 6d8",
                count=4,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(6, 8, "CME8")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="5",
        setup="CME is already active; Scorching Ray is cast with the normal action; Action Surge supplies an Attack action using Valor cantrip replacement; Illusionist's Bracers repeat Eldritch Blast as the bonus action. The target cannot be beheaded.",
        resources=(
            "8th-level slot: CME",
            "7th-level slot: Scorching Ray",
            "Action Surge",
            "Illusionist's Bracers",
            "Vorpal Scimitar x2",
            "Spell Sniper",
            "Dual Wielder",
            "Weapon Mastery: Nick",
            "concentration",
            "3 attunements",
        ),
        notes=(
            "Extreme item-dependent branch with exactly three attunements: Illusionist's Bracers and two Vorpal Scimitars.",
            "Spell Sniper is assumed to remove adjacent ranged-spell disadvantage.",
            "Two scimitar hits are modeled with Two-Weapon Fighting ability damage from the Fighter fighting style.",
            "Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded.",
            "No Advantage, paralysis, or prior Vex is assumed.",
        ),
        option_name="Valor Bard16 / Warlock2 / Fighter2 CME Turret",
        variant="item_ceiling",
    )


def _paralyzed(event: AttackEvent) -> AttackEvent:
    return AttackEvent(
        name=f"Paralyzed target: {event.name}",
        count=event.count,
        attack_bonus=event.attack_bonus,
        damage=event.damage,
        flat_damage=event.flat_damage,
        miss_damage=event.miss_damage,
        advantage="advantage",
        target_ac=event.target_ac,
        crit_min=event.crit_min,
        crit_on_hit=True,
        crit_flat_damage=event.crit_flat_damage,
    )


def _paralyzed_miss_reroll(event: MissRerollEvent) -> MissRerollEvent:
    return MissRerollEvent(
        name=f"{event.name} against Paralyzed target",
        trigger_event_names=tuple(f"Paralyzed target: {name}" for name in event.trigger_event_names),
        uses=event.uses,
    )


def valor_bard_warlock_fighter_turret_bracers_vorpal_dual_scimitar_paralyzed_20() -> DamageRoutine:
    base = valor_bard_warlock_fighter_turret_bracers_vorpal_dual_scimitar_20()
    return DamageRoutine(
        name="Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Vorpal Dual Scimitar Paralyzed",
        level=20,
        category="close_burst",
        events=tuple(_paralyzed(event) for event in base.events),
        burst_window=base.burst_window,
        recovery=base.recovery,
        range_band=base.range_band,
        setup=f"{base.setup} Target is Paralyzed and all attacks are made within 5 feet.",
        resources=base.resources + ("Paralyzed target",),
        notes=tuple(note for note in base.notes if "No Advantage" not in note)
        + (
            "Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit.",
            "Flat damage is not doubled; all damage dice on the attack are doubled.",
        ),
        option_name=base.option_name,
        variant="condition_ceiling",
    )


def champion_polearm_gwf_20() -> DamageRoutine:
    return DamageRoutine(
        name="Champion 20 Polearm GWF GWM/PAM",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + GWM",
                count=7,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(2, 6, "greatsword"),),
                flat_damage=11,
                miss_damage=5,
                crit_min=18,
            ),
            AttackEvent(
                name="Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(1, 10, "glaive"),),
                flat_damage=11,
                miss_damage=5,
                crit_min=18,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 GWF + STR",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(1, 4, "glaive haft"),),
                flat_damage=5,
                miss_damage=5,
                crit_min=18,
            ),
        ),
        miss_reroll_events=(
            MissRerollEvent(
                name="Champion Heroic Inspiration rerolls one missed attack",
                trigger_event_names=(
                    "Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + GWM",
                    "Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM",
                    "Polearm Master bonus attack, 1d4 GWF + STR",
                ),
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="10",
        setup="Action Surge is used; Greatsword is used until the final Attack-action hit, then Glaive enables Polearm Master.",
        resources=("Action Surge", "Great Weapon Fighting", "Great Weapon Master", "Polearm Master", "Weapon Mastery: Graze"),
        notes=(
            "GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack.",
            "GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3.",
            "Graze miss damage is Strength modifier only and does not trigger GWM.",
            "Champion level 15+ crits on 18-20 with weapon attacks and Unarmed Strikes.",
            "Champion level 10+ is modeled as spending one Heroic Inspiration reroll on the first missed attack in the burst turn.",
        ),
    )


def battle_master_polearm_gwf_20() -> DamageRoutine:
    return DamageRoutine(
        name="Battle Master 20 Polearm GWF GWM/PAM",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + GWM",
                count=7,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(2, 6, "greatsword"),),
                flat_damage=11,
                miss_damage=5,
            ),
            AttackEvent(
                name="Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(1, 10, "glaive"),),
                flat_damage=11,
                miss_damage=5,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 GWF + STR",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(1, 4, "glaive haft"),),
                flat_damage=5,
                miss_damage=5,
            ),
        ),
        hit_pool_events=(
            HitPoolDamageEvent(
                name="Superiority dice spent on successful hits, up to 6d12",
                trigger_event_names=(
                    "Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + GWM",
                    "Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM",
                    "Polearm Master bonus attack, 1d4 GWF + STR",
                ),
                dice_count=6,
                die_sides=12,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="10",
        setup="Action Surge and superiority dice are committed; Greatsword is used until the final Attack-action hit, then Glaive enables Polearm Master.",
        resources=("Action Surge", "Great Weapon Fighting", "Great Weapon Master", "Polearm Master", "Weapon Mastery: Graze", "superiority dice"),
        notes=(
            "GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack.",
            "GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3.",
            "Graze miss damage is Strength modifier only and does not trigger GWM.",
            "Superiority dice are modeled as a limited pool spent only on successful hits.",
        ),
    )


def eldritch_knight_polearm_gwf_cme_true_strike_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Polearm GWF GWM/PAM CME4 True Strike",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Greatsword Attack-action hits, 5 attacks, 2d6 GWF + STR + GWM + CME4",
                count=5,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(2, 6, "greatsword"), _gwf(2, 8, "CME4")),
                flat_damage=11,
                miss_damage=5,
            ),
            AttackEvent(
                name="Greatsword True Strike replacements, 2 attacks, 2d6 GWF + STR + GWM + CME4 + 3d6 radiant",
                count=2,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(2, 6, "greatsword"), _gwf(2, 8, "CME4"), _gwf(3, 6, "True Strike")),
                flat_damage=11,
                miss_damage=5,
            ),
            AttackEvent(
                name="Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + GWM + CME4",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(1, 10, "glaive"), _gwf(2, 8, "CME4")),
                flat_damage=11,
                miss_damage=5,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 GWF + STR + CME4",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_gwf(1, 4, "glaive haft"), _gwf(2, 8, "CME4")),
                flat_damage=5,
                miss_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="15",
        setup="CME4 is already active; Action Surge creates two Attack actions, each replacing one attack with PHB 2024 True Strike.",
        resources=("4th-level slot: CME", "Action Surge", "Great Weapon Fighting", "Great Weapon Master", "Polearm Master", "Weapon Mastery: Graze", "War Magic", "True Strike", "concentration"),
        notes=(
            "This ordinary EK row uses PHB 2024 True Strike rather than Booming Blade.",
            "GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack.",
            "CME and True Strike dice are included in the broad GWF dice-floor benchmark; this is table-sensitive.",
            "Graze miss damage is Strength modifier only and does not trigger CME, True Strike, or GWM.",
        ),
    )


def fighter_vorpal_polearm_cme8_20() -> DamageRoutine:
    return DamageRoutine(
        name="Fighter 20 Vorpal Polearm CME8",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8",
                count=7,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(2, 6, "vorpal greatsword"), _gwf(6, 8, "CME8")),
                flat_damage=14,
                miss_damage=5,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(1, 10, "vorpal glaive"), _gwf(6, 8, "CME8")),
                flat_damage=14,
                miss_damage=5,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(1, 4, "vorpal glaive haft"), _gwf(6, 8, "CME8")),
                flat_damage=8,
                miss_damage=5,
                crit_flat_damage=30,
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="15",
        setup="CME8 is pre-cast from a random Enspelled Weapon; Action Surge is used; the target cannot be beheaded.",
        resources=("Enspelled Weapon: CME8", "Vorpal Greatsword", "Vorpal Glaive", "Action Surge", "Great Weapon Fighting", "Great Weapon Master", "Polearm Master", "Weapon Mastery: Graze", "concentration", "3 attunements"),
        notes=(
            "Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Vorpal Glaive.",
            "This is a no-subclass Fighter comparison row with no Champion crit expansion or Heroic Inspiration reroll.",
            "GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack.",
            "Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded.",
            "CME dice are included in the broad GWF dice-floor benchmark; this is table-sensitive.",
        ),
        option_name="Fighter 20 Polearm GWF GWM/PAM",
        variant="item_ceiling",
    )


def fighter_vorpal_polearm_cme8_paralyzed_20() -> DamageRoutine:
    base = fighter_vorpal_polearm_cme8_20()
    return DamageRoutine(
        name="Fighter 20 Vorpal Polearm CME8 Paralyzed",
        level=base.level,
        category=base.category,
        events=tuple(_paralyzed(event) for event in base.events),
        burst_window=base.burst_window,
        recovery=base.recovery,
        range_band=base.range_band,
        setup=f"{base.setup} Target is Paralyzed and all attacks are made within 5 feet.",
        resources=base.resources + ("Paralyzed target",),
        notes=base.notes
        + (
            "Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit.",
            "Flat damage is not doubled; all damage dice on the attack are doubled.",
            "Graze miss damage still applies on misses but does not trigger CME, Vorpal, or GWM.",
        ),
        option_name=base.option_name,
        variant="condition_ceiling",
    )


def champion_vorpal_polearm_cme8_20() -> DamageRoutine:
    return DamageRoutine(
        name="Champion 20 Vorpal Polearm CME8",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8",
                count=7,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(2, 6, "vorpal greatsword"), _gwf(6, 8, "CME8")),
                flat_damage=14,
                miss_damage=5,
                crit_min=18,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(1, 10, "vorpal glaive"), _gwf(6, 8, "CME8")),
                flat_damage=14,
                miss_damage=5,
                crit_min=18,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(1, 4, "vorpal glaive haft"), _gwf(6, 8, "CME8")),
                flat_damage=8,
                miss_damage=5,
                crit_min=18,
                crit_flat_damage=30,
            ),
        ),
        miss_reroll_events=(
            MissRerollEvent(
                name="Champion Heroic Inspiration rerolls one missed attack",
                trigger_event_names=(
                    "Vorpal Greatsword Attack-action hits, 7 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8",
                    "Vorpal Glaive final Attack-action hit, 1 attack, 1d10 GWF + STR + Vorpal + GWM + CME8",
                    "Vorpal Glaive Polearm Master bonus attack, 1d4 GWF + STR + Vorpal + CME8",
                ),
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="15",
        setup="CME8 is pre-cast from a random Enspelled Weapon; Action Surge is used; the target cannot be beheaded.",
        resources=("Enspelled Weapon: CME8", "Vorpal Greatsword", "Vorpal Glaive", "Action Surge", "Great Weapon Fighting", "Great Weapon Master", "Polearm Master", "Weapon Mastery: Graze", "concentration", "3 attunements"),
        notes=(
            "Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Vorpal Glaive.",
            "GWM damage applies to Attack-action hits only, not the Polearm Master bonus attack.",
            "Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded.",
            "CME dice are included in the broad GWF dice-floor benchmark; this is table-sensitive.",
            "Champion level 10+ is modeled as spending one Heroic Inspiration reroll on the first missed attack in the burst turn.",
        ),
        option_name="Champion 20 Polearm GWF GWM/PAM",
        variant="item_ceiling",
    )


def champion_vorpal_polearm_cme8_paralyzed_20() -> DamageRoutine:
    base = champion_vorpal_polearm_cme8_20()
    return DamageRoutine(
        name="Champion 20 Vorpal Polearm CME8 Paralyzed",
        level=base.level,
        category=base.category,
        events=tuple(_paralyzed(event) for event in base.events),
        miss_reroll_events=tuple(_paralyzed_miss_reroll(event) for event in base.miss_reroll_events),
        burst_window=base.burst_window,
        recovery=base.recovery,
        range_band=base.range_band,
        setup=f"{base.setup} Target is Paralyzed and all attacks are made within 5 feet.",
        resources=base.resources + ("Paralyzed target",),
        notes=base.notes
        + (
            "Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit.",
            "Flat damage is not doubled; all damage dice on the attack are doubled.",
            "Graze miss damage still applies on misses but does not trigger CME, Vorpal, or GWM.",
        ),
        option_name=base.option_name,
        variant="condition_ceiling",
    )


def eldritch_knight_vorpal_cme8_bracers_booming_blade_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Vorpal Greatsword CME8 Bracers Booming Blade",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Vorpal Greatsword Attack-action hits, 6 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8",
                count=6,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(2, 6, "vorpal greatsword"), _gwf(6, 8, "CME8")),
                flat_damage=14,
                miss_damage=5,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Attack-action Booming Blade replacements, 2 attacks, 2d6 GWF + STR + Vorpal + GWM + CME8 + 3d8 thunder",
                count=2,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(2, 6, "vorpal greatsword"), _gwf(6, 8, "CME8"), _gwf(3, 8, "Booming Blade")),
                flat_damage=14,
                miss_damage=5,
                crit_flat_damage=30,
            ),
            AttackEvent(
                name="Illusionist's Bracers bonus-action Booming Blade, 2d6 GWF + STR + Vorpal + CME8 + 3d8 thunder",
                count=1,
                attack_bonus=14,
                target_ac=23,
                damage=(_gwf(2, 6, "vorpal greatsword"), _gwf(6, 8, "CME8"), _gwf(3, 8, "Booming Blade")),
                flat_damage=8,
                miss_damage=5,
                crit_flat_damage=30,
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="15",
        setup="CME8 is pre-cast from a random Enspelled Weapon; Action Surge creates two Attack actions, and Illusionist's Bracers repeats Booming Blade as a bonus action.",
        resources=("Enspelled Weapon: CME8", "Vorpal Greatsword", "Illusionist's Bracers", "Action Surge", "Great Weapon Fighting", "Great Weapon Master", "Weapon Mastery: Graze", "War Magic", "Booming Blade", "concentration", "3 attunements"),
        notes=(
            "Item-ceiling branch with exactly three attunements: Enspelled Weapon, Vorpal Greatsword, and Illusionist's Bracers.",
            "The ordinary EK row remains PHB 2024 True Strike; Booming Blade is used only for this non-PHB item-ceiling case.",
            "GWM damage applies to Attack-action hits only, not the Bracers bonus-action Booming Blade.",
            "Only Booming Blade's on-hit thunder damage is counted; target movement damage is excluded.",
            "Vorpal +30 is modeled as crit-only flat damage because the target cannot be beheaded.",
            "CME and Booming Blade dice are included in the broad GWF dice-floor benchmark; this is table-sensitive.",
        ),
        option_name="Eldritch Knight 20 Greatsword GWM",
        variant="item_ceiling",
    )


def eldritch_knight_vorpal_cme8_bracers_booming_blade_paralyzed_20() -> DamageRoutine:
    base = eldritch_knight_vorpal_cme8_bracers_booming_blade_20()
    return DamageRoutine(
        name="Eldritch Knight 20 Vorpal Greatsword CME8 Bracers Booming Blade Paralyzed",
        level=base.level,
        category=base.category,
        events=tuple(_paralyzed(event) for event in base.events),
        burst_window=base.burst_window,
        recovery=base.recovery,
        range_band=base.range_band,
        setup=f"{base.setup} Target is Paralyzed and all attacks are made within 5 feet.",
        resources=base.resources + ("Paralyzed target",),
        notes=base.notes
        + (
            "Condition-dependent branch: attacks have Advantage and any hit from within 5 feet is a critical hit.",
            "Flat damage is not doubled; all damage dice on the attack are doubled.",
            "Graze miss damage still applies on misses but does not trigger CME, Booming Blade, Vorpal, or GWM.",
        ),
        option_name=base.option_name,
        variant="condition_ceiling",
    )


def vengeance_paladin_dual_wield_20() -> DamageRoutine:
    return DamageRoutine(
        name="Vengeance Paladin 20 Dual Wield Hunter's Mark Divine Favor",
        level=20,
        category="close_sustained",
        events=(
            AttackEvent(
                name="Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 1d6 + 1d4",
                count=4,
                attack_bonus=13,
                target_ac=22,
                damage=(
                    _dice(1, 6, "weapon"),
                    _dice(1, 8, "Radiant Strikes"),
                    _dice(1, 6, "Hunter's Mark"),
                    _dice(1, 4, "Divine Favor"),
                ),
                flat_damage=5,
                advantage="advantage",
            ),
        ),
        burst_window="prebuffed",
        recovery="encounter_low_cost",
        range_band="5",
        setup="Hunter's Mark and Divine Favor are already active; Vow advantage is active.",
        resources=("Hunter's Mark", "Divine Favor", "Vow of Enmity", "Nick", "Dual Wielder"),
        notes=("This is a sustained weapon-rider branch, not a smite nova branch.",),
    )


def noble_genies_paladin_cme_20() -> DamageRoutine:
    return DamageRoutine(
        name="Noble Genies Paladin 20 Dual Wield CME5 Divine Favor",
        level=20,
        category="close_sustained",
        events=(
            AttackEvent(
                name="Dual-wield melee hits, 4 hits, 1d6 + 5 + 1d8 + 3d8 + 1d4",
                count=4,
                attack_bonus=13,
                target_ac=22,
                damage=(
                    _dice(1, 6, "weapon"),
                    _dice(1, 8, "Radiant Strikes"),
                    _dice(3, 8, "CME5"),
                    _dice(1, 4, "Divine Favor"),
                ),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="15",
        setup="CME and Divine Favor are already active.",
        resources=("5th-level slot: CME", "Divine Favor", "concentration", "Nick", "Dual Wielder"),
        notes=("Close-range concentration branch; lower hit count than full-caster ray/EB CME routines.",),
    )


def paladin_gwm_searing_smite_20() -> DamageRoutine:
    trigger = "Greatsword Attack-action hits, 2 attacks, 2d6 GWF + STR + GWM + Radiant Strikes + Spirit Shroud5 + Divine Favor"
    return DamageRoutine(
        name="Paladin 20 Greatsword GWF GWM Spirit Shroud Searing Smite5 Graze",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name=trigger,
                count=2,
                attack_bonus=11,
                target_ac=22,
                damage=(
                    _gwf(2, 6, "greatsword"),
                    _gwf(1, 8, "Radiant Strikes"),
                    _gwf(2, 8, "Spirit Shroud5"),
                    _gwf(1, 4, "Divine Favor"),
                ),
                flat_damage=11,
                miss_damage=5,
            ),
        ),
        conditional_events=(
            ConditionalDamageEvent(
                name="5th-level Searing Smite initial and guaranteed burn damage, 10d6 if any greatsword attack hits",
                trigger_event_names=(trigger,),
                damage=(_gwf(5, 6, "Searing Smite5 initial", crit_doubles=False), _dice(5, 6, "Searing Smite5 burn", crit_doubles=False)),
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="5",
        setup="Spirit Shroud and Divine Favor are already active; 5th-level Searing Smite is cast after the first greatsword hit, so it contributes only if at least one attack hits.",
        resources=(
            "5th-level slot: Spirit Shroud",
            "Divine Favor",
            "5th-level slot: Searing Smite",
            "Great Weapon Fighting",
            "Great Weapon Master",
            "Weapon Mastery: Graze",
            "concentration",
        ),
        notes=(
            "Searing Smite is modeled as two guaranteed 5d6 damage packets after a hit: the initial rider and the follow-up burn; only the initial hit-linked packet uses the broad GWF dice-floor benchmark.",
            "If every greatsword attack misses, Searing Smite is not cast and adds no damage.",
            "Graze miss damage does not trigger Searing Smite, Spirit Shroud, Radiant Strikes, or Great Weapon Master.",
            "GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3.",
        ),
        option_name="Paladin 20 Greatsword GWM",
    )


def berserker_gwm_20() -> DamageRoutine:
    return DamageRoutine(
        name="Berserker Barbarian 20 GWF GWM Graze",
        level=20,
        category="close_sustained",
        events=(
            AttackEvent(
                name="Reckless greatsword Attack-action hits, 2 attacks, 2d6 GWF + STR + Rage + GWM + Frenzy",
                count=2,
                attack_bonus=13,
                target_ac=22,
                damage=(_gwf(2, 6, "weapon"), _gwf(4, 6, "Frenzy once-per-turn", crit_doubles=False)),
                flat_damage=17,
                advantage="advantage",
                miss_damage=7,
            ),
        ),
        burst_window="sustained",
        recovery="encounter_low_cost",
        range_band="5",
        setup="Rage is active; Reckless Attack is used.",
        resources=("Rage", "Reckless Attack", "Great Weapon Fighting", "Great Weapon Master", "Weapon Mastery: Graze"),
        notes=(
            "Frenzy dice are folded into the event as once-per-turn damage.",
            "GWM damage applies to Attack-action hits.",
            "Graze miss damage is modeled as Strength modifier only; Rage, GWM, and Frenzy are not added to Graze.",
            "GWF is modeled with the broad 2024 benchmark reading: eligible attack damage dice of 1-2 count as 3.",
        ),
    )


def hunter_ranger_dual_wield_20() -> DamageRoutine:
    return DamageRoutine(
        name="Hunter Ranger 20 Dual Wield Hunter's Mark",
        level=20,
        category="close_sustained",
        events=(
            AttackEvent(
                name="Dual-wield hits, 4 hits, 1d6 + 5 + 1d6",
                count=4,
                attack_bonus=13,
                target_ac=22,
                damage=(_dice(1, 6, "weapon"), _dice(1, 6, "Hunter's Mark")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="encounter_low_cost",
        range_band="5",
        setup="Hunter's Mark is active.",
        resources=("Hunter's Mark", "Nick", "Dual Wielder"),
        notes=("Subclass damage riders are not included; use as a Ranger floor branch.",),
    )


def warlock_eldritch_blast_hex_20() -> DamageRoutine:
    return DamageRoutine(
        name="Warlock 20 Eldritch Blast Hex",
        level=20,
        category="ranged_sustained",
        events=(
            AttackEvent(
                name="Eldritch Blast, 4 beams, 1d10 + 5 + 1d6",
                count=4,
                attack_bonus=11,
                target_ac=22,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(1, 6, "Hex")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="encounter_low_cost",
        range_band="120+",
        setup="Hex is active.",
        resources=("Hex", "concentration", "Agonizing Blast"),
        option_name="Warlock 20 Eldritch Blast Hex",
    )


def warlock_eldritch_blast_hex_bracers_20() -> DamageRoutine:
    return DamageRoutine(
        name="Warlock 20 Eldritch Blast Hex Bracers",
        level=20,
        category="ranged_sustained",
        events=(
            AttackEvent(
                name="Eldritch Blast action plus Illusionist's Bracers bonus action, 8 beams, 1d10 + 5 + 1d6",
                count=8,
                attack_bonus=11,
                target_ac=22,
                damage=(_dice(1, 10, "Eldritch Blast"), _dice(1, 6, "Hex")),
                flat_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="encounter_low_cost",
        range_band="120+",
        setup="Hex is active; Illusionist's Bracers repeat Eldritch Blast as a bonus action.",
        resources=("Hex", "concentration", "Agonizing Blast", "Illusionist's Bracers"),
        notes=("Item-ceiling sustained branch; not part of default Warlock DPR ranking.",),
        option_name="Warlock 20 Eldritch Blast Hex",
        variant="item_ceiling",
    )


def light_cleric_fireball_9() -> DamageRoutine:
    return DamageRoutine(
        name="Light Cleric 9 Fireball",
        level=9,
        category="ranged_aoe",
        save_events=(
            SaveEvent(
                name="3rd-level Fireball, 8d6, Dex half, 3 targets",
                count=1,
                save_dc=17,
                save_bonus=2,
                target_count=3,
                damage=(_dice(8, 6, "Fireball", crit_doubles=False),),
                on_success="half",
            ),
        ),
        burst_window="cold_start",
        recovery="long_rest",
        range_band="150",
        setup="Fireball is cast in the burst turn.",
        resources=("3rd-level slot",),
        notes=("Uses the ranged AoE default of three meaningful targets.",),
    )


def druid_conjure_woodland_beings_13() -> DamageRoutine:
    return DamageRoutine(
        name="Druid 13 Conjure Woodland Beings Movement",
        level=13,
        category="close_aoe",
        save_events=(
            SaveEvent(
                name="Conjure Woodland Beings, 5d8, Wis half, 2 targets",
                count=1,
                save_dc=18,
                save_bonus=6,
                target_count=2,
                damage=(_dice(5, 8, "CWB", crit_doubles=False),),
                on_success="half",
            ),
        ),
        burst_window="prebuffed",
        recovery="long_rest",
        range_band="10",
        setup="The emanation is already active and the Druid can move through two targets.",
        resources=("4th-level slot", "concentration", "movement access"),
        notes=("This is movement/table-position sensitive and should not be treated as automatic multi-hit damage.",),
    )
