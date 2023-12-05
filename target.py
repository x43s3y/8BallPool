import pygame
from ball import Ball


class Target(Ball):
    RADIUS = 18
    def __init__(self, display, display_x, display_y, color, x, y):
        super().__init__(display, display_x, display_y, color, x, y)

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Target.RADIUS)