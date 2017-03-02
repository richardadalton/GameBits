from config import Config
from ball import Ball
from paddle import Paddle

class Pong:
    def __init__(self, hit_wall_sound, hit_paddle_sound):
        self.leftPaddle = Paddle(Config.paddle_left_start_x, Config.paddle_left_start_y)
        self.rightPaddle = Paddle(Config.paddle_right_start_x, Config.paddle_right_start_y)
        self.ball = Ball(Config.ball_left_start_x, Config.ball_left_start_y)
        self.left_score = 0
        self.right_score = 0
        self.serve = self.serve_left
        self.hit_wall_sound = hit_wall_sound
        self.hit_paddle_sound = hit_paddle_sound

    def move_left_up(self):
        if self.leftPaddle.y > 0:
            self.leftPaddle.move_up()

    def move_left_down(self):
        if self.leftPaddle.y < (500 - 80):
            self.leftPaddle.move_down()

    def move_right_up(self):
        if self.rightPaddle.y > 0:
            self.rightPaddle.move_up()

    def move_right_down(self):
        if self.rightPaddle.y < (500 - 80):
            self.rightPaddle.move_down()

    def serve_left(self):
        self.ball = Ball(Config.ball_left_start_x, Config.ball_left_start_y, Config.ball_serve_left_vx, Config.ball_serve_left_vy)
        self.serve = self.in_play

    def serve_right(self):
        self.ball = Ball(Config.ball_right_start_x, Config.ball_right_start_y, Config.ball_serve_right_vx, Config.ball_serve_right_vy)
        self.serve = self.in_play

    def in_play(self):
        pass

    def move_ball(self):
        if self.ball.y == 0 or self.ball.y == 480:
            self.ball.bounce_off_wall()
            self.hit_wall_sound.play()

        if self.ball.x == 30 and self.leftPaddle.y <= self.ball.y <= (self.leftPaddle.y + self.leftPaddle.size):
            self.ball.bounce_off_paddle()
            self.hit_paddle_sound.play()

        if self.ball.x == 960 and self.rightPaddle.y <= self.ball.y <= (self.rightPaddle.y + self.rightPaddle.size):
            self.ball.bounce_off_paddle()
            self.hit_paddle_sound.play()

        if self.ball.x < 0:
            self.ball = Ball(Config.ball_left_start_x, Config.ball_left_start_y, 0, 0)
            self.serve = self.serve_left
            self.right_score += 1

        if self.ball.x > 1000:
            self.ball = Ball(Config.ball_right_start_x, Config.ball_right_start_y, 0, 0)
            self.serve = self.serve_right
            self.left_score += 1

        self.ball.move()



