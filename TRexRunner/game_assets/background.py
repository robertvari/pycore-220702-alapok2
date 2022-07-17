import pygame
from utilities.resources import get_resource_path
from utilities.settings import *

MOUNTAIN_IMAGE = pygame.image.load(get_resource_path("mountains.png")).convert()

CLOUDS_IMAGE = pygame.image.load(get_resource_path("clouds.png")).convert_alpha()
CLOUDS_IMAGE_1_RECT = CLOUDS_IMAGE.get_rect(x=0, y=0)
CLOUDS_IMAGE_2_RECT = CLOUDS_IMAGE.get_rect(topleft=CLOUDS_IMAGE_1_RECT.topright)


def draw_background(screen):
    screen.blit(MOUNTAIN_IMAGE, (-300, -80))

    if CLOUDS_IMAGE_1_RECT.right < 0:
        CLOUDS_IMAGE_1_RECT.topleft = CLOUDS_IMAGE_2_RECT.topright

    if CLOUDS_IMAGE_2_RECT.right < 0:
        CLOUDS_IMAGE_2_RECT.topleft = CLOUDS_IMAGE_1_RECT.topright

    screen.blit(CLOUDS_IMAGE, CLOUDS_IMAGE_1_RECT)

    CLOUDS_IMAGE_1_RECT.x -= GROUND_SPEED // 6
    # pygame.draw.rect(screen, "blue", CLOUDS_IMAGE_1_RECT, 10)

    CLOUDS_IMAGE_2_RECT.x -= GROUND_SPEED // 6
    screen.blit(CLOUDS_IMAGE, CLOUDS_IMAGE_2_RECT)
    # pygame.draw.rect(screen, "red", CLOUDS_IMAGE_2_RECT, 10)