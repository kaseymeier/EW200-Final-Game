import pygame.key


class BlueTeam(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/images/characterBlue (5).png")
        self.rect = self.image.get_rect()
        self.rect.left = 20
        self.rect.centery = screen_height/2

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



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/images/ball_soccer2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y