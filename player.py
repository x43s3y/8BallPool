import math
import pygame
from ball import Ball

class Player(Ball):
    PLAYER_RADIUS = 20
    def __init__(self, display, display_x, display_y, color, x, y):
        super().__init__(display, display_x, display_y, color, x, y)

    def movement(self, location, mouse, vel_scale):
            t_x, t_y = location
            m_x, m_y = mouse
            vel_x = (m_x - t_x)/vel_scale
            vel_y = (m_y - t_y)/vel_scale
            self.x += vel_x
            self.y += vel_y

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Player.PLAYER_RADIUS)
