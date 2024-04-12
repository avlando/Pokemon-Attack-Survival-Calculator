# TO DO:
# Fix bug where incorrect damage rolls are calculated for lower than 252 EV
# Typing for Type modifier
# Natures for Atk, Def, Sp. Atk, and Sp. Def
# Crit off and on


from itertools import product
import math

IV = 31
level = 50
nature = 1.0
base_power = 75
Crit = 1.5
STAB = 1.5
Type = 1.0

atk_base = (100, 130, 100, 63, 60, 97) #Urshifu (Single Strike)
atk_EV = (4, 252, 0, 0, 0, 252)

def_base = (55, 55, 55, 135, 135, 135) #Flutter Mane
def_EV = (4, 0, 0, 252, 0, 252)

atk_HP_stat = math.floor(((2 * atk_base[0] + IV + math.floor(atk_EV[0] / 4)) * level) / 100) + level + 10
atk_attack_stat = math.floor(((math.floor(2*atk_base[1] + IV + math.floor(atk_EV[1]/4))*level/100)+5)*nature)
atk_defense_stat = math.floor(((math.floor(2*atk_base[2] + IV + math.floor(atk_EV[2]/4))*level/100)+5)*nature)
atk_sp_attack_stat = math.floor(((math.floor(2*atk_base[3] + IV + math.floor(atk_EV[3]/4))*level/100)+5)*nature)
atk_sp_defense_stat = math.floor(((math.floor(2*atk_base[4] + IV + math.floor(atk_EV[4]/4))*level/100)+5)*nature)
atk_speed_stat = math.floor(((math.floor(2*atk_base[5] + IV + math.floor(atk_EV[5]/4))*level/100)+5)*nature)

def_HP_stat = math.floor(((2 * def_base[0] + IV + math.floor(atk_EV[0] / 4)) * level) / 100) + level + 10
def_attack_stat = math.floor(((math.floor(2*def_base[1] + IV + math.floor(def_EV[1]/4))*level/100)+5)*nature)
def_defense_stat = math.floor(((math.floor(2*def_base[2] + IV + math.floor(def_EV[2]/4))*level/100)+5)*nature)
def_sp_attack_stat = math.floor(((math.floor(2*def_base[3] + IV + math.floor(def_EV[3]/4))*level/100)+5)*nature)
def_sp_defense_stat = math.floor(((math.floor(2*def_base[4] + IV + math.floor(def_EV[4]/4))*level/100)+5)*nature)
def_speed_stat = math.floor(((math.floor(2*def_base[5] + IV + math.floor(def_EV[5]/4))*level/100)+5)*nature)

def custom_round(x):
    """Custom rounding method to round down at 0.5"""
    return int(x + 0.5) if x - int(x) >= 0.5 else int(x)

def damage_calc(level, base_power, atk_attack_stat, def_defense_stat):
    # Calculate the intermediate values, rounding each multiplication to the nearest integer
    damage = ((2 * level / 5 + 2) * base_power * (atk_attack_stat / def_defense_stat) / 50 + 2)
    damage = custom_round(damage) * Crit #Apply Crit modeifier here
    # Multiply by the modifiers
    return damage

# Applying modifiers (in order of priority)

damage_rolls = []
for i in range(85, 101):  # Multiply by 0.85 to 1, inclusive
    multiplier = i / 100  # Convert the range to a float multiplier
    damage = math.floor(damage_calc(level, base_power, atk_attack_stat, def_defense_stat) * multiplier)
    damage_rolls.append(damage)

# Apply STAB modifier rounding
damage_rolls = [math.floor(damage * STAB) for damage in damage_rolls]

# Apply Type modifier rounding
damage_rolls = [math.floor(damage * Type) for damage in damage_rolls]

Min_roll = min(damage_rolls)
Max_roll = max(damage_rolls)

# print("Attacking Pokemon HP stat:", atk_HP_stat)
# print("Attacking Pokemon Attack stat:", atk_attack_stat)
# print("Attacking Pokemon Defense stat:", atk_defense_stat)
# print("Attacking Pokemon Sp. Atk stat:", atk_sp_attack_stat)
# print("Attacking Pokemon Sp. Def stat:", atk_sp_defense_stat)
# print("Attacking PokemonSpeed stat:", atk_speed_stat)

# print("Defending Pokemon HP stat:", def_HP_stat)
# print("Defending Pokemon Attack stat:", def_attack_stat)
# print("Defending Pokemon Defense stat:", def_defense_stat)
# print("Defending Pokemon Sp. Atk stat:", def_sp_attack_stat)
# print("Defending Pokemon Sp. Def stat:", def_sp_defense_stat)
# print("Defending PokemonSpeed stat:", def_speed_stat)

print(atk_EV[1],"Urshifu (Single Strike) Wicked Blow vs.",def_EV[0],"HP /",def_EV[2],"Def Flutter Mane on a crital hit:",damage_rolls[0],"-",damage_rolls[-1], "(",math.floor(Min_roll/def_HP_stat * 100),"% -",math.floor(Max_roll/def_HP_stat * 100),"%)")

attack_1 = damage_rolls
attack_2 = [60, 61, 61, 63, 63, 64, 64, 66, 66, 67, 67, 69, 69, 70, 70, 72]

combinations = list(product(attack_1, attack_2))
count = sum(1 for combination in combinations if sum(combination) >= def_HP_stat)

print("Number of damage rolls equal to", def_HP_stat ,"or more:", count)
print("Chance to Survive:", (1 - count / len(combinations)) * 100,"%")
