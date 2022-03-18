import pyglet
from pyglet.gl import *
import pyshaders as ps
from shaders import Shaders
from utils import Utils
from models import Models
import math


# Nice rendering example
# https://github.com/pyglet/pyglet/blob/master/examples/3dmodel/model.py


class Renderer:

    def __init__(self, height, width, world):
        self.window = pyglet.window.Window(height, width)
        self.world = world
        self.shader_program = None
        self.init_shaders()
        self.boid_model = Models.boid_model
        self.wireframe_world_model = Models.wireframe_world_cube

        @self.window.event
        def on_draw():
            glClearColor(0.1, 0.1, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            self.render_boids()
            self.render_box()

    def init_shaders(self):
        self.shader_program = None
        self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        self.shader_program.use()

        self.shader_program.uniforms.project = Utils.perspective(1, .6*math.pi, 0.1, 100)
        self.shader_program.uniforms.color = (0.8, 0.8, 0.8, 1)

    def render_boids(self):
        scale = Utils.scale(.02, .02, .02)
        for boid in self.world.boids:
            translate = Utils.translate(boid.pos[0], boid.pos[1], boid.pos[2]-2)
            heading = boid.heading.as_euler("xyz")
            rotate = Utils.rotate(heading[0], heading[1], heading[2])
            total = Utils.combine_matrices(translate, scale, rotate)
            self.shader_program.uniforms.model = total
            self.boid_model.draw(pyglet.gl.GL_TRIANGLES)

    def render_box(self):
        self.shader_program.uniforms.model = Utils.translate(0, 0, -2)
        self.wireframe_world_model.draw(pyglet.gl.GL_LINES)



    def render(self):
        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()
