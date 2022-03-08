from boid import Boid
from world import World
from renderer import Renderer


if __name__ == '__main__':
    world = World()
    world.spawn_boids(10)
    renderer = Renderer(800, 800)


def main_loop():
    while True:
        world.tick()


main_loop()
