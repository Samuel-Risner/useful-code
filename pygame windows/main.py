import pygame

from settings import WINDOW_INIT_WIDTH, WINDOW_INIT_HEIGHT, GAME_NAME, FPS, FPS_IDLE
import screens

pygame.init()

CLOCK = pygame.time.Clock()
MONITOR_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
CANVAS = pygame.Surface((WINDOW_INIT_WIDTH, WINDOW_INIT_HEIGHT))

CANVAS_SCALE = [WINDOW_INIT_WIDTH, WINDOW_INIT_HEIGHT]
CANVAS_POS = [0, 0]

pygame.display.set_caption(GAME_NAME)
screen = pygame.display.set_mode((WINDOW_INIT_WIDTH, WINDOW_INIT_HEIGHT), pygame.RESIZABLE)

fullscreen = False
window_width = WINDOW_INIT_WIDTH
window_height = WINDOW_INIT_HEIGHT

while True:
    a = screens.StartScreen(CANVAS, CANVAS_SCALE, CANVAS_POS, CLOCK, FPS_IDLE, MONITOR_SIZE)
    a.set_variables(fullscreen, window_width, window_height, screen)
    a.main_loop()
    fullscreen, window_width, window_height, screen = a.get_variables()

    b = screens.InGame(CANVAS, CANVAS_SCALE, CANVAS_POS, CLOCK, FPS, MONITOR_SIZE)
    b.set_variables(fullscreen, window_width, window_height, screen)
    b.main_loop()
    fullscreen, window_width, window_height, screen = b.get_variables()

    c = screens.EndScreen(CANVAS, CANVAS_SCALE, CANVAS_POS, CLOCK, FPS_IDLE, MONITOR_SIZE)
    c.set_variables(fullscreen, window_width, window_height, screen)
    c.main_loop()
    fullscreen, window_width, window_height, screen = c.get_variables()

    break
    # You should remove this if you want to actually use this.
    # It simply makes looking at the result easier.