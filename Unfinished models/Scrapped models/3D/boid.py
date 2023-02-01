import random
import math
import numpy as np
from utils import Utils
from scipy.spatial.transform import Rotation as R

class Boid:

    def __init__(self, world_size):
        self.world_size = world_size
        self.x = random.randrange(0, self.world_size)
        self.y = random.randrange(0, self.world_size)
        self.z = random.randrange(0, self.world_size)
        self.x_rot = random.uniform(-math.pi, math.pi)
        self.y_rot = random.uniform(-math.pi, math.pi)
        self.z_rot = random.uniform(-math.pi, math.pi)
        self.heading = R.from_euler('xyz', [self.x_rot, self.y_rot, self.z_rot]).apply([0, 1, 0])
        self.heading = Utils.normalize(self.heading)

    def move(self):
        self.x += self.heading[0] * 1
        self.y += self.heading[1] * 1
        self.z += self.heading[2] * 1
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

    def get_rot(self):
        return self.x_rot, self.y_rot, self.z_rot

