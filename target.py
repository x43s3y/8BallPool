import pygame
from ball import Ball


class Target(Ball):
    Target_RADIUS = 18
    def __init__(self, display, color, x, y):
        super().__init__(display, color, x, y)

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Target.Target_RADIUS)