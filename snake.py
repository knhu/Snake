import pygame
import sys
import random

pygame.init()

screen_width, screen_height = 800, 800

GRID_BLOCK_SIZE = 50

# FONT = pygame.font.Font("font.ttf", 100)

sc = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = GRID_BLOCK_SIZE, GRID_BLOCK_SIZE
        self.xdirection = 1
        self.ydirection = 0
        self.snakehead = pygame.Rect(self.x, self.y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
        self.snakebody = [pygame.Rect(self.x-GRID_BLOCK_SIZE, self.y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)]
        self.isdead = False

    def update(self):

        global snack

        for square in self.snakebody:
            if self.snakehead.x == square.x and self.snakehead.y == square.y:
                self.isdead = True
            if self.snakehead.x not in range(0, screen_width) or self.snakehead.y not in range(0, screen_height):
                self.isdead = True
            
            if self.isdead:
                self.x, self.y = GRID_BLOCK_SIZE, GRID_BLOCK_SIZE
                self.snakehead = pygame.Rect(self.x, self.y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
                self.snakebody = [pygame.Rect(self.x-GRID_BLOCK_SIZE, self.y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)]
                self.xdirection = 1
                self.ydirection = 0
                self.isdead = False
                snack = Snack()

        self.snakebody.append(self.snakehead)
        for i in range(len(self.snakebody)-1):
            self.snakebody[i].x, self.snakebody[i].y = self.snakebody[i+1].x, self.snakebody[i+1].y
        self.snakehead.x += self.xdirection * GRID_BLOCK_SIZE
        self.snakehead.y += self.ydirection * GRID_BLOCK_SIZE
        self.snakebody.remove(self.snakehead)

class Snack:
    def __init__(self):
        self.x = int(random.randint(0, screen_width)/GRID_BLOCK_SIZE) * GRID_BLOCK_SIZE
        self.y = int(random.randint(0, screen_height)/GRID_BLOCK_SIZE) * GRID_BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
    
    def update(self):
        pygame.draw.rect(sc, "orange", self.rect)

def drawGrid():
    for x in range(0, screen_width, GRID_BLOCK_SIZE):
        for y in range(0, screen_height, GRID_BLOCK_SIZE):
            rect = pygame.Rect(x, y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)
            pygame.draw.rect(sc, "#edeade", rect, 1)

drawGrid()

snake = Snake()

snack = Snack()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydirection = 1
                snake.xdirection = 0
            elif event.key == pygame.K_UP:
                snake.ydirection = -1
                snake.xdirection = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydirection = 0
                snake.xdirection = 1
            elif event.key == pygame.K_LEFT:
                snake.ydirection = 0
                snake.xdirection = -1
    
    snake.update()

    sc.fill('black')
    drawGrid()

    snack.update()
    

    pygame.draw.rect(sc, "green", snake.snakehead)

    for square in snake.snakebody:
        pygame.draw.rect(sc, "green", square)
    
    if snake.snakehead.x == snack.x and snake.snakehead.y == snack.y:
        snake.snakebody.append(pygame.Rect(square.x, square.y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE))
        snack = Snack()

    pygame.display.update()
    clock.tick(10)