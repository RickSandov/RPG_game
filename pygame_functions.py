### MADE BY: Ricardo Javier Sandoval Calderón



import pygame
pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
grey = (149, 149, 149)
white = (255, 255, 255)
blue = (0, 93, 255)

# Players Varaibles...
player_font = pygame.font.Font('Retro.ttf', 30)
stats_font = pygame.font.Font('normal.ttf', 20)

wizard_name = player_font.render('Merlin', 0, white)
knight_name = player_font.render('Sirnyro', 0, white)
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


## Classes

# def PlayerInfo(player_name, shield, life_percent, start_coords=(0,0), end_coords=(100,0)):
#     # Player names and Stats...
#     screen.blit(player_name, (start_coords[0], 30))
    
#     screen.blit(life_percent, (start_coords, 100))
#     screen.blit(shield, (start_coords[0], 120))

#     # Life Bar
#     pygame.draw.line(screen, grey, start_coords, end_coords, 14)
#     pygame.draw.line(screen, red, ((start_coords[0]+10), (start_coords[1])), ((end_coords[0]-10), (end_coords[1])), 5)
    
class PlayerInfo():
    def __init__(self, player_name, shield, life_percent):
        self.player_name = player_name
        self.shield = shield
        self.life_percent = (1.5625 * life_percent)
    
    def show_info(self, player_number):
        # STATIC ELEMENTS
        pygame.draw.line(screen, grey, (30, 80), (300, 80), 14)     #Grey player 1 life bar's backgorund line
        pygame.draw.line(screen, grey, (770, 80), (500, 80), 14)    #Grey player 2 life bar's backgorund line
        screen.blit(shield_percent, (30, 120))
        screen.blit(shield_percent, (500, 120))
        screen.blit(attack_percent, (30, 100))
        screen.blit(attack_percent, (500, 100))

        
            # PLAYER NAME
        screen.blit(wizard_name, (30, 30))
            # LIFE BAR
        pygame.draw.line(screen, red, (40, 80), ((40 + self.life_percent), 80), 5)
            # PLAYER STATS
            

        
            # PLAYER NAME
        screen.blit(knight_name, (500, 30))

            # LIFE BAR
        pygame.draw.line(screen, red, (510, 80), ((510 + self.life_percent), 80), 5)

    
wizard_info = PlayerInfo('Merlin',30, 120)
knight_info = PlayerInfo('Sirnyro', 40, 180)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(bc, (0, 0 ))


    wizard_info.show_info(1)
    knight_info.show_info(2)
    # # Life Bar
    # pygame.draw.line(screen, grey, (30, 80), (300, 80), 14)
    # pygame.draw.line(screen, red, (40, 80), (290, 80), 5)


    # pygame.draw.line(screen, grey, (770, 80), (500, 80), 14)
    # pygame.draw.line(screen, red, (760, 80), (510, 80), 5)

    # # # Player names and Stats...
    # screen.blit(wizard_name, (30, 30))
    # screen.blit(knight_name, (500, 30))
    # screen.blit(shield_percent, (30, 120))
    # screen.blit(shield_percent, (500, 120))
    # screen.blit(attack_percent, (30, 100))
    # screen.blit(attack_percent, (500, 100))

    merlin_sprites_list.draw(screen)
    nyro_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()