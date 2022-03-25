import random
from scipy.spatial.transform import Rotation as R
from utils import Utils as U
import numpy as np
import config
import math


class Predator:
    speed = config.predator_speed
    color = config.predator_color

    def __init__(self, world):

        self.up = np.array([0, 1, 0])
        self.world = world
        self.pos = U.random_np_array(3, -1, 1)
        random_direction = R.from_rotvec((random.uniform(0, 0), 0, random.uniform(0, 0)))
        self.forward = np.array(random_direction.apply(np.array((0, -1, 0))))
        self.rotation = self.up
        self.chase_counter = 0
        self.target = None
        self.ID = 0

    # Find closest boid and change direction to it
    def find_target(self):
        target = None
        if self.chase_counter == 0:
            self.chase_counter = config.predator_chase_time
            # Distance of closest boid
            closest_distance = 1000
            # Boids close enough for confusion
            close_enough = []
            for boid in self.world.boids:

                vec_to_boid = U.wrapping_distance_vector(self.pos, boid.pos)
                dist = U.vec3_magnitude(vec_to_boid)

                # If it is the new closest boid save it
                if dist < closest_distance:
                    closest_distance = dist
                    target = boid
                # If it is close enough for confusion, save it
                if dist < config.predator_confusion_distance:
                    close_enough.append(boid)

            # If boids are close enough for confusion, pick a random one that is close enough
            if config.predator_confusion:
                if len(close_enough) > 0:
                    print("yes")
                    target = random.choice(close_enough)
        else:
            target = self.target[0]
            self.chase_counter -= 1

        vec_to_boid = U.wrapping_distance_vector(self.pos, target.pos)
        dist = U.vec3_magnitude(vec_to_boid)
        self.target = (target, vec_to_boid, dist)

        # Eat boid if close enough
        if self.target[2] < config.predator_eating_distance:
            self.target[0].alive = False
            self.world.boids.remove(self.target[0])
            self.chase_counter = 0

        # Change direction
        self.change_heading_to_boid(self.target[1])

    def change_heading_to_boid(self, boid_vector):
        boid_vector = U.normalize(boid_vector)
        # Find angle, cap at maximal turning speed
        theta = -np.arccos(np.dot(boid_vector, self.forward))
        if abs(theta) > config.predator_turning_speed:
            theta = math.copysign(config.predator_turning_speed, theta)
        # Find axis
        axis = U.normalize_nparray(np.cross(boid_vector, self.forward))
        # Construct quaternion
        quaternion = [np.sin(theta/2) * axis[0], np.sin(theta/2) * axis[1],
                      np.sin(theta/2) * axis[2], np.cos(theta/2)]

        # Apply quaternion
        change = R.from_quat(quaternion)
        self.forward = U.normalize_nparray(change.apply(self.forward))
        self.rotation = change.apply(self.rotation)

    def move(self):
        self.find_target()
        self.pos += self.forward * Predator.speed
        self.wrap()

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2





