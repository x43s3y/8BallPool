import pygame
from ball import Ball

class Player(Ball):
    PLAYER_RADIUS = 20
    def __init__(self, display, display_x, display_y, color, x, y):
        super().__init__(display, display_x, display_y, color, x, y)
        self.clicked = False

    def movement(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Player.PLAYER_RADIUS)
