import sys

# uncomment the next to lines if you don't want to have the pygame info printed to the console
# import os
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "Hello from the pygame community. https://www.pygame.org/contribute.html"

import pygame

import settings
import screens
from data import Data

pygame.init()

CLOCK           = pygame.time.Clock()
MONITOR_SIZE    = (pygame.display.Info().current_w, pygame.display.Info().current_h)
CANVAS          = pygame.Surface((settings.window.INIT_WIDTH, settings.window.INIT_HEIGHT))

canvas_scale    = [settings.window.INIT_WIDTH, settings.window.INIT_HEIGHT]
canvas_pos      = [0, 0]

pygame.display.set_caption(settings.general.GAME_NAME)
screen = pygame.display.set_mode((settings.window.INIT_WIDTH, settings.window.INIT_HEIGHT), pygame.RESIZABLE)

fullscreen      = False
window_width    = settings.window.INIT_WIDTH
window_height   = settings.window.INIT_HEIGHT

DATA = Data(
    CLOCK=CLOCK,
    MONITOR_SIZE=MONITOR_SIZE,
    CANVAS=CANVAS,
    canvas_scale=canvas_scale,
    canvas_pos=canvas_pos,
    screen=screen,
    fullscreen=fullscreen,
    window_width=window_width,
    window_height=window_height
)

while True:
    a = screens.StartScreen(DATA, settings.general.FPS_IDLE)
    a.main_loop()
    a.set_variables_to_data()

    b = screens.InGame(DATA, settings.general.FPS)
    b.main_loop()
    b.set_variables_to_data()

    c = screens.EndScreen(DATA, settings.general.FPS_IDLE)
    c.main_loop()
    c.set_variables_to_data()

    break
    # You should remove this if you want to actually use this.
    # It simply makes looking at the result easier.

sys.exit()