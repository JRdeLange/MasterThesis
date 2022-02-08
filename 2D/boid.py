import random


class Boid:

    def __init__(self):
        self.x = random.randrange(0, 100)
        self.y = random.randrange(0, 100)

    def move(self):
        self.x += random.randrange(-1, 2)
        self.y += random.randrange(-1, 2)
