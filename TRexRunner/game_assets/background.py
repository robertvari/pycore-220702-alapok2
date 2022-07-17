import pygame
from utilities.resources import get_resource_path

MOUNTAIN_IMAGE = pygame.image.load(get_resource_path("mountains.png")).convert()
CLOUDS_IMAGE = pygame.image.load(get_resource_path("clouds.png")).convert_alpha()


def draw_background(screen):
    screen.blit(MOUNTAIN_IMAGE, (-300, -80))

    screen.blit(CLOUDS_IMAGE, (0, 0))