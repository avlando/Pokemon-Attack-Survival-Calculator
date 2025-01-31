def ruin_ability(ability, atk_attack_stat, atk_special_attack_stat, def_defense_stat, def_special_defense_stat):
    if ability == "Tablets of Ruin":
        atk_attack_stat *= 0.75
    if ability == "Vessel of Ruin":
        atk_special_attack_stat *= 0.75
    if ability == "Sword of Ruin":
        def_defense_stat *= 0.75
    if ability == "Beads of Ruin":
        def_special_defense_stat *= 0.75
    if ability == "None":
        atk_attack_stat *= 1
        atk_special_attack_stat *= 1
        def_defense_stat *= 1
        def_special_defense_stat *= 1

    return atk_attack_stat, atk_special_attack_stat, def_defense_stat, def_special_defense_stat
