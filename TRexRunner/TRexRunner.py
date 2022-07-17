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
