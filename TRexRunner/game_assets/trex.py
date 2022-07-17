import pygame
from utilities.resources import get_resource_path

TREX_FRAMES = [
    pygame.image.load(get_resource_path("trex_run_01.png")).convert_alpha(),
    pygame.image.load(get_resource_path("trex_run_02.png")).convert_alpha()
]
FRAME = 0
ANIM_SPEED = 0.1
GRAVITY = 0
ON_GROUND = True
TREX_IMAGE = TREX_FRAMES[FRAME]
TREX_RECT = TREX_IMAGE.get_rect(x=0, y=250)


def draw_trex(screen):
    global FRAME, GRAVITY, ON_GROUND

    FRAME += ANIM_SPEED
    if FRAME >= len(TREX_FRAMES):
        FRAME = 0

    # apply gravity
    GRAVITY += 1
    TREX_RECT.y += GRAVITY
    if TREX_RECT.y >= 250:
        GRAVITY = 0
        TREX_RECT.y = 250
        ON_GROUND = True

    TREX_IMAGE = TREX_FRAMES[int(FRAME)]
    screen.blit(TREX_IMAGE, TREX_RECT)


def jump():
    global GRAVITY, ON_GROUND

    if not ON_GROUND:
        return

    GRAVITY -= 20
    ON_GROUND = False