import random
import math
import ratcave as rc
from utils import Utils


class Boid:

    def __init__(self, size):
        self.size = size
        self.x = random.randrange(0, size)
        self.y = random.randrange(0, size)
        self.direction = random.uniform(-math.pi, math.pi)
        self.model = rc.WavefrontReader("boid.obj").get_mesh("Boid")
        self.model.scale = 0.05
        self.model.position.xyz = (random.uniform(-1, 1), random.uniform(-1, 1), -2)

    def move(self):
        self.model.rotation.x += 1
        self.model.rotation.y += 0.4
        self.model.rotation.z += -0.7
        x, y = Utils.radians_to_vec(self.direction)
        self.x += x * 0.5
        self.y += y * 0.5
        self.wrap()

    def wrap(self):
        if self.x > self.size:
            self.x -= self.size
        if self.y > self.size:
            self.y -= self.size
        if self.x < 0:
            self.x += self.size
        if self.y < 0:
            self.y += self.size

