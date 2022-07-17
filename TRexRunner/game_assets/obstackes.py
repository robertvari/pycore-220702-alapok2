import pygame
from utilities.resources import get_resource_path
from utilities.settings import *

CACTUS_IMAGE = pygame.image.load(get_resource_path("cactus_01.png")).convert_alpha()
CACTUS_X_POS = 1000

BIRD_FRAMES = [
    pygame.image.load(get_resource_path("bird_01.png")).convert_alpha(),
    pygame.image.load(get_resource_path("bird_02.png")).convert_alpha()
]
FRAME = 0
ANIM_SPEED = 0.1
BIRD_IMAGE = BIRD_FRAMES[FRAME]
BIRD_X_POS = 1400


def draw_cactus(screen):
    global CACTUS_X_POS

    CACTUS_X_POS -= GROUND_SPEED
    screen.blit(CACTUS_IMAGE, (CACTUS_X_POS, 250))


def draw_bird(screen):
    global FRAME, BIRD_X_POS

    FRAME += ANIM_SPEED
    if FRAME >= len(BIRD_FRAMES):
        FRAME = 0

    BIRD_IMAGE = BIRD_FRAMES[int(FRAME)]
    BIRD_X_POS -= GROUND_SPEED
    screen.blit(BIRD_IMAGE, (BIRD_X_POS, 150))