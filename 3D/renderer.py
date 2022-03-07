import math
import pyglet
from pyglet.gl import *
from utils import Utils
from world import World
from boid import Boid
from shaders import Shaders
import pyshaders as ps


class Renderer:
    batch = pyglet.graphics.Batch()

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window()
        self.world = world
        self.boid_model = pyglet.graphics.vertex_list(6, ('v2f', (0, 1, -0.7, -1, 0, -0.7,
                                                                  0, 1, 0, -0.7, 0.7, -1,)))
        self.boid_model_matrices = []

        self.shader_program = None
        self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        self.shader_program.use()

        @self.window.event
        def on_draw():
            glClearColor(0.1, 0.1, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            self.render_boids()

    def render(self):
        self.boid_model.draw(GL_TRIANGLES)

    def load_shaders(self):
        try:
            self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        except ps.ShaderCompilationError as e:
            print(e.logs)
            exit()


    def render_boids(self):
        self.shader_program.uniforms.color = (0.8, 0.8, 0.8, 1)
        for boid in self.world.get_boids():

            trans_x, trans_y, trans_z = Utils.world_to_unit(self.world, boid.x, boid.y, boid.z)
            trans = Utils.translate(trans_x, trans_y, trans_z)
            scale = Utils.scale(0.05, 0.05)
            rot = Utils.identity()
            mat = Utils.combine_matrices(trans, scale, rot)
            self.shader_program.uniforms.model = mat
            self.render()


