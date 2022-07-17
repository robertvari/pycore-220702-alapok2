import pygame
from utilities.resources import get_resource_path

TREX_FRAMES = [
    pygame.image.load(get_resource_path("trex_run_01.png")).convert_alpha(),
    pygame.image.load(get_resource_path("trex_run_02.png")).convert_alpha()
]
FRAME = 0
ANIM_SPEED = 0.1
TREX_IMAGE = TREX_FRAMES[FRAME]


def draw_trex(screen):
    global FRAME
    FRAME += ANIM_SPEED
    if FRAME >= len(TREX_FRAMES):
        FRAME = 0

    TREX_IMAGE = TREX_FRAMES[int(FRAME)]
    screen.blit(TREX_IMAGE, (0, 250))
