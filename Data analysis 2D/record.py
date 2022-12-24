class Record:

    def __init__(self):
        self.slices = []

    def add_slice(self, tick, boids_eaten, predator, boids):
        self.slices.append(Slice(tick, boids_eaten, predator, boids))


class Slice:

    def __init__(self, tick, boids_eaten, predator, boids):
        self.tick = tick
        self.boids_eaten = boids_eaten
        self.predator_pos = predator.pos
        self.predator_rotation = predator.rotation
        self.boids_pos = []
        self.boids_rotation = []
        for boid in boids:
            self.boids_pos.append(boid.pos)
            self.boids_rotation.append(boid.rotation)
