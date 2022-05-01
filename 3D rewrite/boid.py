import numpy as np
import math
from scipy.spatial.transform import Rotation as R
import random
import config
from utils import Utils as U


class Boid:
    color = config.boid_color
    speed = config.boid_speed

    def __init__(self):
        self.pos = U.random_np_array(3, -1, 1)
        x, y, z = U.normalize_nparray(U.random_np_array(3, -1, 1))
        random_quat = U.construct_quaternion(z, y, z, random.uniform(-math.pi, math.pi))
        self.heading = R.from_quat(random_quat)
        self.forward = np.array(self.heading.apply(U.normalize_nparray(U.random_np_array(3, -1, 1))))
        self.rand2 = random.random() - .5
        self.rand3 = random.random() - .5
        self.alive = True
        self.id = None

    def set_id(self, id):
        self.id = id

    def move(self):
        self.pos += self.forward * Boid.speed
        change = R.from_rotvec((self.rand2*0.02, 0, self.rand3*0.02))
        self.heading *= change
        self.forward = np.array(self.heading.apply(np.array((0, 1, 0))))
        self.wrap()

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2

    def turn_by_quaternion(self, quaternion):
        change = R.from_quat(quaternion)
        self.forward = U.normalize_nparray(change.apply(self.forward))

