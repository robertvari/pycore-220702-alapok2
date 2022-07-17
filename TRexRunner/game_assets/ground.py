import pygame
from utilities.resources import get_resource_path

GROUND_IMAGE = pygame.image.load(get_resource_path("ground.png")).convert_alpha()


def draw_ground(screen):
    screen.blit(GROUND_IMAGE, (0, 0))