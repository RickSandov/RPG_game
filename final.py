import pygame
from wizard import merlin
from knight import sirnyro
import game_functions as game

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('battle1.mp3')
pygame.mixer.music.play()


player = merlin
enemy = sirnyro

black = (0, 0, 0)
red = (255, 0, 0)
grey = (149, 149, 149)
white = (255, 255, 255)
blue = (0, 93, 255)
green = (0, 120, 25)

# Players Varaibles...
player_font = pygame.font.Font('Retro.ttf', 30)
stats_font = pygame.font.Font('normal.ttf', 20)
levels_font = pygame.font.Font('Retro.ttf', 15)

player.warrior_name = player_font.render(player.warrior_name, 0, white)
enemy.warrior_name = player_font.render(enemy.warrior_name, 0, white)

shield_percent = stats_font.render('SHIELD:', 0, blue)
attack_percent = stats_font.render('ATTACK:', 0, red)


class Wizard_player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('wizard/PNG/wizard_fire/1_IDLE_000.png').convert()
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

class Knight_player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('knight/_PNG/1_KNIGHT/Knight_01__IDLE_000.png').convert()
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (570, 285))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()


def attack_card(attack_option, current_player):
    attack = stats_font.render(str(attack_option.attack_name), 0, white)
    damage = levels_font.render(str(attack_option.attack_level), 0, red)

    pygame.draw.line(screen, grey, (20, 515), (250, 515), 60)

    
    screen.blit(attack, (30, 500))
    screen.blit(damage, (30, 520))
    

def defense_card(defense_option, current_player):
    defense = stats_font.render(str(defense_option.defense_name), 0, white)
    level = levels_font.render(str(defense_option.defense_level), 0, blue)

    pygame.draw.line(screen, grey, (267, 515), (528, 515), 60)

   
    screen.blit(defense, (280, 500))
    screen.blit(level, (280, 520))
    


def heal_card(heal_option, current_player):
    heal = stats_font.render(str(heal_option.heal_name), 0, white)
    heal_level = levels_font.render(str(heal_option.heal_level), 0, green)

    pygame.draw.line(screen, grey, (545, 515), (775, 515), 60)

   
    screen.blit(heal, (555, 500))
    screen.blit(heal_level, (555, 520))
    


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

done = False

bc = pygame.image.load('background.png').convert()

merlin_sprites_list = pygame.sprite.Group()

merlin = Wizard_player()
merlin.rect.x = 90
merlin.rect.y = 330

merlin_sprites_list.add(merlin)

nyro_sprites_list = pygame.sprite.Group()

nyro = Knight_player()
nyro.rect.x = 340
nyro.rect.y = 290

nyro_sprites_list.add(nyro)




player_shield = levels_font.render(str(player.defense_level), 0, white)
enemy_shield = levels_font.render(str(enemy.defense_level), 0, white)

player_attack = levels_font.render(str(player.attack_level), 0, white)
enemy_attack = levels_font.render(str(enemy.attack_level), 0, white)

player_attack_option = player.attacks_list[(game.random_ability(player.attacks_list))]
player_defense_option = player.defenses_list[(game.random_ability(player.defenses_list))]
player_heal_option = player.healings_list[(game.random_ability(player.healings_list))]

enemy_attack_option = enemy.attacks_list[(game.random_ability(enemy.attacks_list))]
enemy_defense_option = enemy.defenses_list[(game.random_ability(enemy.defenses_list))]
enemy_heal_option = enemy.healings_list[(game.random_ability(enemy.healings_list))]


player_life_percent = (1.5625 * player.life_level)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(bc, (0, 0 ))


    attack_card(player_attack_option, player)
    defense_card(player_defense_option, player)
    heal_card(player_heal_option, player)

    player_life_percent = (1.5625 * player.life_level)
    enemy_life_percent = (1.5625 * enemy.life_level)

    # # Life Bar
    pygame.draw.line(screen, grey, (30, 80), (300, 80), 14)
    # pygame.draw.line(screen, red, (40, 80), (290, 80), 5)
    pygame.draw.line(screen, red, (40, 80), ((40 + player_life_percent), 80), 5)


    pygame.draw.line(screen, grey, (770, 80), (500, 80), 14)
    # pygame.draw.line(screen, red, (760, 80), (510, 80), 5)
    pygame.draw.line(screen, red, (510, 80), ((510 + enemy_life_percent), 80), 5)

    # # # Player names
    screen.blit(player.warrior_name, (30, 30))
    screen.blit(enemy.warrior_name, (500, 30))

    # SHIELD INFO
    screen.blit(shield_percent, (30, 120))
    screen.blit(shield_percent, (500, 120))
    screen.blit(player_shield, (110, 120))
    screen.blit(enemy_shield, (580, 120))

    # ATTACK INFO
    screen.blit(attack_percent, (30, 100))
    screen.blit(attack_percent, (500, 100))
    screen.blit(player_attack, (130, 100))
    screen.blit(enemy_attack, (600, 100))

    # SPRITES
    merlin_sprites_list.draw(screen)
    nyro_sprites_list.draw(screen)

    # KEYBOARD EVENT
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            player.attack_level = player_attack_option.attack_level
            game.Attack(player,enemy)
        elif event.key == pygame.K_h:
            player.life_level += player_heal_option.heal_level
        elif event.key == pygame.K_d:
            player.defense_level = player_defense_option.defense_level



    pygame.display.flip()
    clock.tick(60)


pygame.quit()