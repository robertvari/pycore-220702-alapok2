import pygame
from utilities.resources import get_resource_path

CACTUS_IMAGE = pygame.image.load(get_resource_path("cactus_01.png")).convert_alpha()


BIRD_FRAMES = [
    pygame.image.load(get_resource_path("bird_01.png")).convert_alpha(),
    pygame.image.load(get_resource_path("bird_02.png")).convert_alpha()
]
FRAME = 0
ANIM_SPEED = 0.1
BIRD_IMAGE = BIRD_FRAMES[FRAME]


def draw_cactus(screen):
    screen.blit(CACTUS_IMAGE, (300, 250))


def draw_bird(screen):
    global FRAME
    FRAME += ANIM_SPEED
    if FRAME >= len(BIRD_FRAMES):
        FRAME = 0

    BIRD_IMAGE = BIRD_FRAMES[int(FRAME)]
    screen.blit(BIRD_IMAGE, (600, 150))