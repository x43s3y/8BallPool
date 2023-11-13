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

    def check_if_clicked(self):
        if self.display.get_at(pygame.mouse.get_pos()) == self.color:
            self.clicked = True
            print("CLICKED")
            while self.clicked:
                pygame.draw.line(self.display, "white", (self.x, self.y), pygame.mouse.get_pos())
                time.sleep(0.1)