import pygame
from background import tile_size
from background import screen
from main import white
red_score = 0
blue_score = 0
game_font = pygame.font.Font("Oswald-Bold.ttf", 32)

red_text = game_font.render(f"{red_score}", False, white)
screen.blit(red_text, ((7*tile_size, tile_size+16)))
blue_text = game_font.render(f"{blue_score}", False, white)
screen.blit(blue_text, (8*tile_size-16, tile_size+16))
