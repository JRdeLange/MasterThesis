import pyglet
from pyglet.gl import *
from utils import Utils

class Renderer:
    batch = pyglet.graphics.Batch()

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window()
        self.world = world

        @self.window.event
        def on_draw():
            self.window.clear()
            self.render_boids()

    def render_boids(self):
        coords = []
        for boid in self.world.get_boids():
            x, y = Utils.world_to_screen(self, self.world, boid.x, boid.y)
            coords.append(x)
            coords.append(y)
            coords.append(int(x - 5))
            coords.append(int(y - 12))
            coords.append(int(x))
            coords.append(int(y - 9))

            coords.append(x)
            coords.append(y)
            coords.append(int(x + 5))
            coords.append(int(y - 12))
            coords.append(int(x))
            coords.append(int(y - 9))

        pyglet.graphics.draw(int(len(coords)/2), pyglet.gl.GL_TRIANGLES, ("v2f", tuple(coords)))

