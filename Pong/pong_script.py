import pygame
import sys
from pong import Pong
from draw_pong import draw_pong

width, height = 1000, 500

pygame.init()
clock = pygame.time.Clock()
hit_wall = pygame.mixer.Sound('pong_wall.wav')
hit_paddle = pygame.mixer.Sound('pong_wall.wav')

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock( )

pong = Pong(hit_wall, hit_paddle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pong.move_left_up()

    if keys[pygame.K_a]:
        pong.move_left_down()


    if keys[pygame.K_p]:
        pong.move_right_up()

    if keys[pygame.K_l]:
        pong.move_right_down()


    if keys[pygame.K_SPACE]:
        pong.serve()

    pong.move_ball()
    draw_pong(screen, pong)
    clock.tick(50)
