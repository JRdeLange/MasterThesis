import pyglet
from pyglet.gl import *
from utils import Utils
from ctypes import *
from shaders import Shaders


class Renderer:
    batch = pyglet.graphics.Batch()
    shaders = Shaders()

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window()
        self.world = world
        self.triangle = [0, 0.5,
                         -0.5, -0.5,
                         0.5, -0.5]
        self.vbo = GLuint()
        #self.vao = GLuint()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.render_boids()
            self.opengl_render()

    def opengl_render(self):
        pass

    def gen_buffers(self):
        glGenBuffers(1, pointer(self.vbo))
        #glGenVertexArrays(1, pointer(self.vao))

    def bind_buffers(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

    def set_basic_shaders(self):
        vert_shader = self.shaders.basic_vert_shader
        frag_shader = self.shaders.basic_frag_shader

    def buffer_data(self, data):
        data_gl = (GLfloat * len(data))(*data)
        glBufferData(GL_ARRAY_BUFFER, sizeof(data_gl), data_gl, GL_STATIC_DRAW)


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

        pyglet.graphics.draw(int(len(coords) / 2), pyglet.gl.GL_TRIANGLES, ("v2f", tuple(coords)))
