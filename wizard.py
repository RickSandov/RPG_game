from warrior import Warrior

class Wizard(Warrior):

    # Special ability

    def StealLife(self,wizard,enemy):
        enemy.life_level -= (enemy.life_level * .4)
        wizard.life_level += (enemy.life_level * .4)

        return print(f'\n{self.warrior_name} has requested help from the hell!!!')



merlin = Wizard(attack_level=20,defense_level=20,life_level=120,warrior_name='Merlín',attacks_list=[],defenses_list=[],healings_list=[])

# Create attacks

merlin.new_attack(40,'Fireball')
merlin.new_attack(20,'Mucusball')
merlin.new_attack(30,'Lethal sparks')
merlin.new_attack(46,'Poison enemy')
merlin.new_attack(44,'Invoke lethal snake')
merlin.new_attack(36,'Tornado')
merlin.new_attack(56,'Thunderstorm')


# Create shields

merlin.new_defense(30,'Rock shied',2)
merlin.new_defense(40,'Diamond shield',3)
merlin.new_defense(25,'Wooden shield',1)
merlin.new_defense(35,'Magic defense',3)
merlin.new_defense(15,'Grass shield',2)
merlin.new_defense(22,'Water shield', 1)


# Create heal

merlin.new_heal(15,'Nature heal')
merlin.new_heal(10,'Mermaid tears')
merlin.new_heal(5,'Mud cure')
merlin.new_heal(2,'Flower remedy')
merlin.new_heal(7,'Magic heal')
merlin.new_heal(8,'Frog blood')



