import pyglet

class Renderer:
    x = 0
    y = 0
    window = None

    def __init__(self, world, w, h):
        self.window = pyglet.window.Window()
        self.label = pyglet.text.Label('Hello, world',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=self.window.width//2, y=self.window.height//2,
                                  anchor_x='center', anchor_y='center')
        self.world = world
        print(self.label.x)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.label.draw()
            self.render_boids()

    def move(self):
        self.label.y += 1

    def render_boids(self):
        coords = []
        for boid in self.world.get_boids():
            coords.append(boid.x)
            coords.append(boid.y)
        print(coords, len(coords))
        pyglet.graphics.draw(int(len(coords)/2), pyglet.gl.GL_POINTS, ("v2i", tuple(coords)))

