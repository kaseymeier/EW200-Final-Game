import random
import time
from background import *

pygame.init()
pygame.mixer.init()
background_sound = pygame.mixer.Sound("assets/sounds/soccer_stadium.wav")
blue_sound = pygame.mixer.Sound("assets/sounds/blue_sound.wav")
red_sound = pygame.mixer.Sound("assets/sounds/red_sound.wav")
clock = pygame.time.Clock()


def show_title_screen():
    title_font = pygame.font.Font("Oswald-Bold.ttf", 100)
    subtitle_font = pygame.font.Font("Oswald-Bold.ttf", 40)
    title_picture = pygame.image.load("assets/images/title screen.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.blit(title_picture, (0, 0))
        title_text = title_font.render("Soccer Pong", True, (0, 0, 0))
        subtitle_text = subtitle_font.render("Press Enter to Start OR Backspace to Quit", True, (0, 0, 0))

        title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 3))
        subtitle_rect = subtitle_text.get_rect(center=(screen_width / 2, screen_height / 2))

        screen.blit(title_text, title_rect)
        screen.blit(subtitle_text, subtitle_rect)

        pygame.display.flip()
        clock.tick(60)


show_title_screen()

drawbackground()
background_sound.play(-1)
gray = (200, 0, 0)
lightblue = (0, 0, 200)
red = (200, 0, 0)
black = (0, 0, 0)

scaling_factor = 1.25
ball = pygame.Rect(screen_width / 2 - 30, screen_height / 2 - 30, 2, 2)
ball1_image = pygame.image.load("assets/images/ball_soccer2.png").convert_alpha()
ball_image = pygame.transform.scale(ball1_image, (
ball1_image.get_width() * scaling_factor, ball1_image.get_height() * scaling_factor))

blueplayer = pygame.Rect(13 * tile_size - 10, screen_height / 2 - 70, 12, 150)
redplayer = pygame.Rect(2 * tile_size, screen_height / 2 - 70, 12, 150)

ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))
blueplayer_speed = 0
redplayer_speed = 0

blueplayer_score = 0
redplayer_score = 0
game_font = pygame.font.Font("Oswald-Bold.ttf", 64)

score_time = None


def ball_restart():
    global ball_speed_x, ball_speed_y, blueplayer_score, redplayer_score, score_time

    pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y = 5 * random.choice((1, -1))
    ball_speed_x = 5 * random.choice((1, -1))
    time.sleep(1)

# random bench team sprites
class Redbench(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterRed (3).png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 13 * tile_size - self.rect.width)
        self.rect.y = random.randint(0, tile_size - self.rect.height)
        self.dx = random.choice([1, 1])  # Random direction along the x-axis
        self.dy = random.choice([1, 1])  # Random direction along the y-axis

    def update(self):
        # Move the sprite
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Bounce off the walls
        if self.rect.left < tile_size or self.rect.right > 2 * tile_size:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > tile_size:
            self.dy = -self.dy

    def rotate_90_degrees(self):
        # Rotate the sprite by 90 degrees
        self.rotate_90_degrees()
        self.rect = self.image.get_rect(center=self.rect.center)

all_sprites = pygame.sprite.Group()

# Create random sprites
for _ in range(9):
    red = Redbench()
    all_sprites.add(red)

class Bluebench(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/characterBlue (5).png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(2, 13 * tile_size - self.rect.width)
        self.rect.y = random.randint(0, tile_size - self.rect.height)
        self.dx = random.choice([1, 1])  # Random direction along the x-axis
        self.dy = random.choice([1, 1])  # Random direction along the y-axis


    def update(self):
        # Move the sprite
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Bounce off the walls
        if self.rect.left < tile_size or self.rect.right > 2 * tile_size:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > tile_size:
            self.dy = -self.dy


# Create random sprites
for _ in range(9):
    blue = Bluebench()
    all_sprites.add(blue)

#monitors movement inputs/ key events
while redplayer_score < 5 and blueplayer_score < 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Help from Joshua Reid

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                blueplayer_speed += 10
            if event.key == pygame.K_UP:
                blueplayer_speed -= 10
            if event.key == pygame.K_w:
                redplayer_speed -= 10
            if event.key == pygame.K_s:
                redplayer_speed += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                blueplayer_speed -= 10
            if event.key == pygame.K_UP:
                blueplayer_speed += 10
            if event.key == pygame.K_w:
                redplayer_speed += 10
            if event.key == pygame.K_s:
                redplayer_speed -= 10

    blue_wins = False
    red_wins = False

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    blueplayer.y += blueplayer_speed
    redplayer.y += redplayer_speed

#bounds
    if blueplayer.top <= tile_size:
        blueplayer.top = tile_size
    if blueplayer.bottom >= 8 * tile_size:
        blueplayer.bottom = 8 * tile_size

    if redplayer.top <= tile_size:
        redplayer.top = tile_size
    if redplayer.bottom >= 8 * tile_size:
        redplayer.bottom = 8 * tile_size

    if ball.top <= tile_size or ball.bottom >= 8 * tile_size:
        ball_speed_y *= -1
    if ball.left <= tile_size:
        blueplayer_score += 1
        score_time = pygame.time.get_ticks()
        ball_restart()
    if ball.right >= 14 * tile_size:
        redplayer_score += 1
        score_time = pygame.time.get_ticks()
        ball_restart()

#collision
    if ball.colliderect(blueplayer) or ball.colliderect(redplayer):
        ball_speed_x *= -2

#draw paddles and sprites
    screen.blit(background, (0, 0))
    pygame.draw.ellipse(screen, gray, ball)
    screen.blit(ball_image, ball)
    pygame.draw.rect(screen, lightblue, blueplayer)
    pygame.draw.rect(screen, gray, redplayer)
    all_sprites.update()
    all_sprites.draw(screen)

#scores
    redplayer_text = game_font.render(f"{redplayer_score}", False, gray)
    screen.blit(redplayer_text, (6 * tile_size, tile_size))

    blueplayer_text = game_font.render(f"{blueplayer_score}", False, lightblue)
    screen.blit(blueplayer_text, (8 * tile_size + 32, tile_size))

# winners screen
    if blueplayer_score >= 5:
        screen.fill(lightblue)  # Change the background color for blue wins
        background_sound.stop()
        blue_text = game_font.render("Blue team wins!", False, gray)
        screen.blit(blue_text, (screen_width / 2 - 200, screen_height / 2))
        blue_sound.play(-1)
        blue_wins = True

    if redplayer_score >= 5:
        screen.fill(black)  # Change the background color for red wins
        background_sound.stop()
        red_text = game_font.render("Red team wins!", False, lightblue)
        screen.blit(red_text, (screen_width / 2 - 150, screen_height / 2))
        red_sound.play(-1)
        red_wins = True

    clock.tick(60)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blue_sound.stop()
            pygame.quit()
            sys.exit()
            background_sound.stop()
