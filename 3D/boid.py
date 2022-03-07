import random
import math
import numpy as np
from utils import Utils


class Boid:

    def __init__(self, world_size):
        self.world_size = world_size
        self.x = random.randrange(0, self.world_size)
        self.y = random.randrange(0, self.world_size)
        self.z = random.randrange(0, self.world_size)
        self.y_rotation = random.uniform(-math.pi, math.pi)
        self.z_rotation = random.uniform(-math.pi, math.pi)
        self.test_heading = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]
        self.test_heading = Utils.normalize(self.test_heading)

    def move(self):
        self.x += self.test_heading[0]
        self.y += self.test_heading[1]
        self.z += self.test_heading[2]
        self.wrap()

    def wrap(self):
        if self.x > self.world_size:
            self.x -= self.world_size
        if self.y > self.world_size:
            self.y -= self.world_size
        if self.z > self.world_size:
            self.z -= self.world_size
        if self.x < 0:
            self.x += self.world_size
        if self.y < 0:
            self.y += self.world_size
        if self.z < 0:
            self.z += self.world_size

    def get_pos(self):
        return self.x, self.y

