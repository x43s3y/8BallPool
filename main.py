import time
import pygame
from board import Board
from player import Player
from target import Target

def create_player(DISPLAY,BOARD_WIDTH, BOARD_HEIGHT, player_color, player_pos):
    obj = Player(DISPLAY,BOARD_WIDTH, BOARD_HEIGHT, player_color, *player_pos)

    return obj


WIDTH, HEIGHT = 900, 600
BG_COLOR = (219, 148, 101)
BOARD_COLOR = (98, 189, 146)
BOARD_WIDTH, BOARD_HEIGHT = 800, 490
VEL_SCALE = 20
player_color = (210, 210, 210)

FPS = 60


pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
running = True



def main():
    board = Board(BOARD_COLOR, BOARD_WIDTH, BOARD_HEIGHT, WIDTH, HEIGHT, DISPLAY)

    running = True
    clock = pygame.time.Clock()
    mouse_pos = pygame.mouse.get_pos()

    temp_player_pos = None
    player_pos = (210, 300)
    target_x, target_y, target_radius = 600, 425, Target.RADIUS
    target_idx = 13
    
    shooting = False

    player = create_player(DISPLAY, BOARD_WIDTH, BOARD_HEIGHT, player_color, player_pos)
    targets = [Target(DISPLAY,BOARD_WIDTH, BOARD_HEIGHT, target_color, target_x, target_y) for target_color in range(0, 14000, 1000)]

    #TARGETS POSITIONING
    for col in range(5, -1, -1):
        temp_target_y = target_y
        for row in range(col+1, 0, -1):
            target_y -= target_radius*2
            targets[target_idx].x = target_x
            targets[target_idx].y = target_y
            target_idx -= 1
        target_x -= target_radius*2
        target_y = temp_target_y - (target_radius*row)


    while running:
        clock.tick(FPS)
        
        DISPLAY.fill(BG_COLOR)
        board.draw()
        player.draw()
        for target_idx in range(13, -1, -1):
            targets[target_idx].draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:   
                if temp_player_pos:
                    
                    temp_player_pos = None
                    shooting = True
                else:
                    shooting = False
                    temp_player_pos = mouse_pos
                    
        #PLAYER MOVEMENT            
        if temp_player_pos and not shooting:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(DISPLAY, "black", player_pos, mouse_pos, 2)
        elif shooting:
            player.movement(player_pos, mouse_pos, VEL_SCALE, targets)
            player_pos = (player.x, player.y)

        

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()