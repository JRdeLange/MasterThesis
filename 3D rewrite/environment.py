import numpy as np
import gym
from gym import spaces
import math
import config
from utils import Utils as U


class Environment(gym.Env):

    def __init__(self, world):
        self.world = world
        # [axis x, axis y, axis z, angle]
        self.action_space = spaces.Box(np.array([-1, -1, -1, -1]),
                                       np.array([1, 1, 1, 1]))
        # [[predator],
        #  [boid],
        #  [boid]....
        #
        # [distance,   vector,   orientation]
        # [f,          f, f, f,  f, f, f, f]
        self.observation_space = spaces.Box(low=-1, high=1,
                                            shape=(8, config.nr_observed_boids))

    def step(self, action):
        x, y, z, t = action
        the_one = self.world.the_one
        quaternion = U.construct_quaternion(x, y, z, t)

    def reset(self, **kwargs):
        pass

    def render(self, mode="human"):
        pass

    def close(self):
        pass
