from __future__ import annotations

from .core.model import AttackEvent, ConditionalDamageEvent, DamageDice, DamageRoutine, DirectDamageEvent, SaveEvent, VexChainEvent


def _dice(count: int, sides: int, label: str = "", crit_doubles: bool = True) -> DamageDice:
    return DamageDice(count, sides, crit_doubles=crit_doubles, label=label)


def all_routines() -> dict[str, DamageRoutine]:
    routines = [
        wizard_cme_scorching_ray_20(),
        valor_bard_warlock_fighter_turret_longbow_20(),
        valor_bard_warlock_fighter_turret_shortbow_20(),
        valor_bard_warlock_fighter_turret_shortbow_prior_vex_20(),
        valor_bard_warlock_fighter_turret_dual_scimitar_20(),
        valor_bard_warlock_fighter_turret_bracers_dual_scimitar_20(),
        valor_bard_warlock_fighter_turret_bracers_dual_scimitar_paralyzed_20(),
        eldritch_knight_polearm_20(),
        eldritch_knight_polearm_cme_20(),
        eldritch_knight_gwm_cme_20(),
        eldritch_knight_rapier_shield_20(),
        eldritch_knight_rapier_shield_spirit_shroud_20(),
        battle_master_polearm_20(),
        champion_polearm_20(),
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


def _paralyzed(event: AttackEvent) -> AttackEvent:
    return AttackEvent(
        name=f"Paralyzed target: {event.name}",
        count=event.count,
        attack_bonus=event.attack_bonus,
        damage=event.damage,
        flat_damage=event.flat_damage,
        advantage="advantage",
        target_ac=event.target_ac,
        crit_min=event.crit_min,
        crit_on_hit=True,
    )


def valor_bard_warlock_fighter_turret_bracers_dual_scimitar_paralyzed_20() -> DamageRoutine:
    base = valor_bard_warlock_fighter_turret_bracers_dual_scimitar_20()
    return DamageRoutine(
        name="Valor Bard16 Warlock2 Fighter2 CME Turret Bracers Dual Scimitar Paralyzed",
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


def eldritch_knight_polearm_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Polearm Spirit Shroud",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Main polearm attacks with Action Surge, 8 hits, 1d10 + 11 + 1d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "weapon"), _dice(1, 8, "Spirit Shroud")),
                flat_damage=11,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 + 11 + 1d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 4, "weapon"), _dice(1, 8, "Spirit Shroud")),
                flat_damage=11,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="10",
        setup="Spirit Shroud is already active; Action Surge is used.",
        resources=("4th-level slot: Spirit Shroud", "Action Surge", "Polearm Master", "Great Weapon Master"),
        notes=("EK's 4th-level Spirit Shroud remains 1d8; this is a martial burst anchor.",),
    )


def eldritch_knight_polearm_cme_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Polearm CME4",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Main polearm attacks with Action Surge, 8 hits, 1d10 + 11 + 2d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 10, "weapon"), _dice(2, 8, "CME4")),
                flat_damage=11,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 + 11 + 2d8",
                count=1,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(1, 4, "weapon"), _dice(2, 8, "CME4")),
                flat_damage=11,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="15",
        setup="CME is already active from EK's single 4th-level slot; Action Surge is used.",
        resources=("4th-level slot: CME", "Action Surge", "Polearm Master", "Great Weapon Master", "concentration"),
        notes=("CME adds 2d8 per hit at 4th level but requires targets within 15 feet.",),
        option_name="Eldritch Knight 20 Polearm",
    )


def eldritch_knight_gwm_cme_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Greatsword GWM CME4 Graze",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Greatsword attacks with Action Surge, 8 hits, 2d6 + 11 + 2d8",
                count=8,
                attack_bonus=11,
                target_ac=23,
                damage=(_dice(2, 6, "greatsword"), _dice(2, 8, "CME4")),
                flat_damage=11,
                miss_damage=5,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="15",
        setup="CME is already active from EK's single 4th-level slot; Action Surge is used.",
        resources=("4th-level slot: CME", "Action Surge", "Great Weapon Master", "Weapon Mastery: Graze", "concentration"),
        notes=(
            "Graze miss damage is only the Strength modifier and does not count as a hit.",
            "CME is not added to Graze damage because a missed attack is not a hit.",
        ),
        option_name="Eldritch Knight 20 Greatsword GWM",
    )


def eldritch_knight_rapier_shield_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Rapier Shield Dueling Vex Surge",
        level=20,
        category="close_burst",
        vex_events=(
            VexChainEvent(
                name="Rapier Vex chain with Action Surge, 8 attacks, 1d8 + 7",
                count=8,
                attack_bonus=13,
                target_ac=23,
                damage=(_dice(1, 8, "rapier"),),
                flat_damage=7,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="5",
        setup="Action Surge is used; Vex advantage only appears after the previous rapier hit.",
        resources=("Action Surge", "Dueling Fighting Style", "shield", "Vex"),
        notes=("This is a defensive rapier-and-shield reference, not a maximum DPR route.",),
        option_name="Eldritch Knight 20 Rapier Shield",
        exclude_from_calibration=True,
    )


def eldritch_knight_rapier_shield_spirit_shroud_20() -> DamageRoutine:
    return DamageRoutine(
        name="Eldritch Knight 20 Rapier Shield Dueling Vex Spirit Shroud Surge",
        level=20,
        category="close_burst",
        vex_events=(
            VexChainEvent(
                name="Rapier Vex chain with Action Surge, 8 attacks, 1d8 + 7 + 1d8",
                count=8,
                attack_bonus=13,
                target_ac=23,
                damage=(_dice(1, 8, "rapier"), _dice(1, 8, "Spirit Shroud")),
                flat_damage=7,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="5",
        setup="Spirit Shroud is already active; Action Surge is used; Vex advantage depends on the previous hit.",
        resources=("4th-level slot: Spirit Shroud", "Action Surge", "Dueling Fighting Style", "shield", "Vex"),
        notes=("EK's 4th-level Spirit Shroud remains 1d8; Vex is modeled as a sequential chain.",),
        option_name="Eldritch Knight 20 Rapier Shield",
        exclude_from_calibration=True,
    )


def battle_master_polearm_20() -> DamageRoutine:
    return DamageRoutine(
        name="Battle Master 20 Polearm Surge",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Main polearm attacks with Action Surge, 8 hits, 1d10 + 11",
                count=8,
                attack_bonus=13,
                target_ac=23,
                damage=(_dice(1, 10, "weapon"),),
                flat_damage=11,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 + 11",
                count=1,
                attack_bonus=13,
                target_ac=23,
                damage=(_dice(1, 4, "weapon"),),
                flat_damage=11,
            ),
        ),
        direct_events=(
            DirectDamageEvent(
                name="Superiority dice spent on hits, 6d12",
                count=1,
                damage=(_dice(6, 12, "maneuvers", crit_doubles=False),),
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="10",
        setup="Action Surge and superiority dice are committed to the burst turn.",
        resources=("Action Surge", "Polearm Master", "Great Weapon Master", "superiority dice"),
        notes=("Maneuver dice are modeled as spent on successful hits, not as separate attack rolls.",),
    )


def champion_polearm_20() -> DamageRoutine:
    return DamageRoutine(
        name="Champion 20 Polearm Surge",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name="Main polearm attacks with Action Surge, 8 hits, 1d10 + 11",
                count=8,
                attack_bonus=13,
                target_ac=23,
                damage=(_dice(1, 10, "weapon"),),
                flat_damage=11,
                crit_min=18,
            ),
            AttackEvent(
                name="Polearm Master bonus attack, 1d4 + 11",
                count=1,
                attack_bonus=13,
                target_ac=23,
                damage=(_dice(1, 4, "weapon"),),
                flat_damage=11,
                crit_min=18,
            ),
        ),
        burst_window="prebuffed",
        recovery="short_rest",
        range_band="10",
        setup="Action Surge turn with Superior Critical expanded crit range.",
        resources=("Action Surge", "Polearm Master", "Great Weapon Master"),
        notes=("Champion level 15+ crits on 18-20 with weapon attacks and Unarmed Strikes.",),
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
    trigger = "Greatsword attacks, 2 hits, 2d6 + 5 + 1d8 + 2d8 + 1d4"
    return DamageRoutine(
        name="Paladin 20 Greatsword GWM Spirit Shroud Searing Smite5 Graze",
        level=20,
        category="close_burst",
        events=(
            AttackEvent(
                name=trigger,
                count=2,
                attack_bonus=13,
                target_ac=22,
                damage=(
                    _dice(2, 6, "greatsword"),
                    _dice(1, 8, "Radiant Strikes"),
                    _dice(2, 8, "Spirit Shroud5"),
                    _dice(1, 4, "Divine Favor"),
                ),
                flat_damage=11,
                miss_damage=5,
            ),
        ),
        conditional_events=(
            ConditionalDamageEvent(
                name="5th-level Searing Smite initial and guaranteed burn damage, 10d6 if any greatsword attack hits",
                trigger_event_names=(trigger,),
                damage=(_dice(10, 6, "Searing Smite5", crit_doubles=False),),
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
            "Great Weapon Master",
            "Weapon Mastery: Graze",
            "concentration",
        ),
        notes=(
            "Searing Smite is modeled as two guaranteed 5d6 damage packets after a hit: the initial rider and the follow-up burn.",
            "If every greatsword attack misses, Searing Smite is not cast and adds no damage.",
            "Graze miss damage does not trigger Searing Smite, Spirit Shroud, Radiant Strikes, or Great Weapon Master.",
        ),
        option_name="Paladin 20 Greatsword GWM",
    )


def berserker_gwm_20() -> DamageRoutine:
    return DamageRoutine(
        name="Berserker Barbarian 20 GWM",
        level=20,
        category="close_sustained",
        events=(
            AttackEvent(
                name="Reckless greatsword attacks, 2 hits, 2d6 + STR + Rage + GWM + Frenzy",
                count=2,
                attack_bonus=13,
                target_ac=22,
                damage=(_dice(2, 6, "weapon"), _dice(4, 6, "Frenzy once-per-turn", crit_doubles=False)),
                flat_damage=15,
                advantage="advantage",
                miss_damage=7,
            ),
        ),
        burst_window="sustained",
        recovery="encounter_low_cost",
        range_band="5",
        setup="Rage is active; Reckless Attack is used.",
        resources=("Rage", "Reckless Attack", "Great Weapon Master"),
        notes=(
            "Frenzy dice are folded into the event as once-per-turn damage.",
            "Graze miss damage is modeled as Strength modifier only; Rage, GWM, and Frenzy are not added to Graze.",
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
