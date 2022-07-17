import pygame
from utilities.resources import get_resource_path

CACTUS_IMAGE = pygame.image.load(get_resource_path("cactus_01.png")).convert_alpha()
BIRD_IMAGE = pygame.image.load(get_resource_path("bird_01.png")).convert_alpha()


def draw_cactus(screen):
    screen.blit(CACTUS_IMAGE, (300, 250))


def draw_bird(screen):
    screen.blit(BIRD_IMAGE, (600, 150))