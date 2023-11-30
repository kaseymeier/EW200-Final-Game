import pygame
import sys
from background import *

pygame.init()
clock = pygame.time.Clock()
drawbackground()
screen.blit(background, (0, 0))
gray = (200, 200, 200)

#ball
class Ball (pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/ball_soccer2.png")
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x

ball = pygame.sprite.Group()
ball.add()
ball.draw(screen)

player = pygame.image.load("assets/images/characterRed (5).png")
redplayer = pygame.Rect(2*tile_size, screen_height/2-70, 10 ,140)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect(redplayer):
        ball_speed_x *= -1

    pygame.draw.ellipse(screen, gray, ball)
    pygame.draw.rect(screen, gray, player)
    pygame.draw.rect(screen, gray, redplayer)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)