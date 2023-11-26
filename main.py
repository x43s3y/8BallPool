import time
import pygame
from board import Board
from player import Player
from target import Target

def create_player():
    obj = Player(DISPLAY,BOARD_WIDTH, BOARD_HEIGHT, player_color, *player_pos)

    return obj


WIDTH, HEIGHT = 900, 600
BG_COLOR = (219, 148, 101)
BOARD_COLOR = (98, 189, 146)
BOARD_WIDTH, BOARD_HEIGHT = 800, 490
VEL_SCALE = 100
player_color = (210, 210, 210)
target_x, target_y = 600, 300
FPS = 60


pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
player_pos = (210, 300)

board = Board(BOARD_COLOR, BOARD_WIDTH, BOARD_HEIGHT, WIDTH, HEIGHT, DISPLAY)
targets = [Target(DISPLAY,BOARD_WIDTH, BOARD_HEIGHT, target_color, target_x, target_y) for target_color in range(1000, 15000, 1000)]

for target in targets:
    target.draw()

def main():
    running = True
    clock = pygame.time.Clock()
    mouse_pos = pygame.mouse.get_pos()

    temp_player_pos = None
    shooting = False
    player = create_player()

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        DISPLAY.fill(BG_COLOR)
        board.draw()
        player.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_player_pos:
                    player_pos = temp_player_pos
                    temp_player_pos = None
                    shooting = True
                else:
                    temp_player_pos = mouse_pos
                    shooting = False
                    


            
        if temp_player_pos and not shooting:
            pygame.draw.line(DISPLAY, "black", temp_player_pos, mouse_pos, 2)
        elif shooting:
            player.movement(player_pos, mouse_pos, VEL_SCALE)
        

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()