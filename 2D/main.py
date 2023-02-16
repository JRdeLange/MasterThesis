import os
from world import World
from renderer import Renderer
from config import Config
from environment import Environment

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, Concatenate
from tensorflow.keras.optimizers import Adam


from rl.memory import SequentialMemory
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.policy import EpsGreedyQPolicy
from rl.policy import LinearAnnealedPolicy


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

    config.change_to_configuration(2)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)

    config.change_to_configuration(3)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)

    config.change_to_configuration(4)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)

    config.change_to_configuration(5)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)

    config.change_to_configuration(6)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)

    config.change_to_configuration(7)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)


    '''


    config.change_to_configuration(2)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    experiment(dqn, environment, 10, config)

    config.change_to_configuration(3)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    dqn.test_policy = EpsGreedyQPolicy(0)
    dqn.load_weights("data/only_the_one/only_the_one1500000.h5f")
    experiment(dqn, environment, 10000, config)

    config.change_to_configuration(4)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    dqn.test_policy = EpsGreedyQPolicy(0)
    dqn.load_weights("data/only_the_one/only_the_one1500000.h5f")
    experiment(dqn, environment, 10000, config)

    config.change_to_configuration(5)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    dqn.test_policy = EpsGreedyQPolicy(0)
    dqn.load_weights("data/only_the_one/only_the_one1500000.h5f")
    experiment(dqn, environment, 10000, config)

    
    config.change_to_configuration(3)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    run(dqn, environment, 100000, 5, config.run_name, config)
    
    
    
    config.change_to_configuration(2)
    world = World(config)
    world.spawn_things()
    renderer = Renderer(800, 800, world)
    environment, model, dqn = prepare_run(world, renderer, config)
    dqn.load_weights("data/2D_rec_10_total_boids_short_chase/2D_rec_10_total_boids_short_chase100000.h5f")
    #load(dqn, "2D_rec_10_total_boids", "2D_rec_10_total_boids500000.h5f")
    #run(dqn, environment, 100000, 5, config.run_name, config)

    #input("waiter")

    dqn.test(environment, nb_episodes=10, visualize=True, nb_max_episode_steps=2000)
    '''



if __name__ == '__main__':
    main()

