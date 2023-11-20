import pygame
import sys
from background import *

pygame.init()
clock = pygame.time.Clock()
drawbackground()
screen.blit(background, (0, 0))
class WhiteTeam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterWhite (1).png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create a row of sprites
for i in range(1):
    goalie = WhiteTeam(tile_size*2+20, 4*tile_size+16)
    all_sprites.add(goalie)
dspacing = tile_size
for i in range(2):
     defense = WhiteTeam(3*tile_size+16, i* 2*dspacing+30 + 3*tile_size-16)
     all_sprites.add(defense)
midspacing = 1.25*tile_size
for i in range(5):
    midfield = WhiteTeam(6*tile_size+16, i *midspacing+ 2*tile_size-16 )
    all_sprites.add(midfield)
topspacing = 1.25*tile_size
for i in range(3):
    striker = WhiteTeam(9.5*tile_size+16, i *topspacing + 3*tile_size )
    all_sprites.add(striker)
    # Update
all_sprites.update()

    # Check for collisions
collisions = pygame.sprite.groupcollide(all_sprites, all_sprites, False, False)
#for sprite1, sprite2_list in collisions.items():
    #for sprite2 in sprite2_list:
        #if sprite1 != sprite2:

    # Draw
all_sprites.draw(screen)





#rows of red players

#rows of blue players


pygame.display.flip()
clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
