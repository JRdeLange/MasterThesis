import random
from boid import Boid


class World:

    def __init__(self, size):
        self.size = size
        self.boids = []
        pass

    def tick(self):
        for boid in self.boids:
            boid.move()

    def gen_boid(self):
        boid = Boid(self.size)
        self.boids.append(boid)

    def gen_boids(self, n):
        for x in range(n):
            self.gen_boid()

    def get_boids(self):
        return self.boids

    def get_nr_of_boids(self):
        return len(self.boids)

    def get_size(self):
        return self.size, self.size
