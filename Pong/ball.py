ball_size = 20
ball_step_size = 5


class Ball:
    def __init__(self, x, y, vx=ball_step_size, vy=ball_step_size):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def bounce_off_paddle(self):
        self.vx *= -1

    def bounce_off_wall(self):
        self.vy *= -1

    def move(self):
        self.x += self.vx
        self.y += self.vy
