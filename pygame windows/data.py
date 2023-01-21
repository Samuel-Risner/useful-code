from dataclasses import dataclass

import pygame

@dataclass
class Data():
    CLOCK           :pygame.time.Clock
    MONITOR_SIZE    :tuple[int, int]
    CANVAS          :pygame.Surface

    canvas_scale    :list[int]
    canvas_pos      :list[int]

    screen          :pygame.surface.Surface

    fullscreen      :bool
    window_width    :int
    window_height   :int