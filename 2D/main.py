import os
from world import World
from renderer import Renderer
from config import Config
from environment import Environment

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, Concatenate
from tensorflow.keras.optimizers import Adam

from rlcustom.memory import SequentialMemory
from rlcustom.agents.dqn import DQNAgent
from rlcustom.policy import BoltzmannQPolicy
from rlcustom.policy import EpsGreedyQPolicy
from rlcustom.policy import LinearAnnealedPolicy


def make_policy(config):
    if config.linear_annealing:
        policy = None

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
    if config.linear_annealing:
        set_annealing_params()
    dqn = DQNAgent(model=model, nb_actions=n_actions, memory=memory, nb_steps_warmup=50, target_model_update=1e-2,
                   policy=policy, environment=environment)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    environment.set_dqn_agent(dqn)
    return environment, model, dqn

def set_annealing_params(idx, times, config):


def run(dqn, environment, steps, times, name, config):
    for i in range(times):
        if
        dqn.fit(environment, nb_steps=steps, visualize=False, verbose=2, nb_max_episode_steps=10000)
        save(dqn, name, name + str(steps * (i + 1)) + ".h5f")
        environment.save_record(name, name + str(i))

def save(dqn, folder, name):
    if not os.path.exists("data/" + folder):
        os.mkdir("data/" + folder)
    dqn.save_weights("data/" + folder + "/" + name, overwrite=True)

def load(dqn, folder, name):
    dqn.load_weights("data/" + str(folder) + "/" + str(name))

def main():
    config = Config(0)
    world = World(config)

    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    dqn.policy.eps = 0.2
    print(dqn.policy.get_config())

    #run(dqn, environment, 100000, 10, config.run_name)



    input("waiter")

    dqn.test(environment, nb_episodes=10, visualize=True, nb_max_episode_steps=2000)


if __name__ == '__main__':
    main()


