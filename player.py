import pygame
from ball import Ball

class Player(Ball):
    PLAYER_RADIUS = 20
    def __init__(self, display, color, x, y):
        super().__init__(display, color, x, y)
        self.clicked = False

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Player.PLAYER_RADIUS)
