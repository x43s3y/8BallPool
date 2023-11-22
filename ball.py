from abc import ABC, abstractmethod


class Ball(ABC):
    def __init__(self, display, color, x, y) -> None:
        self.display = display
        self.color = color
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        ...