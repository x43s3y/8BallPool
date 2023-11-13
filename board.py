import pygame

class Board:
    HOLE_RADIUS = 30
    def __init__(self, color: tuple, board_width: int, board_height: int, width: int, height: int, display):
        self.color = color
        self.board_width = board_width
        self.board_height = board_height
        self.width = width
        self.height = height
        self.display = display
    
    def draw(self):
        pygame.draw.rect(self.display, self.color, (50, 55, self.board_width, self.board_height))
        pygame.draw.polygon(self.display, self.color, [[37.1, 72], [67.1, 42], [82, 55], [50, 85]])
        pygame.draw.polygon(self.display, self.color, [[425, 30], [475, 30], [475, 55], [425, 55]])
        pygame.draw.polygon(self.display, self.color, [[self.width-37.1, self.height-72], [self.width-67.1, self.height-42], [self.width-82, self.height-55], [self.width-50, self.height-85]])
        pygame.draw.polygon(self.display, self.color, [[self.width-37.1, 72], [self.width-67.1, 42], [self.width-82, 55], [self.width-50, 85]])
        pygame.draw.polygon(self.display, self.color, [[425, self.height-30], [475, self.height-30], [475, self.height-55], [425, self.height-55]])
        pygame.draw.polygon(self.display, self.color, [[37.1, self.height-72], [67.1, self.height-42], [82, self.height-55], [50, self.height-85]])
        pygame.draw.circle(self.display, (0, 0, 0), (37.1, 42), Board.HOLE_RADIUS)
        pygame.draw.circle(self.display, (0, 0, 0), (self.width/2, 30), Board.HOLE_RADIUS-5)
        pygame.draw.circle(self.display, (0, 0, 0), (self.width-37.1, 42), Board.HOLE_RADIUS)
        pygame.draw.circle(self.display, (0, 0, 0), (37.1, self.height-42), Board.HOLE_RADIUS)
        pygame.draw.circle(self.display, (0, 0, 0), (self.width/2, self.height-30), Board.HOLE_RADIUS-5)
        pygame.draw.circle(self.display, (0, 0, 0), (self.width-37.1, self.height-42), Board.HOLE_RADIUS)


