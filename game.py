import pygame
from settings import *
import sys



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
wall = pygame.image.load("assets/images/wall0.png").convert()
floor = pygame.image.load("assets/images/floor.png").convert()

background = screen.copy()
clock = pygame.time.Clock()
def drawbackground():
    #bottom
    for i in range (SCREEN_WIDTH // TILE_SIZE):
        background.blit(wall,(TILE_SIZE *i,SCREEN_HEIGHT-16 ))
    #left side
for i in range (SCREEN_HEIGHT// TILE_SIZE):
    background.blit(wall, (0, TILE_SIZE * i))
    #right side
for i in range (SCREEN_HEIGHT //TILE_SIZE):
    background.blit(wall, (SCREEN_WIDTH-16, TILE_SIZE* i))
    # ceiling
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(wall, (TILE_SIZE * i, 0))
    #floor
[background.blit(floor, (SCREEN_WIDTH - (x * TILE_SIZE), (TILE_SIZE * i + (2 * TILE_SIZE)))) for x in range(SCREEN_WIDTH-2*TILE_SIZE)) for i
 in range(SCREEN_WIDTH // TILE_SIZE)]



drawbackground()
screen.blit(background, (0, 0))
pygame.display.flip()
clock.tick(60)

while True:
    # listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


