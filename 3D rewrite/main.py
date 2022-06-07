from boid import Boid
from world import World
from renderer import Renderer
import pyglet
import config
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

def main_loop():
    graphics = config.graphics
    while True:
        # world.tick()

        if graphics:
            renderer.render()


if __name__ == '__main__':
    world = World()
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

    dqn.load_weights('groupedquadroturn14act9pass120000020000.h5f')

    '''dqn.fit(environment, nb_steps=400000, visualize=False, verbose=2, nb_max_episode_steps=10000, forward_other_agents=True)

    dqn.save_weights('groupedquadroturn14act9pass160000020000.h5f', overwrite=True)

    dqn.fit(environment, nb_steps=400000, visualize=False, verbose=2, nb_max_episode_steps=10000,
            forward_other_agents=True)

    dqn.save_weights('groupedquadroturn14act9pass200000020000.h5f', overwrite=True)

    dqn.fit(environment, nb_steps=400000, visualize=False, verbose=2, nb_max_episode_steps=10000,
            forward_other_agents=True)

    dqn.save_weights('groupedquadroturn14act9pass240000020000.h5f', overwrite=True)'''

    #input("waiter")
    #environment.print_info = True

    dqn.test(environment, nb_episodes=5, visualize=True, nb_max_episode_steps=2000, forward_other_agents=True)


    '''nb_actions = environment.action_space.shape[0]

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





# main_loop()




# if = input("Kies steen papier of schaar")
# print(random.choice(["Je wint!", "Je verliest 😥", "Gelijkspel!"]))
