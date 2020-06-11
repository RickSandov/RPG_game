from wizard import merlin
from knight import sirnyro
import game_functions as game
from functions import pause_and_clear as clear


normal_pause = 1.5
long_pause = 3
very_long_pause = 7

# Creating the player and the enemy
while True:
    player = int(input('\n\n1.- Knight              2.- Wizard\n\nType the number of the player you\'d like to use ---> '))
    name = input('Name of your character --> ')
    if player == 1: 
        player = sirnyro
        player.warrior_name = name
        enemy = merlin
        break
    elif player == 2: 
        player = merlin
        player.warrior_name = name
        enemy = sirnyro 
        break

clear(normal_pause)

# Set the difficulty of the enemy
while True:
    difficulty = int(input('\n\nDifficulty levels:             1.- Easy          2.- Normal          3.- Hard\n\nType the number of the difficulty you\'d like to play ---> '))
    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        break
    print('Choose a valid difficulty')

clear(normal_pause)

if difficulty == 1: 
    difficulty_string = 'easy'
    game.set_difficulty(enemy,'easy',10,100,40)
elif difficulty == 2: 
    difficulty_string = 'normal'
    game.set_difficulty(enemy,'normal',15,120,25)
elif difficulty == 3: 
    difficulty_string = 'hard'
    game.set_difficulty(enemy,'hard',25,150,35)

print('\n\nLoading game...')
clear(very_long_pause)

print('\n\nTIME TO FIGHT!!!\n\nYou play first...')

while True:
    # Set game over
    if player.life_level <= 0:
        print('\n\nWOOOAA. You\'ve lost!! You\'re weak...\n\n')
        break
    elif enemy.life_level <= 0:
        print('\n\nUNBELIEVABLE. You\'ve defeated your oponent!! Congratulations... Want a beer?\n\n')
        break
    
    print('\n\nWait...\n\n')
    clear(long_pause)

    player_special_power = False
    enemy_special_power = False

    print('\n\nShaking cards...\n\n')

    clear(long_pause)

    # Set if the player can use their special power
    player_special_power = game.player_special_power(difficulty_string)
    enemy_special_power = game.enemy_special_power(difficulty_string)

    player_attack_option = player.attacks_list[(game.random_ability(player.attacks_list))]
    player_defense_option = player.defenses_list[(game.random_ability(player.defenses_list))]
    player_heal_option = player.healings_list[(game.random_ability(player.healings_list))]

    enemy_attack_option = enemy.attacks_list[(game.random_ability(enemy.attacks_list))]
    enemy_defense_option = enemy.defenses_list[(game.random_ability(enemy.defenses_list))]
    enemy_heal_option = enemy.healings_list[(game.random_ability(enemy.healings_list))]
    
    print(f'\n\n{player.warrior_name}\'s current info.\nlife: {int(player.life_level)}               defense: {player.defense_level}')
    print(f'\n\n{enemy.warrior_name}\'s current info.\nlife: {int(enemy.life_level)}               defense: {enemy.defense_level}')

    print('\n\nYour options are:\n\n')
    
    print(f'1.- Attack: {player_attack_option.attack_name}({player_attack_option.attack_level})           2.- Defense: {player_defense_option.defense_name}({player_defense_option.defense_level}%)            3.- Heal: {player_heal_option.heal_name}({player_heal_option.heal_level})')

    if player_special_power:
        if enemy.warrior_name == 'SirNyro':
            print('\nYou can use your special power (UNDERWORLD HELP). Steal part of your opponent\'s life and heal yourself with that stolen life.\nType 4 to choose it!\n')
        else:
            print('\nYou can use your special power (SUMMON LIGHTNING). Burn your opponent\'s spell and attack your opponent.\nType 4 to choose it!\n')

    player_option = int(input('Type the number of what you want to do ---> '))
    
    if player_option == 1: 
        player.attack_level = player_attack_option.attack_level
        game.Attack(player,enemy)
        print('\n\nYou attacked your opponent...\n\n')
    elif player_option == 2: 
        player.defense_level = player_defense_option.defense_level
        print('\n\nYou changed your defense...\n\n')
    elif player_option == 3: 
        player.life_level += player_heal_option.heal_level
        print('\n\nYou healed yourself...\n\n')
    elif player_option == 4 and player_special_power == True:
        if enemy.warrior_name == 'SirNyro':
            player.StealLife(player,enemy)
        else:
            player.SummonLightning(enemy)

    continue_playing = input("\n\nPress enter to continue...\n\n")
    
    clear(.1)
    
    if enemy.life_level <= 0:
        print('\n\nUNBELIEVABLE. You\'ve defeated your oponent!! Congratulations... Want a beer?\n\n')
        break

    print(f'\n\n{player.warrior_name}\'s current info.\nlife: {int(player.life_level)}               defense: {player.defense_level}')
    print(f'\n\n{enemy.warrior_name}\'s current info.\nlife: {int(enemy.life_level)}               defense: {enemy.defense_level}')

    print(f'\n\n{enemy.warrior_name}\'s options are:\n\n')
    
    print(f'1.- Attack: {enemy_attack_option.attack_name}({enemy_attack_option.attack_level})           2.- Defense: {enemy_defense_option.defense_name}({enemy_defense_option.defense_level}%)            3.- Heal: {enemy_heal_option.heal_name}({enemy_heal_option.heal_level})')

    if enemy_special_power == True:
        if enemy.warrior_name == 'SirNyro':
            print(f'\n{enemy.warrior_name} can use his special power (UNDERWORLD HELP). Steal part of your life and heal himself with that stolen life.\n\n')
        else:
            print(f'\n{enemy.warrior_name} can use his special power (SUMMON LIGHTNING). Burn your spell book and attack you.\n\n')

    if enemy_special_power: enemy_option = 4
    elif enemy.life_level < 30: enemy_option = 3
    elif enemy.defense_level < enemy_defense_option.defense_level: enemy_option = 2
    elif player.life_level > enemy.life_level or player.life_level > 60: enemy_option = 1
    elif enemy.life_level < 65 or enemy.life_level < player.life_level: enemy_option = 3
    else: enemy_option = 2

    if enemy_option == 1: 
        if difficulty_string == 'easy': enemy.attack_level = enemy_attack_option.attack_level * .8
        elif difficulty_string == 'hard': enemy.attack_level = enemy_attack_option.attack_level * 1.2
        else: enemy.attack_level = enemy_attack_option.attack_level
        game.Attack(enemy,player)
        print(f'\n\n{enemy.warrior_name} attacked you!!!\n\n')
    elif enemy_option == 2: 
        enemy.defense_level = enemy_defense_option.defense_level
        print(f'\n\n{enemy.warrior_name} changed his defense...\n\n')
    elif enemy_option == 3: 
        enemy.life_level += enemy_heal_option.heal_level
        print(f'\n\n{enemy.warrior_name} healed himself...\n\n')
    elif enemy_option == 4 and enemy_special_power == True:
        if enemy.warrior_name == 'Merlín':
            enemy.StealLife(enemy,player)
        else:
            enemy.SummonLightning(player)

    continue_playing = input("\n\nPress enter to continue...\n\n")
    
    clear(.1)
