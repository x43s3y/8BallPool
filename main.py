import time
import pygame
from board import Board
from player import Player
from target import Target

WIDTH, HEIGHT = 900, 600
BG_COLOR = (219, 148, 101)
BOARD_COLOR = (98, 189, 146)
BOARD_WIDTH, BOARD_HEIGHT = 800, 490
player_color = (210, 210, 210)
player_x, player_y = 210, 300
target_x, target_y = 600, 300
FPS = 60

pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
aiming = False

board = Board(BOARD_COLOR, BOARD_WIDTH, BOARD_HEIGHT, WIDTH, HEIGHT, DISPLAY)
player = Player(DISPLAY, player_color, player_x, player_y)
targets = [Target(DISPLAY, target_color, target_x, target_y) for target_color in range(1000, 16000, 1000)]


while running:

    DISPLAY.fill(BG_COLOR)
    board.draw()
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if DISPLAY.get_at(pygame.mouse.get_pos()) == player.color:
                aiming = True
            elif event.type == pygame.K_SPACE:
                aiming = False

    if aiming:
        pygame.draw.line(DISPLAY, "black", (player.x, player.y), (pygame.mouse.get_pos()), 5)
        time.sleep(0.01)

    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()