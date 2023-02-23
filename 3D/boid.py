import numpy as np
import math
from scipy.spatial.transform import Rotation as R
import random
from config import Config
from utils import Utils as U
from history import History


class Boid:

    def __init__(self, config):
        self.config = config
        self.pos = U.random_np_array(3, -1, 1)
        if config.grouped_spawn:
            self.pos = U.random_np_array(3, 0, 1)
        x, y, z = U.normalize_nparray(U.random_np_array(3, -1, 1))
        random_quat = U.construct_quaternion(z, y, z, random.uniform(-math.pi, math.pi))
        self.heading = R.from_quat(random_quat)
        self.forward = np.array(self.heading.apply(U.normalize_nparray(U.random_np_array(3, -1, 1))))
        self.alive = True
        self.id = None
        self.history = History()
        self.history.fill(self.pos)

    def set_id(self, id):
        self.id = id

    def move(self):
        self.pos += self.forward * self.config.boid_speed
        self.wrap()
        self.history.add(self.pos)

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2

    def turn_by_quaternion(self, quaternion):
        change = R.from_quat(quaternion)
        self.forward = U.normalize_nparray(change.apply(self.forward))

    def respawn(self):
        self.pos = U.random_np_array(3, -1, 1)
        x, y, z = U.normalize_nparray(U.random_np_array(3, -1, 1))
        random_quat = U.construct_quaternion(z, y, z, random.uniform(-math.pi, math.pi))
        self.heading = R.from_quat(random_quat)
        self.forward = np.array(self.heading.apply(U.normalize_nparray(U.random_np_array(3, -1, 1))))
        self.history.fill(self.pos)


