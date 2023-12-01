import pygame
import sys
from background import *
from pong_main import *
game_font = pygame.font.Font("Oswald-Bold.ttf", 64)

def bluewin (text, color, y_offset=0):
    text_surface = game_font.render("Blue Wins", True, color)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text_surface, text_rect)

screen.fill((0,0,255))