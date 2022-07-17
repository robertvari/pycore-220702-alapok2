import pygame
from utilities.resources import get_resource_path

TREX_IMAGE = pygame.image.load(get_resource_path("trex_idle.png")).convert_alpha()


def draw_trex(screen):
    screen.blit(TREX_IMAGE, (0, 250))