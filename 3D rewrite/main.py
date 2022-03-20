from boid import Boid
from world import World
from renderer import Renderer
import pyglet



if __name__ == '__main__':
    world = World()
    world.spawn_boids(50)
    renderer = Renderer(800, 800, world)
    graphics = True

def main_loop():
    while True:
        world.tick()

        if graphics:
            renderer.render()


main_loop()
