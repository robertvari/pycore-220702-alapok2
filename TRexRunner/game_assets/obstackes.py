import pygame
from utilities.resources import get_resource_path

CACTUS_IMAGE = pygame.image.load(get_resource_path("cactus_01.png")).convert()


def draw_cactus(screen):
    screen.blit(CACTUS_IMAGE, (100, 0))