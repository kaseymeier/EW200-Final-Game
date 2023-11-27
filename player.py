import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, team, x, y):
        pygame.sprite.Sprite.__init__(self)
        if team == 'blue':
            self.image = pygame.image.load("assets/images/characterBlue (5).png")
        else:
            self.image = pygame.image.load("assets/images/characterRed (5).png")

        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x

