from world import World
from renderer import Renderer
from controller import Controller
from utils import Utils
import pyglet

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    world = World(100)
    world.gen_boids(500)
    renderer = Renderer(world, 500, 500)


def main_loop():
    while True:

        keys = pyglet.window.key.KeyStateHandler()

        world.tick()

        pyglet.clock.tick()

        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()


main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

