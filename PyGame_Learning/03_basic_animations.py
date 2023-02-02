import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("NoobCoder")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#use use .convert() when we import any image to import faster and run faster...
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('I am a Noob Coder', False,'Black')


#for animation-->
#here we make snail surface to animate this:
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#for moving we need to varify its position:
snail_x_pos = 600


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if(snail_x_pos < 0):
        snail_x_pos = 800
    screen.blit(snail_surface,((snail_x_pos,300)))
    

    pygame.display.update()
    clock.tick(60)