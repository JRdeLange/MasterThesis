from boid import Boid
from world import World
from renderer import Renderer
import pyglet
import config


if __name__ == '__main__':
    world = World()
    world.spawn_boids(3)
    world.add_predator()
    renderer = Renderer(800, 800, world)


def main_loop():
    graphics = config.graphics
    while True:
        world.tick()

        if graphics:
            renderer.render()


main_loop()

# if = input("Kies steen papier of schaar")
# print(random.choice(["Je wint!", "Je verliest 😥", "Gelijkspel!"]))
