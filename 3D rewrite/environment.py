import numpy as np
import gym
from gym import spaces
import math
import config
from utils import Utils as U
from agentinfo import AgentInfo


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
        # [distance,   vector,   forward]
        # [f,          f, f, f,  f, f, f]
        self.observation_space = spaces.Box(low=-1, high=1,
                                            shape=(config.nr_observed_agents, 7))

    def step(self, action):
        x, y, z, t = action
        the_one = self.world.the_one
        quaternion = U.construct_quaternion(x, y, z, t)

    def construct_observation(self):
        observation = np.zeros(8, config.nr_observed_agents)
        predator_info: AgentInfo = self.world.distance_matrix[self.world.the_one.id, self.world.predator.id]
        self.fill_in_observation_row(observation, 0, predator_info)
        agents = []
        for x in range(config.nr_observed_agents):
            agents

    def extract_distance(self, agent_info):
        return agent_info.dist

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
