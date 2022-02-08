from world import World
from renderer import Renderer
from controller import Controller
import pyglet

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    world = World()
    print(world.secret)
    renderer = Renderer(world, 500, 500)
    world.tester()
    world.gen_boids(40)


def main_loop():
    while True:
        #renderer.move()

        world.tick()


        pyglet.clock.tick()

        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()


main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

