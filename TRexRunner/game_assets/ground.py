import pygame
from utilities.resources import get_resource_path

GROUND_IMAGE = pygame.image.load(get_resource_path("ground.png")).convert_alpha()
GROUND_X_POS = 0


def draw_ground(screen):
    global GROUND_X_POS
    GROUND_X_POS -= 10

    screen.blit(GROUND_IMAGE, (GROUND_X_POS, -27))