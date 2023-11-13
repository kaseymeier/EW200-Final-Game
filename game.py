import pygame
from settings import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
wall = pygame.image.load("assets/images/wall0.png").convert()
floor = pygame.image.load("assets/images/floor.png").convert()

background = screen.copy()
def drawbackground():
	for i in range(SCREEN_WIDTH // TILE_SIZE):
		background.blit(wall, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
		background.blit(floor, (TILE_SIZE * i, SCREEN_HEIGHT - (2 * TILE_SIZE)))


drawbackground()
screen.blit(background, (0, 0))
pygame.display.flip()




