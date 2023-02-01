import random
import math
import numpy as np
from utils import Utils


class Boid:

    def __init__(self, world_size):
        self.world_size = world_size
        self.x = random.randrange(0, self.world_size)
        self.y = random.randrange(0, self.world_size)
        self.rotation = random.uniform(-math.pi, math.pi)


    def move(self):
        x, y = Utils.radians_to_vec(self.rotation)
        self.x += x
        self.y += y
        self.rotation += 0.05 + random.randrange(-1, 1) / 50.
        self.wrap()

    def wrap(self):
        if self.x > self.world_size:
            self.x -= self.world_size
        if self.y > self.world_size:
            self.y -= self.world_size
        if self.x < 0:
            self.x += self.world_size
        if self.y < 0:
            self.y += self.world_size

    def get_pos(self):
        return self.x, self.y

