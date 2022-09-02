import random
from scipy.spatial.transform import Rotation as R
from utils import Utils as U
import numpy as np
import config
import math
from agentinfo import AgentInfo
from history import History


class Predator:

    def __init__(self, world):
        self.counter = 0
        self.speed = config.predator_speed_slow
        self.up = np.array([0, 1, 0])
        self.world = world
        self.pos = U.random_np_array(2, -1, 1)
        if config.grouped_spawn:
            self.pos = U.random_np_array(2, -1, 0)
        random_direction = R.from_rotvec((random.uniform(0, 0), 0, random.uniform(0, 0)))
        self.forward = np.array(random_direction.apply(np.array((0, -1, 0))))
        self.rotation = (random.random() * 2 - 1) * math.pi
        self.forward = U.rot_to_vec(self.rotation)
        self.chase_counter = 0
        self.target = None
        self.id = 0
        self.halt_counter = 0
        self.history = History()
        self.history.fill(self.pos)

    # Find closest boid and change direction to it
    def find_target(self):
        target = None
        if self.counter % 20 == 0 or self.target:
            self.chase_counter = config.predator_chase_time
            # Distance of closest boid
            closest_distance = 1000
            # Boids close enough for confusion
            close_enough = []
            for boid in self.world.boids:
                current = self.world.distance_matrix[(self.id, boid.id)]
                # If it is the new closest boid save it
                if current.dist < closest_distance:
                    closest_distance = current.dist
                    target = current
                # If it is close enough for confusion, save it
                if current.dist < config.predator_confusion_distance:
                    close_enough.append(current)

            # If boids are close enough for confusion, pick a random one that is close enough
            if config.predator_confusion:
                if len(close_enough) > 0:
                    target = random.choice(close_enough)
        else:
            target = self.world.distance_matrix[(self.id, self.target.agent.id)]
            self.chase_counter -= 1

        self.target = target

        # Change direction
        self.change_heading_to_boid(self.target.vector)

    def change_heading_to_boid(self, boid_vector):
        goal_rot = U.vec_to_rot(boid_vector)
        change = U.wrapping_distance_radians(self.rotation, goal_rot)
        change = U.capped_rotation(change, config.predator_turning_speed)

        self.rotation = U.wrap_radians(self.rotation + change)
        self.forward = U.rot_to_vec(self.rotation)

    def move(self):
        self.counter += 1
        if self.counter == 80:
            self.speed = config.predator_speed_fast
        if self.counter == 100:
            self.speed = config.predator_speed_slow
            self.counter = 0
        if self.halt_counter:
            self.halt_counter -= 1
            return
        self.find_target()
        self.pos += self.forward * self.speed
        self.wrap()
        self.eat()
        #self.history.add(self.pos)

    def eat(self):
        if self.target.dist < config.predator_eating_distance:
            self.world.eat_boid(self.target.agent)
            self.chase_counter = 0
            self.halt_counter = config.predator_halt_time

    def wrap(self):
        for i, val in enumerate(self.pos):
            if val > 1:
                self.pos[i] = val - 2
            elif val < - 1:
                self.pos[i] = val + 2





