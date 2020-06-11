from warrior import Warrior

class Knight(Warrior):

    # Special ability

    def SummonLightning(self,enemy):
        enemy.life_level -= enemy.life_level * .3
        self.life_level += enemy.life_level * .3
        return print(f'\n{self.warrior_name} attacked and {enemy.warrior_name} has heal him.')



sirnyro = Knight(attack_level=20,defense_level=20,life_level=120,warrior_name='SirNyro',attacks_list=[],defenses_list=[],healings_list=[])


# Create attacks

sirnyro.new_attack(40,'Sword attack')
sirnyro.new_attack(20,'Throw rock')
sirnyro.new_attack(30,'Arrow')
sirnyro.new_attack(46,'Poisoned arrow')
sirnyro.new_attack(44,'Invoke fire wave')
sirnyro.new_attack(36,'Mallet')
sirnyro.new_attack(56,'Burned arrow')


# Create shields

sirnyro.new_defense(30,'Gold shied',2)
sirnyro.new_defense(40,'Iron shield',3)
sirnyro.new_defense(25,'Wooden shield',1)
sirnyro.new_defense(35,'Diamond shield',3)
sirnyro.new_defense(15,'Mesh armour',2)
sirnyro.new_defense(22,'Helmet', 1)


# Create heal

sirnyro.new_heal(15,'1st aid kit')
sirnyro.new_heal(10,'Bandage')
sirnyro.new_heal(5,'Mud cure')
sirnyro.new_heal(2,'Clean')
sirnyro.new_heal(7,'Energy shot')
sirnyro.new_heal(8,'Witch blood')