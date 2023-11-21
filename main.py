import pygame
import sys
from background import *

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

# Create a sprite group
blue_sprites = pygame.sprite.Group()

# Create a row of sprites
for i in range(1):
    goalie = BlueTeam(tile_size*2+20, 4*tile_size+16)
    blue_sprites.add(goalie)
dspacing = tile_size
for i in range(2):
     defense = BlueTeam(3*tile_size+40, i* 2*dspacing+30 + 3*tile_size-16)
     blue_sprites.add(defense)
midspacing = 1.25*tile_size
for i in range(5):
    midfield = BlueTeam(6*tile_size+16, i *midspacing+ 2*tile_size-16 )
    blue_sprites.add(midfield)
topspacing = 1.25*tile_size
for i in range(3):
    striker = BlueTeam(9.5*tile_size+30, i *topspacing + 3*tile_size )
    blue_sprites.add(striker)
    # Update
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
    goalie = RedTeam(tile_size*13-42, 4*tile_size+16)
    red_sprites.add(goalie)
dspacing = tile_size
for i in range(2):
     defense = RedTeam(11*tile_size+10, i* 2*dspacing+30 + 3*tile_size-16)
     red_sprites.add(defense)
midspacing = 1.25*tile_size
for i in range(5):
    midfield = RedTeam(9*tile_size-32, i *midspacing+ 2*tile_size-16 )
    red_sprites.add(midfield)
topspacing = 1.25*tile_size
for i in range(3):
    striker = RedTeam(4.5*tile_size+16, i *topspacing + 3*tile_size )
    red_sprites.add(striker)
    # Update
red_sprites.update()

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/ball_soccer2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


ball_sprite = pygame.sprite.Group()

ball_sprite.add(ball)


    # Check for collisions
collisions = pygame.sprite.groupcollide(red_sprites, blue_sprites, ball_sprite, False, False)
#for sprite1, sprite2_list in collisions.items():
    #for sprite2 in sprite2_list:
        #if sprite1 != sprite2:

    # Draw
red_sprites.draw(screen)
blue_sprites.draw(screen)
ball_sprite.draw(screen)





#rows of red players

#rows of blue players


pygame.display.flip()
clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
