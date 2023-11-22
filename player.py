import time
import pygame

class Player:
    PLAYER_RADIUS = 20
    def __init__(self, display, color, x, y):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.clicked = False

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Player.PLAYER_RADIUS)
