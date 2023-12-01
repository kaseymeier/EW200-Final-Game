import pygame
import random
from background import  tile_size, screen



class Bluebench(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterBlue (5).png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 10*tile_size - self.rect.width)
        self.rect.y = random.randint(0, 8*tile_size - self.rect.height)
        self.dx = random.choice([-1, 1])  # Random direction along the x-axis
        self.dy = random.choice([1, 1])  # Random direction along the y-axis

    def update(self):
        # Move the sprite
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off the walls
        if self.rect.left < 8*tile_size or self.rect.right >  13*tile_size:
            self.dx = -self.dx
        if self.rect.top < 8*tile_size or self.rect.bottom > 9* tile_size:
            self.dy = -self.dy

all_sprites = pygame.sprite.Group()

# Create random sprites
for _ in range(6):
    sprite = Bluebench()
    all_sprites.add(sprite)
    all_sprites.update()
    all_sprites.draw(screen)



# Quit Pygame
pygame.quit()