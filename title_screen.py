import pygame
from pong_main import game_font
from background import*

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Function to display text on the screen
def display_text(text, color, y_offset=0):
    text_surface = game_font.render("Soccer Pong", True, color)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Display title and instructions
    display_text("Soccer Pong", white, -50)
    display_text("Press space bar to Start", white, 50)

    # Update the display
    pygame.display.flip()


    key_pressed = pygame.key.get_pressed()
    if any(key_pressed):
        break