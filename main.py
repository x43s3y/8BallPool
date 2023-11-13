import pygame
from board import Board
from player import Player

WIDTH, HEIGHT = 900, 600
BG_COLOR = (219, 148, 101)
BOARD_COLOR = (98, 189, 146)
BOARD_WIDTH, BOARD_HEIGHT = 800, 490
player_color = (210, 210, 210)
player_x = 210
player_y = 300
FPS = 60

pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

board = Board(BOARD_COLOR, BOARD_WIDTH, BOARD_HEIGHT, WIDTH, HEIGHT, DISPLAY)
player = Player(DISPLAY, player_color, player_x, player_y)

while running:

    DISPLAY.fill(BG_COLOR)
    board.draw()
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.check_if_clicked()
            print(pygame.mouse.get_pos())

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()