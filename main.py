import pygame
import sys
from background import *

import pygame.key
white = (255, 255, 255)
from player import *


pygame.init()
clock = pygame.time.Clock()
drawbackground()
screen.blit(background, (0, 0))


class BlueTeam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.image.load("assets/images/characterBlue (5).png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.dy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.dy = -3
        if keystate[pygame.K_s]:
            self.dy = 3
        self.rect.y += self.dy

blue_sprites = pygame.sprite.Group()

# Create a row of sprites
for i in range(1):
    goalie = BlueTeam((tile_size * 2 + 20), (4 * tile_size + 16))
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


blue_sprites.update()
blue_sprites.draw(screen)


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

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/images/ball_soccer2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

soccer_ball = Ball(screen_width,screen_height)
ball_sprite = pygame.sprite.Group()
ball_sprite.add(soccer_ball)
ball_sprite.update()
ball_sprite.draw(screen)


all_sprites = pygame.sprite.Group()


redteam = RedTeam(screen_width, screen_height)
blueteam = BlueTeam(screen_width, screen_height)
ball = Ball(screen_width,screen_height)
all_sprites.add(redteam, blueteam, ball)
red_score = 0
blue_score = 0
game_font = pygame.font.Font("Oswald-Bold.ttf", 32)



pygame.display.flip()
clock.tick(60)
previous_time = clock.get_time()
fps = clock.get_fps()
print(previous_time)
print(fps)
game_clock = (game_font.render(f"{previous_time}", False, white))
screen.blit(game_clock, (6*tile_size, tile_size))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
