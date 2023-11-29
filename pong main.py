import pygame
import sys
from background import *

pygame.init()
clock = pygame.time.Clock()
drawbackground()
screen.blit(background, (0, 0))
gray = (200, 200, 200)

#ball
ball = pygame.Rect(screen_width/2- 7.5, screen_height/2-7.5, 15,15)
blueplayer = pygame.Rect(screen_width- 2*tile_size, screen_height/2 - 70, 10, 140)
redplayer = pygame.Rect(2*tile_size, screen_height/2-70, 10 ,140)

ball_speed_x = 7
ball_speed_y = 7

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    pygame.draw.rect(screen, gray, blueplayer)
    pygame.draw.rect(screen, gray, redplayer)
    pygame.draw.ellipse(screen, gray, ball)




    pygame.display.flip()
    clock.tick(60)

