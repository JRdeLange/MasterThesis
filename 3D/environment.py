import numpy as np
import gym
from gym import spaces
import math
from config import Config
from utils import Utils as U
from agentinfo import AgentInfo
from theone import TheOne
import pyglet
from renderer import Renderer
from record import Record
from copy import deepcopy


class Environment(gym.Env):

    def __init__(self, world, renderer, config):
        self.config = config
        self.renderer = renderer
        self.current_boid_index = None
        self.world = world
        self.dqn_agent = None

        self.stop_exp_at_tick = 100000

        if self.config.record_keeping:
            self.record = Record()
            self.world.record = self.record

        # [axis x, axis y, axis z, angle]
        # new forward direction [x, y, z]
        #self.action_space = spaces.Box(np.array([np.float32(-1), np.float32(-1), np.float32(-1)]),
        #                               np.array([np.float32(1), np.float32(1), np.float32(1)]))
        self.action_space = spaces.Discrete(14)
        '''self.action_dict = {
            0: np.array([1, 0, 0]),
            1: np.array([0, 1, 0]),
            2: np.array([0, 0, 1]),
            3: np.array([-1, 0, 0]),
            4: np.array([0, -1, 0]),
            5: np.array([0, 0, -1])
        }
        self.action_dict = {
            0: np.array([1, -1, -1]),
            1: np.array([1, -1, 1]),
            2: np.array([-1, -1, 1]),
            3: np.array([-1, -1, -1]),
            4: np.array([1, 1, -1]),
            5: np.array([1, 1, 1]),
            6: np.array([-1, 1, 1]),
            7: np.array([-1, 1, -1])
        }'''
        self.action_dict = {
            0: np.array([1, 0, 0]),
            1: np.array([0, 1, 0]),
            2: np.array([0, 0, 1]),
            3: np.array([-1, 0, 0]),
            4: np.array([0, -1, 0]),
            5: np.array([0, 0, -1]),
            6: np.array([1, -1, -1]),
            7: np.array([1, -1, 1]),
            8: np.array([-1, -1, 1]),
            9: np.array([-1, -1, -1]),
            10: np.array([1, 1, -1]),
            11: np.array([1, 1, 1]),
            12: np.array([-1, 1, 1]),
            13: np.array([-1, 1, -1])
        }

        # [[self]
        #  [predator],
        #  [boid],
        #  [boid]....
        #
        # speed as well? No, put speed in forward vector
        # [distance,   vector,   forward]
        # [f,          f, f, f,  f, f, f]
        # [pos t-2, pos t-1, pos now]
        # [f,f,f,   f,f,f,   f,f,f]
        self.nr_of_obs_rows = self.config.nr_observed_agents + 1
        if self.config.predator_present:
            self.nr_of_obs_rows += 1
        self.observation_space = spaces.Box(low=-1, high=1,
                                            shape=(self.nr_of_obs_rows, 9))

    def set_dqn_agent(self, dqn_agent):
        self.dqn_agent = dqn_agent

    def perform_passives_actions(self):
        for agent in self.world.passives:
            state = self.construct_observation(agent)
            state = deepcopy(state)
            action = self.dqn_agent.forward(state)
            self.perform_agent_action(agent, action)

    def perform_agent_action(self, agent, action):
        goal = U.normalize_nparray(self.action_dict[action])
        quaternion = U.capped_quaternion(agent.forward, goal, self.config.boid_turning_speed)
        agent.turn_by_quaternion(quaternion)

    def step(self, action):
        the_one: TheOne = self.world.the_one
        self.perform_agent_action(the_one, action)
        self.perform_passives_actions()
        self.world.tick()
        state = self.construct_observation(the_one)
        reward = self.get_reward()
        done = not self.world.the_one.alive
        info = {}

        if (self.world.overarching_tick % self.config.record_frequency == 0) and self.config.record_keeping:
            if self.dqn_agent.training or (not self.dqn_agent.training and self.world.overarching_tick < self.stop_exp_at_tick):
                self.keep_record()

        if not self.dqn_agent.training:
            if self.world.overarching_tick == self.stop_exp_at_tick:
                self.save_record(self.config.run_name, self.config.run_name + "100000_ticks")

            if self.world.overarching_tick > self.stop_exp_at_tick:
                done = True

        return state, reward, done, info

    def keep_record(self):
        self.record.add_slice(self.world)

    def save_record(self, folder, name):
        self.record.save_to_file(folder, name, self.config)

    def get_reward(self):
        if self.world.the_one.alive:
            return 1
        return -1000

    def construct_observation(self, agent):
        # Make observation array
        observation = np.zeros((self.nr_of_obs_rows, 9))
        # Fill in first row about self
        self.fill_in_first_observation_row(observation, agent)
        if self.nr_of_obs_rows == 1:
            return observation
        # Fill in second row about predator
        if self.config.predator_present:
            predator_info: AgentInfo = self.world.distance_matrix[agent.id, self.world.predator.id]
            self.fill_in_observation_row(observation, 1, predator_info)
        # Store AgentInfo about all agents in agents_info
        agents_info = []
        for boid in self.world.boids:
            if not agent.id == boid.id:
                agents_info.append(self.world.distance_matrix[agent.id, boid.id])
        # Sort the info based on distance
        agents_info.sort(key=self.extract_distance)
        # Fill out the observation
        for row in range(2, self.config.nr_observed_agents+2):
            idx = row - 2
            if idx < len(agents_info):
                self.fill_in_observation_row(observation, row, agents_info[idx])
        return observation

    def extract_distance(self, agent_info):
        return agent_info.dist

    def fill_in_first_observation_row(self, observation, agent):
        idx = 0
        for pos in agent.history.get():
            for coord in pos:
                observation[0, idx] = coord
                idx += 1

    def fill_in_observation_row(self, observation, row, agent_info: AgentInfo):
        if row >= self.nr_of_obs_rows:
            return
        idx = 0
        for pos in agent_info.agent.history.get():
            for coord in pos:
                observation[row, idx] = coord
                idx += 1

    def reset(self, **kwargs):
        self.world.reset()
        return self.construct_observation(self.world.the_one)

    def render(self, mode="human"):
        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()

    def close(self):
        pass
