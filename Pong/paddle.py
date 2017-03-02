
class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 80
        self.step_size = 5

    def move_up(self):
        self.y -= self.step_size

    def move_down(self):
        self.y += self.step_size
