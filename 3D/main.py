from world import World
from renderer import Renderer
from controller import Controller
from utils import Utils
from environment import Environment
import pyglet
import time
from scipy.spatial.transform import Rotation as Rot

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    world = World(100)
    print(Utils.world_to_render_spot(world, -.5, -.5, -.5))
    world.gen_boids(10)
    graphics = True
    renderer = Renderer(world, 500, 500)
    environment = Environment(world, True, renderer)


def main_loop():
    prev_time = time.time() - 1

    '''n_actions = environment.action_space.n

    model = Sequential()
    model.add(Flatten(input_shape=(1,) + environment.observation_space.shape))
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
    dqn = DQNAgent(model=model, nb_actions=n_actions, memory=memory, nb_steps_warmup=25, target_model_update=1e-2, policy=policy)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])

    dqn.fit(environment, nb_steps=20000, visualize=False, verbose=2)

    dqn.save_weights('dqn_weights.h5f', overwrite=True)

    environment.set_graphics(True)

    dqn.test(environment, nb_episodes=5, visualize=True)'''

    while True:

        #print(1.0/(time.time()-prev_time))
        prev_time = time.time()

        keys = pyglet.window.key.KeyStateHandler()
        #state, reward, done, info = environment.step(4)
        #print(reward)

        world.tick()
        environment.render()

        #pyglet.clock.tick()
        '''
        if graphics:
            for window in pyglet.app.windows:
                window.switch_to()
                window.dispatch_events()
                window.dispatch_event('on_draw')
                window.flip()
        '''

print(pyglet.gl.gluPerspective(65, 1, .1, 1000))

heading = [1, 0, 0]
r = Rot.from_euler("xyz", [0, 3.14, 0])
print(r.apply(heading))



main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

