
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        super().__init__()
        self.image = pygame.image.load("assets/images/ball_soccer2.png")
        self.rect = self.image.get_rect(center=screen_rect.center)
        self.speed = [random.uniform(-2, 2), random.uniform(-2, 2)]

    def update(self, screen_rect, RedTeam, BlueTeam):
        self.rect.move_ip(self.speed)

        # Bounce off the walls
        if self.rect.left < screen_rect.left or self.rect.right > screen_rect.right:
            self.speed[0] = -self.speed[0]
        if self.rect.top < screen_rect.top or self.rect.bottom > screen_rect.bottom:
            self.speed[1] = -self.speed[1]

collision_sprites = pygame.sprite.spritecollide(self, RedTeam, BlueTeam, False)
for sprite in collision_sprites:

width = screen_width-tile_size
height = screen_height-tile_size
screen = pygame.display.set_mode((width, height))

ball = Ball(screen.get_rect())
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

all_sprites.update(screen.get_rect(), all_sprites)
all_sprites.draw(screen)



class RandomRedSprite(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterRed (5).png")
        self.rect = self.image.get_rect(center=rect.center)
        self.speed = [random.uniform(-2, 2), random.uniform(-2, 2)]
    def update(self):
        self.rect.move_ip(self.speed)
        rect = ()
        # Bounce off the walls
        if self.rect.left < rect.left or self.rect.right > rect.right:
            self.speed[0] = -self.speed[0]
        if self.rect.top < rect.top or self.rect.bottom > rect.bottom:
            self.speed[1] = -self.speed[1]
randomredsprites = pygame.sprite.Group()

for _ in range(8):
    randomredsprite = RandomRedSprite(screen.get_rect())
    randomredsprites.add(randomredsprite)
    randomredsprites.update()
