import pygame
from ball import Ball


class Target(Ball):
    Target_RADIUS = 18
    def __init__(self, display, display_x, display_y, color, x, y):
        super().__init__(display, display_x, display_y, color, x, y)

    # @property
    # def x(self):
    #     return self.x
    
    # @x.setter
    # def x(self, value):
    #     ...

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Target.Target_RADIUS)