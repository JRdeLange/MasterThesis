import random
import math
import numpy as np
from utils import Utils


class Boid:

    def __init__(self, size):
        self.size = size
        self.x = random.randrange(0, size)
        self.y = random.randrange(0, size)
        self.rotation = random.uniform(-math.pi, math.pi)


    def move(self):
        x, y = Utils.radians_to_vec(self.rotation)
        self.x += x + 0.001 * np.sign(x)
        self.y += y + 0.001 * np.sign(y)
        self.rotation += 0.05 + random.randrange(-1, 1) / 50.
        self.wrap()

    def wrap(self):
        if self.x > self.size:
            self.x -= self.size
        if self.y > self.size:
            self.y -= self.size
        if self.x < 0:
            self.x += self.size
        if self.y < 0:
            self.y += self.size

