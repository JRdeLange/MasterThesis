from boid import Boid
from world import World
from renderer import Renderer
import pyglet
from config import Config
from environment import Environment
import numpy as np
from utils import Utils
import math

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, Concatenate
from tensorflow.keras.optimizers import Adam

from rlcustom.agents.ddpg import DDPGAgent
from rlcustom.memory import SequentialMemory
from rlcustom.random import OrnsteinUhlenbeckProcess

from rlcustom.agents.dqn import DQNAgent
from rlcustom.policy import BoltzmannQPolicy
import sys


def prepare_run(world, renderer, config):
    environment = Environment(world, renderer, config)
    n_actions = environment.action_space.n
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + environment.observation_space.shape))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(n_actions))
    model.add(Activation('linear'))
    print(model.summary())
    memory = SequentialMemory(limit=50000, window_length=1)
    policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model, nb_actions=n_actions, memory=memory, nb_steps_warmup=50, target_model_update=1e-2,
                   policy=policy, environment=environment)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    return environment, model, dqn


def run(dqn, environment, steps, times, name):
    for i in range(times):
        dqn.fit(environment, nb_steps=steps, visualize=True, verbose=2, nb_max_episode_steps=10000,
                forward_other_agents=True)
        #dqn.save_weights(name + str(steps * (i + 1)) + '.h5f', overwrite=True)


def main():
    config = Config(0)
    print(vars(config))
    world = World(config)

    world.spawn_things()
    renderer = Renderer(800, 800, world)

    environment, model, dqn = prepare_run(world, renderer, config)

    run(dqn, environment, 500, 4, config.run_name)
    environment.save_record(config.run_name)


    input("waiter")
    # environment.print_info = True
    # dqn.load_weights('reworked1500000.h5f')

    dqn.test(environment, nb_episodes=5, visualize=True, nb_max_episode_steps=2000, forward_other_agents=True)


if __name__ == '__main__':
    main()
