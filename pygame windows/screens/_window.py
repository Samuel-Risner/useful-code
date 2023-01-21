"""Contains the parent class from which all other classes in '/screens' should inherit."""

import pygame

from data import Data
import settings

class Window():

    def __init__(self, data: Data, fps:int):
        self.DATA = data
        self.fps = fps

        self.run = True
        """The game loop only runs aslong as this value is 'True'."""

        self.set_variables_from_data()

    def set_variables_from_data(self):
        self.CLOCK          = self.DATA.CLOCK
        self.MONITOR_SIZE   = self.DATA.MONITOR_SIZE
        self.CANVAS         = self.DATA.CANVAS

        self.canvas_scale   = self.DATA.canvas_scale
        self.canvas_pos     = self.DATA.canvas_pos

        self.screen         = self.DATA.screen

        self.fullscreen     = self.DATA.fullscreen
        self.window_width   = self.DATA.window_width
        self.window_height  = self.DATA.window_height
    
    def set_variables_to_data(self):
        # commented out things shouldn't have been overwritten, maybe changed, but not more

        # self.DATA.CLOCK         = self.CLOCK
        # self.DATA.MONITOR_SIZE  = self.MONITOR_SIZE
        # self.DATA.CANVAS        = self.CANVAS

        # self.DATA.canvas_scale  = self.canvas_scale
        # self.DATA.canvas_pos    = self.canvas_pos

        self.DATA.screen        = self.screen

        self.DATA.fullscreen    = self.fullscreen
        self.DATA.window_width  = self.window_width
        self.DATA.window_height = self.window_height

    def on_quit(self):
        """This function is called from the main loop when the user closes the window and should be overwritten in
        all child classes."""

        print("Quitting...")

    def draw(self):
        """This function is called from the main loop and isused to draw things to the canvas and should be
        overwritten in all child classes."""

        print("Drawing...")

    def on_event(self, event):
        """This function is called multiple times each loop for every single event. This function only needs to be
        overwritten if pygame events want to be accessed."""

        print("Handeling event...")

    def on_size_change(self):
        """This function is called from the main loop when the window size changes and should NOT be overwritten
        anywhere. It calculates the size the canvas has to be scaled to and the position it has to be drawn to to
        nicely on the screen."""

        w = self.screen.get_width()
        h = self.screen.get_height()

        h_new = int(w * settings.window.RELATIVE_WIDTH)
        w_new = int(h * settings.window.RELATIVE_HEIGHT)

        if w_new > w:
            self.canvas_scale[0] = w
            self.canvas_scale[1] = h_new
        else:
            self.canvas_scale[0] = w_new
            self.canvas_scale[1] = h

        self.canvas_pos[0] = int((w - self.canvas_scale[0]) / 2)
        self.canvas_pos[1] = int((h - self.canvas_scale[1]) / 2)

    def main_loop(self):
        """The main loop. It should not be overwritten anywhere. It calls different functions that can be
        overwritten: `on_quit`, `draw` and `on_event`. The loop continues indefinetly aslong as `self.run` is 'True'
        or until the user closes the window and `on_quit` is called. If the programm does not terminate then,
        it will return automatically."""

        while self.run:
            self.DATA.CLOCK.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_quit()
                    return

                if event.type == pygame.VIDEORESIZE:
                    if not self.fullscreen:
                        self.window_width, self.window_height = event.w, event.h

                        if self.window_width < settings.window.MIN_WIDTH:
                            self.window_width = settings.window.MIN_WIDTH
                        if self.window_height < settings.window.MIN_HEIGHT:
                            self.window_height = settings.window.MIN_HEIGHT

                        self.screen = pygame.display.set_mode(
                            (self.window_width, self.window_height),
                            pygame.RESIZABLE
                        )
                        self.on_size_change()

                if event.type == pygame.KEYDOWN:

                    if event.key in settings.general.FULLSCREEN_KEYS:
                        self.fullscreen = not self.fullscreen

                        if self.fullscreen:
                            self.screen = pygame.display.set_mode(self.MONITOR_SIZE, pygame.FULLSCREEN)
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
                    self.CANVAS, self.canvas_scale
                ).convert_alpha(), self.canvas_pos)

            pygame.display.update()