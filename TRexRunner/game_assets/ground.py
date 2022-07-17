import pygame
from utilities.resources import get_resource_path
from utilities.settings import *

GROUND_IMAGE_1 = pygame.image.load(get_resource_path("ground.png")).convert_alpha()

GROUND_IMAGE_1_RECT = GROUND_IMAGE_1.get_rect(bottomleft=(0, 400))
GROUND_IMAGE_2_RECT = GROUND_IMAGE_1.get_rect(bottomleft=GROUND_IMAGE_1_RECT.bottomright)


def draw_ground(screen):
    # ground 1
    GROUND_IMAGE_1_RECT.x -= GROUND_SPEED
    screen.blit(GROUND_IMAGE_1, GROUND_IMAGE_1_RECT)

    # debug outline for GROUND_IMAGE_1_RECT
    pygame.draw.rect(screen, "green", GROUND_IMAGE_1_RECT, 10)

    # ground 2
    GROUND_IMAGE_2_RECT.x -= GROUND_SPEED
    screen.blit(GROUND_IMAGE_1, GROUND_IMAGE_2_RECT)

    # debug outline for GROUND_IMAGE_2_RECT
    pygame.draw.rect(screen, "blue", GROUND_IMAGE_2_RECT, 10)