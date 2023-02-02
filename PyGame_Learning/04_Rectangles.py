import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("NoobCoder")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)


sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('I am a Noob Coder', False,'Black')


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

#moving snail by rectangle:
snail_rect = snail_surface.get_rect(bottomright = (600,300))

#makig player surface:
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    #moving snail by rectangle:
    snail_rect.x -= 4
    if(snail_rect.right <= 0):
        snail_rect.left = 800
    screen.blit(snail_surface,(snail_rect))
    #placing player:
    # print(player_rect.left) 
    screen.blit(player_surface,(player_rect))
    

    pygame.display.update()
    clock.tick(60)