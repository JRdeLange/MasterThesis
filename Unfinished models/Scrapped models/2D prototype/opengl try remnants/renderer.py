import pyglet
from pyglet.gl import *
from utils import Utils
from ctypes import *
from shaders import Shaders
import pyshaders as ps


class Renderer:
    batch = pyglet.graphics.Batch()

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window()
        self.world = world
        self.triangle = [0, 0.5,
                         -0.5, -0.5,
                         0.5, -0.5]
        self.vbo = GLuint()
        self.vao = GLuint()

        self.shader_program = None
        self.pos_attrib_loc = None

        self.gen_buffers()
        self.bind_buffers()
        self.buffer_data(self.triangle)
        self.tris = pyglet.graphics.vertex_list(3,
                                                ('v2f', (0, 0.5, -0.5, -0.5, 0.5, -0.5)))
        self.load_shaders()
        #self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        self.shader_program.use()

        #self.set_basic_shaders()
        #self.manage_attrib_locations()

        @self.window.event
        def on_draw():
            #glClearColor(0.1, 0.1, 0.1, 1.0)
            #glClear(GL_COLOR_BUFFER_BIT)
            #self.opengl_render()
            self.render()

    def render(self):
        self.tris.draw(GL_TRIANGLES)

    def opengl_render(self):
        glDrawArrays(GL_TRIANGLES, 0, 3)


    def gen_buffers(self):
        glGenBuffers(1, pointer(self.vbo))
        glGenVertexArrays(1, pointer(self.vao))

    def bind_buffers(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBindVertexArray(self.vao)

    def load_shaders(self):
        try:
            self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        except ps.ShaderCompilationError as e:
            print(e.logs)
            exit()


    def set_basic_shaders(self):
        vert_shader_raw = Shaders.basic_vert_shader
        vert_len = len(vert_shader_raw)
        vert_shader_src = (c_char_p * vert_len)(*vert_shader_raw)
        vert_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vert_shader, vert_len, cast(pointer(vert_shader_src), POINTER(POINTER(c_char))), None)
        glCompileShader(vert_shader)

        frag_shader_raw = Shaders.basic_frag_shader
        frag_len = len(frag_shader_raw)
        frag_shader_src = (c_char_p * frag_len)(*frag_shader_raw)
        frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(frag_shader, frag_len, cast(pointer(frag_shader_src), POINTER(POINTER(c_char))), None)
        glCompileShader(frag_shader)

        glAttachShader(self.shader_program, frag_shader)
        glAttachShader(self.shader_program, vert_shader)
        glLinkProgram(self.shader_program)

        glUseProgram(self.shader_program)

    def manage_attrib_locations(self):
        self.pos_attrib_loc = glGetAttribLocation(self.shader_program, "pos")
        glVertexAttribPointer(self.pos_attrib_loc, 2, GL_FLOAT, GL_FALSE, 0, 0)
        glEnableVertexAttribArray(self.pos_attrib_loc)




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
