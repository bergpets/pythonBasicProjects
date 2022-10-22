import sys
import pygame

pygame.init()
size_block = 100
margin = 15
width = height = size_block*3 + margin*4
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tac-Toe")
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            raw = y_mouse // (size_block + margin)
            mas[col][raw] = 'x'
    for row in range(3):
        for col in range(3):
            if mas[col][row] == 'x':
                color = red
            else:
                color = white
            x = col*size_block + (col+1)*margin
            y = row*size_block + (row+1)*margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
    pygame.display.update()