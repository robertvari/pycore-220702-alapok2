import pygame, sys
from pygame import mixer
# init pygame and pygame audio mixer
pygame.init()
mixer.init()

from utilities.settings import *

# set window size
# tuple: (1200, 400)
SCREEN = pygame.display.set_mode(size=WINDOW_SIZE)

# import game assets
from game_assets.background import draw_background
from game_assets.ground import draw_ground
from game_assets.obstackes import draw_cactus, draw_bird
from game_assets.trex import draw_trex, jump

# set window title
pygame.display.set_caption(GAME_TITLE)

# set screen fps
CLOCK = pygame.time.Clock()


def main():
    def game_loop():
        while True:
            # get input events
            check_events()

            # clear previous screen
            SCREEN.fill("black")

            # draw background image
            draw_background(SCREEN)

            # draw ground
            draw_ground(SCREEN)

            # draw obstacles
            draw_cactus(SCREEN)
            draw_bird(SCREEN)

            # draw T-Rex
            draw_trex(SCREEN)

            pygame.display.update()
            CLOCK.tick(FPS)

    def check_events():
        for event in pygame.event.get():
            # exit game with window X button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # exit game with ESC button
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # SPACE event for jump
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jump()

    # start game_loop
    game_loop()


main()
