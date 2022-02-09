import pyglet
from utils import Utils
from shaders import Shaders
import ratcave as rc

class Renderer:
    batch = pyglet.graphics.Batch()
    obj_reader = rc.WavefrontReader("boid.obj")
    model = rc.WavefrontReader("boid.obj").get_mesh("Boid")
    model.position.xyz = 0, 0, -2
    print(model.model_matrix)
    model.model_matrix = [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., -2.], [0., 0., 0., 1.]]
    print(model.model_matrix)
    #model.uniforms["model_matrix"] = model.model_matrix#[[1., 0., 0., 0.], [0., 1., 0., -0.425], [0., 0., 1., 0.], [0., 0., 0., 1.]]
    scene = None
    shaders = Shaders()

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window()
        self.world = world
        self.create_scene()

        @self.window.event
        def on_draw():
            self.window.clear()
            #self.render_boids()
            #self.model.rotation.x += 1
            with self.shaders.basic_shader:
                self.scene.draw()

    def create_scene(self):
        meshes = [self.model]
        #for boid in self.world.get_boids():
        #    meshes.append(boid.model)
        print(len(meshes))
        self.scene = rc.Scene(meshes = meshes)


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

