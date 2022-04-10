import config
from boid import Boid


class TheOne(Boid):

    def __init__(self):
        super().__init__()
        self.id = 1

    def set_heading(self, heading):
        self.heading = heading

    def move(self):
        self.pos += self.forward * config.boid_speed




