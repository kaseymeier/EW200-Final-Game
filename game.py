import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 900
screen_height = 560
tile_size = 64
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FOOSEBALL')
background_image = pygame.image.load("assets/images/field.png")
wall = pygame.image.load("assets/images/border.png").convert()
background = screen.copy()



def drawbackground():

    for i in range(screen_width // tile_size):
        background.blit(wall, (tile_size * i, screen_height - tile_size))
        background.blit(wall, (tile_size * i, 0))

    for i in range(screen_height // tile_size):
        background.blit(wall, (0, tile_size * i))
        background.blit(wall, (screen_width - tile_size, tile_size * i))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.flip()
    clock.tick(60)


