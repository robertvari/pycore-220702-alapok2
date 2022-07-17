import pygame

MOUNTAIN_IMAGE = pygame.image.load("resources/mountains.png")
CLOUDS_IMAGE = pygame.image.load("resources/clouds.png")


def draw_background(screen):
    screen.blit(MOUNTAIN_IMAGE, (-300, -80))