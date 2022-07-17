import pygame
from utilities.resources import get_resource_path
from utilities.settings import *

MOUNTAIN_IMAGE = pygame.image.load(get_resource_path("mountains.png")).convert()

CLOUDS_IMAGE = pygame.image.load(get_resource_path("clouds.png")).convert_alpha()
CLOUD_X_POS = 0


def draw_background(screen):
    global CLOUD_X_POS

    screen.blit(MOUNTAIN_IMAGE, (-300, -80))

    CLOUD_X_POS -= GROUND_SPEED / 8
    screen.blit(CLOUDS_IMAGE, (CLOUD_X_POS, 0))

