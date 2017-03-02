import pygame
import sys
from random import random, randint

# Colours
white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0

# Board
width, height = 20, 20
cell_size = 10
pill = None

# Snake
snake_pos = (0, 0)
snake_bits = []
speed = 1
vx, vy = speed, 0
snake_length = 1

# Pygame
pygame.init()
screen = pygame.display.set_mode((width * cell_size, height * cell_size))
clock = pygame.time.Clock()


def draw_head():
    rectangle = (snake_pos[0] * cell_size, snake_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, white, rectangle)


def clear_tail(x, y):
    rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, black, rectangle)


def move_snake(pos):
    new_x = pos[0] + vx
    if new_x < 0:
        new_x = width - 1
    if new_x >= width:
        new_x = 0

    new_y = pos[1] + vy
    if new_y < 0:
        new_y = height - 1
    if new_y >= height:
        new_y = 0

    return (new_x, new_y)

def draw_pill():
    rectangle = (pill[0] * cell_size, pill[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, green, rectangle)


# Game Loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vx, vy = 0, -speed

    if keys[pygame.K_DOWN]:
        vx, vy = 0, speed

    if keys[pygame.K_LEFT]:
        vx, vy = -speed, 0

    if keys[pygame.K_RIGHT]:
        vx, vy = speed, 0

    snake_bits.append((snake_pos[0], snake_pos[1]))
    if len(snake_bits) > snake_length:
        tail = snake_bits[:1][0]
        clear_tail(tail[0], tail[1])
        snake_bits = snake_bits[1:]

    if pill is None:
        if random() < 0.3:
            pillx = randint(1, width - 1)
            pilly = randint(1, height - 1)
            pill = (pillx, pilly)
            draw_pill()
    else:
        if (snake_pos[0], snake_pos[1]) == pill:
            snake_length += 1
            pill = None

    snake_pos = move_snake(snake_pos)

    if snake_bits.__contains__(snake_pos):
        game_over = True

    clock.tick(10)
    draw_head()
    pygame.display.update()

print "Game Over"