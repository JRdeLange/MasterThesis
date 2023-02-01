import random
import math
import numpy as np
from utils import Utils
from boid import Boid


class Agent(Boid):

    def __init__(self, world_size):
        super().__init__(world_size)

    def move(self):
        x, y = Utils.radians_to_vec(self.rotation)
        self.x += x
        self.y += y
        self.wrap()

    def turn(self, theta):
        self.rotation += theta

    def wrap(self):
        if self.x > self.world_size:
            self.x -= self.world_size
        if self.y > self.world_size:
            self.y -= self.world_size
        if self.x < 0:
            self.x += self.world_size
        if self.y < 0:
            self.y += self.world_size

