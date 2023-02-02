import pygame
from sys import exit

"""(SRH) ----------init is very important this initialize all the sub-parts of pygame such as render images,sound---------- (SRH)"""
pygame.init()

"""(SRH) ----------Display surface making---------- (SRH)"""  
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Coder")
#making clock object
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #here, we draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)
