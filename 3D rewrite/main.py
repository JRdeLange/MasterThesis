from boid import Boid
from world import World
from renderer import Renderer
import pyglet
import config
from environment import Environment
import numpy as np


if __name__ == '__main__':
    world = World()
    world.spawn_boids(config.nr_of_boids)
    world.add_predator()
    renderer = Renderer(800, 800, world)
    environment = Environment(world)


def main_loop():
    graphics = config.graphics
    while True:
        world.tick()
        environment.construct_observation(world.boids[2])

        if graphics:
            renderer.render()


main_loop()

# if = input("Kies steen papier of schaar")
# print(random.choice(["Je wint!", "Je verliest 😥", "Gelijkspel!"]))
