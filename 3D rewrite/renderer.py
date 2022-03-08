import pyglet.window
from pyglet.gl import *


class Renderer:

    def __init__(self, height, width):
        self.window = pyglet.window.Window(height, width)

        @self.window.event
        def on_draw():
            glClearColor(0.1, 0.5, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

