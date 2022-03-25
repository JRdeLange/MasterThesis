from boid import Boid
from predator import Predator


'''
World goes from -1,-1,-1 to 1,1,1
'''


class World:

    def __init__(self):
        self.n_boids = 0
        self.boids = []
        self.the_one = None
        self.predator = None
        self.distance_matrix = {}
        # ID 0 is reserved for the predator
        self.next_boid_ID = 1

    def spawn_boids(self, n):
        self.n_boids += n
        for x in range(n):
            self.boids.append(Boid(self.next_boid_ID))
            self.next_boid_ID += 1

    def tick(self):
        # move all boids
        for boid in self.boids:
            boid.move()

        if self.predator:
            self.predator.move()

    def add_predator(self):
        self.predator = Predator(self)

    def fill_distance_matrix(self):
        self.distance_matrix = {}
        pass
