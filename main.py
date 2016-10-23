# 21st Century Snakedown
# Python-pygame clone of the classic snake game
# Ning Yuan, ningyuan.sg@gmail.com, ningyuan.io
# With help from wailunoob's (wailunoob2@gmail.com) snake_game

import pygame, sys
from pygame.locals import *

FPS = 8
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 480
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
fpsClock = pygame.time.Clock()
# COLOURS  R :  G :  B
WHITE  = (255, 255, 255)
GREY   = (100, 100, 100)
BLACK  = (  0,   0,   0)
ORANGE = (255, 128,   0)
UP = 'up'; DOWN = 'down'; LEFT = 'left'; RIGHT = 'right'

# SNAKE
class Snake:
    # spatial
    SIZE = 20
    x = WINDOW_WIDTH / 2  # start x
    y = WINDOW_HEIGHT / 2  # start y
    head = pygame.Rect(x, y, SIZE, SIZE)  #pygame Rect Obj
    collide = False # turns True in loop if collide with border, or tail
    # directional
    direction = RIGHT  # start right
snake = Snake()

def main(snake):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)
    pygame.display.set_caption("21st Century Snakedown")

    while True:
        DISPLAYSURF.fill(BLACK)
        pygame.draw.rect(DISPLAYSURF, WHITE, snake.head)

        for event in pygame.event.get():
            # exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # change directions TODO: add wasd controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        if snake.direction == UP:
            snake.y -= snake.SIZE
            snake.head.top = snake.y
        elif snake.direction == DOWN:
            snake.y += snake.SIZE
            snake.head.top = snake.y
        elif snake.direction == RIGHT:
            snake.x += snake.SIZE
            snake.head.left = snake.x
        elif snake.direction == LEFT:
            snake.x -= snake.SIZE
            snake.head.left = snake.x

        pygame.display.update()
        fpsClock.tick(FPS)


while __name__ == '__main__':
    main(snake)
