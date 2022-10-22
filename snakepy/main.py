import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE),randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE),randrange(0, RES, SIZE)
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
lenght = 1
snake = [(x, y)]
score = 0
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Courier New', 16, bold=True)
font_end = pygame.font.SysFont('Courier New', 66, bold=True)
while True:
    sc.fill(pygame.Color('white'))
    
    [(pygame.draw.rect(sc, pygame.Color('black'), (i, j, SIZE-2, SIZE-2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'),(*apple, SIZE, SIZE))
    
    render_score = font_score.render(f'SCORE:{score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-lenght:]
    
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE),randrange(0, RES, SIZE)
        score += 1
        lenght += 1
        fps += 0.1
    
    if x+1 < 0 or x-1 > RES - SIZE or y+1 < 0 or y-1 > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2-200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()            
    
    pygame.display.flip()
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}
