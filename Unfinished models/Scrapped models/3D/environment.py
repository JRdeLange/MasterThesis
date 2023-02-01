import gym
import math
from world import World
from agent import Agent
from boid import Boid
import pyglet
import numpy as np
from utils import Utils


class Environment(gym.Env):

    def __init__(self, world, graphics, renderer):
        self.world = world
        self.graphics = graphics
        self.renderer = renderer
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Box(np.array([-1, -1, -1, -1]), np.array([1, 1, 1, 1]))
        self.counter = 0

    def reset(self):
        self.world.reset()
        rot_x, rot_y = Utils.radians_to_vec(self.world.the_one.rotation)
        state = np.array([self.world.the_one.x, self.world.the_one.y, rot_x, rot_y])
        self.counter = 0
        return state

    def set_graphics(self, graphics):
        self.graphics = graphics

    def step(self, action):
        theta = ((action - 2) * 7) / 360 * math.pi
        self.world.the_one.turn(theta)
        self.world.tick()

        if self.graphics:
            for window in pyglet.app.windows:
                window.switch_to()
                window.dispatch_events()
                window.dispatch_event('on_draw')
                window.flip()

        reward = self.calc_reward()
        x, y = self.world.the_one.get_pos()
        x, y = Utils.world_to_screen(self.world, x, y)
        rot_x, rot_y = Utils.radians_to_vec(self.world.the_one.rotation)
        state = np.array([x, y, rot_x, rot_y])
        done = False
        info = {}

        self.counter += 1
        if self.counter == 1000:
            done = True

        return state, reward, done, info

    def calc_reward(self):
        x, y = self.world.the_one.get_pos()
        if abs(x - 50) < 25 and abs(y - 50) < 25:
            return 1
        return -1

    def render(self, mode="human"):
        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()

    def close(self):
        pass
