import pygame
import sys
import random
import time
from background import *

pygame.init()
clock = pygame.time.Clock()
drawbackground()
gray = (200, 200, 200)

scaling_factor = 1.25
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 2, 2)
ball1_image =  pygame.image.load("assets/images/ball_soccer2.png").convert_alpha()
ball_image =  pygame.transform.scale(ball1_image, (ball1_image.get_width() * scaling_factor, ball1_image.get_height() * scaling_factor))

blueplayer = pygame.Rect(13*tile_size-10, screen_height/2-70,10,140)
blue_image = pygame.image.load("assets/images/characterBlue (5).png")
redplayer = pygame.Rect(2*tile_size, screen_height/2-70, 10 ,140)
red_image = pygame.image.load("assets/images/characterRed (5).png")


ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
blueplayer_speed = 0
redplayer_speed = 0

blueplayer_score = 0
redplayer_score = 0
game_font = pygame.font.Font("Oswald-Bold.ttf", 64)

score_time = None




def ball_restart():
    global ball_speed_x, ball_speed_y, blueplayer_score, redplayer_score, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    # if current_time- score_time <2100:
    #     ball_speed_x = 0
    #     ball_speed_y = 0
    # else:
    ball_speed_y = 7* random.choice((1,-1))
    ball_speed_x = 7* random.choice((1,-1))
    time.sleep(1)

class Redbench(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterRed (3).png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-1, 6*tile_size - self.rect.width)
        self.rect.y = random.randint(0, tile_size - self.rect.height)
        self.dx = random.choice([1, 1])  # Random direction along the x-axis
        self.dy = random.choice([1, 1])  # Random direction along the y-axis

    def update(self):
        # Move the sprite
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off the walls
        if self.rect.left < tile_size or self.rect.right >  2*tile_size:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > tile_size:
            self.dy = -self.dy

all_sprites = pygame.sprite.Group()

# Create random sprites
for _ in range(6):
    red = Redbench()
    all_sprites.add(red)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                blueplayer_speed += 7
            if event.key == pygame.K_UP:
                blueplayer_speed -= 7
            if event.key == pygame.K_w:
                print ("w pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                blueplayer_speed -= 7
            if event.key == pygame.K_UP:
                blueplayer_speed += 7
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    blueplayer.y += blueplayer_speed

    if blueplayer.top <= tile_size:
        blueplayer.top = tile_size
    if blueplayer.bottom >= 8*tile_size:
        blueplayer.bottom = 8*tile_size

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        redplayer_speed -= 4
    #else:
        #redplayer_speed = 0

    elif keys[pygame.K_s]:
        redplayer_speed += 4
    else:
        redplayer_speed = 0

    redplayer.y += redplayer_speed

    if redplayer.top <= tile_size:
        redplayer.top = tile_size
    if redplayer.bottom >= 8*tile_size:
        redplayer.bottom = 8*tile_size

    if ball.top <= tile_size or ball.bottom >= 8*tile_size:
        ball_speed_y *= -1
    if ball.left <= tile_size:
        blueplayer_score += 1
        score_time = pygame.time.get_ticks()
        ball_restart()
    if ball.right >= 14*tile_size:
        redplayer_score += 1
        score_time = pygame.time.get_ticks()
        ball_restart()

    if ball.colliderect(blueplayer) or ball.colliderect(redplayer):
        ball_speed_x *= -1


    screen.blit(background, (0, 0))
    pygame.draw.ellipse(screen, gray, ball)
    screen.blit(ball_image, ball)
    pygame.draw.rect(screen, gray, blueplayer)
    screen.blit(blue_image, blueplayer)
    pygame.draw.rect(screen, gray, redplayer)
    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(red_image, redplayer)


    blueplayer_text = game_font.render(f"{redplayer_score}", False, gray)
    screen.blit(blueplayer_text, (6*tile_size, tile_size))

    redplayer_text= game_font.render(f"{blueplayer_score}", False, gray)
    screen.blit(redplayer_text, (8*tile_size+32, tile_size))



    pygame.display.flip()
    clock.tick(60)



# if red > blueplayer
#     draw blue winsound
#

