import numpy as np
import gym
from gym import spaces
import math
import config
from utils import Utils as U
from agentinfo import AgentInfo
from theone import TheOne
import pyglet
from renderer import Renderer


class Environment(gym.Env):

    def __init__(self, world, renderer):
        self.renderer = renderer
        self.current_boid_index = None
        self.world = world
        self.print_info = False
        # [axis x, axis y, axis z, angle]
        # new forward direction [x, y, z]
        # self.action_space = spaces.Box(np.array([np.float32(-1), np.float32(-1), np.float32(-1)]),
        #                               np.array([np.float32(1), np.float32(1), np.float32(1)]))
        self.action_space = spaces.Discrete(8)
        self.action_dict = {
            0: -1,
            1: -.75,
            2: -.5,
            3: -.25,
            4: 0,
            5: .25,
            6: .5,
            7: .75,
            8: 1
        }

        # [[self]
        #  [predator],
        #  [boid],
        #  [boid]....
        #
        # speed as well? No, put speed in forward vector
        # [distance,   vector,   forward]
        # [f,          f, f, f,  f, f, f]
        self.nr_of_obs_rows = config.nr_observed_agents + 1
        if config.predator_present:
            self.nr_of_obs_rows += 1
        self.observation_space = spaces.Box(low=-1, high=1,
                                            shape=(self.nr_of_obs_rows, 5))

        self.observation_space = spaces.Dict(
            ""
        )

    def perform_agent_action(self, agent, action):
        change = self.action_dict[action] * config.boid_turning_speed
        agent.turn_by_rad(change)

    def step(self, action):
        the_one: TheOne = self.world.the_one
        # for action maybe parameterize the action space
        # How to deal with action: https://stackoverflow.com/questions/22099490/calculate-vector-after-rotating-it-towards-another-by-angle-%CE%B8-in-3d-space
        #goal = U.normalize_nparray(action)
        self.perform_agent_action(the_one, action)
        self.world.tick()
        state = self.construct_observation(the_one)
        reward = self.get_reward()
        done = not self.world.the_one.alive
        info = {}
        if self.print_info:
            print(action, the_one.forward, reward)
        return state, reward, done, info

    def get_reward_test(self):
        return self.world.the_one.forward[1]
        pos = self.world.the_one.pos
        #print(pos)
        if pos[1] < 0:
            return 1
        return -1

    def get_reward(self):
        if self.world.the_one.alive:
            return 1
        return -1000

    def construct_observation(self, agent):
        # Make observation array
        observation = np.zeros((self.nr_of_obs_rows, 5))
        # Fill in first row about self
        self.fill_in_first_observation_row(observation, agent)
        if self.nr_of_obs_rows == 1:
            return observation
        # Fill in second row about predator
        if config.predator_present:
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
        for row in range(2, config.nr_observed_agents+1):
            idx = row - 2
            if idx < len(agents_info):
                self.fill_in_observation_row(observation, row, agents_info[idx])

        return observation

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
        if row >= self.nr_of_obs_rows:
            return
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
