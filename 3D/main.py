from boid import Boid
from world import World
from renderer import Renderer
import pyglet
from config import Config
from environment import Environment
import numpy as np
from utils import Utils
import math
from history import History
import os

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, Concatenate
from tensorflow.keras.optimizers import Adam

from rl.agents.ddpg import DDPGAgent
from rl.memory import SequentialMemory
from rl.random import OrnsteinUhlenbeckProcess

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy


def prepare_run(world, renderer, config):
    environment = Environment(world, renderer, config)
    n_actions = environment.action_space.n
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + environment.observation_space.shape))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(n_actions))
    model.add(Activation('linear'))
    print(model.summary())
    memory = SequentialMemory(limit=50000, window_length=1)
    policy = BoltzmannQPolicy()
    test_policy = BoltzmannQPolicy()
    if config.annealing:
        policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr="eps", value_min=0, value_max=0, value_test=0, nb_steps=0)
        test_policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr="eps", value_min=0, value_max=0, value_test=1, nb_steps=0)

    dqn = DQNAgent(model=model, nb_actions=n_actions, memory=memory, nb_steps_warmup=50, target_model_update=1e-2,
                   policy=policy, test_policy=test_policy)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    environment.set_dqn_agent(dqn)
    return environment, model, dqn

def annealing(dqn, config, i, times, steps):
    eps_range = config.annealing_start - config.annealing_end
    interval = eps_range/times
    start = config.annealing_start - interval * i
    end = config.annealing_start - interval * (i + 1)
    dqn.policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), "eps",
                                      start, end, 0, steps)
    print(start, end)

def run(dqn, environment, steps, times, name, config):
    for i in range(times):
        # Do annealing
        if config.annealing:
            annealing(dqn, config, i, times, steps)
        dqn.fit(environment, nb_steps=steps, visualize=False, verbose=2, nb_max_episode_steps=10000)
        save(dqn, name, name + str(steps * (i + 1)) + ".h5f")
        environment.save_record(name, name + str(i))

def save(dqn, folder, name):
    if not os.path.exists("data/" + folder):
        os.mkdir("data/" + folder)
    dqn.save_weights("data/" + folder + "/" + name, overwrite=True)

def load(dqn, folder, name):
    dqn.load_weights("data/" + str(folder) + "/" + str(name))

def experiment(dqn, environment, episodes, config):
    dqn.policy = EpsGreedyQPolicy(eps=config.annealing_end)
    dqn.test(environment, nb_episodes=episodes, visualize=False, nb_max_episode_steps=10000)
    name = "exp_" + config.run_name
    save(dqn, config.run_name, config.run_name + ".h5f")
    environment.save_record(name, name)

def main():
    config = Config(0)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment = Environment(world, renderer, config)

if __name__ == '__main__':
    main()
    '''config = Config(0)
    world = World(config)
    # world.spawn_boids(config.nr_of_boids)
    # world.add_predator()
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment = Environment(world, renderer)

    n_actions = environment.action_space.n

    model = Sequential()
    model.add(Flatten(input_shape=(1,) + environment.observation_space.shape))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(n_actions))
    model.add(Activation('linear'))
    print(model.summary())

    memory = SequentialMemory(limit=50000, window_length=1)
    policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model, nb_actions=n_actions, memory=memory, nb_steps_warmup=50, target_model_update=1e-2,
                   policy=policy, environment=environment)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    a = [1,2,3,4,5,6,7]
    h = History()
    h.fill(2)
    for thing in a:
        h.add(thing)
        print(h.get())

    dqn.load_weights('Firsttrial6000000.h5f')

    #dqn.test(environment, nb_episodes=5, visualize=True, nb_max_episode_steps=2000, forward_other_agents=True)


    dqn.fit(environment, nb_steps=400000, visualize=True, verbose=2, nb_max_episode_steps=10000, forward_other_agents=True)

    dqn.save_weights('Firsttrial1000000.h5f', overwrite=True)

    dqn.fit(environment, nb_steps=400000, visualize=False, verbose=2, nb_max_episode_steps=10000,
            forward_other_agents=True)

    dqn.save_weights('Firsttrial1400000.h5f', overwrite=True)

    dqn.fit(environment, nb_steps=400000, visualize=False, verbose=2, nb_max_episode_steps=10000,
            forward_other_agents=True)

    dqn.save_weights('Firsttrial1800000.h5f', overwrite=True)

    dqn.fit(environment, nb_steps=400000, visualize=False, verbose=2, nb_max_episode_steps=10000,
            forward_other_agents=True)

    dqn.save_weights('Firsttrial2200000.h5f', overwrite=True)

    input("waiter")
    #environment.print_info = True

    dqn.test(environment, nb_episodes=5, visualize=True, nb_max_episode_steps=2000, forward_other_agents=True)

    
    
    # start of old triple quotes
    nb_actions = environment.action_space.shape[0]

    print(environment.action_space.sample())
    
    actor = Sequential()
    actor.add(Flatten(input_shape=(1,) + environment.observation_space.shape))
    actor.add(Dense(16))
    actor.add(Activation('relu'))
    actor.add(Dense(16))
    actor.add(Activation('relu'))
    actor.add(Dense(16))
    actor.add(Activation('relu'))
    actor.add(Dense(16))
    actor.add(Activation('relu'))
    actor.add(Dense(16))
    actor.add(Activation('relu'))
    actor.add(Dense(nb_actions))
    actor.add(Activation('tanh'))
    print(actor.summary())

    action_input = Input(shape=(nb_actions,), name='action_input')
    observation_input = Input(shape=(1,) + environment.observation_space.shape, name='observation_input')
    flattened_observation = Flatten()(observation_input)
    x = Concatenate()([action_input, flattened_observation])
    x = Dense(32)(x)
    x = Activation('relu')(x)
    x = Dense(32)(x)
    x = Activation('relu')(x)
    x = Dense(32)(x)
    x = Activation('relu')(x)
    x = Dense(32)(x)
    x = Activation('relu')(x)
    x = Dense(32)(x)
    x = Activation('relu')(x)
    x = Dense(1)(x)
    x = Activation('linear')(x)
    critic = Model(inputs=[action_input, observation_input], outputs=x)
    print(critic.summary())

    # Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
    # even the metrics!
    memory = SequentialMemory(limit=100000, window_length=1)
    random_process = OrnsteinUhlenbeckProcess(size=nb_actions, theta=.15, mu=0., sigma=.3)
    #random_process = None
    agent = DDPGAgent(nb_actions=nb_actions, actor=actor, critic=critic, critic_action_input=action_input,
                      memory=memory, nb_steps_warmup_critic=100, nb_steps_warmup_actor=100,
                      random_process=random_process, gamma=.99, target_model_update=1e-3)
    agent.compile(Adam(lr=.001, clipnorm=1.), metrics=['mae'])

    #agent.load_weights('ddpg_weights.h5f')

    agent.fit(environment, nb_steps=30000, visualize=True, verbose=2, nb_max_episode_steps=1000)

    agent.save_weights('ddpg_weights.h5f', overwrite=True)

    input("waiter")

    agent.test(environment, nb_episodes=5, visualize=True, nb_max_episode_steps=1000)'''


# if = input("Kies steen papier of schaar")
# print(random.choice(["Je wint!", "Je verliest 😥", "Gelijkspel!"]))
