import os

class Record:

    def __init__(self):
        self.slices = []

    def add_slice(self, world):
        # If the latest episode has an episode_length set, it is finished, so we need a new one
        episode_slice = Slice(world.overarching_tick, world.predator, world.boids, world.config)
        self.slices.append(episode_slice)

    def boid_eaten(self):
        self.slices[-1].boid_eaten()

    def save_to_file(self, folder, name, config):
        if not os.path.exists("data/" + folder):
            os.mkdir("data/" + folder)
        with open("data/" + folder + "/" + str(name)+".txt", "w") as f:

            # Header with nr of slices, config and data layout
            f.write(str(len(self.slices)) + '\n')
            f.write(str(vars(config)) + '\n')
            f.write("tick\nboids eaten\npredator position\npredator rotation\n")
            f.write("agent positions (and)\nagent rotations (interleaved)\n----\n")

            for slice in self.slices:
                f.write(str(slice.tick) + '\n')
                f.write(str(slice.boids_eaten) + '\n')
                f.write(str(slice.predator_pos[0]) + " " + str(slice.predator_pos[1]) + '\n')
                f.write(str(slice.predator_rotation) + '\n')
                for i in range(len(slice.agents_pos)):
                    f.write(str(slice.agents_pos[i][0]) + " " + str(slice.agents_pos[i][1]) + '\n')
                    f.write(str(slice.agents_rotation[i]) + '\n')
                f.write('---\n')


class Slice:

    def __init__(self, tick, predator, boids, config):
        self.tick = tick
        self.boids_eaten = 0
        self.predator_pos = [None, None]
        self.predator_rotation = None
        if config.predator_present:
            self.predator_pos = predator.pos
            self.predator_rotation = predator.rotation
        self.agents_pos = []
        self.agents_rotation = []
        for boid in boids:
            self.agents_pos.append(boid.pos)
            self.agents_rotation.append(boid.rotation)


    def boid_eaten(self):
        self.boids_eaten += 1


