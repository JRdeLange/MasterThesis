import numpy as np
import math
from scipy.spatial.transform import Rotation as R
import random
import config
from utils import Utils as U
from history import History


class Boid:
    color = config.boid_color
    speed = config.boid_speed

    def __init__(self):
        self.pos = U.random_np_array(2, -1, 1)
        if config.grouped_spawn:
            self.pos = U.random_np_array(2, 0, 1)
        self.rotation = (random.random() * 2 - 1) * math.pi
        self.forward = U.rot_to_vec(self.rotation)
        self.alive = True
        self.id = None
        self.history = History()
        self.history.fill(self.pos)

    def set_id(self, id):
        self.id = id

    def move(self):
        self.pos += self.forward * config.boid_speed
        self.wrap()
        self.history.add(self.pos)

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2

    def turn_by_rad(self, turn):
        self.rotation = U.wrap_radians(self.rotation + turn)
        self.forward = U.rot_to_vec(self.rotation)

    def turn_by_quaternion(self, quaternion):
        change = R.from_quat(quaternion)
        self.forward = U.normalize_nparray(change.apply(self.forward))

    def respawn(self):
        self.pos = U.random_np_array(2, -1, 1)
        self.rotation = (random.random() * 2 - 1) * math.pi
        self.forward = U.rot_to_vec(self.rotation)


