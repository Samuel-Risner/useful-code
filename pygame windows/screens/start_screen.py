import pygame

from ._window import Window
from data import Data

class StartScreen(Window):
    
    def __init__(self, data:Data, fps:int):        
        super().__init__(data, fps)

    def on_quit(self):
        # here goes your code
        pass

    def draw(self):
        # here goes your code
        pass

    def on_event(self, event):
        # here goes your code
        pass