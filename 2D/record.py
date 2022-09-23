class Record:

    def __init__(self):
        self.episodes = []

    def new_episode(self):
        self.episodes.append(EpisodeRecord())

    def end_episode(self, ticks):
        self.episodes[-1].set_episode_length(ticks)

    def add_episode_slice(self, world):
        # If the latest episode has an episode_length set, it is finished, so we need a new one
        if self.episodes[-1].episode_length is not None:
            self.new_episode()
        episode_slice = EpisodeSlice(world.current_tick, world.predator, world.boids)
        self.episodes[-1].add_episode_slice(episode_slice)

    def boid_eaten(self):
        self.episodes[-1].boid_eaten()


class EpisodeRecord:

    def __init__(self):
        self.episode_slices = []
        self.boids_eaten = 0
        self.episode_length = None

    def add_episode_slice(self, episode_slice):
        episode_slice.set_boids_eaten_so_far(self.boids_eaten)
        self.episode_slices.append(episode_slice)

    def boid_eaten(self):
        self.boids_eaten += 1

    def set_episode_length(self, ticks):
        self.episode_length = ticks


class EpisodeSlice:

    def __init__(self, tick, predator, boids):
        self.tick = tick
        self.predator_pos = predator.pos
        self.predator_rotation = predator.rotation
        self.agents_pos = []
        self.agents_rotation = []
        for boid in boids:
            self.agents_pos.append(boid.pos)
            self.agents_rotation.append(boid.rotation)

        self.boids_eaten_so_far = 0

    def set_boids_eaten_so_far(self, nr_eaten):
        self.boids_eaten_so_far = nr_eaten


