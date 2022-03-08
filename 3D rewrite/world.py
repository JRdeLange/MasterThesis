from boid import Boid


'''
World goes from -1,-1,-1 to 1,1,1
'''
class World:

    def __init__(self):
        self.n_boids = 0
        self.boids = []
        self.the_one = None

    def spawn_boids(self, n):
        for x in range(n):
            self.boids.append(Boid())

    def tick(self):
        # move all boids
        for boid in self.boids:
            boid.move()