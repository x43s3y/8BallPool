import math
import pygame
from ball import Ball

class Player(Ball):
    RADIUS = 20
    def __init__(self, display, display_x, display_y, color, x, y):
        super().__init__(display, display_x, display_y, color, x, y)

    def movement(self, location, mouse, vel_scale, list_obj2):
            t_x, t_y = location
            m_x, m_y = mouse
            vel_x = (m_x - t_x)/vel_scale
            vel_y = (m_y - t_y)/vel_scale
            self.x += vel_x
            self.y += vel_y
            for obj2 in list_obj2:
                v1 = pygame.math.Vector2(self.x, self.y)
                v2 = pygame.math.Vector2(obj2.x, obj2.y)
                if v1.distance_to(v2) < Player.RADIUS + obj2.RADIUS - 2:
                    nv = v2 - v1
                    print("nv= ", nv)
                    m1 = pygame.math.Vector2(self.x, self.y).reflect(nv)
                    m2 = pygame.math.Vector2(obj2.x, obj2.y).reflect(nv)
                    print(m1, "====" ,m2)
                    self.x, self.y = m1.x/vel_scale, m1.y/vel_scale
                    obj2.x, obj2.y = m2.x/vel_scale, m2.y/vel_scale
        

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), Player.RADIUS)
