import random as rnd
import warrior as warrior
from termcolor import colored

def set_difficulty(enemy,diff,attack,life,defense):
    enemy.attack_level = attack
    enemy.life_level = life
    enemy.defense_level = defense

    if diff == 'easy': return print(colored('\n\nEasy.','red')), print(colored('Your enemy makes less damage and has less life, but he has more shield.','green')), print(colored('YOU have more probability to use your SPECIAL ATTACK.','cyan'))
    elif diff == 'normal': return print(colored('\n\nNormal.','red')), print(colored('You and your enemy have the same damage, life and shield.','green')), print(colored('Normal probability to use SPECIAL ATTACK.','white'))
    elif diff == 'hard': return print(colored('\n\Hard.','red')), print(colored('Your enemy is more powerful and has more life and shield.','green')), print(colored('More probability to use SPECIAL ATTACK. (But the enemy has even more)','white'))

def random_ability(list):
    return rnd.randint(0,len(list)-1)

def player_special_power(difficulty):
    if difficulty == 'easy': probability = rnd.randint(1,6)
    elif difficulty == 'normal': probability = rnd.randint(1,8)
    elif difficulty == 'hard': probability = rnd.randint(1,5)

    if probability == 1: return True
    else: return False

def enemy_special_power(difficulty):
    if difficulty == 'easy': probability = rnd.randint(1,8)
    elif difficulty == 'normal': probability = rnd.randint(1,8)
    elif difficulty == 'hard': probability = rnd.randint(1,4)

    if probability == 1: return True
    else: return False

def Attack(player1,player2):
    damage = player1.attack_level * (player2.defense_level / 100)
    player2.life_level -= damage

 