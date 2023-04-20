import pyglet
from pyglet.gl import *
import pyshaders as ps

import config
from shaders import Shaders
from utils import Utils
from models import Models
from boid import Boid
import math
from scipy.spatial.transform import Rotation as R



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
            if self.world.config.predator_present:
                self.render_predator()
            self.render_passives()
            self.render_box()

    def init_shaders(self):
        self.shader_program = None
        self.shader_program = ps.from_string(Shaders.basic_vert_shader, Shaders.basic_frag_shader)
        self.shader_program.use()

        self.shader_program.uniforms.project = Utils.perspective(1, .6*math.pi, 0.1, 100)
        self.shader_program.uniforms.color = (0.8, 0.8, 0.8, 1)

    def render_passives(self):
        scale = Utils.scale(.05, .05, .05)
        self.shader_program.uniforms.color = self.world.config.boid_color
        reset_color = False
        for boid in self.world.boids:
            translate = Utils.translate(boid.pos[0], boid.pos[1], boid.pos[2] - 2)
            quat = Utils.capped_quaternion([0, 1, 0], boid.forward, 1000)
            rots = R.from_quat(quat).as_euler('xyz')
            rotate = Utils.rotate(rots[0], rots[1], rots[2])
            total = Utils.combine_matrices(translate, scale, rotate)
            if boid.id == self.world.the_one.id:
                self.shader_program.uniforms.color = [.1, .6, .1]
                reset_color = True
            if boid.id == self.world.predator.target.agent.id:
                self.shader_program.uniforms.color = [.8, .4, .1]
                reset_color = True
            self.shader_program.uniforms.model = total
            self.boid_model.draw(pyglet.gl.GL_TRIANGLES)
            if reset_color:
                self.shader_program.uniforms.color = self.world.config.boid_color

    def render_predator(self):
        predator = self.world.predator
        scale = Utils.scale(.05, .05, .05)
        translate = Utils.translate(predator.pos[0], predator.pos[1], predator.pos[2] - 2)
        quat = Utils.capped_quaternion([0, 1, 0], predator.forward, 1000)
        rots = R.from_quat(quat).as_euler('xyz')
        rotate = Utils.rotate(rots[0], rots[1], rots[2])
        total = Utils.combine_matrices(translate, scale, rotate)
        self.shader_program.uniforms.model = total
        self.shader_program.uniforms.color = self.world.config.predator_color
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

