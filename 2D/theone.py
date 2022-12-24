
from boid import Boid


class TheOne(Boid):

    def __init__(self, config):
        super().__init__(config)
        self.id = 1

    def move(self):
        self.pos += self.forward * self.config.boid_speed
        self.wrap()
        #self.history.add(self.pos)




