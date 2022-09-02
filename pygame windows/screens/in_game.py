import pygame

from window import Window

class InGame(Window):
    
    def __init__(self, canvas:pygame.Surface, canvas_scale:list[int, int], canvas_pos:list[int, int],
        clock:pygame.time.Clock, fps:int, monitor_size:tuple[int, int]):
        
        super().__init__(canvas, canvas_scale, canvas_pos, clock, fps, monitor_size)

    def on_quit(self):
        # here goes your code
        pass

    def draw(self):
        # here goes your code
        pass

    def on_event(self, event):
        # here goes your code
        pass