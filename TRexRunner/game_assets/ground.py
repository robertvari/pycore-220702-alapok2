import pygame
from utilities.resources import get_resource_path

GROUND_IMAGE = pygame.image.load(get_resource_path("ground.png")).convert()


def draw_round(screen):
    screen.blit(GROUND_IMAGE, (0, 0))