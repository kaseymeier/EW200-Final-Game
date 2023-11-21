import pygame
import sys
from background import *
import random

pygame.init()
clock = pygame.time.Clock()
drawbackground()
screen.blit(background, (0, 0))


class BlueTeam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterBlue (5).png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        pass


# Create a sprite group
blue_sprites = pygame.sprite.Group()

# Create a row of sprites
for i in range(1):
    goalie = BlueTeam(tile_size * 2 + 20, 4 * tile_size + 16)
    blue_sprites.add(goalie)

dspacing = tile_size
for i in range(2):
    defense = BlueTeam(3 * tile_size + 40, i * 2 * dspacing + 30 + 3 * tile_size - 16)
    blue_sprites.add(defense)

midspacing = 1.25 * tile_size
for i in range(5):
    midfield = BlueTeam(6 * tile_size + 16, i * midspacing + 2 * tile_size - 16)
    blue_sprites.add(midfield)

topspacing = 1.25 * tile_size
for i in range(3):
    striker = BlueTeam(9.5 * tile_size + 30, i * topspacing + 3 * tile_size)
    blue_sprites.add(striker)

keys = pygame.key.get_pressed()
for players in blue_sprites:
    if keys[pygame.K_w]:
        players.rect.y -= players.speed
    if keys[pygame.K_s]:
        players.rect.y += players.speed

blue_sprites.update()



class RedTeam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterRed (3).png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Create a sprite group
red_sprites = pygame.sprite.Group()
# Create a row of sprites
for i in range(1):
    goalie = RedTeam(tile_size * 13 - 42, 4 * tile_size + 16)
    red_sprites.add(goalie)
dspacing = tile_size
for i in range(2):
    defense = RedTeam(11 * tile_size + 10, i * 2 * dspacing + 30 + 3 * tile_size - 16)
    red_sprites.add(defense)
midspacing = 1.25 * tile_size
for i in range(5):
    midfield = RedTeam(9 * tile_size - 32, i * midspacing + 2 * tile_size - 16)
    red_sprites.add(midfield)
topspacing = 1.25 * tile_size
for i in range(3):
    striker = RedTeam(4.5 * tile_size + 16, i * topspacing + 3 * tile_size)
    red_sprites.add(striker)

red_sprites.update()
red_sprites.draw(screen)
blue_sprites.draw(screen)

# rows of red players

# rows of blue players


pygame.display.flip()
clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for player in blue_sprites:
                    player.is_moving_up = True
            elif event.key == pygame.K_s:
                for player in blue_sprites:
                    player.is_moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                for player in blue_sprites:
                    player.is_moving_up = False
            elif event.key == pygame.K_s:
                for player in blue_sprites:
                    player.is_moving_down = False

