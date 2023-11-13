import pygame

WIDTH, HEIGHT = 900, 600
BG_COLOR = (219, 148, 101)
BOARD_COLOR = (98, 189, 146)
BOARD_WIDTH, BOARD_HEIGHT = 800, 490
HOLE_RADIUS = 30
FPS = 60

pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    DISPLAY.fill(BG_COLOR)
    pygame.draw.rect(DISPLAY, BOARD_COLOR, (50, 55, BOARD_WIDTH, BOARD_HEIGHT))
    pygame.draw.polygon(DISPLAY, BOARD_COLOR, [[37.1, 72], [67.1, 42], [82, 55], [50, 85]])
    pygame.draw.polygon(DISPLAY, BOARD_COLOR, [[425, 30], [475, 30], [475, 55], [425, 55]])
    pygame.draw.polygon(DISPLAY, BOARD_COLOR, [[WIDTH-37.1, HEIGHT-72], [WIDTH-67.1, HEIGHT-42], [WIDTH-82, HEIGHT-55], [WIDTH-50, HEIGHT-85]])
    pygame.draw.polygon(DISPLAY, BOARD_COLOR, [[WIDTH-37.1, 72], [WIDTH-67.1, 42], [WIDTH-82, 55], [WIDTH-50, 85]])
    pygame.draw.polygon(DISPLAY, BOARD_COLOR, [[425, HEIGHT-30], [475, HEIGHT-30], [475, HEIGHT-55], [425, HEIGHT-55]])
    pygame.draw.polygon(DISPLAY, BOARD_COLOR, [[37.1, HEIGHT-72], [67.1, HEIGHT-42], [82, HEIGHT-55], [50, HEIGHT-85]])
    pygame.draw.circle(DISPLAY, (0, 0, 0), (37.1, 42), HOLE_RADIUS)
    pygame.draw.circle(DISPLAY, (0, 0, 0), (WIDTH/2, 30), HOLE_RADIUS-5)
    pygame.draw.circle(DISPLAY, (0, 0, 0), (WIDTH-37.1, 42), HOLE_RADIUS)
    pygame.draw.circle(DISPLAY, (0, 0, 0), (37.1, HEIGHT-42), HOLE_RADIUS)
    pygame.draw.circle(DISPLAY, (0, 0, 0), (WIDTH/2, HEIGHT-30), HOLE_RADIUS-5)
    pygame.draw.circle(DISPLAY, (0, 0, 0), (WIDTH-37.1, HEIGHT-42), HOLE_RADIUS)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()