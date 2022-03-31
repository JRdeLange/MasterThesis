from boid import Boid
from predator import Predator
from utils import Utils as U
from agentinfo import AgentInfo

'''
World goes from -1,-1,-1 to 1,1,1
'''


class World:

    def __init__(self):
        self.n_boids = 0
        self.boids = []
        self.agents = []
        self.the_one = None
        self.predator = None
        self.distance_matrix = {}
        # ID 0 is reserved for the predator
        # ID 1 is reserved for The One
        self.next_boid_ID = 2

    def spawn_boids(self, n):
        self.n_boids += n
        for x in range(n):
            self.boids.append(Boid(self.next_boid_ID))
            self.next_boid_ID += 1
        self.agents += self.boids

    def tick(self):
        self.fill_distance_matrix()

        if self.predator:
            self.predator.move()

        # move all boids
        for boid in self.boids:
            boid.move()

    def add_predator(self):
        self.predator = Predator(self)
        self.agents.append(self.predator)

    def remove_boid(self, boid):
        self.agents.remove(boid)
        self.boids.remove(boid)

    def fill_distance_matrix(self):
        self.distance_matrix = {}
        print(self.agents)
        n_agents = len(self.agents)
        for x in range(n_agents):
            for y in range(x, n_agents):
                vec = U.wrapping_distance_vector(self.agents[x].pos, self.agents[y].pos)
                min_vec = [-vec[0], -vec[1], -vec[2]]
                dist = U.vec3_magnitude(vec)
                item = AgentInfo(self.agents[y], vec, dist)
                min_item = AgentInfo(self.agents[x], min_vec, dist)
                self.distance_matrix[(self.agents[x].ID, self.agents[y].ID)] = item
                self.distance_matrix[(self.agents[y].ID, self.agents[x].ID)] = min_item
