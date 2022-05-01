from boid import Boid
from world import World
from renderer import Renderer
import pyglet
import config
from environment import Environment
import numpy as np
from utils import Utils

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, Concatenate
from tensorflow.keras.optimizers import Adam

from rlcustom.agents.ddpg import DDPGAgent
from rlcustom.memory import SequentialMemory
from rlcustom.random import OrnsteinUhlenbeckProcess


if __name__ == '__main__':
    world = World()
    # world.spawn_boids(config.nr_of_boids)
    # world.add_predator()
    world.spawn_things()
    renderer = Renderer(600, 600, world)
    environment = Environment(world, renderer)


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
    actor.add(Activation('linear'))
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
    #random_process = OrnsteinUhlenbeckProcess(size=nb_actions, theta=.15, mu=0., sigma=.3)
    random_process = None
    agent = DDPGAgent(nb_actions=nb_actions, actor=actor, critic=critic, critic_action_input=action_input,
                      memory=memory, nb_steps_warmup_critic=100, nb_steps_warmup_actor=100,
                      random_process=random_process, gamma=.99, target_model_update=1e-3)
    agent.compile(Adam(lr=.001, clipnorm=1.), metrics=['mae'])

    agent.fit(environment, nb_steps=10000, visualize=False, verbose=2, nb_max_episode_steps=150)

    agent.save_weights('ddpg_weights.h5f', overwrite=True)

    input("waiter")

    agent.test(environment, nb_episodes=5, visualize=True, nb_max_episode_steps=500)


def main_loop():
    graphics = config.graphics
    while True:
        # world.tick()

        if graphics:
            renderer.render()


#main_loop()



# if = input("Kies steen papier of schaar")
# print(random.choice(["Je wint!", "Je verliest 😥", "Gelijkspel!"]))
