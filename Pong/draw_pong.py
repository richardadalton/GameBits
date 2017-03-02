import pygame

white = 255, 255, 255


def clear_screen(screen):
    screen.fill((0, 0, 0))


# Court
def draw_court(screen):
    rectangle = (495, 0, 10, 500)
    pygame.draw.rect(screen, white, rectangle)


# Ball
def draw_ball(screen, ball):
    rectangle = (ball.x, ball.y, 20, 20)
    pygame.draw.rect(screen, white, rectangle)


# Paddles
def draw_paddle(screen, paddle):
    rectangle = (paddle.x, paddle.y, 10, paddle.size)
    pygame.draw.rect(screen, white, rectangle)


def draw_paddles(screen, pong):
    draw_paddle(screen, pong.leftPaddle)
    draw_paddle(screen, pong.rightPaddle)


# Score
def draw_score(screen, pong):
    top = (0, 0, 40, 10)
    middle = (0, 35, 40, 10)
    bottom = (0, 70, 40, 10)

    top_left = (0, 0, 10, 40)
    bottom_left = (0, 40, 10, 40)

    top_right = (30, 0, 10, 40)
    bottom_right = (30, 40, 10, 40)


    segments = [top, middle, bottom, top_left, top_right, bottom_left, bottom_right]

    digits = [
        [top, bottom, top_left, top_right, bottom_left, bottom_right],  # Zero
        [top_right,bottom_right],  # One
        [top, middle, bottom, top_right, bottom_left],  # Two
        [top, middle, bottom, top_right, bottom_right],  # Three
        [middle, top_left, top_right, bottom_right],  # Four
        [top, middle, bottom, top_left, bottom_right],  # Five
        [top, middle, bottom, top_left, bottom_left, bottom_right],  # Six
        [top, top_right, bottom_right],  # Seven
        [top, middle, bottom, top_left, top_right, bottom_left, bottom_right],  # Eight
        [top, middle, bottom, top_left, top_right, bottom_right],  # Eight
    ]


    x_offset = 400
    y_offset = 50
    for segment in digits[pong.left_score]:
        (x, y, width, height) = segment
        offset_segment = (x + x_offset, y + y_offset, width, height)
        pygame.draw.rect(screen, white, offset_segment)


    x_offset = 560
    y_offset = 50
    for segment in digits[pong.right_score]:
        (x, y, width, height) = segment
        offset_segment = (x + x_offset, y + y_offset, width, height)
        pygame.draw.rect(screen, white, offset_segment)


def draw_pong(screen, pong):
    clear_screen(screen)
    draw_court(screen)
    draw_ball(screen, pong.ball)
    draw_paddles(screen, pong)
    draw_score(screen, pong)
    pygame.display.update()


