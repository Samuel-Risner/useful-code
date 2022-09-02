"""Contains general settings and constants used in multiple different classes."""

import pygame

#
# - screen dimensions
#

# You should settle on these first before starting to code.

WINDOW_INIT_WIDTH   = 850
"""The initial width the screen will have when created."""
WINDOW_INIT_HEIGHT  = 480
"""The initial height the screen will have when created."""
WINDOW_MIN_WIDTH    = WINDOW_INIT_WIDTH
"""The minimum width the screen can have."""
WINDOW_MIN_HEIGHT   = WINDOW_INIT_HEIGHT
"""The minimum height the screen can have."""

#
# - misc
#

GAME_NAME   = "TEST"
"""The name of the window."""
FPS         = 60
"""The standard FPS for when tha game is running."""
FPS_IDLE    = 30
"""Slower FPS for start- and endscreen."""

FULLSCREEN_KEYS = [pygame.K_f, pygame.K_F11, pygame.KSCAN_F11]
"""If one of these keys is pressed fullscreen is toggeled. No clue what `pygame.KSCAN_F11` is. Feel free to remove
it. It shouldn't affect anything."""

#
# - colours
#

BLACK = (0, 0, 0, 255)