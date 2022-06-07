import random
from boid import Boid
from agent import Agent


class World:

    def __init__(self, size):
        self.size = size
        self.n_boids = 0
        self.boids = []
        self.the_one = Agent(self.size)
        self.boids.append(self.the_one)
        pass

    def reset(self):
        self.boids = []
        self.the_one = Agent(self.size)
        self.boids.append(self.the_one)
        self.gen_boids(self.n_boids)

    def tick(self):
        for boid in self.boids:
            boid.move()

    def gen_boid(self):
        boid = Boid(self.size)
        self.boids.append(boid)

    def gen_boids(self, n):
        self.n_boids = n
        for x in range(n):
            self.gen_boid()

    def get_boids(self):
        return self.boids

    def get_nr_of_boids(self):
        return len(self.boids)

    def get_size(self):
        return self.size, self.size
