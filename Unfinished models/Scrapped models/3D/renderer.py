import math
import pyglet
from pyglet.gl import *
from utils import Utils
from world import World
from boid import Boid
from shaders import Shaders
import pyshaders as ps
from scipy.spatial.transform import Rotation as R

class Renderer:
    batch = pyglet.graphics.Batch()

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window(850, 850)
        self.world = world
        self.box_model = pyglet.graphics.vertex_list(8, ('v3f', (-.5, -.5, -.5,   .5, -.5, -.5,
                                                                 -.5, .5, -.5,   .5, .5, -.5,
                                                                 -.5, -.5, .5,   .5, -.5, .5,
                                                                 -.5, .5, .5,   .5, .5, .5,)))
        self.boid_model = pyglet.graphics.vertex_list(6, ('v3f', (0, 1, 0, -0.7, -1, 0, 0, -0.7, 0,
                                                                  0, 1, 0, 0, -0.7, 0, 0.7, -1, 0,)))
        self.boid_model_matrices = []

        self.project = Utils.perspective(1, math.pi/3, .1, 10)

        self.shader_program = None
        self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        self.shader_program.use()
        self.shader_program.uniforms.project = self.project
        self.shader_program.uniforms.color = (0.8, 0.8, 0.8, 1)

        @self.window.event
        def on_draw():
            glClearColor(0.1, 0.1, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            self.render_box()
            self.render_boids()

    def render_boid(self):
        self.boid_model.draw(GL_TRIANGLES)

    def render_box(self):
        verts = [[-.5, -.5, -.5],[.5, -.5, -.5],[-.5, .5, -.5],[.5, .5, -.5],
                 [-.5, -.5, .5],[.5, -.5, .5],[-.5, .5, .5],[.5, .5, .5,]]
        for pos in verts:
            x, y, z = pos
            trans = Utils.translate(x, y, z-1.7)
            scale = Utils.scale(0.05, 0.05)
            rot = Utils.identity()
            mat = Utils.combine_matrices(trans, scale, rot)
            self.shader_program.uniforms.model = mat
            self.render_boid()

    def load_shaders(self):
        try:
            self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        except ps.ShaderCompilationError as e:
            print(e.logs)
            exit()

    def render_boids(self):
        for boid in self.world.get_boids():

            trans_x, trans_y, trans_z = Utils.world_to_render_spot(self.world, boid.x, boid.y, boid.z)
            trans = Utils.translate(trans_x, trans_y, trans_z)
            scale = Utils.scale(0.05, 0.05)
            x, y, z = boid.get_rot()
            rot = Utils.rotate(x, y, z)
            mat = Utils.combine_matrices(trans, scale, rot)
            self.shader_program.uniforms.model = mat
            self.render_boid()



