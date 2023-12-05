from abc import ABC, abstractmethod
import math


class Ball(ABC):
    def __init__(self, display, display_x, display_y, color, x, y) -> None:
        self.display = display
        self.display_x = display_x
        self.display_y = display_y
        self.color = color
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        ...