from utils import Utils as u
import numpy as np
import math


class Boid:

    def __init__(self):
        self.pos = u.random_np_array(3, -1, 1)
        self.heading = u.random_np_array(3, -math.pi, math.pi)

    def move(self):
        self.pos += self.heading * 0.03
        self.wrap()

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2
