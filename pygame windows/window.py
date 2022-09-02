"""Contains the parent class from which all other classes in '/screens' should inherit."""

import pygame

from settings import SCREEN_INIT_WIDTH, SCREEN_INIT_HEIGHT, SCREEN_MIN_WIDTH, SCREEN_MIN_HEIGHT, FULLSCREEN_KEYS

class Window():

    def __init__(self, canvas:pygame.Surface, canvas_scale:list[int, int], canvas_pos:list[int, int],
        clock:pygame.time.Clock, fps:int, monitor_size:tuple[int, int]):
        """All parameters passed are considered constants that will be used and not changed or objects that will
        be manipulated"""

        self.canvas = canvas
        self.canvas_scale = canvas_scale
        self.canvas_pos = canvas_pos
        self.monitor_size = monitor_size

        self.clock = clock
        self.fps = fps

        self.run = True
        """The game loop only runs aslong as this value is 'True'."""

    def set_variables(self, fullscreen:bool, window_width:int, window_height:int, screen:pygame.Surface):
        """Sets some variables zhat will be used and changed. This should be called after creating the object.
        Otherwise the variables will be missing and a buch of errors will occur."""

        self.fullscreen = fullscreen
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen

    def get_variables(self) -> tuple[bool, int, int, pygame.Surface]:
        """Returns the changed variables set with the function `set_variables`."""

        return self.fullscreen, self.window_width, self.window_height, self.screen

    def on_quit(self):
        """This function is called from the main loop when the user closes the window and should be overwritten in
        all classes in '/screens'."""

        print("Quitting...")

    def draw(self):
        """This function is called from the main loop every loop and should be used to draw things to the canvas and
        should be overwritten in all classes in '/screens'."""

        print("Drawing...")

    def on_event(self, event):
        """This function is called multiple times each loop of the main loop for each single event. This function
        only needs to be overwritten if pygame events want to be accessed."""

        print("Handeling event...")

    def on_size_change(self):
        """This function is called from the main loop when the window size changes and should NOT be overwritten
        anywhere. It calculates the size the canvas has to be scaled to and the position it has to be drawn to to
        nicely on the screen."""

        w = self.screen.get_width()
        h = self.screen.get_height()

        h_rel = SCREEN_INIT_WIDTH / SCREEN_INIT_HEIGHT
        w_rel = SCREEN_INIT_HEIGHT / SCREEN_INIT_WIDTH

        h_new = w * w_rel
        w_new = h * h_rel

        if w_new > w:
            self.canvas_scale[0] = w
            self.canvas_scale[1] = h_new
        else:
            self.canvas_scale[0] = w_new
            self.canvas_scale[1] = h

        self.canvas_pos[0] = (w - self.canvas_scale[0]) / 2
        self.canvas_pos[1] = (h - self.canvas_scale[1]) / 2

    def main_loop(self):
        """The main loop. It should not be overwritten anywhere. It calls different functions that can be
        overwritten: `on_quit`, `draw` and `on_event`. The loop continues indefinetly aslong as `self.run` is 'True'
        or until the user closes the window and `on_quit` is called. If the programm does not terminate then,
        it will return automatically."""

        while self.run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_quit()
                    return

                if event.type == pygame.VIDEORESIZE:
                    if not self.fullscreen:
                        self.window_width, self.window_height = event.w, event.h

                        if self.window_width < SCREEN_MIN_WIDTH:
                            self.window_width = SCREEN_MIN_WIDTH
                        if self.window_height < SCREEN_MIN_HEIGHT:
                            self.window_height = SCREEN_MIN_HEIGHT

                        self.screen = pygame.display.set_mode(
                            (self.window_width, self.window_height),
                            pygame.RESIZABLE
                        )
                        self.on_size_change()

                if event.type == pygame.KEYDOWN:

                    if event.key in FULLSCREEN_KEYS:
                        self.fullscreen = not self.fullscreen

                        if self.fullscreen:
                            self.screen = pygame.display.set_mode(self.monitor_size, pygame.FULLSCREEN)
                            self.on_size_change()
                        else:
                            self.screen = pygame.display.set_mode(
                                (self.window_width, self.window_height),
                                pygame.RESIZABLE
                            )

                self.on_event(event)

            self.draw()

            self.screen.blit(
                pygame.transform.scale(
                    self.canvas, self.canvas_scale
                ).convert_alpha(), self.canvas_pos)

            pygame.display.update()