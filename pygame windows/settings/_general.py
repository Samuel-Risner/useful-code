import pygame

GAME_NAME   = "TEST"
"""The name of the window."""
FPS         = 60
"""The standard FPS for when tha game is running."""
FPS_IDLE    = 30
"""Slower FPS for start- and endscreen or other parts of the program that need fewer ressources.."""

FULLSCREEN_KEYS = [pygame.K_f, pygame.K_F11, pygame.KSCAN_F11]
"""If one of these keys is pressed fullscreen is toggeled. No clue what `pygame.KSCAN_F11` is. Feel free to remove
it. It shouldn't affect anything."""