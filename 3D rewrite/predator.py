import random
from scipy.spatial.transform import Rotation as R
from utils import Utils as u
import numpy as np


class Predator:
    speed = 0.02
    color = (0.2, 0.8, 0.2, 1)

    def __init__(self, world):
        self.world = world
        self.pos = u.random_np_array(3, -1, 1)
        self.heading = R.from_rotvec((random.uniform(0, 0), 0, random.uniform(0, 0)))
        self.forward = np.array(self.heading.apply(np.array((0, 1, 0))))

    def find_closest(self):
        closest_distance = 1000
        closest = None
        for boid in self.world.boids:
            dist = self.pos - boid.pos
            dist = np.sqrt(dist[0]*dist[0] + dist[1]*dist[1] + dist[2]*dist[2])
            if dist < closest_distance:
                closest_distance = dist
                closest = boid

        if closest_distance < 0.02:
            closest.alive = False
            self.world.boids.remove(closest)
        self.forward = (closest.pos - self.pos) * 1/closest_distance

    def move(self):
        self.find_closest()
        self.pos += self.forward * Predator.speed
        self.wrap()

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2



