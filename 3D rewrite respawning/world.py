from boid import Boid
from predator import Predator
from utils import Utils as U
from agentinfo import AgentInfo
from theone import TheOne
import config

'''
World goes from -1,-1,-1 to 1,1,1
'''


class World:

    def __init__(self):
        self.boids = []
        self.passives = []
        self.agents = []
        self.the_one = None
        self.predator = None
        self.distance_matrix = {}
        # ID 0 is reserved for the predator
        # ID 1 is reserved for The One
        self.next_boid_ID = 2

    def spawn_boids(self, n):
        for x in range(n):
            boid = Boid()
            boid.set_id(self.next_boid_ID)
            self.boids.append(boid)
            self.next_boid_ID += 1
        self.agents += self.boids
        self.passives += self.boids

    def tick(self):
        if self.predator:
            self.predator.move()

        # move all boids
        for boid in self.boids:
            boid.move()

        self.fill_distance_matrix()

    def add_predator(self):
        self.predator = Predator(self)
        self.agents.append(self.predator)

    def add_the_one(self):
        self.the_one = TheOne()
        self.agents.append(self.the_one)
        self.boids.append(self.the_one)

    def eat_boid(self, boid):
        if boid.id == self.the_one.id:
            self.the_one.alive = False
        boid.respawn()

    def fill_distance_matrix(self):
        self.distance_matrix = {}
        n_agents = len(self.agents)
        for x in range(n_agents):
            for y in range(x, n_agents):
                vec = U.wrapping_distance_vector(self.agents[x].pos, self.agents[y].pos)
                min_vec = [-vec[0], -vec[1], -vec[2]]
                dist = U.vec3_magnitude(vec)
                item = AgentInfo(self.agents[y], vec, dist)
                min_item = AgentInfo(self.agents[x], min_vec, dist)
                self.distance_matrix[(self.agents[x].id, self.agents[y].id)] = item
                self.distance_matrix[(self.agents[y].id, self.agents[x].id)] = min_item

    def reset(self):
        self.reset_vars()
        self.spawn_things()

    def spawn_things(self):
        self.add_the_one()
        if config.predator_present:
            self.add_predator()
        self.spawn_boids(config.nr_of_boids)
        self.fill_distance_matrix()

    def reset_vars(self):
        self.boids = []
        self.passives = []
        self.agents = []
        self.the_one = None
        self.predator = None
        self.distance_matrix = {}
        # ID 0 is reserved for the predator
        # ID 1 is reserved for The One
        self.next_boid_ID = 2





