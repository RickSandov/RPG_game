
class Warrior:
    def __init__(self, attack_level, defense_level, life_level, warrior_name,attacks_list,defenses_list,healings_list):
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.life_level = life_level
        self.warrior_name = warrior_name
        self.attacks_list = attacks_list
        self.defenses_list = defenses_list
        self.healings_list = healings_list

    # def get_life_level(self):
    #     return self.life_level

    # def get_warrior_name(self):
    #     return self.warrior_name

    def new_attack(self,attack_level,attack_name):
        self.attacks_list.append(Attack(attack_level,attack_name))

    def new_defense(self,defense_level,defense_name,defense_duration):
        self.defenses_list.append(Defense(defense_level,defense_name,defense_duration))
    
    def new_heal(self,heal_level,heal_name):
        self.healings_list.append(Healing(heal_level,heal_name))


class Attack:
    def __init__(self, attack_level, attack_name):
        self.attack_level = attack_level
        self.attack_name = attack_name

class Defense:
    def __init__(self, defense_level, defense_name, defense_duration):
        self.defense_level = defense_level
        self.defense_name = defense_name
        self.defense_duration = defense_duration

class Healing:
    def __init__(self, heal_level,heal_name):
        self.heal_level = heal_level
        self.heal_name = heal_name

