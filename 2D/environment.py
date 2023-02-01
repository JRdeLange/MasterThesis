from copy import deepcopy

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
from record import Slice, Record
import os


class Environment(gym.Env):

    def __init__(self, world, renderer, config):
        self.config = config
        self.renderer = renderer
        self.current_boid_index = None
        self.world = world
        self.dqn_agent = None
        if self.config.record_keeping:
            self.record = Record()
            self.world.record = self.record

        self.action_space = spaces.Discrete(5)
        self.action_dict = {
            0: -1,
            1: -.5,
            2: 0,
            3: .5,
            4: 1
        }

        # Each row in the observations:
        # [distance, direction, orientation]
        # [f,        f,         f]
        self.nr_of_obs_rows = self.config.nr_observed_agents + 1
        if self.config.predator_present:
            self.nr_of_obs_rows += 1
        self.observation_space = spaces.Box(low=-1, high=1, shape=(self.nr_of_obs_rows, 3))

    def set_dqn_agent(self, dqn_agent):
        self.dqn_agent = dqn_agent

    def perform_passives_actions(self):
        for agent in self.world.passives:
            state = self.construct_observation(agent)
            state = deepcopy(state)
            action = self.dqn_agent.forward(state)
            self.perform_agent_action(agent, action)

    def perform_agent_action(self, agent, action):
        change = self.action_dict[action] * self.config.boid_turning_speed
        agent.turn_by_rad(change)

    def step(self, action):
        # Perform boid actions
        the_one: TheOne = self.world.the_one
        self.perform_agent_action(the_one, action)
        self.perform_passives_actions()

        # Advance world
        self.world.tick()

        # Gather info for next iteration
        state = self.construct_observation(the_one)
        reward = self.get_reward()
        done = not self.world.the_one.alive
        info = {}

        # Keep records for statistical analysis
        if (self.world.overarching_tick % self.config.record_frequency == 0) and self.config.record_keeping:
            self.keep_record()

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
        observation = np.zeros((self.nr_of_obs_rows, 3))
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
        observation[0, 2] = agent.rotation

    def fill_in_observation_row(self, observation, row, agent_info: AgentInfo):
        if row >= self.nr_of_obs_rows:
            return
        observation[row, 0] = agent_info.dist
        observation[row, 1] = agent_info.direction
        observation[row, 2] = agent_info.agent.rotation

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
