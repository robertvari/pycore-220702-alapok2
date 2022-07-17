import pygame, sys
from pygame import mixer
# init pygame and pygame audio mixer
pygame.init()
mixer.init()


# set window size
# tuple: (1200, 400)
SCREEN = pygame.display.set_mode(size=(1200, 400))

# set window title
pygame.display.set_caption("T-Rex Runner")

# set screen fps
FPS = 60
CLOCK = pygame.time.Clock()


def main():
    def game_loop():
        while True:
            # get input events
            check_events()

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

    # start game_loop
    game_loop()

main()