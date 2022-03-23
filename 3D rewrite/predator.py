import random
from scipy.spatial.transform import Rotation as R
from utils import Utils as U
import numpy as np


class Predator:
    speed = 0.01
    color = (0.2, 0.8, 0.2, 1)

    def __init__(self, world):
        up = np.array((1,0,0))
        right = np.array((0,1,0))

        boid_vector = right
        theta = np.arccos(np.dot(boid_vector, up))
        axis = np.cross(boid_vector, up)
        print(theta, axis)
        change = R.from_quat([0,0,-1,1.570796])
        up = U.normalize_nparray(change.apply(up))
        print(up)


        self.world = world
        self.pos = U.random_np_array(3, -1, 1)
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

        self.change_heading_to_boid(closest, closest_distance)

    def change_heading_to_boid(self, boid, distance):
        boid_vector = U.normalize_nparray(boid.pos - self.pos)
        theta = np.arccos(np.dot(boid_vector, self.forward))
        axis = np.cross(boid_vector, self.forward)

        change = R.from_quat(np.append(axis, -theta))
        self.forward = U.normalize_nparray(change.apply(self.forward))

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



