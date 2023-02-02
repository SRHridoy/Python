import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("NoobCoder")
clock = pygame.time.Clock()
#making font-->
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

""" #Plain surface making
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
#here origin starts from top left """

#image sky suface makig:
sky_surface = pygame.image.load('graphics/Sky.png')
#making ground surface:
ground_surface = pygame.image.load('graphics/ground.png')
#making text surface:
text_surface = test_font.render('I am a Noob Coder', False,'Black')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #blit-->block image transfer(put one suface to another)
    #placing sky_surface to display surface
    screen.blit(sky_surface,(0,0))
    #placing ground_surface to display surface to place it we need to check the pic size of sky_surface
    screen.blit(ground_surface,(0,300))
    #placing text surface in middle:
    screen.blit(text_surface,(300,50))
    

    pygame.display.update()
    clock.tick(60)