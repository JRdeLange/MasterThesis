import numpy as np
import gym
from gym import spaces
import math
import config
from utils import Utils as U
from agentinfo import AgentInfo
from theone import TheOne


class Environment(gym.Env):

    def __init__(self, world):
        self.world = world
        # [axis x, axis y, axis z, angle]
        self.action_space = spaces.Box(np.array([np.float32(-1), np.float32(-1), np.float32(-1)]),
                                       np.array([np.float32(1), np.float32(1), np.float32(1)]))
        # [[self]
        #  [predator],
        #  [boid],
        #  [boid]....
        #
        # speed as well? No, put speed in forward vector
        # [distance,   vector,   forward]
        # [f,          f, f, f,  f, f, f]
        self.observation_space = spaces.Box(low=-1, high=1,
                                            shape=(config.nr_observed_agents+1, 7))

    def step(self, action):
        the_one: TheOne = self.world.the_one
        # for action maybe parameterize the action space
        quaternion = U.capped_quaternion(the_one.forward, action, config.boid_turning_speed)
        the_one.turn_by_quaternion(quaternion)
        state = self.construct_observation(the_one)


    def construct_observation(self, agent):
        # Make observation array
        observation = np.zeros((config.nr_observed_agents+1, 7))
        # Fill in first row about self
        self.fill_in_first_observation_row(observation, agent)
        # Fill in second row about predator
        predator_info: AgentInfo = self.world.distance_matrix[agent.id, self.world.predator.id]
        self.fill_in_observation_row(observation, 1, predator_info)
        # Store AgentInfo about all agents in agents_info
        agents_info = []
        for boid in self.world.boids:
            if not agent.id == boid.id:
                agents_info.append(self.world.distance_matrix[agent.id, boid.id])
        # Sort the info based on distance
        agents_info.sort(key=self.extract_distance)

    def extract_distance(self, agent_info):
        return agent_info.dist

    def fill_in_first_observation_row(self, observation, agent):
        observation[0, 0] = 0
        x, y, z = agent.pos
        observation[0, 1] = x
        observation[0, 2] = y
        observation[0, 3] = z
        x, y, z = agent.forward
        observation[0, 4] = x
        observation[0, 5] = y
        observation[0, 6] = z

    def fill_in_observation_row(self, observation, row, agent_info: AgentInfo):
        observation[row, 0] = agent_info.dist
        x, y, z = agent_info.vector
        observation[row, 1] = x
        observation[row, 2] = y
        observation[row, 3] = z
        x, y, z = agent_info.agent.forward
        observation[row, 4] = x
        observation[row, 5] = y
        observation[row, 6] = z


    def reset(self, **kwargs):
        pass

    def render(self, mode="human"):
        pass

    def close(self):
        pass
