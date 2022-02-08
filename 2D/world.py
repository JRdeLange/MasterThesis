import random
from boid import Boid


class World:
    secret = "boe"
    boids = []
    dim_x = 100
    dim_y = 100

    def __init__(self):
        boid = Boid()
        self.boids.append(boid)
        pass

    def tick(self):
        for boid in self.boids:
            boid.move()

    def tester(self):
        print(random.random())

    def gen_boid(self):
        boid = Boid()
        self.boids.append(boid)

    def gen_boids(self, n):
        for x in range(n):
            self.gen_boid()

    def get_boids(self):
        return self.boids